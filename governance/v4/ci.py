#!/usr/bin/env python3
"""Check Git objects against the integration branch's v4 authority, never a specialist's policy."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from validator import GovernanceViolation, require, scope_allows, validate_runtime_documents, validate_live_task


def git(root, *args):
    result = subprocess.run(["git", *args], cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    require(result.returncode == 0, "CI_GIT_ERROR", result.stderr.decode(errors="replace"))
    return result.stdout


def read(root, ref, path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "CI_DUPLICATE_JSON_KEY", key)
            result[key] = value
        return result
    return json.loads(git(root, "show", f"{ref}:{path}"), object_pairs_hook=unique)


def sha(root, ref):
    return git(root, "rev-parse", "--verify", ref).decode().strip()


def validate_branch(root: Path, authority: str, branch: str, head: str) -> dict:
    authority = sha(root, authority + "^{commit}")
    head = sha(root, head + "^{commit}")
    state = read(root, authority, "governance/v4/runtime/STATE.json")
    require(state.get("migration_control", {}).get("cutover_performed") is True, "CI_V4_NOT_ACTIVE", authority)
    contracts = read(root, authority, state["canonical_refs"]["contracts"])
    roles = read(root, authority, state["canonical_refs"]["roles"])
    workstreams = state.get("workstreams", {})
    matches = [entry for entry in workstreams.values() if entry.get("branch") == branch]
    require(len(matches) == 1, "CI_UNKNOWN_WORKSTREAM", branch)
    expected_tree = state["source_checkpoint"]["locked_release_tree_sha"]
    require(sha(root, head + ":releases/v2.6") == expected_tree, "CI_LOCKED_TREE_DRIFT", branch)
    active_id = state.get("active_project_task_id")
    task = read(root, authority, f"governance/v4/tasks/{active_id}.json") if active_id else None
    if not task or task.get("scope", {}).get("branch") != branch:
        require(head == matches[0].get("head"), "CI_UNAUTHORIZED_BRANCH_CHANGE", branch)
        return {"branch": branch, "head": head, "status": "PASS / FROZEN / NO_WRITE_AUTHORITY", "changed_files": 0}
    validate_runtime_documents(state, {active_id: task}, contracts, roles)
    require(task["authorization"]["enabled"] is True and task["authorization"]["write_authorized"] is True,
            "CI_TASK_WRITE_CLOSED", active_id)
    boundary = contracts["lifecycle"]["role_boundaries"][task["executor_role"]]
    require(boundary["branch"] == branch, "CI_ROLE_BRANCH_MISMATCH", branch)
    task_path = f"governance/v4/tasks/{active_id}.json"
    additions = git(root, "log", "--diff-filter=A", "--format=%H", authority, "--", task_path).decode().splitlines()
    require(len(additions) == 1, "CI_ACTIVATION_AMBIGUOUS", active_id)
    baseline = additions[0]
    require(subprocess.run(["git", "merge-base", "--is-ancestor", baseline, head], cwd=root,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0,
            "CI_WRONG_BASELINE", branch)
    for pin in task.get("inputs", []):
        require(sha(root, head + ":" + pin["path"]) == pin["git_blob"], "CI_TASK_INPUT_DRIFT", pin["path"])
    validate_live_task(root, task, state, contracts)
    for action in task["authorization"]["allowed_actions"]:
        permission = contracts["runtime_authorization"]["action_permission_map"].get(action)
        if permission:
            require(state["permissions"].get(permission) is True, "CI_PERMISSION_CLOSED", permission)
    # The committed baseline is implicit in task creation; a branch cannot edit
    # its own task or contracts to enlarge the authority read above.
    names = git(root, "diff", "--no-renames", "--name-only", "-z", baseline, head).decode().split("\x00")
    paths = [name for name in names if name]
    scope = task["scope"]
    require(len(paths) <= scope["max_changed_files"], "CI_FILE_COUNT_EXCEEDED", str(len(paths)))
    for path in paths:
        require(scope_allows(boundary, path) and scope_allows(scope, path), "CI_OUT_OF_SCOPE_PATH", path)
        require(Path(path).suffix in scope["allowed_extensions"], "CI_FILE_TYPE_FORBIDDEN", path)
        entry = git(root, "ls-tree", head, "--", path).decode().strip()
        require(entry.startswith("100644 blob "), "CI_UNSAFE_FILE_MODE_OR_DELETION", path)
        if scope["binary_files_allowed"] is False:
            data = git(root, "show", f"{head}:{path}")
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                require(False, "CI_BINARY_FORBIDDEN", path)
            require("\x00" not in text, "CI_BINARY_FORBIDDEN", path)
    return {"branch": branch, "head": head, "task_id": active_id, "baseline": baseline,
            "authority": authority, "status": "PASS / TASK_SCOPE_ONLY", "changed_files": len(paths)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--authority", required=True)
    parser.add_argument("--branch")
    parser.add_argument("--head")
    parser.add_argument("--all-workstreams", action="store_true")
    args = parser.parse_args()
    try:
        if args.all_workstreams:
            state = read(args.root, args.authority, "governance/v4/runtime/STATE.json")
            results = [validate_branch(args.root, args.authority, row["branch"], "refs/remotes/origin/" + row["branch"])
                       for row in state["workstreams"].values()]
        else:
            require(bool(args.branch and args.head), "CI_ARGUMENTS", "branch and head are required")
            results = [validate_branch(args.root, args.authority, args.branch, args.head)]
        print(json.dumps({"result": "PASS", "workstreams": results}, ensure_ascii=False, indent=2))
    except (GovernanceViolation, ValueError, KeyError, OSError) as exc:
        parser.exit(1, f"FOULWAKE v4 CI: BLOCKED — {exc}\n")


if __name__ == "__main__":
    main()
