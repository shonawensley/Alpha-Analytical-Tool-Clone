# Analysis Arena Stage 4C Shadow Translator Prototype

Purpose: convert Stage 4B primitive clusters into a read-only shadow translator design package with strict lane separation.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- prototype_rule_rows: `328`
- lane_matrix_rows: `6`
- support_gate_effect_rows: `124`
- restraint_audit_rows: `327`
- holdout_scorecard_rows: `24`
- casebook_rows: `85`

## Non-Negotiable Guardrails
- Stage 4C is read-only and cannot change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.
- Clean candidate lanes are aggregate shadow expressions only; they are not deployable candidate lists.
- Lineage-guarded lanes require duplicate-credit removal before any future scoring prototype.
- Support gates cannot stand alone. They can only provide context beside sharper bounded evidence.
- VTRAC/decay lanes stay in carryforward/watch territory and cannot become boxed spend permission.
- Concentration and negative-control pressure become restraint/retest surfaces, not promotion surfaces.
- Old-system source names remain locators; `future_primitive` labels are the architecture-facing vocabulary.

## Prototype Lane Counts

- `support_gate_only`: `124`
- `concentration_retest_or_restraint`: `91`
- `low_denominator_watchlist`: `57`
- `decay_watch_only`: `33`
- `lineage_guarded_boxed_candidate`: `18`
- `clean_boxed_candidate`: `5`

## Shadow Permission Counts

- `shadow_confidence_boost_only`: `124`
- `shadow_restraint_or_retest`: `91`
- `shadow_collect_more_windows`: `57`
- `shadow_decay_watch_only`: `33`
- `shadow_box_candidate_expression_with_dedup`: `18`
- `shadow_box_candidate_expression`: `5`

## Restraint Pressure Counts

- `high`: `308`
- `medium`: `20`

## Lane Separation Matrix

| lane | rules | holdout | avg pos/100 ASD | avg support/100 ASD | pressure mix | guardrail |
|---|---:|---:|---:|---:|---|---|
| `clean_boxed_candidate` | 5 | 64.8% | 1.016 | 2.996 | `high:5` | read_only_candidate_expression_no_live_scoring |
| `lineage_guarded_boxed_candidate` | 18 | 77.9% | 1.131 | 3.040 | `high:12|medium:6` | read_only_candidate_expression_requires_lineage_dedup |
| `support_gate_only` | 124 | 79.6% | 0.895 | 4.954 | `high:119|medium:5` | support_gate_never_standalone_candidate |
| `decay_watch_only` | 33 | 100.0% | 7.351 | 36.895 | `high:33` | decay_or_vtrac_watch_never_boxed_spend_permission |
| `concentration_retest_or_restraint` | 91 | 66.6% | 0.844 | 2.396 | `high:83|medium:8` | concentration_block_requires_broader_state_retest |
| `low_denominator_watchlist` | 57 | 50.7% | 0.590 | 1.572 | `high:56|medium:1` | insufficient_denominator_collect_more_windows |

## Holdout Mode Summary

- `clean_boxed_only`: holdout `79/122` confirmed (`64.8%`)
- `clean_plus_lineage_deduped`: holdout `587/774` confirmed (`75.8%`)
- `decay_watch_context`: holdout `160/160` confirmed (`100.0%`)
- `low_denominator_watchlist`: holdout `70/138` confirmed (`50.7%`)
- `restraint_retest`: holdout `438/658` confirmed (`66.6%`)
- `support_gate_context`: holdout `1479/1857` confirmed (`79.6%`)

## Top Candidate-Expression Clusters

