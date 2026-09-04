#!/usr/bin/env python3
"""One-time scope and parity audit for the Governance v4 cutover rework."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

import validator

DEFAULT_ROOT = Path(__file__).resolve().parents[2]


def changed_paths_from_git(root: Path, baseline: str) -> tuple[list[str], list[str]]:
    committed = set(
        filter(None, validator.git(root, "diff", "--name-only", f"{baseline}..HEAD").splitlines())
    )
    status = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    ).stdout
    working: set[str] = set()
    for line in status.splitlines():
        if not line:
            continue
        value = line[3:].split(" -> ", 1)[-1]
        parts = PurePosixPath(value).parts
        if "__pycache__" in parts or value.endswith(".pyc"):
            continue
        working.add(value)
    paths = sorted(committed | working)

    binary: set[str] = set()
    for line in validator.git(root, "diff", "--numstat", f"{baseline}..HEAD").splitlines():
        parts = line.split("\t")
        if len(parts) >= 3 and "-" in parts[:2]:
            binary.add(parts[-1])
    for relative in working:
        path = root / relative
        if path.is_file() and b"\0" in path.read_bytes()[:8192]:
            binary.add(relative)
    return paths, sorted(binary)


def audit_scope(
    task: dict[str, Any],
    branch: str,
    changed_paths: Iterable[str],
    binary_paths: Iterable[str],
) -> None:
    scope = task["scope"]
    validator.require(branch == scope["branch"], "WRONG_BRANCH", f"expected {scope['branch']}, got {branch}")
    paths = [validator.normalize_path(path) for path in changed_paths]
    validator.require(len(paths) == len(set(paths)), "DUPLICATE_CHANGED_PATH", "scope input")
    for path in paths:
        validator.require(validator.scope_allows(scope, path), "OUT_OF_SCOPE_PATH", path)

    expected = set(scope.get("expected_paths", []))
    if expected:
        missing = sorted(expected - set(paths))
        extra = sorted(set(paths) - expected)
        validator.require(not missing and not extra, "SCOPE_PATH_SET_DRIFT", f"missing={missing}; extra={extra}")
    maximum = scope.get("max_changed_files")
    validator.require(isinstance(maximum, int) and len(paths) <= maximum, "CHANGED_FILE_BUDGET", f"{len(paths)} > {maximum}")
    extensions = set(scope.get("allowed_extensions", []))
    wrong_type = [path for path in paths if PurePosixPath(path).suffix not in extensions]
    validator.require(not wrong_type, "DISALLOWED_FILE_TYPE", ", ".join(wrong_type))
    validator.require(
        not list(binary_paths) or scope.get("binary_files_allowed") is True,
        "BINARY_CHANGE_FORBIDDEN",
        ", ".join(binary_paths),
    )


def compare_v3_runtime(v3: dict[str, Any], state: dict[str, Any]) -> dict[str, bool]:
    v3_streams = v3.get("workstreams", {})
    v4_streams = state.get("workstreams", {})
    return {
        "write_authority": v3.get("current_authorization") is None and state.get("active_project_task_id") is None,
        "active_task": v3.get("current_authorization") is None and state.get("active_project_task_id") is None,
        "v26_tree": v3.get("locked_release_tree_sha") == state.get("source_checkpoint", {}).get("locked_release_tree_sha"),
        "active_candidate": v3.get("active_visual_candidate") == state.get("active_visual_candidate"),
        "open_blockers": set(v3.get("open_blockers", {})) == set(state.get("open_blockers", {})),
        "permissions": v3.get("permissions") == state.get("permissions"),
        "workstream_heads": all(
            v3_streams.get(name, {}).get("head") == v4_streams.get(name, {}).get("head")
            for name in ("story", "art_direction", "visual", "simulation")
        ),
        "accepted_art_direction": (
            v3_streams.get("art_direction", {}).get("accepted_commit")
            == v4_streams.get("art_direction", {}).get("accepted_commit")
        ),
    }


def json_at_commit(root: Path, commit: str, path: str) -> dict[str, Any]:
    try:
        value = json.loads(validator.git(root, "show", f"{commit}:{path}"))
    except Exception as exc:
        validator.reject("BASELINE_JSON_ERROR", f"{path}: {exc}")
    validator.require(isinstance(value, dict), "BASELINE_JSON_ERROR", path)
    return value


def path_unchanged(root: Path, baseline: str, path: str) -> bool:
    result = subprocess.run(
        ["git", "diff", "--quiet", baseline, "--", path],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return result.returncode == 0


def preserves_baseline_structure(baseline: Any, current: Any) -> bool:
    """Allow additive schema fields while forbidding removal or semantic drift."""
    if isinstance(baseline, dict):
        return isinstance(current, dict) and all(
            key in current and preserves_baseline_structure(value, current[key])
            for key, value in baseline.items()
        )
    return baseline == current


def validate_rework(root: Path = DEFAULT_ROOT) -> dict[str, Any]:
    root = root.resolve()
    runtime_result = validator.validate_repository(root)
    state, tasks, contracts, _registry = validator.load_repository_bundle(root)
    migration = state["migration_control"]
    task_id = migration["task_id"]
    validator.require(task_id in tasks, "TASK_NOT_FOUND", task_id)
    task = tasks[task_id]
    baseline = task.get("source", {}).get("commit")
    validator.require(isinstance(baseline, str), "MIGRATION_AUDIT_SCHEMA", "source commit")
    validator.require(validator.git(root, "cat-file", "-t", baseline, check=False) == "commit", "SOURCE_COMMIT_UNAVAILABLE", baseline)
    validator.require(
        validator.git(root, "rev-parse", f"{baseline}^{{tree}}")
        == task.get("source", {}).get("tree"),
        "SOURCE_TREE_DRIFT",
        baseline,
    )
    validator.require(
        migration.get("rework_source_commit") == baseline,
        "MIGRATION_CONTROL_SOURCE_DRIFT",
        str(migration.get("rework_source_commit")),
    )
    validator.require(
        migration.get("task_ref") == f"governance/v4/tasks/{task_id}.json",
        "MIGRATION_CONTROL_TASK_REF_DRIFT",
        str(migration.get("task_ref")),
    )
    validator.require(
        migration.get("evidence_ref") == task.get("completion_evidence"),
        "MIGRATION_CONTROL_EVIDENCE_REF_DRIFT",
        str(migration.get("evidence_ref")),
    )
    ancestry = subprocess.run(
        ["git", "merge-base", "--is-ancestor", baseline, "HEAD"],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    validator.require(ancestry.returncode == 0, "SOURCE_NOT_ANCESTOR", baseline)

    paths, binary = changed_paths_from_git(root, baseline)
    branch = validator.git(root, "branch", "--show-current")
    audit_scope(task, branch, paths, binary)
    validator.validate_locked_tree(
        validator.git(root, "rev-parse", "HEAD:releases/v2.6"),
        task["source"]["locked_release_tree_sha"],
    )

    for protected in task.get("protected_unchanged_paths", []):
        validator.require(path_unchanged(root, baseline, protected), "PROTECTED_EVIDENCE_CHANGED", protected)

    baseline_contracts = json_at_commit(root, baseline, state["canonical_refs"]["contracts"])
    for key in (
        "quality_principle",
        "protected_quality_gates",
        "project_owner_required_actions",
    ):
        validator.require(contracts.get(key) == baseline_contracts.get(key), "QUALITY_PARITY_DRIFT", key)
    validator.require(
        preserves_baseline_structure(
            baseline_contracts.get("owner_controls"),
            contracts.get("owner_controls"),
        ),
        "QUALITY_PARITY_DRIFT",
        "owner_controls",
    )

    v3 = validator.load_json(root / "governance" / "CURRENT_STAGE.json")
    parity = compare_v3_runtime(v3, state)
    failures = sorted(key for key, passed in parity.items() if not passed)
    validator.require(not failures, "V3_V4_PARITY_FAIL", ", ".join(failures))
    validator.require(migration.get("cutover_performed") is False, "CUTOVER_PERFORMED", task_id)
    validator.require(migration.get("project_owner_cutover_approval") is None, "OWNER_CUTOVER_ASSUMED", task_id)

    evidence = validator.load_json(root / migration["evidence_ref"])
    validator.require(evidence.get("source", {}).get("commit") == baseline, "REWORK_EVIDENCE_DRIFT", "source")
    validator.require(evidence.get("task", {}).get("task_id") == task_id, "REWORK_EVIDENCE_DRIFT", "task")
    validator.require(
        evidence.get("scope_audit", {}).get("changed_files") == len(paths),
        "REWORK_EVIDENCE_DRIFT",
        "changed_files",
    )
    validator.require(
        evidence.get("v26_locked_tree_preserved") is True
        and evidence.get("source", {}).get("v26_locked_tree")
        == task["source"]["locked_release_tree_sha"],
        "REWORK_EVIDENCE_DRIFT",
        "v2.6 tree",
    )
    validator.require(
        evidence.get("game_content_or_production_artifact_changed") is False,
        "REWORK_EVIDENCE_DRIFT",
        "content change",
    )
    validator.require(
        evidence.get("result")
        == "V4_REWORK_COMPLETE / GENERIC_RUNTIME_PASS / PENDING_PROJECT_OWNER_CUTOVER_APPROVAL",
        "REWORK_EVIDENCE_DRIFT",
        str(evidence.get("result")),
    )
    validator.require(evidence.get("cutover_performed") is False, "EVIDENCE_CUTOVER_DRIFT", task_id)
    return {
        "baseline": baseline,
        "changed_files": len(paths),
        "parity": parity,
        "runtime": runtime_result,
        "v26_tree": task["source"]["locked_release_tree_sha"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()
    try:
        result = validate_rework(args.root)
    except validator.GovernanceViolation as exc:
        print(f"FOULWAKE v4 migration rework audit: BLOCKED — {exc}", file=sys.stderr)
        raise SystemExit(1)
    print("FOULWAKE v4 migration rework audit: PASS")
    print(f"- source: {result['baseline']}")
    print(f"- exact rework scope: {result['changed_files']} files")
    print("- v3/v4 parity: PASS")
    print("- original migration evidence: byte-exact preserved")
    print("- cutover: NO")


if __name__ == "__main__":
    main()
