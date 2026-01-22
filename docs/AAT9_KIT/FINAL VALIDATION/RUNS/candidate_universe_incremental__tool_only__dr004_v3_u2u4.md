# Candidate Universe — Incremental Report

Reporting-only: compares `__UNION__` rows between baseline and experiment-tag grade outputs.

## Inputs

- RUNS dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS`
- Profile: `tool_only`
- Baseline tag: `—`
- Experiment tag: `dr004_v3_u2u4`
- Focus method prefix: `digit_reduction_dr004`

## Summary (union hit_any)

| Rows | base hit_any | exp hit_any | incremental | regressions | avg base cost | avg exp cost | avg Δcost | Δcost / incremental |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 382 | 0.2382 | 0.2461 | 3 | 0 | 163.77 | 182.86 | 19.09 | 2431.33 |

## Breakdown (winner_label × winner_type)

| winner_label | winner_type | Rows | base hit_any | exp hit_any | incremental | regressions | avg Δcost | Δcost / incremental |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Evening | double | 57 | 0.3158 | 0.3158 | 0 | 0 | 17.60 |  |
| Evening | unique | 135 | 0.2370 | 0.2519 | 2 | 0 | 19.74 | 1332.50 |
| Midday | double | 47 | 0.2979 | 0.2979 | 0 | 0 | 19.04 |  |
| Midday | triple | 3 | 0.0000 | 0.0000 | 0 | 0 | 17.67 |  |
| Midday | unique | 140 | 0.1929 | 0.2000 | 1 | 0 | 19.13 | 2678.00 |

## Incremental-hit cases (baseline miss → experiment hit)

| Date | State | Outcome | Winner | Winner type | focus_hit_any | focus_sanity | Δcost |
|---|---|---|---:|---|---:|---|---:|
| 2025-12-30 | Michigan4 | Midday | 250 | unique | 1 | ok | 18 |
| 2026-01-01 | SouthCarolina4 | Evening | 821 | unique | 1 | ok | 13 |
| 2026-01-08 | Pennsylvania4 | Evening | 574 | unique | 1 | ok | 21 |

## Outputs

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_incremental__tool_only__dr004_v3_u2u4.csv`
- MD: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_incremental__tool_only__dr004_v3_u2u4.md`
