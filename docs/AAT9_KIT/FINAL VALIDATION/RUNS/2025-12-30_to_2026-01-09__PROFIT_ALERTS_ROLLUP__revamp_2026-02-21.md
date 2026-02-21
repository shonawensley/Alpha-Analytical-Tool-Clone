# Profit Alerts Rollup — 2025-12-30 → 2026-01-09

Label: `revamp_2026-02-21`

Small, corpus-level summary of Profit Alerts evaluation outputs (row-level and merged play-sets).

Inputs (per day):
- `sharepacks/<D>/control_center/profit_alerts_eval.csv`
- `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`

Outputs:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-09__PROFIT_ALERTS_ROLLUP__revamp_2026-02-21_ROWS.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-09__PROFIT_ALERTS_ROLLUP__revamp_2026-02-21_MERGED.csv`

## Overall (row-level)

- Total alert rows: **721**
- Candidate rows: **543**
- Promoter rows: **139**

- Status HIT: **4/721** (0.6%)
- Status EXPIRED: **461/721** (63.9%)
- Status CENSORED: **117/721** (16.2%)

## Overall (merged play-sets)

- Merged sets: **494**
- Status HIT: **4/494** (0.8%)
- Status EXPIRED: **396/494** (80.2%)
- Status CENSORED: **94/494** (19.0%)

## D-only diagnostic (strict_hit)

- Candidate rows strict-hit: **4/522** (unknown: 21)
- Strict hit types: Boxed=3, Straight=2

## Window hits (DecayDraws): hit types

- Hit types: Boxed=3, Straight=2

## Candidate rows: hits within window (rollup by AlertId)

| alert_id | rows | strict_hit | hit_decay | hit_any_decay | hit_any<=7 | hit_any<=14 |
|---|---:|---:|---:|---:|---:|---:|
| A12 | 60 | 2/58 | 2/54 | 2/54 | 4/22 | 4/6 |
| A04 | 142 | 2/139 | 2/103 | 2/103 | 7/46 | 9/19 |
| A05 | 141 | 0/137 | 0/123 | 0/123 | 0/43 | 0/10 |
| A01 | 80 | 0/72 | 0/44 | 0/44 | 1/16 | 1/4 |
| A02 | 69 | 0/68 | 0/57 | 0/57 | 0/23 | 0/5 |
| A10 | 32 | 0/30 | 0/26 | 0/26 | 0/15 | 0/5 |
| A09 | 13 | 0/12 | 0/13 | 0/13 | 2/5 | 2/2 |
| A06 | 5 | 0/5 | 0/5 | 0/5 | 0/2 | - |
| A07 | 1 | 0/1 | 0/1 | 0/1 | - | - |

## Merged play-sets: by suggested kind

| suggested_kinds | sets | hit_any_decay | hit_any<=7 | hit_any<=14 |
|---|---:|---:|---:|---:|
| BOX | 218 | 2/160 | 8/67 | 10/25 |
| STR8_3 | 201 | 0/172 | 0/62 | 0/15 |
| STR8_4of8 | 60 | 2/54 | 3/21 | 3/5 |
| STR8_8 | 15 | 0/14 | 0/5 | 0/1 |

## Notes

- `strict_hit` is a D-only diagnostic (does not use the decay window).
- `hit_decay` is variant-faithful (Midday rows grade Midday-only; Evening rows grade Evening-only; Combined rows grade Midday→Evening→…).
- `hit_any_*` is the cross-variant diagnostic lens (Midday alerts can be credited if the hit lands on Evening within the same time span, etc.).
- Hit types (`Straight` / `Boxed` / `VTRAC`) come from the evaluator’s first-hit typing and can be mapped into the broader system’s semantics if desired.
- Use `CENSORED` and `?` counts (in the CSVs) to see where results coverage is insufficient for the requested windows.
