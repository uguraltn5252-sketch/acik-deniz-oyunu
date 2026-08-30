#!/usr/bin/env python3
"""FOULWAKE editorial-governance and active-source integrity checks."""

from __future__ import annotations

import json
import hashlib
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def require(path: str) -> Path:
    target = ROOT / path
    if not target.exists():
        error(f"missing required path: {path}")
    return target


def read_text(path: str) -> str:
    target = require(path)
    if not target.is_file():
        return ""
    try:
        return target.read_text(encoding="utf-8")
    except OSError as exc:
        error(f"cannot read {path}: {exc}")
        return ""


def read_json(path: str) -> Any:
    text = read_text(path)
    if not text:
        return {}
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        error(f"invalid JSON {path}: {exc}")
        return {}


def require_markers(path: str, markers: list[str]) -> None:
    text = read_text(path)
    for marker in markers:
        if marker not in text:
            error(f"{path} missing marker: {marker}")


def is_sha(value: Any, length: int = 40) -> bool:
    return bool(re.fullmatch(rf"[0-9a-f]{{{length}}}", str(value or "")))


def git_blob_sha(path: str) -> str:
    data = (ROOT / path).read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


REQUIRED_PATHS = [
    "AI_HANDOFF.md",
    "PROJECT_STATE.md",
    "README.md",
    "CHANGELOG.md",
    ".github/CODEOWNERS",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/foulwake-governance.yml",
    "releases/v2.6",
    "governance/EDITORIAL_CHARTER.md",
    "governance/WORKSTREAM_PROTOCOL.md",
    "governance/RELEASE_GATE.md",
    "governance/ACTIVE_WORKSTREAMS.json",
    "governance/DECISION_REGISTER.md",
    "governance/WORKSTREAM_ASSIGNMENTS.md",
    "governance/COORDINATION_LOG.md",
    "governance/CHIEF_EDITOR_AUDIT_20260825.md",
    "governance/VISIBLE_CHAT_ACKS_20260820.json",
    "governance/STORY_HANDOFF_20260820.json",
    "governance/VISUAL_HANDOFF_20260825.json",
    "governance/ART_DIRECTION_ACK_20260825.json",
    "governance/ART_DIRECTION_HANDOFF_20260825.json",
    "governance/ART_DIRECTION_PILOT_REVIEW_20260825.json",
    "governance/ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json",
    "governance/ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json",
    "governance/VISUAL_LIGHTHOUSE_ONLY_HANDOFF_20260830.json",
    "governance/ART_DIRECTION_LIGHTHOUSE_FINAL_REVIEW_20260830.json",
    "governance/SIM_QA_ATTESTATION_SCHEMA.json",
    "governance/LOCK_AUTHORIZATION_SCHEMA.json",
    "working/v2.7/SOURCE_HIERARCHY_v2.7.json",
    "working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json",
    "working/v2.7/FOULWAKE_NARRATIVE_VALIDATION_v2.7.md",
    "working/v2.7/FOULWAKE_VISUAL_SYSTEM.md",
    "working/v2.7/visual/FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md",
    "working/v2.7/visual/FOULWAKE_PILOT_REWORK_ORDER_v2.7.md",
    "working/v2.7/visual/FOULWAKE_REVISED_PILOT_TARGETED_REWORK_ORDER_v2.7.md",
    "working/v2.7/visual/FOULWAKE_BACK_LIGHTHOUSE_ONLY_REWORK_ORDER_v2.7.md",
    "working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md",
    "working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTION_BIBLE_v2.7.md",
    "working/v2.7/visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json",
    "working/v2.7/visual/art_direction/FOULWAKE_12_PILOT_PRODUCTION_BRIEFS_v2.7.md",
    "working/v2.7/visual/art_direction/FOULWAKE_7_BACK_BRIEFS_v2.7.md",
    "working/v2.7/BINARY_ARTIFACTS.md",
    "working/v2.7/V27_MECHANIC_DECISIONS.json",
    "working/v2.7/qa/RELEASE_BLOCKER_RESOLUTION_PLAN_v2.7.md",
]
for required_path in REQUIRED_PATHS:
    require(required_path)


# Parse every active/governance JSON so malformed evidence cannot hide behind
# marker checks.
for directory in (ROOT / "governance", ROOT / "working/v2.7"):
    if directory.exists():
        for path in sorted(directory.rglob("*.json")):
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                error(f"invalid JSON {path.relative_to(ROOT)}: {exc}")


# Locked v2.6 manifest and immutable working-copy guard.
manifest = read_json("releases/v2.6/V26_RELEASE_MANIFEST.json")
if manifest.get("version") != "v2.6" or manifest.get("status") != "STABLE / LOCKED":
    error("v2.6 manifest must remain STABLE / LOCKED")
if manifest.get("release_lock") is not True or manifest.get("user_approved_lock") is not True:
    error("v2.6 manifest lost its lock authorization")
expected_v26_hashes = {
    "rulebook": "192f790d89e987a312d6a36879e7b063ee13426c9508b4e474f16f2cad723c2a",
    "cards": "769eaadf989b3d7e4b35ca00d62b0505bcafd7dc61174a11314b607887de9298",
    "zip": "ffc9c17c725e6093c62a3ebddc5f19c36fb0647f6a51a3e7014852fe0623d534",
}
for key, expected in expected_v26_hashes.items():
    actual = manifest.get("artifacts", {}).get(key, {}).get("sha256")
    if actual != expected:
        error(f"v2.6 {key} artifact hash changed")

release_v26 = ROOT / "releases/v2.6"
working_v27 = ROOT / "working/v2.7"
if release_v26.exists() and working_v27.exists():
    for source in release_v26.iterdir():
        if not source.is_file() or source.name == "BINARY_ARTIFACTS.md":
            continue
        mirror = working_v27 / source.name
        if not mirror.is_file():
            error(f"missing v2.6 working mirror: working/v2.7/{source.name}")
        elif source.read_bytes() != mirror.read_bytes():
            error(f"v2.6 working mirror drift: working/v2.7/{source.name}")


# Current state and specialist evidence.
state = read_json("governance/ACTIVE_WORKSTREAMS.json")
if state.get("schema_version") != 2:
    error("ACTIVE_WORKSTREAMS schema_version must be 2")
locked = state.get("locked_release", {})
if locked != {"version": "v2.6", "status": "STABLE_LOCKED", "path": "releases/v2.6", "mutable": False}:
    error("ACTIVE_WORKSTREAMS locked_release contract changed")
readiness = state.get("release_readiness", {})
if readiness.get("verdict") != "BLOCKER" or readiness.get("lock_allowed") is not False:
    error("v2.7 must remain BLOCKER with lock_allowed=false")
if readiness.get("active_visual_candidate") is not None:
    error("no active visual candidate may be claimed during art rework")

roles = state.get("roles", {})
art_direction_role = roles.get("art_direction", {})
if art_direction_role.get("official_chat") != "FOULWAKE Sanat Yönetmeni":
    error("Art Direction official visible chat is wrong")
if art_direction_role.get("work_branch") != "work/v2.7-art-direction":
    error("Art Direction work branch is wrong")
if art_direction_role.get("write_scope") != "working/v2.7/visual/art_direction/**":
    error("Art Direction write scope is wrong")
if art_direction_role.get("may_produce_final_art") is not False:
    error("Art Direction cannot own final art production")
if art_direction_role.get("final_aesthetic_authority") != "project_owner":
    error("final aesthetic authority must remain with project owner")
activation = state.get("art_direction_activation", {})
if activation.get("status") != "ACKNOWLEDGED_COMMUNICATION_TEST_ONLY_READY_FOR_CREATIVE_WORK":
    error("Art Direction communication ACK activation status is wrong")
if activation.get("branch_created") is not True:
    error("Art Direction branch activation must be recorded")
if activation.get("temporary_subagents_used") is not False:
    error("Art Direction activation cannot use temporary subagents")
if activation.get("source_commit") != "3f50cdbf1abf43b929bfdb4564055c9c63f79f21":
    error("Art Direction activation source commit is wrong")
if activation.get("ack_evidence_path") != "governance/ART_DIRECTION_ACK_20260825.json":
    error("Art Direction activation evidence path is wrong")
if activation.get("creative_work_authorized") is not True:
    error("Art Direction creative work must be authorized after accepted ACK")

deliveries = state.get("specialist_deliveries", {})
story = deliveries.get("story", {})
art_direction = deliveries.get("art_direction", {})
if art_direction.get("status") != "PILOT_ART_DIRECTION_PASS_PENDING_PROJECT_OWNER_AND_CHIEF_EDITOR_ACCEPTANCE":
    error("Art Direction status must record pilot Art Direction PASS pending owner/Chief acceptance")
if art_direction.get("work_branch") != "work/v2.7-art-direction":
    error("Art Direction delivery branch is wrong")
if art_direction.get("may_start_creative_work") is not True:
    error("Art Direction creative work must remain enabled")
if art_direction.get("delivery_recorded") is not True:
    error("accepted Art Direction brief delivery must be recorded")
if art_direction.get("communication_ack_recorded") is not True:
    error("Art Direction communication ACK must remain recorded")
