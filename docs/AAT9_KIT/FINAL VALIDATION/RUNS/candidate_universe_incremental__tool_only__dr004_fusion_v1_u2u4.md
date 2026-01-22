# Candidate Universe — Incremental Report

Reporting-only: compares `__UNION__` rows between baseline and experiment-tag grade outputs.

## Inputs

- RUNS dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS`
- Profile: `tool_only`
- Baseline tag: `—`
- Experiment tag: `dr004_fusion_v1_u2u4`
- Focus method prefix: `fusion_gate_dr004`

## Summary (union hit_any)

| Rows | base hit_any | exp hit_any | incremental | regressions | avg base cost | avg exp cost | avg Δcost | Δcost / incremental |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 382 | 0.2382 | 0.2330 | 2 | 4 | 163.77 | 172.72 | 8.95 | 1710.00 |

## Breakdown (winner_label × winner_type)

| winner_label | winner_type | Rows | base hit_any | exp hit_any | incremental | regressions | avg Δcost | Δcost / incremental |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Evening | double | 57 | 0.3158 | 0.3158 | 0 | 0 | 8.25 |  |
| Evening | unique | 135 | 0.2370 | 0.2296 | 0 | 1 | 9.33 |  |
| Midday | double | 47 | 0.2979 | 0.3191 | 1 | 0 | 8.09 | 380.00 |
| Midday | triple | 3 | 0.0000 | 0.0000 | 0 | 0 | 10.00 |  |
| Midday | unique | 140 | 0.1929 | 0.1786 | 1 | 3 | 9.15 | 1281.00 |

## Incremental-hit cases (baseline miss → experiment hit)

| Date | State | Outcome | Winner | Winner type | focus_hit_any | focus_sanity | Δcost |
|---|---|---|---:|---|---:|---|---:|
| 2026-01-07 | OntarioCanada4 | Midday | 547 | unique | 0 | missing | 27 |
| 2026-01-09 | Pennsylvania4 | Midday | 811 | double | 1 | ok | 23 |

## Regression cases (baseline hit → experiment miss)

| Date | State | Outcome | Winner | Winner type | Δcost |
|---|---|---|---:|---|---:|
| 2025-06-22 | NorthCarolina4 | Evening | 153 | unique | -3 |
| 2026-01-03 | Florida4 | Midday | 708 | unique | 15 |
| 2026-01-04 | NewJersey4 | Midday | 275 | unique | 10 |
| 2026-01-07 | Michigan4 | Midday | 692 | unique | -9 |

## Outputs

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_incremental__tool_only__dr004_fusion_v1_u2u4.csv`
- MD: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_incremental__tool_only__dr004_fusion_v1_u2u4.md`
