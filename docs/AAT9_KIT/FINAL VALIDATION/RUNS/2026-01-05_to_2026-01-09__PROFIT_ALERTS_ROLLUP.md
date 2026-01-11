# Profit Alerts Rollup — 2026-01-05 → 2026-01-09

Small, corpus-level summary of Profit Alerts evaluation outputs (row-level and merged play-sets).

Inputs (per day):
- `sharepacks/<D>/control_center/profit_alerts_eval.csv`
- `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`

Outputs:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__PROFIT_ALERTS_ROLLUP_ROWS.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__PROFIT_ALERTS_ROLLUP_MERGED.csv`

## Overall (row-level)

- Total alert rows: **375**
- Candidate rows: **282**
- Promoter rows: **70**

- Status HIT: **4/375** (1.1%)
- Status EXPIRED: **194/375** (51.7%)
- Status CENSORED: **107/375** (28.5%)

## Overall (merged play-sets)

- Merged sets: **263**
- Status HIT: **4/263** (1.5%)
- Status EXPIRED: **172/263** (65.4%)
- Status CENSORED: **87/263** (33.1%)

## Candidate rows: hits within window (rollup by AlertId)

| alert_id | rows | hit_decay | hit_any_decay | hit_any<=7 | hit_any<=14 |
|---|---:|---:|---:|---:|---:|
| A12 | 33 | 2/27 | 2/27 | 2/6 | 2/2 |
| A04 | 70 | 2/32 | 2/32 | 3/6 | 3/3 |
| A05 | 69 | 0/52 | 0/52 | 0/5 | - |
| A01 | 52 | 0/24 | 0/24 | 1/5 | 2/2 |
| A02 | 35 | 0/23 | 0/23 | 0/1 | - |
| A10 | 15 | 0/9 | 0/9 | 0/3 | - |
| A09 | 6 | 0/6 | 0/6 | 1/2 | 1/1 |
| A07 | 1 | 0/1 | 0/1 | - | - |
| A06 | 1 | 0/1 | 0/1 | - | - |

## Merged play-sets: by suggested kind

| suggested_kinds | sets | hit_any_decay | hit_any<=7 | hit_any<=14 |
|---|---:|---:|---:|---:|
| BOX | 117 | 2/65 | 4/14 | 6/6 |
| STR8_3 | 104 | 0/76 | 0/8 | 0/0 |
| STR8_4of8 | 33 | 2/27 | 2/6 | 2/2 |
| STR8_8 | 9 | 0/8 | 0/1 | 0/0 |

## Notes

- `hit_decay` is variant-faithful (Midday rows grade Midday-only; Evening rows grade Evening-only; Combined rows grade Midday→Evening→…).
- `hit_any_*` is the cross-variant diagnostic lens (Midday alerts can be credited if the hit lands on Evening within the same time span, etc.).
- Use `CENSORED` and `?` counts (in the CSVs) to see where results coverage is insufficient for the requested windows.
