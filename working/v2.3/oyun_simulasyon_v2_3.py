#!/usr/bin/env python3
"""OYUN v2.3 gizli Geçilmez Kayalık statik sözleşme doğrulayıcısı."""
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = HERE / "OYUN_SIMULASYON_SPEC_v2.3.json"


def load_spec():
    return json.loads(SPEC.read_text(encoding="utf-8"))


def geometry(width: int, height: int, blocks: int):
    # Son Liman/Ufuk hattı Geçilmez olamaz.
    cells = [(r,c) for r in range(height-1) for c in range(width)]
    def raw(row,col,port):
        nr=row+1
        if nr>=height: return []
        out=[]
        for dc in (-1,0,1):
            nc=col+dc
            if 0<=nc<width and abs(nc-port)<=height-1-nr:
                out.append((nr,nc))
        return out
    def can(row,col,port,blocked,memo):
        k=(row,col)
        if k in memo: return memo[k]
        if k in blocked: ans=False
        elif row==height-1: ans=(col==port)
        else: ans=any(can(r,c,port,blocked,memo) for r,c in raw(row,col,port))
        memo[k]=ans
        return ans
    total=legal=0
    for start in range(width):
        for port in range(width):
            for combo in itertools.combinations(cells,blocks):
                total += 1
                b=frozenset(combo)
                first=[x for x in raw(-1,start,port) if x not in b]
                if first and can(-1,start,port,b,{}): legal += 1
    return total, legal


def validate(run_geometry=False):
    s=load_spec(); errors=[]
    md=s["metadata"]; cards=s["cards"]; setup=s["setup"]; hidden=s["hidden_map_semantics"]; reveal=s["reveal_semantics"]; cap=s["captain"]
    if md["version"]!="2.3" or md["baseline_release"]!="v2.2": errors.append("version/baseline")
    if cards["map_cards"]!=52 or cards["map_categories"]!={"Acik Deniz":30,"Kayalik":12,"Ada":6,"Deniz Feneri":4}: errors.append("map counts")
    if cards["total_card_identities"]!=118: errors.append("118 identities")
    reefs=cards["impassable_rock_cards"]
    if [x["id"] for x in reefs] != ["HAR-KY-01","HAR-KY-03"]: errors.append("reef ids")
    if not all(x["category_face"]=="KAYALIK" and x["indistinguishable_from_other_rocks"] and x["impassable"] for x in reefs): errors.append("hidden category face")
    if setup["impassable_is_overlay_marker"] or not setup["impassable_is_map_card"] or not setup["counts_inside_rock_quota"]: errors.append("map-card integration")
    expected={"5x5":1,"5x6":1,"6x5":1,"5x7":2,"6x6":2,"6x7":2}
    if setup["impassable_count_by_shape"]!=expected: errors.append("shape counts")
    if not hidden["closed_impassable_is_route_candidate"] or not hidden["closed_impassable_is_horizon_candidate"] or hidden["special_visible_symbol_or_marker"]: errors.append("hidden route semantics")
    if reveal["ship_enters_square"] or not reveal["ship_stays_at_previous_position"] or not reveal["normal_route_day_consumes_movement"] or not reveal["card_stays_face_up"]: errors.append("reveal semantics")
    if setup["starting_hull"]!=2: errors.append("hull")
    if not cap["permanent_role"] or not cap["first_route_selected_by_captain_alone_blind"] or cap["night_wakeup"] or cap["automatic_horizon_information"]: errors.append("captain")
    result={}
    if run_geometry:
        invalid_by={}; total=legal=0
        for shape,n in expected.items():
            w,h=map(int,shape.split("x")); t,l=geometry(w,h,n); total+=t; legal+=l; invalid_by[shape]=t-l
        result={"total":total,"legal":legal,"invalid":total-legal,"invalid_by_shape":invalid_by}
        ev=s["technical_evidence"]["geometry"]
        if total!=ev["total"] or legal!=ev["legal"] or total-legal!=ev["invalid"] or invalid_by!=ev["invalid_by_shape"]: errors.append("geometry evidence")
    if errors:
        print("SONUC: FAIL")
        for e in errors: print("-",e)
        raise SystemExit(1)
    print("SONUC: PASS")
    print("- v2.3 / v2.2 baseline sözleşmesi doğru.")
    print("- 52 Harita / 12 Kayalık / 2 gizli Geçilmez / 118 toplam kimlik doğru.")
    print("- HAR-KY-01 ve HAR-KY-03 Geçilmez; kategori yüzünde ayırt edilemez.")
    print("- Kapalı Geçilmez normal Ufuk/rota hedefidir; açılınca Gemi giremez ve kart kamusal engel olur.")
    print("- Kaptan omurgası ve 2 Gövde korunur.")
    if run_geometry: print("GEOMETRY_AUDIT:", json.dumps(result,ensure_ascii=False,sort_keys=True))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--validate-only",action="store_true"); ap.add_argument("--geometry-audit",action="store_true"); a=ap.parse_args()
    validate(a.geometry_audit)

if __name__=="__main__": main()
