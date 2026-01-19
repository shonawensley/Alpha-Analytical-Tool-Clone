# Hot Zones — Weight Sweep (HOTZ-003 harness)

Reporting-only: reruns Hot Zones against frozen sharepack JSON tables and grades against results.

## Inputs

- Sharepacks root: `sharepacks`
- Dates: `2026-01-05` → `2026-01-09` (5 days requested)
- States (requested): 14
- Sweep: `w_vt_only_lane_bonus` = 0.8, 0.9, 1, 1.1; `w_col1_arrival` = 2.1, 2.4, 2.7, 3 (baseline=vt_only=0.8,col1=2.4)

## Summary (all winners; winner canonical in top-K)

| Weights | Rows | Top8% | Top12% | Top20% | avg Δrank vs baseline |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8,col1=2.4 | 138 | 0.043 | 0.065 | 0.094 | 0.000 |
| vt_only=0.8,col1=2.1 | 138 | 0.051 | 0.065 | 0.094 | 0.111 |
| vt_only=0.8,col1=2.7 | 138 | 0.043 | 0.065 | 0.094 | -0.111 |
| vt_only=0.8,col1=3 | 138 | 0.036 | 0.065 | 0.094 | 0.007 |
| vt_only=0.9,col1=2.1 | 138 | 0.051 | 0.065 | 0.094 | -0.104 |
| vt_only=0.9,col1=2.4 | 138 | 0.043 | 0.065 | 0.094 | -0.104 |
| vt_only=0.9,col1=2.7 | 138 | 0.043 | 0.065 | 0.094 | -0.230 |
| vt_only=0.9,col1=3 | 138 | 0.036 | 0.065 | 0.094 | -0.163 |
| vt_only=1,col1=2.1 | 138 | 0.043 | 0.065 | 0.094 | 0.230 |
| vt_only=1,col1=2.4 | 138 | 0.043 | 0.065 | 0.094 | 0.163 |
| vt_only=1,col1=2.7 | 138 | 0.036 | 0.065 | 0.094 | 0.030 |
| vt_only=1,col1=3 | 138 | 0.036 | 0.065 | 0.094 | 0.015 |
| vt_only=1.1,col1=2.1 | 138 | 0.043 | 0.065 | 0.094 | 0.437 |
| vt_only=1.1,col1=2.4 | 138 | 0.043 | 0.065 | 0.094 | 0.437 |
| vt_only=1.1,col1=2.7 | 138 | 0.036 | 0.065 | 0.094 | 0.319 |
| vt_only=1.1,col1=3 | 138 | 0.036 | 0.065 | 0.094 | 0.252 |

## VTRAC index hit (winner index present in top-K)

| Weights | Rows | Top8% | Top12% | Top20% |
|---|---:|---:|---:|---:|
| vt_only=0.8,col1=2.4 | 138 | 0.152 | 0.283 | 0.399 |
| vt_only=0.8,col1=2.1 | 138 | 0.167 | 0.275 | 0.399 |
| vt_only=0.8,col1=2.7 | 138 | 0.145 | 0.268 | 0.391 |
| vt_only=0.8,col1=3 | 138 | 0.138 | 0.268 | 0.391 |
| vt_only=0.9,col1=2.1 | 138 | 0.167 | 0.275 | 0.399 |
| vt_only=0.9,col1=2.4 | 138 | 0.152 | 0.283 | 0.391 |
| vt_only=0.9,col1=2.7 | 138 | 0.145 | 0.268 | 0.391 |
| vt_only=0.9,col1=3 | 138 | 0.138 | 0.268 | 0.391 |
| vt_only=1,col1=2.1 | 138 | 0.159 | 0.275 | 0.399 |
| vt_only=1,col1=2.4 | 138 | 0.145 | 0.283 | 0.391 |
| vt_only=1,col1=2.7 | 138 | 0.145 | 0.268 | 0.391 |
| vt_only=1,col1=3 | 138 | 0.138 | 0.268 | 0.391 |
| vt_only=1.1,col1=2.1 | 138 | 0.159 | 0.275 | 0.399 |
| vt_only=1.1,col1=2.4 | 138 | 0.145 | 0.283 | 0.391 |
| vt_only=1.1,col1=2.7 | 138 | 0.145 | 0.268 | 0.391 |
| vt_only=1.1,col1=3 | 138 | 0.138 | 0.268 | 0.391 |

## VTRAC index hit only (index present but winner canonical not in top-K)