| cluster | lane | holdout | pos/100 ASD | support/100 ASD | pressure | permission |
|---|---:|---:|---:|---:|---:|---|
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::brain1:dominant_canonicals+old_candidate_universe:mirror_pair_closure` | `clean_boxed_candidate` | 100.0% | 0.505 | 3.030 | high | shadow_box_candidate_expression |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::brain1:secondary_canonicals+old_candidate_universe:mirror_pair_closure` | `clean_boxed_candidate` | 75.0% | 1.322 | 4.405 | high | shadow_box_candidate_expression |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::board_scoreboard:top_canonicals+old_candidate_universe:vtrac_enhanced_top` | `clean_boxed_candidate` | 75.0% | 0.976 | 2.927 | high | shadow_box_candidate_expression |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b12_budget_surface+positional:positional_canonical` | `clean_boxed_candidate` | 60.8% | 1.139 | 2.308 | high | shadow_box_candidate_expression |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b12_budget_surface+positional:positional_combo` | `clean_boxed_candidate` | 60.8% | 1.139 | 2.308 | high | shadow_box_candidate_expression |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:budgeted_canonicals_top` | `lineage_guarded_boxed_candidate` | 100.0% | 1.577 | 3.155 | medium | shadow_box_candidate_expression_with_dedup |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:b36_budget_surface` | `lineage_guarded_boxed_candidate` | 95.5% | 1.583 | 3.970 | high | shadow_box_candidate_expression_with_dedup |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:b36_budget_surface` | `lineage_guarded_boxed_candidate` | 85.7% | 1.193 | 2.785 | medium | shadow_box_candidate_expression_with_dedup |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:b24_budget_surface` | `lineage_guarded_boxed_candidate` | 83.3% | 1.441 | 3.576 | high | shadow_box_candidate_expression_with_dedup |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:b24_budget_surface` | `lineage_guarded_boxed_candidate` | 82.5% | 1.178 | 2.785 | medium | shadow_box_candidate_expression_with_dedup |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_candidate_universe:top_canonicals` | `lineage_guarded_boxed_candidate` | 75.0% | 1.866 | 3.358 | high | shadow_box_candidate_expression_with_dedup |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_candidate_universe:r_perm` | `lineage_guarded_boxed_candidate` | 75.0% | 1.630 | 3.261 | high | shadow_box_candidate_expression_with_dedup |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:budgeted_canonicals_top` | `lineage_guarded_boxed_candidate` | 75.0% | 1.146 | 3.438 | high | shadow_box_candidate_expression_with_dedup |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:ranked_candidate_canonical` | `lineage_guarded_boxed_candidate` | 75.0% | 0.873 | 2.620 | medium | shadow_box_candidate_expression_with_dedup |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:ranked_candidate_combo` | `lineage_guarded_boxed_candidate` | 75.0% | 0.873 | 2.620 | medium | shadow_box_candidate_expression_with_dedup |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:ranked_candidate_canonical` | `lineage_guarded_boxed_candidate` | 75.0% | 0.717 | 2.867 | high | shadow_box_candidate_expression_with_dedup |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:ranked_candidate_combo` | `lineage_guarded_boxed_candidate` | 75.0% | 0.717 | 2.867 | high | shadow_box_candidate_expression_with_dedup |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_candidate_universe:vtrac_enhanced_top` | `lineage_guarded_boxed_candidate` | 75.0% | 0.510 | 4.082 | high | shadow_box_candidate_expression_with_dedup |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:b12_budget_surface` | `lineage_guarded_boxed_candidate` | 70.8% | 1.073 | 2.993 | high | shadow_box_candidate_expression_with_dedup |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:b36_budget_surface` | `lineage_guarded_boxed_candidate` | 70.0% | 1.019 | 3.111 | high | shadow_box_candidate_expression_with_dedup |

## Support / Restraint Read
- support_gate_rows: `124`
- paired_support_context_rows: `53`
- restraint_audit_rows: `327`
- Support context should be treated as a confidence modifier only after a candidate lane already exists.
- High negative-control or concentration pressure should become future penalty/veto/retest material before any promotion discussion.

## Interpretation
- Stage 4C gives us a clean vocabulary for future translator design, not a scoring rewrite.
- The most useful immediate output is lane separation: candidate expression, lineage deduplication, support context, decay watch, restraint, and low-denominator watchlist are now separated instead of blended.
- The next safe engineering step after reviewing Stage 4C is a fixture-backed prototype evaluation harness, still read-only, that checks candidate-expression modes before any live scoring rewrite.

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_SHADOW_TRANSLATOR_PROTOTYPE.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_SHADOW_TRANSLATOR_PROTOTYPE.json`
- rule_registry_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_PROTOTYPE_RULE_REGISTRY.csv`
- lane_matrix_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_LANE_SEPARATION_MATRIX.csv`
- support_effects_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_SUPPORT_GATE_EFFECTS.csv`
- restraint_audit_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_RESTRAINT_APPLICATION_AUDIT.csv`
- holdout_scorecard_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_HOLDOUT_PROTOTYPE_SCORECARD.csv`
- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_TRANSLATOR_PROTOTYPE_CASEBOOK.csv`
- casebook_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4C_TRANSLATOR_PROTOTYPE_CASEBOOK.md`
