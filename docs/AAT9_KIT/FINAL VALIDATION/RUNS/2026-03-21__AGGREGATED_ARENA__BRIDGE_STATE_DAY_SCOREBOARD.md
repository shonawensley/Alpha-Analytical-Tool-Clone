# Aggregated Arena Bridge State-Day Scoreboard

- Purpose: collapse measured bridge rows from outcome-level into one state-day result per source family, so same-state same-day crossover is visible as one performance unit.
- Rule analyzed: `top4_perm`
- summary_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-21__AGGREGATED_ARENA__BRIDGE_STATE_DAY_SCOREBOARD.csv`
- outcome rows: `16`
- state-day rows: `15`

## By Family

| source_mix | state_days | same_day_state | future_day_state | miss_state |
|---|---|---|---|---|
| aux_overdue+aux_badge | 7 | 4/7 | 0/7 | 3/7 |
| due_doubles+aux_badge | 2 | 1/2 | 1/2 | 0/2 |
| profit_alert+aux_badge | 3 | 1/3 | 1/3 | 1/3 |
| profit_alert+due_doubles+aux_overdue+aux_badge | 3 | 0/3 | 1/3 | 2/3 |

## By Family And Outcome Span

| source_mix | outcome_span | state_days | same_day_state | future_day_state | miss_state |
|---|---|---|---|---|---|
| aux_overdue+aux_badge | Evening | 1 | 1/1 | 0/1 | 0/1 |
| aux_overdue+aux_badge | Midday | 5 | 2/5 | 0/5 | 3/5 |
| aux_overdue+aux_badge | Midday+Evening | 1 | 1/1 | 0/1 | 0/1 |
| due_doubles+aux_badge | Evening | 2 | 1/2 | 1/2 | 0/2 |
| profit_alert+aux_badge | Midday | 3 | 1/3 | 1/3 | 1/3 |
| profit_alert+due_doubles+aux_overdue+aux_badge | Evening | 1 | 0/1 | 0/1 | 1/1 |
| profit_alert+due_doubles+aux_overdue+aux_badge | Midday | 2 | 0/2 | 1/2 | 1/2 |

## Notes

- `same_day_state` means at least one row for that state-day-family resolved on the same day, including Midday/Evening carry-forward.
- `future_day_state` means no same-day resolution occurred, but a later-day decay hit did.
- `miss_state` means neither same-day nor later-day resolution occurred for that state-day-family.
- `outcome_span` shows whether the family was measured on Midday only, Evening only, or both outcomes for the same state-day.
