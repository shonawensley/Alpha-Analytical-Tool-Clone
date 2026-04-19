# Analysis Arena Stage 4C Shadow Translator Prototype

Purpose: convert Stage 4B primitive clusters into a read-only shadow translator design package with strict lane separation.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- prototype_rule_rows: `314`
- lane_matrix_rows: `6`
- support_gate_effect_rows: `144`
- restraint_audit_rows: `261`
- holdout_scorecard_rows: `30`
- casebook_rows: `96`

## Non-Negotiable Guardrails
- Stage 4C is read-only and cannot change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.
- Clean candidate lanes are aggregate shadow expressions only; they are not deployable candidate lists.
- Lineage-guarded lanes require duplicate-credit removal before any future scoring prototype.
- Support gates cannot stand alone. They can only provide context beside sharper bounded evidence.
- VTRAC/decay lanes stay in carryforward/watch territory and cannot become boxed spend permission.
- Concentration and negative-control pressure become restraint/retest surfaces, not promotion surfaces.
- Old-system source names remain locators; `future_primitive` labels are the architecture-facing vocabulary.

## Prototype Lane Counts

- `support_gate_only`: `144`
- `concentration_retest_or_restraint`: `61`
- `decay_watch_only`: `34`
- `low_denominator_watchlist`: `29`
- `lineage_guarded_boxed_candidate`: `28`
- `clean_boxed_candidate`: `18`

## Shadow Permission Counts

- `shadow_confidence_boost_only`: `144`
- `shadow_restraint_or_retest`: `61`
- `shadow_decay_watch_only`: `34`
- `shadow_collect_more_windows`: `29`
- `shadow_box_candidate_expression_with_dedup`: `28`
- `shadow_box_candidate_expression`: `18`

## Restraint Pressure Counts

- `high`: `236`
- `medium`: `78`

## Lane Separation Matrix

| lane | rules | holdout | avg pos/100 ASD | avg support/100 ASD | pressure mix | guardrail |
|---|---:|---:|---:|---:|---|---|
| `clean_boxed_candidate` | 18 | 77.1% | 0.979 | 3.471 | `medium:9|high:9` | read_only_candidate_expression_no_live_scoring |
| `lineage_guarded_boxed_candidate` | 28 | 78.5% | 1.117 | 3.687 | `medium:24|high:4` | read_only_candidate_expression_requires_lineage_dedup |
| `support_gate_only` | 144 | 85.6% | 0.763 | 4.903 | `high:121|medium:23` | support_gate_never_standalone_candidate |
| `decay_watch_only` | 34 | 100.0% | 6.629 | 36.857 | `high:34` | decay_or_vtrac_watch_never_boxed_spend_permission |
| `concentration_retest_or_restraint` | 61 | 45.2% | 0.651 | 2.559 | `high:47|medium:14` | concentration_block_requires_broader_state_retest |
| `low_denominator_watchlist` | 29 | 50.4% | 0.719 | 2.129 | `high:21|medium:8` | insufficient_denominator_collect_more_windows |

## Holdout Mode Summary

- `clean_boxed_only`: holdout `346/449` confirmed (`77.1%`)
- `clean_plus_lineage_deduped`: holdout `1304/1669` confirmed (`78.1%`)
- `decay_watch_context`: holdout `200/200` confirmed (`100.0%`)
- `low_denominator_watchlist`: holdout `64/127` confirmed (`50.4%`)
- `restraint_retest`: holdout `168/372` confirmed (`45.2%`)
- `support_gate_context`: holdout `2012/2350` confirmed (`85.6%`)

## Top Candidate-Expression Clusters

