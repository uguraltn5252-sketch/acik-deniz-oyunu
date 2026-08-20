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
    "governance/VISIBLE_CHAT_ACKS_20260820.json",
    "governance/STORY_HANDOFF_20260820.json",
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
        communication = state.get("communication_policy", {})
        acknowledgements = state.get("visible_chat_acknowledgements", {})
        deliveries = state.get("specialist_deliveries", {})
        handoff = state.get("cross_workstream_handoff", {})
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
        if communication.get("official_workstream_credit_requires_named_visible_chat") is not True:
            ERRORS.append("official workstream credit must require the named visible chat")
        if communication.get("github_work_order_is_not_acknowledgement") is not True:
            ERRORS.append("GitHub work orders must not count as visible-chat acknowledgement")
        if communication.get("temporary_subagents_allowed") is not False:
            ERRORS.append("temporary subagents must remain disabled")
        if communication.get("temporary_subagent_exception_requires_prior_project_owner_approval") is not True:
            ERRORS.append("temporary-subagent exceptions require prior project-owner approval")
        if communication.get("temporary_subagent_output_counts_as_official_specialist_delivery") is not False:
            ERRORS.append("temporary-subagent output must not count as specialist delivery")
        if acknowledgements.get("evidence_path") != "governance/VISIBLE_CHAT_ACKS_20260820.json":
            ERRORS.append("visible-chat acknowledgement evidence path is incorrect")
        if acknowledgements.get("scope") != "COMMUNICATION_TEST_ONLY":
            ERRORS.append("visible-chat acknowledgements must remain communication-test only")
        if acknowledgements.get("required") != 3 or acknowledgements.get("acknowledged") != 3:
            ERRORS.append("all three named visible chats must have communication ACK")
        if acknowledgements.get("all_named_chats_acknowledged") is not True:
            ERRORS.append("3/3 named visible-chat acknowledgement must be recorded")
        if acknowledgements.get("chief_editor_disposition") != "ACKNOWLEDGED_COMMUNICATION_TEST_ONLY":
            ERRORS.append("chief-editor ACK disposition must remain communication-only")
        for field in (
            "specialist_delivery_completed",
            "specialist_revalidation_completed",
            "work_branches_created",
        ):
            if acknowledgements.get(field) is not False:
                ERRORS.append(f"{field} must remain false after an ACK-only test")
        if readiness.get("verdict") == "BLOCKER" and readiness.get("lock_allowed") is not False:
            ERRORS.append("BLOCKER readiness must prohibit locking")
        blocker_ids = [item.get("id") for item in blockers if item.get("status") == "OPEN"]
        if len(blocker_ids) != len(set(blocker_ids)):
            ERRORS.append("open blocker ids must be unique")
        if readiness.get("verdict") == "BLOCKER" and not blocker_ids:
            ERRORS.append("BLOCKER readiness must name at least one open blocker")
        if "COM-001" not in blocker_ids:
            ERRORS.append("COM-001 must remain open until all named visible chats revalidate")
        if "CAN-001" in blocker_ids:
            ERRORS.append("CAN-001 must not remain open after Story reclassification")
        if "CAN-001" not in {item.get("id") for item in resolved}:
            ERRORS.append("CAN-001 resolution must be recorded")
        can_resolution = next((item for item in resolved if item.get("id") == "CAN-001"), {})
        if can_resolution.get("official_story_revalidation") != "ACCEPTED":
            ERRORS.append("CAN-001 must record accepted official Story revalidation")
        if can_resolution.get("official_story_revalidation_evidence") != "governance/STORY_HANDOFF_20260820.json":
            ERRORS.append("CAN-001 Story revalidation evidence path is incorrect")
        mechanic = next((item for item in blockers if item.get("id") == "MEC-001"), {})
        if mechanic.get("decision_status") != "APPROVED_FOR_V2.7_DRAFT":
            ERRORS.append("MEC-001 must preserve the approved Sea=Rock v2.7 draft decision")
        communication_blocker = next((item for item in blockers if item.get("id") == "COM-001"), {})
        communication_progress = communication_blocker.get("progress", {})
        if communication_progress.get("visible_chat_acknowledgements") != "COMPLETE_3_OF_3_COMMUNICATION_TEST_ONLY":
            ERRORS.append("COM-001 must record the completed 3/3 communication ACK subgate")
        expected_revalidation = {
            "story": "ACCEPTED",
            "visual": "PENDING",
            "simulation": "PENDING",
        }
        if communication_progress.get("independent_specialist_revalidation") != expected_revalidation:
            ERRORS.append("COM-001 must record accepted Story and pending Visual/Simulation revalidation")
        expected_branches = {
            "story": True,
            "visual": True,
            "simulation": False,
            "completed": 2,
            "required": 3,
        }
        if communication_progress.get("work_branches_created") != expected_branches:
            ERRORS.append("COM-001 must record exactly two of three specialist branches created")
        expected_deliveries = {
            "story": "ACCEPTED",
            "visual": "PENDING",
            "simulation": "PENDING",
        }
        if communication_progress.get("branch_bound_specialist_deliveries") != expected_deliveries:
            ERRORS.append("COM-001 must record accepted Story and pending Visual/Simulation deliveries")
        if handoff.get("story_to_visual") != "ACCEPTED_READY_FOR_VISUAL_INPUT":
            ERRORS.append("story_to_visual must record the accepted Story handoff")
        if handoff.get("story_to_simulation") != "RECORDED_FOR_LATER_EXACT_CANDIDATE_QA":
            ERRORS.append("story_to_simulation must defer testing to exact-candidate QA")
        if handoff.get("visual_to_simulation") != "PENDING_SPECIALIST_DELIVERY":
            ERRORS.append("visual_to_simulation must await the Visual delivery")
        for field in ("simulation_to_story", "simulation_to_visual"):
            if handoff.get(field) != "PENDING_QA_FINDINGS":
                ERRORS.append(f"{field} must remain PENDING_QA_FINDINGS")
        if handoff.get("simulation_to_chief_editor") != "PENDING_SPECIALIST_DELIVERY":
            ERRORS.append("simulation_to_chief_editor must await specialist delivery")
        if handoff.get("communication_acknowledgement") != "COMPLETE_3_OF_3_COMMUNICATION_TEST_ONLY":
            ERRORS.append("cross-workstream state must record the 3/3 communication ACK")
        if handoff.get("final_directives") != "STORY_ACCEPTED_FOR_VISUAL_INPUT_V2_7_REMAINS_BLOCKED":
            ERRORS.append("final directives must accept Story while keeping v2.7 blocked")
        if handoff.get("chief_editor_disposition") != "STORY_ACCEPTED_VISUAL_AND_SIMULATION_DELIVERIES_PENDING":
            ERRORS.append("chief-editor handoff disposition must keep Visual and Simulation pending")
        if handoff.get("source_commit") != acknowledgements.get("source_commit"):
            ERRORS.append("ACK and handoff source commits must match")
        if handoff.get("story_evidence_path") != "governance/STORY_HANDOFF_20260820.json":
            ERRORS.append("cross-workstream state must point to the Story handoff evidence")
        if handoff.get("story_source_commit") != "e04eef7f1fef6ea407feaaf26558551297c44b37":
            ERRORS.append("cross-workstream state has the wrong Story source commit")
        story_delivery = deliveries.get("story", {})
        if story_delivery.get("status") != "ACCEPTED_STORY_WORKSTREAM_PASS_FOR_VISUAL_INPUT":
            ERRORS.append("Story specialist delivery must be accepted for Visual input")
        if story_delivery.get("evidence_path") != "governance/STORY_HANDOFF_20260820.json":
            ERRORS.append("Story specialist delivery evidence path is incorrect")
        if story_delivery.get("source_branch") != "work/v2.7-story":
            ERRORS.append("Story specialist delivery branch is incorrect")
        if story_delivery.get("source_commit") != "e04eef7f1fef6ea407feaaf26558551297c44b37":
            ERRORS.append("Story specialist delivery commit is incorrect")
        if story_delivery.get("integrated_to_v2_7_design") is not False:
            ERRORS.append("Story content must not be claimed integrated before chief-editor integration")
        visual_delivery = deliveries.get("visual", {})
        if visual_delivery.get("status") != "AUTHORIZED_BRANCH_CREATED_PENDING_VISIBLE_CHAT_DELIVERY":
            ERRORS.append("Visual delivery must remain pending after authorized branch creation")
        if visual_delivery.get("branch_created") is not True:
            ERRORS.append("Visual branch creation must be recorded")
        if visual_delivery.get("start_commit") != "e04eef7f1fef6ea407feaaf26558551297c44b37":
            ERRORS.append("Visual branch must start from the accepted Story commit")
        simulation_delivery = deliveries.get("simulation", {})
        if simulation_delivery.get("status") != "PENDING_SPECIALIST_DELIVERY":
            ERRORS.append("Simulation specialist delivery must remain pending")
        if simulation_delivery.get("branch_created") is not False:
            ERRORS.append("Simulation branch must not be claimed before authorized work")
        for role_name, chat_name, branch_name in (
            ("story_editor", "Foulwake Hikâye Editör", "work/v2.7-story"),
            ("visual_design", "FOULWAKE görsel tasarım", "work/v2.7-visual"),
            ("simulation_test", "Simülasyon Testi", "work/v2.7-simulation"),
        ):
            role = roles.get(role_name, {})
            if role.get("official_chat") != chat_name:
                ERRORS.append(f"{role_name} official visible chat is incorrect")
            if role.get("work_branch") != branch_name:
                ERRORS.append(f"{role_name} work branch is incorrect")

