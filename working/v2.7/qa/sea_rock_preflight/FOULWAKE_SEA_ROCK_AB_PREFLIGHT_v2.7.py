#!/usr/bin/env python3
"""Pinned Sea/Rock information preflight; never a full-game balance acceptance.

Python standard library only. Read and hash-check the locked v2.6 ZIP before
loading its unchanged v2.5 engine. Engine defects are evidence, not silently
patched mechanics. --check reproduces the evidence without rewriting outputs.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import importlib
import io
import json
import math
import platform
import random
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

TASK = "MEC-SEA-ROCK-PREFLIGHT-001"
AUTHORITY = "dba2dff0b9ec7c1f3361630da41d5f31c232e029"
ACTIVATION = "75763ab1736733f41eff40618a36a82c8a172909"
RESULT = "INCONCLUSIVE / HUMAN_PLAYTEST_REQUIRED"
PREFIX = "working/v2.7/qa/sea_rock_preflight/"
SCRIPT = PREFIX + "FOULWAKE_SEA_ROCK_AB_PREFLIGHT_v2.7.py"
RESULTS = PREFIX + "FOULWAKE_SEA_ROCK_AB_PREFLIGHT_RESULTS_v2.7.json"
REPORT = PREFIX + "FOULWAKE_SEA_ROCK_AB_PREFLIGHT_REPORT_v2.7.md"
SPEC = "OYUN_SIMULASYON_SPEC_v2.5.json"
CATEGORIES = {"Açık Deniz": "sea", "Kayalık": "rock", "Ada": "island", "Deniz Feneri": "lighthouse"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.PIPE)


def read_authority(root, authority):
    task_path = f"governance/v4/tasks/{TASK}.json"
    read = lambda p: json.loads(git(root, "show", f"{authority}:{p}"))
    state, task = read("governance/v4/runtime/STATE.json"), read(task_path)
    roles = read("governance/v4/roles/REGISTRY.json")
    require(state["active_project_task_id"] == TASK and task["status"] == "ACTIVE", "TASK_NOT_ACTIVE")
    require(task["executor_role"] == "SIMULATION_QA", "ROLE_DRIFT")
    require(task["scope"]["branch"] == "work/v2.7-simulation", "BRANCH_AUTHORITY_DRIFT")
    require(task["authorization"]["write_authorized"] and state["permissions"]["simulation"], "AUTHORITY_CLOSED")
    require("QA_REVIEW" in roles["roles"]["SIMULATION_QA"]["allowed_actions"], "ROLE_ACTION_CLOSED")
    require(set(task["scope"]["allowed_exact_paths"]) == {SCRIPT, RESULTS, REPORT}, "OUTPUT_SCOPE_DRIFT")
    for key, value in state["permissions"].items():
        if key != "simulation":
            require(value is False, f"UNEXPECTED_PRODUCTION_PERMISSION: {key}")
    baseline = git(root, "log", "--diff-filter=A", "--format=%H", authority, "--", task_path).decode().splitlines()
    require(baseline == [ACTIVATION], "ACTIVATION_DRIFT")
    require(git(root, "rev-parse", ACTIVATION + "^").decode().strip() == task["source"]["commit"], "SOURCE_PARENT_DRIFT")
    git(root, "merge-base", "--is-ancestor", ACTIVATION, "HEAD")
    pins = []
    for item in task["inputs"]:
        data = git(root, "show", f"{authority}:{item['path']}")
        for ref in (authority, task["source"]["commit"], ACTIVATION, "HEAD"):
            actual = git(root, "rev-parse", f"{ref}:{item['path']}").decode().strip()
            require(actual == item["git_blob"], f"SOURCE_DRIFT: {ref}:{item['path']}")
        require((root / item["path"]).read_bytes() == data, f"WORKTREE_INPUT_DRIFT: {item['path']}")
        pins.append({**item, "sha256": digest(data)})
    locked = task["source"]["locked_release_tree_sha"]
    for ref in (authority, ACTIVATION, "HEAD"):
        require(git(root, "rev-parse", ref + ":releases/v2.6").decode().strip() == locked, "LOCKED_TREE_DRIFT")
    manifest = read("releases/v2.6/V26_RELEASE_MANIFEST.json")
    return task, manifest, {
        "source_head": authority, "task_source_commit": task["source"]["commit"],
        "execution_baseline": ACTIVATION, "locked_v26_tree": locked,
        "branch": task["scope"]["branch"], "input_hashes": pins,
        "permissions": state["permissions"], "delivery_binding": "Git commit containing all three exact outputs; no self-acceptance",
    }


def load_package(path, manifest):
    data = path.read_bytes()
    expected = manifest["artifacts"]["zip"]
    require(len(data) == expected["size_bytes"] and digest(data) == expected["sha256"], "V26_PACKAGE_HASH_MISMATCH")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        nested = archive.read("MEKANIK_BASELINE_OYUN_SIMULASYON_PAKETI_v2.5.zip")
    require(digest(nested) == manifest["artifacts"]["mechanical_baseline_zip_sha256"], "V25_PACKAGE_HASH_MISMATCH")
    with zipfile.ZipFile(io.BytesIO(nested)) as archive:
        m = json.loads(archive.read("V25_RELEASE_MANIFEST.json"))
        for name, expected_hash in m["content_hashes"].items():
            require(digest(archive.read(name)) == expected_hash, f"PACKAGE_MEMBER_HASH_MISMATCH: {name}")
        needed = (SPEC, "prototype_balance_sim_v2_5.py", "tam_sistem_sim_v2_5.py", "OYUN_TAM_KURALLAR_v2.5.md", "OYUN_SIMULASYON_SPEC_v2.5.delta.json")
        files = {name: archive.read(name) for name in needed}
    return files, {"v26_zip_sha256": digest(data), "v25_zip_sha256": digest(nested),
                   "verified_manifest_members": len(m["content_hashes"]),
                   "used_member_sha256": {n: digest(b) for n, b in files.items()}}


def token(card, variant, known=False):
    if known:
        return "FRONT:" + card["id"]
    cat = CATEGORIES[card["category"]]
    return "BACK:" + ("sea_rock" if variant == "B" and cat in {"sea", "rock"} else cat)


def information_metrics(cards):
    distributions = {v: collections.Counter(token(c, v) for c in cards) for v in ("A", "B")}
    entropy = lambda counts: -sum((n / len(cards)) * math.log2(n / len(cards)) for n in counts.values())
    collisions = {v: sum(n * (n - 1) // 2 for n in c.values()) for v, c in distributions.items()}
    return {"sampling_space": "one uniformly selected identity from the 52-card pool; ideal labels only",
            "inventory": dict(collections.Counter(CATEGORIES[c["category"]] for c in cards)),
            "category_bits_removed_per_uniform_map_card": entropy(distributions["A"]) - entropy(distributions["B"]),
            "indistinguishable_unordered_identity_pairs": collisions,
            "additional_pairs_merged": collisions["B"] - collisions["A"],
            "sea_rock_identity_uncertainty_A_bits": (30 * math.log2(30) + 12 * math.log2(12)) / 42,
            "sea_rock_identity_uncertainty_B_bits": math.log2(42)}


def isolated_two_choice(spec):
    """Exhaustive finite inventory exercise, NOT a legal-horizon risk estimate.

    Two ordered distinct cards sampled uniformly from the Sea/Rock setup quota.
    Same objective in both variants: avoid an impassable entry. A selects Sea
    when available; B has indistinguishable backs and selects the first slot.
    Within equal observations both use the first slot. No score/human utility.
    """
    rows = []
    for shape, q in sorted(spec["setup"]["category_quotas"].items()):
        reef = spec["setup"]["impassable_rocks_by_map"][shape]
        pool = [("sea", False)] * q["sea"] + [("rock", True)] * reef + [("rock", False)] * (q["rock"] - reef)
        bad_a = bad_b = total = 0
        for i, a in enumerate(pool):
            for j, b in enumerate(pool):
                if i == j:
                    continue
                choice_a = a if a[0] == "sea" or b[0] != "sea" else b
                bad_a += int(choice_a[1]); bad_b += int(a[1]); total += 1
        require(bad_a / total == reef * (q["rock"] - 1) / (len(pool) * (len(pool) - 1)), "FINITE_ORACLE_A")
        require(bad_b / total == reef / len(pool), "FINITE_ORACLE_B")
        rows.append({"shape": shape, "sea": q["sea"], "rock": q["rock"], "impassable": reef,
                     "ordered_pairs": total, "impassable_picks_A": bad_a, "impassable_picks_B": bad_b,
                     "risk_A": bad_a / total, "risk_B": bad_b / total})
    return {"scope": "uniform unordered-inventory content with ordered two-choice draws; excludes board positions, setup conditioning, peeks, votes, effects and later recovery",
            "interpretation": "isolated information value for one hazard objective; neither full-game win rate nor back-design acceptance",
            "rows": rows}


def setup_check(g, spec, card_ids):
    """Independent checks: use spec rows and a separate breadth-first search."""
    w, h = g.voyage.width, g.voyage.height
    shape = f"{w}x{h}"
    grid = {pos: card_ids[id(event)] for pos, event in g.grid.items()}
    counts = collections.Counter(CATEGORIES[c["category"]] for c in grid.values())
    require(counts == spec["setup"]["category_quotas"][shape], "SETUP_CATEGORY_QUOTA")
    require(len({c["id"] for c in grid.values()}) == w * h, "SETUP_DUPLICATE_PHYSICAL_ID")
    damage = spec["setup"]["direct_hull_damage_quotas"][str(g.n)][g.config.length]
    for cat in ("sea", "rock"):
        require(sum(bool(c["damage"]) for c in grid.values() if CATEGORIES[c["category"]] == cat) == damage[cat], "SETUP_DAMAGE_QUOTA")
    blockers = {p for p, c in grid.items() if c.get("impassable", False)}
    islands = {p for p, c in grid.items() if c["category"] == "Ada"}
    require(len(blockers) == spec["setup"]["impassable_rocks_by_map"][shape], "SETUP_REEF_QUOTA")
    require(all(r < h - 1 for r, _ in blockers), "REEF_IN_FINAL_ROW")
    forbidden = [p for p, c in grid.items() if c["family"] in {"Girdap", "Ters Akıntı"}]
    require(all(max(abs(a[0] - b[0]), abs(a[1] - b[1])) > 1 for a in islands for b in forbidden), "ISLAND_ADJACENCY")
    frontier = {(-1, g.col, False)}
    for r in range(h):
        frontier = {(r, nc, seen or (r, nc) in islands) for _, col, seen in frontier
                    for nc in (col - 1, col, col + 1) if 0 <= nc < w and (r, nc) not in blockers
                    and abs(nc - g.port_col) <= h - 1 - r}
    require((h - 1, g.port_col, True) in frontier, "NO_ISLAND_PORT_PATH")
    near = [(0, col) for col in range(max(0, g.col - 1), min(w, g.col + 2)) if abs(col - g.port_col) <= h - 1]
    require(near and any(p not in blockers for p in near), "INITIAL_TOTAL_LOCK")
    require(all(grid[p]["family"] != "Sis" for p in near), "INITIAL_FOG")
    require(near == [(r, c) for r, c, _ in g.valid_candidates()], "INITIAL_HORIZON_DRIFT")
    require(all(len(p.powers) == 1 for p in g.players), "OPENING_POWER_COUNT")
    require(sum(p.traitor for p in g.players) == spec["setup"]["traitors"][str(g.n)], "LOYALTY_QUOTA")
    require(g.captain_opening_peek in near and g.player(g.captain).knowledge == {g.captain_opening_peek}, "CAPTAIN_PEEK")
    return grid, near


def engine_checks(m, spec):
    cards = spec["cards"]["maps"]
    require(len(cards) == 52 and len({c["id"] for c in cards}) == 52, "MAP_INVENTORY")
    require({c["id"] for c in cards if c.get("impassable")} == {"HAR-KY-01", "HAR-KY-03"}, "REEF_IDS")
    for card, event in zip(cards, m.V25_MAP_POOL):
        require(bool(card["damage"]) == m.event_is_damage(event), "ENGINE_DAMAGE_MAPPING")
        require(card["family"] == event.name and card["score"] == event.score, "ENGINE_EVENT_MAPPING")
    require(len(m.V25_MAP_POOL) == len(cards), "ENGINE_POOL_SIZE")
    by_id = {c["id"]: c for c in cards}
    sea, rock, reef = [by_id[x] for x in ("HAR-AD-01", "HAR-KY-02", "HAR-KY-01")]
    require(token(sea, "B") == token(rock, "B") and token(sea, "A") != token(rock, "A"), "BACK_MODEL_MAPPING")
    require(token(rock, "A") == token(reef, "A"), "IMPASSABLE_BACK_LEAK")
    require(token(sea, "B", True) != token(rock, "B", True), "KNOWN_FRONT_MUST_PERSIST")
    g = m.V25AuditGame(random.Random(50), m.canonical_config(10, length="normal"))
    pos = next(c for c, e in g.grid.items() if e.kind == "impassable_reef")
    p = next(p for p in g.players if p.pid != g.captain)
    p.knowledge.clear(); g.look_for_player(p, [pos])
    require(pos in p.knowledge and pos not in g.public_known and pos not in g.public_blocked, "PRIVATE_REEF_REVEAL")
    before = (g.row, g.col)
    g.public_reveal([pos])
    require(pos in g.public_known and pos in g.public_blocked and pos not in g.opened_cards and before == (g.row, g.col), "PUBLIC_REEF_REVEAL")

    # Two indistinguishable observation states, same ordinary persona and RNG.
    # Only unobserved Sea fronts are swapped. No production source is modified.
    safe = next(e for e in m.V25_MAP_POOL if e.name == "Sakin Deniz")
    bad = next(e for e in m.V25_MAP_POOL if e.name == "Fırtına")
    claims = []
    for swapped in (False, True):
        g = object.__new__(m.V25AuditGame)
        g.grid = {(0, 0): bad if swapped else safe, (0, 1): safe if swapped else bad}
        g.hull = 2; g.scurvy_active = False; g.rng = random.Random(0)
        g.persona = m.PERSONAS["dengeli"]; g.public_known = set(); g.hain_team_known = set()
        g.metrics_count = collections.Counter(); g.players = [m.AuditPlayer(pid=0, traitor=True)]; g.day = 2
        claims.append([m.asdict(c) for c in g._make_claims([(0, 0, 0), (0, 1, 1)])])
    require(claims[0][0]["coord"] != claims[1][0]["coord"] and not claims[0][0]["informed"] and not claims[1][0]["informed"], "ORACLE_REPRO_CHANGED")

    # Start a real canonical opening, stop immediately before first movement.
    # The boundary changes no choice or information code; run() calls the real
    # use_day_information() before the interception point.
    g = m.V25AuditGame(random.Random(3), m.canonical_config(10, length="short"))
    p = g.player(4)
    require(not p.traitor and p.pid != g.captain and "kirik_durbun" in p.powers, "OPENING_REPRO_CHANGED")
    before = sorted(p.knowledge)
    class BeforeMovement(Exception):
        pass
    def boundary(*args, **kwargs):
        raise BeforeMovement()
    g.move_once = boundary
    try:
        g.run()
    except BeforeMovement:
        pass
    require(g.day == 1 and g.row == -1 and not before and p.knowledge and "kirik_durbun" not in p.powers, "OPENING_REPRO_NOT_REPRODUCED")
    return {
        "passed_checks": ["52 unique map identities", "exact impassable IDs", "engine event/damage mapping", "ideal A/B back projection", "known fronts preserved", "private peek remains private", "public impassable blocks without entry or event resolution"],
        "full_game_evidence_gate": "FAIL",
        "findings": [
            {"id": "PREFLIGHT-ENGINE-01", "severity": "BLOCKER_FOR_INFORMATION_AB_GAME_OUTCOMES", "status": "REPRODUCED",
             "source": "tam_sistem_sim_v2_5.py:AuditGame._make_claims / true_worst",
             "expected": "Same player-visible information and RNG must produce the same bluff target after swapping unobserved same-category fronts.",
             "actual": "Uninformed traitor targets the true worst hidden front in both worlds.",
             "fixture_type": "minimal two-candidate unit fixture, not a complete legal game setup", "seed": 0, "persona": "dengeli",
             "visible_observations_in_both_worlds": {"A": ["BACK:sea", "BACK:sea"], "B": ["BACK:sea_rock", "BACK:sea_rock"]}, "private_and_team_knowledge": [],
             "world_1_ids": ["HAR-AD-01", "HAR-AD-11"], "world_2_ids": ["HAR-AD-11", "HAR-AD-01"], "claims": claims},
            {"id": "PREFLIGHT-ENGINE-02", "severity": "BLOCKER_FOR_CANONICAL_OPENING", "status": "REPRODUCED",
             "source": "tam_sistem_sim_v2_5.py:V25AuditGame.run -> use_day_information; OYUN_TAM_KURALLAR_v2.5.md §11.3 first-route information restriction",
             "expected": "No optional information power before the first voyage route; Captain neutral-night peek is the only special opening information.",
             "actual": "Non-Captain crew consumes Broken Spyglass and learns an additional front before the first movement.",
             "seed": 3, "players": 10, "length": "short", "actor": p.pid, "captain": g.captain,
             "day": g.day, "position_before_first_move": [g.row, g.col], "knowledge_before": before,
             "knowledge_after": sorted(p.knowledge), "power_consumed": "kirik_durbun",
             "instrumentation": "move_once replaced only with an exception boundary to stop execution before first movement"},
        ],
    }


def sample_openings(m, spec, seed, samples):
    ids = {id(e): c for e, c in zip(m.V25_MAP_POOL, spec["cards"]["maps"])}
    rows, cells = [], []
    for n in range(6, 16):
        for li, length in enumerate(("short", "normal", "long")):
            counts = collections.Counter()
            for sample in range(samples):
                run_seed = seed + n * 1_000_000 + li * 10_000 + sample
                g = m.V25AuditGame(random.Random(run_seed), m.canonical_config(n, length=length))
                grid, near = setup_check(g, spec, ids)
                obs = {v: [token(grid[p], v) for p in near] for v in ("A", "B")}
                cap = {v: [token(grid[p], v, p == g.captain_opening_peek) for p in near] for v in ("A", "B")}
                added = lambda view: sum(view["B"][i] == view["B"][j] and view["A"][i] != view["A"][j]
                                         for i in range(len(near)) for j in range(i + 1, len(near)))
                counts["setups"] += 1
                counts["mixed_sea_rock_first_horizons"] += int(added(obs) > 0)
                counts["category_distinctions_lost_ordinary_pairs"] += added(obs)
                counts["category_distinctions_lost_captain_pairs"] += added(cap)
                row = {"n": n, "length": length, "seed": run_seed, "width": g.voyage.width, "height": g.voyage.height,
                       "start_col": g.col, "port_col": g.port_col,
                       "grid_ids_row_major": [grid[pos]["id"] for pos in sorted(grid)],
                       "near": near, "captain": g.captain, "captain_peek": g.captain_opening_peek,
                       "backs": obs, "captain_observations": cap}
                row["paired_board_sha256"] = digest(canonical({k: row[k] for k in ("grid_ids_row_major", "width", "height", "start_col", "port_col")}))
                rows.append(row)
            cells.append({"n": n, "length": length, **dict(counts)})
    totals = {k: sum(c.get(k, 0) for c in cells) for k in ("setups", "mixed_sea_rock_first_horizons", "category_distinctions_lost_ordinary_pairs", "category_distinctions_lost_captain_pairs")}
    return {"scope": "paired observations on identical valid canonical opening boards, before any route choice; zero complete games",
            "sampling_limitation": "descriptive under the packaged setup sampler; not uniform over all legal layouts or predictive of moderator/human setup",
            "independent_setup_checks": "PASS for every sample: inventory, damage/reef quotas, no final-row reef, island adjacency, island-to-port BFS, first-horizon legality/no-fog, opening power/loyalty counts and Captain peek",
            "totals": totals, "cells": cells, "raw_paired_openings": rows}


def report_text(d, results_hash):
    info, checks, sample = d["information"], d["engine_validation"], d["paired_openings"]
    counts = sample["totals"]
    table = "\n".join(f"| {r['shape']} | {r['sea']} / {r['rock']} / {r['impassable']} | {100*r['risk_A']:.3f}% | {100*r['risk_B']:.3f}% |" for r in d["isolated_two_choice"]["rows"])
    pins = "\n".join(f"| `{p['path']}` | `{p['git_blob']}` |" for p in d["provenance"]["input_hashes"])
    return f"""# FOULWAKE — Deniz/Kayalık A/B ön testi

