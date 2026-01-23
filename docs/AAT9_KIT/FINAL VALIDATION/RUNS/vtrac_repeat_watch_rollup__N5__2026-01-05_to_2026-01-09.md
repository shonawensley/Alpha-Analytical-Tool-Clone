# VTRAC Repeat Watch grade — 2026-01-05 → 2026-01-09 (N=5)

Purpose
- Grade VTRAC repeat-watch (index + streak) vs posted winners (same-day + windowed).
- Sharepacks root: `sharepacks/_predictive`
- Detailed CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__VTRAC_REPEAT_WATCH_GRADE__N5.csv`
- Rollup CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/vtrac_repeat_watch_rollup__N5__2026-01-05_to_2026-01-09.csv`

Notes
- `same_day` checks whether `Current Index == winner VTRAC` for that period.
- `window` checks D..D+(N-1) for that period (days forward including D).

## Rollup (rates)

| Variant | Streak | Period | Rows | same_day_hit | window_hit |
|---|---:|---|---:|---:|---:|
| Combined | 1 | Evening | 68 | 0.0000 | 0.0588 |
| Combined | 1 | Midday | 68 | 0.0000 | 0.1029 |
| Combined | 2 | Evening | 1 | 0.0000 | 0.0000 |
| Combined | 2 | Midday | 1 | 0.0000 | 0.0000 |
| Evening | 1 | Evening | 68 | 0.0000 | 0.0588 |
| Evening | 1 | Midday | 68 | 0.0000 | 0.1029 |
| Evening | 2 | Evening | 1 | 0.0000 | 0.0000 |
| Evening | 2 | Midday | 1 | 0.0000 | 0.0000 |
| Midday | 1 | Evening | 65 | 0.0000 | 0.0462 |
| Midday | 1 | Midday | 65 | 0.0308 | 0.0769 |
| Midday | 2 | Evening | 4 | 0.0000 | 0.2500 |
| Midday | 2 | Midday | 4 | 0.0000 | 0.2500 |