if art_direction.get("ack_evidence_path") != "governance/ART_DIRECTION_ACK_20260825.json":
    error("Art Direction ACK evidence path is wrong")
if art_direction.get("evidence_path") != "governance/ART_DIRECTION_HANDOFF_20260825.json":
    error("Art Direction accepted handoff evidence path is wrong")
if art_direction.get("source_commit") != "7418d9c2c89c265cb6efd30f6a5a7f2addd528da":
    error("Art Direction accepted source commit is wrong")
if art_direction.get("integrated_to_v2_7_design") is not True:
    error("accepted Art Direction package must be integrated")
if art_direction.get("project_owner_final_approval") is not True or art_direction.get("art_direction_brief_pass") is not True:
    error("Art Direction brief requires project-owner and Chief Editor acceptance")
if story.get("status") != "ACCEPTED_STORY_WORKSTREAM_PASS_FOR_VISUAL_INPUT":
    error("Story delivery acceptance is missing")
if story.get("source_commit") != "e04eef7f1fef6ea407feaaf26558551297c44b37":
    error("Story delivery exact commit is wrong")
if story.get("integrated_to_v2_7_design") is not True:
    error("accepted Story blobs must be recorded as integrated")
visual = deliveries.get("visual", {})
if visual.get("status") != "PILOT_ART_DIRECTION_PASS_RECORDED_PRODUCTION_PAUSED":
    error("Visual status must record Art Direction PASS with production paused")
if visual.get("source_commit") != "e91581bb336dfcbab5da1d48a256577f9251f891":
    error("Visual delivery exact head is wrong")
if visual.get("full_production_delivery_commit") != "494b8440bba722a9053f72b2fdeffc4286a61e17":
    error("Visual full-production commit is wrong")
if visual.get("art_accepted") is not False or visual.get("active_candidate") is not False:
    error("Rejected Visual art must not become an active candidate")
if visual.get("observed_pilot_commit") != "b4afbcf49784b85338453cbf29a956cbb620c9e6":
    error("observed pre-brief Visual pilot commit is wrong")
if visual.get("observed_pilot_classification") != "PRE_BRIEF_PILOT_REVIEWED_REWORK_REQUIRED_INPUT_ONLY":
    error("pre-brief Visual pilot must remain reviewed rework input only")
if visual.get("observed_pilot_visible_chat_handoff_received") is not False:
    error("GitHub pilot cannot count as visible-chat handoff")
if visual.get("observed_pilot_art_accepted") is not False:
    error("pre-brief Visual pilot cannot be art-accepted")
if visual.get("pilot_only_production_authorized") is not True or visual.get("full_production_authorized") is not False:
    error("Visual authorization must remain pilot-only")
if visual.get("art_direction_review_received") is not True or visual.get("art_direction_review_result") != "REWORK_REQUIRED":
    error("Visual pilot must record the exact Art Direction REWORK_REQUIRED review")
if visual.get("art_direction_review_evidence") != "governance/ART_DIRECTION_PILOT_REVIEW_20260825.json":
    error("Visual pilot Art Direction review evidence path is wrong")
expected_next_pilot = ["KAR-01", "KAR-06", "KAR-19", "GUC-06", "GUC-27", "ERZ-01", "SAD-H-03", "HAR-AD-08", "HAR-KY-06", "HAR-AA-06", "HAR-FN-04", "SET-KP-01"]
if visual.get("next_pilot_front_ids") != expected_next_pilot:
    error("next Visual pilot must use the accepted 12 hard-case card set")
if visual.get("next_pilot_exact_reuse") != expected_next_pilot:
    error("lighthouse-only rework must preserve all twelve pilot fronts")
revised_review = state.get("revised_art_direction_pilot_review", {})
if revised_review.get("status") != "REWORK_REQUIRED_ACCEPTED_FOR_TARGETED_PILOT_REWORK":
    error("revised Art Direction review disposition is missing")
if revised_review.get("evidence_path") != "governance/ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json":
    error("revised Art Direction review evidence path is wrong")
if revised_review.get("input_visual_commit") != "1b27232a53b09ac3ff00030f625bfc2703d15764" or revised_review.get("exact_visual_files_opened") != 40:
    error("revised Art Direction exact input/count is wrong")
if revised_review.get("front_counts") != {"keep": 10, "rework_required": 2}:
    error("revised front counts must be 10 KEEP / 2 REWORK")
if revised_review.get("back_counts") != {"keep": 5, "rework_required": 2}:
    error("revised back counts must be 5 KEEP / 2 REWORK")
if revised_review.get("rework_front_ids") != ["KAR-01", "HAR-AA-06"]:
    error("revised front rework set is wrong")
if revised_review.get("rework_back_ids") != ["BACK_ISLAND", "BACK_LIGHTHOUSE"]:
    error("revised back rework set is wrong")
if revised_review.get("authorized_changed_files_exact") != 25:
    error("targeted rework changed-file budget must be 25")
if visual.get("targeted_rework_order") != "working/v2.7/visual/FOULWAKE_BACK_LIGHTHOUSE_ONLY_REWORK_ORDER_v2.7.md":
    error("Visual lighthouse-only rework order path is wrong")
if visual.get("new_visual_production_authorized") is not False or visual.get("rework_authorized") is not False:
    error("Visual production must pause after lighthouse-only handoff")
if visual.get("lighthouse_only_authorization_consumed") is not True:
    error("lighthouse-only authorization must be recorded as consumed")
if visual.get("full_production_authorized") is not False:
    error("full production must remain unauthorized")
if visual.get("targeted_rework_front_ids") != []:
    error("lighthouse-only rework cannot change pilot fronts")
if visual.get("targeted_rework_back_ids") != ["BACK_LIGHTHOUSE"]:
    error("Visual lighthouse-only back set is wrong")
if visual.get("authorized_changed_files_exact") != 15:
    error("Visual lighthouse-only changed-file budget is wrong")
if visual.get("current_workstream_branch_head") != "23c062f6de06c32eab224b3440c8474725d4fe9e":
    error("Visual current branch head is wrong")
if visual.get("lighthouse_only_canonical_delivery_commit") != "c8081aa9f781737b0d7e14c8b224bf1fd988e8bb":
    error("lighthouse-only canonical delivery commit is wrong")
if visual.get("lighthouse_only_evidence_commit") != "23c062f6de06c32eab224b3440c8474725d4fe9e":
    error("lighthouse-only evidence commit is wrong")
if visual.get("lighthouse_only_handoff_evidence") != "governance/VISUAL_LIGHTHOUSE_ONLY_HANDOFF_20260830.json":
    error("lighthouse-only handoff evidence path is wrong")
if visual.get("lighthouse_only_changed_files_exact") != 15:
    error("lighthouse-only delivered changed-file count is wrong")
if visual.get("targeted_four_master_delivery_commit") != "88907294edd326c118573f5ada7406e5fc42ee4d":
    error("targeted four-master canonical delivery commit is wrong")
if visual.get("byte_exact_keep_main_assets") != 18 or visual.get("byte_exact_keep_source_art") != 16:
    error("lighthouse-only main/source KEEP counts are wrong")
if visual.get("byte_exact_keep_sketch_gates") != 10 or visual.get("byte_exact_keep_unaffected_contact_sheets") != 3:
    error("lighthouse-only gate/contact KEEP counts are wrong")

lighthouse_review = state.get("art_direction_lighthouse_review", {})
if lighthouse_review.get("status") != "BACK_LIGHTHOUSE_ONLY_REWORK_REQUIRED_ACCEPTED":
    error("lighthouse-only Art Direction disposition is missing")
if lighthouse_review.get("evidence_path") != "governance/ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json":
    error("lighthouse-only review evidence path is wrong")
if lighthouse_review.get("input_visual_commit") != "0cb2bd6f03e2d84948741c162f22b8fd2ff064ad":
    error("lighthouse-only reviewed Visual commit is wrong")
if lighthouse_review.get("canonical_visual_delivery_commit") != "88907294edd326c118573f5ada7406e5fc42ee4d":
    error("lighthouse-only canonical delivery commit is wrong")
if lighthouse_review.get("accepted_new_keep_assets") != ["KAR-01", "HAR-AA-06", "BACK_ISLAND"]:
    error("three newly accepted assets are wrong")
if lighthouse_review.get("rework_back_ids") != ["BACK_LIGHTHOUSE"]:
    error("only BACK_LIGHTHOUSE may remain in rework")
if lighthouse_review.get("main_asset_counts") != {"keep": 18, "rework_required": 1}:
    error("main asset counts must be 18 KEEP / 1 REWORK")
if lighthouse_review.get("authorized_changed_files_exact") != 15:
    error("lighthouse-only authorization must be 15 files")
if lighthouse_review.get("full_121_production_authorized") is not False or lighthouse_review.get("simulation_authorized") is not False:
    error("lighthouse review cannot grant full production or Simulation")

visual_lighthouse_handoff = state.get("visual_lighthouse_handoff", {})
if visual_lighthouse_handoff.get("status") != "VISUAL_LIGHTHOUSE_ONLY_HANDOFF_ACCEPTED_FOR_EXACT_ART_DIRECTION_REVIEW":
    error("visual lighthouse handoff state is missing")
