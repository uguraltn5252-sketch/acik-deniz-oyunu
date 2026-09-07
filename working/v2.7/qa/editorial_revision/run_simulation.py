"""Paired, seeded whole-voyage heuristic stress runs; no human balance claim."""
import argparse
import collections
import csv
import hashlib
import json
import platform
import random
import statistics
from pathlib import Path
from observation_engine import load_engine, make_engine

QA = Path(__file__).resolve().parent


def run(package, seeds):
    m, temporary, evidence = load_engine(package)
    G = make_engine(m)
    rows = []
    for n in range(6, 16):
        for length in ('short', 'normal', 'long'):
            for persona in ('temkinli', 'dengeli', 'kaotik'):
                for i in range(seeds):
                    seed = int.from_bytes(hashlib.sha256(f'FOULWAKE-20260907-{n}-{length}-{persona}-{i}'.encode()).digest()[:8], 'big')
                    starts = []
                    for variant in ('A', 'B'):
                        game = G(random.Random(seed), m.canonical_config(n, length=length, persona=persona), variant)
                        starts.append((dict(game.grid), game.captain, game.scurvy_owner, game.captain_opening_peek))
                        result = game.run()
                        assert result['hull_left'] in (0, 1, 2)
                        assert not result['identity_discards']
                        rows.append({'n':n, 'length':length, 'persona':persona, 'seed':seed, 'variant':variant,
                                     **{k:result.get(k,0) for k in ('winner','reason','days','nights','hull_left','scurvy_started','scurvy_cleared','attacks','rule_fallbacks','empty_ship_stalemate','identity_discards','relocation_rollbacks')}})
                    assert starts[0] == starts[1], 'A/B setup mismatch'
        print(f'{n} players completed; {len(rows)} voyages', flush=True)
    with (QA/'simulation_games.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    def summarize(group):
        wins = sum(r['winner']=='crew' for r in group)
        return {'games':len(group),'crew_wins':wins,'crew_win_rate':wins/len(group),
                'mean_days':statistics.mean(r['days'] for r in group),
                'reasons':dict(collections.Counter(r['reason'] for r in group)),
                'empty_ship_stalemates':sum(r['empty_ship_stalemate'] for r in group),
                'identity_discards':sum(r['identity_discards'] for r in group)}
    report={'task_id':'FOULWAKE-EDITORIAL-OVERHAUL-001','seed_formula':'SHA256(FOULWAKE-20260907-N-length-persona-index), first 8 bytes big endian',
            'evidence_class':'HEURISTIC_WHOLE_VOYAGE_STRESS / SAME_OPERATOR / NOT_RULE_COMPLETE / NOT_HUMAN_PLAYTEST',
            'python':platform.python_version(),'source':evidence,'paired_setups':len(rows)//2,'total_games':len(rows),
            'seeds_per_player_length_persona':seeds,
            'variants':{'A':'separate Sea/Rock visible category','B':'shared Sea/Rock visible category; current v2.7 decision'},
            'summary':{v:summarize([r for r in rows if r['variant']==v]) for v in ('A','B')},
            'by_player_count':{str(n):{v:summarize([r for r in rows if r['n']==n and r['variant']==v]) for v in ('A','B')} for n in range(6,16)},
            'limitations':['Social dialogue, Captain elections and revotes remain heuristic abstractions.',
                           'Not all card interactions are modeled: see editorial_report.md; these rates cannot approve balance or physical backs.',
                           'Setup is paired; post-choice random streams diverge. This is not a controlled causal estimate of the back effect.',
                           'No human session, print/physical information leak test, art acceptance or release approval.']}
    (QA/'simulation_results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report['summary'],ensure_ascii=False),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--package',required=True);p.add_argument('--seeds',type=int,default=20);a=p.parse_args()
    run(a.package,a.seeds)
