# Analysis Arena Stage 4C Shadow Translator Prototype

Purpose: convert Stage 4B primitive clusters into a read-only shadow translator design package with strict lane separation.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2`
- prototype_rule_rows: `282`
- lane_matrix_rows: `6`
- support_gate_effect_rows: `77`
- restraint_audit_rows: `231`
- holdout_scorecard_rows: `18`
- casebook_rows: `88`

## Non-Negotiable Guardrails
- Stage 4C is read-only and cannot change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.
- Clean candidate lanes are aggregate shadow expressions only; they are not deployable candidate lists.
- Lineage-guarded lanes require duplicate-credit removal before any future scoring prototype.
- Support gates cannot stand alone. They can only provide context beside sharper bounded evidence.
- VTRAC/decay lanes stay in carryforward/watch territory and cannot become boxed spend permission.
- Concentration and negative-control pressure become restraint/retest surfaces, not promotion surfaces.
- Old-system source names remain locators; `future_primitive` labels are the architecture-facing vocabulary.

## Prototype Lane Counts

- `support_gate_only`: `77`
- `concentration_retest_or_restraint`: `74`
- `low_denominator_watchlist`: `64`
- `decay_watch_only`: `33`
- `lineage_guarded_boxed_candidate`: `26`
- `clean_boxed_candidate`: `8`

## Shadow Permission Counts

- `shadow_confidence_boost_only`: `77`
- `shadow_restraint_or_retest`: `74`
- `shadow_collect_more_windows`: `64`
- `shadow_decay_watch_only`: `33`
- `shadow_box_candidate_expression_with_dedup`: `26`
- `shadow_box_candidate_expression`: `8`

## Restraint Pressure Counts

- `high`: `199`
- `medium`: `83`

## Lane Separation Matrix

| lane | rules | holdout | avg pos/100 ASD | avg support/100 ASD | pressure mix | guardrail |
|---|---:|---:|---:|---:|---|---|
| `clean_boxed_candidate` | 8 | 0.0% | 3.323 | 3.935 | `medium:7|high:1` | read_only_candidate_expression_no_live_scoring |
| `lineage_guarded_boxed_candidate` | 26 | 0.0% | 4.395 | 4.456 | `medium:15|high:11` | read_only_candidate_expression_requires_lineage_dedup |
| `support_gate_only` | 77 | 0.0% | 2.238 | 6.152 | `high:69|medium:8` | support_gate_never_standalone_candidate |
| `decay_watch_only` | 33 | 0.0% | 17.418 | 37.070 | `high:18|medium:15` | decay_or_vtrac_watch_never_boxed_spend_permission |
| `concentration_retest_or_restraint` | 74 | 0.0% | 2.493 | 2.832 | `high:53|medium:21` | concentration_block_requires_broader_state_retest |
| `low_denominator_watchlist` | 64 | 0.0% | 2.197 | 2.289 | `high:47|medium:17` | insufficient_denominator_collect_more_windows |

## Holdout Mode Summary

- `clean_boxed_only`: holdout `0/0` confirmed (`0.0%`)
- `clean_plus_lineage_deduped`: holdout `0/0` confirmed (`0.0%`)
- `decay_watch_context`: holdout `0/0` confirmed (`0.0%`)
- `low_denominator_watchlist`: holdout `0/0` confirmed (`0.0%`)
- `restraint_retest`: holdout `0/0` confirmed (`0.0%`)
- `support_gate_context`: holdout `0/0` confirmed (`0.0%`)

## Top Candidate-Expression Clusters

| cluster | lane | holdout | pos/100 ASD | support/100 ASD | pressure | permission |
|---|---:|---:|---:|---:|---:|---|
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+translation_sandbox:diagnostic_straight_seed` | `clean_boxed_candidate` | 0.0% | 5.155 | 5.155 | medium | shadow_box_candidate_expression |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::brain1:secondary_canonicals+old_candidate_universe:mirror_pair_closure` | `clean_boxed_candidate` | 0.0% | 5.147 | 5.147 | medium | shadow_box_candidate_expression |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+translation_sandbox:diagnostic_boxed_seed` | `clean_boxed_candidate` | 0.0% | 4.070 | 4.070 | medium | shadow_box_candidate_expression |
| `blackapple_related_boxed_overlap::blackapple_support_gate_or_restraint::blackapple:recommended_canonicals+old_play_card:b36_budget_surface` | `clean_boxed_candidate` | 0.0% | 2.954 | 3.692 | medium | shadow_box_candidate_expression |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+translation_sandbox:diagnostic_boxed_seed` | `clean_boxed_candidate` | 0.0% | 2.841 | 3.409 | medium | shadow_box_candidate_expression |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+shadow_policy:primary_cluster_canonicals` | `clean_boxed_candidate` | 0.0% | 2.410 | 3.012 | high | shadow_box_candidate_expression |
| `blackapple_related_boxed_overlap::blackapple_support_gate_or_restraint::blackapple:recommended_canonicals+old_play_card:b24_budget_surface` | `clean_boxed_candidate` | 0.0% | 2.398 | 2.962 | medium | shadow_box_candidate_expression |
| `blackapple_related_boxed_overlap::blackapple_support_gate_or_restraint::blackapple:recommended_canonicals+brain1:dominant_canonicals` | `clean_boxed_candidate` | 0.0% | 1.613 | 4.032 | medium | shadow_box_candidate_expression |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_candidate_universe:r_perm` | `lineage_guarded_boxed_candidate` | 0.0% | 6.818 | 6.818 | medium | shadow_box_candidate_expression_with_dedup |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:b36_budget_surface` | `lineage_guarded_boxed_candidate` | 0.0% | 5.254 | 5.254 | medium | shadow_box_candidate_expression_with_dedup |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:ranked_candidate_canonical` | `lineage_guarded_boxed_candidate` | 0.0% | 5.128 | 5.128 | medium | shadow_box_candidate_expression_with_dedup |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:ranked_candidate_combo` | `lineage_guarded_boxed_candidate` | 0.0% | 5.128 | 5.128 | medium | shadow_box_candidate_expression_with_dedup |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_candidate_universe:top_canonicals` | `lineage_guarded_boxed_candidate` | 0.0% | 4.965 | 4.965 | medium | shadow_box_candidate_expression_with_dedup |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:b12_budget_surface` | `lineage_guarded_boxed_candidate` | 0.0% | 4.839 | 4.839 | medium | shadow_box_candidate_expression_with_dedup |
| `old_play_card_expression_spine::legacy_budget_expression_locator::old_candidate_universe:aux_vtrac_index_overdue+old_play_card:ranked_candidate_canonical` | `lineage_guarded_boxed_candidate` | 0.0% | 4.839 | 4.839 | high | shadow_box_candidate_expression_with_dedup |
| `old_play_card_expression_spine::legacy_budget_expression_locator::old_candidate_universe:aux_vtrac_index_overdue+old_play_card:ranked_candidate_combo` | `lineage_guarded_boxed_candidate` | 0.0% | 4.839 | 4.839 | high | shadow_box_candidate_expression_with_dedup |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:budgeted_canonicals_top` | `lineage_guarded_boxed_candidate` | 0.0% | 4.721 | 4.721 | medium | shadow_box_candidate_expression_with_dedup |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:ranked_candidate_canonical` | `lineage_guarded_boxed_candidate` | 0.0% | 4.569 | 4.569 | medium | shadow_box_candidate_expression_with_dedup |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:ranked_candidate_combo` | `lineage_guarded_boxed_candidate` | 0.0% | 4.569 | 4.569 | medium | shadow_box_candidate_expression_with_dedup |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:b36_budget_surface` | `lineage_guarded_boxed_candidate` | 0.0% | 4.560 | 4.695 | high | shadow_box_candidate_expression_with_dedup |