if visual_lighthouse_handoff.get("evidence_path") != "governance/VISUAL_LIGHTHOUSE_ONLY_HANDOFF_20260830.json":
    error("visual lighthouse handoff state evidence path is wrong")
if visual_lighthouse_handoff.get("source_commit") != "23c062f6de06c32eab224b3440c8474725d4fe9e":
    error("visual lighthouse handoff source commit is wrong")
if visual_lighthouse_handoff.get("canonical_delivery_commit") != "c8081aa9f781737b0d7e14c8b224bf1fd988e8bb":
    error("visual lighthouse handoff canonical delivery is wrong")
if visual_lighthouse_handoff.get("input_visual_commit") != "0cb2bd6f03e2d84948741c162f22b8fd2ff064ad":
    error("visual lighthouse handoff input commit is wrong")
if visual_lighthouse_handoff.get("changed_files_exact") != 15:
    error("visual lighthouse handoff changed-file count is wrong")
if visual_lighthouse_handoff.get("technical_handoff_accepted") is not True or visual_lighthouse_handoff.get("aesthetic_accepted") is not False:
    error("visual lighthouse handoff acceptance boundary is wrong")
if visual_lighthouse_handoff.get("art_direction_review_authorized") is not True or visual_lighthouse_handoff.get("visual_production_authorized") is not False:
    error("visual lighthouse handoff next-stage authorization is wrong")
if visual_lighthouse_handoff.get("full_121_production_authorized") is not False or visual_lighthouse_handoff.get("simulation_authorized") is not False:
    error("visual lighthouse handoff cannot grant full production or Simulation")

final_lighthouse_review = state.get("art_direction_lighthouse_final_review", {})
if final_lighthouse_review.get("status") != "PILOT_ART_DIRECTION_PASS_PENDING_PROJECT_OWNER_AND_CHIEF_EDITOR_ACCEPTANCE":
    error("final lighthouse Art Direction review state is missing")
if final_lighthouse_review.get("evidence_path") != "governance/ART_DIRECTION_LIGHTHOUSE_FINAL_REVIEW_20260830.json":
    error("final lighthouse Art Direction evidence path is wrong")
if final_lighthouse_review.get("source_commit") != "7418d9c2c89c265cb6efd30f6a5a7f2addd528da":
    error("final lighthouse Art Direction source commit is wrong")
if final_lighthouse_review.get("input_visual_commit") != "23c062f6de06c32eab224b3440c8474725d4fe9e":
    error("final lighthouse reviewed Visual commit is wrong")
if final_lighthouse_review.get("canonical_visual_delivery_commit") != "c8081aa9f781737b0d7e14c8b224bf1fd988e8bb":
    error("final lighthouse canonical Visual delivery commit is wrong")
if final_lighthouse_review.get("exact_visuals_opened") != 9 or final_lighthouse_review.get("back_lighthouse_disposition") != "KEEP":
    error("final lighthouse review must record 9 visuals and KEEP")
if final_lighthouse_review.get("front_counts") != {"keep": 12, "rework_required": 0}:
    error("final pilot fronts must be 12 KEEP / 0 REWORK")
if final_lighthouse_review.get("back_counts") != {"keep": 7, "rework_required": 0}:
    error("final pilot backs must be 7 KEEP / 0 REWORK")
if final_lighthouse_review.get("art_direction_gate_passed") is not True:
    error("final lighthouse Art Direction gate must be passed")
if final_lighthouse_review.get("project_owner_final_aesthetic_acceptance") is not False or final_lighthouse_review.get("chief_editor_pilot_art_acceptance") is not False:
    error("final lighthouse review cannot pre-approve owner or Chief pilot acceptance")
if final_lighthouse_review.get("active_visual_candidate") is not False or final_lighthouse_review.get("visual_production_authorized") is not False:
    error("final lighthouse review cannot activate candidate or Visual production")
if final_lighthouse_review.get("full_121_production_authorized") is not False or final_lighthouse_review.get("simulation_authorized") is not False:
    error("final lighthouse review cannot authorize full production or Simulation")

simulation = deliveries.get("simulation", {})
if simulation.get("status") != "PENDING_PROJECT_OWNER_AND_CHIEF_EDITOR_PILOT_ACCEPTANCE":
    error("Simulation must wait for project-owner and Chief Editor pilot acceptance")
if simulation.get("branch_created") is not False or simulation.get("may_start") is not False:
    error("Simulation branch/start must remain false")

blockers = {item.get("id"): item for item in state.get("open_blockers", [])}
required_blockers = {"MEC-001", "SRC-001", "SRC-002", "ART-001", "QA-001", "QA-002", "GOV-001", "COM-001"}
if set(blockers) != required_blockers:
    error(f"open blocker set mismatch: {sorted(blockers)}")
for blocker_id in required_blockers:
    if blockers.get(blocker_id, {}).get("severity") != "BLOCKER":
        error(f"{blocker_id} must remain BLOCKER")
if blockers.get("SRC-002", {}).get("must_not_be_silently_fixed") is not True:
    error("SRC-002 must prohibit silent identity fixes")

backs = state.get("visual_rework_contract", {}).get("back_mapping", {})
expected_backs = {
    "BACK_CHARACTER": 20,
    "BACK_POWER": 31,
    "BACK_LOYALTY": 15,
    "BACK_SEA_ROCK": 42,
    "BACK_ISLAND": 6,
    "BACK_LIGHTHOUSE": 4,
    "BACK_SUPPORT": 3,
}
if backs != expected_backs or sum(backs.values()) != 121:
    error("back mapping must be exact 7-family / 121-card topology")
contract = state.get("visual_rework_contract", {})
if contract.get("fronts_required") != 121:
    error("visual rework must require 121 fronts")
if contract.get("unique_hash_counts_as_unique_art") is not False:
    error("unique hash must not count as unique artwork")
if contract.get("text_in_illustration") != "FORBIDDEN":
    error("text in illustration must be forbidden")
if contract.get("art_direction_review_required") is not True:
    error("visual rework must require independent Art Direction review")
if contract.get("art_direction_work_order") != "working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md":
    error("visual rework Art Direction work order path is wrong")
if contract.get("art_direction_recommendation_is_release_pass") is not False:
    error("Art Direction recommendation cannot count as release PASS")


art_ack = read_json("governance/ART_DIRECTION_ACK_20260825.json")
if art_ack.get("record_type") != "VISIBLE_CHAT_ART_DIRECTION_COMMUNICATION_TEST_AND_CHIEF_EDITOR_DISPOSITION":
    error("Art Direction ACK record type is wrong")
if art_ack.get("status") != "ACKNOWLEDGED_COMMUNICATION_TEST_ONLY_READY_FOR_FIRST_CREATIVE_ASSIGNMENT":
    error("Art Direction ACK status is wrong")
art_ack_delivery = art_ack.get("art_direction_ack", {})
if art_ack_delivery.get("visible_chat") != "FOULWAKE Sanat Yönetmeni" or art_ack_delivery.get("visible_chat_ack") is not True:
    error("Art Direction ACK requires correct visible chat")
if art_ack_delivery.get("source_branch") != "work/v2.7-art-direction" or art_ack_delivery.get("source_commit") != "3f50cdbf1abf43b929bfdb4564055c9c63f79f21":
    error("Art Direction ACK branch/commit mismatch")
if art_ack_delivery.get("changed_files") != []:
    error("Art Direction communication test must not change files")
if art_ack_delivery.get("temporary_subagent_used") is not False or art_ack_delivery.get("lock_requested") is not False:
    error("Art Direction communication test cannot use temporary agents or request lock")
art_ack_disposition = art_ack.get("chief_editor_disposition", {})
if art_ack_disposition.get("communication_test") != "ACCEPTED" or art_ack_disposition.get("creative_work_authorized") is not True:
    error("Art Direction ACK Chief Editor disposition is wrong")
if art_ack_disposition.get("specialist_creative_delivery_completed") is not False:
    error("Communication ACK cannot complete creative Art Direction delivery")
if art_ack_disposition.get("release_pass") is not False or art_ack_disposition.get("lock_allowed") is not False:
    error("Art Direction ACK cannot grant release or lock")

art_handoff = read_json("governance/ART_DIRECTION_HANDOFF_20260825.json")
if art_handoff.get("record_type") != "VISIBLE_CHAT_ART_DIRECTION_BRIEF_HANDOFF_AND_CHIEF_EDITOR_DISPOSITION":
    error("Art Direction handoff record type is wrong")
if art_handoff.get("status") != "ART_DIRECTION_BRIEF_ACCEPTED_PILOT_ONLY_AUTHORIZED":
    error("Art Direction handoff status is wrong")
art_delivery = art_handoff.get("art_direction_delivery", {})
if art_delivery.get("visible_chat") != "FOULWAKE Sanat Yönetmeni" or art_delivery.get("visible_chat_ack") is not True:
    error("Art Direction handoff requires correct visible chat ACK")
if art_delivery.get("source_branch") != "work/v2.7-art-direction" or art_delivery.get("source_commit") != "7418d9c2c89c265cb6efd30f6a5a7f2addd528da":
    error("Art Direction accepted branch/commit mismatch")
