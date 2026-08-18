#!/usr/bin/env python3
"""OYUN v2.2 compact machine-contract validator.

Not a social balance simulator. Validates v2.2 invariants and exhaustive
Impassable Rock geometry against the machine-readable v2.2 delta spec.
"""
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path

SPEC = Path(__file__).with_name('OYUN_SIMULASYON_SPEC_v2.2.json')
EXPECTED_TRAITORS={'6':1,'7':2,'8':3,'9':3,'10':3,'11':4,'12':4,'13':4,'14':5,'15':5}
EXPECTED_IMPASSABLE={'5x5':1,'5x6':1,'6x5':1,'5x7':2,'6x6':2,'6x7':2}
EXPECTED_INVALID={'5x5':0,'5x6':0,'5x7':20,'6x5':8,'6x6':50,'6x7':24}
EXPECTED_CARDS={'characters':20,'powers':30,'scurvy':1,'loyalties':15,'maps':52,'total_identities':118}
CARD_HASH='bdfaff343cdff14af5ad2d93125bb82860fdc2d3c5746b3ede900d821612bd65'

def load():
    return json.loads(SPEC.read_text(encoding='utf-8'))

def can_reach(row,col,h,port):
    return 0 <= col and 0 <= port and -1 <= row < h and abs(col-port) <= h-1-row

def forward(row,col,w,h,port,blocked=frozenset()):
    nr=row+1
    return [(nr,nc) for nc in (col-1,col,col+1)
            if 0<=nr<h and 0<=nc<w and (nr,nc) not in blocked and can_reach(nr,nc,h,port)]

def far_horizon(row,col,w,h,port,blocked=frozenset()):
    target=row+2
    if target>=h: return []
    near=forward(row,col,w,h,port,blocked)
    out=[]
    for tc in (col-1,col,col+1):
        if not (0<=tc<w) or (target,tc) in blocked or not can_reach(target,tc,h,port): continue
        if any((target,tc) in forward(nr,nc,w,h,port,blocked) for nr,nc in near): out.append((target,tc))
    return out

def path_exists(w,h,start,port,blocked):
    cols={start}
    for r in range(h):
        nxt=set()
        for c in cols:
            nxt.update(nc for _,nc in forward(r-1,c,w,h,port,blocked))
        cols=nxt
        if not cols: return False
    return port in cols

def legal_blockers(w,h,start,port,blocked,expected_count):
    return (len(blocked)==expected_count and
            all(r != h-1 for r,_ in blocked) and
            bool(forward(-1,start,w,h,port,blocked)) and
            path_exists(w,h,start,port,blocked))

def emergency_reverse(row,col,w,h,port,blocked,has_previous=True):
    if not has_previous or row<0: return False
    return not forward(row,col,w,h,port,blocked) and bool(forward(row,col,w,h,port,frozenset()))

def audit_geometry():
    total=legal=invalid=0; invalid_by={}
    for shape,count in EXPECTED_IMPASSABLE.items():
        w,h=map(int,shape.split('x')); bad=0
        cells=[(r,c) for r in range(h-1) for c in range(w)]
        for start in range(w):
            for port in range(w):
                for combo in itertools.combinations(cells,count):
                    total+=1; blocked=frozenset(combo)
                    if legal_blockers(w,h,start,port,blocked,count): legal+=1
                    else: invalid+=1; bad+=1
        invalid_by[shape]=bad
    return {'total':total,'legal':legal,'invalid':invalid,'invalid_by_shape':invalid_by}