## Support / Restraint Read
- support_gate_rows: `77`
- paired_support_context_rows: `57`
- restraint_audit_rows: `231`
- Support context should be treated as a confidence modifier only after a candidate lane already exists.
- High negative-control or concentration pressure should become future penalty/veto/retest material before any promotion discussion.

## Interpretation
- Stage 4C gives us a clean vocabulary for future translator design, not a scoring rewrite.
- The most useful immediate output is lane separation: candidate expression, lineage deduplication, support context, decay watch, restraint, and low-denominator watchlist are now separated instead of blended.
- The next safe engineering step after reviewing Stage 4C is a fixture-backed prototype evaluation harness, still read-only, that checks candidate-expression modes before any live scoring rewrite.

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_SHADOW_TRANSLATOR_PROTOTYPE.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_SHADOW_TRANSLATOR_PROTOTYPE.json`
- rule_registry_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_PROTOTYPE_RULE_REGISTRY.csv`
- lane_matrix_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_LANE_SEPARATION_MATRIX.csv`
- support_effects_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_SUPPORT_GATE_EFFECTS.csv`
- restraint_audit_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_RESTRAINT_APPLICATION_AUDIT.csv`
- holdout_scorecard_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_HOLDOUT_PROTOTYPE_SCORECARD.csv`
- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_TRANSLATOR_PROTOTYPE_CASEBOOK.csv`
- casebook_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4C_TRANSLATOR_PROTOTYPE_CASEBOOK.md`
