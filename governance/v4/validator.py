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
SHA256_RE = re.compile(r"[0-9a-f]{64}")
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
    expected_fields = list(fields)
    missing = sorted(set(expected_fields) - set(supplied))
    unexpected = sorted(set(supplied) - set(expected_fields))
    require(
        not missing and not unexpected,
        "COPY_FIELD_SET_MISMATCH",
        f"missing={missing}; unexpected={unexpected}",
    )
    differing = sorted(
        field
        for field in expected_fields
        if supplied.get(field) != canonical.get(field)
    )
    require(not differing, "EXACT_COPY_DRIFT", ", ".join(differing))


def normalized_copy_record(
    record: Any,
    identity_field: str,
    visible_fields: Iterable[str],
    source_label: str,
) -> dict[str, Any]:
    require(isinstance(record, dict), "COPY_RECORD_SCHEMA", source_label)
    fields = [identity_field, *visible_fields]
    require(len(fields) == len(set(fields)), "COPY_RECORD_SCHEMA", f"duplicate field in {source_label}")
    missing = [field for field in fields if field not in record]
    require(not missing, "COPY_RECORD_SCHEMA", f"{source_label}: missing {missing}")
    require(
        all(isinstance(record[field], str) and record[field] for field in fields),
        "COPY_RECORD_SCHEMA",
        source_label,
    )
    return {field: record[field] for field in fields}


