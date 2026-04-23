# Analysis Arena Stage 6D Restraint Calibration Workbench

## Guardrail

Stage 6D is read-only. It turns restraint evidence into research buckets and soft-penalty hypotheses only; it does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

## Executive Readback

- restraint bucket rows generated: `36`
- high-pressure rescue/downweight candidates generated: `20`
- The aggregate hard-exclusion reference is useful evidence, but Stage 6D keeps it blocked from live use and focuses on soft-before-hard calibration.

## Top High-Pressure Buckets

| candidate_id | bucket_id | positive | fp | yield | recommended_use |
| --- | --- | --- | --- | --- | --- |
| S6D-RESCUE-002 | pressure_support::high::support_on | 473 | 48.8% | 20.700 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-008 | pressure_mechanism::high::vtrac_enhanced_secondary_spine | 91 | 38.5% | 20.588 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-009 | pressure_mechanism_lane::high::vtrac_enhanced_secondary_spine::lineage_guarded_boxed_candidate | 89 | 38.6% | 20.554 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-010 | pressure_lane::high::clean_boxed_candidate | 88 | 46.6% | 23.978 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-011 | pressure_mechanism::high::positional_spine | 78 | 47.3% | 26.000 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-012 | pressure_mechanism_lane::high::positional_spine::clean_boxed_candidate | 78 | 47.3% | 26.000 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-013 | high_pressure_cluster::positional_spine::bounded_positional_box_overlap::old_play_card:b12_budget_surface+positional:positional_canonical | 39 | 47.3% | 26.000 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-014 | high_pressure_cluster::positional_spine::bounded_positional_box_overlap::old_play_card:b12_budget_surface+positional:positional_combo | 39 | 47.3% | 26.000 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-015 | high_pressure_cluster::vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:b36_budget_surface | 38 | 43.4% | 18.537 | high_pressure_rescue_candidate_soft_penalty_only |
| S6D-RESCUE-016 | high_pressure_cluster::mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:b12_budget_surface | 38 | 44.2% | 20.000 | high_pressure_rescue_candidate_soft_penalty_only |

## Soft-Penalty Policy Matrix

| policy_id | fp | yield | positive | permission |
| --- | --- | --- | --- | --- |
| no_penalty_all_candidate_rows | 47.2% | 21.296 | 667.000 | reference_only |
| hard_exclusion_non_high_pressure | 41.0% | 25.815 | 190.000 | reference_only |
| removed_high_pressure_candidate_rows | 49.1% | 19.908 | 477.000 | reference_only |
| soft_penalty_keep_high_25pct | 44.6% | 23.165 | 309.250 | penalty_research_only |
| soft_penalty_keep_high_50pct | 46.0% | 22.156 | 428.500 | penalty_research_only |
| soft_penalty_keep_high_75pct | 46.7% | 21.625 | 547.750 | penalty_research_only |
| stage6d_recommendation | 0.0% | 0.000 | 0.000 | penalty_research_only |

## Next Actions

| priority | action_type | subject | action |
| --- | --- | --- | --- |
| 1 | soft_penalty_grid_replay | restraint_pressure_high | Replay high-pressure rows under soft penalty bands rather than hard exclusion. |
| 2 | rescue_bucket_review | high_pressure_rescue_candidates | Inspect rescue buckets before declaring high pressure globally bad; the aggregate is weaker but contains conversions. |
| 3 | future_window_confirmation | restraint_soft_penalty | Run this workbench after each future Stage 6B replay to see whether restraint calibration repeats. |

## Outputs

- workbench_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_CALIBRATION_WORKBENCH.json`
- restraint_bucket_scorecard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_BUCKET_SCORECARD.csv`
- high_pressure_rescue_candidates: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6D_HIGH_PRESSURE_RESCUE_CANDIDATES.csv`
- soft_penalty_policy_matrix: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6D_SOFT_PENALTY_POLICY_MATRIX.csv`
- restraint_next_actions: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_NEXT_ACTIONS.csv`
