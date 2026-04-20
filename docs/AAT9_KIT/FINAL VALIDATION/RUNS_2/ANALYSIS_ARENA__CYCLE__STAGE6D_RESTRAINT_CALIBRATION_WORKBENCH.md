# Analysis Arena Stage 6D Restraint Calibration Workbench

## Guardrail

Stage 6D is read-only. It turns restraint evidence into research buckets and soft-penalty hypotheses only; it does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

## Executive Readback

- restraint bucket rows generated: `38`
- high-pressure rescue/downweight candidates generated: `16`
- The aggregate hard-exclusion reference is useful evidence, but Stage 6D keeps it blocked from live use and focuses on soft-before-hard calibration.

## Top High-Pressure Buckets

| candidate_id | bucket_id | positive | fp | yield | recommended_use |
| --- | --- | --- | --- | --- | --- |
| S6D-RESCUE-012 | high_pressure_cluster::positional_spine::bounded_positional_box_overlap::old_candidate_universe:aux_positional+old_play_card:b12_budget_surface | 50 | 47.8% | 18.382 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-015 | high_pressure_cluster::positional_spine::bounded_positional_box_overlap::old_play_card:b12_budget_surface+positional:positional_canonical | 39 | 47.6% | 18.571 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-016 | high_pressure_cluster::positional_spine::bounded_positional_box_overlap::old_play_card:b12_budget_surface+positional:positional_combo | 39 | 47.6% | 18.571 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-001 | pressure_support::high::support_on | 502 | 62.8% | 12.623 | high_pressure_downweight_candidate |
| S6D-RESCUE-002 | pressure::high | 502 | 62.8% | 12.550 | high_pressure_downweight_candidate |
| S6D-RESCUE-003 | pressure_mechanism::high::positional_spine | 494 | 63.1% | 12.456 | high_pressure_downweight_candidate |
| S6D-RESCUE-004 | pressure_lane::high::clean_boxed_candidate | 294 | 62.2% | 12.312 | high_pressure_downweight_candidate |
| S6D-RESCUE-005 | pressure_mechanism_lane::high::positional_spine::clean_boxed_candidate | 286 | 62.7% | 12.150 | high_pressure_downweight_candidate |
| S6D-RESCUE-006 | pressure_lane::high::lineage_guarded_boxed_candidate | 208 | 63.6% | 12.903 | high_pressure_downweight_candidate |
| S6D-RESCUE-007 | pressure_mechanism_lane::high::positional_spine::lineage_guarded_boxed_candidate | 208 | 63.6% | 12.903 | high_pressure_downweight_candidate |

## Soft-Penalty Policy Matrix

| policy_id | fp | yield | positive | permission |
| --- | --- | --- | --- | --- |
| no_penalty_all_candidate_rows | 54.5% | 14.372 | 1190.000 | reference_only |
| hard_exclusion_non_high_pressure | 46.8% | 16.075 | 688.000 | reference_only |
| removed_high_pressure_candidate_rows | 62.8% | 12.550 | 502.000 | reference_only |
| soft_penalty_keep_high_25pct | 49.8% | 15.407 | 813.500 | penalty_research_only |
| soft_penalty_keep_high_50pct | 51.9% | 14.952 | 939.000 | penalty_research_only |
| soft_penalty_keep_high_75pct | 53.4% | 14.622 | 1064.500 | penalty_research_only |
| stage6d_recommendation | 0.0% | 0.000 | 0.000 | penalty_research_only |

## Next Actions

| priority | action_type | subject | action |
| --- | --- | --- | --- |
| 1 | soft_penalty_grid_replay | restraint_pressure_high | Replay high-pressure rows under soft penalty bands rather than hard exclusion. |
| 2 | rescue_bucket_review | high_pressure_rescue_candidates | Inspect rescue buckets before declaring high pressure globally bad; the aggregate is weaker but contains conversions. |
| 3 | future_window_confirmation | restraint_soft_penalty | Run this workbench after each future Stage 6B replay to see whether restraint calibration repeats. |

## Outputs

- workbench_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_CALIBRATION_WORKBENCH.json`
- restraint_bucket_scorecard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_BUCKET_SCORECARD.csv`
- high_pressure_rescue_candidates: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_HIGH_PRESSURE_RESCUE_CANDIDATES.csv`
- soft_penalty_policy_matrix: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_SOFT_PENALTY_POLICY_MATRIX.csv`
- restraint_next_actions: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_NEXT_ACTIONS.csv`
