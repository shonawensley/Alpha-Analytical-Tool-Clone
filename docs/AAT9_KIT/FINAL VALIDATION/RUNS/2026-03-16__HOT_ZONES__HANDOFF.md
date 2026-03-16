# Hot Zones Handoff

Date: `2026-03-16`

## Current Role

`Hot Zones` should now be treated as:

- a late-tail pressure extractor
- a vertical-support / survivorship extractor
- a lane/index corroboration feed

It should **not** be treated as a tiny top-k direct-caller oracle.

## Predictive-Side Artifacts To Feed The Arena

Primary:

- `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<STATE>_hot_zones_top_lanes.csv`
- `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<STATE>_hot_zones_meta.json`

Transitional compatibility:

- `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<D>_hot_zones_winner_map.json`

Forensic only:

- `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<STATE>_hot_zones_per_lane.csv`

## Audit-Only Winners Lens

Keep outside predictive mode:

- Hot Zones winner summaries
- winner-map hit diagnostics
- post-results placement summaries

These remain the audit/validation layer, not the predictive feed.

## Most Valuable Arena Contribution

Hot Zones’ best arena contribution is:

- `late_tail_pressure_strength`
- `superhot_echo_strength`
- `vertical_repeat_strength`
- `rowtype_span_support`
- `precol1_funnel_strength`
- `col1_arrival_strength`
- `vt_only_lane_pressure`
- `repeat_3value_score`
- `consensus_column_signal`
- `set1_funnel_density`

## One Bounded Finish Still Worth Doing

If any final slice is taken, it should be:

- digest / ledger validator outputs
- lean ingest contract clarification

Recommended digest layer:

- `hot_zones_summary_digest.csv`
- `hot_zones_ledger_all.csv`
- schema/manifest

Not:

- another guard iteration
- another broad weight loop

## Validation Closeout

The most useful summary/validator path already exists:

- `scripts/tools/hot_zones_sharepack_summary.py`

It was smoke-run successfully on representative gold-day artifacts:

- `sharepacks/2025-06-21/Virginia4/hot_zones/Virginia4`
- `sharepacks/2026-01-03/Florida4/hot_zones/Florida4`

The summaries confirmed the current lean ingest is viable:

- winner presence/rank inside `top_lanes.csv`
- straight vs VT-straight evidence from `per_lane.csv`
- compact winner-map placement diagnostics
- top-lane evidence tags suitable for arena interpretation

That means the bounded closeout is now mainly contract/digest framing, not another analyzer-tuning problem.

## Freeze Criteria

Freeze `Hot Zones` for this phase when:

1. `top_lanes.csv + meta.json` are the explicit arena ingest contract
2. `per_lane.csv` is explicitly forensic-only
3. digest/validator closeout is documented or implemented
4. no new bounded evidence feature clearly justifies reopening analyzer tuning

## Recommended Next Step After Freeze

Move Hot Zones into the aggregated analysis arena as a pressure / survivorship feed and judge any remaining gap there before reopening the analyzer.
