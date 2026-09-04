#!/usr/bin/env python3
"""Generate concise, non-canonical FOULWAKE role bootstrap instructions."""

from __future__ import annotations

import argparse
from pathlib import Path

from validator import (
    DEFAULT_ROOT,
    GovernanceViolation,
    authorize_repository_request,
    git,
    load_repository_bundle,
    reject,
)


def build_bootstrap(root: Path, role_name: str, task_id: str | None = None) -> str:
    extra = [task_id] if task_id else []
    state, tasks, contracts, registry = load_repository_bundle(root, extra)

    roles = registry.get("roles", {})
    if role_name not in roles:
        reject("UNKNOWN_ROLE", role_name)
    role = roles[role_name]

    selected_task = task_id or state.get("active_project_task_id")
    task = tasks.get(selected_task) if selected_task else None
    migration_task = (state.get("migration_control") or {}).get("task_id")
    binding = "NONE"
    if selected_task == state.get("active_project_task_id") and selected_task:
        binding = "ACTIVE_PROJECT_TASK"
    elif selected_task == migration_task and selected_task:
        binding = "MIGRATION_CONTROL_ONLY"
    elif selected_task:
        binding = "INACTIVE / NO AUTHORITY"

    lines = [
        "# GENERATED / NON_CANONICAL — FOULWAKE ROLE BOOTSTRAP",
        "",
        f"ROLE: {role_name}",
        f"RUNTIME_STATE: governance/v4/runtime/STATE.json ({state.get('status')})",
        f"ACTIVE_PROJECT_TASK: {state.get('active_project_task_id') or 'NONE'}",
        f"ACTIVE_CANDIDATE: {state.get('active_visual_candidate') or 'NONE'}",
        "DEFAULT: DENY unless an exact active task and this role both authorize the action.",
        "",
        "ALLOWED_ROLE_ACTIONS: " + ", ".join(role.get("allowed_actions", [])),
    ]
    if role.get("cannot"):
        lines.append("ROLE_PROHIBITIONS: " + "; ".join(role["cannot"]))

    if task:
        authorization = task.get("authorization", {})
        role_actions = authorization.get("role_actions", {}).get(role_name, [])
        lines.extend([
            "",
            f"TASK_ID: {task.get('task_id')}",
            f"TASK_STATUS: {task.get('status')}",
            f"TASK_BINDING: {binding}",
            f"TASK_BRANCH: {task.get('scope', {}).get('branch')}",
            f"CURRENT_WRITE_AUTHORIZED: {str(authorization.get('write_authorized') is True and binding == 'ACTIVE_PROJECT_TASK').upper()}",
            "CURRENT_ROLE_TASK_ACTIONS: " + (", ".join(role_actions) or "NONE"),
        ])
    else:
        lines.extend([
            "",
            "TASK_STATUS: NO ACTIVE PROJECT TASK",
            "CURRENT_WRITE_AUTHORIZED: FALSE",
        ])

    lines.extend([
        "",
        "QUALITY_CONTRACT: governance/v4/contracts/CONTRACTS.json",
        f"QUALITY_PRINCIPLE: {contracts.get('quality_principle')}",
        "HISTORY_EVIDENCE: NON-CANONICAL / CANNOT AUTHORIZE WORK",
        "PROJECT_OWNER_APPROVAL: Never infer it; require an explicit material decision.",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--role", required=True)
    parser.add_argument("--task-id")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        root = args.root.resolve()
        rendered = build_bootstrap(root, args.role, args.task_id)
        if args.output:
            generated_root = (root / "governance" / "v4" / "generated").resolve()
            destination = args.output
            if not destination.is_absolute():
                destination = generated_root / destination
            destination = destination.resolve()
            if destination.parent != generated_root:
                reject("GENERATED_OUTPUT_SCOPE", str(destination))
            state, _tasks, _contracts, _registry = load_repository_bundle(root)
            task_id = args.task_id or state.get("active_project_task_id")
            if not task_id:
                reject("NO_ACTIVE_TASK", "generated output writes require an exact active task")
            authorize_repository_request(root, {
                "role": args.role,
                "action": "WRITE",
                "task_id": task_id,
                "branch": git(root, "branch", "--show-current"),
                "path": destination.relative_to(root).as_posix(),
            })
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(rendered, encoding="utf-8")
            print(destination)
        else:
            print(rendered, end="")
    except GovernanceViolation as exc:
        parser.exit(1, f"FOULWAKE bootstrap: BLOCKED — {exc}\n")


if __name__ == "__main__":
    main()
