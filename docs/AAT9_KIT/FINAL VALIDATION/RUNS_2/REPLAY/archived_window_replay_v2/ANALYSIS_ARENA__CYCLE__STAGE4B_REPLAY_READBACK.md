# Analysis Arena Stage 4B Replay Readback

Purpose: turn Stage 4 fixture replay into primitive-level decision intelligence before any scoring or translator rewrite.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2`
- stage4_decision_rows: `1097`
- primitive_clusters: `294`
- holdout_rows: `3291`
- translator_queue_rows: `282`
- negative_control_families: `11`

## Guardrails
- Stage 4B is read-only and cannot change scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.
- Primitive clusters collapse aliases and old-system locator names; they are not live rules.
- Holdout confirmation is a research filter, not live-play permission.
- Support gates, VTRAC/decay rows, concentration-blocked rows, and negative controls must stay in their lanes.

## Stage 4 Decision Baseline

- `survived_as_support_gate`: `386`
- `low_denominator_watchlist`: `269`
- `blocked_by_state_concentration`: `230`
- `survived_with_lineage_guardrail`: `118`
- `watch_decay_only`: `40`
- `fixture_only_low_denominator`: `24`
- `diagnostic_fixture_only`: `14`
- `survived_as_boxed_translator_candidate`: `14`
- `demote_to_restraint`: `2`

## Primitive Cluster Uses

- `support_gate_cluster`: `77`
- `state_concentration_retest_or_restraint`: `74`
- `low_denominator_watchlist`: `64`
- `decay_or_vtrac_watch_cluster`: `33`
- `translator_candidate_with_duplicate_credit_guardrail`: `26`
- `diagnostic_fixture_cluster`: `12`
- `translator_candidate_cluster`: `8`

## Leave-One-Window-Out Outcomes

- `train_did_not_survive`: `3291`

## Translator Queue Next Actions

- `prototype_as_gate_not_standalone`: `77`
- `retest_by_state_and_consider_penalty`: `74`
- `collect_more_windows_before_promotion`: `64`
- `keep_in_decay_watch_not_boxed_spend`: `33`
- `prototype_with_lineage_deduplication`: `26`
- `prototype_as_read_only_boxed_translator_rule`: `8`

## Top Translator Candidate Clusters

| cluster | use | holdout confirm | pos/100 ASD | support/100 ASD | representative |
|---|---:|---:|---:|---:|---|
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+translation_sandbox:diagnostic_straight_seed` | translator_candidate_cluster | 0.0% | 5.155 | 5.155 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + translation_sandbox:diagnostic_straight_seed` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::brain1:secondary_canonicals+old_candidate_universe:mirror_pair_closure` | translator_candidate_cluster | 0.0% | 5.147 | 5.147 | `box_overlap::brain1:secondary_canonicals + old_candidate_universe:pack:mirror_pair_closure` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+translation_sandbox:diagnostic_boxed_seed` | translator_candidate_cluster | 0.0% | 4.070 | 4.070 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + translation_sandbox:diagnostic_boxed_seed` |
| `blackapple_related_boxed_overlap::blackapple_support_gate_or_restraint::blackapple:recommended_canonicals+old_play_card:b36_budget_surface` | translator_candidate_cluster | 0.0% | 2.954 | 3.692 | `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+translation_sandbox:diagnostic_boxed_seed` | translator_candidate_cluster | 0.0% | 2.841 | 3.409 | `box_overlap::old_candidate_universe:pack:R-perm-4 + translation_sandbox:diagnostic_boxed_seed` |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+shadow_policy:primary_cluster_canonicals` | translator_candidate_cluster | 0.0% | 2.410 | 3.012 | `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + shadow_policy:primary_cluster_canonicals` |
| `blackapple_related_boxed_overlap::blackapple_support_gate_or_restraint::blackapple:recommended_canonicals+old_play_card:b24_budget_surface` | translator_candidate_cluster | 0.0% | 2.398 | 2.962 | `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` |
| `blackapple_related_boxed_overlap::blackapple_support_gate_or_restraint::blackapple:recommended_canonicals+brain1:dominant_canonicals` | translator_candidate_cluster | 0.0% | 1.613 | 4.032 | `box_overlap::blackapple:recommended_canonicals + brain1:dominant_canonicals` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_candidate_universe:r_perm` | translator_candidate_with_duplicate_credit_guardrail | 0.0% | 6.818 | 6.818 | `box_overlap::old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack:mirror_pair_closure` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:b36_budget_surface` | translator_candidate_with_duplicate_credit_guardrail | 0.0% | 5.254 | 5.254 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B36:combos` |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:ranked_candidate_canonical` | translator_candidate_with_duplicate_credit_guardrail | 0.0% | 5.128 | 5.128 | `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:ranked_candidate_canonical` |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:ranked_candidate_combo` | translator_candidate_with_duplicate_credit_guardrail | 0.0% | 5.128 | 5.128 | `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:ranked_candidate_combo` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_candidate_universe:top_canonicals` | translator_candidate_with_duplicate_credit_guardrail | 0.0% | 4.965 | 4.965 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:top_canonicals` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:b12_budget_surface` | translator_candidate_with_duplicate_credit_guardrail | 0.0% | 4.839 | 4.839 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B12:boxed_canonicals` |
| `old_play_card_expression_spine::legacy_budget_expression_locator::old_candidate_universe:aux_vtrac_index_overdue+old_play_card:ranked_candidate_canonical` | translator_candidate_with_duplicate_credit_guardrail | 0.0% | 4.839 | 4.839 | `box_overlap::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:ranked_candidate_canonical` |
| `old_play_card_expression_spine::legacy_budget_expression_locator::old_candidate_universe:aux_vtrac_index_overdue+old_play_card:ranked_candidate_combo` | translator_candidate_with_duplicate_credit_guardrail | 0.0% | 4.839 | 4.839 | `box_overlap::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:ranked_candidate_combo` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:budgeted_canonicals_top` | translator_candidate_with_duplicate_credit_guardrail | 0.0% | 4.721 | 4.721 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:budgeted_canonicals_top` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:ranked_candidate_canonical` | translator_candidate_with_duplicate_credit_guardrail | 0.0% | 4.569 | 4.569 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:ranked_candidate_canonical` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:ranked_candidate_combo` | translator_candidate_with_duplicate_credit_guardrail | 0.0% | 4.569 | 4.569 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:ranked_candidate_combo` |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:b36_budget_surface` | translator_candidate_with_duplicate_credit_guardrail | 0.0% | 4.560 | 4.695 | `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B36:boxed_canonicals` |

## Interpretation
- The cleanest future translator material is the cluster set marked `translator_candidate_cluster`.
- `translator_candidate_with_duplicate_credit_guardrail` is valuable but must be de-duplicated before any scoring prototype.
- `support_gate_cluster` should help later ranking/translator confidence only when paired with sharper bounded evidence.
- `state_concentration_retest_or_restraint` rows are warning signs until broader state confirmation appears.
- Negative-control families remain restraint/penalty/veto assets.

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_REPLAY_READBACK.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_REPLAY_READBACK.json`
- cluster_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_PRIMITIVE_CLUSTER_REGISTRY.csv`
- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.csv`
- casebook_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.md`
- holdout_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_LEAVE_ONE_WINDOW_OUT_MATRIX.csv`
- translator_queue_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE4B_TRANSLATOR_DESIGN_QUEUE.csv`