| cluster | lane | holdout | pos/100 ASD | support/100 ASD | pressure | permission |
|---|---:|---:|---:|---:|---:|---|
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+translation_sandbox:diagnostic_straight_seed` | `clean_boxed_candidate` | 100.0% | 1.392 | 4.872 | medium | shadow_box_candidate_expression |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::brain1:dominant_canonicals+old_candidate_universe:mirror_pair_closure` | `clean_boxed_candidate` | 100.0% | 0.450 | 3.604 | medium | shadow_box_candidate_expression |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::brain1:secondary_canonicals+old_candidate_universe:aux_positional` | `clean_boxed_candidate` | 80.0% | 1.316 | 3.070 | medium | shadow_box_candidate_expression |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b36_budget_surface+positional:positional_canonical` | `clean_boxed_candidate` | 80.0% | 1.168 | 3.631 | high | shadow_box_candidate_expression |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b36_budget_surface+positional:positional_combo` | `clean_boxed_candidate` | 80.0% | 1.168 | 3.631 | high | shadow_box_candidate_expression |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::brain1:secondary_canonicals+old_candidate_universe:mirror_pair_closure` | `clean_boxed_candidate` | 80.0% | 1.136 | 5.303 | medium | shadow_box_candidate_expression |
| `profit_alert_related_boxed_overlap::tracker_boxed_support_gate::positional:positional_canonical+profit_alerts:implied_canonicals` | `clean_boxed_candidate` | 80.0% | 1.124 | 2.809 | high | shadow_box_candidate_expression |
| `profit_alert_related_boxed_overlap::tracker_boxed_support_gate::positional:positional_combo+profit_alerts:implied_canonicals` | `clean_boxed_candidate` | 80.0% | 1.124 | 2.809 | high | shadow_box_candidate_expression |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::brain1:dominant_canonicals+old_candidate_universe:vtrac_enhanced_top` | `clean_boxed_candidate` | 80.0% | 0.885 | 4.204 | medium | shadow_box_candidate_expression |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+shadow_policy:primary_cluster_canonicals` | `clean_boxed_candidate` | 80.0% | 0.885 | 3.835 | medium | shadow_box_candidate_expression |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::board_scoreboard:top_canonicals+old_candidate_universe:vtrac_enhanced_top` | `clean_boxed_candidate` | 80.0% | 0.862 | 3.448 | medium | shadow_box_candidate_expression |
| `blackapple_related_boxed_overlap::blackapple_support_gate_or_restraint::blackapple:recommended_canonicals+old_candidate_universe:mirror_pair_closure` | `clean_boxed_candidate` | 80.0% | 0.840 | 2.941 | high | shadow_box_candidate_expression |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+translation_sandbox:diagnostic_straight_seed` | `clean_boxed_candidate` | 80.0% | 0.604 | 3.021 | medium | shadow_box_candidate_expression |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+shadow_policy:primary_cluster_context` | `clean_boxed_candidate` | 80.0% | 0.595 | 2.976 | medium | shadow_box_candidate_expression |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b24_budget_surface+positional:positional_canonical` | `clean_boxed_candidate` | 76.7% | 1.030 | 3.323 | high | shadow_box_candidate_expression |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b24_budget_surface+positional:positional_combo` | `clean_boxed_candidate` | 76.7% | 1.030 | 3.323 | high | shadow_box_candidate_expression |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b12_budget_surface+positional:positional_canonical` | `clean_boxed_candidate` | 70.1% | 1.005 | 2.835 | high | shadow_box_candidate_expression |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b12_budget_surface+positional:positional_combo` | `clean_boxed_candidate` | 70.1% | 1.005 | 2.835 | high | shadow_box_candidate_expression |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:budgeted_canonicals_top` | `lineage_guarded_boxed_candidate` | 100.0% | 1.587 | 5.357 | medium | shadow_box_candidate_expression_with_dedup |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:budgeted_canonicals_top` | `lineage_guarded_boxed_candidate` | 100.0% | 1.420 | 3.125 | medium | shadow_box_candidate_expression_with_dedup |

## Support / Restraint Read
- support_gate_rows: `144`
- paired_support_context_rows: `78`
- restraint_audit_rows: `261`
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
