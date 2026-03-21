# Aggregated Arena Bridge Family Mode Scoreboard

- Purpose: summarize bridge evidence by source family plus reviewed outcome, with simple sample-size bands so thin slices are not over-read.
- Rule analyzed: `top4_perm`
- summary_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-20__AGGREGATED_ARENA__BRIDGE_FAMILY_MODE_SCOREBOARD.csv`
- total bridge rows: `16`
- sample bands: `thin < 3`, `provisional < 5`, `measured >= 5`

## Family + Mode

| source_mix | outcome | rows | sample_band | mode_hint | same_day_any | resolved_any | direct_same_outcome | same_day_precursor_plus_same_day | same_day_carryforward | future_day_decay | miss |
|---|---|---|---|---|---|---|---|---|---|---|---|
| aux_overdue+aux_badge | Evening | 2 | thin | same_day_only | 2/2 | 2/2 | 1/2 | 1/2 | 0/2 | 0/2 | 0/2 |
| aux_overdue+aux_badge | Midday | 6 | measured | same_day_mixed | 3/6 | 3/6 | 2/6 | 0/6 | 1/6 | 0/6 | 3/6 |
| due_doubles+aux_badge | Evening | 2 | thin | resolved_mixed | 1/2 | 2/2 | 1/2 | 0/2 | 0/2 | 1/2 | 0/2 |
| profit_alert+aux_badge | Midday | 3 | provisional | mixed_all_modes | 1/3 | 2/3 | 1/3 | 0/3 | 0/3 | 1/3 | 1/3 |
| profit_alert+due_doubles+aux_overdue+aux_badge | Evening | 1 | thin | all_miss | 0/1 | 0/1 | 0/1 | 0/1 | 0/1 | 0/1 | 1/1 |
| profit_alert+due_doubles+aux_overdue+aux_badge | Midday | 2 | thin | future_day_mixed | 0/2 | 1/2 | 0/2 | 0/2 | 0/2 | 1/2 | 1/2 |

## Guidance

- `thin` means the slice is interesting but too small for a strong judgment.
- `provisional` means the slice is worth studying, but not promoting.
- `measured` means the slice has enough rows to guide the next bounded study mode more confidently.
- `same_day_any` counts direct, same-day precursor+same-day, and same-day carry-forward together.
- `resolved_any` counts any non-miss resolution, including future-day decay.
