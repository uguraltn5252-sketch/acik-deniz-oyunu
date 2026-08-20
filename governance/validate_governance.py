#!/usr/bin/env python3
"""FOULWAKE editorial-governance integrity checks."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def require(path: str) -> Path:
    target = ROOT / path
    if not target.exists():
        ERRORS.append(f"missing required path: {path}")
    return target


required_paths = [
    "AI_HANDOFF.md",
    "PROJECT_STATE.md",
    "releases/v2.6",
    "governance/EDITORIAL_CHARTER.md",
    "governance/WORKSTREAM_PROTOCOL.md",
    "governance/RELEASE_GATE.md",
    "governance/ACTIVE_WORKSTREAMS.json",
    "governance/COORDINATION_LOG.md",
    "governance/LOCK_AUTHORIZATION_SCHEMA.json",
    "governance/SIM_QA_ATTESTATION_SCHEMA.json",
]

for required_path in required_paths:
    require(required_path)

state_path = ROOT / "governance/ACTIVE_WORKSTREAMS.json"
if state_path.exists():
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"ACTIVE_WORKSTREAMS.json is invalid: {exc}")
    else:
        locked = state.get("locked_release", {})
        draft = state.get("active_draft", {})
        roles = state.get("roles", {})
        policy = state.get("lock_policy", {})
        readiness = state.get("release_readiness", {})
        blockers = state.get("open_blockers", [])

        if locked.get("version") != "v2.6":
            ERRORS.append("locked release must remain v2.6")
        if locked.get("status") != "STABLE_LOCKED":
            ERRORS.append("v2.6 must remain STABLE_LOCKED")
        if locked.get("mutable") is not False:
            ERRORS.append("locked release must be immutable")
        if draft.get("version") != "v2.7":
            ERRORS.append("active draft must be v2.7")
        if draft.get("status") != "DRAFT_NOT_LOCKED":
            ERRORS.append("v2.7 must remain DRAFT_NOT_LOCKED")
        if not roles.get("chief_editor", {}).get("exclusive_lock_authority"):
            ERRORS.append("chief editor must retain exclusive lock authority")
        if not roles.get("simulation_test", {}).get("mandatory_release_gate"):
            ERRORS.append("simulation test must remain a mandatory release gate")
        if policy.get("blocker_veto") is not True:
            ERRORS.append("BLOCKER veto must remain enabled")
        if readiness.get("verdict") == "BLOCKER" and readiness.get("lock_allowed") is not False:
            ERRORS.append("BLOCKER readiness must prohibit locking")
        blocker_ids = [item.get("id") for item in blockers if item.get("status") == "OPEN"]
        if len(blocker_ids) != len(set(blocker_ids)):
            ERRORS.append("open blocker ids must be unique")
        if readiness.get("verdict") == "BLOCKER" and not blocker_ids:
            ERRORS.append("BLOCKER readiness must name at least one open blocker")

project_state = ROOT / "PROJECT_STATE.md"
if project_state.exists():
    text = project_state.read_text(encoding="utf-8")
    for marker in ("v2.6 STABLE / LOCKED", "v2.7 DRAFT / NOT LOCKED"):
        if marker not in text:
            ERRORS.append(f"PROJECT_STATE.md is missing marker: {marker}")

future_release = ROOT / "releases/v2.7"
authorization = ROOT / "governance/LOCK_AUTHORIZATION_v2.7.json"
if future_release.exists() and not authorization.exists():
    ERRORS.append("releases/v2.7 exists without chief-editor lock authorization")
elif future_release.exists() and authorization.exists():
    try:
        lock = json.loads(authorization.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"LOCK_AUTHORIZATION_v2.7.json is invalid: {exc}")
    else:
        if lock.get("version") != "v2.7":
            ERRORS.append("lock authorization version must be v2.7")
        if lock.get("authorized_by_project_owner") is not True:
            ERRORS.append("lock authorization requires explicit project-owner authorization")
        if lock.get("executed_by_role") != "chief_editor":
            ERRORS.append("only chief_editor may execute the lock")
        if not re.fullmatch(r"[0-9a-f]{40}", str(lock.get("candidate_commit", ""))):
            ERRORS.append("lock authorization requires an exact 40-character candidate commit")
        if lock.get("simulation_verdict") not in {"PASS", "PASS_WITH_MINOR_ISSUES"}:
            ERRORS.append("lock authorization requires a passing simulation verdict")
        if lock.get("open_blockers") != []:
            ERRORS.append("lock authorization requires an empty open_blockers list")
        attestation_path = lock.get("simulation_attestation_path")
        attestation_rel = Path(attestation_path) if isinstance(attestation_path, str) else None
        if (
            attestation_rel is None
            or attestation_rel.is_absolute()
            or ".." in attestation_rel.parts
            or not (ROOT / attestation_rel).is_file()
        ):
            ERRORS.append("lock authorization requires an existing simulation attestation")
        else:
            try:
                attestation = json.loads((ROOT / attestation_rel).read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                ERRORS.append(f"simulation attestation is invalid: {exc}")
            else:
                if attestation.get("candidate_commit") != lock.get("candidate_commit"):
                    ERRORS.append("simulation attestation must match the authorized candidate commit")
                if attestation.get("overall_verdict") != lock.get("simulation_verdict"):
                    ERRORS.append("simulation attestation verdict must match lock authorization")
                if not re.fullmatch(
                    r"[0-9a-f]{64}", str(attestation.get("evidence_bundle_sha256", ""))
                ):
                    ERRORS.append("simulation attestation requires a SHA-256 evidence bundle hash")

if ERRORS:
    print("FOULWAKE GOVERNANCE: FAIL")
    for error in ERRORS:
        print(f"- {error}")
    sys.exit(1)

print("FOULWAKE GOVERNANCE: PASS")
