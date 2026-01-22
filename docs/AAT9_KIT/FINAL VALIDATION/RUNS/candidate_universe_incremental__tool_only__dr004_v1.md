# Candidate Universe — Incremental Report

Reporting-only: compares `__UNION__` rows between baseline and experiment-tag grade outputs.

## Inputs

- RUNS dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS`
- Profile: `tool_only`
- Baseline tag: `—`
- Experiment tag: `dr004_v1`
- Focus method prefix: `digit_reduction_dr004`

## Summary (union hit_any)

| Rows | base hit_any | exp hit_any | incremental | regressions | avg base cost | avg exp cost | avg Δcost | Δcost / incremental |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 382 | 0.2382 | 0.2487 | 4 | 0 | 163.77 | 175.13 | 11.36 | 1084.75 |

## Breakdown (winner_label × winner_type)

| winner_label | winner_type | Rows | base hit_any | exp hit_any | incremental | regressions | avg Δcost | Δcost / incremental |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Evening | double | 57 | 0.3158 | 0.3158 | 0 | 0 | 10.46 |  |
| Evening | unique | 135 | 0.2370 | 0.2519 | 2 | 0 | 11.73 | 791.50 |
| Midday | double | 47 | 0.2979 | 0.2979 | 0 | 0 | 11.09 |  |
| Midday | triple | 3 | 0.0000 | 0.3333 | 1 | 0 | 14.00 | 42.00 |
| Midday | unique | 140 | 0.1929 | 0.2000 | 1 | 0 | 11.41 | 1597.00 |

## Incremental-hit cases (baseline miss → experiment hit)

| Date | State | Outcome | Winner | Winner type | focus_hit_any | focus_sanity | Δcost |
|---|---|---|---:|---|---:|---|---:|
| 2025-12-30 | Michigan4 | Midday | 250 | unique | 1 | ok | 12 |
| 2026-01-01 | SouthCarolina4 | Evening | 821 | unique | 1 | ok | 8 |
| 2026-01-06 | OntarioCanada4 | Midday | 111 | triple | 1 | ok | 15 |
| 2026-01-08 | Pennsylvania4 | Evening | 574 | unique | 1 | ok | 12 |

## Outputs

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_incremental__tool_only__dr004_v1.csv`
- MD: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_incremental__tool_only__dr004_v1.md`