if art_delivery.get("temporary_subagent_used") is not False or art_delivery.get("lock_requested") is not False:
    error("Art Direction accepted delivery cannot use temporary agents or request lock")
if art_delivery.get("source_risk") != "SRC-002":
    error("Art Direction handoff must preserve SRC-002")
owner_decision = art_handoff.get("project_owner_decision", {})
if owner_decision.get("decision") != "OPTION_2 — FAMILY-VISIBLE MAP BACKS" or owner_decision.get("final_rework_approved") is not True:
    error("project-owner family-visible map-back approval is missing")
art_disposition = art_handoff.get("chief_editor_disposition", {})
if art_disposition.get("art_direction_brief_pass") != "GRANTED":
    error("Chief Editor Art Direction brief PASS is missing")
if art_disposition.get("visual_production_authorized") != "PILOT_ONLY" or art_disposition.get("full_121_production_authorized") is not False:
    error("Art Direction acceptance may authorize pilot only")
if art_disposition.get("simulation_may_start") is not False or art_disposition.get("release_pass") is not False or art_disposition.get("lock_allowed") is not False:
    error("Art Direction brief acceptance cannot grant Simulation, release or lock")
observed_pilot = art_handoff.get("observed_visual_pilot", {})
if observed_pilot.get("source_commit") != "b4afbcf49784b85338453cbf29a956cbb620c9e6":
    error("Art Direction handoff observed Visual pilot commit is wrong")
if observed_pilot.get("visible_chat_handoff_received") is not False or observed_pilot.get("art_accepted") is not False:
    error("observed pre-brief Visual pilot cannot count as handoff or accepted art")
if observed_pilot.get("classification") != "PRE_BRIEF_IN_FLIGHT_PILOT_REVIEW_INPUT_ONLY":
    error("observed Visual pilot classification is wrong")


art_review = read_json("governance/ART_DIRECTION_PILOT_REVIEW_20260825.json")
if art_review.get("record_type") != "VISIBLE_CHAT_ART_DIRECTION_EXACT_PILOT_REVIEW_AND_CHIEF_EDITOR_DISPOSITION":
    error("Art Direction pilot review record type is wrong")
if art_review.get("status") != "REWORK_REQUIRED_ACCEPTED_FOR_PILOT_REWORK":
    error("Art Direction pilot review status is wrong")
review_delivery = art_review.get("art_direction_review", {})
if review_delivery.get("visible_chat") != "FOULWAKE Sanat Yönetmeni" or review_delivery.get("visible_chat_ack") is not True:
    error("Art Direction pilot review requires the correct visible chat ACK")
if review_delivery.get("evidence_type") != "EXACT_VISUAL_PILOT_REVIEW":
    error("Art Direction pilot review evidence type is wrong")
if review_delivery.get("input_visual_branch") != "work/v2.7-visual" or review_delivery.get("input_visual_commit") != "b4afbcf49784b85338453cbf29a956cbb620c9e6":
    error("Art Direction pilot review exact Visual input is wrong")
if review_delivery.get("changed_files") != [] or review_delivery.get("temporary_subagents") != []:
    error("Art Direction exact pilot review must be read-only and use no temporary subagents")
if review_delivery.get("lock_requested") is not False or review_delivery.get("art_direction_pilot_pass_recommendation") is not False:
    error("Rejected pilot review cannot request lock or recommend PASS")
front_totals = art_review.get("front_disposition", {}).get("totals", {})
back_totals = art_review.get("back_disposition", {}).get("totals", {})
if front_totals != {"keep": 3, "rework_required": 9}:
    error("Art Direction front review counts must be 3 KEEP / 9 REWORK")
if back_totals != {"keep": 0, "rework_required": 7}:
    error("Art Direction back review counts must be 0 KEEP / 7 REWORK")
review_disposition = art_review.get("chief_editor_disposition", {})
if review_disposition.get("reviewed_pilot_accepted") is not False:
    error("reviewed b4afbcf pilot cannot be accepted")
if review_disposition.get("visual_production_authorized") != "PILOT_ONLY" or review_disposition.get("full_121_production_authorized") is not False:
    error("pilot review disposition must remain pilot-only")
if review_disposition.get("next_pilot_front_ids") != expected_next_pilot:
    error("pilot review disposition must route the accepted 12 hard-case cards")
if review_disposition.get("exact_reuse_from_reviewed_pilot") != ["SAD-H-03", "HAR-KY-06"]:
    error("pilot review exact KEEP reuse set is wrong")
if review_disposition.get("redraw_all_back_ids") != ["BACK_CHARACTER", "BACK_POWER", "BACK_LOYALTY", "BACK_SEA_ROCK", "BACK_ISLAND", "BACK_LIGHTHOUSE", "BACK_SUPPORT"]:
    error("all seven pilot backs must be redrawn")
if review_disposition.get("simulation_may_start") is not False or review_disposition.get("release_pass") is not False or review_disposition.get("lock_allowed") is not False:
    error("pilot review cannot grant Simulation, release or lock")

revised_art_review = read_json("governance/ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json")
if revised_art_review.get("record_type") != "VISIBLE_CHAT_ART_DIRECTION_REVISED_EXACT_PILOT_REVIEW_AND_CHIEF_EDITOR_DISPOSITION":
    error("revised Art Direction review record type is wrong")
if revised_art_review.get("status") != "REVISED_PILOT_REWORK_REQUIRED_ACCEPTED_FOR_TARGETED_REWORK":
    error("revised Art Direction review status is wrong")
revised_delivery = revised_art_review.get("art_direction_review", {})
if revised_delivery.get("visible_chat") != "FOULWAKE Sanat Yönetmeni" or revised_delivery.get("visible_chat_ack") is not True:
    error("revised Art Direction review requires correct visible chat ACK")
if revised_delivery.get("evidence_type") != "VISIBLE_CHAT_WORKSTREAM" or revised_delivery.get("review_evidence_type") != "EXACT_VISUAL_PILOT_REVIEW":
    error("revised Art Direction evidence types are wrong")
if revised_delivery.get("source_commit") != "7418d9c2c89c265cb6efd30f6a5a7f2addd528da" or revised_delivery.get("input_visual_commit") != "1b27232a53b09ac3ff00030f625bfc2703d15764":
    error("revised Art Direction exact source chain is wrong")
if revised_delivery.get("changed_files") != [] or revised_delivery.get("temporary_subagents") != []:
    error("revised Art Direction review must be read-only and use no temporary subagents")
if revised_delivery.get("scope", {}).get("exact_visual_files_opened") != 40:
    error("revised Art Direction review must open 40/40 exact visuals")
if revised_art_review.get("front_disposition", {}).get("totals") != {"keep": 10, "rework_required": 2}:
    error("revised Art Direction front disposition is wrong")
if revised_art_review.get("back_disposition", {}).get("totals") != {"keep": 5, "rework_required": 2}:
    error("revised Art Direction back disposition is wrong")
revised_disposition = revised_art_review.get("chief_editor_disposition", {})
if revised_disposition.get("visual_production_authorized") != "TARGETED_PILOT_REWORK_ONLY":
    error("Chief Editor must authorize only targeted pilot rework")
if revised_disposition.get("authorized_changed_files_exact") != 25:
    error("Chief Editor targeted file budget is wrong")
if revised_disposition.get("full_121_production_authorized") is not False or revised_disposition.get("simulation_may_start") is not False:
    error("revised review cannot grant full production or Simulation")
if revised_disposition.get("release_pass") is not False or revised_disposition.get("lock_allowed") is not False:
    error("revised review cannot grant release or lock")

lighthouse_art_review = read_json("governance/ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json")
if lighthouse_art_review.get("record_type") != "VISIBLE_CHAT_ART_DIRECTION_TARGETED_PILOT_ACCEPTANCE_REVIEW_AND_CHIEF_EDITOR_DISPOSITION":
    error("lighthouse-only review record type is wrong")
if lighthouse_art_review.get("status") != "BACK_LIGHTHOUSE_ONLY_REWORK_REQUIRED_ACCEPTED_FOR_FINAL_TARGETED_REWORK":
    error("lighthouse-only review status is wrong")
lighthouse_delivery = lighthouse_art_review.get("art_direction_review", {})
if lighthouse_delivery.get("visible_chat") != "FOULWAKE Sanat Yönetmeni" or lighthouse_delivery.get("visible_chat_ack") is not True:
    error("lighthouse-only review requires correct visible chat ACK")
if lighthouse_delivery.get("evidence_type") != "VISIBLE_CHAT_WORKSTREAM" or lighthouse_delivery.get("review_evidence_type") != "EXACT_VISUAL_PILOT_REVIEW":
    error("lighthouse-only review evidence types are wrong")
if lighthouse_delivery.get("input_visual_commit") != "0cb2bd6f03e2d84948741c162f22b8fd2ff064ad":
    error("lighthouse-only review input commit is wrong")
if lighthouse_delivery.get("canonical_visual_delivery_commit") != "88907294edd326c118573f5ada7406e5fc42ee4d":
    error("lighthouse-only canonical delivery is wrong")
