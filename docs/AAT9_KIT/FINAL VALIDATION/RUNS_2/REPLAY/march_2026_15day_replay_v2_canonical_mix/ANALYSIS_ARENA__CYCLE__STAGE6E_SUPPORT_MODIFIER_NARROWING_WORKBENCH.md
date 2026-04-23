# Analysis Arena Stage 6E Support Modifier Narrowing Workbench

## Guardrail

Stage 6E is read-only. It tests support context as a narrow paired modifier only; it does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

## Executive Readback

- support bucket rows generated: `65`
- support narrowing/retest candidates generated: `4`
- support failure rows generated: `2`
- Broad support-on failed Stage 6B readback, so Stage 6E searches only for narrow support pockets that beat a matched support-off peer.

## Top Support Narrowing Candidates

| candidate_id | bucket_id | peer | positive | fp_delta_peer | yield_delta_peer | recommended_use |
| --- | --- | --- | --- | --- | --- | --- |
| S6E-SUPPORT-001 | support::support_on | support::support_off | 639 | -0.054 | 3.149 | narrow_support_modifier_candidate |
| S6E-SUPPORT-002 | support_pressure::support_on::high | support_pressure::support_off::high | 473 | -0.071 | 17.097 | narrow_support_modifier_candidate |
| S6E-SUPPORT-003 | support_mechanism::support_on::mirror_pair_closure_spine | support_mechanism::support_off::mirror_pair_closure_spine | 304 | -0.074 | 12.869 | narrow_support_modifier_candidate |
| S6E-SUPPORT-004 | support_lane::support_on::lineage_guarded_boxed_candidate | support_lane::support_off::lineage_guarded_boxed_candidate | 551 | -0.056 | -0.118 | mixed_support_modifier_retest |

## Failure Modes

| failure_id | failure_mode | recommended_response |
| --- | --- | --- |
| S6E-FAIL-001 | broad_support_on_is_not_a_positive_modifier | Keep broad support-on out of scoring and search only for narrow paired buckets. |
| S6E-FAIL-002 | support_gate_standalone_stays_context_only | Do not convert support-gate context into candidate-pool permission. |

## Next Actions

| priority | action_type | subject | action |
| --- | --- | --- | --- |
| 1 | support_narrowing_replay | narrow_support_modifier_candidates | Replay only narrow support candidates that beat their support-off peer; do not use broad support-on. |
| 2 | support_failure_quarantine | support_on_failure_modes | Keep failed support-on buckets as context-only annotations and exclude from candidate-pool permission. |
| 3 | future_window_confirmation | support_modifier_boundary | Rerun Stage 6E after the next fresh Stage 6B replay to test whether any support pockets repeat. |

## Outputs

- workbench_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_MODIFIER_NARROWING_WORKBENCH.json`
- support_bucket_scorecard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_BUCKET_SCORECARD.csv`
- support_narrowing_candidates: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_NARROWING_CANDIDATES.csv`
- support_failure_modes: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_FAILURE_MODES.csv`
- support_next_actions: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_NEXT_ACTIONS.csv`
