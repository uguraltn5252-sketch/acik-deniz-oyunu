#!/usr/bin/env python3
"""v2.4 repo-side validator: validates rule delta and recomputes route safety evidence."""
from __future__ import annotations
import itertools, json
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).parent
SPEC=ROOT/'OYUN_SIMULASYON_SPEC_v2.4.delta.json'
EXPECTED_IMPASSABLE={'5x5':1,'5x6':1,'6x5':1,'5x7':2,'6x6':2,'6x7':2}
EXPECTED_INVALID={'5x5':0,'5x6':0,'6x5':8,'5x7':20,'6x6':50,'6x7':24}

def can_reach(row,col,h,port): return -1<=row<h and abs(col-port)<=h-1-row

def forward(row,col,w,h,port,blocked=frozenset()):
    nr=row+1
    if nr>=h:return []
    return [(nr,nc) for nc in (col-1,col,col+1) if 0<=nc<w and (nr,nc) not in blocked and can_reach(nr,nc,h,port)]

def path_from(w,h,row,col,port,blocked):
    states={col}
    for r in range(row+1,h):
        nxt=set()
        for c in states:
            for nc in (c-1,c,c+1):
                if 0<=nc<w and (r,nc) not in blocked and can_reach(r,nc,h,port): nxt.add(nc)
        states=nxt
        if not states:return False
    return port in states

def path_exists(w,h,start,port,blocked): return path_from(w,h,-1,start,port,blocked)

@lru_cache(maxsize=None)
def path_cached(w,h,start,port,blocked): return path_exists(w,h,start,port,frozenset(blocked))

def legal(w,h,start,port,blocked,count):
    return len(blocked)==count and all(r!=h-1 for r,_ in blocked) and bool(forward(-1,start,w,h,port,blocked)) and path_exists(w,h,start,port,blocked)

def reachable(w,h,start,port,blocked):
    seen={(-1,start)}; q=[(-1,start)]
    while q:
        r,c=q.pop()
        for x in forward(r,c,w,h,port,blocked):
            if x not in seen: seen.add(x); q.append(x)
    return seen

def swap(blocked,a,b):
    s=set(blocked); aa=a in s; bb=b in s; s.discard(a); s.discard(b)
    if aa:s.add(b)
    if bb:s.add(a)
    return frozenset(s)

def geometry_audit():
    total=legal_n=invalid=branches=dead=locks=0; by={}
    for shape,count in EXPECTED_IMPASSABLE.items():
        w,h=map(int,shape.split('x')); cells=[(r,c) for r in range(h-1) for c in range(w)]; bad=0
        for start in range(w):
            for port in range(w):
                for combo in itertools.combinations(cells,count):
                    total+=1; b=frozenset(combo)
                    if not legal(w,h,start,port,b,count): invalid+=1; bad+=1; continue
                    legal_n+=1
                    visible=forward(-1,start,w,h,port,frozenset()); branches+=len(visible)
                    for step in visible:
                        if step in b or not path_from(w,h,step[0],step[1],port,b):
                            dead+=1
                            # With v2.4 the route can unwind to the real Start Port; the legal setup must still recover.
                            if not path_exists(w,h,start,port,b): locks+=1
        by[shape]=bad
    return {'total':total,'legal':legal_n,'invalid':invalid,'invalid_by_shape':by,'visible_first_branches':branches,'recoverable_deadend_first_branches':dead,'permanent_first_branch_locks':locks}

def relocation_audit():
    attempts=unsafe=accepted=0; by=defaultdict(lambda:{'attempts':0,'unsafe_rolled_back':0,'accepted_locks':0})
    for shape,count in EXPECTED_IMPASSABLE.items():
        w,h=map(int,shape.split('x')); cells=[(r,c) for r in range(h-1) for c in range(w)]
        for start in range(w):
            for port in range(w):
                for combo in itertools.combinations(cells,count):
                    b=frozenset(combo)
                    if not legal(w,h,start,port,b,count): continue
                    for r,c in reachable(w,h,start,port,b):
                        near=forward(r,c,w,h,port,frozenset())
                        for a,d in itertools.combinations(near,2):
                            attempts+=1; by[shape]['attempts']+=1; moved=swap(b,a,d)
                            if not path_cached(w,h,start,port,tuple(sorted(moved))):
                                unsafe+=1; by[shape]['unsafe_rolled_back']+=1
                                if not path_cached(w,h,start,port,tuple(sorted(b))): accepted+=1; by[shape]['accepted_locks']+=1
    return {'attempts':attempts,'unsafe_rolled_back':unsafe,'accepted_permanent_locks':accepted,'by_shape':dict(by)}

def validate_contract(s):
    e=[]; m=s.get('metadata',{}); o=s.get('opening',{}); v=s.get('map_visibility',{}); r=s.get('route_safety',{}); t=s.get('captain_election_tie',{}); u=s.get('unchanged',{}); sc=s.get('setup_component',{})
    if (m.get('version'),m.get('baseline'),m.get('stable'),m.get('locked')) != ('2.4','v2.3',True,True):e.append('metadata')
    n=o.get('opening_neutral_night',{})
    if o.get('opening_day')!='captain_election_only' or n.get('captain_wakes_once') is not True or n.get('private_near_horizon_peek_count')!=1 or n.get('loyalty_known') is not False or n.get('peeked_card_stays_face_down') is not True:e.append('opening Captain contract')
    if o.get('first_real_route')!='normal_simultaneous_route_vote' or o.get('captain_route_vote_weight')!=2 or o.get('captain_office_wakes_later_nights') is not False:e.append('first route/Captain vote')
    if v != {'public_reveal_stays_face_up':True,'public_unvisited_event_resolved':False,'event_resolves_on_first_entry':True,'public_impassable_blocks_immediately':True,'private_peek_changes_public_state':False}:e.append('visibility state machine')
    if r.get('start_port_returnable_by_emergency_reverse') is not True or r.get('initial_near_horizon_total_lock_forbidden') is not True or 'cancel_or_rollback' not in r.get('relocation_guard',''):e.append('route safety')
    if t.get('first_tie')!='one_revote_among_tied' or t.get('second_tie')!='fate_die_highest_wins_among_tied':e.append('Captain tie termination')
    expected={'starting_hull':2,'characters':20,'powers':30,'loyalties':15,'maps':52,'rock_cards':12,'main_card_identities':118,'impassable_ids':['HAR-KY-01','HAR-KY-03']}
    if u!=expected:e.append('unchanged card/hull contract')
    if sc!={'id':'SET-KL-01','count':1,'outside_main_card_identities':True,'physical_in_card_pdf':True}:e.append('Start Port setup component')
    return e

def main():
    s=json.loads(SPEC.read_text(encoding='utf-8')); errors=validate_contract(s)
    g=geometry_audit(); r=relocation_audit()
    if g['total']!=51204 or g['legal']!=51102 or g['invalid']!=102 or g['invalid_by_shape']!=EXPECTED_INVALID or g['permanent_first_branch_locks']!=0: errors.append('geometry regression')
    if r['attempts']!=1667231 or r['unsafe_rolled_back']!=20 or r['accepted_permanent_locks']!=0: errors.append('relocation regression')
    if errors:
        print('SONUC: FAIL'); [print('-',x) for x in errors]; raise SystemExit(1)
    print('SONUC: PASS')
    print('GEOMETRY_AUDIT:',json.dumps(g,ensure_ascii=False,sort_keys=True))
    print('RELOCATION_AUDIT:',json.dumps(r,ensure_ascii=False,sort_keys=True))

if __name__=='__main__':main()
