#!/usr/bin/env python3
"""Task-independent, fail-closed validation for FOULWAKE Governance v4."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

V4_DIR = Path(__file__).resolve().parent
DEFAULT_ROOT = V4_DIR.parents[1]
EXPECTED_SOURCE = "5564c7fbdea297ab1b8b3fa675c83f6e788151f1"
EXPECTED_V26_TREE = "efb41c46f06174c42dcdab2859b7c0ba517f86f0"
EXPECTED_BRANCH = "migration/governance-v4"
QUALITY_PRINCIPLE = (
    "LEAN GOVERNANCE SHALL REDUCE CONTEXT AND CEREMONY, NEVER REVIEW DEPTH, "
    "CREATIVE SCRUTINY, EVIDENCE QUALITY OR PROJECT OWNER CONTROL."
)
EXPECTED_BLOCKERS = {
    "ART-001", "SRC-002", "MEC-001", "QA-001", "QA-002",
    "GOV-001", "GOV-002", "PHYSICAL-PROOF",
}
EXPECTED_ROLES = {
    "PROJECT_OWNER", "CHIEF_EDITOR", "STORY_EDITOR", "VISUAL_DESIGN",
    "ART_DIRECTION", "SIMULATION_QA",
}
EXPECTED_GATES = {
    "V2_6_IMMUTABILITY",
    "CANONICAL_SOURCE_HIERARCHY",
    "EXACT_COPY",
    "KAPTAN_OWNER_CONTRACT",
    "INDEPENDENT_ART_DIRECTION",
    "FRAMING_PASS_OR_REFRAME_REQUIRED",
    "SEMANTIC_VISUAL_FIT",
    "COMPOSITION_AND_ANATOMY_OBJECT_INTEGRITY",
    "ORIGINALITY_AND_DECK_REPETITION",
    "PERIOD_FIT",
    "BACK_SECRECY_AND_TOPOLOGY",
    "PROJECT_OWNER_AESTHETIC_ACCEPTANCE",
    "FULL_DECK_COHESION_REVIEW",
    "INDEPENDENT_SIMULATION_QA",
    "PHYSICAL_PRINT_DUPLEX_TABLE_EVIDENCE",
    "EXPLICIT_PROJECT_OWNER_RELEASE_AND_LOCK",
}
OWNER_REQUIRED_ACTIONS = {
    "CANON_DECISION",
    "PROJECT_OWNER_AESTHETIC_ACCEPTANCE",
    "MECHANIC_OR_PLAYER_EXPERIENCE_DECISION",
    "EXPENSIVE_OR_IRREVERSIBLE_PRODUCTION_DECISION",
    "CUTOVER_DECISION",
    "RELEASE",
    "LOCK",
}
WRITE_ACTIONS = {
    "WRITE", "OPEN_TASK", "INTEGRATE", "MANAGE_STATE",
    "PRODUCE_STORY", "PRODUCE_FLAVOR", "PRODUCE_VISUAL",
    "PRODUCE_LAYOUT",
}


class GovernanceViolation(ValueError):
    """A stable blocker code with a concise reason."""

    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


def reject(code: str, detail: str) -> None:
    raise GovernanceViolation(code, detail)


def load_json(path: Path) -> dict[str, Any]:
    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        value: dict[str, Any] = {}
        for key, item in pairs:
            if key in value:
                raise ValueError(f"duplicate key: {key}")
            value[key] = item
        return value

    try:
        value = json.loads(
            path.read_text(encoding="utf-8"), object_pairs_hook=unique_object
        )
    except Exception as exc:  # fail closed with the original parse reason
        reject("INVALID_JSON", f"{path}: {exc}")
    if not isinstance(value, dict):
        reject("INVALID_JSON_ROOT", f"{path} must contain a JSON object")
    return value


def load_task(root: Path, task_id: str) -> dict[str, Any]:
    if not task_id or any(char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for char in task_id):
        reject("INVALID_TASK_ID", str(task_id))
    task = load_json(root / "governance" / "v4" / "tasks" / f"{task_id}.json")
    if task.get("task_id") != task_id:
        reject("TASK_ID_DRIFT", f"requested {task_id}, record has {task.get('task_id')}")
    if task.get("canonical_task_authority") is not True:
        reject("TASK_NOT_CANONICAL", task_id)
    return task


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def normalize_path(value: str) -> str:
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or value.startswith("./"):
        reject("INVALID_PATH", value)
    normalized = path.as_posix()
    if normalized in {"", "."}:
        reject("INVALID_PATH", value)
    return normalized


def matches_glob(path: str, pattern: str) -> bool:
    if pattern.endswith("/**"):
        prefix = pattern[:-3].rstrip("/")
        return path.startswith(prefix + "/")
    return PurePosixPath(path).match(pattern)


def validate_locked_tree(actual: str, expected: str = EXPECTED_V26_TREE) -> None:
    if actual != expected:
        reject("V26_TREE_DRIFT", f"expected {expected}, got {actual}")


def audit_delivery_scope(
    task: dict[str, Any],
    branch: str,
    changed_paths: Iterable[str],
    binary_paths: Iterable[str] = (),
) -> None:
    scope = task.get("delivery_scope", {})
    if branch != scope.get("branch"):
        reject("WRONG_BRANCH", f"expected {scope.get('branch')}, got {branch}")

    paths = [normalize_path(item) for item in changed_paths]
    if len(paths) != len(set(paths)):
        reject("DUPLICATE_CHANGED_PATH", "changed path list contains duplicates")

    forbidden_exact = set(scope.get("forbidden_exact_paths", []))
    forbidden_prefixes = tuple(scope.get("forbidden_prefixes", []))
    for path in paths:
        if path in forbidden_exact or path.startswith(forbidden_prefixes):
            reject("OUT_OF_SCOPE_PATH", path)
        if not any(matches_glob(path, pattern) for pattern in scope.get("allowed_globs", [])):
            reject("OUT_OF_SCOPE_PATH", path)

    expected = set(scope.get("expected_paths", []))
    if expected and set(paths) != expected:
        missing = sorted(expected - set(paths))
        extra = sorted(set(paths) - expected)
        reject("SCOPE_PATH_SET_DRIFT", f"missing={missing}; extra={extra}")

    maximum = scope.get("max_changed_files")
    if not isinstance(maximum, int) or len(paths) > maximum:
        reject("CHANGED_FILE_BUDGET", f"{len(paths)} > {maximum}")

    allowed_extensions = set(scope.get("allowed_extensions", []))
    wrong_type = [path for path in paths if PurePosixPath(path).suffix not in allowed_extensions]
    if wrong_type:
        reject("DISALLOWED_FILE_TYPE", ", ".join(wrong_type))

    binary = sorted(set(binary_paths))
    if binary and not scope.get("binary_files_allowed", False):
        reject("BINARY_CHANGE_FORBIDDEN", ", ".join(binary))


def validate_exact_copy(
    supplied: dict[str, Any],
    canonical: dict[str, Any],
    fields: Iterable[str] | None = None,
) -> None:
    compared_fields = set(fields) if fields is not None else set(supplied) | set(canonical)
    differing = sorted(
        key for key in compared_fields
        if key not in supplied or supplied.get(key) != canonical.get(key)
    )
    if differing:
        reject("EXACT_COPY_DRIFT", ", ".join(differing) or "record differs")


def authorize_request(
    state: dict[str, Any],
    task: dict[str, Any],
    registry: dict[str, Any],
    contracts: dict[str, Any],
    request: dict[str, Any],
    canonical_copy: dict[str, Any] | None = None,
) -> None:
    role = request.get("role")
    action = request.get("action")
    roles = registry.get("roles", {})
    if role not in roles:
        reject("UNKNOWN_ROLE", str(role))
    if not isinstance(action, str):
        reject("INVALID_ACTION", "action must be a string")

    owner_required = set(contracts.get("project_owner_required_actions", []))
    if action in owner_required and role != "PROJECT_OWNER":
        reject("PROJECT_OWNER_REQUIRED", action)

    if action == "FRAMING_DECISION":
        framing = contracts.get("owner_controls", {}).get("framing", {})
        if role != framing.get("independent_reviewer_role"):
            reject("FRAMING_REVIEWER_INVALID", str(role))
        if request.get("producer_role") == role:
            reject("SELF_APPROVAL_FORBIDDEN", "framing reviewer is the producer")
        if request.get("disposition") not in framing.get("allowed_dispositions", []):
            reject("INVALID_FRAMING_DISPOSITION", str(request.get("disposition")))

    if (
        request.get("producer_role") == role
        and action in {"FINAL_AESTHETIC_APPROVAL", "PROJECT_OWNER_AESTHETIC_ACCEPTANCE"}
    ):
        reject("SELF_APPROVAL_FORBIDDEN", f"{role} cannot final-approve its own work")

    if "copy_record" in request:
        if canonical_copy is None:
            reject("CANONICAL_COPY_UNAVAILABLE", "copy comparison source is missing")
        copy_contract = contracts.get("owner_controls", {}).get("exact_copy", {})
        copy_fields = [copy_contract.get("identity_field")] + copy_contract.get("visible_fields", [])
        validate_exact_copy(
            request["copy_record"], canonical_copy,
            fields=[field for field in copy_fields if field],
        )

    if action in {"RELEASE", "LOCK"}:
        if request.get("explicit_owner_decision") is not True:
            reject("EXPLICIT_OWNER_DECISION_REQUIRED", action)
        if state.get("open_blockers"):
            reject("OPEN_BLOCKERS", ", ".join(sorted(state["open_blockers"])))
        permission_key = action.lower()
        if state.get("permissions", {}).get(permission_key) is not True:
            reject("PERMISSION_CLOSED", action)

    if action not in roles[role].get("allowed_actions", []):
        reject("ROLE_ACTION_FORBIDDEN", f"{role}: {action}")

    if action in WRITE_ACTIONS:
        if request.get("task_id") != task.get("task_id"):
            reject("TASK_MISMATCH", str(request.get("task_id")))
        if task.get("current_authorization", {}).get("write_authorized") is not True:
            reject("TASK_CLOSED", str(task.get("status")))
        scope = task.get("delivery_scope", {})
        if request.get("branch") != scope.get("branch"):
            reject("WRONG_BRANCH", str(request.get("branch")))
        path = normalize_path(str(request.get("path", "")))
        if not any(matches_glob(path, pattern) for pattern in scope.get("allowed_globs", [])):
            reject("OUT_OF_SCOPE_PATH", path)
    elif request.get("task_id") == task.get("task_id"):
        allowed = task.get("current_authorization", {}).get("allowed_actions", [])
        if action not in allowed:
            reject("TASK_ACTION_FORBIDDEN", action)


def changed_paths_from_git(root: Path, source: str) -> tuple[list[str], list[str]]:
    committed = set(filter(None, git(root, "diff", "--name-only", f"{source}..HEAD").splitlines()))
    status_lines = git(root, "status", "--porcelain", "--untracked-files=all").splitlines()
    working: set[str] = set()
    for line in status_lines:
        if not line:
            continue
        value = line[3:]
        if " -> " in value:
            value = value.split(" -> ", 1)[1]
        # Python bytecode is transient execution output, never migration input.
        # It is intentionally excluded from a source/commit scope audit.
        parts = PurePosixPath(value).parts
        if "__pycache__" in parts or value.endswith(".pyc"):
            continue
        working.add(value)
    paths = sorted(committed | working)

    binary: set[str] = set()
    for line in git(root, "diff", "--numstat", f"{source}..HEAD").splitlines():
        parts = line.split("\t")
        if len(parts) >= 3 and "-" in parts[:2]:
            binary.add(parts[-1])
    for relative in working:
        path = root / relative
        if path.is_file() and b"\0" in path.read_bytes()[:8192]:
            binary.add(relative)
    return paths, sorted(binary)


def compare_v3_v4(v3: dict[str, Any], state: dict[str, Any]) -> dict[str, bool]:
    v3_streams = v3.get("workstreams", {})
    v4_streams = state.get("workstreams", {})
    return {
        "write_authority": (
            v3.get("current_authorization") is None
            and state.get("current_project_authorization") is None
        ),
        "active_task": (
            v3.get("current_authorization") is None
            and state.get("active_project_task_id") is None
        ),
        "v26_tree": (
            v3.get("locked_release_tree_sha")
            == state.get("source_checkpoint", {}).get("locked_release_tree_sha")
        ),
        "active_candidate": (
            v3.get("active_visual_candidate") == state.get("active_visual_candidate")
        ),
        "open_blockers": (
            set(v3.get("open_blockers", {})) == set(state.get("open_blockers", {}))
        ),
        "permissions": v3.get("permissions") == state.get("permissions"),
        "workstream_heads": all(
            v3_streams.get(name, {}).get("head") == v4_streams.get(name, {}).get("head")
            for name in {"story", "art_direction", "visual", "simulation"}
        ),
        "accepted_art_direction": (
            v3_streams.get("art_direction", {}).get("accepted_commit")
            == v4_streams.get("art_direction", {}).get("accepted_commit")
        ),
    }


def validate_repository(
    root: Path = DEFAULT_ROOT,
    audit_branch: str | None = None,
    changed_paths: Iterable[str] | None = None,
) -> dict[str, Any]:
    v4 = root / "governance" / "v4"
    state = load_json(v4 / "runtime" / "STATE.json")
    contracts = load_json(v4 / "contracts" / "CONTRACTS.json")
    registry = load_json(v4 / "roles" / "REGISTRY.json")
    history = load_json(v4 / "history" / "evidence" / "INDEX.json")
    evidence = load_json(v4 / "evidence" / "MIGRATION_RESULT.json")
    v3 = load_json(root / "governance" / "CURRENT_STAGE.json")

    migration_task_id = state.get("migration_control", {}).get("task_id")
    task = load_task(root, migration_task_id)

    for json_path in sorted(v4.rglob("*.json")):
        load_json(json_path)

    if state.get("canonical") is not True:
        reject("STATE_NOT_CANONICAL", "runtime/STATE.json")
    if state.get("status") != (
        "V4_PARALLEL_BUILD_COMPLETE / PARITY_PASS / "
        "PENDING_PROJECT_OWNER_CUTOVER_APPROVAL"
    ):
        reject("STATE_STATUS_DRIFT", str(state.get("status")))
    checkpoint = state.get("source_checkpoint", {})
    if checkpoint.get("commit") != EXPECTED_SOURCE:
        reject("SOURCE_CHECKPOINT_DRIFT", str(checkpoint.get("commit")))
    if checkpoint.get("v3_status") != "V3_CLEAN_CLOSURE_COMPLETE":
        reject("V3_CLOSURE_DRIFT", str(checkpoint.get("v3_status")))
    if state.get("active_project_task_id") is not None:
        reject("UNEXPECTED_ACTIVE_PROJECT_TASK", str(state.get("active_project_task_id")))
    if state.get("active_visual_candidate") is not None:
        reject("UNEXPECTED_ACTIVE_CANDIDATE", str(state.get("active_visual_candidate")))
    if state.get("current_project_authorization") is not None:
        reject("UNEXPECTED_PROJECT_AUTHORIZATION", "authorization must remain null")
    if set(state.get("open_blockers", {})) != EXPECTED_BLOCKERS:
        reject("BLOCKER_SET_DRIFT", str(sorted(state.get("open_blockers", {}))))
    if not state.get("permissions") or any(state["permissions"].values()):
        reject("PERMISSION_DRIFT", "all project permissions must remain false")
    migration = state.get("migration_control", {})
    if migration.get("branch") != EXPECTED_BRANCH:
        reject("MIGRATION_BRANCH_DRIFT", str(migration.get("branch")))
    if migration.get("cutover_performed") is not False:
        reject("CUTOVER_PERFORMED", "parallel build cannot perform cutover")
    if migration.get("project_owner_cutover_approval") is not None:
        reject("OWNER_CUTOVER_ASSUMED", "owner approval must remain null")

    expected_refs = {
        "contracts": "governance/v4/contracts/CONTRACTS.json",
        "roles": "governance/v4/roles/REGISTRY.json",
    }
    if state.get("canonical_refs") != expected_refs:
        reject("CANONICAL_REFERENCE_DRIFT", str(state.get("canonical_refs")))
    if history.get("canonical") is not False or history.get("may_authorize_work") is not False:
        reject("HISTORY_AUTHORITY_LEAK", "history evidence must remain non-authoritative")

    expected_task_ref = f"governance/v4/tasks/{migration_task_id}.json"
    if state.get("migration_control", {}).get("task_ref") != expected_task_ref:
        reject("TASK_REFERENCE_DRIFT", str(state.get("migration_control", {}).get("task_ref")))
    if task.get("source", {}).get("commit") != EXPECTED_SOURCE:
        reject("TASK_SOURCE_DRIFT", str(task.get("source")))
    if task.get("current_authorization", {}).get("write_authorized") is not False:
        reject("MIGRATION_WRITE_LEFT_OPEN", "delivered task must be read-only")

    if contracts.get("quality_principle") != QUALITY_PRINCIPLE:
        reject("QUALITY_PRINCIPLE_DRIFT", str(contracts.get("quality_principle")))
    if set(contracts.get("protected_quality_gates", [])) != EXPECTED_GATES:
        reject("QUALITY_GATE_PARITY_DRIFT", "protected gate set differs")
    if set(contracts.get("project_owner_required_actions", [])) != OWNER_REQUIRED_ACTIONS:
        reject("OWNER_CONTROL_DRIFT", "material owner action set differs")
    framing = contracts.get("owner_controls", {}).get("framing", {})
    if framing.get("independent_reviewer_role") != "ART_DIRECTION":
        reject("FRAMING_REVIEWER_DRIFT", str(framing.get("independent_reviewer_role")))
    if framing.get("producer_self_approval") is not False:
        reject("FRAMING_SELF_APPROVAL_DRIFT", "producer self-approval must be false")
    if framing.get("allowed_dispositions") != ["FRAMING_PASS", "REFRAME_REQUIRED"]:
        reject("FRAMING_DISPOSITION_DRIFT", str(framing.get("allowed_dispositions")))
    required_dimensions = {
        "bleed", "safe area", "subject scale", "focus", "unintended crop",
        "copy-area collision", "thumbnail and table-distance readability",
        "repeated plan/model/pose", "full-deck composition rhythm",
    }
    if set(framing.get("required_dimensions", [])) != required_dimensions:
        reject("FRAMING_DIMENSION_DRIFT", "framing coverage differs")

    roles = registry.get("roles", {})
    if set(roles) != EXPECTED_ROLES or "RULES_EDITOR" in roles:
        reject("ROLE_REGISTRY_DRIFT", str(sorted(roles)))
    if registry.get("task_scoped_writes") is not True:
        reject("ROLE_WRITE_POLICY_DRIFT", "writes must be task-scoped")
    if "FRAMING_DECISION" in roles.get("VISUAL_DESIGN", {}).get("allowed_actions", []):
        reject("VISUAL_SELF_FRAMING_AUTHORITY", "Visual Design cannot decide framing")
    if "FRAMING_DECISION" not in roles.get("ART_DIRECTION", {}).get("allowed_actions", []):
        reject("ART_DIRECTION_FRAMING_MISSING", "Art Direction must decide framing")

    validate_locked_tree(git(root, "rev-parse", "HEAD:releases/v2.6"))
    if git(root, "cat-file", "-t", EXPECTED_SOURCE, check=False) != "commit":
        reject("SOURCE_COMMIT_UNAVAILABLE", EXPECTED_SOURCE)
    ancestry = subprocess.run(
        ["git", "merge-base", "--is-ancestor", EXPECTED_SOURCE, "HEAD"],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if ancestry.returncode:
        reject("SOURCE_NOT_ANCESTOR", EXPECTED_SOURCE)
    v3_blob_at_source = git(root, "rev-parse", f"{EXPECTED_SOURCE}:governance/CURRENT_STAGE.json")
    v3_blob_at_head = git(root, "rev-parse", "HEAD:governance/CURRENT_STAGE.json")
    if v3_blob_at_source != v3_blob_at_head:
        reject("V3_GOVERNANCE_CHANGED", "CURRENT_STAGE.json differs from source checkpoint")

    actual_paths, binary_paths = changed_paths_from_git(root, EXPECTED_SOURCE)
    if changed_paths is not None:
        actual_paths = sorted(set(changed_paths))
    current_branch = audit_branch or git(root, "branch", "--show-current")
    audit_delivery_scope(task, current_branch, actual_paths, binary_paths)

    parity = compare_v3_v4(v3, state)
    failed_parity = sorted(name for name, passed in parity.items() if not passed)
    if failed_parity:
        reject("V3_V4_PARITY_FAIL", ", ".join(failed_parity))

    owner = contracts.get("owner_controls", {})
    kaptan = owner.get("kaptan", {})
    copy_contract = owner.get("exact_copy", {})
    kaptan_path = root / kaptan.get("binding_visual_source", "")
    copy_path = root / copy_contract.get("source", "")
    patch_path = root / kaptan.get("accepted_art_direction_patch", "")
    if sha256(kaptan_path) != kaptan.get("source_sha256"):
        reject("KAPTAN_SOURCE_DRIFT", str(kaptan_path))
    if sha256(copy_path) != copy_contract.get("source_sha256"):
        reject("EXACT_COPY_SOURCE_DRIFT", str(copy_path))
    if git(root, "rev-parse", f"HEAD:{kaptan['binding_visual_source']}") != kaptan.get("source_git_blob"):
        reject("KAPTAN_SOURCE_BLOB_DRIFT", kaptan["binding_visual_source"])
    if git(root, "rev-parse", f"HEAD:{copy_contract['source']}") != copy_contract.get("source_git_blob"):
        reject("EXACT_COPY_BLOB_DRIFT", copy_contract["source"])
    if git(root, "rev-parse", f"HEAD:{kaptan['accepted_art_direction_patch']}") != kaptan.get("accepted_patch_blob"):
        reject("ART_DIRECTION_PATCH_DRIFT", str(patch_path))

    copy_doc = load_json(copy_path)
    records = copy_doc.get("records", [])
    if len(records) != 1 or records[0].get("id") != "SET-KP-01":
        reject("EXACT_COPY_RECORD_DRIFT", "SET-KP-01 must be the sole owner override")

    tracked = set(git(root, "ls-files").splitlines())
    draft_name = "FOULWAKE_Kural_Kitabi_v2.7_TASLAK.pdf"
    if any(PurePosixPath(path).name == draft_name for path in tracked):
        reject("NONCANONICAL_DRAFT_TRACKED", draft_name)
    external = next(
        (item for item in history.get("records", []) if item.get("evidence_id") == "EXTERNAL-RULEBOOK-DRAFT"),
        {},
    )
    if external.get("status") != "NON_CANONICAL_DRAFT / REFERENCE_ONLY":
        reject("EXTERNAL_DRAFT_STATUS_DRIFT", str(external.get("status")))
    if external.get("repository_artifact_present") is not False:
        reject("EXTERNAL_DRAFT_AUTHORITY_LEAK", "draft must stay outside repository")

    if evidence.get("result") != (
        "V4_PARALLEL_BUILD_COMPLETE / PARITY_PASS / "
        "PENDING_PROJECT_OWNER_CUTOVER_APPROVAL"
    ):
        reject("MIGRATION_EVIDENCE_DRIFT", str(evidence.get("result")))
    if evidence.get("cutover_performed") is not False:
        reject("EVIDENCE_CUTOVER_DRIFT", "cutover must be false")

    return {
        "changed_files": len(actual_paths),
        "v26_tree": EXPECTED_V26_TREE,
        "parity": parity,
        "cutover_performed": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--audit-branch")
    parser.add_argument("--changed-file", action="append", dest="changed_files")
    parser.add_argument("--request", type=Path)
    args = parser.parse_args()

    try:
        if args.request:
            root = args.root.resolve()
            state = load_json(root / "governance/v4/runtime/STATE.json")
            request = load_json(args.request)
            task_id = request.get("task_id") or state.get("migration_control", {}).get("task_id")
            task = load_task(root, task_id)
            registry = load_json(root / "governance/v4/roles/REGISTRY.json")
            contracts = load_json(root / "governance/v4/contracts/CONTRACTS.json")
            copy_doc = load_json(root / contracts["owner_controls"]["exact_copy"]["source"])
            authorize_request(
                state, task, registry, contracts, request,
                canonical_copy=copy_doc["records"][0],
            )
            print("FOULWAKE governance v4 request: ALLOW")
            return
        result = validate_repository(args.root.resolve(), args.audit_branch, args.changed_files)
    except GovernanceViolation as exc:
        print(f"FOULWAKE governance v4: BLOCKED — {exc}", file=sys.stderr)
        raise SystemExit(1)

    print("FOULWAKE governance v4: PASS")
    print(f"- exact migration scope: {result['changed_files']} files")
    print(f"- locked v2.6 tree: {result['v26_tree']}")
    print("- v3/v4 runtime, role and quality-gate parity: PASS")
    print("- cutover: NO")


if __name__ == "__main__":
    main()
