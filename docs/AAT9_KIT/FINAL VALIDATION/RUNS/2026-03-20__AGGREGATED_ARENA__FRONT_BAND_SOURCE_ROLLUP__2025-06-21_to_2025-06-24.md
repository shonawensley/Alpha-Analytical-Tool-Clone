# Aggregated Arena Front-Band Source Rollup

- Purpose: summarize the strongest front-band rows by source mix and short-horizon decay before a bounded bridge study.
- Review scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-24__AGGREGATED_ANALYSIS_ARENA__REVIEW.csv`
- Decay scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-24__AGGREGATED_ANALYSIS_ARENA__DECAY_D3.csv`
- Front-band rows: `7`

## Gap Split

- `lane_alive_literal_missing_front3`: `0/7`
- `lane_alive_literal_missing_front5`: `2/7`
- `family_alive_literal_missing_front5`: `5/7`

## Source Presence

| source | rows | front3 | front5 | family_front5 | dominant_vtrac_same_day | dominant_vtrac_<=3d | watchlist_box_same_day | watchlist_box_<=3d |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| aux_badge | 6 | 0 | 2 | 4 | 3/6 | 4/6 | 1/6 | 3/6 |
| aux_overdue | 5 | 0 | 2 | 3 | 2/5 | 3/5 | 0/5 | 2/5 |
| repeat_watch | 3 | 0 | 1 | 2 | 2/3 | 2/3 | 1/3 | 2/3 |
| blackapple | 1 | 0 | 0 | 1 | 1/1 | 1/1 | 1/1 | 1/1 |
| due_doubles | 1 | 0 | 1 | 0 | 1/1 | 1/1 | 0/1 | 0/1 |
| profit_alert | 1 | 0 | 1 | 0 | 1/1 | 1/1 | 0/1 | 1/1 |

## Source Mixes

| source_mix | rows | front3 | front5 | family_front5 | median_vtrac_rank_hint | dominant_vtrac_same_day | dominant_vtrac_<=3d | watchlist_box_same_day | watchlist_box_<=3d | downstream_literal_present |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| aux_overdue+aux_badge | 2 | 0 | 0 | 2 | 15 | 0/2 | 1/2 | 0/2 | 1/2 | 0/2 |

## Bridge Candidates

- `aux_overdue+aux_badge` rows `2` | dominant_vtrac `<=3d 1/2` | watchlist_box `<=3d 1/2`
