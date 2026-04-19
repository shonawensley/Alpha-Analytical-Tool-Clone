# Analysis Arena Stage 4B Replay Readback

Purpose: turn Stage 4 fixture replay into primitive-level decision intelligence before any scoring or translator rewrite.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- stage4_decision_rows: `1135`
- primitive_clusters: `335`
- holdout_rows: `5675`
- translator_queue_rows: `314`
- negative_control_families: `11`

## Guardrails
- Stage 4B is read-only and cannot change scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.
- Primitive clusters collapse aliases and old-system locator names; they are not live rules.
- Holdout confirmation is a research filter, not live-play permission.
- Support gates, VTRAC/decay rows, concentration-blocked rows, and negative controls must stay in their lanes.

## Stage 4 Decision Baseline

- `survived_as_support_gate`: `508`
- `blocked_by_state_concentration`: `217`
- `survived_with_lineage_guardrail`: `127`
- `low_denominator_watchlist`: `118`
- `diagnostic_fixture_only`: `58`
- `watch_decay_only`: `40`
- `fixture_only_low_denominator`: `33`
- `survived_as_boxed_translator_candidate`: `32`
- `needs_replay_refinement`: `2`

## Primitive Cluster Uses

- `support_gate_cluster`: `144`
- `state_concentration_retest_or_restraint`: `61`
- `decay_or_vtrac_watch_cluster`: `34`
- `low_denominator_watchlist`: `29`
- `translator_candidate_with_duplicate_credit_guardrail`: `28`
- `diagnostic_fixture_cluster`: `20`
- `translator_candidate_cluster`: `18`
- `fixture_only_cluster`: `1`

## Leave-One-Window-Out Outcomes

- `holdout_confirmed`: `3846`
- `holdout_missed`: `984`
- `train_did_not_survive`: `843`
- `no_holdout_denominator`: `2`

## Translator Queue Next Actions

- `prototype_as_gate_not_standalone`: `144`
- `retest_by_state_and_consider_penalty`: `61`
- `keep_in_decay_watch_not_boxed_spend`: `34`
- `collect_more_windows_before_promotion`: `29`
- `prototype_with_lineage_deduplication`: `28`
- `prototype_as_read_only_boxed_translator_rule`: `18`

## Top Translator Candidate Clusters

