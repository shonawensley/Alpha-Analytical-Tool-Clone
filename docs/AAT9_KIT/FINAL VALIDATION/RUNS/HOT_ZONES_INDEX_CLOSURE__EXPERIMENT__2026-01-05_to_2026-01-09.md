# Hot Zones — Index-Closure Experiment (tool_only) — Jan window

Purpose: measure whether adding the optional `hot_zones_index_closure` pack (bounded BOX-expansion from dominant Hot Zones index votes) improves **gateway conversion** under tool-only defaults.

Window: `2026-01-05 → 2026-01-09` (predictive sharepacks; graded against `data/results/<D>.txt`).

## Candidate Universe (UNION rows)

| Variant | Rows | hit_any | straight_hit | box_hit | vtrac_index_hit | vtrac_index_hit_only | union_size_mean | union_size_min | union_size_max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline_current | 140 | 31 | 25 | 31 | 90 | 59 | 160.7 | 125 | 224 |
| +hot_zones_index_closure | 140 | 31 | 23 | 31 | 90 | 59 | 166.9 | 135 | 231 |

Delta (experiment - baseline):
- hit_any: 0  | box_hit: 0  | vtrac_index_hit_only: 0
- union size mean: +6.2 lines

## Play Cards (selection cuts)

Rows here are per (state, draw, strategy, budget).

| Strategy | Budget | Rows | hit_any (base→exp) | box_hit (base→exp) | vtrac_index_hit (base→exp) |
|---|---|---:|---:|---:|---:|
| analysis_prefix | B12 | 140 | 4→4 | 2→2 | 22→18 |
| analysis_prefix | B24 | 140 | 6→6 | 4→4 | 29→28 |
| analysis_prefix | B36 | 140 | 6→6 | 5→5 | 35→34 |
| convergence_box_first | B12 | 140 | 3→3 | 3→3 | 9→10 |
| convergence_box_first | B24 | 140 | 6→6 | 6→6 | 18→18 |
| convergence_box_first | B36 | 140 | 6→6 | 6→6 | 26→23 |
| conversion_box_first | B12 | 140 | 3→3 | 3→3 | 16→15 |
| conversion_box_first | B24 | 140 | 6→5 | 6→5 | 26→23 |
| conversion_box_first | B36 | 140 | 8→8 | 8→8 | 29→28 |
| play_box_first | B12 | 140 | 5→5 | 5→5 | 12→12 |
| play_box_first | B24 | 140 | 8→8 | 8→8 | 21→19 |
| play_box_first | B36 | 140 | 8→8 | 8→8 | 25→25 |
