# Analysis Arena Stage 5 Shadow Translator Fixture Evaluator

Purpose: replay Stage 4C shadow translator lanes against completed Stage 2B state-day fixtures without changing live scoring or candidate generation.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- value_level_replay_rows: `14752`
- prototype_modes: `9`
- ablation_rows: `43`
- support_ablation_rows: `15`
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
- matched_stage5_rows: `14752`
- matched_value_level_complete: `14752`
- matched_sample_truncated: `0`
- matched_sample_completeness_rate: `100.0%`

## Prototype Lane Rows

- `decay_watch_only`: `6145`
- `support_gate_only`: `4288`
- `lineage_guarded_boxed_candidate`: `2702`
- `clean_boxed_candidate`: `1062`
- `concentration_retest_or_restraint`: `415`
- `low_denominator_watchlist`: `140`

## Prototype Mode Scorecard

| mode | rows | ASD | avg pool | pos/100 ASD | wrong-free/100 ASD | FP proxy | complete |
|---|---:|---:|---:|---:|---:|---:|---:|
| `clean_boxed_only` | 1062 | 53 | 50.642 | 628.302 | 628.302 | 60.4% | 100.0% |
| `clean_lineage_supported_restrained` | 1740 | 43 | 75.349 | 1009.302 | 1009.302 | 46.3% | 100.0% |
| `clean_plus_lineage_deduped` | 3764 | 71 | 116.620 | 1676.056 | 1676.056 | 54.5% | 100.0% |
| `clean_with_restraint_filter` | 2276 | 62 | 69.032 | 1109.677 | 1109.677 | 46.8% | 100.0% |
| `clean_with_support_context` | 3221 | 55 | 131.218 | 1701.818 | 1701.818 | 55.4% | 100.0% |
| `decay_watch_companion` | 6145 | 354 | 106.788 | 418.644 | 170.621 | 82.5% | 100.0% |
| `low_denominator_watchlist` | 140 | 40 | 4.875 | 100.000 | 100.000 | 28.2% | 100.0% |
| `restraint_retest` | 415 | 47 | 13.149 | 295.745 | 295.745 | 32.8% | 100.0% |
| `support_gate_context` | 4288 | 95 | 106.000 | 1697.895 | 1696.842 | 57.4% | 100.0% |

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
| `low_denominator_watchlist` | `low_denominator_watchlist` | `due_doubles_support_spine` | -12.672 | 2.227 | overlap_reduces_pool_but_does_not_beat_best_source |
| `low_denominator_watchlist` | `low_denominator_watchlist` | `r_perm_spine` | -17.633 | 1.977 | overlap_reduces_pool_but_does_not_beat_best_source |
| `restraint_retest` | `concentration_retest_or_restraint` | `profit_alert_related_boxed_overlap` | -21.328 | 1.959 | overlap_reduces_pool_but_does_not_beat_best_source |
| `restraint_retest` | `concentration_retest_or_restraint` | `vtrac_enhanced_secondary_spine` | -22.677 | 2.722 | overlap_reduces_pool_but_does_not_beat_best_source |
| `low_denominator_watchlist` | `low_denominator_watchlist` | `misc_stage3_replay` | -25.461 | 3.515 | overlap_reduces_pool_but_does_not_beat_best_source |
| `restraint_retest` | `concentration_retest_or_restraint` | `old_play_card_expression_spine` | -26.673 | 2.052 | overlap_reduces_pool_but_does_not_beat_best_source |
| `restraint_retest` | `concentration_retest_or_restraint` | `mirror_pair_closure_spine` | -26.767 | 2.596 | overlap_reduces_pool_but_does_not_beat_best_source |
| `restraint_retest` | `concentration_retest_or_restraint` | `misc_stage3_replay` | -27.457 | 2.725 | overlap_reduces_pool_but_does_not_beat_best_source |
| `clean_plus_lineage_deduped` | `lineage_guarded_boxed_candidate` | `vtrac_enhanced_secondary_spine` | -29.061 | 2.896 | overlap_reduces_pool_but_does_not_beat_best_source |
| `clean_plus_lineage_deduped` | `lineage_guarded_boxed_candidate` | `r_perm_spine` | -29.512 | 2.621 | overlap_reduces_pool_but_does_not_beat_best_source |

## Interpretation
- Stage 5 moves the work from cluster-level governance into fixture-backed shadow expression evaluation.
- The key read is not whether every mode has high raw support; it is which modes preserve positive conversion while controlling pool size, duplicate lineage, support-only evidence, and restraint pressure.
- This is still a pre-rewrite evidence layer. Any actual translator/scoring rewrite should be specified only after Stage 5 results are reviewed.

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.json`
- value_completeness_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_COMPLETENESS_AUDIT.csv`
- value_ledger_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_REPLAY_LEDGER.csv`
- mode_scorecard_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_PROTOTYPE_MODE_SCORECARD.csv`
- ablation_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_ABLATION_MATRIX.csv`
- window_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_WINDOW_STRATIFICATION.csv`
- state_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_STATE_STRATIFICATION.csv`
- restraint_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_RESTRAINT_EFFECT_AUDIT.csv`
- support_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_SUPPORT_GATE_ABLATION.csv`
- pro44_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_PRO44_COMPLIANCE_CHECKLIST.csv`
- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_CASEBOOK.csv`
- casebook_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_CASEBOOK.md`
