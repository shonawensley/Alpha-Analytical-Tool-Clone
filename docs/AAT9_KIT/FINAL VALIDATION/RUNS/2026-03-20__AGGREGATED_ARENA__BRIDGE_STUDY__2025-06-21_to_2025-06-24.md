# Aggregated Arena Bridge Study

- Purpose: test bounded watchlist-based lane-to-literal bridge rules on the strongest measured cohorts before any production conversion change.
- Cohort mixes: `aux_overdue+aux_badge, due_doubles+aux_overdue+aux_badge, due_doubles`
- Rules: `top3_perm, top4_perm`
- Row count: `6`

## Rule Summary

| rule | rows | avg_watch_items | avg_watchlist_canonicals | same_day_box | same_day_exact | within_3d_box | within_3d_exact | baseline_same_day_literal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| top3_perm | 3 | 3.00 | 11.00 | 0/3 | 0/3 | 1/3 | 1/3 | 0/3 |
| top4_perm | 3 | 4.00 | 13.67 | 0/3 | 0/3 | 1/3 | 1/3 | 0/3 |

## Cohort Summary

| source_mix | rows | avg_watch_items | avg_watchlist_canonicals | same_day_box | same_day_exact | within_3d_box | within_3d_exact | baseline_same_day_literal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| aux_overdue+aux_badge | 4 | 3.50 | 11.75 | 0/4 | 0/4 | 2/4 | 2/4 | 0/4 |
| due_doubles+aux_overdue+aux_badge | 2 | 3.50 | 13.50 | 0/2 | 0/2 | 0/2 | 0/2 | 0/2 |

## Notes

- `same_day_*` compares the bridge candidates against the reviewed outcome row itself.
- `within_3d_*` freezes the same bridge candidates and checks later outcomes for the same state through the next 3 days.
- `baseline_same_day_literal` is the current downstream literal presence from Candidate Universe / Play Card for the same reviewed row.
