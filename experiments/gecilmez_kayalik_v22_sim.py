#!/usr/bin/env python3
"""v2.1 sonrası Geçilmez Kayalık + acil geri dönüş deneyi.

Bu dosya stabil v2.1'i değiştirmez. 14 Ağustos tarihli davranışsal Monte Carlo
motorunu kullanarak 18 Ağustos 2026'da kesinleşen aday kuralları sınar:

- Gemi tüm harita boylarında 2 Gövde.
- Başlangıç, alt kenarın dışındaki herhangi bir sütun.
- İlk rotayı Kaptan tek başına seçer.
- 30 kareye kadar 1, 35+ karede 2 Geçilmez Kayalık.
- Geçilmez Kayalık son Harita satırına konulamaz.
- Geçilmez Kayalık fiziksel olarak girilemez ve rota adayı değildir.
- Yalnız Geçilmez Kayalık kaynaklı tam ileri çıkmazda gemi geldiği önceki
  kareye 1 adım geri çekilir; hareket/gün harcanır, olay tekrar çalışmaz.
- Geri çekilinen çıkmaz kolu kamusal olarak öğrenilmiş kabul edilir ve başka
  rota varsa aynı kola hemen tekrar girilmez.

Monte Carlo insan eğlencesini kanıtlamaz; rota kilidi, süre/gece baskısı ve
kazanma dengesi için yapısal bir stres testidir.
"""
from __future__ import annotations

import argparse
import itertools
import json
import random
import statistics
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from tam_sistem_sim import (
    AuditConfig,
    AuditGame,
    RECOMMENDED_HAINS,
    ROCK,
    Event,
    event_is_damage,
)


DAMAGE_QUOTAS = {
    6: ((6, 4), (5, 4)),
    7: ((5, 4), (4, 4)),
    8: ((5, 4), (4, 4)),
    9: ((5, 4), (4, 4)),
    10: ((6, 4), (5, 4)),
    11: ((7, 5), (6, 5)),
    12: ((7, 5), (6, 5)),
    13: ((9, 5), (8, 5)),
    14: ((9, 5), (8, 5)),
    15: ((9, 5), (8, 5)),
}

LENGTH_LABEL = {"short": "Hızlı", "normal": "Standart", "long": "Uzun"}


def reef_count_for(width: int, height: int) -> int:
    return 2 if width * height >= 35 else 1


def damage_quota_for(n: int, length: str) -> tuple[int, int]:
    normal, long = DAMAGE_QUOTAS[n]
    return long if length == "long" else normal


