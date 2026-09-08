"""Reproduce this review's paired stress run without overwriting the prior run."""
import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

QA = Path(__file__).resolve().parent
P = QA.parent.parent
sys.path.insert(0, str(P / 'qa/editorial_revision'))
spec = importlib.util.spec_from_file_location('prior_voyage_runner', P / 'qa/editorial_revision/run_simulation.py')
sim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sim)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--package', required=True)
    parser.add_argument('--seeds', type=int, default=20)
    args = parser.parse_args()
    sim.QA = QA
    sim.run(args.package, args.seeds)
    path = QA / 'simulation_results.json'
    data = json.loads(path.read_text())
    data.update(task_id='FOULWAKE-WHOLE-GAME-POLISH-001', run_date='2026-09-08',
                rulebook_sha256=hashlib.sha256((P / 'FOULWAKE_KURAL_KITABI_v2.7.md').read_bytes()).hexdigest())
    data['limitations'].append('The 20260908 wording and GUC-27 window clarification are source-reviewed; this observation adapter does not execute every current card interaction.')
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
