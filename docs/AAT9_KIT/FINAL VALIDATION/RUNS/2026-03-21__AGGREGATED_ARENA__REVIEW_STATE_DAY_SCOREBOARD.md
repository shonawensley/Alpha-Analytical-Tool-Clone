# Aggregated Arena Review State-Day Scoreboard

- Purpose: collapse aggregated arena review rows from `date x state x outcome` into one `date x state` performance unit while preserving row-level review as the diagnostic layer.
- summary_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-21__AGGREGATED_ARENA__REVIEW_STATE_DAY_SCOREBOARD.csv`
- outcome rows: `579`
- state-days: `291`

## State-Day Gap Class

| state_day_gap_class | state_days | share |
|---|---|---|
| arena_present_but_underweighted | 212 | 212/291 |
| downstream_present | 53 | 53/291 |
| arena_missing | 14 | 14/291 |
| conversion_gap | 12 | 12/291 |

## By Outcome Span

| outcome_span | state_days | arena_canonical_state_present | arena_vtrac_state_present | arena_family_state_present | context_reinforced_state | downstream_literal_state |
|---|---|---|---|---|---|---|
| Evening | 3 | 3/3 | 3/3 | 3/3 | 0/3 | 0/3 |
| Midday+Evening | 288 | 261/288 | 274/288 | 253/288 | 154/288 | 53/288 |

## Notes

- `state_day_gap_class` is the best available gap class for that date/state, using the priority: `downstream_present > arena_present_but_underweighted > conversion_gap > arena_missing`.
- `context_reinforced_state` means at least one outcome row for that state-day had canonical/VTRAC/family context reinforcement.
- `downstream_literal_state` means Candidate Universe or Play Card had a same-day literal closure on at least one outcome row for that state-day.
- This is the performance/accounting lens; keep the original outcome-row review for diagnostics.
