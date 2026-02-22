# Profit Alerts Rollup — 2025-12-30 → 2026-01-09

Label: `provloc_v1`

Small, corpus-level summary of Profit Alerts evaluation outputs (row-level and merged play-sets).

Inputs (per day):
- `sharepacks/<D>/control_center/profit_alerts_eval.csv`
- `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`

Outputs:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_revamp__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/2025-12-30_to_2026-01-09__PROFIT_ALERTS_ROLLUP__provloc_v1_ROWS.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_revamp__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/2025-12-30_to_2026-01-09__PROFIT_ALERTS_ROLLUP__provloc_v1_MERGED.csv`

## Overall (row-level)

- Total alert rows: **721**
- Candidate rows: **543**
- Promoter rows: **139**

- Status HIT: **4/721** (0.6%)
- Status EXPIRED: **578/721** (80.2%)

## Overall (merged play-sets)

- Merged sets: **494**
- Status HIT: **4/494** (0.8%)
- Status EXPIRED: **490/494** (99.2%)

## D-only diagnostic (strict_hit)

- Candidate rows strict-hit: **4/522** (unknown: 21)
- Strict hit types: Boxed=3, Straight=2

## Window hits (DecayDraws): hit types

- Hit types: Boxed=3, Straight=2

## Candidate rows: hits within window (rollup by AlertId)

| alert_id | rows | strict_hit | hit_decay | hit_any_decay | hit_any<=7 | hit_any<=14 |
|---|---:|---:|---:|---:|---:|---:|
| A12 | 60 | 2/58 | 2/60 | 2/60 | 4/60 | 5/58 |
| A04 | 142 | 2/139 | 2/142 | 2/142 | 11/142 | 15/132 |
| A05 | 141 | 0/137 | 0/141 | 0/141 | 2/141 | 7/133 |
| A01 | 80 | 0/72 | 0/80 | 0/80 | 2/80 | 3/72 |
| A02 | 69 | 0/68 | 0/69 | 0/69 | 4/69 | 10/62 |
| A10 | 32 | 0/30 | 0/32 | 0/32 | 0/32 | 1/32 |
| A09 | 13 | 0/12 | 0/13 | 0/13 | 4/13 | 10/13 |
| A06 | 5 | 0/5 | 0/5 | 0/5 | 0/5 | 1/5 |
| A07 | 1 | 0/1 | 0/1 | 0/1 | 1/1 | 1/1 |

## Merged play-sets: by suggested kind

| suggested_kinds | sets | hit_any_decay | hit_any<=7 | hit_any<=14 |
|---|---:|---:|---:|---:|
| BOX | 218 | 2/218 | 14/218 | 21/204 |
| STR8_3 | 201 | 0/201 | 4/201 | 11/191 |
| STR8_4of8 | 60 | 2/60 | 3/60 | 3/58 |
| STR8_8 | 15 | 0/15 | 0/15 | 1/13 |

## Notes

- `strict_hit` is a D-only diagnostic (does not use the decay window).
- `hit_decay` is variant-faithful (Midday rows grade Midday-only; Evening rows grade Evening-only; Combined rows grade Midday→Evening→…).
- `hit_any_*` is the cross-variant diagnostic lens (Midday alerts can be credited if the hit lands on Evening within the same time span, etc.).
- Hit types (`Straight` / `Boxed` / `VTRAC`) come from the evaluator’s first-hit typing and can be mapped into the broader system’s semantics if desired.
- Use `CENSORED` and `?` counts (in the CSVs) to see where results coverage is insufficient for the requested windows.
