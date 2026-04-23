# Analysis Arena Stage 4B Replay Readback

Purpose: turn Stage 4 fixture replay into primitive-level decision intelligence before any scoring or translator rewrite.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix`
- stage4_decision_rows: `1170`
- primitive_clusters: `343`
- holdout_rows: `4680`
- translator_queue_rows: `328`
- negative_control_families: `11`

## Guardrails
- Stage 4B is read-only and cannot change scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.
- Primitive clusters collapse aliases and old-system locator names; they are not live rules.
- Holdout confirmation is a research filter, not live-play permission.
- Support gates, VTRAC/decay rows, concentration-blocked rows, and negative controls must stay in their lanes.

## Stage 4 Decision Baseline

- `blocked_by_state_concentration`: `369`
- `survived_as_support_gate`: `363`
- `low_denominator_watchlist`: `172`
- `fixture_only_low_denominator`: `123`
- `survived_with_lineage_guardrail`: `71`
- `watch_decay_only`: `40`
- `diagnostic_fixture_only`: `21`
- `survived_as_boxed_translator_candidate`: `9`
- `needs_replay_refinement`: `2`

## Primitive Cluster Uses

- `support_gate_cluster`: `124`
- `state_concentration_retest_or_restraint`: `91`
- `low_denominator_watchlist`: `57`
- `decay_or_vtrac_watch_cluster`: `33`
- `translator_candidate_with_duplicate_credit_guardrail`: `18`
- `diagnostic_fixture_cluster`: `14`
- `translator_candidate_cluster`: `5`
- `fixture_only_cluster`: `1`

## Leave-One-Window-Out Outcomes

- `holdout_confirmed`: `2795`
- `train_did_not_survive`: `1029`
- `holdout_missed`: `854`
- `no_holdout_denominator`: `2`

## Translator Queue Next Actions

- `prototype_as_gate_not_standalone`: `124`
- `retest_by_state_and_consider_penalty`: `91`
- `collect_more_windows_before_promotion`: `57`
- `keep_in_decay_watch_not_boxed_spend`: `33`
- `prototype_with_lineage_deduplication`: `18`
- `prototype_as_read_only_boxed_translator_rule`: `5`

## Top Translator Candidate Clusters

| cluster | use | holdout confirm | pos/100 ASD | support/100 ASD | representative |
|---|---:|---:|---:|---:|---|
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::brain1:dominant_canonicals+old_candidate_universe:mirror_pair_closure` | translator_candidate_cluster | 100.0% | 0.505 | 3.030 | `box_overlap::brain1:dominant_canonicals + old_candidate_universe:pack:mirror_pair_closure` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::brain1:secondary_canonicals+old_candidate_universe:mirror_pair_closure` | translator_candidate_cluster | 75.0% | 1.322 | 4.405 | `box_overlap::brain1:secondary_canonicals + old_candidate_universe:pack:mirror_pair_closure` |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::board_scoreboard:top_canonicals+old_candidate_universe:vtrac_enhanced_top` | translator_candidate_cluster | 75.0% | 0.976 | 2.927 | `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b12_budget_surface+positional:positional_canonical` | translator_candidate_cluster | 60.8% | 1.139 | 2.308 | `box_overlap::old_play_card:strategy:analysis_prefix:B12:combos + positional:positional_canonical` |
| `positional_spine::bounded_positional_box_overlap::old_play_card:b12_budget_surface+positional:positional_combo` | translator_candidate_cluster | 60.8% | 1.139 | 2.308 | `box_overlap::old_play_card:strategy:analysis_prefix:B12:combos + positional:positional_combo` |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:budgeted_canonicals_top` | translator_candidate_with_duplicate_credit_guardrail | 100.0% | 1.577 | 3.155 | `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:budgeted_canonicals_top` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:b36_budget_surface` | translator_candidate_with_duplicate_credit_guardrail | 95.5% | 1.583 | 3.970 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:v0_2_default:B36:combos` |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:b36_budget_surface` | translator_candidate_with_duplicate_credit_guardrail | 85.7% | 1.193 | 2.785 | `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:b24_budget_surface` | translator_candidate_with_duplicate_credit_guardrail | 83.3% | 1.441 | 3.576 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B24:combos` |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:b24_budget_surface` | translator_candidate_with_duplicate_credit_guardrail | 82.5% | 1.178 | 2.785 | `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:analysis_prefix:B24:boxed_canonicals` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_candidate_universe:top_canonicals` | translator_candidate_with_duplicate_credit_guardrail | 75.0% | 1.866 | 3.358 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:top_canonicals` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_candidate_universe:r_perm` | translator_candidate_with_duplicate_credit_guardrail | 75.0% | 1.630 | 3.261 | `box_overlap::old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack:mirror_pair_closure` |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:budgeted_canonicals_top` | translator_candidate_with_duplicate_credit_guardrail | 75.0% | 1.146 | 3.438 | `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:budgeted_canonicals_top` |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:ranked_candidate_canonical` | translator_candidate_with_duplicate_credit_guardrail | 75.0% | 0.873 | 2.620 | `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:ranked_candidate_canonical` |
| `r_perm_spine::bounded_r_perm_box_overlap::old_candidate_universe:r_perm+old_play_card:ranked_candidate_combo` | translator_candidate_with_duplicate_credit_guardrail | 75.0% | 0.873 | 2.620 | `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:ranked_candidate_combo` |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:ranked_candidate_canonical` | translator_candidate_with_duplicate_credit_guardrail | 75.0% | 0.717 | 2.867 | `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:ranked_candidate_canonical` |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:ranked_candidate_combo` | translator_candidate_with_duplicate_credit_guardrail | 75.0% | 0.717 | 2.867 | `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:ranked_candidate_combo` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_candidate_universe:vtrac_enhanced_top` | translator_candidate_with_duplicate_credit_guardrail | 75.0% | 0.510 | 4.082 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` |
| `mirror_pair_closure_spine::bounded_mirror_pair_box_overlap::old_candidate_universe:mirror_pair_closure+old_play_card:b12_budget_surface` | translator_candidate_with_duplicate_credit_guardrail | 70.8% | 1.073 | 2.993 | `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B12:boxed_canonicals` |
| `vtrac_enhanced_secondary_spine::bounded_vtrac_enhanced_box_overlap::old_candidate_universe:vtrac_enhanced_top+old_play_card:b36_budget_surface` | translator_candidate_with_duplicate_credit_guardrail | 70.0% | 1.019 | 3.111 | `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` |

## Interpretation
- The cleanest future translator material is the cluster set marked `translator_candidate_cluster`.
- `translator_candidate_with_duplicate_credit_guardrail` is valuable but must be de-duplicated before any scoring prototype.
- `support_gate_cluster` should help later ranking/translator confidence only when paired with sharper bounded evidence.
- `state_concentration_retest_or_restraint` rows are warning signs until broader state confirmation appears.
- Negative-control families remain restraint/penalty/veto assets.

## Output Files

- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4B_REPLAY_READBACK.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4B_REPLAY_READBACK.json`
- cluster_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4B_PRIMITIVE_CLUSTER_REGISTRY.csv`
- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4B_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.csv`
- casebook_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4B_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.md`
- holdout_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4B_LEAVE_ONE_WINDOW_OUT_MATRIX.csv`
- translator_queue_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE4B_TRANSLATOR_DESIGN_QUEUE.csv`
