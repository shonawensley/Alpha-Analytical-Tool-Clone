# Analysis Arena Stage 6B Readback Decision Memo

Purpose: convert Stage 6B shadow replay outputs into explicit readback decisions before any translator/scoring rewrite discussion.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix`
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
- Primary restrained lane decision: `primary_not_ready` with FP proxy `41.0%`, yield `25.815`, and avg pool `38.737`.
- The primary lane is the best current shadow-design seed, but it requires future/fresh-window confirmation before rewrite specification.
- Secondary lineage support is useful as modifier/retest context, not as independent expansion.
- Support-on behavior is not yet validated as a positive modifier; support remains context-only until narrower paired support passes.
- Restraint remains promising penalty research, with soft-before-hard calibration required.
- Decay/watch remains companion-only, not boxed candidate permission.

## Scenario Decisions
| scenario | decision | status | permission | FP proxy | yield | top-window share |
| --- | --- | --- | --- | --- | --- | --- |
| baseline_clean_boxed | baseline_reference_only | baseline_only | baseline_only | 46.6% | 23.978 | 100.0% |
| primary_restrained_candidate_expression | primary_not_ready | blocked | blocked | 41.0% | 25.815 | 100.0% |
| secondary_lineage_supported_restrained | secondary_modifier_not_independent_expansion | keep_as_lineage_modifier_retest | modifier_research_only | 40.9% | 23.919 | 100.0% |
| stage6a_allowed_candidate_union | duplicate_credit_blocked_cleanly | guardrail_pass_reference | readback_reference_only | 41.0% | 25.815 | 100.0% |
| broad_lineage_foundation_reference | broad_lineage_blocked_until_narrowed | narrow_before_design | narrowing_research_only | 47.2% | 21.296 | 100.0% |
| candidate_rows_with_support_context | support_on_not_validated_as_modifier | modifier_not_ready | support_research_only | 46.9% | 21.450 | 100.0% |
| candidate_rows_without_support_context | support_off_reference_is_sharper | support_ablation_reference | reference_only | 52.3% | 18.301 | 100.0% |
| support_gate_context_excluded | support_gate_remains_context_only | context_only | context_only | 58.1% | 19.317 | 100.0% |
| decay_watch_companion_excluded | decay_watch_remains_companion_only | companion_only | companion_only | 82.5% | 4.382 | 100.0% |
| low_denominator_watchlist_excluded | low_denominator_watchlist_retest | retest_only | retest_only | 36.1% | 23.954 | 100.0% |
| restraint_retest_surface_excluded | restraint_surface_promising_but_excluded | penalty_research_only | penalty_research_only | 59.3% | 16.612 | 100.0% |

## Requirement Results
| requirement | target | result | next action |
| --- | --- | --- | --- |
| S6B-001 | primary_restrained_candidate_expression | fail | Do not advance primary lane. |
| S6B-002 | secondary_lineage_supported_restrained | partial_modifier_only | Keep as lineage/support modifier research only. |
| S6B-003 | support_context_modifier | pass_modifier_candidate | Retest support modifier on future windows. |
| S6B-004 | restraint_calibration_surface | pass_research_not_live | Build soft-penalty calibration before any hard veto design. |
| S6B-005 | source_a_source_b_overlap | pass | Keep overlap as narrowing/restraint unless future source-side ablation proves lift. |
| S6B-006 | window_and_state_concentration | pass_with_warning | Require future/fresh repeat before rewrite claims. |
| S6B-007 | decay_watch_companion | pass_excluded | Keep as carryforward/context only. |

## Guardrail Verdict
| area | status | verdict |
| --- | --- | --- |
| stage6b_compliance | pass | Readback may proceed. |
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
- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO.json`
- scenario_decisions_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_SCENARIO_DECISIONS.csv`
- requirement_results_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_REQUIREMENT_RESULTS.csv`
- guardrail_verdict_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_GUARDRAIL_VERDICT.csv`
- next_action_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_NEXT_ACTION_QUEUE.csv`
- macro_findings_candidates_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_MACRO_FINDINGS_CANDIDATES.csv`