if lighthouse_delivery.get("changed_files") != [] or lighthouse_delivery.get("temporary_subagents") != []:
    error("lighthouse-only Art Direction review must be read-only and use no temporary subagents")
chain = lighthouse_art_review.get("exact_chain_verification", {})
if chain.get("changed_files_from_prior_visual_input") != 25 or chain.get("main_keep_assets_byte_exact") != 15:
    error("reviewed 25-file targeted chain is wrong")
if chain.get("protected_sketch_gates_byte_exact") != 9 or chain.get("full_121_production_started") is not False:
    error("reviewed gate/full-production scope is wrong")
lighthouse_disposition = lighthouse_art_review.get("chief_editor_disposition", {})
if lighthouse_disposition.get("visual_production_authorized") != "BACK_LIGHTHOUSE_ONLY_PILOT_REWORK":
    error("Chief Editor must authorize lighthouse-only rework")
if lighthouse_disposition.get("authorized_changed_files_exact") != 15:
    error("Chief Editor lighthouse-only file budget is wrong")
if lighthouse_disposition.get("byte_exact_main_assets_required") != 18 or lighthouse_disposition.get("byte_exact_sketch_gates_required") != 10:
    error("Chief Editor lighthouse-only KEEP requirements are wrong")
if lighthouse_disposition.get("full_121_production_authorized") is not False or lighthouse_disposition.get("simulation_may_start") is not False:
    error("lighthouse-only review cannot grant full production or Simulation")
if lighthouse_disposition.get("release_pass") is not False or lighthouse_disposition.get("lock_allowed") is not False:
    error("lighthouse-only review cannot grant release or lock")

visual_lighthouse_evidence = read_json("governance/VISUAL_LIGHTHOUSE_ONLY_HANDOFF_20260830.json")
if visual_lighthouse_evidence.get("record_type") != "VISIBLE_CHAT_VISUAL_LIGHTHOUSE_ONLY_HANDOFF":
    error("visual lighthouse handoff record type is wrong")
visual_lighthouse_delivery = visual_lighthouse_evidence.get("visual_handoff", {})
if visual_lighthouse_delivery.get("visible_chat") != "FOULWAKE Görsel Tasarım 2" or visual_lighthouse_delivery.get("visible_chat_ack") is not True:
    error("visual lighthouse handoff requires correct visible chat ACK")
if visual_lighthouse_delivery.get("evidence_type") != "VISIBLE_CHAT_WORKSTREAM":
    error("visual lighthouse handoff evidence type is wrong")
if visual_lighthouse_delivery.get("source_branch") != "work/v2.7-visual":
    error("visual lighthouse handoff branch is wrong")
if visual_lighthouse_delivery.get("source_commit") != "23c062f6de06c32eab224b3440c8474725d4fe9e":
    error("visual lighthouse handoff source commit is wrong")
if visual_lighthouse_delivery.get("canonical_delivery_commit") != "c8081aa9f781737b0d7e14c8b224bf1fd988e8bb":
    error("visual lighthouse handoff canonical delivery is wrong")
if visual_lighthouse_delivery.get("evidence_commit") != "23c062f6de06c32eab224b3440c8474725d4fe9e":
    error("visual lighthouse handoff evidence commit is wrong")
if visual_lighthouse_delivery.get("input_visual_commit") != "0cb2bd6f03e2d84948741c162f22b8fd2ff064ad":
    error("visual lighthouse handoff input commit is wrong")
if visual_lighthouse_delivery.get("changed_files_exact") != 15:
    error("visual lighthouse handoff file count is wrong")
if visual_lighthouse_delivery.get("temporary_subagents_used") is not False or visual_lighthouse_delivery.get("lock_requested") is not False:
    error("visual lighthouse handoff cannot use temporary subagents or request lock")
if visual_lighthouse_delivery.get("full_121_production_authorized") is not False or visual_lighthouse_delivery.get("simulation_authorized") is not False:
    error("visual lighthouse handoff cannot grant full production or Simulation")
visual_lighthouse_exact = visual_lighthouse_evidence.get("chief_editor_exact_verification", {})
if visual_lighthouse_exact.get("cumulative_changed_files_exact") != 15:
    error("visual lighthouse exact cumulative file count is wrong")
if len(visual_lighthouse_exact.get("cumulative_changed_files", [])) != 15:
    error("visual lighthouse exact path list must contain 15 files")
if visual_lighthouse_exact.get("evidence_followup_changed_files_exact") != 5:
    error("visual lighthouse evidence followup scope is wrong")
keep_counts = visual_lighthouse_exact.get("byte_exact_keep", {})
if keep_counts != {"main_assets": 18, "source_art": 16, "sketch_gates": 10, "unaffected_contact_sheets": 3, "accepted_kar_01_har_aa_06_back_island": True}:
    error("visual lighthouse byte-exact KEEP counts are wrong")
sha_index = visual_lighthouse_exact.get("sha256_index", {})
if sha_index.get("indexed_files") != 61 or sha_index.get("unique_paths") != 61 or sha_index.get("pending_delivery_placeholders") != 0:
    error("visual lighthouse SHA-256 index summary is wrong")
if visual_lighthouse_exact.get("chief_editor_aesthetic_pass_declared") is not False:
    error("Chief Editor technical handoff cannot self-declare aesthetic pass")
if visual_lighthouse_evidence.get("chief_editor_disposition") != "VISUAL_LIGHTHOUSE_ONLY_HANDOFF_ACCEPTED_FOR_EXACT_ART_DIRECTION_REVIEW":
    error("visual lighthouse Chief Editor disposition is wrong")
if visual_lighthouse_evidence.get("art_direction_review_authorized") is not True or visual_lighthouse_evidence.get("visual_production_authorized") is not False:
    error("visual lighthouse evidence next-stage authorization is wrong")
if visual_lighthouse_evidence.get("temporary_subagents_used") is not False or visual_lighthouse_evidence.get("lock_requested") is not False:
    error("visual lighthouse evidence cannot use temporary subagents or request lock")

final_lighthouse_evidence = read_json("governance/ART_DIRECTION_LIGHTHOUSE_FINAL_REVIEW_20260830.json")
if final_lighthouse_evidence.get("record_type") != "VISIBLE_CHAT_ART_DIRECTION_LIGHTHOUSE_FINAL_REVIEW_AND_CHIEF_EDITOR_RECORD":
    error("final lighthouse Art Direction evidence record type is wrong")
final_art_review = final_lighthouse_evidence.get("art_direction_review", {})
if final_art_review.get("visible_chat") != "FOULWAKE Sanat Yönetmeni" or final_art_review.get("visible_chat_ack") is not True:
    error("final lighthouse Art Direction evidence requires correct visible chat ACK")
if final_art_review.get("evidence_type") != "VISIBLE_CHAT_WORKSTREAM" or final_art_review.get("review_evidence_type") != "EXACT_VISUAL_LIGHTHOUSE_FINAL_REVIEW":
    error("final lighthouse Art Direction evidence types are wrong")
if final_art_review.get("source_commit") != "7418d9c2c89c265cb6efd30f6a5a7f2addd528da":
    error("final lighthouse Art Direction exact source is wrong")
if final_art_review.get("input_visual_commit") != "23c062f6de06c32eab224b3440c8474725d4fe9e":
    error("final lighthouse Art Direction exact Visual input is wrong")
if final_art_review.get("canonical_visual_delivery_commit") != "c8081aa9f781737b0d7e14c8b224bf1fd988e8bb":
    error("final lighthouse Art Direction canonical Visual delivery is wrong")
if final_art_review.get("exact_visuals_opened") != "9/9" or final_art_review.get("back_lighthouse_disposition") != "KEEP":
    error("final lighthouse Art Direction evidence must record 9/9 and KEEP")
if final_art_review.get("pilot_front_counts") != {"keep": 12, "rework_required": 0} or final_art_review.get("pilot_back_counts") != {"keep": 7, "rework_required": 0}:
    error("final lighthouse pilot Art Direction counts are wrong")
if final_art_review.get("temporary_subagents") != [] or final_art_review.get("lock_requested") is not False:
    error("final lighthouse Art Direction review cannot use temporary subagents or request lock")
final_exact = final_lighthouse_evidence.get("chief_editor_exact_verification", {})
if final_exact.get("integration_branch_head") != "7d18ae9b9b0d03de33362e803896c26c29fd0dca":
    error("final lighthouse evidence Chief Editor input head is wrong")
if final_exact.get("visual_branch_head") != "23c062f6de06c32eab224b3440c8474725d4fe9e" or final_exact.get("art_direction_branch_head") != "7418d9c2c89c265cb6efd30f6a5a7f2addd528da":
    error("final lighthouse exact branch heads are wrong")
if final_exact.get("reviewed_rasters_exact") != 9 or len(final_exact.get("reviewed_rasters", [])) != 9:
    error("final lighthouse exact raster evidence must contain 9 entries")
if final_exact.get("chief_editor_evidence_acceptance") is not True or final_exact.get("chief_editor_pilot_art_acceptance") is not False:
    error("final lighthouse Chief Editor evidence/pilot boundary is wrong")