ack_path = ROOT / "governance/VISIBLE_CHAT_ACKS_20260820.json"
if ack_path.exists():
    try:
        ack_state = json.loads(ack_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"VISIBLE_CHAT_ACKS_20260820.json is invalid: {exc}")
    else:
        if ack_state.get("record_type") != "VISIBLE_CHAT_COMMUNICATION_TEST":
            ERRORS.append("visible-chat ACK evidence has the wrong record type")
        if ack_state.get("status") != "ACCEPTED_3_OF_3_COMMUNICATION_ONLY":
            ERRORS.append("visible-chat ACK evidence must record 3/3 communication-only acceptance")
        if ack_state.get("chief_editor_disposition") != "ACKNOWLEDGED_COMMUNICATION_TEST_ONLY":
            ERRORS.append("visible-chat evidence has the wrong chief-editor disposition")
        if not re.fullmatch(r"[0-9a-f]{40}", str(ack_state.get("source_commit", ""))):
            ERRORS.append("visible-chat evidence requires an exact source commit")
        for field in (
            "specialist_delivery_completed",
            "specialist_revalidation_completed",
            "work_branches_created",
            "temporary_subagents_used",
        ):
            if ack_state.get(field) is not False:
                ERRORS.append(f"visible-chat evidence field {field} must remain false")
        expected_records = {
            "Foulwake Hikâye Editör": "work/v2.7-story",
            "FOULWAKE görsel tasarım": "work/v2.7-visual",
            "Simülasyon Testi": "work/v2.7-simulation",
        }
        records = ack_state.get("records", [])
        if len(records) != 3:
            ERRORS.append("visible-chat evidence must contain exactly three records")
        records_by_chat = {item.get("visible_chat"): item for item in records}
        if set(records_by_chat) != set(expected_records):
            ERRORS.append("visible-chat evidence must contain the three named official chats")
        for chat_name, branch_name in expected_records.items():
            record = records_by_chat.get(chat_name, {})
            if record.get("visible_chat_ack") is not True:
                ERRORS.append(f"{chat_name} communication ACK is missing")
            if record.get("evidence_type") != "VISIBLE_CHAT_WORKSTREAM":
                ERRORS.append(f"{chat_name} evidence type is incorrect")
            if record.get("assigned_work_branch") != branch_name:
                ERRORS.append(f"{chat_name} assigned work branch is incorrect")
            if record.get("scope") != "COMMUNICATION_TEST_ONLY":
                ERRORS.append(f"{chat_name} ACK must remain communication-test only")
            if record.get("changed_files") != []:
                ERRORS.append(f"{chat_name} communication test must not change files")
            if not record.get("protected_fields_confirmed"):
                ERRORS.append(f"{chat_name} must confirm protected fields")
            if record.get("temporary_subagent_used") is not False:
                ERRORS.append(f"{chat_name} communication test must not use a temporary subagent")
            if record.get("lock_requested") is not False:
                ERRORS.append(f"{chat_name} communication test must not request a lock")

