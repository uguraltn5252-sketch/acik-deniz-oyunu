#!/usr/bin/env python3
from __future__ import annotations
import argparse, itertools, json, random, statistics, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import tam_sistem_sim as t
from tam_sistem_sim import AuditConfig, AuditGame, Event, RECOMMENDED_HAINS, SEA, ROCK, ISLAND, LIGHT, event_is_damage

DAMAGE_QUOTAS = {
    6: ((6,4),(5,4)),7:((5,4),(4,4)),8:((5,4),(4,4)),9:((5,4),(4,4)),10:((6,4),(5,4)),
    11:((7,5),(6,5)),12:((7,5),(6,5)),13:((9,5),(8,5)),14:((9,5),(8,5)),15:((9,5),(8,5)),
}

SAFE_ROCK_LABELS = [
    'Ufak Kayalık', 'Batık Kalyon#1', 'Batık Kalyon#2', 'Gizli Geçit',
    'Kaçakçı Oyuğu', 'Kırılan Sandıklar', 'İki Taraftan Sıyırdık'
]

def reef_count_for(w,h): return 2 if w*h >= 35 else 1

def damage_quota_for(n,length):
    a,b=DAMAGE_QUOTAS[n]
    return b if length=='long' else a

def build_pool(pair: tuple[int,int]) -> list[Event]:
    pool=list(t.CANDIDATE_MAP_POOL)
    safe_indices=[i for i,e in enumerate(pool) if e.category==ROCK and not event_is_damage(e)]
    assert len(safe_indices)==7
    for j, safe_pos in enumerate(pair, 1):
        idx=safe_indices[safe_pos]
        pool[idx]=Event(ROCK, f'Geçilmez Kayalık {j}', -1, 'impassable_reef')
    assert len(pool)==52
    assert sum(e.category==ROCK for e in pool)==12
    assert sum(event_is_damage(e) for e in pool if e.category==ROCK)==5
    assert sum(e.kind=='impassable_reef' for e in pool)==2
    return pool

def path_exists(w,h,start,port,blocked):
    cols={start}
    for r in range(h):
        nxt=set()
        for c in cols:
            for nc in (c-1,c,c+1):
                if 0<=nc<w and (r,nc) not in blocked and abs(nc-port)<=h-1-r:
                    nxt.add(nc)
        cols=nxt
        if not cols:return False
    return port in cols

def path_via_island(w,h,start,port,blocked,islands):
    states={(start,False)}
    for r in range(h):
        nxt=set()
        for c,seen in states:
            for nc in (c-1,c,c+1):
                if 0<=nc<w and (r,nc) not in blocked and abs(nc-port)<=h-1-r:
                    nxt.add((nc, seen or (r,nc) in islands))
        states=nxt
        if not states:return False
    return (port,True) in states

