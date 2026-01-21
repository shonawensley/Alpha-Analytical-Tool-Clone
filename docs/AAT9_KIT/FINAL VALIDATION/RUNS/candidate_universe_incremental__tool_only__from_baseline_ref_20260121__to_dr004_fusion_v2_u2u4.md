# Candidate Universe — Incremental Report

Reporting-only: compares `__UNION__` rows between baseline and experiment-tag grade outputs.

## Inputs

- RUNS dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS`
- Profile: `tool_only`
- Baseline tag: `baseline_ref_20260121`
- Experiment tag: `dr004_fusion_v2_u2u4`
- Focus method prefix: `fusion_gate_dr004`

## Summary (union hit_any)

| Rows | base hit_any | exp hit_any | incremental | regressions | avg base cost | avg exp cost | avg Δcost | Δcost / incremental |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 382 | 0.2382 | 0.2408 | 1 | 0 | 163.77 | 172.53 | 8.76 | 3346.00 |

## Breakdown (winner_label × winner_type)

| winner_label | winner_type | Rows | base hit_any | exp hit_any | incremental | regressions | avg Δcost | Δcost / incremental |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Evening | double | 57 | 0.3158 | 0.3158 | 0 | 0 | 7.60 |  |
| Evening | unique | 135 | 0.2370 | 0.2370 | 0 | 0 | 9.33 |  |
| Midday | double | 47 | 0.2979 | 0.3191 | 1 | 0 | 9.36 | 440.00 |
| Midday | triple | 3 | 0.0000 | 0.0000 | 0 | 0 | 7.33 |  |
| Midday | unique | 140 | 0.1929 | 0.1929 | 0 | 0 | 8.51 |  |

## Incremental-hit cases (baseline miss → experiment hit)

| Date | State | Outcome | Winner | Winner type | focus_hit_any | focus_sanity | Δcost |
|---|---|---|---:|---|---:|---|---:|
| 2026-01-09 | Pennsylvania4 | Midday | 811 | double | 1 | ok | 13 |

## Outputs

- CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_incremental__tool_only__from_baseline_ref_20260121__to_dr004_fusion_v2_u2u4.csv`
- MD: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_incremental__tool_only__from_baseline_ref_20260121__to_dr004_fusion_v2_u2u4.md`
