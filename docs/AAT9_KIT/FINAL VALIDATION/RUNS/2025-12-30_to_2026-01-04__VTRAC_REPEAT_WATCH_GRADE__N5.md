# VTRAC Repeat Watch grade — 2025-12-30 → 2026-01-04 (N=5)

Purpose
- Grade VTRAC repeat-watch (index + streak) vs posted winners (same-day + windowed).
- Sharepacks root: `sharepacks`
- Detailed CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__VTRAC_REPEAT_WATCH_GRADE__N5.csv`
- Rollup CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/vtrac_repeat_watch_rollup__N5__2025-12-30_to_2026-01-04.csv`

Notes
- `same_day` checks whether `Current Index == winner VTRAC` for that period.
- `window` checks D..D+(N-1) for that period (days forward including D).

## Rollup (rates)

| Variant | Streak | Period | Rows | same_day_hit | window_hit |
|---|---:|---|---:|---:|---:|
| Combined | 1 | Evening | 78 | 0.0385 | 0.1667 |
| Combined | 1 | Midday | 77 | 0.0390 | 0.2078 |
| Combined | 2 | Evening | 4 | 0.0000 | 0.2500 |
| Combined | 2 | Midday | 4 | 0.0000 | 0.0000 |
| Evening | 1 | Evening | 80 | 0.0375 | 0.1750 |
| Evening | 1 | Midday | 79 | 0.0380 | 0.1899 |
| Evening | 2 | Evening | 2 | 0.0000 | 0.0000 |
| Evening | 2 | Midday | 2 | 0.0000 | 0.5000 |
| Midday | 1 | Evening | 80 | 0.0250 | 0.2375 |
| Midday | 1 | Midday | 79 | 0.0380 | 0.1392 |
| Midday | 2 | Evening | 2 | 0.0000 | 0.0000 |
| Midday | 2 | Midday | 2 | 0.0000 | 0.0000 |
