# Aggregated Arena Bridge Study

- Purpose: test bounded watchlist-based lane-to-literal bridge rules on the strongest measured cohorts before any production conversion change.
- Cohort mixes: `aux_overdue+aux_badge, due_doubles+aux_badge, profit_alert+aux_badge, profit_alert+due_doubles+aux_overdue+aux_badge`
- Rules: `top3_perm, top4_perm`
- Gap details: `lane_alive_literal_missing_front3, lane_alive_literal_missing_front5`
- Max VTRAC rank: `5`
- Row count: `6`

## Rule Summary

| rule | rows | avg_watch_items | avg_watchlist_canonicals | same_day_box | same_day_exact | within_3d_box | within_3d_exact | baseline_same_day_literal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| top3_perm | 3 | 3.00 | 8.67 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 |
| top4_perm | 3 | 4.00 | 11.33 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 |

## Cohort Summary

| source_mix | rows | avg_watch_items | avg_watchlist_canonicals | same_day_box | same_day_exact | within_3d_box | within_3d_exact | baseline_same_day_literal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| aux_overdue+aux_badge | 2 | 3.50 | 7.00 | 0/2 | 0/2 | 0/2 | 0/2 | 0/2 |
| profit_alert+aux_badge | 2 | 3.50 | 10.00 | 0/2 | 0/2 | 0/2 | 0/2 | 0/2 |
| profit_alert+due_doubles+aux_overdue+aux_badge | 2 | 3.50 | 13.00 | 0/2 | 0/2 | 0/2 | 0/2 | 0/2 |

## Notes

- `same_day_*` compares the bridge candidates against the reviewed outcome row itself.
- `within_3d_*` freezes the same bridge candidates and checks later outcomes for the same state through the next 3 days.
- `baseline_same_day_literal` is the current downstream literal presence from Candidate Universe / Play Card for the same reviewed row.
