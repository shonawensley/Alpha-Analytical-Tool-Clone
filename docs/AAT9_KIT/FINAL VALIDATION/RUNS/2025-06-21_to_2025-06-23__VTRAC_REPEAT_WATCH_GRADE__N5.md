# VTRAC Repeat Watch grade — 2025-06-21 → 2025-06-23 (N=5)

Purpose
- Grade VTRAC repeat-watch (index + streak) vs posted winners (same-day + windowed).
- Sharepacks root: `sharepacks`
- Detailed CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__VTRAC_REPEAT_WATCH_GRADE__N5.csv`
- Rollup CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/vtrac_repeat_watch_rollup__N5__2025-06-21_to_2025-06-23.csv`

Notes
- `same_day` checks whether `Current Index == winner VTRAC` for that period.
- `window` checks D..D+(N-1) for that period (days forward including D).

## Rollup (rates)

| Variant | Streak | Period | Rows | same_day_hit | window_hit |
|---|---:|---|---:|---:|---:|
| Combined | 1 | Evening | 41 | 0.0000 | 0.1707 |
| Combined | 1 | Midday | 40 | 0.0000 | 0.0500 |
| Evening | 1 | Evening | 41 | 0.0000 | 0.1707 |
| Evening | 1 | Midday | 40 | 0.0000 | 0.0500 |
| Midday | 1 | Evening | 39 | 0.0000 | 0.1026 |
| Midday | 1 | Midday | 38 | 0.0526 | 0.2105 |
| Midday | 2 | Evening | 2 | 0.0000 | 0.5000 |
| Midday | 2 | Midday | 2 | 0.0000 | 0.0000 |