story_handoff_path = ROOT / "governance/STORY_HANDOFF_20260820.json"
if story_handoff_path.exists():
    try:
        story_handoff = json.loads(story_handoff_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"STORY_HANDOFF_20260820.json is invalid: {exc}")
    else:
        if story_handoff.get("record_type") != "VISIBLE_CHAT_STORY_WORKSTREAM_HANDOFF":
            ERRORS.append("Story handoff evidence has the wrong record type")
        if story_handoff.get("status") != "ACCEPTED_STORY_WORKSTREAM_PASS_FOR_VISUAL_INPUT":
            ERRORS.append("Story handoff evidence has the wrong accepted status")
        if story_handoff.get("chief_editor_integration_parent") != "bc148e33343b4066259a996a9c299aab17fd8e3d":
            ERRORS.append("Story handoff evidence has the wrong integration parent")
        delivery = story_handoff.get("story_delivery", {})
        if delivery.get("workstream") != "Hikâye":
            ERRORS.append("Story handoff workstream name is incorrect")
        if delivery.get("visible_chat") != "Foulwake Hikâye Editör":
            ERRORS.append("Story handoff visible chat is incorrect")
        if delivery.get("visible_chat_ack") is not True:
            ERRORS.append("Story handoff requires visible-chat ACK")
        if delivery.get("evidence_type") != "VISIBLE_CHAT_WORKSTREAM":
            ERRORS.append("Story handoff evidence type is incorrect")
        if delivery.get("source_branch") != "work/v2.7-story":
            ERRORS.append("Story handoff source branch is incorrect")
        if delivery.get("source_commit") != "e04eef7f1fef6ea407feaaf26558551297c44b37":
            ERRORS.append("Story handoff source commit is incorrect")
        expected_story_files = [
            "working/v2.7/FOULWAKE_RULEBOOK_STORY_v2.7.md",
            "working/v2.7/FOULWAKE_STORY_FRAMEWORK.md",
            "working/v2.7/FOULWAKE_STORY_REVALIDATION_v2.7.md",
        ]
        if delivery.get("changed_files") != expected_story_files:
            ERRORS.append("Story handoff changed-file scope is incorrect")
        if delivery.get("lock_requested") is not False:
            ERRORS.append("Story handoff must not request a lock")
        if delivery.get("temporary_subagent_used") is not False:
            ERRORS.append("Story handoff must not use a temporary subagent")
        audit = story_handoff.get("chief_editor_audit", {})
        if audit.get("merge_base") != "bc148e33343b4066259a996a9c299aab17fd8e3d":
            ERRORS.append("Story audit merge base is incorrect")
        if audit.get("branch_ahead_by") != 1 or audit.get("branch_behind_by") != 0:
            ERRORS.append("Story audit branch relationship is incorrect")
        if audit.get("protected_paths_changed") != []:
            ERRORS.append("Story audit must record zero protected-path changes")
        expected_blobs = {
            "working/v2.7/FOULWAKE_STORY_FRAMEWORK.md": "962222d83d669763c4ac8e2765f024b9fade180c",
            "working/v2.7/FOULWAKE_RULEBOOK_STORY_v2.7.md": "f1e0eb75434540a85e8b21484acd99ca0abc66cf",
            "working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json": "38a03b71cd3232fd844db8d80d8e53662510b6a3",
            "working/v2.7/FOULWAKE_NARRATIVE_VALIDATION_v2.7.md": "9c27b177fb86be584a4817f38470dc425ac9c0de",
            "working/v2.7/FOULWAKE_STORY_REVALIDATION_v2.7.md": "2b4b4d423c65d5b72f756d322d9b0bd3c8537afa",
        }
        if audit.get("source_blobs") != expected_blobs:
            ERRORS.append("Story audit source blob record is incorrect")
        expected_counts = {"characters": 20, "powers": 30, "unique_ids": 50, "duplicate_ids": 0}
        if audit.get("card_source_counts") != expected_counts:
            ERRORS.append("Story audit card counts are incorrect")
        if audit.get("content_integrated_to_v2_7_design") is not False:
            ERRORS.append("Story evidence must not claim content integration")
        if audit.get("release_pass") is not False or audit.get("lock_allowed") is not False:
            ERRORS.append("Story acceptance must not grant release or lock authority")

