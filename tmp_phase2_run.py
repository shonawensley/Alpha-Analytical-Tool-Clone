import sys
import json
from datetime import datetime
from pathlib import Path

sys.path.append('src')

from alpha_analytical.control_center import batch_runner
from modules.aux_loaders import load_state_draws

WINNERS = {
    'Indiana': {'midday': '940', 'evening': '188'},
    'Michigan': {'midday': '618', 'evening': '339'},
    'NewJersey': {'midday': '758', 'evening': '926'},
    'NewYork': {'midday': '211', 'evening': '680'},
}

entries = []
for label, winners in WINNERS.items():
    project_state = f"{label}4"
    midday_list, _ = load_state_draws(project_state, variant='midday')
    evening_list, _ = load_state_draws(project_state, variant='evening')
    combined_list, _ = load_state_draws(project_state, variant='combined')

    midday = winners.get('midday') or (midday_list[0] if midday_list else None)
    evening = winners.get('evening') or (evening_list[0] if evening_list else None)

    raw_digits = []
    if midday:
        raw_digits.append(midday)
    if evening and evening != midday:
        raw_digits.append(evening)
    extra = next((d for d in combined_list if d not in raw_digits), None)
    if extra:
        raw_digits.append(extra)

    entries.append(
        batch_runner.ParsedWinnerEntry(
            label=label,
            canonical=label,
            project_state=project_state,
            midday=midday,
            evening=evening,
            raw_digits=tuple(raw_digits),
        )
    )

stamp = datetime.now().strftime('%Y%m%d')

stable = batch_runner.run_stable_bundles(entries, bundle_stamp=stamp, write_bundle=True)
digit_reduction = batch_runner.run_digit_reduction_workflow(
    entries,
    bundle_stamp=stamp,
    run_reducer=True,
    run_overlay=True,
    run_analyzer=True,
    run_bundle=True,
    include_overlay_html=True,
    include_hits=True,
    mirror_to_winners=True,
)
winners = batch_runner.run_winner_reports(entries)

Path('tmp_batch_results_phase2.json').write_text(
    json.dumps({'stamp': stamp, 'stable': stable, 'digit_reduction': digit_reduction, 'winners': winners}, indent=2),
    encoding='utf-8'
)
print('Phase 2 batch regenerated with stamp', stamp)
