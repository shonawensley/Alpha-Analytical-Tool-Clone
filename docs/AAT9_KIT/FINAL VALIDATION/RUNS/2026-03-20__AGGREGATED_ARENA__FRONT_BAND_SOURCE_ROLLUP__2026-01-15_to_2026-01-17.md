# Aggregated Arena Front-Band Source Rollup

- Purpose: summarize the strongest front-band rows by source mix and short-horizon decay before a bounded bridge study.
- Review scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-17__AGGREGATED_ANALYSIS_ARENA__REVIEW.csv`
- Decay scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-17__AGGREGATED_ANALYSIS_ARENA__DECAY_D3.csv`
- Front-band rows: `17`

## Gap Split

- `lane_alive_literal_missing_front3`: `9/17`
- `lane_alive_literal_missing_front5`: `2/17`
- `family_alive_literal_missing_front5`: `6/17`

## Source Presence

| source | rows | front3 | front5 | family_front5 | dominant_vtrac_same_day | dominant_vtrac_<=3d | watchlist_box_same_day | watchlist_box_<=3d |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| aux_badge | 14 | 9 | 1 | 4 | 12/14 | 12/14 | 4/14 | 9/14 |
| aux_overdue | 9 | 4 | 0 | 5 | 7/9 | 7/9 | 2/9 | 5/9 |
| due_doubles | 7 | 6 | 0 | 1 | 7/7 | 7/7 | 1/7 | 4/7 |
| profit_alert | 6 | 5 | 1 | 0 | 6/6 | 6/6 | 1/6 | 4/6 |
| blackapple | 4 | 2 | 1 | 1 | 4/4 | 4/4 | 1/4 | 3/4 |
| repeat_watch | 1 | 1 | 0 | 0 | 1/1 | 1/1 | 0/1 | 1/1 |

## Source Mixes

| source_mix | rows | front3 | front5 | family_front5 | median_vtrac_rank_hint | dominant_vtrac_same_day | dominant_vtrac_<=3d | watchlist_box_same_day | watchlist_box_<=3d | downstream_literal_present |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| aux_overdue+aux_badge | 4 | 0 | 0 | 4 | 999 | 2/4 | 2/4 | 2/4 | 2/4 | 0/4 |
| due_doubles+aux_badge | 2 | 2 | 0 | 0 | 3 | 2/2 | 2/2 | 1/2 | 2/2 | 0/2 |
| profit_alert+aux_badge | 2 | 2 | 0 | 0 | 3 | 2/2 | 2/2 | 0/2 | 1/2 | 0/2 |
| profit_alert+due_doubles+aux_overdue+aux_badge | 2 | 2 | 0 | 0 | 3 | 2/2 | 2/2 | 0/2 | 1/2 | 0/2 |

## Bridge Candidates

- `aux_overdue+aux_badge` rows `4` | dominant_vtrac `<=3d 2/4` | watchlist_box `<=3d 2/4`
- `due_doubles+aux_badge` rows `2` | dominant_vtrac `<=3d 2/2` | watchlist_box `<=3d 2/2`
- `profit_alert+aux_badge` rows `2` | dominant_vtrac `<=3d 2/2` | watchlist_box `<=3d 1/2`
- `profit_alert+due_doubles+aux_overdue+aux_badge` rows `2` | dominant_vtrac `<=3d 2/2` | watchlist_box `<=3d 1/2`