def build_canonical_copy_index(
    owner_document: dict[str, Any],
    full_document: dict[str, Any],
    copy_contract: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    identity_field = copy_contract.get("identity_field")
    require(isinstance(identity_field, str) and identity_field, "COPY_CONTRACT_SCHEMA", "identity_field")
    owner_fields = string_list(
        copy_contract.get("visible_fields"),
        "COPY_CONTRACT_SCHEMA",
        "owner override visible_fields",
    )
    owner_records = owner_document.get("records")
    require(isinstance(owner_records, list) and owner_records, "COPY_SOURCE_SCHEMA", "owner records")

    index: dict[str, dict[str, Any]] = {}
    for position, record in enumerate(owner_records):
        normalized = normalized_copy_record(
            record,
            identity_field,
            owner_fields,
            f"owner override record {position}",
        )
        card_id = normalized[identity_field]
        require(card_id not in index, "DUPLICATE_COPY_ID", card_id)
        index[card_id] = normalized

    full_source = copy_contract.get("full_source")
    require(isinstance(full_source, dict), "COPY_CONTRACT_SCHEMA", "full_source")
    collections = full_source.get("collections")
    require(isinstance(collections, dict) and collections, "COPY_CONTRACT_SCHEMA", "collections")
    full_seen: set[str] = set()
    for collection_name, collection_contract in collections.items():
        records = full_document.get(collection_name)
        require(isinstance(records, list), "COPY_SOURCE_SCHEMA", collection_name)
        require(isinstance(collection_contract, dict), "COPY_CONTRACT_SCHEMA", collection_name)
        visible_fields = string_list(
            collection_contract.get("visible_fields"),
            "COPY_CONTRACT_SCHEMA",
            f"{collection_name}.visible_fields",
        )
        for position, record in enumerate(records):
            normalized = normalized_copy_record(
                record,
                identity_field,
                visible_fields,
                f"{collection_name} record {position}",
            )
            card_id = normalized[identity_field]
            require(card_id not in full_seen, "DUPLICATE_COPY_ID", card_id)
            full_seen.add(card_id)
            if card_id not in index:
                index[card_id] = normalized
    return index


def load_canonical_copy_index(
    root: Path,
    contracts: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    copy_contract = contracts.get("owner_controls", {}).get("exact_copy", {})
    owner_document = load_json(root / normalize_path(copy_contract["source"]))
    full_source = copy_contract.get("full_source", {})
    full_document = load_json(root / normalize_path(full_source["source"]))
    return build_canonical_copy_index(owner_document, full_document, copy_contract)


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
        if migration.get("cutover_performed") is True:
            require(
                migration.get("cutover_commit_binding") == "EXPLICIT_CUTOVER_COMMIT",
                "CUTOVER_BINDING_DRIFT",
                str(migration.get("cutover_commit_binding")),
            )
            require(
                SHA_RE.fullmatch(str(migration.get("cutover_commit", ""))) is not None,
                "STATE_SCHEMA",
                "cutover_commit",
            )


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
        "general_production_actions",
    ):
        string_list(
            policy.get(key),
            "CONTRACT_SCHEMA",
            f"runtime_authorization.{key}",
            allow_empty=key == "copy_check_actions",
        )
    for key in ("read_only_action", "cutover_action", "cutover_required_role"):
        require(isinstance(policy.get(key), str) and policy[key], "CONTRACT_SCHEMA", key)
    require(policy["read_only_action"] not in policy["write_actions"], "CONTRACT_SCHEMA", "read-only action classified as write")
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
    granular_actions = policy.get("granular_production_actions")
    require(
        isinstance(granular_actions, dict) and granular_actions,
        "CONTRACT_SCHEMA",
        "granular_production_actions",
    )
    require(
        len(granular_actions.values()) == len(set(granular_actions.values())),
        "CONTRACT_SCHEMA",
        "granular permissions must be one-to-one",
    )
    require(
        all(
            action in registry_actions
            and isinstance(permission, str)
            and permission
            and permission_map.get(action) == permission
            for action, permission in granular_actions.items()
        ),
        "CONTRACT_SCHEMA",
        "granular action permission mapping",
    )
    require(
        not set(policy["general_production_actions"]) & set(granular_actions),
        "CONTRACT_SCHEMA",
        "general and granular production actions overlap",
    )
    require(
        all(action in registry_actions for action in policy["general_production_actions"]),
        "CONTRACT_SCHEMA",
        "general production actions",
    )
    require(
        isinstance(policy.get("production_master_permission"), str)
        and policy["production_master_permission"],
        "CONTRACT_SCHEMA",
        "production_master_permission",
    )

    copy_contract = contracts.get("owner_controls", {}).get("exact_copy", {})
    for key in ("source", "source_sha256", "source_git_blob", "identity_field"):
        require(isinstance(copy_contract.get(key), str) and copy_contract[key], "COPY_CONTRACT_SCHEMA", key)
    require(SHA256_RE.fullmatch(copy_contract["source_sha256"]) is not None, "COPY_CONTRACT_SCHEMA", "source_sha256")
    require(SHA_RE.fullmatch(copy_contract["source_git_blob"]) is not None, "COPY_CONTRACT_SCHEMA", "source_git_blob")
    string_list(copy_contract.get("visible_fields"), "COPY_CONTRACT_SCHEMA", "visible_fields")
    require(
        copy_contract.get("source_precedence") == ["PROJECT_OWNER_OVERRIDE", "FULL_V27_SOURCE"],
        "COPY_PRECEDENCE_INVALID",
        str(copy_contract.get("source_precedence")),
    )
    require(
        isinstance(copy_contract.get("required_identity_decision"), str)
        and copy_contract["required_identity_decision"],
        "COPY_CONTRACT_SCHEMA",
        "required_identity_decision",
    )
    full_source = copy_contract.get("full_source")
    require(isinstance(full_source, dict), "COPY_CONTRACT_SCHEMA", "full_source")
    for key in ("source", "source_sha256", "source_git_blob"):
        require(isinstance(full_source.get(key), str) and full_source[key], "COPY_CONTRACT_SCHEMA", f"full_source.{key}")
    require(SHA256_RE.fullmatch(full_source["source_sha256"]) is not None, "COPY_CONTRACT_SCHEMA", "full_source.source_sha256")
    require(SHA_RE.fullmatch(full_source["source_git_blob"]) is not None, "COPY_CONTRACT_SCHEMA", "full_source.source_git_blob")
    require(isinstance(full_source.get("collections"), dict) and full_source["collections"], "COPY_CONTRACT_SCHEMA", "full_source.collections")
    for collection_name, collection in full_source["collections"].items():
        require(isinstance(collection, dict), "COPY_CONTRACT_SCHEMA", collection_name)
        string_list(collection.get("visible_fields"), "COPY_CONTRACT_SCHEMA", f"{collection_name}.visible_fields")
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
    completed = contracts.get("lifecycle", {}).get("completed_hardening", {})
    if active_id is not None and completed.get("task_reuse_allowed") is False:
        require(active_id != completed.get("task_id"), "INACTIVE_TASK_REUSE", str(active_id))
    if (state.get("migration_control") or {}).get("cutover_performed") is True:
        policy = contracts["runtime_authorization"]
        required_permissions = {
            policy["production_master_permission"],
            *policy["granular_production_actions"].values(),
        }
        missing_permissions = sorted(required_permissions - set(state["permissions"]))
        require(not missing_permissions, "STATE_PERMISSION_MISSING", ", ".join(missing_permissions))
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
    canonical_copies: Mapping[str, dict[str, Any]] | None = None,
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

    control_id = (state.get("coordination_control") or {}).get("task_id")
    if control_id and request.get("task_id") == control_id:
        control = tasks.get(control_id)
        require(control is not None, "TASK_NOT_FOUND", control_id)
        require(role == "CHIEF_EDITOR", "COORDINATION_ROLE_REQUIRED", str(role))
        require(control.get("status") == "ACTIVE_CONTROL" and control["authorization"]["enabled"] is True,
                "COORDINATION_CLOSED", control_id)
        require(action in contracts["lifecycle"]["coordination"]["allowed_actions"], "COORDINATION_ACTION_FORBIDDEN", action)
        if action == "INTEGRATE":
            require(control["authorization"]["write_authorized"] is True, "TASK_WRITE_CLOSED", control_id)
            require(request.get("branch") == control["scope"]["branch"], "WRONG_BRANCH", control_id)
            require(scope_allows(contracts["lifecycle"]["coordination"]["integration_scope"], request.get("path")),
                    "INTEGRATION_PATH_FORBIDDEN", str(request.get("path")))
            return  # Repository entry verifies delivery and independent acceptance.
        bind_task_request(control, registry, contracts, request)
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

    if action in set(policy.get("general_production_actions", [])):
        reject("GRANULAR_ACTION_REQUIRED", action)

    permission = policy.get("action_permission_map", {}).get(action)
    if permission is not None:
        required_permissions = [permission]
        if action in policy.get("granular_production_actions", {}):
            required_permissions.insert(0, policy["production_master_permission"])
        for permission_key in required_permissions:
            require(permission_key in state["permissions"], "STATE_PERMISSION_MISSING", permission_key)
            require(
                state["permissions"][permission_key] is True,
                "PERMISSION_CLOSED",
                f"{action}: {permission_key}",
            )

    if action in set(policy.get("copy_check_actions", [])):
        require(canonical_copies is not None, "CANONICAL_COPY_UNAVAILABLE", action)
        card_id = request.get("card_id")
        require(isinstance(card_id, str) and card_id, "CARD_ID_REQUIRED", action)
        require(card_id in canonical_copies, "UNKNOWN_CARD_ID", card_id)
        require(isinstance(request.get("copy_record"), dict), "COPY_RECORD_REQUIRED", action)
        canonical_copy = canonical_copies[card_id]
        validate_exact_copy(request["copy_record"], canonical_copy, canonical_copy.keys())

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
    control_id = (state.get("coordination_control") or {}).get("task_id")
    if control_id:
        task_ids.add(control_id)
    # Discover real registry entries, including orphan ACTIVE tasks. Fixtures are
    # deliberately outside this directory and never create runtime authority.
    registry_active = []
    for path in sorted((root / "governance/v4/tasks").glob("*.json")):
        record = load_json(path)
        require(record.get("task_id") == path.stem, "TASK_ID_DRIFT", str(path))
        if record.get("status") == "ACTIVE":
            registry_active.append(path.stem)
        if record.get("project_task") is True:
            task_ids.add(path.stem)
        if str(record.get("status", "")).startswith("CLOSED"):
            auth = record.get("authorization", {})
            require(auth.get("enabled") is False and auth.get("write_authorized") is False,
                    "CLOSED_TASK_AUTHORITY_OPEN", path.stem)
            completed = contracts.get("lifecycle", {}).get("completed_hardening", {}).get("task_id")
            if record.get("project_task") is True and path.stem != completed:
                validate_task_closure(root, record)
    expected_active = [state["active_project_task_id"]] if state.get("active_project_task_id") else []
    require(registry_active == expected_active, "TASK_REGISTRY_DRIFT", str(registry_active))
    tasks = {task_id: load_task(root, task_id) for task_id in task_ids}
    validate_runtime_documents(state, tasks, contracts, registry)
    if control_id:
        control = tasks[control_id]
        policy = contracts["lifecycle"]["coordination"]
        require(control.get("project_task") is False and control.get("status") == "ACTIVE_CONTROL",
                "COORDINATION_SCHEMA", control_id)
        binding = state["coordination_control"]
        require(binding.get("role") == "CHIEF_EDITOR" and binding.get("status") == control["status"]
                and binding.get("task_ref") == f"governance/v4/tasks/{control_id}.json", "COORDINATION_BINDING_DRIFT", control_id)
        require(control.get("executor_role") == policy["role"] == "CHIEF_EDITOR"
                and control.get("issued_by") == "PROJECT_OWNER", "COORDINATION_ROLE_REQUIRED", control_id)
        require(control.get("owner_authorization", {}).get("decision") == "AUTHORIZED", "COORDINATION_OWNER_AUTHORIZATION_MISSING", control_id)
        source = control.get("source", {}).get("commit")
        require(SHA_RE.fullmatch(str(source or "")) is not None, "TASK_BASELINE_MISSING", control_id)
        require(subprocess.run(["git", "merge-base", "--is-ancestor", source, "HEAD"], cwd=root,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0,
                "TASK_BASELINE_NOT_ANCESTOR", str(source))
        require(control["scope"].get("binary_files_allowed") is False
                and isinstance(control["scope"].get("max_changed_files"), int), "COORDINATION_SCHEMA", control_id)
        require(control["scope"]["branch"] == policy["branch"], "COORDINATION_BRANCH", control_id)
        require(set(control["authorization"]["allowed_actions"]) <= set(policy["allowed_actions"]),
                "COORDINATION_ACTION_FORBIDDEN", control_id)
        require(control["authorization"]["role_actions"] == {"CHIEF_EDITOR": control["authorization"]["allowed_actions"]},
                "COORDINATION_ROLE_REQUIRED", control_id)
        for path in control["scope"].get("allowed_exact_paths", []) + control["scope"].get("allowed_globs", []):
            require(scope_allows(policy, path), "COORDINATION_PATH_FORBIDDEN", path)
    if not expected_active:
        require(all(value is False for value in state["permissions"].values()),
                "IDLE_PERMISSION_OPEN", "No task can own an enabled permission")
    else:
        validate_live_task(root, tasks[expected_active[0]], state, contracts)
    return state, tasks, contracts, registry


def validate_live_task(root: Path, task: dict[str, Any], state: dict[str, Any], contracts: dict[str, Any]) -> None:
    """Validate actual registry records; synthetic scenario tests use document validation."""
    task_id = task["task_id"]
    require(not task.get("completion"), "ACTIVE_BUT_CLOSED_TASK", task_id)
    require(task.get("project_task") is True, "TASK_NOT_PROJECT_TASK", task_id)
    approval = task.get("owner_authorization", {})
    if task.get("issued_by") == "CHIEF_EDITOR":
        delegation = contracts["lifecycle"].get("task_issuance_delegation", {})
        require(delegation.get("authorized_by") == "PROJECT_OWNER"
                and approval.get("delegation_id") == delegation.get("id"), "TASK_DELEGATION_MISSING", task_id)
        require(set(task["authorization"]["allowed_actions"]) <= set(delegation.get("allowed_actions", [])),
                "TASK_DELEGATION_ACTION_FORBIDDEN", task_id)
        enabled = {key for key, value in task.get("runtime_permissions", {}).items() if value}
        require(enabled <= set(delegation.get("allowed_permissions", [])), "TASK_DELEGATION_PERMISSION_FORBIDDEN", task_id)
    else:
        require(task.get("issued_by") == "PROJECT_OWNER", "PROJECT_OWNER_REQUIRED", task_id)
    require(approval.get("task_id") == task_id and approval.get("decision") == "AUTHORIZED"
            and approval.get("recorded_from"), "TASK_OWNER_AUTHORIZATION_MISSING", task_id)
    source = task.get("source", {})
    baseline = source.get("commit")
    require(SHA_RE.fullmatch(str(baseline or "")) is not None, "TASK_BASELINE_MISSING", task_id)
    require(subprocess.run(["git", "merge-base", "--is-ancestor", baseline, "HEAD"], cwd=root,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0,
            "TASK_BASELINE_NOT_ANCESTOR", str(baseline))
    string_list(task.get("acceptance_criteria"), "TASK_ACCEPTANCE_MISSING", task_id)
    scope = task["scope"]
    require(isinstance(scope.get("max_changed_files"), int) and scope["max_changed_files"] > 0,
            "TASK_SCOPE_LIMIT_MISSING", task_id)
    string_list(scope.get("allowed_extensions"), "TASK_SCOPE_LIMIT_MISSING", task_id)
    require(isinstance(scope.get("binary_files_allowed"), bool), "TASK_SCOPE_LIMIT_MISSING", task_id)
    boundary = contracts["lifecycle"]["role_boundaries"].get(task["executor_role"])
    require(isinstance(boundary, dict), "ROLE_BOUNDARY_MISSING", task["executor_role"])
    require(scope["branch"] == boundary["branch"], "ROLE_BRANCH_MISMATCH", task_id)
    for path in scope.get("allowed_exact_paths", []) + scope.get("allowed_globs", []):
        require(scope_allows(boundary, path), "ROLE_PATH_MISMATCH", path)
    granted = task.get("runtime_permissions")
    require(isinstance(granted, dict) and granted == state["permissions"], "TASK_PERMISSION_DRIFT", task_id)
    actions = task["authorization"]["allowed_actions"]
    policy = contracts["runtime_authorization"]
    permission_actions = {**policy["action_permission_map"], **policy["granular_production_actions"]}
    for permission, enabled in granted.items():
        if not enabled:
            continue
        require(task["authorization"]["write_authorized"] is True, "TASK_WRITE_CLOSED", task_id)
        permitted = any(permission_actions.get(action) == permission for action in actions)
        if permission == policy["production_master_permission"]:
            permitted = any(action in policy["granular_production_actions"] for action in actions)
        require(permitted, "UNOWNED_PERMISSION", permission)
    inputs = task.get("inputs")
    require(isinstance(inputs, list) and inputs, "TASK_INPUTS_MISSING", task_id)
    for pin in inputs:
        require(isinstance(pin, dict) and isinstance(pin.get("path"), str)
                and SHA_RE.fullmatch(str(pin.get("git_blob", ""))) is not None, "TASK_INPUT_SCHEMA", task_id)
        relative = normalize_path(pin["path"])
        require(git(root, "rev-parse", f"{baseline}:{relative}") == pin["git_blob"], "TASK_INPUT_BASELINE_DRIFT", relative)
        require(git(root, "hash-object", relative) == pin.get("git_blob"), "TASK_INPUT_DRIFT", relative)


def validate_task_closure(root: Path, task: dict[str, Any]) -> None:
    completion = task.get("completion", {})
    require(isinstance(completion, dict), "TASK_CLOSURE_MISSING", task["task_id"])
    reviewer = completion.get("accepted_by")
    require(reviewer in task.get("reviewer_roles", []) and reviewer != task.get("executor_role"),
            "INDEPENDENT_ACCEPTANCE_MISSING", task["task_id"])
    delivery = completion.get("delivery_commit")
    require(SHA_RE.fullmatch(str(delivery or "")) is not None, "DELIVERY_COMMIT_MISSING", task["task_id"])
    require(subprocess.run(["git", "merge-base", "--is-ancestor", delivery, "HEAD"], cwd=root,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0,
            "DELIVERY_NOT_ANCESTOR", str(delivery))
    evidence = completion.get("accepted_blobs", {})
    require(isinstance(evidence, dict) and evidence, "ACCEPTANCE_EVIDENCE_MISSING", task["task_id"])
    required_outputs = task.get("required_outputs", task["scope"].get("allowed_exact_paths", []))
    require(set(evidence) == set(required_outputs), "ACCEPTANCE_OUTPUT_SET_DRIFT", task["task_id"])
    for relative, blob in evidence.items():
        require(scope_allows(task["scope"], relative), "OUT_OF_SCOPE_PATH", relative)
        require(git(root, "rev-parse", f"{delivery}:{relative}") == blob
                and git(root, "hash-object", relative) == blob, "ACCEPTED_ARTIFACT_DRIFT", relative)


def validate_task_opening(root: Path, before_commit: str, actor: str) -> dict[str, Any]:
    """Read-only gate for an owner-issued idle -> ACTIVE repository change."""
    require(actor == "CHIEF_EDITOR", "TASK_ISSUER_ROLE", str(actor))
    require(SHA_RE.fullmatch(str(before_commit)) is not None, "TASK_BASELINE_MISSING", str(before_commit))
    require(git(root, "rev-parse", "HEAD") == before_commit, "STALE_TASK_OPENING_BASELINE", before_commit)
    before = json.loads(git(root, "show", f"{before_commit}:governance/v4/runtime/STATE.json"))
    require(before.get("active_project_task_id") is None and all(v is False for v in before["permissions"].values()),
            "TASK_OPENING_REQUIRES_IDLE", before_commit)
    result = validate_repository(root)
    state, tasks, contracts, registry = load_repository_bundle(root)
    task_id = state.get("active_project_task_id")
    require(task_id in tasks, "TASK_NOT_FOUND", str(task_id))
    task_path = f"governance/v4/tasks/{task_id}.json"
    exists = subprocess.run(["git", "cat-file", "-e", f"{before_commit}:{task_path}"], cwd=root,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    require(exists.returncode != 0, "INACTIVE_TASK_REUSE", str(task_id))
    require(tasks[task_id]["source"]["commit"] == before_commit, "TASK_BASELINE_DRIFT", task_id)
    require(git(root, "branch", "--show-current") in {"", tasks[task_id]["source"].get("branch")},
            "TASK_OPENING_BRANCH_MISMATCH", task_id)
    mutable = {"state_id", "status", "updated_at", "active_project_task_id", "permissions", "workstreams", "next_action"}
    require({k: v for k, v in state.items() if k not in mutable} ==
            {k: v for k, v in before.items() if k not in mutable}, "TASK_OPENING_STATE_SCOPE", task_id)
    for workstream, previous in before.get("workstreams", {}).items():
        current = state.get("workstreams", {}).get(workstream)
        if previous.get("branch") == tasks[task_id]["scope"]["branch"]:
            require(isinstance(current, dict) and current.get("branch") == previous["branch"],
                    "TASK_OPENING_WORKSTREAM_DRIFT", workstream)
        else:
            require(current == previous, "TASK_OPENING_WORKSTREAM_DRIFT", workstream)
    changed = set(git(root, "diff", "--name-only", before_commit).splitlines())
    changed.update(git(root, "ls-files", "--others", "--exclude-standard").splitlines())
    allowed = {task_path, "governance/v4/runtime/STATE.json", "governance/v4/tests/fixtures/RUNTIME_SCENARIOS.json"}
    require(changed <= allowed, "TASK_OPENING_PATH_SCOPE", str(sorted(changed - allowed)))
    return result


def committed_coordination_integrations(root: Path, task: dict[str, Any]) -> set[str]:
    """Separate immutable accepted deliveries from the coordinator's own writes."""
    state = load_json(root / "governance/v4/runtime/STATE.json")
    if task["task_id"] != state.get("coordination_control", {}).get("task_id"):
        return set()
    accepted_paths: set[str] = set()
    for path in sorted((root / "governance/v4/evidence").glob("*.json")):
        relative = path.relative_to(root).as_posix()
        committed = git(root, "rev-parse", f"HEAD:{relative}", check=False)
        # Pending acceptance cannot exempt a pending specialist content write.
        if not SHA_RE.fullmatch(committed) or git(root, "hash-object", relative) != committed:
            continue
        accepted = load_json(path)
        if accepted.get("status") != "ACCEPTED":
            continue
        delivered_task = load_task(root, accepted.get("task_id"))
        require(delivered_task.get("project_task") is True, "TASK_NOT_PROJECT_TASK", relative)
        completion = {"accepted_by": accepted.get("reviewer_role"),
                      "delivery_commit": accepted.get("delivery_commit"),
                      "accepted_blobs": accepted.get("accepted_blobs")}
        validate_task_closure(root, {**delivered_task, "completion": completion})
        for output, blob in completion["accepted_blobs"].items():
            require(git(root, "rev-parse", f"HEAD:{output}", check=False) == blob,
                    "INTEGRATION_NOT_COMMITTED", output)
            accepted_paths.add(output)
    return accepted_paths


def validate_execution_scope(root: Path, task: dict[str, Any], request: dict[str, Any]) -> None:
    """Check cumulative Git changes, worktree changes and the real checkout branch."""
    require(git(root, "branch", "--show-current") == request.get("branch"),
            "CHECKOUT_BRANCH_MISMATCH", str(request.get("branch")))
    task_path = f"governance/v4/tasks/{task['task_id']}.json"
    commits = git(root, "log", "--diff-filter=A", "--format=%H", "HEAD", "--", task_path).splitlines()
    require(len(commits) == 1, "TASK_ACTIVATION_COMMIT_MISSING", task['task_id'])
    activation = commits[0]
    require(git(root, "hash-object", task_path) == git(root, "rev-parse", f"{activation}:{task_path}"),
            "ACTIVE_TASK_MODIFIED", task['task_id'])
    paths = set(git(root, "diff", "--name-only", activation).splitlines())
    paths.update(git(root, "ls-files", "--others", "--exclude-standard").splitlines())
    paths.difference_update(committed_coordination_integrations(root, task))
    # Even an accepted output cannot become a direct coordinator WRITE target.
    paths.add(normalize_path(request["path"]))
    scope = task["scope"]
    require(len(paths) <= scope["max_changed_files"], "TASK_FILE_COUNT_EXCEEDED", str(len(paths)))
    for relative in paths:
        require(scope_allows(scope, relative), "OUT_OF_SCOPE_PATH", relative)
        path = root / relative
        require(path.suffix in scope["allowed_extensions"], "TASK_FILE_TYPE_FORBIDDEN", relative)
        require(not path.is_symlink() and path.resolve().is_relative_to(root.resolve()), "INVALID_PATH", relative)
        if path.is_file() and scope["binary_files_allowed"] is False:
            try:
                text = path.read_bytes().decode("utf-8")
            except UnicodeDecodeError:
                reject("TASK_BINARY_FORBIDDEN", relative)
            require("\x00" not in text, "TASK_BINARY_FORBIDDEN", relative)


def verify_contract_integrity(root: Path, contracts: dict[str, Any]) -> None:
    owner = contracts.get("owner_controls", {})
    kaptan = owner.get("kaptan", {})
    exact_copy = owner.get("exact_copy", {})
    pins = [
        (kaptan.get("binding_visual_source"), kaptan.get("source_sha256"), kaptan.get("source_git_blob")),
        (exact_copy.get("source"), exact_copy.get("source_sha256"), exact_copy.get("source_git_blob")),
        (
            exact_copy.get("full_source", {}).get("source"),
            exact_copy.get("full_source", {}).get("source_sha256"),
            exact_copy.get("full_source", {}).get("source_git_blob"),
        ),
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


def verify_resolved_source_decision(
    state: dict[str, Any],
    contracts: dict[str, Any],
    canonical_copies: Mapping[str, dict[str, Any]],
) -> None:
    copy_contract = contracts["owner_controls"]["exact_copy"]
    decision_id = copy_contract["required_identity_decision"]
    decisions = state.get("resolved_source_decisions")
    require(isinstance(decisions, dict), "SOURCE_DECISION_MISSING", decision_id)
    require(decision_id in decisions, "SOURCE_DECISION_MISSING", decision_id)
    decision = decisions[decision_id]
    require(isinstance(decision, dict), "SOURCE_DECISION_SCHEMA", decision_id)
    require(
        decision.get("status") == "RESOLVED / PROJECT_OWNER_BINDING_CANON",
        "SOURCE_DECISION_UNRESOLVED",
        decision_id,
    )
    require(decision_id not in state.get("open_blockers", {}), "RESOLVED_BLOCKER_STILL_OPEN", decision_id)
    full_source = copy_contract["full_source"]
    require(decision.get("source") == full_source["source"], "SOURCE_DECISION_DRIFT", decision_id)
    require(decision.get("source_git_blob") == full_source["source_git_blob"], "SOURCE_DECISION_DRIFT", decision_id)
    identity_field = decision.get("identity_field")
    require(isinstance(identity_field, str) and identity_field, "SOURCE_DECISION_SCHEMA", "identity_field")
    mapping = decision.get("mapping")
    require(isinstance(mapping, dict) and mapping, "SOURCE_DECISION_SCHEMA", "mapping")
    for card_id, identity in mapping.items():
        require(card_id in canonical_copies, "SOURCE_DECISION_UNKNOWN_ID", str(card_id))
        canonical = canonical_copies[card_id]
        require(identity_field in canonical, "SOURCE_DECISION_FIELD_MISSING", f"{card_id}: {identity_field}")
        require(canonical[identity_field] == identity, "SOURCE_DECISION_MAPPING_DRIFT", card_id)


def verify_hardening_closure(
    root: Path,
    state: dict[str, Any],
    contracts: dict[str, Any],
    registry: dict[str, Any],
) -> None:
    # Closure is an immutable historical fact, not a freeze on future live tasks.
    completed = contracts.get("lifecycle", {}).get("completed_hardening")
    require(isinstance(completed, dict), "HARDENING_CONTROL_SCHEMA", "completed_hardening")
    snapshot_commit = completed.get("snapshot_commit")
    require(SHA_RE.fullmatch(str(snapshot_commit or "")) is not None, "HARDENING_CONTROL_SCHEMA", "snapshot_commit")
    require(completed.get("task_reuse_allowed") is False, "HARDENING_CONTROL_SCHEMA", "task_reuse_allowed")
    ancestry = subprocess.run(
        ["git", "merge-base", "--is-ancestor", snapshot_commit, "HEAD"],
        cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    require(ancestry.returncode == 0, "HARDENING_SNAPSHOT_NOT_ANCESTOR", snapshot_commit)
    state_ref = completed.get("state_ref")
    require(isinstance(state_ref, str), "HARDENING_CONTROL_SCHEMA", "state_ref")
    resolve_governance_ref(root, state_ref)
    snapshot = json.loads(git(root, "show", f"{snapshot_commit}:{state_ref}"))
    validate_state_document(snapshot)
    control = state.get("hardening_control")
    require(isinstance(control, dict), "HARDENING_CONTROL_MISSING", "runtime state")
    task_id = control.get("task_id")
    require(valid_task_id(task_id), "HARDENING_CONTROL_SCHEMA", str(task_id))
    require(task_id == completed.get("task_id"), "HARDENING_CONTROL_SCHEMA", "task_id")
    require(control == snapshot.get("hardening_control"), "HARDENING_CONTROL_SCHEMA", "closure control drift")
    expected_task_ref = f"governance/v4/tasks/{task_id}.json"
    require(control.get("task_ref") == expected_task_ref, "HARDENING_CONTROL_SCHEMA", "task_ref")
    task = load_task(root, task_id)
    validate_task_document(task, registry)
    require(
        task.get("status") == "CLOSED / HARDENING_COMPLETE"
        and control.get("status") == task.get("status"),
        "HARDENING_NOT_CLOSED",
        str(task.get("status")),
    )
    authorization = task["authorization"]
    require(authorization.get("enabled") is False, "HARDENING_AUTHORITY_OPEN", "enabled")
    require(authorization.get("write_authorized") is False, "HARDENING_AUTHORITY_OPEN", "write")
    require(state.get("active_project_task_id") != task_id, "INACTIVE_TASK_REUSE", task_id)
    require(snapshot.get("active_project_task_id") is None, "HARDENING_RUNTIME_NOT_IDLE", snapshot_commit)
    require(all(value is False for value in snapshot["permissions"].values()), "HARDENING_PERMISSION_OPEN", snapshot_commit)

    evidence_ref = control.get("evidence_ref")
    require(isinstance(evidence_ref, str), "HARDENING_CONTROL_SCHEMA", "evidence_ref")
    require(evidence_ref == completed.get("evidence_ref"), "HARDENING_CONTROL_SCHEMA", "evidence_ref")
    for relative in (expected_task_ref, evidence_ref):
        require(
            git(root, "hash-object", relative) == git(root, "rev-parse", f"{snapshot_commit}:{relative}"),
            "HARDENING_SNAPSHOT_DRIFT", relative,
        )
    evidence = load_json(resolve_governance_ref(root, evidence_ref))
    require(evidence.get("canonical_authority") is False, "HARDENING_EVIDENCE_AUTHORITY", evidence_ref)
    require(evidence.get("task", {}).get("task_id") == task_id, "HARDENING_EVIDENCE_DRIFT", "task_id")
    require(evidence.get("task", {}).get("final_status") == task["status"], "HARDENING_EVIDENCE_DRIFT", "status")
    require(evidence.get("result") == snapshot.get("status"), "HARDENING_EVIDENCE_DRIFT", "historical result")
    require(evidence.get("task", {}).get("active_project_task") is None, "HARDENING_EVIDENCE_DRIFT", "historical active task")
    for key in ("authorization_enabled", "write_authorized"):
        require(evidence.get("task", {}).get(key) is False, "HARDENING_EVIDENCE_DRIFT", key)

    source_head = task.get("reactivation", {}).get("source_head")
    require(SHA_RE.fullmatch(str(source_head or "")) is not None, "HARDENING_CONTROL_SCHEMA", "source_head")
    require(evidence.get("source", {}).get("head") == source_head, "HARDENING_EVIDENCE_DRIFT", "source_head")
    before = json.loads(git(root, "show", f"{source_head}:governance/v4/runtime/STATE.json"))
    decision_id = contracts["owner_controls"]["exact_copy"]["required_identity_decision"]
    expected_blockers = dict(before["open_blockers"])
    require(decision_id in expected_blockers, "HARDENING_SOURCE_DRIFT", decision_id)
    expected_blockers.pop(decision_id)
    require(snapshot["open_blockers"] == expected_blockers, "HARDENING_BLOCKER_SCOPE", decision_id)
    require(decision_id not in state["open_blockers"], "RESOLVED_BLOCKER_STILL_OPEN", decision_id)
    decision = snapshot["resolved_source_decisions"][decision_id]
    require(state.get("resolved_source_decisions", {}).get(decision_id) == decision, "SOURCE_DECISION_DRIFT", decision_id)
    for key in ("status", "source", "source_git_blob", "mapping"):
        require(evidence.get("src_002", {}).get(key) == decision[key], "HARDENING_EVIDENCE_DRIFT", key)
    historical_contract = json.loads(git(root, "show", f"{snapshot_commit}:{snapshot['canonical_refs']['contracts']}"))["owner_controls"]["exact_copy"]
    historical_owner = json.loads(git(root, "show", f"{snapshot_commit}:{historical_contract['source']}"))
    historical_full = json.loads(git(root, "show", f"{snapshot_commit}:{historical_contract['full_source']['source']}"))
    require(
        len(build_canonical_copy_index(historical_owner, historical_full, historical_contract)) == evidence.get("copy_resolver", {}).get("resolved_record_count"),
        "HARDENING_COPY_COUNT_DRIFT", "resolver count",
    )


def validate_repository(root: Path = DEFAULT_ROOT) -> dict[str, Any]:
    root = root.resolve()
    for path in sorted((root / "governance" / "v4").rglob("*.json")):
        load_json(path)
    state, tasks, contracts, registry = load_repository_bundle(root)

    source = state["source_checkpoint"]
    expected_tree = source["locked_release_tree_sha"]
    validate_locked_tree(git(root, "rev-parse", "HEAD:releases/v2.6"), expected_tree)
    require(not git(root, "diff", "--name-only", "HEAD", "--", "releases/v2.6")
            and not git(root, "ls-files", "--others", "--exclude-standard", "--", "releases/v2.6"),
            "LOCKED_WORKTREE_DRIFT", "releases/v2.6")
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
    for relative, expected_blob in contracts.get("protected_content_blobs", {}).items():
        require(git(root, "hash-object", relative) == expected_blob, "CONTENT_SOURCE_DRIFT", relative)
    canonical_copies = load_canonical_copy_index(root, contracts)
    verify_resolved_source_decision(state, contracts, canonical_copies)
    verify_hardening_closure(root, state, contracts, registry)
    migration = state.get("migration_control") or {}
    if migration.get("cutover_performed") is True:
        cutover_commit = migration["cutover_commit"]
        require(git(root, "cat-file", "-t", cutover_commit, check=False) == "commit", "CUTOVER_COMMIT_UNAVAILABLE", cutover_commit)
        cutover_ancestry = subprocess.run(
            ["git", "merge-base", "--is-ancestor", cutover_commit, "HEAD"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        require(cutover_ancestry.returncode == 0, "CUTOVER_COMMIT_NOT_ANCESTOR", cutover_commit)
    return {
        "state_id": state["state_id"],
        "status": state["status"],
        "active_task_id": state.get("active_project_task_id"),
        "locked_release_tree_sha": expected_tree,
        "cutover_performed": (state.get("migration_control") or {}).get("cutover_performed"),
        "loaded_task_ids": sorted(tasks),
        "canonical_copy_records": len(canonical_copies),
    }


def authorize_repository_request(root: Path, request: dict[str, Any]) -> None:
    root = root.resolve()
    if request.get("action") == "OPEN_TASK" and request.get("baseline_commit"):
        result = validate_task_opening(root, request.get("baseline_commit", ""), request.get("role"))
        require(request.get("task_id") == result["active_task_id"], "ACTIVE_TASK_MISMATCH", str(request.get("task_id")))
        return
    validate_repository(root)
    task_id = request.get("task_id")
    extras = [task_id] if valid_task_id(task_id) else []
    state, tasks, contracts, registry = load_repository_bundle(root.resolve(), extras)
    canonical_copies = load_canonical_copy_index(root, contracts)
    authorize_request(state, tasks, registry, contracts, request, canonical_copies)
    if request.get("action") == "INTEGRATE" and task_id == (state.get("coordination_control") or {}).get("task_id"):
        validate_integration_request(root, state, tasks, request)
        return
    if request.get("action") != contracts["runtime_authorization"]["read_only_action"]:
        task = tasks[task_id]
        validate_execution_scope(root, task, request)
        if request.get("action") == "PRODUCE_FULL_121":
            require(len(canonical_copies) == contracts["owner_controls"]["exact_copy"]["expected_full_deck_records"],
                    "COPY_COVERAGE_INCOMPLETE", str(len(canonical_copies)))


def validate_integration_request(root: Path, state: dict[str, Any], tasks: dict[str, Any], request: dict[str, Any]) -> None:
    """Chief Editor may copy reviewed specialist bytes, never author them through integration."""
    from ci import validate_branch
    require(git(root, "branch", "--show-current") == request["branch"], "CHECKOUT_BRANCH_MISMATCH", request["branch"])
    active = tasks.get(state.get("active_project_task_id"))
    require(active is not None, "INTEGRATION_NO_ACTIVE_TASK", str(state.get("active_project_task_id")))
    path = request["path"]
    require(scope_allows(active["scope"], path), "INTEGRATION_PATH_FORBIDDEN", path)
    ref = request.get("acceptance_ref")
    require(isinstance(ref, str) and ref.startswith("governance/v4/evidence/"), "INTEGRATION_ACCEPTANCE_MISSING", str(ref))
    accepted = load_json(resolve_governance_ref(root, ref))
    require(accepted.get("task_id") == active["task_id"] and accepted.get("status") == "ACCEPTED",
            "INTEGRATION_ACCEPTANCE_MISMATCH", ref)
    reviewer = accepted.get("reviewer_role")
    require(reviewer in active.get("reviewer_roles", []) and reviewer != active["executor_role"],
            "INDEPENDENT_ACCEPTANCE_MISSING", ref)
    delivery = accepted.get("delivery_commit")
    require(SHA_RE.fullmatch(str(delivery or "")) is not None, "DELIVERY_COMMIT_MISSING", ref)
    branch = active["scope"]["branch"]
    require(git(root, "rev-parse", f"refs/remotes/origin/{branch}") == delivery, "INTEGRATION_STALE_DELIVERY", branch)
    validate_branch(root, "HEAD", branch, delivery)
    blobs = accepted.get("accepted_blobs", {})
    require(path in blobs and git(root, "rev-parse", f"{delivery}:{path}") == blobs[path], "INTEGRATION_BLOB_DRIFT", path)
    # Any pending content write must already equal an accepted delivery blob.
    pending = set(git(root, "diff", "--name-only", "HEAD", "--", "working/").splitlines())
    pending.update(git(root, "ls-files", "--others", "--exclude-standard", "--", "working/").splitlines())
    control = tasks[state["coordination_control"]["task_id"]]
    for changed in pending:
        if scope_allows(control["scope"], changed):
            continue
        require(changed in blobs and git(root, "hash-object", changed) == blobs[changed]
                and git(root, "rev-parse", f"{delivery}:{changed}") == blobs[changed], "INTEGRATION_CONTENT_EDIT", changed)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--request", type=Path)
    parser.add_argument("--open-task-from", help="Validate a proposed idle -> ACTIVE change against this exact HEAD")
    parser.add_argument("--role", help="Role performing the proposed lifecycle transition")
    args = parser.parse_args()
    try:
        if args.open_task_from:
            result = validate_task_opening(args.root.resolve(), args.open_task_from, args.role)
            print(f"FOULWAKE governance v4 task opening: PASS — {result['active_task_id']}")
            return
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
