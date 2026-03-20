# Aggregated Arena Bridge Family Scoreboard

- Purpose: summarize measured bridge families by direct closure, same-day carry-forward, future-day decay, and miss across the current frozen-window corpus.
- Rule analyzed: `top4_perm`
- summary_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-20__AGGREGATED_ARENA__BRIDGE_FAMILY_SCOREBOARD.csv`
- total rows: `16`

## By Family

| source_mix | rows | direct_same_outcome | same_day_precursor_plus_same_day | same_day_carryforward | future_day_decay | miss |
|---|---|---|---|---|---|---|
| aux_overdue+aux_badge | 8 | 3/8 | 1/8 | 1/8 | 0/8 | 3/8 |
| due_doubles+aux_badge | 2 | 1/2 | 0/2 | 0/2 | 1/2 | 0/2 |
| profit_alert+aux_badge | 3 | 1/3 | 0/3 | 0/3 | 1/3 | 1/3 |
| profit_alert+due_doubles+aux_overdue+aux_badge | 3 | 0/3 | 0/3 | 0/3 | 1/3 | 2/3 |

## By Reviewed Outcome

| outcome | rows | direct_same_outcome | same_day_precursor_plus_same_day | same_day_carryforward | future_day_decay | miss |
|---|---|---|---|---|---|---|
| Evening | 5 | 2/5 | 1/5 | 0/5 | 1/5 | 1/5 |
| Midday | 11 | 3/11 | 0/11 | 1/11 | 2/11 | 5/11 |

## By Family And Outcome

| source_mix | outcome | rows | direct_same_outcome | same_day_precursor_plus_same_day | same_day_carryforward | future_day_decay | miss |
|---|---|---|---|---|---|---|---|
| aux_overdue+aux_badge | Evening | 2 | 1/2 | 1/2 | 0/2 | 0/2 | 0/2 |
| aux_overdue+aux_badge | Midday | 6 | 2/6 | 0/6 | 1/6 | 0/6 | 3/6 |
| due_doubles+aux_badge | Evening | 2 | 1/2 | 0/2 | 0/2 | 1/2 | 0/2 |
| profit_alert+aux_badge | Midday | 3 | 1/3 | 0/3 | 0/3 | 1/3 | 1/3 |
| profit_alert+due_doubles+aux_overdue+aux_badge | Evening | 1 | 0/1 | 0/1 | 0/1 | 0/1 | 1/1 |
| profit_alert+due_doubles+aux_overdue+aux_badge | Midday | 2 | 0/2 | 0/2 | 0/2 | 1/2 | 1/2 |

## Notes

- `direct_same_outcome` means the bridge hit the reviewed row itself.
- `same_day_precursor_plus_same_day` means the bridge already hit another same-day outcome while still hitting the reviewed row.
- `same_day_carryforward` means the bridge missed the reviewed row but converted on the other draw from the same day.
- `future_day_decay` means the bridge resolved only on a later day inside the measured horizon.