**RESULT: {RESULT}**

Ortak arka yüzün hangi bilgiyi kaldırdığı doğrulandı. Hangi tasarımın bütün
oyun için daha iyi olduğu belirlenemedi. Paket erişilebilir ve hashleri doğru;
motorun iki davranışı tam oyun karşılaştırmasını engelliyor. MEC-001 OPEN.

## Yetki ve yeniden üretim

- TASK_ID: `{TASK}`; rol: SIMULATION_QA; dal: `work/v2.7-simulation`.
- SOURCE_HEAD: `{d['provenance']['source_head']}`.
- Görev kaynak commit'i: `{d['provenance']['task_source_commit']}`.
- Çalışma başlangıcı: `{ACTIVATION}`; v2.6 tree: `{d['provenance']['locked_v26_tree']}`.
- Paket: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.6.zip`.
- v2.6 ZIP SHA-256: `{d['package']['v26_zip_sha256']}`.
- İç v2.5 ZIP SHA-256: `{d['package']['v25_zip_sha256']}`.
- İç manifestin {d['package']['verified_manifest_members']} üyesi byte düzeyinde doğrulandı.
- Repo/paket v2.5 delta dosyaları farklı JSON biçimindedir; nesne içerikleri
  birebir eşittir. İki ayrı byte hash'i RESULTS içinde korunur.
- Çalıştırıcı SHA-256: `{d['script_sha256']}`.
- RESULTS SHA-256: `{results_hash}`.
- Ortam: {d['environment']['implementation']} {d['environment']['python']}; {d['environment']['system']}; yalnız standart kütüphane.
- Seed: {d['configuration']['seed']}; her oyuncu/süre hücresinde {d['configuration']['samples_per_cell']} kurulum.

```bash
python -B {SCRIPT} --package /absolute/path/OYUN_SIMULASYON_PAKETI_v2.6.zip --authority {d['provenance']['source_head']} --seed {d['configuration']['seed']} --samples-per-cell {d['configuration']['samples_per_cell']}
```

`--check` eklendiğinde dosyaları değiştirmeden kayıtlı hesap ve rapor bütünlüğü
doğrulanır; farklı ortam bilgisi ayrı bildirilir. Paket yeniden indirilirse
manifest hash'i zorunludur. Yeni kaynak/candidate için bu sonuç devralınmaz.
Teslim commit'i bu üç dosyayı taşıyan Git commit'idir; handoff exact commit ve
blobları verir. Bu rapor kabul/kapanış kaydı değildir.

| Girdi | Beklenen Git blob |
|---|---|
{pins}

## Kontrollü A/B bulgusu

A, kilitli v2.6 Deniz ve Kayalık kategori arka yüzlerini ayırır. B, yalnız
`DEC-20260820-01` gereğince bunları BACK_SEA_ROCK altında birleştirir. Ada ve
Fener ayrı kalır. Envanter 30 Deniz, 12 Kayalık, 6 Ada, 4 Fener; Geçilmezler
HAR-KY-01/HAR-KY-03'tür. Kapalı Geçilmezler A'da da diğer Kayalıklardan
ayırt edilemez. Görülmüş ön yüz bilgisi her iki modelde korunur.

52 kimlikten eşit olasılıkla tek kart seçilen ideal etiket modelinde B,
{info['category_bits_removed_per_uniform_map_card']:.6f} bit kategori bilgisini
kaldırır. Arka yüzden ayırt edilemeyen kimlik çiftleri
{info['indistinguishable_unordered_identity_pairs']['A']} → {info['indistinguishable_unordered_identity_pairs']['B']}
olur; ek {info['additional_pairs_merged']} çift tam olarak 30×12 Deniz/Kayalık
çiftidir. Bu, basılı arka yüzün fiziksel sızıntı testi değildir.

6–15 oyuncu × üç süre üzerinden {counts['setups']} geçerli açılış üretildi;
aynı board/seed üzerinde iki görünürlük modeli uygulandı. Bütün kurulumlar
spec'ten ayrı yazılmış kota, komşuluk ve Ada→Liman yol denetimlerini geçti.
{counts['mixed_sea_rock_first_horizons']} açılışta ilk Ufukta hem Deniz hem
Kayalık vardı. Sıradan oyuncu için toplam
{counts['category_distinctions_lost_ordinary_pairs']} aday çifti arasındaki
kategori ayrımı silindi; Kaptanın başlangıç bakışı korunduğunda bu sayı
{counts['category_distinctions_lost_captain_pairs']}. Bunlar kurulum örnekleminin
betimidir; insan oyunu frekansı veya kazanma oranı değildir. JSON, her örneğin
seed'ini, kimlikli haritasını, limanlarını, bakışını ve iki gözlemini içerir.

## Tek amaçlı, konumsuz risk örneği

Aşağıdaki ayrı sonlu deneyde kurulumun yalnız Deniz/Kayalık havuzundan iki
farklı kart eşit olasılıkla çekilir. Amaç sadece Geçilmez seçmemektir. A,
görüyorsa Deniz'i seçer; eşit görünen seçeneklerde iki model de ilk konumu
seçer. Bütün sıralı çiftler tüketilmiştir; örnekleme hatası yoktur.

| Kota kaynağı | Deniz / Kayalık / Geçilmez | A: Geçilmez seçimi | B: Geçilmez seçimi |
|---|---:|---:|---:|
{table}

Bu tablo **yasal ilk Ufuk riski değildir**: konum, son satır yasağı, Ada
komşuluğu, kurulum elemesi, özel bilgi, oylar ve geri dönüş dışarıdadır.
Kapalı kartlar için tek tek bağımsız zar gibi yorumlanamaz. A'nın bu dar
amaçtaki avantajı ortak arka yüzün oyuna uygun olmadığını kanıtlamaz; B'nin
artan bilgi ihtiyacı da daha eğlenceli olduğunu kanıtlamaz.

## Motor bulguları — tam oyun kanıt kapısı FAIL

1. **PREFLIGHT-ENGINE-01 / gizli bilgi erişimi.**
   `AuditGame._make_claims`, bilgisiz Hainin blöf hedefini `true_worst`
   üzerinden seçer. Seed 0, dengeli persona; iki adayın arkasında da Deniz
   vardır, kişisel/takım/kamusal bilgi boştur. HAR-AD-01/HAR-AD-11 yer
   değiştirince iddia hedefi (0,1) → (0,0) değişir; iki kayıtta da
   `informed=false`. Gözlem ve RNG aynı kaldığı halde karar gizli ön yüze
   bağlıdır. JSON iki dünya ve iddiaları saklar. Bu iki adaylı birim örneği
   tam kurulum değildir; karar yordamının bilgi sınırını sınar.
2. **PREFLIGHT-ENGINE-02 / ilk rota bilgi penceresi.**
   Gerçek kanonik kurulum: 10 oyuncu, kısa oyun, seed 3. Kaptan 7;
   Tayfa oyuncusu 4, ilk hareket öncesinde Kırık Dürbün tüketip (0,1)'i
   öğrenir. Gün 1, gemi hâlâ (-1,2)'dedir. Paket kural kitabı §11.3,
   ilk rota öncesi isteğe bağlı bilgi güçlerini yasaklar. `run` gerçek bilgi
   yordamını çalıştırır; test yalnız ilk `move_once` çağrısında durdurur.
   Açılış bilgi avantajı bu nedenle baseline sözleşmesini karşılamaz.

Kaynak motor değiştirilmedi. Bu bulgular düzeltilmeden yalnız kategori
ortalamalarını birleştiren bir A/B yaması geçerli denge kanıtı olmaz.
`look_for_player`, `look_for_hains`, `perceived_value` ve ek hareket kararları
da gerçek kategoriye erişir; B için bütün karar girdilerinin görünür bilgi
sınırından geçirilmesi bağımsız yeni motor görevinin kapsamı olmalıdır.

## Sınırlar ve teslim

- Tamamlanmış oyun: **0**. Yapılanlar: matematiksel bilgi modeli, sonlu
  iki-seçenek deneyi, eşleştirilmiş açılış gözlemleri ve motor tekrar testleri.
- İnsan eğlencesi, güven, şüphe, tempo ve denge hakkında PASS verilmedi.
  Kabul eşiği veya insan verisi uydurulmadı.
- Sonraki açık işler: iki motor bulgusu, gözleme bağlı A/B motoru, tam
  simülasyon, kör insan testi ve fiziksel bilgi sızıntısı/baskı proof'u.
- MEC-001 OPEN. Üretim/PDF/release/lock izinleri false; v2.6 değişmedi.
- Yalnız görevdeki üç QA çıktısı teslim edilir. CHIEF_EDITOR exact commit
  ve blobları bağımsız inceleyip kabul/kapanış kaydını yönetir.
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--authority", default=AUTHORITY)
    parser.add_argument("--seed", type=int, default=20260905)
    parser.add_argument("--samples-per-cell", type=int, default=32)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    require(1 <= args.samples_per_cell <= 1000, "SAMPLE_LIMIT")
    root = Path(__file__).resolve().parents[4]
    task, manifest, provenance = read_authority(root, args.authority)
    files, package_info = load_package(args.package, manifest)
    delta = next(p for p in provenance["input_hashes"] if p["path"].endswith("OYUN_SIMULASYON_SPEC_v2.5.delta.json"))
    package_delta = files["OYUN_SIMULASYON_SPEC_v2.5.delta.json"]
    require(json.loads(package_delta) == json.loads(git(root, "show", f"{args.authority}:{delta['path']}")), "NESTED_DELTA_SEMANTIC_DRIFT")
    package_info["delta_reconciliation"] = {"repository_sha256": delta["sha256"], "package_sha256": digest(package_delta), "json_values_equal": True, "byte_equal": digest(package_delta) == delta["sha256"]}
    spec = json.loads(files[SPEC])
    sys.dont_write_bytecode = True
    with tempfile.TemporaryDirectory(prefix="foulwake-sea-rock-") as tmp:
        for name, data in files.items():
            (Path(tmp) / name).write_bytes(data)
        sys.path.insert(0, tmp)
        try:
            m = importlib.import_module("tam_sistem_sim_v2_5")
            checks = engine_checks(m, spec)
            sampled = sample_openings(m, spec, args.seed, args.samples_per_cell)
        finally:
            sys.path.remove(tmp)
    d = {"schema_version": 1, "task_id": TASK, "result": RESULT, "MEC-001": "OPEN",
         "provenance": provenance, "package": package_info,
         "script_sha256": digest(Path(__file__).read_bytes()),
         "environment": {"implementation": platform.python_implementation(), "python": platform.python_version(), "system": platform.system(), "machine": platform.machine(), "dependencies": "Python standard library only"},
         "configuration": {"seed": args.seed, "samples_per_cell": args.samples_per_cell, "players": list(range(6, 16)), "lengths": ["short", "normal", "long"], "seed_formula": "master + n*1000000 + length_index*10000 + sample_index", "completed_games": 0},
         "information": information_metrics(spec["cards"]["maps"]),
         "isolated_two_choice": isolated_two_choice(spec), "engine_validation": checks, "paired_openings": sampled,
         "open_blockers": ["MEC-001", "PREFLIGHT-ENGINE-01", "PREFLIGHT-ENGINE-02", "FULL_OBSERVATION_CORRECT_AB_SIMULATION", "HUMAN_PLAYTEST", "BLIND_PHYSICAL_LEAK_AND_PRINT_PROOF"]}
    result_bytes = canonical(d) + b"\n"
    report = report_text(d, digest(result_bytes))
    if args.check:
        saved_bytes = (root / RESULTS).read_bytes()
        saved = json.loads(saved_bytes)
        require((root / REPORT).read_text(encoding="utf-8") == report_text(saved, digest(saved_bytes)), "REPORT_OR_RESULTS_INTEGRITY_DRIFT")
        environment_matches = saved["environment"] == d["environment"]
        actual_computation = {k: v for k, v in d.items() if k != "environment"}
        saved_computation = {k: v for k, v in saved.items() if k != "environment"}
        require(canonical(actual_computation) == canonical(saved_computation), "REPRODUCTION_DRIFT")
        print(json.dumps({"reproduction": "MATCH", "environment_matches": environment_matches, "result": RESULT, "engine_gate": checks["full_game_evidence_gate"], "setups": sampled["totals"]["setups"]}))
    else:
        (root / RESULTS).write_bytes(result_bytes)
        (root / REPORT).write_text(report, encoding="utf-8")
        print(json.dumps({"result": RESULT, "engine_gate": checks["full_game_evidence_gate"], "paired_openings": sampled["totals"], "outputs": [SCRIPT, RESULTS, REPORT]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
