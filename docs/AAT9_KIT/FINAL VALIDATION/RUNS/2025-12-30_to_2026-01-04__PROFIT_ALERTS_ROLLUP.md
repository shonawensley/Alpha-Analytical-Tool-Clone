# Profit Alerts Rollup — 2025-12-30 → 2026-01-04

Small, corpus-level summary of Profit Alerts evaluation outputs (row-level and merged play-sets).

Inputs (per day):
- `sharepacks/<D>/control_center/profit_alerts_eval.csv`
- `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`

Outputs:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__PROFIT_ALERTS_ROLLUP_ROWS.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__PROFIT_ALERTS_ROLLUP_MERGED.csv`

## Overall (row-level)

- Total alert rows: **408**
- Candidate rows: **309**
- Promoter rows: **79**

- Status HIT: **1/408** (0.2%)
- Status EXPIRED: **318/408** (77.9%)
- Status CENSORED: **10/408** (2.5%)

## Overall (merged play-sets)

- Merged sets: **274**
- Status HIT: **1/274** (0.4%)
- Status EXPIRED: **266/274** (97.1%)
- Status CENSORED: **7/274** (2.6%)

## Candidate rows: hits within window (rollup by AlertId)

| alert_id | rows | hit_decay | hit_any_decay | hit_any<=7 | hit_any<=14 |
|---|---:|---:|---:|---:|---:|
| A04 | 84 | 1/83 | 1/83 | 5/42 | 7/15 |
| A05 | 84 | 0/83 | 0/83 | 0/41 | 0/8 |
| A01 | 40 | 0/32 | 0/32 | 1/16 | 1/4 |
| A02 | 38 | 0/38 | 0/38 | 0/23 | 0/5 |
| A12 | 32 | 0/32 | 0/32 | 2/20 | 2/4 |
| A10 | 18 | 0/18 | 0/18 | 0/13 | 0/3 |
| A09 | 9 | 0/9 | 0/9 | 1/4 | 1/1 |
| A06 | 4 | 0/4 | 0/4 | 0/2 | - |

## Merged play-sets: by suggested kind

| suggested_kinds | sets | hit_any_decay | hit_any<=7 | hit_any<=14 |
|---|---:|---:|---:|---:|
| BOX | 123 | 1/117 | 6/62 | 8/20 |
| STR8_3 | 110 | 0/109 | 0/58 | 0/11 |
| STR8_4of8 | 32 | 0/32 | 1/19 | 1/3 |
| STR8_8 | 9 | 0/9 | 0/4 | 0/0 |

## Notes

- `hit_decay` is variant-faithful (Midday rows grade Midday-only; Evening rows grade Evening-only; Combined rows grade Midday→Evening→…).
- `hit_any_*` is the cross-variant diagnostic lens (Midday alerts can be credited if the hit lands on Evening within the same time span, etc.).
- Use `CENSORED` and `?` counts (in the CSVs) to see where results coverage is insufficient for the requested windows.
