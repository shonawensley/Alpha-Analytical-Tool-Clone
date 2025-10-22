import json
from pathlib import Path

data = json.loads(Path('tmp_batch_results_phase2.json').read_text())
summary = {}
for entry in data['stable']:
    summary[entry['state']] = {
        'stamp': data['stamp'],
        'winners': entry['metrics']['winners'],
        'patterns': entry['metrics']['total_patterns'],
        'families': entry['metrics']['total_families'],
        'spotlight_rate': entry['metrics']['spotlight_rate'],
        'best_straight_rank': entry['metrics']['best_straight_rank'],
        'winners_evidence': entry['winners_evidence'],
    }
Path('tmp_phase2_summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
print('Summary written to tmp_phase2_summary.json (stamp', data['stamp'], ')')
