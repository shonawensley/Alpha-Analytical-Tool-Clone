# Env Verdict Label Gaps — B36 (MV synthesis)

Purpose
- Identify which outcome rows (date/state/period) are **missing** `env_verdict` labels in MV synthesis.
- This explains `UNLABELED` buckets in posture scoreboards and tells you exactly what to open to label them.

Inputs
- MV synthesis labels: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`
- Window `2026-01-01_to_2026-01-09`: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.csv`
- Window `2026-01-15_to_2026-01-22`: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only.csv`

How to use
1) Pick a missing row below.
2) Open the suggested `run_report_guess` if it exists (best), otherwise open the portfolio + results for context.
3) Add (or fill) the `env_verdict` for that (date, state, period) row in `corpus_summary.csv`.

## Coverage summary

| Window | Rows (winner-present) | Rows with non-empty env_verdict | Missing |
|---|---:|---:|---:|
| 2026-01-01_to_2026-01-09 | 245 | 245 | 0 |
| 2026-01-15_to_2026-01-22 | 193 | 193 | 0 |

No gaps found for the requested windows/budget.

