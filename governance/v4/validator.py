#!/usr/bin/env python3
"""Generic, data-driven runtime authorization for FOULWAKE Governance v4."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping

V4_DIR = Path(__file__).resolve().parent
DEFAULT_ROOT = V4_DIR.parents[1]
SHA_RE = re.compile(r"[0-9a-f]{40}")
TASK_ID_RE = re.compile(r"[A-Z0-9][A-Z0-9_-]*")


class GovernanceViolation(ValueError):
    """A stable blocker code with a concise reason."""

    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


def reject(code: str, detail: str) -> None:
    raise GovernanceViolation(code, detail)


def require(condition: bool, code: str, detail: str) -> None:
    if not condition:
        reject(code, detail)


def load_json(path: Path) -> dict[str, Any]:
    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key: {key}")
            result[key] = value
        return result

    try:
        value = json.loads(
            path.read_text(encoding="utf-8"), object_pairs_hook=unique_object
        )
    except Exception as exc:
        reject("INVALID_JSON", f"{path}: {exc}")
    require(isinstance(value, dict), "INVALID_JSON_ROOT", str(path))
    return value


def git(root: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode:
        reject("GIT_ERROR", f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout.strip()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_path(value: str) -> str:
    require(isinstance(value, str), "INVALID_PATH", repr(value))
    path = PurePosixPath(value)
    require(
        not path.is_absolute() and ".." not in path.parts and not value.startswith("./"),
        "INVALID_PATH",
        value,
    )
    normalized = path.as_posix()
    require(normalized not in {"", "."}, "INVALID_PATH", value)
    return normalized


def resolve_governance_ref(root: Path, value: str) -> Path:
    relative = normalize_path(value)
    require(
        relative.startswith("governance/v4/"),
        "CANONICAL_REF_OUTSIDE_V4",
        relative,
    )
    return root / relative


def valid_task_id(value: Any) -> bool:
    return isinstance(value, str) and TASK_ID_RE.fullmatch(value) is not None


def load_task(root: Path, task_id: str) -> dict[str, Any]:
    require(valid_task_id(task_id), "INVALID_TASK_ID", str(task_id))
    task = load_json(root / "governance" / "v4" / "tasks" / f"{task_id}.json")
    require(task.get("task_id") == task_id, "TASK_ID_DRIFT", task_id)
    require(task.get("canonical_task_authority") is True, "TASK_NOT_CANONICAL", task_id)
    return task


def string_list(value: Any, code: str, label: str, allow_empty: bool = False) -> list[str]:
    require(isinstance(value, list), code, f"{label} must be a list")
    require(allow_empty or bool(value), code, f"{label} must not be empty")
    require(all(isinstance(item, str) and item for item in value), code, label)
    require(len(value) == len(set(value)), code, f"{label} contains duplicates")
    return value


def matches_glob(path: str, pattern: str) -> bool:
    if pattern.endswith("/**"):
        prefix = pattern[:-3].rstrip("/")
        return path.startswith(prefix + "/")
    return PurePosixPath(path).match(pattern)


def scope_allows(scope: dict[str, Any], path: str) -> bool:
    normalized = normalize_path(path)
    if normalized in set(scope.get("forbidden_exact_paths", [])):
        return False
    if any(normalized.startswith(prefix) for prefix in scope.get("forbidden_prefixes", [])):
        return False
    exact_paths = set(scope.get("allowed_exact_paths", []))
    globs = scope.get("allowed_globs", [])
    return normalized in exact_paths or any(matches_glob(normalized, pattern) for pattern in globs)


def validate_locked_tree(actual: str, expected: str) -> None:
    require(actual == expected, "V26_TREE_DRIFT", f"expected {expected}, got {actual}")


def validate_exact_copy(
    supplied: dict[str, Any],
    canonical: dict[str, Any],
    fields: Iterable[str],
) -> None:
    differing = sorted(
        field
        for field in fields
        if field not in supplied or supplied.get(field) != canonical.get(field)
    )
    require(not differing, "EXACT_COPY_DRIFT", ", ".join(differing))


def validate_state_document(state: dict[str, Any]) -> None:
    require(str(state.get("schema_version", "")).startswith("4."), "STATE_SCHEMA", "schema_version")
    require(state.get("canonical") is True, "STATE_NOT_CANONICAL", "runtime state")
    require(isinstance(state.get("state_id"), str) and state["state_id"], "STATE_SCHEMA", "state_id")
    require(isinstance(state.get("status"), str) and state["status"], "STATE_SCHEMA", "status")

    source = state.get("source_checkpoint")
    require(isinstance(source, dict), "STATE_SCHEMA", "source_checkpoint")
    require(SHA_RE.fullmatch(str(source.get("commit", ""))) is not None, "STATE_SCHEMA", "source commit")
    require(
        SHA_RE.fullmatch(str(source.get("locked_release_tree_sha", ""))) is not None,
        "STATE_SCHEMA",
        "locked_release_tree_sha",
    )

    active = state.get("active_project_task_id")
    require(active is None or valid_task_id(active), "STATE_SCHEMA", "active_project_task_id")
    candidate = state.get("active_visual_candidate")
    require(candidate is None or isinstance(candidate, str), "STATE_SCHEMA", "active_visual_candidate")

    permissions = state.get("permissions")
    require(isinstance(permissions, dict) and permissions, "STATE_SCHEMA", "permissions")
    require(all(isinstance(value, bool) for value in permissions.values()), "STATE_SCHEMA", "permission values")
    blockers = state.get("open_blockers")
    require(isinstance(blockers, dict), "STATE_SCHEMA", "open_blockers")
    require(
        all(isinstance(key, str) and isinstance(value, str) for key, value in blockers.items()),
        "STATE_SCHEMA",
        "open_blockers values",
    )

    refs = state.get("canonical_refs")
    require(isinstance(refs, dict), "STATE_SCHEMA", "canonical_refs")
    for key in ("contracts", "roles"):
        require(isinstance(refs.get(key), str), "STATE_SCHEMA", f"canonical_refs.{key}")
        normalize_path(refs[key])

    require(
        isinstance(state.get("default_policy"), str) and "DENY" in state["default_policy"],
        "STATE_NOT_FAIL_CLOSED",
        "default_policy",
    )
    if state.get("current_project_authorization") is not None:
        reject("DUPLICATE_RUNTIME_AUTHORITY", "authorization belongs only in active task")

    migration = state.get("migration_control")
    if migration is not None:
        require(isinstance(migration, dict), "STATE_SCHEMA", "migration_control")
        require(isinstance(migration.get("cutover_performed"), bool), "STATE_SCHEMA", "cutover_performed")
        task_id = migration.get("task_id")
        require(task_id is None or valid_task_id(task_id), "STATE_SCHEMA", "migration task_id")


def validate_registry_document(registry: dict[str, Any]) -> None:
    require(str(registry.get("schema_version", "")).startswith("4."), "REGISTRY_SCHEMA", "schema_version")
    require(registry.get("canonical") is True, "REGISTRY_SCHEMA", "canonical")
    require(registry.get("default_policy") == "DENY", "REGISTRY_NOT_FAIL_CLOSED", "default_policy")
    require(registry.get("task_scoped_writes") is True, "REGISTRY_SCHEMA", "task_scoped_writes")
    roles = registry.get("roles")
    require(isinstance(roles, dict) and roles, "REGISTRY_SCHEMA", "roles")
    for role_name, role in roles.items():
        require(isinstance(role_name, str) and isinstance(role, dict), "REGISTRY_SCHEMA", str(role_name))
        string_list(role.get("allowed_actions"), "REGISTRY_SCHEMA", f"{role_name}.allowed_actions")
        require(role.get("writes_require_exact_task") is True, "REGISTRY_SCHEMA", f"{role_name}.writes_require_exact_task")


def validate_contracts_document(contracts: dict[str, Any], registry: dict[str, Any]) -> None:
    require(str(contracts.get("schema_version", "")).startswith("4."), "CONTRACT_SCHEMA", "schema_version")
    require(contracts.get("canonical") is True, "CONTRACT_SCHEMA", "canonical")
    require(
        isinstance(contracts.get("quality_principle"), str) and contracts["quality_principle"],
        "CONTRACT_SCHEMA",
        "quality_principle",
    )
    string_list(contracts.get("protected_quality_gates"), "CONTRACT_SCHEMA", "protected_quality_gates")
    string_list(
        contracts.get("project_owner_required_actions"),
        "CONTRACT_SCHEMA",
        "project_owner_required_actions",
    )

    policy = contracts.get("runtime_authorization")
    require(isinstance(policy, dict), "CONTRACT_SCHEMA", "runtime_authorization")
    for key in (
        "active_task_statuses",
        "cutover_review_statuses",
        "write_actions",
        "self_approval_actions",
        "copy_check_actions",
    ):
        string_list(
            policy.get(key),
            "CONTRACT_SCHEMA",
            f"runtime_authorization.{key}",
            allow_empty=key == "copy_check_actions",
        )
    for key in ("read_only_action", "cutover_action", "cutover_required_role"):
        require(isinstance(policy.get(key), str) and policy[key], "CONTRACT_SCHEMA", key)
    require(
        policy.get("branch_and_path_required_for_non_read_only") is True,
        "CONTRACT_SCHEMA",
        "branch/path binding",
    )
    require(policy.get("request_task_must_equal_active_project_task") is True, "CONTRACT_SCHEMA", "task binding")
    require(policy.get("executor_or_explicit_reviewer_required") is True, "CONTRACT_SCHEMA", "role binding")

    roles = registry["roles"]
    permission_map = policy.get("action_permission_map")
    require(isinstance(permission_map, dict), "CONTRACT_SCHEMA", "action_permission_map")
    registry_actions = {
        action
        for role in roles.values()
        for action in role.get("allowed_actions", [])
    }
    require(
        all(
            isinstance(action, str)
            and action in registry_actions
            and isinstance(permission, str)
            and permission
            for action, permission in permission_map.items()
        ),
        "CONTRACT_SCHEMA",
        "action_permission_map entries",
    )
    require(policy["cutover_required_role"] in roles, "CONTRACT_SCHEMA", "cutover role")
    framing = contracts.get("owner_controls", {}).get("framing", {})
    require(isinstance(framing.get("action"), str), "CONTRACT_SCHEMA", "framing.action")
    require(framing.get("independent_reviewer_role") in roles, "CONTRACT_SCHEMA", "framing reviewer")
    string_list(framing.get("allowed_dispositions"), "CONTRACT_SCHEMA", "framing dispositions")


def validate_task_document(task: dict[str, Any], registry: dict[str, Any]) -> None:
    task_id = task.get("task_id")
    require(valid_task_id(task_id), "TASK_SCHEMA", "task_id")
    require(task.get("canonical_task_authority") is True, "TASK_NOT_CANONICAL", str(task_id))
    require(isinstance(task.get("status"), str) and task["status"], "TASK_SCHEMA", f"{task_id}.status")

    roles = registry["roles"]
    executor = task.get("executor_role")
    require(executor in roles, "TASK_SCHEMA", f"{task_id}.executor_role")
    reviewers = string_list(
        task.get("reviewer_roles", []),
        "TASK_SCHEMA",
        f"{task_id}.reviewer_roles",
        allow_empty=True,
    )
    require(executor not in reviewers, "TASK_SCHEMA", f"{task_id}: executor cannot review itself")
    require(all(role in roles for role in reviewers), "TASK_SCHEMA", f"{task_id}.reviewer_roles")

    authorization = task.get("authorization")
    require(isinstance(authorization, dict), "TASK_SCHEMA", f"{task_id}.authorization")
    require(isinstance(authorization.get("enabled"), bool), "TASK_SCHEMA", f"{task_id}.authorization.enabled")
    require(isinstance(authorization.get("write_authorized"), bool), "TASK_SCHEMA", f"{task_id}.write_authorized")
    allowed = string_list(authorization.get("allowed_actions"), "TASK_SCHEMA", f"{task_id}.allowed_actions")
    role_actions = authorization.get("role_actions")
    require(isinstance(role_actions, dict) and role_actions, "TASK_SCHEMA", f"{task_id}.role_actions")
    participants = {executor, *reviewers}
    assigned: set[str] = set()
    for role, actions in role_actions.items():
        require(role in participants, "TASK_SCHEMA", f"{task_id}: unauthorized role mapping {role}")
        action_list = string_list(actions, "TASK_SCHEMA", f"{task_id}.{role}.actions")
        require(set(action_list) <= set(allowed), "TASK_SCHEMA", f"{task_id}: role action outside task list")
        require(set(action_list) <= set(roles[role]["allowed_actions"]), "TASK_SCHEMA", f"{task_id}: role action outside registry")
        assigned.update(action_list)
    require(assigned == set(allowed), "TASK_SCHEMA", f"{task_id}: unassigned or extra action")

    scope = task.get("scope")
    require(isinstance(scope, dict), "TASK_SCHEMA", f"{task_id}.scope")
    require(isinstance(scope.get("branch"), str) and scope["branch"], "TASK_SCHEMA", f"{task_id}.scope.branch")
    globs = string_list(scope.get("allowed_globs", []), "TASK_SCHEMA", f"{task_id}.allowed_globs", allow_empty=True)
    exact = string_list(scope.get("allowed_exact_paths", []), "TASK_SCHEMA", f"{task_id}.allowed_exact_paths", allow_empty=True)
    require(bool(globs or exact), "TASK_SCHEMA", f"{task_id}: no allowed paths")
    for value in [*exact, *scope.get("forbidden_exact_paths", [])]:
        normalize_path(value)


def validate_runtime_documents(
    state: dict[str, Any],
    tasks: Mapping[str, dict[str, Any]],
    contracts: dict[str, Any],
    registry: dict[str, Any],
) -> None:
    validate_state_document(state)
    validate_registry_document(registry)
    validate_contracts_document(contracts, registry)
    for task_id, task in tasks.items():
        require(task.get("task_id") == task_id, "TASK_ID_DRIFT", task_id)
        validate_task_document(task, registry)

    active_id = state.get("active_project_task_id")
    if active_id is None:
        return
    require(active_id in tasks, "TASK_NOT_FOUND", active_id)
    active = tasks[active_id]
    policy = contracts["runtime_authorization"]
    require(
        active.get("status") in policy["active_task_statuses"],
        "INACTIVE_TASK_REUSE",
        f"{active_id}: {active.get('status')}",
    )
    require(active["authorization"].get("enabled") is True, "TASK_AUTHORIZATION_CLOSED", active_id)


def validate_request_location(task: dict[str, Any], request: dict[str, Any]) -> None:
    scope = task["scope"]
    branch = request.get("branch")
    require(isinstance(branch, str), "BRANCH_REQUIRED", task["task_id"])
    require(branch == scope["branch"], "WRONG_BRANCH", f"expected {scope['branch']}, got {branch}")
    path = request.get("path")
    require(isinstance(path, str), "PATH_REQUIRED", task["task_id"])
    require(scope_allows(scope, path), "OUT_OF_SCOPE_PATH", path)


def bind_task_request(
    task: dict[str, Any],
    registry: dict[str, Any],
    contracts: dict[str, Any],
    request: dict[str, Any],
) -> None:
    role = request["role"]
    action = request["action"]
    participants = {task["executor_role"], *task.get("reviewer_roles", [])}
    require(role in participants, "ROLE_TASK_MISMATCH", f"{role} is not assigned to {task['task_id']}")
    authorization = task["authorization"]
    require(action in authorization["allowed_actions"], "TASK_ACTION_FORBIDDEN", action)
    require(
        action in authorization["role_actions"].get(role, []),
        "TASK_ACTION_FORBIDDEN",
        f"{role}: {action}",
    )
    require(action in registry["roles"][role]["allowed_actions"], "ROLE_ACTION_FORBIDDEN", f"{role}: {action}")
    if action in set(contracts["runtime_authorization"]["write_actions"]):
        require(authorization.get("write_authorized") is True, "TASK_WRITE_CLOSED", task["task_id"])
    validate_request_location(task, request)


def authorize_request(
    state: dict[str, Any],
    tasks: Mapping[str, dict[str, Any]],
    registry: dict[str, Any],
    contracts: dict[str, Any],
    request: dict[str, Any],
    canonical_copy: dict[str, Any] | None = None,
) -> None:
    validate_runtime_documents(state, tasks, contracts, registry)
    role = request.get("role")
    action = request.get("action")
    require(role in registry["roles"], "UNKNOWN_ROLE", str(role))
    require(isinstance(action, str), "INVALID_ACTION", str(action))

    policy = contracts["runtime_authorization"]
    if action == policy["read_only_action"]:
        require(action in registry["roles"][role]["allowed_actions"], "ROLE_ACTION_FORBIDDEN", f"{role}: {action}")
        return

    if action == policy["cutover_action"]:
        migration = state.get("migration_control") or {}
        task_id = request.get("task_id")
        require(task_id == migration.get("task_id"), "MIGRATION_TASK_MISMATCH", str(task_id))
        require(task_id in tasks, "TASK_NOT_FOUND", str(task_id))
        task = tasks[task_id]
        require(
            task.get("status") in policy["cutover_review_statuses"],
            "INACTIVE_TASK_REUSE",
            f"{task_id}: {task.get('status')}",
        )
        require(task["authorization"].get("enabled") is True, "TASK_AUTHORIZATION_CLOSED", task_id)
        require(role == policy["cutover_required_role"], "PROJECT_OWNER_REQUIRED", action)
        require(migration.get("cutover_performed") is False, "CUTOVER_ALREADY_PERFORMED", task_id)
        bind_task_request(task, registry, contracts, request)
        return

    active_id = state.get("active_project_task_id")
    require(active_id is not None, "NO_ACTIVE_TASK_FOR_SPECIALIST_ACTION", action)
    require(
        request.get("task_id") == active_id,
        "ACTIVE_TASK_MISMATCH",
        f"expected {active_id}, got {request.get('task_id')}",
    )
    require(active_id in tasks, "TASK_NOT_FOUND", active_id)
    task = tasks[active_id]
    require(
        task.get("status") in policy["active_task_statuses"],
        "INACTIVE_TASK_REUSE",
        f"{active_id}: {task.get('status')}",
    )
    require(task["authorization"].get("enabled") is True, "TASK_AUTHORIZATION_CLOSED", active_id)

    if action in set(contracts.get("project_owner_required_actions", [])):
        require(role == policy["cutover_required_role"], "PROJECT_OWNER_REQUIRED", action)
    if request.get("producer_role") == role and action in set(policy["self_approval_actions"]):
        reject("SELF_APPROVAL_FORBIDDEN", f"{role}: {action}")

    framing = contracts.get("owner_controls", {}).get("framing", {})
    if action == framing.get("action"):
        require(role == framing.get("independent_reviewer_role"), "FRAMING_REVIEWER_INVALID", str(role))
        require(request.get("producer_role") != role, "SELF_APPROVAL_FORBIDDEN", "framing reviewer is producer")
        require(
            request.get("disposition") in framing.get("allowed_dispositions", []),
            "INVALID_FRAMING_DISPOSITION",
            str(request.get("disposition")),
        )

    bind_task_request(task, registry, contracts, request)

    permission = policy.get("action_permission_map", {}).get(action)
    if permission is not None:
        require(permission in state["permissions"], "STATE_PERMISSION_MISSING", permission)
        require(state["permissions"][permission] is True, "PERMISSION_CLOSED", action)

    if action in set(policy.get("copy_check_actions", [])):
        require(canonical_copy is not None, "CANONICAL_COPY_UNAVAILABLE", action)
        require(isinstance(request.get("copy_record"), dict), "COPY_RECORD_REQUIRED", action)
        copy_contract = contracts.get("owner_controls", {}).get("exact_copy", {})
        fields = [copy_contract.get("identity_field"), *copy_contract.get("visible_fields", [])]
        validate_exact_copy(request["copy_record"], canonical_copy, [field for field in fields if field])

    release = contracts.get("release_and_lock", {})
    if action in set(release.get("actions", [])):
        require(request.get("explicit_owner_decision") is True, "EXPLICIT_OWNER_DECISION_REQUIRED", action)
        require(not state.get("open_blockers"), "OPEN_BLOCKERS", ", ".join(sorted(state["open_blockers"])))
        require(state["permissions"].get(action.lower()) is True, "PERMISSION_CLOSED", action)


def load_repository_bundle(
    root: Path,
    extra_task_ids: Iterable[str] = (),
) -> tuple[dict[str, Any], dict[str, dict[str, Any]], dict[str, Any], dict[str, Any]]:
    state = load_json(root / "governance" / "v4" / "runtime" / "STATE.json")
    validate_state_document(state)
    contracts = load_json(resolve_governance_ref(root, state["canonical_refs"]["contracts"]))
    registry = load_json(resolve_governance_ref(root, state["canonical_refs"]["roles"]))

    task_ids = set(extra_task_ids)
    if state.get("active_project_task_id"):
        task_ids.add(state["active_project_task_id"])
    migration_id = (state.get("migration_control") or {}).get("task_id")
    if migration_id:
        task_ids.add(migration_id)
    tasks = {task_id: load_task(root, task_id) for task_id in task_ids}
    validate_runtime_documents(state, tasks, contracts, registry)
    return state, tasks, contracts, registry


def verify_contract_integrity(root: Path, contracts: dict[str, Any]) -> None:
    owner = contracts.get("owner_controls", {})
    kaptan = owner.get("kaptan", {})
    exact_copy = owner.get("exact_copy", {})
    pins = [
        (kaptan.get("binding_visual_source"), kaptan.get("source_sha256"), kaptan.get("source_git_blob")),
        (exact_copy.get("source"), exact_copy.get("source_sha256"), exact_copy.get("source_git_blob")),
        (kaptan.get("accepted_art_direction_patch"), None, kaptan.get("accepted_patch_blob")),
    ]
    for relative, expected_hash, expected_blob in pins:
        require(isinstance(relative, str), "INTEGRITY_PIN_SCHEMA", str(relative))
        normalized = normalize_path(relative)
        path = root / normalized
        require(path.is_file(), "PINNED_SOURCE_MISSING", normalized)
        if expected_hash is not None:
            require(sha256(path) == expected_hash, "PINNED_SOURCE_HASH_DRIFT", normalized)
        if expected_blob is not None:
            require(git(root, "rev-parse", f"HEAD:{normalized}") == expected_blob, "PINNED_SOURCE_BLOB_DRIFT", normalized)


def validate_repository(root: Path = DEFAULT_ROOT) -> dict[str, Any]:
    root = root.resolve()
    for path in sorted((root / "governance" / "v4").rglob("*.json")):
        load_json(path)
    state, tasks, contracts, _registry = load_repository_bundle(root)

    source = state["source_checkpoint"]
    expected_tree = source["locked_release_tree_sha"]
    validate_locked_tree(git(root, "rev-parse", "HEAD:releases/v2.6"), expected_tree)
    source_commit = source["commit"]
    require(git(root, "cat-file", "-t", source_commit, check=False) == "commit", "SOURCE_COMMIT_UNAVAILABLE", source_commit)
    ancestry = subprocess.run(
        ["git", "merge-base", "--is-ancestor", source_commit, "HEAD"],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(ancestry.returncode == 0, "SOURCE_NOT_ANCESTOR", source_commit)
    verify_contract_integrity(root, contracts)
    return {
        "state_id": state["state_id"],
        "status": state["status"],
        "active_task_id": state.get("active_project_task_id"),
        "locked_release_tree_sha": expected_tree,
        "cutover_performed": (state.get("migration_control") or {}).get("cutover_performed"),
        "loaded_task_ids": sorted(tasks),
    }


def authorize_repository_request(root: Path, request: dict[str, Any]) -> None:
    task_id = request.get("task_id")
    extras = [task_id] if valid_task_id(task_id) else []
    state, tasks, contracts, registry = load_repository_bundle(root.resolve(), extras)
    copy_contract = contracts.get("owner_controls", {}).get("exact_copy", {})
    copy_doc = load_json(root / normalize_path(copy_contract["source"]))
    records = copy_doc.get("records", [])
    require(len(records) == 1, "CANONICAL_COPY_UNAVAILABLE", copy_contract["source"])
    authorize_request(state, tasks, registry, contracts, request, records[0])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--request", type=Path)
    args = parser.parse_args()
    try:
        if args.request:
            authorize_repository_request(args.root.resolve(), load_json(args.request))
            print("FOULWAKE governance v4 request: ALLOW")
            return
        result = validate_repository(args.root)
    except GovernanceViolation as exc:
        print(f"FOULWAKE governance v4: BLOCKED — {exc}", file=sys.stderr)
        raise SystemExit(1)

    print("FOULWAKE governance v4 runtime: PASS")
    print(f"- state: {result['state_id']}")
    print(f"- active project task: {result['active_task_id'] or 'NONE'}")
    print(f"- locked v2.6 tree: {result['locked_release_tree_sha']}")
    print(f"- cutover performed: {str(result['cutover_performed']).upper()}")


if __name__ == "__main__":
    main()
