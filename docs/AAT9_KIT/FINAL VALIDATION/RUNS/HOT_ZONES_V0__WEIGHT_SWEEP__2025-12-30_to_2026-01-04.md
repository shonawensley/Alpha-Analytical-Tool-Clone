# Hot Zones — Weight Sweep (HOTZ-003 harness)

Reporting-only: reruns Hot Zones against frozen sharepack JSON tables and grades against results.

## Inputs

- Sharepacks root: `sharepacks`
- Dates: `2025-12-30` → `2026-01-04` (6 days requested)
- States (requested): 14
- Sweep: `w_vt_only_lane_bonus` = 0.8, 0.9, 1, 1.1 (baseline=vt_only=0.8)

## Summary (all winners; winner canonical in top-K)

| Weights | Rows | Top8% | Top12% | Top20% | avg Δrank vs baseline |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8 | 163 | 0.037 | 0.086 | 0.110 | 0.000 |
| vt_only=0.9 | 163 | 0.037 | 0.086 | 0.110 | 0.284 |
| vt_only=1 | 163 | 0.037 | 0.080 | 0.110 | 0.444 |
| vt_only=1.1 | 163 | 0.031 | 0.074 | 0.110 | 0.469 |

## VT-only visibility (winner has vt_only_lane evidence and **no** straight evidence)

| Weights | vt_only rows | Top8% | Top12% | Top20% | avg Δrank (vt_only) |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8 | 23 | 0.000 | 0.000 | 0.000 | 0.000 |
| vt_only=0.9 | 23 | 0.000 | 0.000 | 0.000 | 0.609 |
| vt_only=1 | 23 | 0.000 | 0.000 | 0.000 | 1.174 |
| vt_only=1.1 | 23 | 0.000 | 0.000 | 0.000 | 1.087 |

## Any vt_only_lane evidence (winner has vt_only_lane evidence; may also have straight evidence)

| Weights | vt_any rows | Top8% | Top12% | Top20% | avg Δrank (vt_any) |
|---|---:|---:|---:|---:|---:|
| vt_only=0.8 | 137 | 0.036 | 0.080 | 0.109 | 0.000 |
| vt_only=0.9 | 137 | 0.036 | 0.080 | 0.109 | 0.438 |
| vt_only=1 | 137 | 0.036 | 0.073 | 0.109 | 0.642 |
| vt_only=1.1 | 137 | 0.029 | 0.066 | 0.109 | 0.942 |

## Outputs

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP__2025-12-30_to_2026-01-04.csv`
- MD: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP__2025-12-30_to_2026-01-04.md`
