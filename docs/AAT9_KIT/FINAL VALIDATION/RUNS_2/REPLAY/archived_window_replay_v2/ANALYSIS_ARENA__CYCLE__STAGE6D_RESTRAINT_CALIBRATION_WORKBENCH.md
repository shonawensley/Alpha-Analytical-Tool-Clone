# Analysis Arena Stage 6D Restraint Calibration Workbench

## Guardrail

Stage 6D is read-only. It turns restraint evidence into research buckets and soft-penalty hypotheses only; it does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

## Executive Readback

- restraint bucket rows generated: `37`
- high-pressure rescue/downweight candidates generated: `17`
- The aggregate hard-exclusion reference is useful evidence, but Stage 6D keeps it blocked from live use and focuses on soft-before-hard calibration.

## Top High-Pressure Buckets

| candidate_id | bucket_id | positive | fp | yield | recommended_use |
| --- | --- | --- | --- | --- | --- |
| S6D-RESCUE-003 | pressure_support::high::support_on | 391 | 55.2% | 43.638 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-004 | pressure_mechanism::high::vtrac_enhanced_secondary_spine | 246 | 50.5% | 47.582 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-005 | pressure_mechanism_lane::high::vtrac_enhanced_secondary_spine::lineage_guarded_boxed_candidate | 242 | 50.7% | 47.544 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-009 | high_pressure_cluster::vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:b36_budget_surface | 101 | 54.0% | 44.690 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-011 | high_pressure_cluster::vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:b24_budget_surface | 76 | 52.1% | 46.061 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-012 | high_pressure_cluster::old_play_card_expression_spine::legacy_budget_expression_locator::old_candidate_universe:aux_vtrac_index_overdue+old_play_card:b12_budget_surface | 74 | 50.7% | 49.333 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-013 | high_pressure_cluster::vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:b12_budget_surface | 36 | 27.5% | 70.588 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-017 | high_pressure_cluster::vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:stable_top+old_candidate_universe:vtrac_enhanced_top | 13 | 54.5% | 39.394 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-001 | pressure::high | 492 | 58.3% | 40.898 | high_pressure_downweight_candidate |
| S6D-RESCUE-002 | pressure_lane::high::lineage_guarded_boxed_candidate | 488 | 58.4% | 40.837 | high_pressure_downweight_candidate |

## Soft-Penalty Policy Matrix

| policy_id | fp | yield | positive | permission |
| --- | --- | --- | --- | --- |
| no_penalty_all_candidate_rows | 51.3% | 47.652 | 1583.000 | reference_only |
| hard_exclusion_non_high_pressure | 47.3% | 51.487 | 1091.000 | reference_only |
| removed_high_pressure_candidate_rows | 58.3% | 40.898 | 492.000 | reference_only |
| soft_penalty_keep_high_25pct | 48.7% | 50.170 | 1214.000 | penalty_research_only |
| soft_penalty_keep_high_50pct | 49.7% | 49.145 | 1337.000 | penalty_research_only |
| soft_penalty_keep_high_75pct | 50.6% | 48.324 | 1460.000 | penalty_research_only |
| stage6d_recommendation | 0.0% | 0.000 | 0.000 | penalty_research_only |

## Next Actions

| priority | action_type | subject | action |
| --- | --- | --- | --- |
| 1 | soft_penalty_grid_replay | restraint_pressure_high | Replay high-pressure rows under soft penalty bands rather than hard exclusion. |
| 2 | rescue_bucket_review | high_pressure_rescue_candidates | Inspect rescue buckets before declaring high pressure globally bad; the aggregate is weaker but contains conversions. |
| 3 | future_window_confirmation | restraint_soft_penalty | Run this workbench after each future Stage 6B replay to see whether restraint calibration repeats. |

## Outputs

- workbench_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_CALIBRATION_WORKBENCH.json`
- restraint_bucket_scorecard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_BUCKET_SCORECARD.csv`
- high_pressure_rescue_candidates: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6D_HIGH_PRESSURE_RESCUE_CANDIDATES.csv`
- soft_penalty_policy_matrix: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6D_SOFT_PENALTY_POLICY_MATRIX.csv`
- restraint_next_actions: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_NEXT_ACTIONS.csv`