class ReefGame(AuditGame):
    """Yeni görünür Geçilmez Kayalık ve tek-adımlı geri dönüş semantiği."""

    def __init__(self, rng: random.Random, config: AuditConfig, reef_count: int):
        self.required_reef_count = reef_count
        self.reef_coords: set[tuple[int, int]] = set()
        self.reef_dead_end_cells: set[tuple[int, int]] = set()
        super().__init__(rng, config)

    def _install_experimental_maps(self):
        super()._install_experimental_maps()
        width, height = self.voyage.width, self.voyage.height
        eligible_rocks = [
            coord for coord, event in self.grid.items()
            if event.category == ROCK and coord[0] < height - 1
        ]
        safe_rocks = [
            coord for coord, event in self.grid.items()
            if event.category == ROCK and not event_is_damage(event)
        ]
        if len(eligible_rocks) < self.required_reef_count:
            raise RuntimeError("Geçilmez Kayalık için yeterli son-satır-dışı Kayalık yok")
        if len(safe_rocks) < self.required_reef_count:
            raise RuntimeError("Hasar kotasını koruyacak yeterli güvenli Kayalık yok")

        candidates = []
        for start_col in range(width):
            for combo in itertools.combinations(eligible_rocks, self.required_reef_count):
                blocked = frozenset(combo)
                if not self._can_reach_port(-1, start_col, blocked):
                    continue
                first = [
                    x for x in self._raw_candidates_from(-1, start_col)
                    if (x[0], x[1]) not in blocked
                ]
                if first:
                    candidates.append((start_col, combo))
        if not candidates:
            raise RuntimeError("Geçilmez Kayalık + dinamik başlangıç için çözülebilir kurulum bulunamadı")

        self.col, chosen = self.rng.choice(candidates)
        self.row = -1
        self.route_stack = [(-1, self.col)]
        chosen = list(chosen)

        reserved_safe = [c for c in safe_rocks if c not in chosen]
        for coord in chosen:
            if event_is_damage(self.grid[coord]):
                if not reserved_safe:
                    raise RuntimeError("Geçilmez Kayalık dönüşümünde hasar kotası korunamadı")
                donor = reserved_safe.pop()
                self.grid[coord], self.grid[donor] = self.grid[donor], self.grid[coord]
            self.grid[coord] = Event(ROCK, "Geçilmez Kayalık", -1, "impassable_reef")

        self.reef_coords = set(chosen)
        self.public_blocked = set(chosen)
        self.reef_coord = chosen[0] if chosen else None
        self.metrics_count["reef_installed"] = len(chosen)

        assert all(r < height - 1 for r, _ in self.reef_coords)
        assert self._can_reach_port(-1, self.col, frozenset(self.reef_coords))

    def _structural_candidates_from_current(self):
        raw = self._raw_candidates_from(self.row, self.col)
        return [
            x for x in raw
            if (x[0], x[1]) not in self.reef_coords
            and (x[0], x[1]) not in self.reef_dead_end_cells
        ]

    def valid_candidates(self, ignore_effects: bool = False):
        structural = self._structural_candidates_from_current()
        if ignore_effects:
            return structural

        out = structural[:]
        if self.next_center_lock:
            allowed = {0}
            if self.temporary_yeke and self.yeke_extra_dc is not None:
                allowed.add(self.yeke_extra_dc)
            out = [x for x in out if x[2] in allowed]
        if self.next_disabled_dc is not None:
            out = [x for x in out if x[2] != self.next_disabled_dc]

        if not out and structural:
            out = structural
            self.rule_fallbacks += 1
            self.metrics_count["effect_collision"] += 1
        return out

    def horizon_coords(self, far: bool = False):
        coords = super().horizon_coords(far)
        return [
            c for c in coords
            if c not in self.reef_coords and c not in self.reef_dead_end_cells
        ]

    def _reef_caused_dead_end(self) -> bool:
        raw = self._raw_candidates_from(self.row, self.col)
        if not raw:
            return False
        structural = self._structural_candidates_from_current()
        if structural:
            return False
        return all(
            (r, c) in self.reef_coords or (r, c) in self.reef_dead_end_cells
            for r, c, _ in raw
        )

    def _emergency_backtrack(self) -> bool:
        if not self._reef_caused_dead_end():
            return False
        if len(self.route_stack) <= 1:
            self.metrics_count["reef_start_locks"] += 1
            return False

        trapped = (self.row, self.col)
        self.reef_dead_end_cells.add(trapped)
        self.metrics_count["reef_deadends"] += 1

        self.route_stack.pop()
        self.row, self.col = self.route_stack[-1]
        self.metrics_count["reef_backtracks"] += 1
        self.metrics_count["reef_backtrack_steps"] += 1

        self.last_claims = []
        self.last_votes = {}
        self.last_choice = None
        self.last_choice_voters = []

        self.next_center_lock = False
        self.temporary_yeke = False
        self.yeke_extra_dc = None
        self.next_disabled_dc = None
        return True

    def move_once(self, first_move: bool = False, forced: bool = False):
        candidates = self.valid_candidates()
        if not candidates:
            if forced:
                if self._reef_caused_dead_end():
                    self.metrics_count["forced_reef_cancels"] += 1
                    return False, False
            elif self._emergency_backtrack():
                return False, False
            self.finish_reason = "route_lock"
            self.winner = "hain"
            self.rule_fallbacks += 1
            self.metrics_count["hard_route_locks"] += 1
            return False, False
        return super().move_once(first_move=first_move, forced=forced)


def make_config(n: int, length: str, label: str) -> AuditConfig:
    sea_damage, rock_damage = damage_quota_for(n, length)
    return AuditConfig(
        label=label,
        n=n,
        hains=RECOMMENDED_HAINS[n],
        length=length,
        hull=2,
        night_rule="choice_peek1",
        attack_bias=.55,
        rescue_rule="existing",
        politics_rule="two_stage",
        identity_protected=True,
        identity_exchange=True,
        queen_mode="seyir_zabti",
        kayikci_chain="existing",
        route_policy="social",
        persona="dengeli",
        map_pool_variant="candidate52",
        sea_damage_quota=sea_damage,
        rock_damage_quota=rock_damage,
        port_timing="next_morning",
        yama_replacement="kancali_halat",
        captain_double=True,
        first_move_captain=True,
    )


def aggregate(rows: list[dict]) -> dict:
    n = len(rows)
    reasons = Counter(r["reason"] for r in rows)
    def mean(key):
        return statistics.mean(r.get(key, 0) for r in rows)
    return {
        "runs": n,
        "crew_win": sum(r["winner"] == "crew" for r in rows) / n,
        "hain_win": sum(r["winner"] == "hain" for r in rows) / n,
        "reasons": {k: v / n for k, v in sorted(reasons.items())},
        "days": mean("days"),
        "nights": mean("nights"),
        "estimated_minutes": 5 + mean("days") * (2.0 + .34 * rows[0]["n"]),
        "hull_left": mean("hull_left"),
        "attacks": mean("attacks"),
        "contested_rate": mean("contested_rate"),
        "vote_entropy": mean("vote_entropy"),
        "rule_fallbacks": mean("rule_fallbacks"),
        "effect_collision": mean("effect_collision"),
        "reef_installed": mean("reef_installed"),
        "reef_deadends": mean("reef_deadends"),
        "reef_backtracks": mean("reef_backtracks"),
        "reef_backtrack_steps": mean("reef_backtrack_steps"),
        "hard_route_locks": mean("hard_route_locks"),
        "reef_start_locks": mean("reef_start_locks"),
        "forced_reef_cancels": mean("forced_reef_cancels"),
        "games_with_backtrack": sum(r.get("reef_backtracks", 0) > 0 for r in rows) / n,
        "games_with_hard_lock": sum(r.get("hard_route_locks", 0) > 0 for r in rows) / n,
    }


