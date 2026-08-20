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
    "governance/DECISION_REGISTER.md",
    "governance/WORKSTREAM_ASSIGNMENTS.md",
    "governance/LOCK_AUTHORIZATION_SCHEMA.json",
    "governance/SIM_QA_ATTESTATION_SCHEMA.json",
    "working/v2.7/V27_MECHANIC_DECISIONS.json",
    "working/v2.7/SOURCE_HIERARCHY_v2.7.json",
    "working/v2.7/FOULWAKE_STORY_FRAMEWORK.md",
    "working/v2.7/FOULWAKE_VISUAL_SYSTEM.md",
    "working/v2.7/FOULWAKE_NARRATIVE_VALIDATION_v2.7.md",
    "working/v2.7/BINARY_ARTIFACTS.md",
    "working/v2.7/qa/RELEASE_BLOCKER_RESOLUTION_PLAN_v2.7.md",
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
        resolved = state.get("resolved_blockers", [])

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
        if "CAN-001" in blocker_ids:
            ERRORS.append("CAN-001 must not remain open after Story reclassification")
        if "CAN-001" not in {item.get("id") for item in resolved}:
            ERRORS.append("CAN-001 resolution must be recorded")
        mechanic = next((item for item in blockers if item.get("id") == "MEC-001"), {})
        if mechanic.get("decision_status") != "APPROVED_FOR_V2.7_DRAFT":
            ERRORS.append("MEC-001 must preserve the approved Sea=Rock v2.7 draft decision")

project_state = ROOT / "PROJECT_STATE.md"
if project_state.exists():
    text = project_state.read_text(encoding="utf-8")
    for marker in ("v2.6 STABLE / LOCKED", "v2.7 DRAFT / NOT LOCKED"):
        if marker not in text:
            ERRORS.append(f"PROJECT_STATE.md is missing marker: {marker}")

decision_register = ROOT / "governance/DECISION_REGISTER.md"
if decision_register.exists():
    text = decision_register.read_text(encoding="utf-8")
    for marker in ("DEC-20260820-01", "Açık Deniz ve Kayalık", "APPROVED FOR v2.7 DRAFT"):
        if marker not in text:
            ERRORS.append(f"decision register is missing marker: {marker}")

story_framework = ROOT / "working/v2.7/FOULWAKE_STORY_FRAMEWORK.md"
if story_framework.exists():
    text = story_framework.read_text(encoding="utf-8")
    for identity in ("CAN-08", "CAN-09"):
        if not re.search(rf"\| `{identity}` \| TASLAK \|", text):
            ERRORS.append(f"{identity} must be classified as TASLAK")
        if re.search(rf"\| `{identity}` \| KANON \|", text):
            ERRORS.append(f"{identity} must not remain KANON")

visual_system = ROOT / "working/v2.7/FOULWAKE_VISUAL_SYSTEM.md"
if visual_system.exists():
    text = visual_system.read_text(encoding="utf-8")
    for marker in (
        "FOULWAKE_CARD_TEXTS_v2.7.json",
        "FOULWAKE_RULEBOOK_STORY_v2.7.md",
        "Bağlayıcı v2.7 DRAFT kararı",
        "tam Simülasyon yeniden testi",
    ):
        if marker not in text:
            ERRORS.append(f"visual source contract is missing marker: {marker}")

narrative_validation = ROOT / "working/v2.7/FOULWAKE_NARRATIVE_VALIDATION_v2.7.md"
if narrative_validation.exists():
    text = narrative_validation.read_text(encoding="utf-8")
    if "REPRODUCTION PENDING" not in text or "QA-001 OPEN" not in text:
        ERRORS.append("narrative validation must remain reproduction-pending evidence")

mechanic_decisions = ROOT / "working/v2.7/V27_MECHANIC_DECISIONS.json"
if mechanic_decisions.exists():
    try:
        mechanic_state = json.loads(mechanic_decisions.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"V27_MECHANIC_DECISIONS.json is invalid: {exc}")
    else:
        decisions = {item.get("id"): item for item in mechanic_state.get("decisions", [])}
        sea_rock = decisions.get("DEC-20260820-01", {})
        if sea_rock.get("value") != "SEA_ROCK_SHARED_BACK":
            ERRORS.append("v2.7 mechanic decisions must preserve the shared Sea-Rock back")
        if sea_rock.get("release_status") != "BLOCKER_UNTIL_RETEST":
            ERRORS.append("shared Sea-Rock back must remain blocked until full retest")

source_hierarchy = ROOT / "working/v2.7/SOURCE_HIERARCHY_v2.7.json"
if source_hierarchy.exists():
    try:
        source_state = json.loads(source_hierarchy.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"SOURCE_HIERARCHY_v2.7.json is invalid: {exc}")
    else:
        priorities = [item.get("priority") for item in source_state.get("sources", [])]
        if priorities != [1, 2, 3, 4, 5]:
            ERRORS.append("v2.7 source hierarchy priorities must remain 1 through 5")
        if source_state.get("conflict_action") != "STOP_AND_HANDOFF_TO_CHIEF_EDITOR":
            ERRORS.append("source conflicts must stop and hand off to chief editor")

binary_artifacts = ROOT / "working/v2.7/BINARY_ARTIFACTS.md"
if binary_artifacts.exists():
    text = binary_artifacts.read_text(encoding="utf-8")
    if "tarihsel kanıttır" not in text or "tam 121 kartlık release candidate" not in text:
        ERRORS.append("binary artifact register must distinguish historical proof from current candidate")

qa_plan = ROOT / "working/v2.7/qa/RELEASE_BLOCKER_RESOLUTION_PLAN_v2.7.md"
if qa_plan.exists():
    text = qa_plan.read_text(encoding="utf-8")
    for marker in ("450.000", "1.000.000", "800 kör sınıflandırma", "candidate_commit=C"):
        if marker not in text:
            ERRORS.append(f"QA resolution plan is missing marker: {marker}")

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
