# Analysis Arena Stage 6B Readback Decision Memo

Purpose: convert Stage 6B shadow replay outputs into explicit readback decisions before any translator/scoring rewrite discussion.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2`
- scenario_decisions: `11`
- requirement_results: `7`
- guardrail_verdict_rows: `4`
- next_actions: `6`

## Guardrails
- Stage 6B readback grants no live scoring, candidate-generation, translator, budget, or legacy-infrastructure permission.
- Primary favorable replay is not a rewrite trigger until future/fresh windows repeat the shape.
- Support-only, decay/watch, low-denominator, broad-lineage, and restraint surfaces remain separated.
- Macro Findings Log entries should stay provisional unless repeated or explicitly reviewed as evidence-led conclusions.

## Executive Readback
- Primary restrained lane decision: `blocked_guardrail_failure` with FP proxy `47.3%`, yield `51.487`, and avg pool `78.481`.
- The primary lane is the best current shadow-design seed, but it requires future/fresh-window confirmation before rewrite specification.
- Secondary lineage support is useful as modifier/retest context, not as independent expansion.
- Support-on behavior is not yet validated as a positive modifier; support remains context-only until narrower paired support passes.
- Restraint remains promising penalty research, with soft-before-hard calibration required.
- Decay/watch remains companion-only, not boxed candidate permission.

## Scenario Decisions
| scenario | decision | status | permission | FP proxy | yield | top-window share |
| --- | --- | --- | --- | --- | --- | --- |
| baseline_clean_boxed | blocked_guardrail_failure | blocked | blocked | 35.4% | 55.897 | 51.4% |
| primary_restrained_candidate_expression | blocked_guardrail_failure | blocked | blocked | 47.3% | 51.487 | 46.2% |
| secondary_lineage_supported_restrained | blocked_guardrail_failure | blocked | blocked | 45.7% | 50.631 | 63.7% |
| stage6a_allowed_candidate_union | blocked_guardrail_failure | blocked | blocked | 47.3% | 51.487 | 46.2% |
| broad_lineage_foundation_reference | blocked_guardrail_failure | blocked | blocked | 51.3% | 47.652 | 46.6% |
| candidate_rows_with_support_context | blocked_guardrail_failure | blocked | blocked | 51.0% | 46.737 | 55.7% |
| candidate_rows_without_support_context | blocked_guardrail_failure | blocked | blocked | 51.5% | 48.511 | 50.3% |
| support_gate_context_excluded | blocked_guardrail_failure | blocked | blocked | 62.8% | 36.753 | 51.3% |
| decay_watch_companion_excluded | blocked_guardrail_failure | blocked | blocked | 83.0% | 9.781 | 54.6% |
| low_denominator_watchlist_excluded | blocked_guardrail_failure | blocked | blocked | 36.4% | 61.491 | 51.5% |
| restraint_retest_surface_excluded | blocked_guardrail_failure | blocked | blocked | 49.0% | 49.229 | 47.0% |

## Requirement Results
| requirement | target | result | next action |
| --- | --- | --- | --- |
| S6B-001 | primary_restrained_candidate_expression | fail | Do not advance primary lane. |
| S6B-002 | secondary_lineage_supported_restrained | partial_modifier_only | Keep as lineage/support modifier research only. |
| S6B-003 | support_context_modifier | fail_as_positive_modifier | Keep support-only excluded and search for narrower paired support conditions. |
| S6B-004 | restraint_calibration_surface | pass_research_not_live | Build soft-penalty calibration before any hard veto design. |
| S6B-005 | source_a_source_b_overlap | pass | Keep overlap as narrowing/restraint unless future source-side ablation proves lift. |
| S6B-006 | window_and_state_concentration | fail | Require future/fresh repeat before rewrite claims. |
| S6B-007 | decay_watch_companion | pass_excluded | Keep as carryforward/context only. |

## Guardrail Verdict
| area | status | verdict |
| --- | --- | --- |
| stage6b_compliance | fail | Reject readback until Stage 6B compliance is repaired. |
| live_permission | pass | No live scoring/candidate/budget permission granted. |
| lane_separation | pass | Candidate, support, decay, low-denominator, and restraint lanes remain separate. |
| stage6a_guardrails_referenced | pass | Stage 6A contract is available for readback. |

## Next Action Queue
| priority | type | subject | permission | action |
| --- | --- | --- | --- | --- |
| 1 | support_modifier_rework | support_context | support_research_only | Do not promote support-on as a positive modifier yet; build narrower paired support hypotheses only. |
| 2 | restraint_soft_penalty_calibration | restraint_filter | penalty_research_only | Design soft-penalty calibration before any hard veto or hard exclusion rule. |
| 3 | lineage_narrowing | broad_lineage_foundation_reference | narrowing_research_only | Derive narrowed lineage variants; do not promote broad lineage foundation directly. |
| 4 | decay_companion_boundary | decay_watch_companion | companion_only | Keep decay/watch as carryforward annotations and out of candidate pool metrics. |
| 5 | macro_findings_gate | macro_findings_log | provisional_only_until_repeat | Treat Stage 6B findings as provisional candidates until repeated on future/fresh windows or explicitly reviewed. |
| 6 | rewrite_block | translator_scoring_rewrite | blocked_until_future_confirmation | Do not begin a live translator/scoring rewrite from this readback alone. |

## Macro Findings Candidates
| finding | posture | recommended action |
| --- | --- | --- |
| S6B-MF-001 | provisional_candidate | Hold for future-window confirmation or explicitly log as provisional only. |
| S6B-MF-002 | provisional_candidate | Keep as engineering/research finding unless repeated across future windows. |
| S6B-MF-003 | provisional_supporting_evidence | Reference in readback; promote to macro only after repeated fresh-window confirmation or explicit review. |
| S6B-MF-004 | provisional_candidate | Keep as penalty research follow-up. |

## Interpretation
- Stage 6B readback is favorable enough to preserve the primary restrained lane as the next research spine.
- It is not favorable enough to start a live rewrite because the evidence is still March-concentrated and support/restraint calibration is unfinished.
- The next development layer should be future-window confirmation and soft-penalty/narrow-support design, not live scoring or budget changes.

## Output Files
- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO.json`
- scenario_decisions_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_SCENARIO_DECISIONS.csv`
- requirement_results_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_REQUIREMENT_RESULTS.csv`
- guardrail_verdict_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_GUARDRAIL_VERDICT.csv`
- next_action_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_NEXT_ACTION_QUEUE.csv`
- macro_findings_candidates_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_MACRO_FINDINGS_CANDIDATES.csv`
