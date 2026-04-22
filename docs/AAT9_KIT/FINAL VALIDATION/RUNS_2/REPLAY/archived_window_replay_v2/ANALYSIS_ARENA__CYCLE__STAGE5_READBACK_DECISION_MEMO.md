# Analysis Arena Stage 5 Readback Decision Memo

Purpose: convert Stage 5 fixture evaluator outputs into explicit shadow-spec, support, restraint, watchlist, and documentation gates before any translator/scoring rewrite.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2`
- mode_decisions: `9`
- next_actions: `11`
- matched_stage5_rows: `7656`
- matched_sample_completeness_rate: `100.0%`

## Guardrails
- This readback grants no live scoring, candidate-generation, translator, budget, or legacy-infrastructure permission.
- Stage 5 metrics are fixture evidence. They guide shadow specification and restraint design only.
- Support gates remain modifiers, VTRAC/decay remains companion context, and overlap does not receive duplicate-credit scoring unless it beats source A/source B baselines.
- The Macro Findings Log should receive distilled evidence-led conclusions, not raw infrastructure milestones.

## Executive Readback
- Stage 5 is complete enough to interpret: matched rows are value-level complete for the generated evaluator set.
- The strongest immediate design seed is the restrained candidate-expression lane, not a broad all-lane blend.
- Support context and decay/watch behavior remain valuable, but they are not standalone boxed/straight permission.
- Source overlap mostly acts as a pool-narrowing/restraint surface rather than independent confirmation.
- Positive-conversion labels are currently March-led in the Stage 5 readback, so cross-window structural coverage is not the same as repeated positive-conversion confirmation.
- The next work should be a shadow translator/scoring specification or narrowed fixture prototype, not a live scoring rewrite.

## Mode Decision Queue
| mode | decision | status | avg pool | FP proxy | yield | top window share | allowed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| clean_boxed_only | watchlist_retest | retest_before_design | 8.864 | 35.4% | 55.897 | 51.4% | no_live_permission |
| clean_lineage_supported_restrained | watchlist_retest | retest_before_design | 41.941 | 45.7% | 50.631 | 63.7% | no_live_permission |
| clean_plus_lineage_deduped | candidate_foundation_needs_pool_control | narrow_before_design | 87.421 | 51.3% | 47.652 | 46.6% | no_live_permission |
| clean_with_restraint_filter | watchlist_retest | retest_before_design | 78.481 | 47.3% | 51.487 | 46.2% | no_live_permission |
| clean_with_support_context | watchlist_retest | retest_before_design | 61.885 | 51.0% | 46.737 | 55.7% | no_live_permission |
| decay_watch_companion | companion_only | keep_separate | 110.485 | 83.0% | 9.781 | 54.6% | no_live_permission |
| low_denominator_watchlist | watchlist_retest | retest_before_design | 14.206 | 36.4% | 61.491 | 51.5% | no_live_permission |
| restraint_retest | restraint_calibration | retest_before_design | 29.290 | 49.0% | 49.229 | 47.0% | no_live_permission |
| support_gate_context | support_modifier_only | keep_as_context | 137.522 | 62.8% | 36.753 | 51.3% | no_live_permission |

## Support Context Read
| bucket | rows | state-days | FP proxy | yield | read |
| --- | --- | --- | --- | --- | --- |
| candidate_rows_with_support_context | 788 | 46 | 51.0% | 46.737 | context_modifier_only |
| candidate_rows_without_support_context | 831 | 42 | 51.5% | 48.511 | context_modifier_only |

## Restraint Read
| bucket | rows | state-days | FP proxy | yield | read |
| --- | --- | --- | --- | --- | --- |
| kept_by_restraint_filter | 1117 | 38 | 47.3% | 51.487 | penalty_research_only |
| removed_by_high_restraint_pressure | 502 | 28 | 58.3% | 40.898 | penalty_research_only |

## Ablation Read
- ablation_rows: `42`
- positive_overlap_lift_rows: `0`
- pool_reduction_rows: `42`
- interpretation: overlap should be treated as narrowing/restraint unless it beats the best individual source.

## Next Action Queue
| priority | type | subject | allowed | action |
| --- | --- | --- | --- | --- |
| 1 | retest_before_design | clean_boxed_only | no_live_permission | Keep as a retest/watchlist row and require more state-days before specification work. |
| 2 | retest_before_design | clean_lineage_supported_restrained | no_live_permission | Keep as a retest/watchlist row and require more state-days before specification work. |
| 3 | narrow_before_design | clean_plus_lineage_deduped | no_live_permission | Use as a foundation for narrowed variants, not as a direct translator rule. |
| 4 | retest_before_design | clean_with_restraint_filter | no_live_permission | Keep as a retest/watchlist row and require more state-days before specification work. |
| 5 | retest_before_design | clean_with_support_context | no_live_permission | Keep as a retest/watchlist row and require more state-days before specification work. |
| 6 | retest_before_design | low_denominator_watchlist | no_live_permission | Keep as a retest/watchlist row and require more state-days before specification work. |
| 7 | retest_before_design | restraint_retest | no_live_permission | Use to calibrate future penalty/veto surfaces; do not promote as candidate generation. |
| 8 | ablation_guardrail | source_a_source_b_overlap | no_duplicate_credit | Treat overlap as narrowing/restraint unless it beats the best individual source on support rate. |
| 9 | support_gate_policy | support_context | context_modifier_only | Keep support context as paired context, not standalone candidate expression. |
| 10 | restraint_calibration | restraint_filter | penalty_research_only | Calibrate restraint as penalty/veto pressure, not an automatic discard rule. |
| 11 | macro_findings_gate | macro_findings_log | provisional_only_until_repeat | Do not append a confirmed macro finding until Stage 5 readback conclusions repeat on a future/fresh window or are explicitly reviewed as provisional. |

## Documentation Memory Rule
- `WORKFLOW_CHANGELOG.md` records what was built or changed.
- `AAT9_ANALYSIS_ARENA__SYSTEM_INDEX.md` records what is part of the active package and where it feeds.
- `AAT9_ANALYSIS_ARENA__MACRO_FINDINGS_LOG.md` records evidence-led findings after review, especially repeated or explicitly provisional conclusions.
- RUNS/RUNS_2 reports and receipts record exact run outputs.
- Git commits record exact implementation checkpoints.

## Output Files
- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_DECISION_MEMO.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_DECISION_MEMO.json`
- mode_decisions_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_MODE_DECISIONS.csv`
- next_action_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_NEXT_ACTION_QUEUE.csv`
