# Analysis Arena Stage 5 Shadow Translator Fixture Evaluator

Purpose: replay Stage 4C shadow translator lanes against completed Stage 2B state-day fixtures without changing live scoring or candidate generation.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2`
- value_level_replay_rows: `7656`
- prototype_modes: `9`
- ablation_rows: `42`
- support_ablation_rows: `16`
- restraint_audit_rows: `6`
- casebook_rows: `120`

## Guardrails
- Stage 5 is read-only and cannot change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.
- Stage 5 evaluates fixture behavior; it does not create deployable candidate lists.
- VTRAC/decay remains a companion mode and cannot become boxed spend permission.
- Support gates are context filters/modifiers, not standalone candidates.
- Negative-control and concentration pressure are tested as restraint surfaces.
- Value-level claims are valid only for rows marked `value_level_complete`; truncated samples remain aggregate-only evidence.

## Value Completeness
- matched_stage5_rows: `7656`
- matched_value_level_complete: `7656`
- matched_sample_truncated: `0`
- matched_sample_completeness_rate: `100.0%`

## Prototype Lane Rows

- `decay_watch_only`: `2915`
- `support_gate_only`: `2352`
- `lineage_guarded_boxed_candidate`: `1493`
- `concentration_retest_or_restraint`: `463`
- `low_denominator_watchlist`: `307`
- `clean_boxed_candidate`: `126`

## Prototype Mode Scorecard

| mode | rows | ASD | avg pool | pos/100 ASD | wrong-free/100 ASD | FP proxy | complete |
|---|---:|---:|---:|---:|---:|---:|---:|
| `clean_boxed_only` | 126 | 22 | 8.864 | 495.455 | 495.455 | 35.4% | 100.0% |
| `clean_lineage_supported_restrained` | 387 | 17 | 41.941 | 2123.529 | 2123.529 | 45.7% | 100.0% |
| `clean_plus_lineage_deduped` | 1619 | 38 | 87.421 | 4165.789 | 4165.789 | 51.3% | 100.0% |
| `clean_with_restraint_filter` | 1117 | 27 | 78.481 | 4040.741 | 4040.741 | 47.3% | 100.0% |
| `clean_with_support_context` | 788 | 26 | 61.885 | 2892.308 | 2892.308 | 51.0% | 100.0% |
| `decay_watch_companion` | 2915 | 171 | 110.485 | 1080.702 | 484.795 | 83.0% | 100.0% |
| `low_denominator_watchlist` | 307 | 34 | 14.206 | 873.529 | 873.529 | 36.4% | 100.0% |
| `restraint_retest` | 463 | 31 | 29.290 | 1441.935 | 1441.935 | 49.0% | 100.0% |
| `support_gate_context` | 2352 | 46 | 137.522 | 5054.348 | 5054.348 | 62.8% | 100.0% |

## PRO_44 Compliance

- `split_replay_by_mechanism_family`: `covered` - do_not_blend_all_candidates_into_one_pool
- `legacy_names_are_locators_not_rule_names`: `covered` - future architecture references mechanism_family and future_primitive
- `shared_lineage_deduplication`: `covered_for_replay_modes` - lineage rows do not become independent confirmation credit
- `source_a_source_b_overlap_ablation`: `covered_aggregate_stage4_backed` - overlap cannot be claimed useful without source-side baseline
- `yield_denominator_metrics`: `covered` - do_not_rank_by_raw_hit_counts
- `state_concentration_read`: `covered` - do_not_promote_one_state_fragility
- `negative_controls_as_restraint_assets`: `covered` - negative controls are penalty/veto surfaces, not promotion surfaces
- `vtrac_decay_not_boxed_permission`: `covered` - territory persistence cannot become boxed spend permission
- `sample_completeness_before_value_level_claims`: `new_stage5_control` - do_not_overclaim_truncated_samples

## Top Source A / Source B / Overlap Ablations

| mode | lane | mechanism | overlap lift | pool reduction | interpretation |
|---|---:|---:|---:|---:|---|
| `restraint_retest` | `concentration_retest_or_restraint` | `due_doubles_support_spine` | -15.736 | 1.111 | overlap_reduces_pool_but_does_not_beat_best_source |
| `restraint_retest` | `concentration_retest_or_restraint` | `profit_alert_related_boxed_overlap` | -17.470 | 1.623 | overlap_reduces_pool_but_does_not_beat_best_source |
| `support_gate_context` | `support_gate_only` | `r_perm_spine` | -24.116 | 2.410 | overlap_reduces_pool_but_does_not_beat_best_source |
| `clean_plus_lineage_deduped` | `lineage_guarded_boxed_candidate` | `old_play_card_expression_spine` | -24.512 | 2.729 | overlap_reduces_pool_but_does_not_beat_best_source |
| `restraint_retest` | `concentration_retest_or_restraint` | `vtrac_enhanced_secondary_spine` | -24.751 | 2.693 | overlap_reduces_pool_but_does_not_beat_best_source |
| `restraint_retest` | `concentration_retest_or_restraint` | `mirror_pair_closure_spine` | -27.763 | 2.915 | overlap_reduces_pool_but_does_not_beat_best_source |
| `restraint_retest` | `concentration_retest_or_restraint` | `r_perm_spine` | -28.121 | 2.552 | overlap_reduces_pool_but_does_not_beat_best_source |
| `low_denominator_watchlist` | `low_denominator_watchlist` | `old_play_card_expression_spine` | -29.604 | 2.068 | overlap_reduces_pool_but_does_not_beat_best_source |
| `restraint_retest` | `concentration_retest_or_restraint` | `misc_stage3_replay` | -29.956 | 2.771 | overlap_reduces_pool_but_does_not_beat_best_source |
| `clean_plus_lineage_deduped` | `lineage_guarded_boxed_candidate` | `r_perm_spine` | -29.993 | 2.563 | overlap_reduces_pool_but_does_not_beat_best_source |

## Interpretation
- Stage 5 moves the work from cluster-level governance into fixture-backed shadow expression evaluation.
- The key read is not whether every mode has high raw support; it is which modes preserve positive conversion while controlling pool size, duplicate lineage, support-only evidence, and restraint pressure.
- This is still a pre-rewrite evidence layer. Any actual translator/scoring rewrite should be specified only after Stage 5 results are reviewed.

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.json`
- value_completeness_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_COMPLETENESS_AUDIT.csv`
- value_ledger_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_REPLAY_LEDGER.csv`
- mode_scorecard_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_PROTOTYPE_MODE_SCORECARD.csv`
- ablation_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_ABLATION_MATRIX.csv`
- window_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_WINDOW_STRATIFICATION.csv`
- state_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_STATE_STRATIFICATION.csv`
- restraint_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_RESTRAINT_EFFECT_AUDIT.csv`
- support_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_SUPPORT_GATE_ABLATION.csv`
- pro44_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_PRO44_COMPLIANCE_CHECKLIST.csv`
- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_CASEBOOK.csv`
- casebook_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_CASEBOOK.md`