project_state = ROOT / "PROJECT_STATE.md"
if project_state.exists():
    text = project_state.read_text(encoding="utf-8")
    for marker in ("v2.6 STABLE / LOCKED", "v2.7 DRAFT / NOT LOCKED"):
        if marker not in text:
            ERRORS.append(f"PROJECT_STATE.md is missing marker: {marker}")
    if "COM-001" not in text or "geçici alt ajan" not in text:
        ERRORS.append("PROJECT_STATE.md must disclose pending visible-chat revalidation")
    if "3/3" not in text or "COMMUNICATION_TEST_ONLY" not in text:
        ERRORS.append("PROJECT_STATE.md must record the communication-only 3/3 ACK")
    for marker in (
        "STORY_HANDOFF_20260820.json",
        "e04eef7f1fef6ea407feaaf26558551297c44b37",
        "Görsel ve Simülasyon teslimleri bekleniyor",
    ):
        if marker not in text:
            ERRORS.append(f"PROJECT_STATE.md is missing Story delivery marker: {marker}")

decision_register = ROOT / "governance/DECISION_REGISTER.md"
if decision_register.exists():
    text = decision_register.read_text(encoding="utf-8")
    for marker in (
        "DEC-20260820-01",
        "DEC-20260820-06",
        "DEC-20260820-07",
        "DEC-20260820-08",
        "Açık Deniz ve Kayalık",
        "APPROVED FOR v2.7 DRAFT",
    ):
        if marker not in text:
            ERRORS.append(f"decision register is missing marker: {marker}")

