# Hot Zones — Weight Sweep (HOTZ-003 harness)

Reporting-only: reruns Hot Zones against frozen sharepack JSON tables and grades against results.

## Inputs

- Sharepacks root: `sharepacks`
- Dates: `2025-06-21` → `2025-06-23` (3 days requested)
- States (requested): 14
- Sweep: `w_vt_only_lane_bonus` = 0.8, 0.9, 1, 1.1; `w_col1_arrival` = 2.1, 2.4, 2.7, 3 (baseline=vt_only=0.8,col1=2.4)

## Summary (all winners; winner canonical in top-K)

| Weights | Rows | Top8% | Top12% | Top20% | avg Δrank vs baseline |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8,col1=2.4 | 81 | 0.037 | 0.062 | 0.136 | 0.000 |
| vt_only=0.8,col1=2.1 | 81 | 0.025 | 0.062 | 0.136 | 0.163 |
| vt_only=0.8,col1=2.7 | 81 | 0.037 | 0.062 | 0.136 | -0.250 |
| vt_only=0.8,col1=3 | 81 | 0.037 | 0.062 | 0.123 | -0.562 |
| vt_only=0.9,col1=2.1 | 81 | 0.025 | 0.062 | 0.136 | 0.312 |
| vt_only=0.9,col1=2.4 | 81 | 0.037 | 0.062 | 0.136 | 0.138 |
| vt_only=0.9,col1=2.7 | 81 | 0.037 | 0.062 | 0.136 | -0.025 |
| vt_only=0.9,col1=3 | 81 | 0.037 | 0.062 | 0.123 | -0.425 |
| vt_only=1,col1=2.1 | 81 | 0.025 | 0.062 | 0.136 | 0.287 |
| vt_only=1,col1=2.4 | 81 | 0.037 | 0.062 | 0.136 | 0.100 |
| vt_only=1,col1=2.7 | 81 | 0.037 | 0.062 | 0.123 | -0.138 |
| vt_only=1,col1=3 | 81 | 0.037 | 0.062 | 0.123 | -0.500 |
| vt_only=1.1,col1=2.1 | 81 | 0.025 | 0.062 | 0.123 | 0.725 |
| vt_only=1.1,col1=2.4 | 81 | 0.037 | 0.062 | 0.123 | 0.688 |
| vt_only=1.1,col1=2.7 | 81 | 0.049 | 0.062 | 0.123 | 0.400 |
| vt_only=1.1,col1=3 | 81 | 0.049 | 0.062 | 0.123 | 0.025 |

## VT-only visibility (winner has vt_only_lane evidence and **no** straight evidence)

| Weights | vt_only rows | Top8% | Top12% | Top20% | avg Δrank (vt_only) |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8,col1=2.4 | 14 | 0.000 | 0.000 | 0.000 | 0.000 |
| vt_only=0.8,col1=2.1 | 14 | 0.000 | 0.000 | 0.000 | 0.071 |
| vt_only=0.8,col1=2.7 | 14 | 0.000 | 0.000 | 0.000 | -0.429 |
| vt_only=0.8,col1=3 | 14 | 0.000 | 0.000 | 0.000 | -0.643 |
| vt_only=0.9,col1=2.1 | 14 | 0.000 | 0.000 | 0.000 | -0.571 |
| vt_only=0.9,col1=2.4 | 14 | 0.000 | 0.000 | 0.000 | -0.357 |
| vt_only=0.9,col1=2.7 | 14 | 0.000 | 0.000 | 0.000 | -0.786 |
| vt_only=0.9,col1=3 | 14 | 0.000 | 0.000 | 0.000 | -1.071 |
| vt_only=1,col1=2.1 | 14 | 0.000 | 0.000 | 0.000 | -0.143 |
| vt_only=1,col1=2.4 | 14 | 0.000 | 0.000 | 0.000 | -0.071 |
| vt_only=1,col1=2.7 | 14 | 0.000 | 0.000 | 0.000 | -0.500 |
| vt_only=1,col1=3 | 14 | 0.000 | 0.000 | 0.000 | -0.643 |
| vt_only=1.1,col1=2.1 | 14 | 0.000 | 0.000 | 0.000 | 1.786 |
| vt_only=1.1,col1=2.4 | 14 | 0.000 | 0.000 | 0.000 | 1.857 |
| vt_only=1.1,col1=2.7 | 14 | 0.000 | 0.000 | 0.000 | 1.571 |
| vt_only=1.1,col1=3 | 14 | 0.000 | 0.000 | 0.000 | 1.429 |

## Any vt_only_lane evidence (winner has vt_only_lane evidence; may also have straight evidence)

| Weights | vt_any rows | Top8% | Top12% | Top20% | avg Δrank (vt_any) |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8,col1=2.4 | 65 | 0.046 | 0.077 | 0.154 | 0.000 |
| vt_only=0.8,col1=2.1 | 65 | 0.031 | 0.077 | 0.154 | 0.123 |
| vt_only=0.8,col1=2.7 | 65 | 0.046 | 0.077 | 0.154 | -0.308 |
| vt_only=0.8,col1=3 | 65 | 0.046 | 0.077 | 0.138 | -0.646 |
| vt_only=0.9,col1=2.1 | 65 | 0.031 | 0.077 | 0.154 | 0.323 |
| vt_only=0.9,col1=2.4 | 65 | 0.046 | 0.077 | 0.154 | 0.185 |
| vt_only=0.9,col1=2.7 | 65 | 0.046 | 0.077 | 0.154 | -0.015 |
| vt_only=0.9,col1=3 | 65 | 0.046 | 0.077 | 0.138 | -0.415 |
| vt_only=1,col1=2.1 | 65 | 0.031 | 0.077 | 0.154 | 0.354 |
| vt_only=1,col1=2.4 | 65 | 0.046 | 0.077 | 0.154 | 0.169 |
| vt_only=1,col1=2.7 | 65 | 0.046 | 0.077 | 0.138 | -0.092 |
| vt_only=1,col1=3 | 65 | 0.046 | 0.077 | 0.138 | -0.462 |
| vt_only=1.1,col1=2.1 | 65 | 0.031 | 0.077 | 0.138 | 0.938 |
| vt_only=1.1,col1=2.4 | 65 | 0.046 | 0.077 | 0.138 | 0.908 |
| vt_only=1.1,col1=2.7 | 65 | 0.062 | 0.077 | 0.138 | 0.585 |
| vt_only=1.1,col1=3 | 65 | 0.062 | 0.077 | 0.138 | 0.215 |

## Outputs

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2025-06-21_to_2025-06-23.csv`
- MD: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2025-06-21_to_2025-06-23.md`
