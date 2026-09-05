#!/usr/bin/env python3
"""Integrated, fail-closed validation for the FOULWAKE repository."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

# A completed cutover routes the entry point to the live v4 validator. The v3
# implementation below remains executable at its historical Git checkpoint.
v4_state = ROOT / "governance/v4/runtime/STATE.json"
if v4_state.exists():
    try:
        current = json.loads(v4_state.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        raise SystemExit(f"BLOCKER: invalid v4 state: {exc}")
    if current.get("migration_control", {}).get("cutover_performed") is True:
        raise SystemExit(subprocess.run(
            [sys.executable, "-B", str(ROOT / "governance/v4/validator.py"), "--root", str(ROOT)],
            cwd=ROOT, check=False,
        ).returncode)


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def load_json(relative: str) -> dict:
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"{relative}: invalid JSON: {exc}")
        return {}


def exact_sha256(relative: str) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def git_tree(relative: str) -> str | None:
    result = subprocess.run(
        ["git", "rev-parse", f"HEAD:{relative}"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def jpeg_dimensions(relative: str) -> tuple[int, int] | None:
    data = (ROOT / relative).read_bytes()
    if not data.startswith(b"\xff\xd8"):
        return None
    pos = 2
    sof = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}
    while pos + 4 <= len(data):
        if data[pos] != 0xFF:
            pos += 1
            continue
        while pos < len(data) and data[pos] == 0xFF:
            pos += 1
        if pos >= len(data):
            break
        marker = data[pos]
        pos += 1
        if marker in {0x01, 0xD8, 0xD9}:
            continue
        if pos + 2 > len(data):
            break
        length = int.from_bytes(data[pos:pos + 2], "big")
        if length < 2 or pos + length > len(data):
            break
        if marker in sof and length >= 7:
            height = int.from_bytes(data[pos + 3:pos + 5], "big")
            width = int.from_bytes(data[pos + 5:pos + 7], "big")
            return width, height
        pos += length
    return None


for path in sorted(ROOT.rglob("*.json")):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")

expected_v26_tree = "efb41c46f06174c42dcdab2859b7c0ba517f86f0"
require(
    git_tree("releases/v2.6") == expected_v26_tree,
    "releases/v2.6 exact Git tree differs from the locked baseline",
)

stage = load_json("governance/CURRENT_STAGE.json")
require(stage.get("schema_version") == "3.0", "CURRENT_STAGE schema must be 3.0")
require(stage.get("stage_id") == "STAGE-20260901-V3-CLEAN-CLOSURE", "unexpected current stage")
require(stage.get("stage_status") == "V3_CLEAN_CLOSURE_COMPLETE", "v3 closure is not complete")
require(stage.get("active_visual_candidate") is None, "active visual candidate must be null")
require(stage.get("current_authorization") is None, "v3 closure must have no active authorization")
require(
    stage.get("default_write_policy") == "DENY_UNLESS_EXACTLY_AUTHORIZED_ABOVE",
    "current stage is not fail-closed",
)
require(stage.get("locked_release_tree_sha") == expected_v26_tree, "CURRENT_STAGE v2.6 tree drift")
workstreams = stage.get("workstreams", {})
require(workstreams.get("story", {}).get("head") == "e04eef7f1fef6ea407feaaf26558551297c44b37", "story checkpoint head drift")
require(workstreams.get("art_direction", {}).get("baseline_commit") == "119136812c2c749e14e675f1400640664fa044bc", "Art Direction accepted baseline drift")
require(workstreams.get("art_direction", {}).get("accepted_commit") == "917f8b71f47eeecdfb12b7ec930796bf111e2858", "Art Direction accepted commit drift")
require(workstreams.get("art_direction", {}).get("accepted_blob_sha") == "bae77450d6d10e1e3234a3473bf68ffa1efff810", "Art Direction accepted blob drift")
require(workstreams.get("art_direction", {}).get("validator_word_count") == 645, "Art Direction validator word count record drift")
require(workstreams.get("visual", {}).get("head") == "23c062f6de06c32eab224b3440c8474725d4fe9e", "Visual checkpoint head drift")
require(workstreams.get("simulation", {}).get("head") is None, "Simulation must remain absent")
require(all(item.get("authorization") is None for item in workstreams.values()), "specialist authorization remains open")

permissions = stage.get("permissions", {})
for permission in [
    "visual_production","thumbnails","pilot_or_candidate","full_121_production",
    "pdf_or_print_package","simulation","release","lock",
]:
    require(permissions.get(permission) is False, f"closure permission must be false: {permission}")

migration = stage.get("v4_migration_gate", {})
require(migration.get("status") == "V4_MIGRATION_READY / NOT_STARTED", "v4 migration gate status drift")
require(
    migration.get("quality_principle")
    == "LEAN GOVERNANCE SHALL REDUCE CONTEXT AND CEREMONY, NEVER REVIEW DEPTH, CREATIVE SCRUTINY, EVIDENCE QUALITY OR PROJECT OWNER CONTROL.",
    "lean-governance quality principle drift",
)
require(len(migration.get("entry_conditions", [])) == 8, "v4 entry-condition count drift")
require(len(migration.get("protected_quality_gates", [])) >= 15, "v4 quality-gate parity set incomplete")

scope = load_json("governance/WORKSTREAM_SCOPE_BASELINES.json")
require(scope.get("locked_release_tree_sha") == expected_v26_tree, "scope config v2.6 tree drift")
require(scope.get("checkpoint_stage") == stage.get("stage_id"), "scope/stage checkpoint mismatch")
branches = scope.get("branches", {})
require(set(branches) == {
    "work/v2.7-story","work/v2.7-art-direction","work/v2.7-visual","work/v2.7-simulation",
}, "scope config branch set drift")
require(branches.get("work/v2.7-story", {}).get("baseline_commit") == "e04eef7f1fef6ea407feaaf26558551297c44b37", "story scope baseline drift")
require(branches.get("work/v2.7-art-direction", {}).get("baseline_commit") == "917f8b71f47eeecdfb12b7ec930796bf111e2858", "Art Direction scope baseline drift")
require(branches.get("work/v2.7-art-direction", {}).get("accepted_from_baseline") == "119136812c2c749e14e675f1400640664fa044bc", "Art Direction provenance baseline drift")
require(branches.get("work/v2.7-visual", {}).get("baseline_commit") == "23c062f6de06c32eab224b3440c8474725d4fe9e", "Visual scope baseline drift")
require(all(
    policy.get("authorization") is None for policy in branches.values()
), "a specialist write authorization remains open")
require(branches.get("work/v2.7-simulation", {}).get("branch_must_not_exist") is True, "simulation branch must remain forbidden")

owner = load_json("governance/PROJECT_OWNER_KAPTAN_COPY_CORRECTION_20260830.json")
override = load_json("working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json")
records = override.get("records", [])
require(len(records) == 1, "owner card text override must contain one record")
kcopy = records[0] if records else {}
expected_copy = {
    "id":"SET-KP-01",
    "title":"KAPTAN",
    "section_label":"ÖZEL YETENEK",
    "effect":"Oylamada eşitlik olursa, senin tarafın geçerli olur.",
    "flavor":"Lidere et. Gemi senin emrinde.",
}
for key, value in expected_copy.items():
    require(kcopy.get(key) == value, f"KAPTAN copy drift in {key}")
    evidence_value = owner.get("technical_id") if key == "id" else owner.get("exact_visible_copy", {}).get(key)
    require(evidence_value == value, f"owner KAPTAN evidence drift in {key}")

image_path = "working/v2.7/visual/references/FOULWAKE_KAPTAN_ART_LANGUAGE_REFERENCE_v2.7.jpg"
require((ROOT / image_path).is_file(), "KAPTAN reference image missing")
if (ROOT / image_path).is_file():
    require(exact_sha256(image_path) == "a3224299f1b868ec71b6f637e3cb4bdd48dd5ba978178a0a64bef3e052193a2a", "KAPTAN image SHA-256 drift")
    require(jpeg_dimensions(image_path) == (896, 1536), "KAPTAN image dimensions drift")

manifest = load_json("working/v2.7/visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json")
cards = manifest.get("records", [])
require(len(cards) == 121, "art brief manifest must have 121 records")
ids = [item.get("card_identity", {}).get("id") for item in cards]
require(len(set(ids)) == 121 and None not in ids, "manifest IDs must be 121 unique values")
require([item.get("manifest_index") for item in cards] == list(range(1, 122)), "manifest indices must be 1..121")
expected_fronts = {
    "CHARACTER":20,"POWER":30,"ROTTEN_PROVISIONS":1,"LOYALTY":15,
    "OPEN_SEA":30,"ROCK":12,"ISLAND":6,"LIGHTHOUSE":4,"SUPPORT":3,
}
expected_backs = {
    "BACK_CHARACTER":20,"BACK_POWER":31,"BACK_LOYALTY":15,
    "BACK_SEA_ROCK":42,"BACK_ISLAND":6,"BACK_LIGHTHOUSE":4,"BACK_SUPPORT":3,
}
require(Counter(item.get("card_identity", {}).get("front_family") for item in cards) == Counter(expected_fronts), "front-family counts drift")
require(Counter(item.get("card_identity", {}).get("back_binary") for item in cards) == Counter(expected_backs), "back-binary counts drift")
kp = next((item for item in cards if item.get("card_identity", {}).get("id") == "SET-KP-01"), {})
require(kp.get("card_identity", {}).get("exact_name") == "KAPTAN", "manifest KAPTAN name drift")
require(kp.get("exact_copy", {}).get("name") == "KAPTAN", "manifest KAPTAN exact-copy name drift")
require(kp.get("exact_copy", {}).get("section_label") == "ÖZEL YETENEK", "manifest KAPTAN label drift")
require(kp.get("exact_copy", {}).get("effect") == expected_copy["effect"], "manifest KAPTAN effect drift")
require(kp.get("exact_copy", {}).get("flavor") == expected_copy["flavor"], "manifest KAPTAN flavor drift")
require(kp.get("exact_source", {}).get("authority_scope") == "project_owner_uploaded_card_override", "manifest KAPTAN source is not the project-owner upload")

accepted_patch_path = "working/v2.7/visual/art_direction/FOULWAKE_KAPTAN_ART_LANGUAGE_PATCH_v2.7.md"
accepted_patch = (ROOT / accepted_patch_path).read_text(encoding="utf-8")
require(git_tree(accepted_patch_path) == "bae77450d6d10e1e3234a3473bf68ffa1efff810", "accepted Art Direction patch blob drift")
require(len(re.findall(r"\b[\w’'-]+\b", accepted_patch, flags=re.UNICODE)) <= 700, "accepted Art Direction patch exceeds 700 words")
for phrase in [
    "bağlayıcı ana görsel kaynağıdır",
    "kaynak yalnız `STYLE_ONLY` değildir",
    "boş sandalye veya farklı ana özneyle değiştirilemez",
    "FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json",
    "Görsel üretim modeli bu metni üretmez",
    "bütün ön ve arka kart illüstrasyonlarının kadrajını",
    "kendi kadrajına nihai PASS veremez",
    "FRAMING_PASS",
    "REFRAME_REQUIRED",
    "3 mm bleed",
    "4–5 mm safe area",
    "thumbnail ve normal masa-mesafesi okunurluğu",
    "aynı plan, model, poz",
    "deste genelindeki kompozisyon ve kadraj ritmi",
    "yalınlaştırma sanat değerlendirmesinin derinliğini",
]:
    require(phrase in accepted_patch, f"accepted Art Direction patch semantic drift: {phrase}")

active_docs = [
    "AI_HANDOFF.md","PROJECT_STATE.md","governance/WORKSTREAM_ASSIGNMENTS.md",
    "governance/WORKSTREAM_PROTOCOL.md","governance/RELEASE_GATE.md",
    "working/v2.7/FOULWAKE_VISUAL_SYSTEM.md",
    "working/v2.7/visual/FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md",
    "working/v2.7/visual/FOULWAKE_OWNER_RESET_FAST_MICRO_GATE_ORDER_v2.7.md",
    "working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTION_BIBLE_v2.7.md",
    "working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md",
    "working/v2.7/visual/art_direction/FOULWAKE_12_PILOT_PRODUCTION_BRIEFS_v2.7.md",
    "working/v2.7/visual/art_direction/FOULWAKE_7_BACK_BRIEFS_v2.7.md",
]
for relative in active_docs:
    text = (ROOT / relative).read_text(encoding="utf-8")
    require("STYLE_ONLY" not in text, f"{relative}: superseded STYLE_ONLY token remains active")
    require("Kaptan Makamı" not in text, f"{relative}: superseded Kaptan Makamı remains active")

backs = (ROOT / "working/v2.7/visual/art_direction/FOULWAKE_7_BACK_BRIEFS_v2.7.md").read_text(encoding="utf-8")
for phrase in ["mat ve ışıldamayan","FULL REDRAW","Uzun kayalık sırt zorunlu değildir","Fener daha büyük"]:
    require(phrase in backs, f"back brief is missing owner requirement: {phrase}")

for relative in ["AI_HANDOFF.md","PROJECT_STATE.md","governance/WORKSTREAM_ASSIGNMENTS.md"]:
    text = (ROOT / relative).read_text(encoding="utf-8")
    require("candidate" in text and "**YOK**" in text, f"{relative}: no-candidate state is not explicit")
    require("917f8b71" in text, f"{relative}: accepted Art Direction commit missing")
    require("V3_CLEAN_CLOSURE_COMPLETE" in text, f"{relative}: v3 closure state missing")

source_hierarchy = load_json("working/v2.7/SOURCE_HIERARCHY_v2.7.json")
require(source_hierarchy.get("candidate_commit") is None, "source hierarchy candidate must be null")
require(source_hierarchy.get("active_sources", {}).get("task_authority") == "governance/CURRENT_STAGE.json", "source hierarchy does not use CURRENT_STAGE")

src = load_json("governance/SRC_002_COMPARISON_20260830.json")
require(src.get("status") == "PROJECT_OWNER_DECISION_REQUIRED", "SRC-002 status drift")
require(len(src.get("required_owner_decision", [])) == 2, "SRC-002 must expose two owner choices")

workflow = (ROOT / ".github/workflows/foulwake-governance.yml").read_text(encoding="utf-8")
require("'work/**'" in workflow, "workflow does not trigger for every work branch")
require("actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1" in workflow, "checkout action is not pinned to approved v7.0.1 commit")
require("validate_workstream_scope.py" in workflow, "specialist scope validator is not wired")
require("origin/v2.7-design" in workflow, "specialist policy is not loaded from integration branch")
require(expected_v26_tree in workflow, "workflow does not enforce exact v2.6 tree")
require("github.event.pull_request.head.sha" in workflow, "PR scope does not use the exact head SHA")

pr = (ROOT / ".github/PULL_REQUEST_TEMPLATE.md").read_text(encoding="utf-8")
for field in ["AUTHORIZATION_STAGE","AUTHORIZATION_BASELINE","COPY_AUDIT","FRAMING_DISPOSITION","TOOLS_USED","PLUGINS_USED","PLUGINS_AVAILABLE_BUT_NOT_USED","NOT_USED_REASON"]:
    require(field in pr, f"PR template missing {field}")

protocol = (ROOT / "governance/WORKSTREAM_PROTOCOL.md").read_text(encoding="utf-8")
require("FOULWAKE Görsel Tasarım 2" in protocol, "wrong visible Visual chat")
require("default-deny" in protocol.lower(), "protocol is not default-deny")
require("BLOCKED_COPY_DRIFT" in protocol, "protocol lacks copy failure")
require("BLOCKED_FRAMING_DRIFT" in protocol, "protocol lacks framing failure")

sim_schema = load_json("governance/SIM_QA_ATTESTATION_SCHEMA.json")
props = sim_schema.get("properties", {})
for gate in ["source_identity_gate","mechanics_gate","strategy_gate","social_gate","art_semantics_gate","copy_gate","framing_gate","backs_gate","package_gate","physical_gate"]:
    enum = props.get(gate, {}).get("properties", {}).get("verdict", {}).get("enum")
    require(enum == ["PASS","PASS_WITH_MINOR_ISSUES","FAIL","BLOCKER"], f"SIM schema {gate} verdict is not closed")
lock_schema = load_json("governance/LOCK_AUTHORIZATION_SCHEMA.json")
require(lock_schema.get("properties", {}).get("open_blockers", {}).get("maxItems") == 0, "lock schema permits open blockers")
require(lock_schema.get("properties", {}).get("locked_release_tree_before", {}).get("const") == expected_v26_tree, "lock schema v2.6 tree drift")

decisions = (ROOT / "governance/DECISION_REGISTER.md").read_text(encoding="utf-8")
for decision in ["DEC-20260830-09","DEC-20260830-10","DEC-20260830-11","DEC-20260901-01","DEC-20260901-02"]:
    require(decision in decisions, f"decision register missing {decision}")
require((ROOT / "governance/CHIEF_EDITOR_SYSTEM_AUDIT_20260830.md").is_file(), "Chief Editor system audit report missing")

if ERRORS:
    print("FOULWAKE governance validation: FAIL", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print("FOULWAKE governance validation: PASS")
print("- all JSON parsed")
print("- locked v2.6 exact tree preserved")
print("- v3 clean closure checkpoint and specialist scopes are fail-closed")
print("- KAPTAN visual/copy owner override is exact")
print("- 121 IDs, families and seven back mappings are consistent")
print("- accepted Art Direction patch, copy, framing and v4 quality parity are enforced")
