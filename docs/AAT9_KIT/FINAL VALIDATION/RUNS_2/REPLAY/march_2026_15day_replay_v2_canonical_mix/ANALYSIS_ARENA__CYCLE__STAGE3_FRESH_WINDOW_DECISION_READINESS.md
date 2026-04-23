# Stage 3 Fresh-Window Decision Readiness

Purpose: lock how Stage-3 evidence should be used before the next fresh window.

## Permission Model

- Approved now: observation, replay, casebook review, decay/watch interpretation, negative-control restraint.
- Blocked now: live scoring changes, live budget changes, automatic candidate promotion.
- Required before scoring rewrite: replay candidates must survive cross-window fixture replay with denominator controls.

## Decision Mix

- `negative_control`: `2417`
- `watch_decay_only`: `601`
- `supporting_gate`: `584`
- `blocked_low_denominator`: `441`
- `needs_more_windows`: `97`
- `promote_candidate`: `84`
- `fixture_only`: `67`
- `needs_replay`: `21`

## Highest Priority Replay

- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B12:combos` windows=`4` support=`1.8%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:conversion_box_first:B12:combos` windows=`4` support=`1.8%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B36` windows=`4` support=`1.4%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` windows=`4` support=`1.4%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` windows=`4` support=`1.4%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` windows=`4` support=`1.4%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B36` windows=`4` support=`1.4%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` windows=`4` support=`1.4%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` windows=`4` support=`1.4%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` windows=`4` support=`1.4%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B24:combos` windows=`4` support=`1.4%` match=`2.1%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:play_box_first:B24:boxed_canonicals` windows=`4` support=`1.4%` match=`2.0%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:play_box_first:B24:boxed_canonicals` windows=`4` support=`1.4%` match=`2.0%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B24` windows=`4` support=`1.3%` match=`3.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` windows=`4` support=`1.3%` match=`3.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` windows=`4` support=`1.3%` match=`3.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` windows=`4` support=`1.3%` match=`3.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B24` windows=`4` support=`1.3%` match=`3.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` windows=`4` support=`1.3%` match=`3.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` windows=`4` support=`1.3%` match=`3.3%`

## Highest Priority Restraints

- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack:PackB_mirror3rd` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack:aux_vtrac_index_overdue` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack_method:PackB_mirror3rd:canonical` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:analysis_prefix:B24:boxed_canonicals` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:conversion_box_first:B12:boxed_canonicals` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:play_box_first:B12:boxed_canonicals` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:play_box_first:B12:combos` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:analysis_prefix:B24` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:analysis_prefix:B36` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first:B12` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first:B24` role=`negative_control` windows=`4` false_proxy=`100.0%`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack:PackB_mirror3rd` role=`negative_control` windows=`4` false_proxy=`100.0%`

## Evidence Families To Watch

- `arena` role=`translator_teaching_surface` used=`97` underused=`23` wrong_lane=`66`
- `translation_sandbox` role=`translator_teaching_surface` used=`97` underused=`23` wrong_lane=`66`
- `brain1` role=`translator_teaching_surface` used=`95` underused=`23` wrong_lane=`66`
- `board_scoreboard` role=`support_gate_surface` used=`82` underused=`21` wrong_lane=`50`
- `old_candidate_universe` role=`support_gate_surface` used=`97` underused=`20` wrong_lane=`55`
- `shadow_policy` role=`support_gate_surface` used=`47` underused=`19` wrong_lane=`31`
- `old_play_card` role=`support_gate_surface` used=`75` underused=`13` wrong_lane=`11`
- `survivor` role=`support_gate_surface` used=`28` underused=`12` wrong_lane=`15`
- `profit_alerts` role=`support_gate_surface` used=`15` underused=`10` wrong_lane=`21`
- `positional` role=`support_gate_surface` used=`39` underused=`9` wrong_lane=`8`
- `blackapple` role=`support_gate_surface` used=`27` underused=`8` wrong_lane=`22`
- `due_doubles` role=`support_gate_surface` used=`18` underused=`0` wrong_lane=`11`

## Decay Guardrail

- `arena_box_total` lane=`boxed` horizon=`55.9%` incremental=`39.7%` role=`boxed_carryforward_teacher`
- `sandbox_box_seed` lane=`boxed` horizon=`46.0%` incremental=`34.0%` role=`boxed_carryforward_teacher`
- `brain1_box_core` lane=`boxed` horizon=`41.6%` incremental=`29.8%` role=`boxed_carryforward_teacher`
- `board_top_box_core` lane=`boxed` horizon=`12.6%` incremental=`9.0%` role=`boxed_carryforward_teacher`
- `brain1_vt_core` lane=`vtrac` horizon=`91.0%` incremental=`46.6%` role=`territory_decay_watch`
- `board_top_vt_core` lane=`vtrac` horizon=`68.1%` incremental=`44.1%` role=`territory_decay_watch`
- `arena_vt_total` lane=`vtrac` horizon=`97.3%` incremental=`35.5%` role=`territory_decay_watch`
- `sandbox_vt_seed` lane=`vtrac` horizon=`97.3%` incremental=`35.5%` role=`territory_decay_watch`
- `sandbox_exact_seed` lane=`straight` horizon=`13.9%` incremental=`10.7%` role=`straight_precision_probe`
- `preserved_not_budgeted` lane=`context` horizon=`6.9%` incremental=`5.0%` role=`carryforward_context`

## Files

- Decision workbench: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE3_DECISION_WORKBENCH.md`
- Promotion registry: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE3_PROMOTION_REGISTRY.csv`
- Replay queue: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE3_REPLAY_QUEUE.csv`
- Negative-control map: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE3_NEGATIVE_CONTROL_MAP.csv`
- Evidence-utilization matrix: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE3_EVIDENCE_UTILIZATION_MATRIX.csv`
- Decay stratification: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE3_DECAY_STRATIFICATION.csv`
