# Blackapple grade — 2026-01-05 → 2026-01-09 (N=5)

Purpose
- Grade Blackapple (Aux) candidates vs posted winners (same-day + windowed).
- Sharepacks root: `sharepacks/_predictive`
- Detailed CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__BLACKAPPLE_GRADE__N5.csv`
- Rollup CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/blackapple_rollup__N5__2026-01-05_to_2026-01-09.csv`

Notes
- `#Candidates` is the full BA candidate list size (cap is typically 12).
- `Examples` is only the first 3 candidates (Control Center table readability).
- `hit_any_inclusive` counts `boxed` (includes straight) OR `vtrac` lane hit.

## Rollup (rates)

| Variant | Status | Period | Rows | hit_any_inclusive | hit_any_inclusive_window | boxed | straight | vtrac |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Combined | ALERT | Evening | 8 | 0.3750 | 0.8750 | 0.1250 | 0.0000 | 0.3750 |
| Combined | ALERT | Midday | 8 | 0.2500 | 0.7500 | 0.0000 | 0.0000 | 0.2500 |
| Combined | OFF | Evening | 39 | 0.2308 | 0.7436 | 0.0769 | 0.0256 | 0.2308 |
| Combined | OFF | Midday | 39 | 0.3077 | 0.7436 | 0.1026 | 0.0000 | 0.3077 |
| Combined | WATCH | Evening | 22 | 0.3182 | 0.6364 | 0.0000 | 0.0000 | 0.3182 |
| Combined | WATCH | Midday | 22 | 0.3636 | 0.8182 | 0.1364 | 0.0000 | 0.3636 |
| Evening | ALERT | Evening | 4 | 0.0000 | 0.2500 | 0.0000 | 0.0000 | 0.0000 |
| Evening | ALERT | Midday | 4 | 0.2500 | 0.5000 | 0.0000 | 0.0000 | 0.2500 |
| Evening | OFF | Evening | 42 | 0.2857 | 0.7381 | 0.0714 | 0.0238 | 0.2857 |
| Evening | OFF | Midday | 42 | 0.2381 | 0.6429 | 0.0952 | 0.0000 | 0.2381 |
| Evening | WATCH | Evening | 23 | 0.2609 | 0.3913 | 0.1304 | 0.0000 | 0.2609 |
| Evening | WATCH | Midday | 23 | 0.3913 | 0.6522 | 0.1739 | 0.0000 | 0.3913 |
| Midday | ALERT | Evening | 6 | 0.8333 | 1.0000 | 0.3333 | 0.1667 | 0.8333 |
| Midday | ALERT | Midday | 6 | 0.6667 | 1.0000 | 0.0000 | 0.0000 | 0.6667 |
| Midday | OFF | Evening | 39 | 0.2051 | 0.6667 | 0.0000 | 0.0000 | 0.2051 |
| Midday | OFF | Midday | 39 | 0.2564 | 0.5385 | 0.0256 | 0.0000 | 0.2564 |
| Midday | WATCH | Evening | 24 | 0.2917 | 0.7917 | 0.0000 | 0.0000 | 0.2917 |
| Midday | WATCH | Midday | 24 | 0.1667 | 0.8750 | 0.0417 | 0.0000 | 0.1667 |
