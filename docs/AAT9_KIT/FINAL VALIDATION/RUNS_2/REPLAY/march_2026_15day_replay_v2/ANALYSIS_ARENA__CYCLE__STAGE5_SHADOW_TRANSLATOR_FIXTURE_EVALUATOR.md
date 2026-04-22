# Analysis Arena Stage 5 Shadow Translator Fixture Evaluator

Purpose: replay Stage 4C shadow translator lanes against completed Stage 2B state-day fixtures without changing live scoring or candidate generation.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2`
- value_level_replay_rows: `2698`
- prototype_modes: `1`
- ablation_rows: `4`
- support_ablation_rows: `0`
- restraint_audit_rows: `0`
- casebook_rows: `0`

## Guardrails
- Stage 5 is read-only and cannot change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.
- Stage 5 evaluates fixture behavior; it does not create deployable candidate lists.
- VTRAC/decay remains a companion mode and cannot become boxed spend permission.
- Support gates are context filters/modifiers, not standalone candidates.
- Negative-control and concentration pressure are tested as restraint surfaces.
- Value-level claims are valid only for rows marked `value_level_complete`; truncated samples remain aggregate-only evidence.

## Value Completeness
- matched_stage5_rows: `2698`
- matched_value_level_complete: `2698`
- matched_sample_truncated: `0`
- matched_sample_completeness_rate: `100.0%`

## Prototype Lane Rows

- `decay_watch_only`: `2698`

## Prototype Mode Scorecard

| mode | rows | ASD | avg pool | pos/100 ASD | wrong-free/100 ASD | FP proxy | complete |
|---|---:|---:|---:|---:|---:|---:|---:|
| `decay_watch_companion` | 2698 | 145 | 118.890 | 1027.586 | 413.103 | 83.4% | 100.0% |

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
| `decay_watch_companion` | `decay_watch_only` | `vtrac_enhanced_secondary_spine` | -39.560 | 2.033 | overlap_reduces_pool_but_does_not_beat_best_source |
| `decay_watch_companion` | `decay_watch_only` | `old_play_card_expression_spine` | -42.560 | 5.993 | overlap_reduces_pool_but_does_not_beat_best_source |
| `decay_watch_companion` | `decay_watch_only` | `vtrac_decay_watch_spine` | -45.092 | 2.147 | overlap_reduces_pool_but_does_not_beat_best_source |
| `decay_watch_companion` | `decay_watch_only` | `blackapple_related_boxed_overlap` | -46.075 | 4.049 | overlap_reduces_pool_but_does_not_beat_best_source |

## Interpretation
- Stage 5 moves the work from cluster-level governance into fixture-backed shadow expression evaluation.
- The key read is not whether every mode has high raw support; it is which modes preserve positive conversion while controlling pool size, duplicate lineage, support-only evidence, and restraint pressure.
- This is still a pre-rewrite evidence layer. Any actual translator/scoring rewrite should be specified only after Stage 5 results are reviewed.

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.json`
- value_completeness_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_COMPLETENESS_AUDIT.csv`
- value_ledger_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_REPLAY_LEDGER.csv`
- mode_scorecard_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_PROTOTYPE_MODE_SCORECARD.csv`
- ablation_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_ABLATION_MATRIX.csv`
- window_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_WINDOW_STRATIFICATION.csv`
- state_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_STATE_STRATIFICATION.csv`
- restraint_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_RESTRAINT_EFFECT_AUDIT.csv`
- support_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_SUPPORT_GATE_ABLATION.csv`
- pro44_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_PRO44_COMPLIANCE_CHECKLIST.csv`
- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_CASEBOOK.csv`
- casebook_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE5_VALUE_LEVEL_CASEBOOK.md`