if final_lighthouse_evidence.get("chief_editor_disposition") != "ART_DIRECTION_PASS_RECORDED_PENDING_PROJECT_OWNER_PILOT_DECISION":
    error("final lighthouse Chief Editor disposition is wrong")
if final_lighthouse_evidence.get("project_owner_final_aesthetic_acceptance_pending") is not True:
    error("final lighthouse evidence must retain project-owner decision")
if final_lighthouse_evidence.get("active_visual_candidate") is not False or final_lighthouse_evidence.get("visual_production_authorized") is not False:
    error("final lighthouse evidence cannot activate candidate or production")
if final_lighthouse_evidence.get("full_121_production_authorized") is not False or final_lighthouse_evidence.get("simulation_authorized") is not False or final_lighthouse_evidence.get("release_pass") is not False:
    error("final lighthouse evidence cannot grant downstream PASS")

visual_evidence = read_json("governance/VISUAL_HANDOFF_20260825.json")
if visual_evidence.get("record_type") != "VISIBLE_CHAT_VISUAL_WORKSTREAM_HANDOFF_AND_CHIEF_EDITOR_DISPOSITION":
    error("Visual evidence record type is wrong")
if visual_evidence.get("status") != "REJECTED_ART_REWORK_REQUIRED":
    error("Visual evidence must record art rejection")
delivery = visual_evidence.get("visual_delivery", {})
if delivery.get("visible_chat") != "FOULWAKE görsel tasarım" or delivery.get("visible_chat_ack") is not True:
    error("Visual evidence requires correct visible chat ACK")
if delivery.get("source_branch") != "work/v2.7-visual" or delivery.get("source_commit") != "e91581bb336dfcbab5da1d48a256577f9251f891":
    error("Visual evidence branch/commit mismatch")
if delivery.get("temporary_subagent_used") is not False or delivery.get("lock_requested") is not False:
    error("Visual evidence cannot use temporary agents or request a lock")
audit = visual_evidence.get("chief_editor_audit", {})
if audit.get("art_acceptance") != "FAIL" or audit.get("back_art_acceptance") != "FAIL":
    error("Chief Editor Visual art/back disposition must be FAIL")
if audit.get("release_pass") is not False or audit.get("lock_allowed") is not False:
    error("Rejected Visual handoff cannot grant release or lock")
finding_ids = {item.get("id") for item in audit.get("findings", [])}
for finding_id in ("ART-001-A", "ART-001-C", "ART-001-D", "SRC-001-A", "SRC-001-B", "QA-002-A"):
    if finding_id not in finding_ids:
        error(f"Visual audit missing finding: {finding_id}")


# Historical communication and accepted Story evidence remain immutable facts.
acks = read_json("governance/VISIBLE_CHAT_ACKS_20260820.json")
if acks.get("status") != "ACCEPTED_3_OF_3_COMMUNICATION_ONLY":
    error("communication evidence must remain 3/3 communication-only")
if len(acks.get("records", [])) != 3 or acks.get("temporary_subagents_used") is not False:
    error("communication evidence must contain three no-subagent records")
story_evidence = read_json("governance/STORY_HANDOFF_20260820.json")
if story_evidence.get("status") != "ACCEPTED_STORY_WORKSTREAM_PASS_FOR_VISUAL_INPUT":
    error("Story handoff evidence lost accepted status")
if story_evidence.get("story_delivery", {}).get("source_commit") != "e04eef7f1fef6ea407feaaf26558551297c44b37":
    error("Story handoff evidence exact commit changed")
if story_evidence.get("subsequent_integration", {}).get("status") != "EXACT_ACCEPTED_STORY_BLOBS_INTEGRATED_TO_V2_7_DESIGN":
    error("Story evidence is missing the subsequent exact integration record")
expected_story_blobs = {
    "working/v2.7/FOULWAKE_STORY_FRAMEWORK.md": "962222d83d669763c4ac8e2765f024b9fade180c",
    "working/v2.7/FOULWAKE_RULEBOOK_STORY_v2.7.md": "f1e0eb75434540a85e8b21484acd99ca0abc66cf",
    "working/v2.7/FOULWAKE_STORY_REVALIDATION_v2.7.md": "2b4b4d423c65d5b72f756d322d9b0bd3c8537afa",
}
for path, expected_sha in expected_story_blobs.items():
    if git_blob_sha(path) != expected_sha:
        error(f"integrated Story blob differs from accepted handoff: {path}")


expected_art_direction_blobs = {
    "working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTION_BIBLE_v2.7.md": "11adbf70986401b25872101f986b07ecb9b992b4",
    "working/v2.7/visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json": "16e41ce2fd237dbf1cf43a87a9c682ff1ebb3f7b",
    "working/v2.7/visual/art_direction/FOULWAKE_12_PILOT_PRODUCTION_BRIEFS_v2.7.md": "7af68a33d2e40ee924a2aeb49f75881035ee6fee",
    "working/v2.7/visual/art_direction/FOULWAKE_7_BACK_BRIEFS_v2.7.md": "bb9f9de721d359c08a3f9310eed7e4ed73d24b0e",
}
for path, expected_sha in expected_art_direction_blobs.items():
    if git_blob_sha(path) != expected_sha:
        error(f"integrated Art Direction blob differs from accepted handoff: {path}")


# Active source hierarchy and card source checks.
hierarchy = read_json("working/v2.7/SOURCE_HIERARCHY_v2.7.json")
priorities = [item.get("priority") for item in hierarchy.get("sources", [])]
if priorities != [1, 2, 3, 4, 5]:
    error("source priorities must remain 1 through 5")
if hierarchy.get("conflict_action") != "STOP_AND_HANDOFF_TO_CHIEF_EDITOR":
    error("source conflicts must stop and hand off")
art_source = hierarchy.get("sources", [{}] * 5)[4] if len(hierarchy.get("sources", [])) >= 5 else {}
directive_path = "working/v2.7/visual/FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md"
if directive_path not in art_source.get("paths", []):
    error("source hierarchy does not include binding visual rework directive")
pilot_order_path = "working/v2.7/visual/FOULWAKE_PILOT_REWORK_ORDER_v2.7.md"
if pilot_order_path not in art_source.get("paths", []):
    error("source hierarchy does not include binding pilot rework order")
targeted_order_path = "working/v2.7/visual/FOULWAKE_REVISED_PILOT_TARGETED_REWORK_ORDER_v2.7.md"
if targeted_order_path not in art_source.get("paths", []):
    error("source hierarchy does not include revised targeted pilot rework order")
if art_source.get("revised_art_direction_pilot_review_evidence") != "governance/ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json":
    error("source hierarchy revised pilot review evidence is wrong")
lighthouse_order_path = "working/v2.7/visual/FOULWAKE_BACK_LIGHTHOUSE_ONLY_REWORK_ORDER_v2.7.md"
if lighthouse_order_path not in art_source.get("paths", []):
    error("source hierarchy does not include lighthouse-only rework order")
if art_source.get("art_direction_lighthouse_review_evidence") != "governance/ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json":
    error("source hierarchy lighthouse-only evidence is wrong")
if art_source.get("authorized_changed_files_exact") != 0:
    error("source hierarchy must not retain a Visual changed-file authorization after Art Direction PASS")
if art_source.get("art_direction_pilot_review_evidence") != "governance/ART_DIRECTION_PILOT_REVIEW_20260825.json":
    error("source hierarchy pilot review evidence is wrong")
if art_source.get("current_pilot_result") != "PILOT_ART_DIRECTION_PASS_PENDING_PROJECT_OWNER_AND_CHIEF_EDITOR_ACCEPTANCE":
    error("source hierarchy must record pilot Art Direction PASS pending owner/Chief")
if art_source.get("pilot_authorization_state") != "CONSUMED_ART_DIRECTION_PASS_PENDING_OWNER_CHIEF":
    error("source hierarchy pilot authorization state is wrong")
if art_source.get("latest_visual_delivery_commit") != "c8081aa9f781737b0d7e14c8b224bf1fd988e8bb":
    error("source hierarchy latest Visual delivery is wrong")
if art_source.get("latest_visual_evidence_commit") != "23c062f6de06c32eab224b3440c8474725d4fe9e":
    error("source hierarchy latest Visual evidence commit is wrong")
if art_source.get("latest_visual_handoff_evidence") != "governance/VISUAL_LIGHTHOUSE_ONLY_HANDOFF_20260830.json":
    error("source hierarchy latest Visual handoff evidence is wrong")
if art_source.get("art_direction_review_input_commit") != "23c062f6de06c32eab224b3440c8474725d4fe9e":
    error("source hierarchy Art Direction review input is wrong")
if art_source.get("new_visual_production_authorized") is not False:
    error("source hierarchy must pause Visual production")
if art_source.get("art_direction_lighthouse_final_review_evidence") != "governance/ART_DIRECTION_LIGHTHOUSE_FINAL_REVIEW_20260830.json":
    error("source hierarchy final lighthouse evidence is wrong")
if art_source.get("latest_reviewed_visual_commit") != "23c062f6de06c32eab224b3440c8474725d4fe9e":
    error("source hierarchy final reviewed Visual commit is wrong")
