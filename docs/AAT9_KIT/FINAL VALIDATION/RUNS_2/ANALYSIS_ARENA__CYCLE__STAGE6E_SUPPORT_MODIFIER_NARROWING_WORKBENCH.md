# Analysis Arena Stage 6E Support Modifier Narrowing Workbench

## Guardrail

Stage 6E is read-only. It tests support context as a narrow paired modifier only; it does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

## Executive Readback

- support bucket rows generated: `110`
- support narrowing/retest candidates generated: `5`
- support failure rows generated: `10`
- Broad support-on failed Stage 6B readback, so Stage 6E searches only for narrow support pockets that beat a matched support-off peer.

## Top Support Narrowing Candidates

| candidate_id | bucket_id | peer | positive | fp_delta_peer | yield_delta_peer | recommended_use |
| --- | --- | --- | --- | --- | --- | --- |
| S6E-SUPPORT-001 | support_mechanism::support_on::vtrac_enhanced_secondary_spine | support_mechanism::support_off::vtrac_enhanced_secondary_spine | 98 | -0.200 | 2.174 | narrow_support_modifier_candidate |
| S6E-SUPPORT-002 | support_mechanism_lane::support_on::vtrac_enhanced_secondary_spine::lineage_guarded_boxed_candidate | support_mechanism_lane::support_off::vtrac_enhanced_secondary_spine::lineage_guarded_boxed_candidate | 81 | -0.212 | 1.899 | narrow_support_modifier_candidate |
| S6E-SUPPORT-003 | support_cluster::support_on::vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:b36_budget_surface | support_cluster::support_off::vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:b36_budget_surface | 29 | -0.180 | 0.191 | narrow_support_modifier_candidate |
| S6E-SUPPORT-004 | support_pressure::support_on::medium | support_pressure::support_off::medium | 434 | -0.022 | -11.028 | mixed_support_modifier_retest |
| S6E-SUPPORT-005 | support_cluster::support_on::mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:b12_budget_surface | support_cluster::support_off::mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:b12_budget_surface | 20 | -0.050 | -20.655 | mixed_support_modifier_retest |

## Failure Modes

| failure_id | failure_mode | recommended_response |
| --- | --- | --- |
| S6E-FAIL-001 | broad_support_on_is_not_a_positive_modifier | Keep broad support-on out of scoring and search only for narrow paired buckets. |
| S6E-FAIL-002 | support_gate_standalone_stays_context_only | Do not convert support-gate context into candidate-pool permission. |
| S6E-FAIL-003 | narrow_bucket_support_on_failed_peer_test | Keep as support context only unless a future window reverses the paired peer test. |
| S6E-FAIL-004 | narrow_bucket_support_on_failed_peer_test | Keep as support context only unless a future window reverses the paired peer test. |
| S6E-FAIL-005 | narrow_bucket_support_on_failed_peer_test | Keep as support context only unless a future window reverses the paired peer test. |
| S6E-FAIL-006 | narrow_bucket_support_on_failed_peer_test | Keep as support context only unless a future window reverses the paired peer test. |
| S6E-FAIL-007 | narrow_bucket_support_on_failed_peer_test | Keep as support context only unless a future window reverses the paired peer test. |
| S6E-FAIL-008 | narrow_bucket_support_on_failed_peer_test | Keep as support context only unless a future window reverses the paired peer test. |
| S6E-FAIL-009 | narrow_bucket_support_on_failed_peer_test | Keep as support context only unless a future window reverses the paired peer test. |
| S6E-FAIL-010 | narrow_bucket_support_on_failed_peer_test | Keep as support context only unless a future window reverses the paired peer test. |

## Next Actions

| priority | action_type | subject | action |
| --- | --- | --- | --- |
| 1 | support_narrowing_replay | narrow_support_modifier_candidates | Replay only narrow support candidates that beat their support-off peer; do not use broad support-on. |
| 2 | support_failure_quarantine | support_on_failure_modes | Keep failed support-on buckets as context-only annotations and exclude from candidate-pool permission. |
| 3 | future_window_confirmation | support_modifier_boundary | Rerun Stage 6E after the next fresh Stage 6B replay to test whether any support pockets repeat. |

## Outputs

- workbench_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_MODIFIER_NARROWING_WORKBENCH.json`
- support_bucket_scorecard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_BUCKET_SCORECARD.csv`
- support_narrowing_candidates: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_NARROWING_CANDIDATES.csv`
- support_failure_modes: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_FAILURE_MODES.csv`
- support_next_actions: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_NEXT_ACTIONS.csv`
