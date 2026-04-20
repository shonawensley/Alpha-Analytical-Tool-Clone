# Analysis Arena Stage 6B Readback Decision Memo

Purpose: convert Stage 6B shadow replay outputs into explicit readback decisions before any translator/scoring rewrite discussion.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- scenario_decisions: `11`
- requirement_results: `7`
- guardrail_verdict_rows: `4`
- next_actions: `7`

## Guardrails
- Stage 6B readback grants no live scoring, candidate-generation, translator, budget, or legacy-infrastructure permission.
- Primary favorable replay is not a rewrite trigger until future/fresh windows repeat the shape.
- Support-only, decay/watch, low-denominator, broad-lineage, and restraint surfaces remain separated.
- Macro Findings Log entries should stay provisional unless repeated or explicitly reviewed as evidence-led conclusions.

## Executive Readback
- Primary restrained lane decision: `provisional_primary_shadow_design_seed` with FP proxy `46.8%`, yield `16.075`, and avg pool `69.032`.
- The primary lane is the best current shadow-design seed, but it requires future/fresh-window confirmation before rewrite specification.
- Secondary lineage support is useful as modifier/retest context, not as independent expansion.
- Support-on behavior is not yet validated as a positive modifier; support remains context-only until narrower paired support passes.
- Restraint remains promising penalty research, with soft-before-hard calibration required.
- Decay/watch remains companion-only, not boxed candidate permission.

## Scenario Decisions
| scenario | decision | status | permission | FP proxy | yield | top-window share |
| --- | --- | --- | --- | --- | --- | --- |
| baseline_clean_boxed | baseline_reference_only | baseline_only | baseline_only | 60.4% | 12.407 | 100.0% |
| primary_restrained_candidate_expression | provisional_primary_shadow_design_seed | future_window_confirmation_required | readback_only_no_live_permission | 46.8% | 16.075 | 100.0% |
| secondary_lineage_supported_restrained | secondary_modifier_not_independent_expansion | keep_as_lineage_modifier_retest | modifier_research_only | 46.3% | 13.395 | 100.0% |
| stage6a_allowed_candidate_union | duplicate_credit_blocked_cleanly | guardrail_pass_reference | readback_reference_only | 46.8% | 16.075 | 100.0% |
| broad_lineage_foundation_reference | broad_lineage_blocked_until_narrowed | narrow_before_design | narrowing_research_only | 54.5% | 14.372 | 100.0% |
| candidate_rows_with_support_context | support_on_not_validated_as_modifier | modifier_not_ready | support_research_only | 55.4% | 12.969 | 100.0% |
| candidate_rows_without_support_context | support_off_reference_is_sharper | support_ablation_reference | reference_only | 48.9% | 23.895 | 100.0% |
| support_gate_context_excluded | support_gate_remains_context_only | context_only | context_only | 57.4% | 16.018 | 100.0% |
| decay_watch_companion_excluded | decay_watch_remains_companion_only | companion_only | companion_only | 82.5% | 3.920 | 100.0% |
| low_denominator_watchlist_excluded | low_denominator_watchlist_retest | retest_only | retest_only | 28.2% | 20.513 | 100.0% |
| restraint_retest_surface_excluded | restraint_surface_promising_but_excluded | penalty_research_only | penalty_research_only | 32.8% | 22.492 | 100.0% |

## Requirement Results
| requirement | target | result | next action |
| --- | --- | --- | --- |
| S6B-001 | primary_restrained_candidate_expression | pass_with_concentration_warning | Repeat on future/fresh windows before rewrite specification. |
| S6B-002 | secondary_lineage_supported_restrained | partial_modifier_only | Keep as lineage/support modifier research only. |
| S6B-003 | support_context_modifier | fail_as_positive_modifier | Keep support-only excluded and search for narrower paired support conditions. |
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
| 1 | future_window_confirmation | primary_restrained_candidate_expression | readback_only_no_live_permission | Repeat Stage 6B replay/readback on future/fresh windows before any translator/scoring rewrite specification. |
| 2 | support_modifier_rework | support_context | support_research_only | Do not promote support-on as a positive modifier yet; build narrower paired support hypotheses only. |
| 3 | restraint_soft_penalty_calibration | restraint_filter | penalty_research_only | Design soft-penalty calibration before any hard veto or hard exclusion rule. |
| 4 | lineage_narrowing | broad_lineage_foundation_reference | narrowing_research_only | Derive narrowed lineage variants; do not promote broad lineage foundation directly. |
| 5 | decay_companion_boundary | decay_watch_companion | companion_only | Keep decay/watch as carryforward annotations and out of candidate pool metrics. |
| 6 | macro_findings_gate | macro_findings_log | provisional_only_until_repeat | Treat Stage 6B findings as provisional candidates until repeated on future/fresh windows or explicitly reviewed. |
| 7 | rewrite_block | translator_scoring_rewrite | blocked_until_future_confirmation | Do not begin a live translator/scoring rewrite from this readback alone. |

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
- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO.json`
- scenario_decisions_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_SCENARIO_DECISIONS.csv`
- requirement_results_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_REQUIREMENT_RESULTS.csv`
- guardrail_verdict_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_GUARDRAIL_VERDICT.csv`
- next_action_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_NEXT_ACTION_QUEUE.csv`
- macro_findings_candidates_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_MACRO_FINDINGS_CANDIDATES.csv`