if art_source.get("current_pilot_front_counts") != {"keep": 12, "rework_required": 0} or art_source.get("current_pilot_back_counts") != {"keep": 7, "rework_required": 0}:
    error("source hierarchy final pilot counts are wrong")
if art_source.get("project_owner_final_aesthetic_acceptance") is not False or art_source.get("chief_editor_pilot_acceptance") is not False:
    error("source hierarchy cannot pre-approve owner or Chief pilot acceptance")
art_direction_path = "working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md"
if art_direction_path not in art_source.get("paths", []):
    error("source hierarchy does not include binding Art Direction work order")
accepted_art_paths = {
    "working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTION_BIBLE_v2.7.md",
    "working/v2.7/visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json",
    "working/v2.7/visual/art_direction/FOULWAKE_12_PILOT_PRODUCTION_BRIEFS_v2.7.md",
    "working/v2.7/visual/art_direction/FOULWAKE_7_BACK_BRIEFS_v2.7.md",
}
if not accepted_art_paths.issubset(set(art_source.get("paths", []))):
    error("source hierarchy does not include the accepted Art Direction package")
if art_source.get("accepted_art_direction_source_commit") != "7418d9c2c89c265cb6efd30f6a5a7f2addd528da":
    error("source hierarchy accepted Art Direction commit is wrong")
if art_source.get("production_authorization") != "NONE_PENDING_PROJECT_OWNER_AND_CHIEF_EDITOR_PILOT_ACCEPTANCE" or art_source.get("full_production_authorized") is not False:
    error("source hierarchy must pause production pending owner/Chief pilot acceptance")
if hierarchy.get("candidate_commit") is not None:
    error("source hierarchy cannot claim a candidate during rework")

card_source = read_json("working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json")
characters = card_source.get("characters", [])
powers = card_source.get("powers", [])
ids = [item.get("id") for item in characters + powers]
if len(characters) != 20 or len(powers) != 30 or len(ids) != len(set(ids)):
    error("Card Texts must contain 20 Character + 30 Power unique ids")
powers_by_id = {item.get("id"): item for item in powers}
if powers_by_id.get("GUC-22", {}).get("name") != "Kaptanın Çatlak Kupası":
    error("active v2.7 GUC-22 record changed without SRC-002 resolution")
if powers_by_id.get("GUC-23", {}).get("name") != "Bayat Peksimet":
    error("active v2.7 GUC-23 record changed without SRC-002 resolution")

mechanics = read_json("working/v2.7/V27_MECHANIC_DECISIONS.json")
sea_rock = {item.get("id"): item for item in mechanics.get("decisions", [])}.get("DEC-20260820-01", {})
if sea_rock.get("value") != "SEA_ROCK_SHARED_BACK" or sea_rock.get("release_status") != "BLOCKER_UNTIL_RETEST":
    error("Sea=Rock draft decision/retest blocker changed")



# Current project-owner visual override supersedes the historical Art Direction
# PASS for production/candidate purposes while preserving that review as history.
owner_rejection = read_json("governance/PROJECT_OWNER_VISUAL_REJECTION_20260830.json")
if owner_rejection.get("status") != "PROJECT_OWNER_PILOT_REJECTED_ART_DIRECTION_RESET_REQUIRED":
    error("current project-owner visual rejection status is wrong")
if owner_rejection.get("reviewed_visual_commit") != "23c062f6de06c32eab224b3440c8474725d4fe9e":
    error("project-owner rejection is bound to the wrong Visual commit")
if owner_rejection.get("supersedes_prior_art_direction_pass_for_production") is not True:
    error("project-owner rejection must supersede prior art PASS for production")
if owner_rejection.get("active_visual_candidate") is not None:
    error("owner-rejected pilot cannot be an active candidate")
captain_decision = owner_rejection.get("captain_decision", {})
if captain_decision.get("visible_name") != "KAPTAN" or captain_decision.get("technical_id") != "SET-KP-01":
    error("KAPTAN visible-name / technical-id decision mismatch")
if captain_decision.get("mechanics_policy") != "PRESERVE_CURRENT_TRANSFERABLE_CAPTAINCY_MECHANICS":
    error("KAPTAN decision must preserve current transferable captaincy mechanics")
copy_control = owner_rejection.get("copy_control", {})
if copy_control.get("visual_designer_may_rewrite_copy") is not False or copy_control.get("image_model_may_generate_visible_copy") is not False:
    error("Visual/Image model must not rewrite or generate visible card copy")
if copy_control.get("final_front_ocr_plus_canonical_compare_required") is not True:
    error("final front copy requires real OCR/render-source comparison")
reference_path = "working/v2.7/visual/references/FOULWAKE_KAPTAN_ART_LANGUAGE_REFERENCE_v2.7.jpg"
if not (ROOT / reference_path).is_file():
    error("binding KAPTAN art-language reference is missing")
elif git_blob_sha(reference_path) != "6e3dc9eb5ac00758bc5dd307bc5bd646435ec5f4":
    error("binding KAPTAN art-language reference blob changed")
owner_active = read_json("governance/ACTIVE_WORKSTREAMS.json").get("project_owner_override", {})
if owner_active.get("status") != "PROJECT_OWNER_PILOT_REJECTED_ART_DIRECTION_RESET_REQUIRED":
    error("ACTIVE_WORKSTREAMS lost current owner override")
if owner_active.get("visual_production_authorized") is not False:
    error("owner override cannot authorize Visual production")
owner_hierarchy = read_json("working/v2.7/SOURCE_HIERARCHY_v2.7.json")
if owner_hierarchy.get("project_owner_override", {}).get("current_authorization") != "ART_DIRECTION_MICRO_PATCH_ONLY":
    error("source hierarchy owner override must authorize Art Direction micro patch only")
owner_art_source = next((item for item in owner_hierarchy.get("sources", []) if item.get("priority") == 5), {})
for required_owner_path in ("working/v2.7/visual/references/FOULWAKE_KAPTAN_ART_LANGUAGE_REFERENCE_v2.7.jpg", "working/v2.7/visual/FOULWAKE_OWNER_RESET_FAST_MICRO_GATE_ORDER_v2.7.md", "governance/PROJECT_OWNER_VISUAL_REJECTION_20260830.json"):
    if required_owner_path not in owner_art_source.get("paths", []):
        error(f"source hierarchy missing owner override path: {required_owner_path}")
require_markers("PROJECT_STATE.md", ["PROJECT OWNER REJECTED", "KAPTAN sanat dili reseti", "BLOCKED_COPY_DRIFT"])
require_markers("AI_HANDOFF.md", ["PROJECT_OWNER_REJECTED", "KAPTAN ana sanat dili referansı", "YALNIZ SANAT YÖNETİMİ MİKRO PATCHİ YETKİLİ"])
require_markers("governance/DECISION_REGISTER.md", ["DEC-20260830-05", "DEC-20260830-06", "DEC-20260830-07", "BINDING COPY LOCK / FAST GATE"])
require_markers("working/v2.7/visual/FOULWAKE_OWNER_RESET_FAST_MICRO_GATE_ORDER_v2.7.md", ["BACK_SEA_ROCK", "BACK_ISLAND", "BACK_LIGHTHOUSE", "700 kelimelik", "BLOCKED_COPY_DRIFT", "FULL_121_PRODUCTION_AUTHORIZED: NO"])

