#!/usr/bin/env python3
"""Compact v2.3 release-lock validator.

The full card catalog, detailed rules, simulations and PDFs live in the locked
Library package referenced by SOURCE_PACKAGE.md. This repository-side check
validates the v2.3 release contract and recorded test evidence.
"""
from pathlib import Path
import json

ROOT = Path(__file__).parent
SPEC = ROOT / "OYUN_SIMULASYON_SPEC_v2.3.delta.json"
MANIFEST = ROOT / "V23_RELEASE_MANIFEST.json"

EXPECTED_BY_MAP = {"5x5":1,"5x6":1,"6x5":1,"5x7":2,"6x6":2,"6x7":2}
EXPECTED_IDS = ["HAR-KY-01", "HAR-KY-03"]

def main():
    s=json.loads(SPEC.read_text(encoding="utf-8"))
    m=json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors=[]
    md=s.get("metadata",{})
    mp=s.get("map_pool",{})
    setup=s.get("setup",{})
    move=s.get("movement",{})
    if md.get("version")!="2.3" or md.get("stable") is not True or md.get("status")!="stable-locked": errors.append("stable metadata")
    if mp.get("total_map_cards")!=52 or mp.get("rock_cards_total")!=12 or mp.get("impassable_rock_cards_total")!=2: errors.append("52/12/2 card contract")
    ids=[x.get("card_id") for x in mp.get("replacements",[])]
    if ids!=EXPECTED_IDS or mp.get("closed_category_face_distinguishable_from_other_rocks") is not False: errors.append("hidden impassable IDs/face")
    if setup.get("impassable_rocks_by_map")!=EXPECTED_BY_MAP or setup.get("counts_inside_existing_rock_quota") is not True: errors.append("map-size quota")
    reveal=move.get("on_reveal_impassable",{})
    if not (move.get("unknown_rock_can_be_route_target") and move.get("unknown_rock_can_be_horizon_target")): errors.append("hidden target semantics")
    if reveal.get("ship_enters_card") is not False or reveal.get("ship_stays_on_previous_square") is not True or reveal.get("normal_move_day_spent") is not True: errors.append("reveal movement semantics")
    if move.get("known_impassable_is_legal_route_or_horizon") is not False: errors.append("revealed blocker semantics")
    v=m.get("validation",{})
    if (v.get("validator"),v.get("geometry_total"),v.get("geometry_legal"),v.get("geometry_rejected"),v.get("permanent_route_locks"),v.get("setup_errors")) != ("PASS",51204,51102,102,0,0): errors.append("recorded validation evidence")
    c=m.get("cards_contract",{})
    if c.get("map_cards")!=52 or c.get("rock_cards")!=12 or c.get("total_card_identities")!=118 or c.get("impassable_card_ids")!=EXPECTED_IDS: errors.append("manifest card contract")
    if errors:
        print("SONUC: FAIL")
        for e in errors: print("-",e)
        raise SystemExit(1)
    print("SONUC: PASS")
    print("- v2.3 STABLE / LOCKED")
    print("- 52 Harita / 12 Kayalık / 2 gizli Geçilmez / 118 kimlik")
    print("- HAR-KY-01 + HAR-KY-03 kapalıyken ayırt edilemez")
    print("- 51.204 geometri / 51.102 yasal / 102 reddedilecek / kalıcı kilit 0")

if __name__ == "__main__":
    main()