class HiddenReefGame(AuditGame):
    def __init__(self, rng, config, pool, reef_count):
        self._v23_pool=pool
        self.required_reef_count=reef_count
        self.reef_coords=set()
        self.reef_dead_end_cells=set()
        old=t.CANDIDATE_MAP_POOL
        t.CANDIDATE_MAP_POOL=pool
        try:
            super().__init__(rng,config)
        finally:
            t.CANDIDATE_MAP_POOL=old

    def _setup_map(self):
        by_cat={cat:[e for e in self.map_pool if e.category==cat] for cat in (SEA,ROCK,ISLAND,LIGHT)}
        sea_damage, rock_damage = self.config.sea_damage_quota, self.config.rock_damage_quota
        reef_events=[e for e in by_cat[ROCK] if e.kind=='impassable_reef']
        rock_damage_events=[e for e in by_cat[ROCK] if event_is_damage(e)]
        rock_safe=[e for e in by_cat[ROCK] if not event_is_damage(e) and e.kind!='impassable_reef']
        if len(reef_events)<self.required_reef_count: raise RuntimeError('reef cards')
        for _attempt in range(5000):
            selected=[]
            sea_d=[e for e in by_cat[SEA] if event_is_damage(e)]; sea_s=[e for e in by_cat[SEA] if not event_is_damage(e)]
            sq=self.voyage.quotas[SEA]
            selected += self.rng.sample(sea_d, sea_damage) + self.rng.sample(sea_s, sq-sea_damage)
            rq=self.voyage.quotas[ROCK]
            need_safe=rq-rock_damage-self.required_reef_count
            if need_safe<0 or need_safe>len(rock_safe): raise RuntimeError('rock quota')
            chosen_reefs=self.rng.sample(reef_events,self.required_reef_count)
            selected += self.rng.sample(rock_damage_events,rock_damage)+chosen_reefs+self.rng.sample(rock_safe,need_safe)
            selected += self.rng.sample(by_cat[ISLAND], self.voyage.quotas[ISLAND])
            selected += self.rng.sample(by_cat[LIGHT], self.voyage.quotas[LIGHT])
            self.rng.shuffle(selected)
            grid={(r,c): selected[r*self.voyage.width+c] for r in range(self.voyage.height) for c in range(self.voyage.width)}
            reefs={c for c,e in grid.items() if e.kind=='impassable_reef'}
            if len(reefs)!=self.required_reef_count: continue
            if any(r==self.voyage.height-1 for r,c in reefs): continue
            islands={c for c,e in grid.items() if e.category==ISLAND}
            bad=False
            for (r,c),e in grid.items():
                if e.kind in {'forced_extra','disable_random'}:
                    if any(max(abs(r-ir),abs(c-ic))<=1 for ir,ic in islands): bad=True; break
            if bad: continue
            port=self.rng.randrange(self.voyage.width)
            starts=[s for s in range(self.voyage.width) if path_exists(self.voyage.width,self.voyage.height,s,port,reefs) and path_via_island(self.voyage.width,self.voyage.height,s,port,reefs,islands)]
            if not starts: continue
            self.grid=grid; self.port_col=port
            self._v23_valid_starts=starts
            self._v23_initial_reef_coords=set(reefs)
            return
        raise RuntimeError('v2.3 setup could not be generated')

    def _install_experimental_maps(self):
        self.col=self.rng.choice(self._v23_valid_starts); self.row=-1; self.route_stack=[(-1,self.col)]
        self.reef_coords=set(self._v23_initial_reef_coords)
        self.reef_coord=next(iter(self.reef_coords),None)
        self.public_blocked=set()
        self.metrics_count['reef_installed']=len(self.reef_coords)

    def swap_card_positions(self,ca,cb):
        super().swap_card_positions(ca,cb)
        ra,rb=ca in self.reef_coords, cb in self.reef_coords
        self.reef_coords.discard(ca); self.reef_coords.discard(cb)
        if ra:self.reef_coords.add(cb)
        if rb:self.reef_coords.add(ca)
        pa,pb=ca in self.public_blocked, cb in self.public_blocked
        self.public_blocked.discard(ca); self.public_blocked.discard(cb)
        if pa:self.public_blocked.add(cb)
        if pb:self.public_blocked.add(ca)

    def _structural_candidates_from_current(self):
        raw=self._raw_candidates_from(self.row,self.col)
        blocked=frozenset(self.public_blocked)
        return [x for x in raw if (x[0],x[1]) not in blocked and self._can_reach_port(x[0],x[1],blocked)]

    def valid_candidates(self, ignore_effects=False):
        structural=self._structural_candidates_from_current()
        if ignore_effects:return structural
        out=structural[:]
        if self.next_center_lock:
            allowed={0}
            if self.temporary_yeke and self.yeke_extra_dc is not None: allowed.add(self.yeke_extra_dc)
            out=[x for x in out if x[2] in allowed]
        if self.next_disabled_dc is not None: out=[x for x in out if x[2]!=self.next_disabled_dc]
        if not out and structural:
            out=structural; self.rule_fallbacks+=1; self.metrics_count['effect_collision']+=1
        return out

    def horizon_coords(self,far=False):
        coords=super().horizon_coords(far)
        return [c for c in coords if c not in self.public_blocked]

    def _reef_caused_dead_end(self):
        if self._structural_candidates_from_current(): return False
        raw=self._raw_candidates_from(self.row,self.col)
        return bool(raw) and bool(self.public_blocked)

    def _emergency_backtrack(self):
        if not self._reef_caused_dead_end(): return False
        if len(self.route_stack)<=1:
            self.metrics_count['reef_start_locks']+=1; return False
        trapped=(self.row,self.col)
        self.reef_dead_end_cells.add(trapped)
        self.route_stack.pop(); self.row,self.col=self.route_stack[-1]
        self.metrics_count['reef_deadends']+=1; self.metrics_count['reef_backtracks']+=1; self.metrics_count['reef_backtrack_steps']+=1
        self.last_claims=[]; self.last_votes={}; self.last_choice=None; self.last_choice_voters=[]
        self.next_center_lock=False; self.temporary_yeke=False; self.yeke_extra_dc=None; self.next_disabled_dc=None
        return True

    def move_once(self, first_move=False, forced=False):
        candidates=self.valid_candidates()
        if not candidates:
            if forced and self._reef_caused_dead_end():
                self.metrics_count['forced_reef_cancels']+=1; return False,False
            if not forced and self._emergency_backtrack(): return False,False
            self.finish_reason='route_lock'; self.winner='hain'; self.rule_fallbacks+=1; self.metrics_count['hard_route_locks']+=1
            return False,False
        before_hits=self.metrics_count['reef_hits']
        result=super().move_once(first_move=first_move,forced=forced)
        if self.metrics_count['reef_hits']>before_hits:
            self.metrics_count['hidden_reef_discoveries']+=1
            if first_move:self.metrics_count['first_route_reef_hits']+=1
        return result

