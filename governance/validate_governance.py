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
    "governance/SIM_QA_ATTESTATION_SCHEMA.json",
    "governance/LOCK_AUTHORIZATION_SCHEMA.json",
    "working/v2.7/SOURCE_HIERARCHY_v2.7.json",
    "working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json",
    "working/v2.7/FOULWAKE_NARRATIVE_VALIDATION_v2.7.md",
    "working/v2.7/FOULWAKE_VISUAL_SYSTEM.md",
    "working/v2.7/visual/FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md",
    "working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md",
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
if activation.get("status") != "PENDING_VISIBLE_CHAT_ACK":
    error("Art Direction must remain pending visible-chat ACK until evidence arrives")
if activation.get("branch_created") is not True:
    error("Art Direction branch activation must be recorded")
if activation.get("temporary_subagents_used") is not False:
    error("Art Direction activation cannot use temporary subagents")

deliveries = state.get("specialist_deliveries", {})
story = deliveries.get("story", {})
art_direction = deliveries.get("art_direction", {})
if art_direction.get("status") != "PENDING_VISIBLE_CHAT_ACK_AND_FIRST_REVIEW":
    error("Art Direction delivery status must remain pending visible-chat ACK")
if art_direction.get("work_branch") != "work/v2.7-art-direction":
    error("Art Direction delivery branch is wrong")
if art_direction.get("may_start_creative_work") is not False:
    error("Art Direction creative work cannot start before visible-chat ACK")
if art_direction.get("delivery_recorded") is not False:
    error("Art Direction delivery cannot be fabricated before visible-chat ACK")
if story.get("status") != "ACCEPTED_STORY_WORKSTREAM_PASS_FOR_VISUAL_INPUT":
    error("Story delivery acceptance is missing")
if story.get("source_commit") != "e04eef7f1fef6ea407feaaf26558551297c44b37":
    error("Story delivery exact commit is wrong")
if story.get("integrated_to_v2_7_design") is not True:
    error("accepted Story blobs must be recorded as integrated")
visual = deliveries.get("visual", {})
if visual.get("status") != "DELIVERED_REJECTED_ART_REWORK_REQUIRED":
    error("Visual delivery must be recorded as delivered and art-rejected")
if visual.get("source_commit") != "e91581bb336dfcbab5da1d48a256577f9251f891":
    error("Visual delivery exact head is wrong")
if visual.get("full_production_delivery_commit") != "494b8440bba722a9053f72b2fdeffc4286a61e17":
    error("Visual full-production commit is wrong")
if visual.get("art_accepted") is not False or visual.get("active_candidate") is not False:
    error("Rejected Visual art must not become an active candidate")
simulation = deliveries.get("simulation", {})
if simulation.get("status") != "PENDING_NEW_ART_CANDIDATE":
    error("Simulation must wait for a new accepted art candidate")
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
art_direction_path = "working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md"
if art_direction_path not in art_source.get("paths", []):
    error("source hierarchy does not include binding Art Direction work order")
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


# Human-readable contracts must contain the high-risk rules.
require_markers("AI_HANDOFF.md", [
    "v2.6 STABLE / LOCKED",
    "DELIVERED_REJECTED_ART_REWORK_REQUIRED",
    "e91581bb336dfcbab5da1d48a256577f9251f891",
    "SRC-002",
    "Geçici alt ajan oluşturmak yasaktır",
    "FOULWAKE Sanat Yönetmeni",
    "PENDING_VISIBLE_CHAT_ACK",
])
require_markers("PROJECT_STATE.md", [
    "Aktif görsel candidate",
    "SRC-002",
    "bütün ön/arka yüz sanatı reddedildi",
    "branch protection/ruleset",
    "Sanat Yönetimi",
    "Yaratıcı brief/inceleme",
])
require_markers("governance/DECISION_REGISTER.md", [
    "DEC-20260825-01",
    "DEC-20260825-05",
    "DEC-20260825-06",
    "BINDING CREATIVE GATE",
    "SUPERSEDED 2026-08-25",
    "saçma/anlamsız okunabilir yazı",
])
require_markers("governance/WORKSTREAM_ASSIGNMENTS.md", [
    "DELIVERED / REJECTED_ART_REWORK_REQUIRED",
    "PENDING_NEW_ART_CANDIDATE",
    "SRC-002",
    "FOULWAKE Sanat Yönetmeni",
    "PENDING_VISIBLE_CHAT_ACK",
    "REDRAW_BRIEF",
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
