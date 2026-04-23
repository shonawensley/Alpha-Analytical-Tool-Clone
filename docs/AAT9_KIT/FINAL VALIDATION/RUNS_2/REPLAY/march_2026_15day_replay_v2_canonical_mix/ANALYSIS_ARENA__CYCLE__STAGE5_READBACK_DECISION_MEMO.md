# Analysis Arena Stage 5 Readback Decision Memo

Purpose: convert Stage 5 fixture evaluator outputs into explicit shadow-spec, support, restraint, watchlist, and documentation gates before any translator/scoring rewrite.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix`
- mode_decisions: `9`
- next_actions: `12`
- matched_stage5_rows: `12155`
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
| clean_boxed_only | watchlist_retest | retest_before_design | 13.107 | 46.6% | 23.978 | 100.0% | no_live_permission |
| clean_lineage_supported_restrained | watchlist_retest | retest_before_design | 43.375 | 40.9% | 23.919 | 100.0% | no_live_permission |
| clean_plus_lineage_deduped | candidate_foundation_needs_pool_control | narrow_before_design | 62.640 | 47.2% | 21.296 | 100.0% | no_live_permission |
| clean_with_restraint_filter | watchlist_retest | retest_before_design | 38.737 | 41.0% | 25.815 | 100.0% | no_live_permission |
| clean_with_support_context | broad_context_needs_narrowing | narrow_before_design | 69.279 | 46.9% | 21.450 | 100.0% | no_live_permission |
| decay_watch_companion | companion_only | keep_separate | 109.100 | 82.5% | 4.382 | 100.0% | no_live_permission |
| low_denominator_watchlist | watchlist_retest | retest_before_design | 6.415 | 36.1% | 23.954 | 100.0% | no_live_permission |
| restraint_retest | restraint_calibration | retest_before_design | 52.310 | 59.3% | 16.612 | 100.0% | no_live_permission |
| support_gate_context | support_modifier_only | keep_as_context | 102.857 | 58.1% | 19.317 | 100.0% | no_live_permission |

## Support Context Read
| bucket | rows | state-days | FP proxy | yield | read |
| --- | --- | --- | --- | --- | --- |
| candidate_rows_with_support_context | 1581 | 77 | 46.9% | 21.450 | context_modifier_only |
| candidate_rows_without_support_context | 73 | 13 | 52.3% | 18.301 | context_modifier_only |

## Restraint Read
| bucket | rows | state-days | FP proxy | yield | read |
| --- | --- | --- | --- | --- | --- |
| kept_by_restraint_filter | 434 | 19 | 41.0% | 25.815 | penalty_research_only |
| removed_by_high_restraint_pressure | 1220 | 54 | 49.1% | 19.908 | penalty_research_only |

## Ablation Read
- ablation_rows: `39`
- positive_overlap_lift_rows: `0`
- pool_reduction_rows: `38`
- interpretation: overlap should be treated as narrowing/restraint unless it beats the best individual source.

## Next Action Queue
| priority | type | subject | allowed | action |
| --- | --- | --- | --- | --- |
| 1 | retest_before_design | clean_boxed_only | no_live_permission | Keep as a retest/watchlist row and require more state-days before specification work. |
| 2 | retest_before_design | clean_lineage_supported_restrained | no_live_permission | Keep as a retest/watchlist row and require more state-days before specification work. |
| 3 | narrow_before_design | clean_plus_lineage_deduped | no_live_permission | Use as a foundation for narrowed variants, not as a direct translator rule. |
| 4 | retest_before_design | clean_with_restraint_filter | no_live_permission | Keep as a retest/watchlist row and require more state-days before specification work. |
| 5 | narrow_before_design | clean_with_support_context | no_live_permission | Test support as a paired modifier against clean/restrained candidate rows. |
| 6 | retest_before_design | low_denominator_watchlist | no_live_permission | Keep as a retest/watchlist row and require more state-days before specification work. |
| 7 | retest_before_design | restraint_retest | no_live_permission | Use to calibrate future penalty/veto surfaces; do not promote as candidate generation. |
| 8 | window_concentration_guardrail | positive_conversion_labels | shadow_spec_with_concentration_warning | Treat positive-conversion metrics as March-led until future/fresh windows repeat the same readback shape. |
| 9 | ablation_guardrail | source_a_source_b_overlap | no_duplicate_credit | Treat overlap as narrowing/restraint unless it beats the best individual source on support rate. |
| 10 | support_gate_policy | support_context | context_modifier_only | Keep support context as paired context, not standalone candidate expression. |
| 11 | restraint_calibration | restraint_filter | penalty_research_only | Calibrate restraint as penalty/veto pressure, not an automatic discard rule. |
| 12 | macro_findings_gate | macro_findings_log | provisional_only_until_repeat | Do not append a confirmed macro finding until Stage 5 readback conclusions repeat on a future/fresh window or are explicitly reviewed as provisional. |

## Documentation Memory Rule
- `WORKFLOW_CHANGELOG.md` records what was built or changed.
- `AAT9_ANALYSIS_ARENA__SYSTEM_INDEX.md` records what is part of the active package and where it feeds.
- `AAT9_ANALYSIS_ARENA__MACRO_FINDINGS_LOG.md` records evidence-led findings after review, especially repeated or explicitly provisional conclusions.
- RUNS/RUNS_2 reports and receipts record exact run outputs.
- Git commits record exact implementation checkpoints.

## Output Files
- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_DECISION_MEMO.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_DECISION_MEMO.json`
- mode_decisions_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_MODE_DECISIONS.csv`
- next_action_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_READBACK_NEXT_ACTION_QUEUE.csv`
