# AAT9 Analysis Arena - March Run2 Canonical Mix Readback

## Verdict

The existing March Run2 replay package should not be rerun in place. Its candidate window package exists and is complete, but its first cycle-level Stage6B-through-Stage7B outputs were generated as a one-window-only cycle. That one-window cycle is useful as a diagnostic, but it is not the comparable evidence shape for cross-window promotion or rewrite-gate review.

The corrected comparison target is the canonical replacement cycle:

`docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix`

This cycle uses the three canonical archived windows plus the existing March Run2 candidate window:

| Role | Window |
|---|---|
| archived canonical | `WINDOW_2025-12-30_to_2026-01-04` |
| archived canonical | `WINDOW_2026-01-05_to_2026-01-09` |
| archived canonical | `WINDOW_2026-01-15_to_2026-01-22` |
| same-window replay candidate | `REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23` |

## Comparison Result

The corrected baseline-vs-candidate comparison is complete:

| Metric | Result |
|---|---:|
| total comparison targets | 26 |
| candidate completeness | complete |
| missing required candidate targets | 0 |
| unchanged targets | 26 |
| improved-traceability targets | 0 |
| degraded targets | 0 |
| contradicted targets | 0 |
| blocked-by-missing-data targets | 0 |

The comparison report is:

`docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.md`

## Interpretation

The March Run2 package is a deterministic same-window replay confirmation against the preserved baseline. It supports regression checking, reproducibility, traceability review, and confidence that the canonical replacement path is wired correctly.

It does not provide true fresh-window confirmation. Stage8A, live scoring, candidate-generation rewrite, boxed/straight expression rewrite, and budget rewrite remain blocked.

## Guardrail

Do not interpret the older one-window-only Run2 cycle as a failed March replay. Its Stage6B guardrail failure came from evaluating a cross-window promotion pipeline with only one candidate window. The corrected canonical mix restores the intended comparison shape and removes the false contradiction/degradation signal.
