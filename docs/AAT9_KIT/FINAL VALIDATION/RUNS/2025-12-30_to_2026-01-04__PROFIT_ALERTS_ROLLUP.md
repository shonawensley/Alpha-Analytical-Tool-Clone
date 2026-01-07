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
- Status EXPIRED: **267/408** (65.4%)
- Status CENSORED: **61/408** (15.0%)

## Overall (merged play-sets)

- Merged sets: **274**
- Status HIT: **1/274** (0.4%)
- Status EXPIRED: **222/274** (81.0%)
- Status CENSORED: **51/274** (18.6%)

## Candidate rows: hits within window (rollup by AlertId)

| alert_id | rows | hit_decay | hit_any_decay | hit_any<=7 | hit_any<=14 |
|---|---:|---:|---:|---:|---:|
| A04 | 84 | 1/64 | 1/64 | 2/15 | 3/3 |
| A05 | 84 | 0/73 | 0/73 | 0/13 | - |
| A01 | 40 | 0/21 | 0/21 | 1/5 | 1/1 |
| A02 | 38 | 0/35 | 0/35 | 0/8 | - |
| A12 | 32 | 0/29 | 0/29 | 2/7 | 2/2 |
| A10 | 18 | 0/15 | 0/15 | 0/7 | - |
| A09 | 9 | 0/9 | 0/9 | 1/3 | 1/1 |
| A06 | 4 | 0/3 | 0/3 | 0/1 | - |

## Merged play-sets: by suggested kind

| suggested_kinds | sets | hit_any_decay | hit_any<=7 | hit_any<=14 |
|---|---:|---:|---:|---:|
| BOX | 123 | 1/90 | 3/23 | 4/4 |
| STR8_3 | 110 | 0/95 | 0/21 | 0/0 |
| STR8_4of8 | 32 | 0/29 | 1/6 | 1/1 |
| STR8_8 | 9 | 0/9 | 0/2 | 0/0 |

## Notes

- `hit_decay` is variant-faithful (Midday rows grade Midday-only; Evening rows grade Evening-only; Combined rows grade Midday→Evening→…).
- `hit_any_*` is the cross-variant diagnostic lens (Midday alerts can be credited if the hit lands on Evening within the same time span, etc.).
- Use `CENSORED` and `?` counts (in the CSVs) to see where results coverage is insufficient for the requested windows.