| cluster | use | holdout confirm | pos/100 ASD | support/100 ASD | representative |
|---|---:|---:|---:|---:|---|
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+translation_sandbox:diagnostic_straight_seed` | translator_candidate_cluster | 100.0% | 1.392 | 4.872 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + translation_sandbox:diagnostic_straight_seed` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::brain1:dominant_canonicals+old_candidate_universe:mirror_pair_closure` | translator_candidate_cluster | 100.0% | 0.450 | 3.604 | `box_overlap::brain1:dominant_canonicals + old_candidate_universe:pack:mirror_pair_closure` |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::brain1:secondary_canonicals+old_candidate_universe:aux_positional` | translator_candidate_cluster | 80.0% | 1.316 | 3.070 | `box_overlap::brain1:secondary_canonicals + old_candidate_universe:pack:aux_positional` |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b36_budget_surface+positional:positional_canonical` | translator_candidate_cluster | 80.0% | 1.168 | 3.631 | `box_overlap::old_play_card:strategy_card:convergence_box_first:B36 + positional:positional_canonical` |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b36_budget_surface+positional:positional_combo` | translator_candidate_cluster | 80.0% | 1.168 | 3.631 | `box_overlap::old_play_card:strategy_card:convergence_box_first:B36 + positional:positional_combo` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::brain1:secondary_canonicals+old_candidate_universe:mirror_pair_closure` | translator_candidate_cluster | 80.0% | 1.136 | 5.303 | `box_overlap::brain1:secondary_canonicals + old_candidate_universe:pack:mirror_pair_closure` |
| `profit_alert_related_boxed_overlap::tracker_boxed_support_gate::positional:positional_canonical+profit_alerts:implied_canonicals` | translator_candidate_cluster | 80.0% | 1.124 | 2.809 | `box_overlap::positional:positional_canonical + profit_alerts:implied_canonicals` |
| `profit_alert_related_boxed_overlap::tracker_boxed_support_gate::positional:positional_combo+profit_alerts:implied_canonicals` | translator_candidate_cluster | 80.0% | 1.124 | 2.809 | `box_overlap::positional:positional_combo + profit_alerts:implied_canonicals` |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::brain1:dominant_canonicals+old_candidate_universe:vtrac_enhanced_top` | translator_candidate_cluster | 80.0% | 0.885 | 4.204 | `box_overlap::brain1:dominant_canonicals + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+shadow_policy:primary_cluster_canonicals` | translator_candidate_cluster | 80.0% | 0.885 | 3.835 | `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + shadow_policy:primary_cluster_canonicals` |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::board_scoreboard:top_canonicals+old_candidate_universe:vtrac_enhanced_top` | translator_candidate_cluster | 80.0% | 0.862 | 3.448 | `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` |
| `blackapple_related_boxed_overlap::blackapple_support_gate_or_restraint::blackapple:recommended_canonicals+old_candidate_universe:mirror_pair_closure` | translator_candidate_cluster | 80.0% | 0.840 | 2.941 | `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack:mirror_pair_closure` |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+translation_sandbox:diagnostic_straight_seed` | translator_candidate_cluster | 80.0% | 0.604 | 3.021 | `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + translation_sandbox:diagnostic_straight_seed` |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+shadow_policy:primary_cluster_context` | translator_candidate_cluster | 80.0% | 0.595 | 2.976 | `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + shadow_policy:primary_cluster_context` |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b24_budget_surface+positional:positional_canonical` | translator_candidate_cluster | 76.7% | 1.030 | 3.323 | `box_overlap::old_play_card:strategy:analysis_prefix:B24:boxed_canonicals + positional:positional_canonical` |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b24_budget_surface+positional:positional_combo` | translator_candidate_cluster | 76.7% | 1.030 | 3.323 | `box_overlap::old_play_card:strategy:analysis_prefix:B24:boxed_canonicals + positional:positional_combo` |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b12_budget_surface+positional:positional_canonical` | translator_candidate_cluster | 70.1% | 1.005 | 2.835 | `box_overlap::old_play_card:strategy:analysis_prefix:B12:boxed_canonicals + positional:positional_canonical` |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b12_budget_surface+positional:positional_combo` | translator_candidate_cluster | 70.1% | 1.005 | 2.835 | `box_overlap::old_play_card:strategy:analysis_prefix:B12:boxed_canonicals + positional:positional_combo` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:budgeted_canonicals_top` | translator_candidate_with_duplicate_credit_guardrail | 100.0% | 1.587 | 5.357 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:budgeted_canonicals_top` |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:budgeted_canonicals_top` | translator_candidate_with_duplicate_credit_guardrail | 100.0% | 1.420 | 3.125 | `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:budgeted_canonicals_top` |

## Interpretation
- The cleanest future translator material is the cluster set marked `translator_candidate_cluster`.
- `translator_candidate_with_duplicate_credit_guardrail` is valuable but must be de-duplicated before any scoring prototype.
- `support_gate_cluster` should help later ranking/translator confidence only when paired with sharper bounded evidence.
- `state_concentration_retest_or_restraint` rows are warning signs until broader state confirmation appears.
- Negative-control families remain restraint/penalty/veto assets.

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_REPLAY_READBACK.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_REPLAY_READBACK.json`
- cluster_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_PRIMITIVE_CLUSTER_REGISTRY.csv`
- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.csv`
- casebook_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.md`
- holdout_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_LEAVE_ONE_WINDOW_OUT_MATRIX.csv`
- translator_queue_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE4B_TRANSLATOR_DESIGN_QUEUE.csv`