workstream_protocol = ROOT / "governance/WORKSTREAM_PROTOCOL.md"
if workstream_protocol.exists():
    text = workstream_protocol.read_text(encoding="utf-8")
    for marker in (
        "VISIBLE_CHAT_ACK: YES",
        "EVIDENCE_TYPE: VISIBLE_CHAT_WORKSTREAM",
        "work/v2.7-story",
        "work/v2.7-visual",
        "work/v2.7-simulation",
        "TEMPORARY_SUBAGENT",
    ):
        if marker not in text:
            ERRORS.append(f"workstream protocol is missing marker: {marker}")

coordination_log = ROOT / "governance/COORDINATION_LOG.md"
if coordination_log.exists():
    text = coordination_log.read_text(encoding="utf-8")
    if "KAYIT DÜZELTMESİ / ÖNCEKİ ATIFLARI GEÇERSİZ KILAR" not in text:
        ERRORS.append("coordination log must supersede the incorrect workstream attribution")
    if "3/3 GÖRÜNÜR SOHBET ACK / İLETİŞİM TESTİ" not in text or "COM-001" not in text:
        ERRORS.append("coordination log must record the 3/3 communication ACK and open COM-001")
    for marker in (
        "HİKÂYE WORKSTREAM PASS KABULÜ / GÖRSEL BAŞLANGIÇ",
        "ACCEPTED_STORY_WORKSTREAM_PASS_FOR_VISUAL_INPUT",
        "STORY_HANDOFF_20260820.json",
    ):
        if marker not in text:
            ERRORS.append(f"coordination log is missing Story acceptance marker: {marker}")

assignments = ROOT / "governance/WORKSTREAM_ASSIGNMENTS.md"
if assignments.exists():
    text = assignments.read_text(encoding="utf-8")
    for marker in (
        "ACCEPTED_STORY_WORKSTREAM_PASS / READY_FOR_VISUAL_INPUT",
        "AUTHORIZED_BRANCH_CREATED / PENDING_VISIBLE_CHAT_DELIVERY",
        "ACKNOWLEDGED_COMMUNICATION_TEST_ONLY / PENDING_REAL_DELIVERY",
        "STORY_HANDOFF_20260820.json",
    ):
        if marker not in text:
            ERRORS.append(f"workstream assignments is missing delivery marker: {marker}")

ai_handoff = ROOT / "AI_HANDOFF.md"
if ai_handoff.exists():
    text = ai_handoff.read_text(encoding="utf-8")
    for marker in ("VISIBLE_CHAT_ACKS_20260820.json", "ACKNOWLEDGED_COMMUNICATION_TEST_ONLY", "3/3"):
        if marker not in text:
            ERRORS.append(f"AI_HANDOFF.md is missing ACK marker: {marker}")
    for marker in (
        "STORY_HANDOFF_20260820.json",
        "ACCEPTED_STORY_WORKSTREAM_PASS_FOR_VISUAL_INPUT",
        "e04eef7f1fef6ea407feaaf26558551297c44b37",
    ):
        if marker not in text:
            ERRORS.append(f"AI_HANDOFF.md is missing Story delivery marker: {marker}")

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
    for marker in (
        "RESMÎ SİMÜLASYON TESLİMİ DEĞİLDİR",
        "VISIBLE_CHAT_ACK: YES",
        "450.000",
        "1.000.000",
        "800 kör sınıflandırma",
        "candidate_commit=C",
    ):
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