def validate(s):
    e=[]
    m=s.get('metadata',{}); inh=s.get('inheritance',{}); setup=s.get('setup',{}); cap=s.get('captain',{}); mov=s.get('movement',{}); night=s.get('night',{}); gate=s.get('release_gate',{})
    if m.get('version')!='2.2' or m.get('baseline_release')!='v2.1': e.append('version/baseline')
    if m.get('stable') is not False: e.append('v2.2 must remain development until release gate')
    if inh.get('starting_hull')!=2: e.append('starting hull')
    if inh.get('card_counts')!=EXPECTED_CARDS: e.append('card counts/118 identities')
    if inh.get('canonical_cards_sha256')!=CARD_HASH: e.append('canonical card hash')
    if setup.get('traitors')!=EXPECTED_TRAITORS: e.append('traitor table')
    if setup.get('impassable_rocks_by_map')!=EXPECTED_IMPASSABLE: e.append('impassable count table')
    if setup.get('start',{}).get('fixed_center') is not False: e.append('dynamic start')
    if not setup.get('first_route_fog_free'): e.append('initial fog ban')
    if not setup.get('initial_setup_must_have_path_via_island_to_port'): e.append('setup path-via-island contract')
    if cap.get('permanent_core_role') is not True or cap.get('can_be_removed_from_game') is not False: e.append('captain permanence')
    if cap.get('wakes_separately_at_night') is not False or cap.get('office_grants_horizon_info') is not False: e.append('captain night/info')
    need={'successful_mutiny','death','chamber','stranded','boatman_rescue_trip'}
    if set(cap.get('replacement_triggers',[]))!=need: e.append('captain replacement triggers')
    if cap.get('route_vote_weight')!=2 or cap.get('other_vote_weight')!=1: e.append('captain vote weights')
    er=mov.get('emergency_reverse',{})
    if not er.get('enabled') or er.get('retrigger_event_on_return') is not False or er.get('cannot_reverse_to_outside_start') is not True: e.append('emergency reverse contract')
    if night.get('captain_extra_wake') is not False: e.append('night captain extra wake')
    if not all(gate.get(k) for k in ('human_rules','machine_spec','validator','core_validation_pass')): e.append('core release gate')
    if gate.get('final_release_lock') is not False: e.append('premature final release lock')
    if forward(-1,0,5,5,0)!=[(0,0),(0,1)]: e.append('edge start near horizon')
    if forward(-1,0,6,5,5)!=[(0,1)]: e.append('port reachability initial filter')
    if forward(-1,0,5,5,0,frozenset({(0,1)}))!=[(0,0)]: e.append('blocked target exclusion')
    if legal_blockers(5,5,2,2,frozenset({(4,2)}),1): e.append('final row rock ban')
    if not emergency_reverse(0,1,6,5,5,frozenset({(1,2)}),True): e.append('rock-caused reverse should open')
    if emergency_reverse(0,1,6,5,5,frozenset(),True): e.append('reverse opens with forward route')
    if emergency_reverse(-1,0,6,5,5,frozenset({(0,1)}),False): e.append('reverse to outside start')
    return e

def main():
    p=argparse.ArgumentParser(); p.add_argument('--validate-only',action='store_true'); p.add_argument('--geometry-audit',action='store_true'); a=p.parse_args()
    s=load(); errs=validate(s)
    audit=None
    if a.geometry_audit:
        audit=audit_geometry()
        evidence=s['validation_evidence']
        expected={'total':evidence['geometry_total'],'legal':evidence['geometry_legal'],'invalid':evidence['geometry_invalid'],'invalid_by_shape':evidence['invalid_by_shape']}
        if audit!=expected: errs.append(f'geometry audit mismatch: {audit} != {expected}')
        if audit['invalid_by_shape']!=EXPECTED_INVALID: errs.append('invalid-by-shape regression')
    if errs:
        print('SONUC: FAIL'); [print('-',x) for x in errs]; raise SystemExit(1)
    print('SONUC: PASS')
    print('- v2.2 geliştirme sürümü / v2.1 baseline sözleşmesi doğru.')
    print('- 118 kart kimliği ve v2.1 kanonik kart karması miras yoluyla kilitli.')
    print('- Gövde 2; dinamik başlangıç; 1/2 Geçilmez Kayalık; Kaptan omurgası doğru.')
    print('- Acil geri dönüş yalnız Kayalık kaynaklı tam çıkmaz koşuluna bağlı.')
    if audit: print('GEOMETRY_AUDIT:',json.dumps(audit,ensure_ascii=False,sort_keys=True))

if __name__=='__main__': main()