| Weights | Rows | Top8% | Top12% | Top20% |
|---|---:|---:|---:|---:|
| vt_only=0.8,col1=2.4 | 138 | 0.109 | 0.217 | 0.304 |
| vt_only=0.8,col1=2.1 | 138 | 0.116 | 0.210 | 0.304 |
| vt_only=0.8,col1=2.7 | 138 | 0.101 | 0.203 | 0.297 |
| vt_only=0.8,col1=3 | 138 | 0.101 | 0.203 | 0.297 |
| vt_only=0.9,col1=2.1 | 138 | 0.116 | 0.210 | 0.304 |
| vt_only=0.9,col1=2.4 | 138 | 0.109 | 0.217 | 0.297 |
| vt_only=0.9,col1=2.7 | 138 | 0.101 | 0.203 | 0.297 |
| vt_only=0.9,col1=3 | 138 | 0.101 | 0.203 | 0.297 |
| vt_only=1,col1=2.1 | 138 | 0.116 | 0.210 | 0.304 |
| vt_only=1,col1=2.4 | 138 | 0.101 | 0.217 | 0.297 |
| vt_only=1,col1=2.7 | 138 | 0.109 | 0.203 | 0.297 |
| vt_only=1,col1=3 | 138 | 0.101 | 0.203 | 0.297 |
| vt_only=1.1,col1=2.1 | 138 | 0.116 | 0.210 | 0.304 |
| vt_only=1.1,col1=2.4 | 138 | 0.101 | 0.217 | 0.297 |
| vt_only=1.1,col1=2.7 | 138 | 0.109 | 0.203 | 0.297 |
| vt_only=1.1,col1=3 | 138 | 0.101 | 0.203 | 0.297 |

## VT-only visibility (winner has vt_only_lane evidence and **no** straight evidence)

| Weights | vt_only rows | Top8% | Top12% | Top20% | avg Δrank (vt_only) |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8,col1=2.4 | 36 | 0.000 | 0.000 | 0.056 | 0.000 |
| vt_only=0.8,col1=2.1 | 36 | 0.000 | 0.000 | 0.056 | -0.194 |
| vt_only=0.8,col1=2.7 | 36 | 0.000 | 0.000 | 0.056 | 0.000 |
| vt_only=0.8,col1=3 | 36 | 0.000 | 0.000 | 0.056 | 0.167 |
| vt_only=0.9,col1=2.1 | 36 | 0.000 | 0.000 | 0.056 | 0.028 |
| vt_only=0.9,col1=2.4 | 36 | 0.000 | 0.000 | 0.056 | 0.306 |
| vt_only=0.9,col1=2.7 | 36 | 0.000 | 0.000 | 0.056 | 0.194 |
| vt_only=0.9,col1=3 | 36 | 0.000 | 0.000 | 0.056 | 0.389 |
| vt_only=1,col1=2.1 | 36 | 0.000 | 0.000 | 0.056 | 1.028 |
| vt_only=1,col1=2.4 | 36 | 0.000 | 0.000 | 0.056 | 1.056 |
| vt_only=1,col1=2.7 | 36 | 0.000 | 0.000 | 0.056 | 1.111 |
| vt_only=1,col1=3 | 36 | 0.000 | 0.000 | 0.056 | 1.111 |
| vt_only=1.1,col1=2.1 | 36 | 0.000 | 0.000 | 0.056 | 2.000 |
| vt_only=1.1,col1=2.4 | 36 | 0.000 | 0.000 | 0.056 | 2.111 |
| vt_only=1.1,col1=2.7 | 36 | 0.000 | 0.000 | 0.056 | 2.222 |
| vt_only=1.1,col1=3 | 36 | 0.000 | 0.000 | 0.056 | 2.306 |

## Any vt_only_lane evidence (winner has vt_only_lane evidence; may also have straight evidence)

| Weights | vt_any rows | Top8% | Top12% | Top20% | avg Δrank (vt_any) |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8,col1=2.4 | 112 | 0.045 | 0.071 | 0.107 | 0.000 |
| vt_only=0.8,col1=2.1 | 112 | 0.054 | 0.071 | 0.107 | 0.107 |
| vt_only=0.8,col1=2.7 | 112 | 0.045 | 0.071 | 0.107 | -0.125 |
| vt_only=0.8,col1=3 | 112 | 0.036 | 0.071 | 0.107 | 0.018 |
| vt_only=0.9,col1=2.1 | 112 | 0.054 | 0.071 | 0.107 | -0.152 |
| vt_only=0.9,col1=2.4 | 112 | 0.045 | 0.071 | 0.107 | -0.125 |
| vt_only=0.9,col1=2.7 | 112 | 0.045 | 0.071 | 0.107 | -0.268 |
| vt_only=0.9,col1=3 | 112 | 0.036 | 0.071 | 0.107 | -0.188 |
| vt_only=1,col1=2.1 | 112 | 0.045 | 0.071 | 0.107 | 0.357 |
| vt_only=1,col1=2.4 | 112 | 0.045 | 0.071 | 0.107 | 0.304 |
| vt_only=1,col1=2.7 | 112 | 0.036 | 0.071 | 0.107 | 0.152 |
| vt_only=1,col1=3 | 112 | 0.036 | 0.071 | 0.107 | 0.134 |
| vt_only=1.1,col1=2.1 | 112 | 0.045 | 0.071 | 0.107 | 0.625 |
| vt_only=1.1,col1=2.4 | 112 | 0.045 | 0.071 | 0.107 | 0.652 |
| vt_only=1.1,col1=2.7 | 112 | 0.036 | 0.071 | 0.107 | 0.518 |
| vt_only=1.1,col1=3 | 112 | 0.036 | 0.071 | 0.107 | 0.438 |

## Outputs

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__2026-01-05_to_2026-01-09.csv`
- MD: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__2026-01-05_to_2026-01-09.md`