def run_cell(config: AuditConfig, runs: int, seed: int, reefs: int) -> dict:
    master = random.Random(seed)
    rows = []
    setup_errors = 0
    for _ in range(runs):
        try:
            game = ReefGame(random.Random(master.getrandbits(64)), config, reefs)
            rows.append(game.run())
        except RuntimeError:
            setup_errors += 1
    if not rows:
        raise RuntimeError("Hiç oyun kurulamadı")
    out = aggregate(rows)
    out["setup_errors"] = setup_errors
    return {"config": asdict(config), "reef_count": reefs, "summary": out}


def static_geometry_audit(width: int, height: int, reef_count: int) -> dict:
    cells = [(r, c) for r in range(height - 1) for c in range(width)]

    def raw(row, col, port):
        nr = row + 1
        if nr >= height:
            return []
        out = []
        for dc in (-1, 0, 1):
            nc = col + dc
            if 0 <= nc < width and abs(nc - port) <= height - 1 - nr:
                out.append((nr, nc))
        return out

    def can(row, col, port, blocked, memo):
        key = (row, col)
        if key in memo:
            return memo[key]
        if (row, col) in blocked:
            memo[key] = False
        elif row == height - 1:
            memo[key] = col == port
        else:
            memo[key] = any(can(r, c, port, blocked, memo) for r, c in raw(row, col, port))
        return memo[key]

    total = 0
    solvable = 0
    first_locked = 0
    for start in range(width):
        for port in range(width):
            for combo in itertools.combinations(cells, reef_count):
                total += 1
                blocked = frozenset(combo)
                first = [x for x in raw(-1, start, port) if x not in blocked]
                if not first:
                    first_locked += 1
                if first and can(-1, start, port, blocked, {}):
                    solvable += 1
    return {
        "width": width,
        "height": height,
        "reef_count": reef_count,
        "placement_cases": total,
        "solvable_forward_setups": solvable,
        "solvable_ratio": solvable / total if total else 1.0,
        "first_move_fully_blocked": first_locked,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=300, help="her oyuncu/uzunluk hücresi için oyun")
    ap.add_argument("--seed", type=int, default=20260818)
    ap.add_argument("--output", type=Path, default=Path(__file__).with_name("GECILMEZ_KAYALIK_V22_SONUCLARI.json"))
    args = ap.parse_args()

    payload = {
        "meta": {
            "seed": args.seed,
            "runs_per_cell": args.runs,
            "date": "2026-08-18",
            "scope": "2 Gövde + dinamik başlangıç + Kaptan ilk rota + 1/2 Geçilmez Kayalık + yalnız kayalık çıkmazında geri dönüş",
        },
        "geometry": {},
        "cells": [],
    }

    for width, height in [(5,5),(5,6),(6,5),(5,7),(6,6),(6,7)]:
        rc = reef_count_for(width, height)
        payload["geometry"][f"{width}x{height}"] = static_geometry_audit(width, height, rc)

    cell_no = 0
    for length in ("short", "normal", "long"):
        for n in range(6, 16):
            cfg = make_config(n, length, f"{LENGTH_LABEL[length]} {n}p")
            width, height = (5 if n <= 10 else 6), ({"short":5,"normal":6,"long":7}[length])
            target_reefs = reef_count_for(width, height)
            pair_seed = args.seed + cell_no * 100_003
            control = run_cell(cfg, args.runs, pair_seed, 0)
            control["shape"] = f"{width}x{height}"
            control["variant"] = "control_dynamic_start_no_reef"
            reefed = run_cell(cfg, args.runs, pair_seed + 50_000_021, target_reefs)
            reefed["shape"] = f"{width}x{height}"
            reefed["variant"] = "impassable_reef_backtrack"
            cs, rs = control["summary"], reefed["summary"]
            reefed["delta_vs_control"] = {
                "crew_win_pp": (rs["crew_win"] - cs["crew_win"]) * 100,
                "days": rs["days"] - cs["days"],
                "nights": rs["nights"] - cs["nights"],
                "estimated_minutes": rs["estimated_minutes"] - cs["estimated_minutes"],
                "attacks": rs["attacks"] - cs["attacks"],
            }
            payload["cells"].extend([control, reefed])
            print(
                f"{width}x{height} n={n:2} reefs={target_reefs} "
                f"crew {cs['crew_win']*100:5.1f}->{rs['crew_win']*100:5.1f}% "
                f"Δday={rs['days']-cs['days']:+.2f} Δnight={rs['nights']-cs['nights']:+.2f} "
                f"back={rs['games_with_backtrack']*100:5.1f}% hardlock={rs['games_with_hard_lock']*100:4.1f}%"
            )
            cell_no += 1

    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"SONUC: {args.output}")


if __name__ == "__main__":
    main()
