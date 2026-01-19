# Hot Zones — Weight Sweep (HOTZ-003 harness)

Reporting-only: reruns Hot Zones against frozen sharepack JSON tables and grades against results.

## Inputs

- Sharepacks root: `sharepacks`
- Dates: `2025-06-21` → `2025-06-23` (3 days requested)
- States (requested): 14
- Sweep: `w_vt_only_lane_bonus` = 0.8, 0.9, 1, 1.1 (baseline=vt_only=0.8)

## Summary (all winners; winner canonical in top-K)

| Weights | Rows | Top8% | Top12% | Top20% | avg Δrank vs baseline |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8 | 81 | 0.037 | 0.062 | 0.136 | 0.000 |
| vt_only=0.9 | 81 | 0.037 | 0.062 | 0.136 | 0.138 |
| vt_only=1 | 81 | 0.037 | 0.062 | 0.136 | 0.100 |
| vt_only=1.1 | 81 | 0.037 | 0.062 | 0.123 | 0.688 |

## VT-only visibility (winner has vt_only_lane evidence and **no** straight evidence)

| Weights | vt_only rows | Top8% | Top12% | Top20% | avg Δrank (vt_only) |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8 | 14 | 0.000 | 0.000 | 0.000 | 0.000 |
| vt_only=0.9 | 14 | 0.000 | 0.000 | 0.000 | -0.357 |
| vt_only=1 | 14 | 0.000 | 0.000 | 0.000 | -0.071 |
| vt_only=1.1 | 14 | 0.000 | 0.000 | 0.000 | 1.857 |

## Any vt_only_lane evidence (winner has vt_only_lane evidence; may also have straight evidence)

| Weights | vt_any rows | Top8% | Top12% | Top20% | avg Δrank (vt_any) |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8 | 65 | 0.046 | 0.077 | 0.154 | 0.000 |
| vt_only=0.9 | 65 | 0.046 | 0.077 | 0.154 | 0.185 |
| vt_only=1 | 65 | 0.046 | 0.077 | 0.154 | 0.169 |
| vt_only=1.1 | 65 | 0.046 | 0.077 | 0.138 | 0.908 |

## Outputs

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP__2025-06-21_to_2025-06-23.csv`
- MD: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP__2025-06-21_to_2025-06-23.md`
