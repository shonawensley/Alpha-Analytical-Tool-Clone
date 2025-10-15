import json
from pathlib import Path

data = json.loads(Path('tmp_batch_results.json').read_text())
lookup = {
    'Indiana4': ['940','188'],
    'Michigan4': ['618','339'],
    'NewJersey4': ['758','926'],
    'NewYork4': ['211','680'],
}

for entry in data['stable']:
    state = entry['state']
    base_state = state.rstrip('4')
    if state in lookup:
        print('State', state)
        print('Winners in metrics:', entry['metrics']['winners'])
