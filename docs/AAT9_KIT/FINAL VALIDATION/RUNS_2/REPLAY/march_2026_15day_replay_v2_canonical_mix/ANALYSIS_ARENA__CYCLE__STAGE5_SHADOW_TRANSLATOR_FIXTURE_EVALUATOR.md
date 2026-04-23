# Analysis Arena Stage 5 Shadow Translator Fixture Evaluator

Purpose: replay Stage 4C shadow translator lanes against completed Stage 2B state-day fixtures without changing live scoring or candidate generation.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix`
- value_level_replay_rows: `12155`
- prototype_modes: `9`
- ablation_rows: `39`
- support_ablation_rows: `10`
- restraint_audit_rows: `4`
- casebook_rows: `120`

## Guardrails
- Stage 5 is read-only and cannot change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.
- Stage 5 evaluates fixture behavior; it does not create deployable candidate lists.
- VTRAC/decay remains a companion mode and cannot become boxed spend permission.
- Support gates are context filters/modifiers, not standalone candidates.
- Negative-control and concentration pressure are tested as restraint surfaces.
- Value-level claims are valid only for rows marked `value_level_complete`; truncated samples remain aggregate-only evidence.

## Value Completeness
- matched_stage5_rows: `12155`
- matched_value_level_complete: `12155`
- matched_sample_truncated: `0`
- matched_sample_completeness_rate: `100.0%`

## Prototype Lane Rows

- `decay_watch_only`: `5475`
- `support_gate_only`: `3623`
- `lineage_guarded_boxed_candidate`: `1458`
- `concentration_retest_or_restraint`: `1235`
- `clean_boxed_candidate`: `196`
- `low_denominator_watchlist`: `168`

## Prototype Mode Scorecard

| mode | rows | ASD | avg pool | pos/100 ASD | wrong-free/100 ASD | FP proxy | complete |
|---|---:|---:|---:|---:|---:|---:|---:|
| `clean_boxed_only` | 196 | 28 | 13.107 | 314.286 | 314.286 | 46.6% | 100.0% |
| `clean_lineage_supported_restrained` | 410 | 16 | 43.375 | 1037.500 | 1037.500 | 40.9% | 100.0% |
| `clean_plus_lineage_deduped` | 1654 | 50 | 62.640 | 1334.000 | 1334.000 | 47.2% | 100.0% |
| `clean_with_restraint_filter` | 434 | 19 | 38.737 | 1000.000 | 1000.000 | 41.0% | 100.0% |
| `clean_with_support_context` | 1581 | 43 | 69.279 | 1486.047 | 1486.047 | 46.9% | 100.0% |
| `decay_watch_companion` | 5475 | 310 | 109.100 | 478.065 | 194.516 | 82.5% | 100.0% |
| `low_denominator_watchlist` | 168 | 41 | 6.415 | 153.659 | 153.659 | 36.1% | 100.0% |
| `restraint_retest` | 1235 | 58 | 52.310 | 868.966 | 868.966 | 59.3% | 100.0% |
| `support_gate_context` | 3623 | 84 | 102.857 | 1986.905 | 1983.333 | 58.1% | 100.0% |

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
| `restraint_retest` | `concentration_retest_or_restraint` | `due_doubles_support_spine` | -7.526 | 0.875 | overlap_reduces_pool_but_does_not_beat_best_source |
| `low_denominator_watchlist` | `low_denominator_watchlist` | `due_doubles_support_spine` | -13.505 | 2.125 | overlap_reduces_pool_but_does_not_beat_best_source |
| `low_denominator_watchlist` | `low_denominator_watchlist` | `r_perm_spine` | -17.144 | 1.965 | overlap_reduces_pool_but_does_not_beat_best_source |
| `clean_boxed_only` | `clean_boxed_candidate` | `vtrac_enhanced_secondary_spine` | -24.462 | 2.791 | overlap_reduces_pool_but_does_not_beat_best_source |
| `clean_plus_lineage_deduped` | `clean_boxed_candidate` | `vtrac_enhanced_secondary_spine` | -24.462 | 2.791 | overlap_reduces_pool_but_does_not_beat_best_source |
| `restraint_retest` | `concentration_retest_or_restraint` | `old_play_card_expression_spine` | -24.997 | 2.320 | overlap_reduces_pool_but_does_not_beat_best_source |
| `low_denominator_watchlist` | `low_denominator_watchlist` | `old_play_card_expression_spine` | -25.879 | 3.466 | overlap_reduces_pool_but_does_not_beat_best_source |
| `restraint_retest` | `concentration_retest_or_restraint` | `mirror_pair_closure_spine` | -26.901 | 2.315 | overlap_reduces_pool_but_does_not_beat_best_source |
| `restraint_retest` | `concentration_retest_or_restraint` | `vtrac_enhanced_secondary_spine` | -28.495 | 2.465 | overlap_reduces_pool_but_does_not_beat_best_source |
| `clean_plus_lineage_deduped` | `lineage_guarded_boxed_candidate` | `r_perm_spine` | -29.134 | 2.579 | overlap_reduces_pool_but_does_not_beat_best_source |

## Interpretation
- Stage 5 moves the work from cluster-level governance into fixture-backed shadow expression evaluation.
- The key read is not whether every mode has high raw support; it is which modes preserve positive conversion while controlling pool size, duplicate lineage, support-only evidence, and restraint pressure.
- This is still a pre-rewrite evidence layer. Any actual translator/scoring rewrite should be specified only after Stage 5 results are reviewed.

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.json`
- value_completeness_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_COMPLETENESS_AUDIT.csv`
- value_ledger_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_REPLAY_LEDGER.csv`
- mode_scorecard_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_PROTOTYPE_MODE_SCORECARD.csv`
- ablation_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_ABLATION_MATRIX.csv`
- window_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_WINDOW_STRATIFICATION.csv`
- state_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_STATE_STRATIFICATION.csv`
- restraint_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_RESTRAINT_EFFECT_AUDIT.csv`
- support_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_SUPPORT_GATE_ABLATION.csv`
- pro44_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_PRO44_COMPLIANCE_CHECKLIST.csv`
- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_CASEBOOK.csv`
- casebook_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_CASEBOOK.md`
