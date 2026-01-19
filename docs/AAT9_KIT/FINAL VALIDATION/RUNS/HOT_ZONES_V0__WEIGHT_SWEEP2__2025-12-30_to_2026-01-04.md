# Hot Zones — Weight Sweep (HOTZ-003 harness)

Reporting-only: reruns Hot Zones against frozen sharepack JSON tables and grades against results.

## Inputs

- Sharepacks root: `sharepacks`
- Dates: `2025-12-30` → `2026-01-04` (6 days requested)
- States (requested): 14
- Sweep: `w_vt_only_lane_bonus` = 0.8, 0.9, 1, 1.1; `w_col1_arrival` = 2.1, 2.4, 2.7, 3 (baseline=vt_only=0.8,col1=2.4)

## Summary (all winners; winner canonical in top-K)

| Weights | Rows | Top8% | Top12% | Top20% | avg Δrank vs baseline |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8,col1=2.4 | 163 | 0.037 | 0.086 | 0.110 | 0.000 |
| vt_only=0.8,col1=2.1 | 163 | 0.043 | 0.080 | 0.104 | 0.099 |
| vt_only=0.8,col1=2.7 | 163 | 0.037 | 0.080 | 0.110 | -0.093 |
| vt_only=0.8,col1=3 | 163 | 0.031 | 0.080 | 0.110 | -0.253 |
| vt_only=0.9,col1=2.1 | 163 | 0.043 | 0.080 | 0.104 | 0.407 |
| vt_only=0.9,col1=2.4 | 163 | 0.037 | 0.086 | 0.110 | 0.284 |
| vt_only=0.9,col1=2.7 | 163 | 0.037 | 0.080 | 0.110 | 0.235 |
| vt_only=0.9,col1=3 | 163 | 0.031 | 0.080 | 0.110 | 0.105 |
| vt_only=1,col1=2.1 | 163 | 0.043 | 0.080 | 0.110 | 0.611 |
| vt_only=1,col1=2.4 | 163 | 0.037 | 0.080 | 0.110 | 0.444 |
| vt_only=1,col1=2.7 | 163 | 0.037 | 0.080 | 0.110 | 0.414 |
| vt_only=1,col1=3 | 163 | 0.031 | 0.074 | 0.110 | 0.198 |
| vt_only=1.1,col1=2.1 | 163 | 0.037 | 0.074 | 0.110 | 0.642 |
| vt_only=1.1,col1=2.4 | 163 | 0.031 | 0.074 | 0.110 | 0.469 |
| vt_only=1.1,col1=2.7 | 163 | 0.031 | 0.074 | 0.110 | 0.451 |
| vt_only=1.1,col1=3 | 163 | 0.025 | 0.074 | 0.110 | 0.228 |

## VT-only visibility (winner has vt_only_lane evidence and **no** straight evidence)

| Weights | vt_only rows | Top8% | Top12% | Top20% | avg Δrank (vt_only) |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8,col1=2.4 | 23 | 0.000 | 0.000 | 0.000 | 0.000 |
| vt_only=0.8,col1=2.1 | 23 | 0.000 | 0.000 | 0.000 | 0.217 |
| vt_only=0.8,col1=2.7 | 23 | 0.000 | 0.000 | 0.000 | -0.217 |
| vt_only=0.8,col1=3 | 23 | 0.000 | 0.000 | 0.000 | -0.435 |
| vt_only=0.9,col1=2.1 | 23 | 0.000 | 0.000 | 0.000 | 0.783 |
| vt_only=0.9,col1=2.4 | 23 | 0.000 | 0.000 | 0.000 | 0.609 |
| vt_only=0.9,col1=2.7 | 23 | 0.000 | 0.000 | 0.000 | 0.435 |
| vt_only=0.9,col1=3 | 23 | 0.000 | 0.000 | 0.000 | 0.217 |
| vt_only=1,col1=2.1 | 23 | 0.000 | 0.000 | 0.000 | 1.391 |
| vt_only=1,col1=2.4 | 23 | 0.000 | 0.000 | 0.000 | 1.174 |
| vt_only=1,col1=2.7 | 23 | 0.000 | 0.000 | 0.000 | 1.000 |
| vt_only=1,col1=3 | 23 | 0.000 | 0.000 | 0.000 | 0.783 |
| vt_only=1.1,col1=2.1 | 23 | 0.000 | 0.000 | 0.000 | 1.304 |
| vt_only=1.1,col1=2.4 | 23 | 0.000 | 0.000 | 0.000 | 1.087 |
| vt_only=1.1,col1=2.7 | 23 | 0.000 | 0.000 | 0.000 | 0.913 |
| vt_only=1.1,col1=3 | 23 | 0.000 | 0.000 | 0.000 | 0.783 |

## Any vt_only_lane evidence (winner has vt_only_lane evidence; may also have straight evidence)

| Weights | vt_any rows | Top8% | Top12% | Top20% | avg Δrank (vt_any) |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8,col1=2.4 | 137 | 0.036 | 0.080 | 0.109 | 0.000 |
| vt_only=0.8,col1=2.1 | 137 | 0.044 | 0.080 | 0.102 | 0.139 |
| vt_only=0.8,col1=2.7 | 137 | 0.036 | 0.073 | 0.109 | -0.109 |
| vt_only=0.8,col1=3 | 137 | 0.029 | 0.073 | 0.109 | -0.307 |
| vt_only=0.9,col1=2.1 | 137 | 0.044 | 0.080 | 0.102 | 0.606 |
| vt_only=0.9,col1=2.4 | 137 | 0.036 | 0.080 | 0.109 | 0.438 |
| vt_only=0.9,col1=2.7 | 137 | 0.036 | 0.073 | 0.109 | 0.380 |
| vt_only=0.9,col1=3 | 137 | 0.029 | 0.073 | 0.109 | 0.241 |
| vt_only=1,col1=2.1 | 137 | 0.044 | 0.080 | 0.109 | 0.869 |
| vt_only=1,col1=2.4 | 137 | 0.036 | 0.073 | 0.109 | 0.642 |
| vt_only=1,col1=2.7 | 137 | 0.036 | 0.073 | 0.109 | 0.613 |
| vt_only=1,col1=3 | 137 | 0.029 | 0.066 | 0.109 | 0.387 |
| vt_only=1.1,col1=2.1 | 137 | 0.036 | 0.073 | 0.109 | 1.175 |
| vt_only=1.1,col1=2.4 | 137 | 0.029 | 0.066 | 0.109 | 0.942 |
| vt_only=1.1,col1=2.7 | 137 | 0.029 | 0.066 | 0.109 | 0.920 |
| vt_only=1.1,col1=3 | 137 | 0.022 | 0.066 | 0.109 | 0.679 |

## Outputs

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2025-12-30_to_2026-01-04.csv`
- MD: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2025-12-30_to_2026-01-04.md`
