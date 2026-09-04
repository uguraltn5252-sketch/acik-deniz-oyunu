#!/usr/bin/env python3
"""Generate concise, non-canonical FOULWAKE role bootstrap instructions."""

from __future__ import annotations

import argparse
from pathlib import Path

from validator import (
    DEFAULT_ROOT,
    GovernanceViolation,
    authorize_request,
    git,
    load_json,
    load_task,
    reject,
)


def build_bootstrap(root: Path, role_name: str, task_id: str | None = None) -> str:
    v4 = root / "governance" / "v4"
    state = load_json(v4 / "runtime" / "STATE.json")
    registry = load_json(v4 / "roles" / "REGISTRY.json")
    contracts = load_json(v4 / "contracts" / "CONTRACTS.json")

    roles = registry.get("roles", {})
    if role_name not in roles:
        reject("UNKNOWN_ROLE", role_name)
    role = roles[role_name]

    selected_task = task_id or state.get("active_project_task_id")
    task = None
    if selected_task:
        task_path = v4 / "tasks" / f"{selected_task}.json"
        if not task_path.is_file():
            reject("TASK_NOT_FOUND", selected_task)
        task = load_json(task_path)

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
        current = task.get("current_authorization", {})
        lines.extend([
            "",
            f"TASK_ID: {task.get('task_id')}",
            f"TASK_STATUS: {task.get('status')}",
            f"TASK_BRANCH: {task.get('delivery_scope', {}).get('branch')}",
            f"CURRENT_WRITE_AUTHORIZED: {str(current.get('write_authorized')).upper()}",
            "CURRENT_TASK_ACTIONS: " + ", ".join(current.get("allowed_actions", [])),
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
            state = load_json(root / "governance/v4/runtime/STATE.json")
            task_id = args.task_id or state.get("active_project_task_id")
            if not task_id:
                reject("NO_ACTIVE_TASK", "generated output writes require an exact active task")
            task = load_task(root, task_id)
            registry = load_json(root / "governance/v4/roles/REGISTRY.json")
            contracts = load_json(root / "governance/v4/contracts/CONTRACTS.json")
            authorize_request(
                state,
                task,
                registry,
                contracts,
                {
                    "role": args.role,
                    "action": "WRITE",
                    "task_id": task_id,
                    "branch": git(root, "branch", "--show-current"),
                    "path": destination.relative_to(root).as_posix(),
                },
            )
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(rendered, encoding="utf-8")
            print(destination)
        else:
            print(rendered, end="")
    except GovernanceViolation as exc:
        parser.exit(1, f"FOULWAKE bootstrap: BLOCKED — {exc}\n")


if __name__ == "__main__":
    main()
