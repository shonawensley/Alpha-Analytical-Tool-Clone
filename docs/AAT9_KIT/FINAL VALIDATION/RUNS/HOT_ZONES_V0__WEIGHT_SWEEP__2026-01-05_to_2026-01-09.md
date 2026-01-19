# Hot Zones — Weight Sweep (HOTZ-003 harness)

Reporting-only: reruns Hot Zones against frozen sharepack JSON tables and grades against results.

## Inputs

- Sharepacks root: `sharepacks`
- Dates: `2026-01-05` → `2026-01-09` (5 days requested)
- States (requested): 14
- Sweep: `w_vt_only_lane_bonus` = 0.8, 0.9, 1, 1.1 (baseline=vt_only=0.8)

## Summary (all winners; winner canonical in top-K)

| Weights | Rows | Top8% | Top12% | Top20% | avg Δrank vs baseline |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8 | 138 | 0.043 | 0.065 | 0.094 | 0.000 |
| vt_only=0.9 | 138 | 0.043 | 0.065 | 0.094 | -0.104 |
| vt_only=1 | 138 | 0.043 | 0.065 | 0.094 | 0.163 |
| vt_only=1.1 | 138 | 0.043 | 0.065 | 0.094 | 0.437 |

## VT-only visibility (winner has vt_only_lane evidence and **no** straight evidence)

| Weights | vt_only rows | Top8% | Top12% | Top20% | avg Δrank (vt_only) |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8 | 36 | 0.000 | 0.000 | 0.056 | 0.000 |
| vt_only=0.9 | 36 | 0.000 | 0.000 | 0.056 | 0.306 |
| vt_only=1 | 36 | 0.000 | 0.000 | 0.056 | 1.056 |
| vt_only=1.1 | 36 | 0.000 | 0.000 | 0.056 | 2.111 |

## Any vt_only_lane evidence (winner has vt_only_lane evidence; may also have straight evidence)

| Weights | vt_any rows | Top8% | Top12% | Top20% | avg Δrank (vt_any) |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8 | 112 | 0.045 | 0.071 | 0.107 | 0.000 |
| vt_only=0.9 | 112 | 0.045 | 0.071 | 0.107 | -0.125 |
| vt_only=1 | 112 | 0.045 | 0.071 | 0.107 | 0.304 |
| vt_only=1.1 | 112 | 0.045 | 0.071 | 0.107 | 0.652 |

## Outputs

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP__2026-01-05_to_2026-01-09.csv`
- MD: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP__2026-01-05_to_2026-01-09.md`
