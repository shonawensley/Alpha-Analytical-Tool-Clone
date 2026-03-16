# Aux + Control Center Export Slice

Date: `2026-03-16`

## What Landed

A bounded Aux / Control Center arena-export slice is now implemented.

Code:

- `scripts/tools/aux_control_center_arena.py`
- `scripts/tools/create_candidate_universe.py`

New predictive-side outputs:

- `sharepacks/_predictive/<D>/<STATE>/analysis/aux_control_center_arena*.json`
- `sharepacks/_predictive/<D>/<STATE>/analysis/aux_control_center_arena*.md`

New signals-bundle surface:

- `tools.aux_control_center_context`

This export preserves broader structured Aux / Control Center context without
changing the existing narrow candidate-universe packs.

## Preserved Arena Objects

- `aux_positional_pressure`
- `aux_vtrac_pressure`
- `aux_badge_pressure`
- `aux_pair_band_context`
- `aux_due_doubles_family_pressure`
- `aux_repeat_watch_context`
- `aux_sums_context`
- `aux_blackapple_context`
- `cc_profit_alert_context`
- `cc_compound_event_context`
- `cc_tracker_context`

## Important Boundary

The export slice does **not**:

- retune Aux scoring
- widen existing candidate-universe methods
- force new play-card behavior

It only broadens preservation into the analysis arena.

## Validation

### Unit / regression slice

- `pytest -q tests/test_aux_control_center_arena.py tests/test_stable_candidate_packs.py tests/test_stable_arena.py tests/test_dr_arena.py`
- result: `17 passed`

### Live predictive smoke

Representative live run:

```bash
python3 scripts/tools/create_candidate_universe.py \
  --date 2026-03-15 \
  --sharepacks-root sharepacks/_predictive \
  --profile tool_only \
  --experiment-tag stable10 \
  --states NorthCarolina4 NewJersey4 \
  --top-n-dr 0 \
  --top-n-stable 10 \
  --write-signals-bundle \
  --write-aux-cc-arena \
  --force
```

Observed outputs:

- `NorthCarolina4/analysis/aux_control_center_arena__tool_only__stable10.json`
- `NewJersey4/analysis/aux_control_center_arena__tool_only__stable10.json`
- both signals bundles now include `tools.aux_control_center_context`

## Current Read

This is the right bounded finish for the tool-local Aux / Control Center phase:

- richer structured preservation
- no new narrow scorer loop
- no premature conversion policy

The next lift should come from the aggregated analysis arena using this broader
context layer.
