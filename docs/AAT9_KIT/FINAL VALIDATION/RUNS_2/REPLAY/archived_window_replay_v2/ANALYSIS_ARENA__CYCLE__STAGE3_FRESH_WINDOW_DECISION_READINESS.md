# Stage 3 Fresh-Window Decision Readiness

Purpose: lock how Stage-3 evidence should be used before the next fresh window.

## Permission Model

- Approved now: observation, replay, casebook review, decay/watch interpretation, negative-control restraint.
- Blocked now: live scoring changes, live budget changes, automatic candidate promotion.
- Required before scoring rewrite: replay candidates must survive cross-window fixture replay with denominator controls.

## Decision Mix

- `negative_control`: `2013`
- `watch_decay_only`: `585`
- `blocked_low_denominator`: `496`
- `supporting_gate`: `400`
- `fixture_only`: `370`
- `promote_candidate`: `147`
- `needs_more_windows`: `95`
- `needs_replay`: `14`

## Highest Priority Replay

- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:combos` windows=`3` support=`2.4%` match=`2.7%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:combos` windows=`3` support=`2.4%` match=`2.4%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:combos` windows=`3` support=`2.4%` match=`2.4%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B24:combos` windows=`3` support=`2.4%` match=`2.2%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:analysis_prefix:B24:combos` windows=`3` support=`2.4%` match=`2.2%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:v0_2_default:B24:combos` windows=`3` support=`2.4%` match=`2.1%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:v0_2_default:B24:combos` windows=`3` support=`2.4%` match=`2.0%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy:v0_2_default:B24:combos` windows=`3` support=`2.4%` match=`2.0%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B24:combos` windows=`3` support=`2.2%` match=`2.8%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals` windows=`3` support=`2.2%` match=`2.7%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals` windows=`3` support=`2.2%` match=`2.7%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:play_box_first:B36:boxed_canonicals` windows=`3` support=`2.2%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:play_box_first:B36:combos` windows=`3` support=`2.2%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:play_box_first:B36:boxed_canonicals` windows=`3` support=`2.2%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:play_box_first:B36:combos` windows=`3` support=`2.2%` match=`2.3%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:budgeted_canonicals_top` windows=`3` support=`2.2%` match=`2.1%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:budgeted_canonicals_top` windows=`3` support=`2.2%` match=`2.1%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + translation_sandbox:diagnostic_straight_seed` windows=`3` support=`2.0%` match=`2.8%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + translation_sandbox:diagnostic_straight_seed` windows=`3` support=`2.0%` match=`2.8%`
- `P1_boxed_translator_replay` `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B12:combos` windows=`3` support=`2.0%` match=`2.8%`

## Highest Priority Restraints

- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack:PackB_mirror3rd` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack:aux_vtrac_index_overdue` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack_method:PackB_mirror3rd:canonical` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::blackapple:recommended_canonicals + shadow_policy:primary_cluster_survivor_frontier` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::board_scoreboard:top_canonicals + due_doubles:example_canonicals` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack:PackB_mirror3rd` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack:due_doubles` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:PackA_vt8:canonical` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:PackB_mirror3rd:canonical` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:due_doubles:canonical` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:due_doubles_mirror_double:canonical` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:due_doubles_mirror_single:canonical` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::board_scoreboard:top_canonicals + old_play_card:strategy:v0_2_default:B24:boxed_canonicals` role=`negative_control` windows=`3` false_proxy=`100.0%`
- `box_overlap::board_scoreboard:top_canonicals + shadow_policy:primary_cluster_survivor_frontier` role=`negative_control` windows=`3` false_proxy=`100.0%`

## Evidence Families To Watch

- `arena` role=`translator_teaching_surface` used=`23` underused=`2` wrong_lane=`15`
- `translation_sandbox` role=`translator_teaching_surface` used=`23` underused=`2` wrong_lane=`15`
- `old_candidate_universe` role=`support_gate_surface` used=`23` underused=`2` wrong_lane=`9`
- `brain1` role=`translator_teaching_surface` used=`20` underused=`2` wrong_lane=`15`
- `old_play_card` role=`support_gate_surface` used=`15` underused=`2` wrong_lane=`5`
- `shadow_policy` role=`support_gate_surface` used=`9` underused=`2` wrong_lane=`9`
- `survivor` role=`support_gate_surface` used=`2` underused=`2` wrong_lane=`5`
- `board_scoreboard` role=`support_gate_surface` used=`14` underused=`1` wrong_lane=`11`
- `positional` role=`support_gate_surface` used=`6` underused=`1` wrong_lane=`5`
- `blackapple` role=`support_gate_surface` used=`5` underused=`0` wrong_lane=`9`
- `profit_alerts` role=`support_gate_surface` used=`5` underused=`0` wrong_lane=`3`
- `due_doubles` role=`support_gate_surface` used=`4` underused=`0` wrong_lane=`1`

## Decay Guardrail

- `arena_box_total` lane=`boxed` horizon=`52.4%` incremental=`37.3%` role=`boxed_carryforward_teacher`
- `brain1_box_core` lane=`boxed` horizon=`42.1%` incremental=`31.0%` role=`boxed_carryforward_teacher`
- `sandbox_box_seed` lane=`boxed` horizon=`42.5%` incremental=`30.2%` role=`boxed_carryforward_teacher`
- `board_top_box_core` lane=`boxed` horizon=`15.5%` incremental=`12.3%` role=`boxed_carryforward_teacher`
- `brain1_vt_core` lane=`vtrac` horizon=`89.3%` incremental=`48.4%` role=`territory_decay_watch`
- `board_top_vt_core` lane=`vtrac` horizon=`64.3%` incremental=`40.1%` role=`territory_decay_watch`
- `arena_vt_total` lane=`vtrac` horizon=`98.0%` incremental=`39.3%` role=`territory_decay_watch`
- `sandbox_vt_seed` lane=`vtrac` horizon=`98.0%` incremental=`39.3%` role=`territory_decay_watch`
- `sandbox_exact_seed` lane=`straight` horizon=`15.5%` incremental=`12.3%` role=`straight_precision_probe`
- `preserved_not_budgeted` lane=`context` horizon=`6.3%` incremental=`4.8%` role=`carryforward_context`

## Files

- Decision workbench: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_DECISION_WORKBENCH.md`
- Promotion registry: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_PROMOTION_REGISTRY.csv`
- Replay queue: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_REPLAY_QUEUE.csv`
- Negative-control map: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_NEGATIVE_CONTROL_MAP.csv`
- Evidence-utilization matrix: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_EVIDENCE_UTILIZATION_MATRIX.csv`
- Decay stratification: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_DECAY_STRATIFICATION.csv`