# Human-readable contracts must contain the high-risk rules.
require_markers("AI_HANDOFF.md", [
    "v2.6 STABLE / LOCKED",
    "DELIVERED_REJECTED_ART_REWORK_REQUIRED",
    "e91581bb336dfcbab5da1d48a256577f9251f891",
    "SRC-002",
    "Geçici alt ajan oluşturmak yasaktır",
    "FOULWAKE Sanat Yönetmeni",
    "ACKNOWLEDGED_COMMUNICATION_TEST_ONLY",
    "ART_DIRECTION_ACK_20260825.json",
    "ART_DIRECTION_PILOT_REVIEW_20260825.json",
    "FOULWAKE_PILOT_REWORK_ORDER_v2.7.md",    "ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json",
    "FOULWAKE_REVISED_PILOT_TARGETED_REWORK_ORDER_v2.7.md",
    "ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json",
    "FOULWAKE_BACK_LIGHTHOUSE_ONLY_REWORK_ORDER_v2.7.md",
    "VISUAL_LIGHTHOUSE_ONLY_HANDOFF_ACCEPTED_FOR_EXACT_ART_DIRECTION_REVIEW",
    "VISUAL_LIGHTHOUSE_ONLY_HANDOFF_20260830.json",
    "23c062f6de06c32eab224b3440c8474725d4fe9e",
    "ART_DIRECTION_LIGHTHOUSE_FINAL_REVIEW_20260830.json",
    "PILOT_ART_DIRECTION_PASS",
    "12 FRONT KEEP / 7 BACK KEEP",
])
require_markers("PROJECT_STATE.md", [
    "Aktif görsel candidate",
    "SRC-002",
    "TECHNICAL_PIPELINE_REFERENCE_ONLY",
    "branch protection/ruleset",
    "Sanat Yönetimi",
    "ART_DIRECTION_PILOT_REVIEW_20260825.json",
    "ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json",
    "ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json",
    "VISUAL_LIGHTHOUSE_ONLY_HANDOFF_20260830.json",
    "ART_DIRECTION_LIGHTHOUSE_FINAL_REVIEW_20260830.json",
    "PILOT_ART_DIRECTION_PASS",
    "12 FRONT KEEP / 7 BACK KEEP",
])
require_markers("governance/DECISION_REGISTER.md", [
    "DEC-20260825-01",
    "DEC-20260825-05",
    "DEC-20260825-06",
    "DEC-20260825-08",
    "DEC-20260825-09",
    "DEC-20260825-10",
    "DEC-20260825-11",
    "BINDING PILOT REVIEW DISPOSITION",
    "BINDING CREATIVE GATE",
    "SUPERSEDED 2026-08-25",
    "saçma/anlamsız okunabilir yazı",    "DEC-20260828-01",
    "DEC-20260828-02",
    "TARGETED PILOT REWORK AUTHORIZATION",
    "DEC-20260830-01",
    "DEC-20260830-02",
    "BACK_LIGHTHOUSE-ONLY AUTHORIZATION",
    "DEC-20260830-03",
    "LIGHTHOUSE-ONLY HANDOFF ACCEPTANCE",
    "DEC-20260830-04",
    "FINAL LIGHTHOUSE ART DIRECTION REVIEW",
])
require_markers("governance/WORKSTREAM_ASSIGNMENTS.md", [
    "PENDING_OWNER_CHIEF_PILOT_ACCEPTANCE",
    "SRC-002",
    "FOULWAKE Sanat Yönetmeni",
    "EXACT_PILOT_REVIEW_COMPLETE",
    "REDRAW_BRIEF",
    "REVISED_EXACT_PILOT_REVIEW_COMPLETE",
    "ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json",
    "ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json",
    "VISUAL_LIGHTHOUSE_ONLY_HANDOFF_20260830.json",
    "PILOT_ART_DIRECTION_PASS / OWNER + CHIEF PENDING",
    "PILOT_ART_DIRECTION_PASS_RECORDED / PRODUCTION_PAUSED",
    "ART_DIRECTION_LIGHTHOUSE_FINAL_REVIEW_20260830.json",
    "PILOT_ART_DIRECTION_PASS",
])
require_markers("working/v2.7/visual/FOULWAKE_PILOT_REWORK_ORDER_v2.7.md", [
    "KAR-01",
    "SAD-H-03",
    "HAR-KY-06",
    "BACK_SEA_ROCK",
    "BACK_ISLAND",
    "BACK_LIGHTHOUSE",
    "Sabit 5×5'e bağlı olmayan",
    "PILOT_REWORK_DELIVERED",
    "LOCK_REQUESTED: NO",
])
require_markers("working/v2.7/visual/FOULWAKE_REVISED_PILOT_TARGETED_REWORK_ORDER_v2.7.md", [
    "KAR-01",
    "HAR-AA-06",
    "BACK_ISLAND",
    "BACK_LIGHTHOUSE",
    "CHANGED_FILES",
    "25",
    "BYTE_EXACT_KEEP_VERIFIED",
    "TARGETED_PILOT_REWORK_DELIVERED",
    "LOCK_REQUESTED: NO",
])

require_markers("working/v2.7/visual/FOULWAKE_BACK_LIGHTHOUSE_ONLY_REWORK_ORDER_v2.7.md", [
    "BACK_LIGHTHOUSE",
    "CHANGED_FILES: 15",
    "18/19 ana görsel",
    "16/17 source-art",
    "10/10 sketch gate",
    "LIGHTHOUSE_FAMILY_VISIBILITY_CHECK",
    "BACK_LIGHTHOUSE_ONLY_REWORK_DELIVERED",
    "BLOCKED_SCOPE_DRIFT",
    "LOCK_REQUESTED: NO",
])

require_markers("governance/WORKSTREAM_PROTOCOL.md", [
    "VISIBLE_CHAT_ACK: YES",
    "EVIDENCE_TYPE: VISIBLE_CHAT_WORKSTREAM",
    "unique render SHA",
    "BACK_SEA_ROCK=42",
    "saçma/anlamsız okunabilir yazı",
    "work/v2.7-art-direction",
    "Sanat Yönetmeni ile Görsel Tasarım birbirinin yerine PASS veremez",
])
require_markers("working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md", [
    "teknik bir “görsel QA” masası değildir",
    "FOULWAKE’a mı ait",
    "Brief, yalnız nesne listesi veya üretim promptu değildir",
    "Nihai estetik karar proje sahibinindir",
    "VISIBLE_CHAT_ACK: YES",
    "Geçici alt ajan oluşturulamaz",
    "İlk görünür sohbet testi — tamamlandı",
    "FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7",
])
require_markers("governance/RELEASE_GATE.md", [
    "semantik özgünlük",
    "20+31+15+42+6+4+3 = 121",
    "resim-içi yazı",
    "self-provenance",
])
require_markers("governance/CHIEF_EDITOR_AUDIT_20260825.md", [
    "50 commit ileride ve 2 commit geride",
    "Güç kartı kimlik kaynağı çelişkili",
    "platform düzeyinde zorunlu değil",
])
require_markers("working/v2.7/visual/FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md", [
    "121 kartın bütün ön yüzlerini",
    "yalnız STYLE_ONLY",
    "Resim içindeki yazı yasağı",
    "BACK_POWER",
    "BACK_SEA_ROCK",
    "anonim genel ada",
    "Sabit 5×5",
    "unique render SHA = unique artwork",
    "12 ön",
])
require_markers("working/v2.7/FOULWAKE_VISUAL_SYSTEM.md", [
    "ART REWORK REQUIRED",
    "Güncel aktif v2.7 görsel candidate **yoktur**",
    "tabela, pankart, slogan",
    "BACK_SUPPORT",
])
require_markers("working/v2.7/FOULWAKE_NARRATIVE_VALIDATION_v2.7.md", [
    "REPRODUCTION PENDING",
    "SRC-002 OPEN",
    "Kimlik veya",
])
require_markers("working/v2.7/BINARY_ARTIFACTS.md", [
    "ACTIVE VISUAL CANDIDATE: NONE",
    "REJECTED_ART / TECHNICAL_PIPELINE_REFERENCE_ONLY",
    "STALE SELF-PROVENANCE",
    "ROTATION-SAFETY FAIL",
])
require_markers("working/v2.7/qa/RELEASE_BLOCKER_RESOLUTION_PLAN_v2.7.md", [
    "RESMÎ SİMÜLASYON TESLİMİ DEĞİLDİR",
    "1.000.000",
    "450.000",
    "800 kör sınıflandırma",
    "unique render SHA",
    "candidate_commit=C",
])


# Repository workflow/template must expose scope and locked-release controls.
require_markers(".github/PULL_REQUEST_TEMPLATE.md", [
    "VISIBLE_CHAT_ACK",
    "LOCK_REQUESTED",
    "ART_BRIEF_MANIFEST",
    "BACK_MAPPING_CHECK",
    "ART_DIRECTION_STAGE",
    "REDRAW_BRIEF",
])
require_markers(".github/workflows/foulwake-governance.yml", [
    "Validate editorial governance",
    "Protect locked v2.6",
    "Validate specialist branch scope",
    "work/v2.7-story",
    "work/v2.7-art-direction",
    "work/v2.7-visual",
    "work/v2.7-simulation",
])


# Releasing v2.7 remains impossible without exact authorization and passing QA.
future_release = ROOT / "releases/v2.7"
authorization = ROOT / "governance/LOCK_AUTHORIZATION_v2.7.json"
if future_release.exists() and not authorization.exists():
    error("releases/v2.7 exists without lock authorization")
elif future_release.exists():
    lock = read_json("governance/LOCK_AUTHORIZATION_v2.7.json")
    if lock.get("authorized_by_project_owner") is not True:
        error("v2.7 lock authorization requires project-owner approval")
    if lock.get("executed_by_role") != "chief_editor":
        error("only chief_editor may execute the lock")
    if not is_sha(lock.get("candidate_commit")):
        error("lock authorization requires exact candidate commit")
    if lock.get("simulation_verdict") not in {"PASS", "PASS_WITH_MINOR_ISSUES"}:
        error("lock requires passing Simulation verdict")
    if lock.get("open_blockers") != []:
        error("lock requires an empty blocker list")
    attestation_path = lock.get("simulation_attestation_path")
    if not isinstance(attestation_path, str) or not (ROOT / attestation_path).is_file():
        error("lock requires an existing Simulation attestation")
    else:
        attestation = read_json(attestation_path)
        if attestation.get("candidate_commit") != lock.get("candidate_commit"):
            error("attestation candidate must match lock authorization")
        if not is_sha(attestation.get("evidence_bundle_sha256"), 64):
            error("attestation requires SHA-256 evidence bundle hash")


if ERRORS:
    print("FOULWAKE GOVERNANCE: FAIL")
    for item in ERRORS:
        print(f"- {item}")
    sys.exit(1)

print("FOULWAKE GOVERNANCE: PASS")
