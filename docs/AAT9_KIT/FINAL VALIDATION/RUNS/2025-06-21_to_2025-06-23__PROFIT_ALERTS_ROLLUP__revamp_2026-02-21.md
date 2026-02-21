# Profit Alerts Rollup — 2025-06-21 → 2025-06-23

Label: `revamp_2026-02-21`

Small, corpus-level summary of Profit Alerts evaluation outputs (row-level and merged play-sets).

Inputs (per day):
- `sharepacks/<D>/control_center/profit_alerts_eval.csv`
- `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`

Outputs:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__PROFIT_ALERTS_ROLLUP__revamp_2026-02-21_ROWS.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__PROFIT_ALERTS_ROLLUP__revamp_2026-02-21_MERGED.csv`

## Overall (row-level)

- Total alert rows: **257**
- Candidate rows: **182**
- Promoter rows: **55**

- Status HIT: **3/257** (1.2%)
- Status EXPIRED: **199/257** (77.4%)

## Overall (merged play-sets)

- Merged sets: **157**
- Status HIT: **2/157** (1.3%)
- Status EXPIRED: **155/157** (98.7%)

## D-only diagnostic (strict_hit)

- Candidate rows strict-hit: **0/177** (unknown: 5)

## Window hits (DecayDraws): hit types

- Hit types: Straight=3, Boxed=3

## Candidate rows: hits within window (rollup by AlertId)

| alert_id | rows | strict_hit | hit_decay | hit_any_decay | hit_any<=7 | hit_any<=14 |
|---|---:|---:|---:|---:|---:|---:|
| A02 | 31 | 0/31 | 2/31 | 2/31 | 2/31 | 2/31 |
| A05 | 42 | 0/41 | 1/42 | 1/42 | 2/42 | 3/39 |
| A04 | 42 | 0/41 | 0/42 | 0/42 | 0/42 | 2/41 |
| A01 | 41 | 0/38 | 0/41 | 0/41 | 0/41 | 1/35 |
| A12 | 15 | 0/15 | 0/15 | 0/15 | 0/15 | 1/15 |
| A10 | 9 | 0/9 | 0/9 | 0/9 | 0/9 | 0/9 |
| A09 | 2 | 0/2 | 0/2 | 0/2 | 1/2 | 2/2 |

## Merged play-sets: by suggested kind

| suggested_kinds | sets | hit_any_decay | hit_any<=7 | hit_any<=14 |
|---|---:|---:|---:|---:|
| BOX | 71 | 0/71 | 0/71 | 2/67 |
| STR8_3 | 68 | 2/68 | 3/68 | 4/65 |
| STR8_4of8 | 15 | 0/15 | 0/15 | 0/15 |
| STR8_8 | 3 | 0/3 | 0/3 | 0/3 |

## Notes

- `strict_hit` is a D-only diagnostic (does not use the decay window).
- `hit_decay` is variant-faithful (Midday rows grade Midday-only; Evening rows grade Evening-only; Combined rows grade Midday→Evening→…).
- `hit_any_*` is the cross-variant diagnostic lens (Midday alerts can be credited if the hit lands on Evening within the same time span, etc.).
- Hit types (`Straight` / `Boxed` / `VTRAC`) come from the evaluator’s first-hit typing and can be mapped into the broader system’s semantics if desired.
- Use `CENSORED` and `?` counts (in the CSVs) to see where results coverage is insufficient for the requested windows.
