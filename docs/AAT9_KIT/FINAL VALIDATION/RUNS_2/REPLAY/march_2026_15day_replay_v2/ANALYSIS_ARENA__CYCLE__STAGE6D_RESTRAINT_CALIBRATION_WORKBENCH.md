# Analysis Arena Stage 6D Restraint Calibration Workbench

## Guardrail

Stage 6D is read-only. It turns restraint evidence into research buckets and soft-penalty hypotheses only; it does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

## Executive Readback

- restraint bucket rows generated: `0`
- high-pressure rescue/downweight candidates generated: `0`
- The aggregate hard-exclusion reference is useful evidence, but Stage 6D keeps it blocked from live use and focuses on soft-before-hard calibration.

## Top High-Pressure Buckets

| candidate_id | bucket_id | positive | fp | yield | recommended_use |
| --- | --- | --- | --- | --- | --- |

## Soft-Penalty Policy Matrix

| policy_id | fp | yield | positive | permission |
| --- | --- | --- | --- | --- |
| no_penalty_all_candidate_rows | 0.0% | 0.000 | 0.000 | reference_only |
| hard_exclusion_non_high_pressure | 0.0% | 0.000 | 0.000 | reference_only |
| removed_high_pressure_candidate_rows | 0.0% | 0.000 | 0.000 | reference_only |
| soft_penalty_keep_high_25pct | 0.0% | 0.000 | 0.000 | penalty_research_only |
| soft_penalty_keep_high_50pct | 0.0% | 0.000 | 0.000 | penalty_research_only |
| soft_penalty_keep_high_75pct | 0.0% | 0.000 | 0.000 | penalty_research_only |
| stage6d_recommendation | 0.0% | 0.000 | 0.000 | penalty_research_only |

## Next Actions

| priority | action_type | subject | action |
| --- | --- | --- | --- |
| 1 | soft_penalty_grid_replay | restraint_pressure_high | Replay high-pressure rows under soft penalty bands rather than hard exclusion. |
| 2 | rescue_bucket_review | high_pressure_rescue_candidates | Inspect rescue buckets before declaring high pressure globally bad; the aggregate is weaker but contains conversions. |
| 3 | future_window_confirmation | restraint_soft_penalty | Run this workbench after each future Stage 6B replay to see whether restraint calibration repeats. |

## Outputs

- workbench_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_CALIBRATION_WORKBENCH.json`
- restraint_bucket_scorecard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_BUCKET_SCORECARD.csv`
- high_pressure_rescue_candidates: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6D_HIGH_PRESSURE_RESCUE_CANDIDATES.csv`
- soft_penalty_policy_matrix: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6D_SOFT_PENALTY_POLICY_MATRIX.csv`
- restraint_next_actions: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_NEXT_ACTIONS.csv`
