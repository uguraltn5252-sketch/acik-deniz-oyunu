#!/usr/bin/env python3
"""Repo-side v2.5 validator. Recomputes blocker geometry/baseline relocation and checks locked evidence contracts."""
from __future__ import annotations
import itertools,json
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).parent
EXPECTED_IMPASSABLE={'5x5':1,'5x6':1,'6x5':1,'5x7':2,'6x6':2,'6x7':2}
EXPECTED_INVALID={'5x5':0,'5x6':0,'6x5':8,'5x7':20,'6x6':50,'6x7':24}
def can_reach(r,c,h,p):return -1<=r<h and abs(c-p)<=h-1-r
def fwd(r,c,w,h,p,b=frozenset()):
 nr=r+1
 if nr>=h:return []
 return [(nr,nc) for nc in (c-1,c,c+1) if 0<=nc<w and (nr,nc) not in b and can_reach(nr,nc,h,p)]
def path(w,h,s,p,b):
 states={s}
 for r in range(h):
  states={nc for c in states for nc in (c-1,c,c+1) if 0<=nc<w and (r,nc) not in b and can_reach(r,nc,h,p)}
  if not states:return False
 return p in states
@lru_cache(None)
def pc(w,h,s,p,b):return path(w,h,s,p,frozenset(b))
def legal(w,h,s,p,b,k):return len(b)==k and all(r!=h-1 for r,_ in b) and bool(fwd(-1,s,w,h,p,b)) and path(w,h,s,p,b)
def reachable(w,h,s,p,b):
 seen={(-1,s)};q=[(-1,s)]
 while q:
  r,c=q.pop()
  for x in fwd(r,c,w,h,p,b):
   if x not in seen:seen.add(x);q.append(x)
 return seen
def swap(b,a,d):
 z=set(b);aa=a in z;dd=d in z;z.discard(a);z.discard(d)
 if aa:z.add(d)
 if dd:z.add(a)
 return frozenset(z)
def geometry():
 total=ok=bad=locks=0;by={}
 for shape,k in EXPECTED_IMPASSABLE.items():
  w,h=map(int,shape.split('x'));cells=[(r,c) for r in range(h-1) for c in range(w)];x=0
  for s in range(w):
   for p in range(w):
    for co in itertools.combinations(cells,k):
     total+=1;b=frozenset(co)
     if not legal(w,h,s,p,b,k):bad+=1;x+=1;continue
     ok+=1
     if not path(w,h,s,p,b):locks+=1
  by[shape]=x
 return {'total':total,'legal':ok,'invalid':bad,'invalid_by_shape':by,'permanent_first_branch_locks':locks}
def relocation():
 attempts=unsafe=accepted=0;by=defaultdict(lambda:{'attempts':0,'unsafe_rolled_back':0,'accepted_locks':0})
 for shape,k in EXPECTED_IMPASSABLE.items():
  w,h=map(int,shape.split('x'));cells=[(r,c) for r in range(h-1) for c in range(w)]
  for s in range(w):
   for p in range(w):
    for co in itertools.combinations(cells,k):
     b=frozenset(co)
     if not legal(w,h,s,p,b,k):continue
     for r,c in reachable(w,h,s,p,b):
      near=fwd(r,c,w,h,p,frozenset())
      for a,d in itertools.combinations(near,2):
       attempts+=1;by[shape]['attempts']+=1;m=swap(b,a,d)
       if not pc(w,h,s,p,tuple(sorted(m))):unsafe+=1;by[shape]['unsafe_rolled_back']+=1
       elif not pc(w,h,s,p,tuple(sorted(m))):accepted+=1;by[shape]['accepted_locks']+=1
 return {'attempts':attempts,'unsafe_rolled_back':unsafe,'accepted_permanent_locks':accepted,'by_shape':dict(by)}
def main():
 e=[]
 delta=json.loads((ROOT/'OYUN_SIMULASYON_SPEC_v2.5.delta.json').read_text())
 man=json.loads((ROOT/'V25_RELEASE_MANIFEST.json').read_text())
 aud=json.loads((ROOT/'V25_EXHAUSTIVE_AUDIT.json').read_text())
 pdf=json.loads((ROOT/'V25_PDF_AUDIT.json').read_text())
 if delta['metadata'].get('status')!='STABLE / LOCKED' or not delta['metadata'].get('locked'):e.append('delta lock')
 if not delta['relocation_guard'].get('preserve_recoverable_island_then_port_path_when_scurvy_active'):e.append('scurvy relocation')
 if delta['island_adjacency'].get('scope')!='game_wide_invariant':e.append('adjacency scope')
 if not delta['opening_power_contract'].get('ration_owner_draws_real_power_after_scurvy_resolution'):e.append('ration draw')
 if man.get('status')!='STABLE / LOCKED' or not man.get('locked'):e.append('manifest lock')
 if man['tests']['full_balance']['games']!=100200 or not (0.49<=man['tests']['full_balance']['crew_win']<=0.515):e.append('balance evidence')
 if aud['scurvy_5x5_exact']['accepted_violations']!=0 or aud['scurvy_6m_sample']['accepted_violations']!=0 or aud['island_adjacency_50k']['accepted_adjacency_violations']!=0:e.append('v2.5 safety evidence')
 if pdf.get('status')!='PASS' or pdf.get('rock_back_max_pixel_diff')!=0 or pdf.get('main_card_ids_found')!=118:e.append('pdf audit')
 g=geometry();r=relocation()
 if g['total']!=51204 or g['legal']!=51102 or g['invalid']!=102 or g['invalid_by_shape']!=EXPECTED_INVALID or g['permanent_first_branch_locks']!=0:e.append('geometry')
 if r['attempts']!=1667231 or r['unsafe_rolled_back']!=20 or r['accepted_permanent_locks']!=0:e.append('relocation')
 if e:
  print('SONUC: FAIL');[print('-',x) for x in e];raise SystemExit(1)
 print('SONUC: PASS');print('GEOMETRY_AUDIT',json.dumps(g,ensure_ascii=False));print('RELOCATION_AUDIT',json.dumps(r,ensure_ascii=False))
if __name__=='__main__':main()