def make_config(n,length,label):
    sea,rock=damage_quota_for(n,length)
    return AuditConfig(label=label,n=n,hains=RECOMMENDED_HAINS[n],length=length,hull=2,night_rule='choice_peek1',attack_bias=.55,rescue_rule='existing',politics_rule='two_stage',identity_protected=True,identity_exchange=True,queen_mode='seyir_zabti',kayikci_chain='existing',route_policy='social',persona='dengeli',map_pool_variant='candidate52',sea_damage_quota=sea,rock_damage_quota=rock,port_timing='next_morning',yama_replacement='kancali_halat',captain_double=True,first_move_captain=True)

def run_cell(pair,n,length,runs,seed):
    pool=build_pool(pair); master=random.Random(seed); rows=[]; errors=0
    cfg=make_config(n,length,'v2.3_hidden_reef')
    for _ in range(runs):
        rr=random.Random(master.getrandbits(64))
        try:
            v=t.audit_voyage(n,length); rc=reef_count_for(v.width,v.height)
            g=HiddenReefGame(rr,cfg,pool,rc); rows.append(g.run())
        except RuntimeError: errors+=1
    if not rows: raise RuntimeError('no games')
    def mean(k):return statistics.mean(r.get(k,0) for r in rows)
    return {'n':n,'length':length,'runs':len(rows),'setup_errors':errors,'crew_win':sum(r['winner']=='crew' for r in rows)/len(rows),'days':mean('days'),'nights':mean('nights'),'hull_left':mean('hull_left'),'reef_hits':mean('reef_hits'),'hidden_reef_discoveries':mean('hidden_reef_discoveries'),'games_with_reef_hit':sum(r.get('reef_hits',0)>0 for r in rows)/len(rows),'first_route_reef_hit_rate':sum(r.get('first_route_reef_hits',0)>0 for r in rows)/len(rows),'backtracks':mean('reef_backtracks'),'games_with_backtrack':sum(r.get('reef_backtracks',0)>0 for r in rows)/len(rows),'hard_locks':sum(r.get('hard_route_locks',0)>0 for r in rows)/len(rows),'forced_reef_cancels':mean('forced_reef_cancels'),'hain_peeks':mean('hain_peeks'),'crew_role_peeks':mean('crew_role_peeks'),'contested_rate':mean('contested_rate'),'vote_entropy':mean('vote_entropy')}

def screen_pairs(runs,seed):
    cells=[(8,'short'),(8,'normal'),(8,'long'),(13,'short'),(13,'normal'),(13,'long')]
    out=[]
    for pair in itertools.combinations(range(7),2):
        rows=[run_cell(pair,n,l,runs,seed+1000*(pair[0]+1)+100*(pair[1]+1)+i) for i,(n,l) in enumerate(cells)]
        out.append({'pair':list(pair),'labels':[SAFE_ROCK_LABELS[i] for i in pair],'crew_win':statistics.mean(r['crew_win'] for r in rows),'days':statistics.mean(r['days'] for r in rows),'nights':statistics.mean(r['nights'] for r in rows),'reef_hit_rate':statistics.mean(r['games_with_reef_hit'] for r in rows),'backtrack_rate':statistics.mean(r['games_with_backtrack'] for r in rows),'hard_lock_rate':statistics.mean(r['hard_locks'] for r in rows),'setup_errors':sum(r['setup_errors'] for r in rows)})
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--screen-runs',type=int,default=200); ap.add_argument('--final-runs',type=int,default=1000); ap.add_argument('--seed',type=int,default=20260818); ap.add_argument('--output',type=Path,default=Path('v23_hidden_reef_results.json')); a=ap.parse_args()
    screening=screen_pairs(a.screen_runs,a.seed); preferred=(0,1)
    full=[]
    for i,(n,l) in enumerate([(8,'short'),(8,'normal'),(8,'long'),(13,'short'),(13,'normal'),(13,'long')]): full.append(run_cell(preferred,n,l,a.final_runs,a.seed+90000+i))
    payload={'meta':{'date':'2026-08-18','scope':'v2.3 hidden integrated impassable rock cards; same Kayalık backs; 52 maps total','screen_runs_per_cell':a.screen_runs,'final_runs_per_cell':a.final_runs,'seed':a.seed},'safe_rock_labels':SAFE_ROCK_LABELS,'screening':screening,'preferred_pair':{'pair':list(preferred),'labels':[SAFE_ROCK_LABELS[i] for i in preferred],'reason':'removes no-effect Ufak Kayalık and one duplicate Batık Kalyon; preserves all damage cards and every unique rock mechanic'},'preferred_full':full,'preferred_summary':{'crew_win':statistics.mean(r['crew_win'] for r in full),'days':statistics.mean(r['days'] for r in full),'nights':statistics.mean(r['nights'] for r in full),'reef_hit_rate':statistics.mean(r['games_with_reef_hit'] for r in full),'first_route_hit_rate':statistics.mean(r['first_route_reef_hit_rate'] for r in full),'backtrack_rate':statistics.mean(r['games_with_backtrack'] for r in full),'hard_lock_rate':statistics.mean(r['hard_locks'] for r in full),'setup_errors':sum(r['setup_errors'] for r in full)}}
    a.output.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(payload['preferred_summary'],ensure_ascii=False,indent=2))
if __name__=='__main__': main()
