# Analysis Arena Stage 3 Decision Workbench

Purpose: convert Stage-2/Stage-2B evidence into disciplined promotion, replay, restraint, and readiness decisions.

## Executive Read

- Stage 3 is a decision surface, not a live scoring surface.
- Cross-window repeatability is now the main filter separating replay candidates from one-window noise.
- VTRAC/territory strength remains valuable, but it is explicitly watch/decay unless paired with bounded boxed/exact proof.
- Negative controls are promoted as restraint assets so future ranking/budget work learns what not to spend on.

## Corpus

- Cross-window windows: `3`
- Focus casebook window: `WINDOW_2026-01-20_to_2026-01-22`
- Registry rows: `4120`
- Replay rows: `1097`
- Negative-control rows: `3111`
- Evidence-family rows: `15`
- Decay rows: `10`
- Casebook rows: `46`

## Decision Role Mix

- `negative_control`: `2013`
- `watch_decay_only`: `585`
- `blocked_low_denominator`: `496`
- `supporting_gate`: `400`
- `fixture_only`: `370`
- `promote_candidate`: `147`
- `needs_more_windows`: `95`
- `needs_replay`: `14`

## Replay Queue Mix

- `P4_low_denominator_fixture_replay`: `496`
- `P2_support_gate_replay`: `400`
- `P1_boxed_translator_replay`: `147`
- `P3_vtrac_decay_watch_replay`: `40`
- `P4_diagnostic_replay`: `14`

## Top Boxed Translator Candidates

- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:combos` windows=`3` pool=`2.0` match=`2.7%` support=`2.4%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:combos` windows=`3` pool=`2.1` match=`2.4%` support=`2.4%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:combos` windows=`3` pool=`2.1` match=`2.4%` support=`2.4%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B24:combos` windows=`3` pool=`2.3` match=`2.2%` support=`2.4%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:analysis_prefix:B24:combos` windows=`3` pool=`2.3` match=`2.2%` support=`2.4%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:v0_2_default:B24:combos` windows=`3` pool=`2.4` match=`2.1%` support=`2.4%`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:v0_2_default:B24:combos` windows=`3` pool=`2.4` match=`2.0%` support=`2.4%`
- `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy:v0_2_default:B24:combos` windows=`3` pool=`2.4` match=`2.0%` support=`2.4%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B24:combos` windows=`3` pool=`1.9` match=`2.8%` support=`2.2%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals` windows=`3` pool=`1.8` match=`2.7%` support=`2.2%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals` windows=`3` pool=`1.8` match=`2.7%` support=`2.2%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:play_box_first:B36:boxed_canonicals` windows=`3` pool=`2.1` match=`2.3%` support=`2.2%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:play_box_first:B36:combos` windows=`3` pool=`2.1` match=`2.3%` support=`2.2%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:play_box_first:B36:boxed_canonicals` windows=`3` pool=`2.1` match=`2.3%` support=`2.2%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:play_box_first:B36:combos` windows=`3` pool=`2.1` match=`2.3%` support=`2.2%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:budgeted_canonicals_top` windows=`3` pool=`2.2` match=`2.1%` support=`2.2%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:budgeted_canonicals_top` windows=`3` pool=`2.2` match=`2.1%` support=`2.2%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + translation_sandbox:diagnostic_straight_seed` windows=`3` pool=`1.8` match=`2.8%` support=`2.0%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + translation_sandbox:diagnostic_straight_seed` windows=`3` pool=`1.8` match=`2.8%` support=`2.0%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B12:combos` windows=`3` pool=`1.7` match=`2.8%` support=`2.0%`

## Top Support Gates

- `old_play_card:strategy:v0_2_default:B24:combos` windows=`3` match=`0.2%` support=`29.8%`
- `translation_sandbox:diagnostic_straight_seed` windows=`3` match=`0.2%` support=`27.9%`
- `old_play_card:strategy:conversion_box_first:B36:combos` windows=`3` match=`0.3%` support=`25.3%`
- `positional:positional_combo` windows=`3` match=`0.0%` support=`23.1%`
- `blackapple:recommended_canonicals` windows=`3` match=`1.0%` support=`22.7%`
- `old_play_card:strategy:play_box_first:B36:combos` windows=`3` match=`0.3%` support=`21.1%`
- `old_play_card:strategy:play_box_first:B24:combos` windows=`3` match=`0.2%` support=`14.2%`
- `old_candidate_universe:pack:R-perm-4` windows=`3` match=`1.6%` support=`12.3%`
- `old_candidate_universe:pack_method:R-perm-4:canonical` windows=`3` match=`1.6%` support=`12.3%`
- `old_play_card:strategy:play_box_first:B12:combos` windows=`3` match=`0.3%` support=`9.1%`
- `old_candidate_universe:pack_method:PackA_vt8:canonical` windows=`3` match=`1.2%` support=`4.5%`
- `old_candidate_universe:pack_method:PackB_mirror3rd:canonical` windows=`3` match=`1.1%` support=`4.5%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:v0_2_default:B24:combos` windows=`3` match=`2.4%` support=`2.8%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:v0_2_default:B24:combos` windows=`3` match=`2.4%` support=`2.8%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B36:combos` windows=`3` match=`2.1%` support=`2.8%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:analysis_prefix:B36:combos` windows=`3` match=`2.1%` support=`2.8%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:v0_2_default:B36:combos` windows=`3` match=`2.1%` support=`2.8%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:v0_2_default:B36:combos` windows=`3` match=`2.1%` support=`2.8%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B24:combos` windows=`3` match=`2.1%` support=`2.6%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:conversion_box_first:B24:combos` windows=`3` match=`2.1%` support=`2.6%`

## Top Watch/Decay Surfaces

- `translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`3` support=`37.4%`
- `vtrac_box_confirmation::old_candidate_universe:candidate_universe_union_combo + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`3` support=`33.8%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:stable_top:canonical + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`3` support=`27.5%`
- `vtrac_box_confirmation::old_candidate_universe:pack:stable_top + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`3` support=`25.9%`
- `brain1:dominant_vtrac_indices` lane=`vtrac` windows=`3` support=`25.3%`
- `vtrac_overlap::brain1:dominant_vtrac_indices + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`3` support=`25.1%`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:candidate_universe_union_combo` lane=`vtrac` windows=`3` support=`24.7%`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack_method:stable_top:canonical` lane=`vtrac` windows=`3` support=`22.9%`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack:stable_top` lane=`vtrac` windows=`3` support=`21.7%`
- `vtrac_box_confirmation::brain1:secondary_canonicals + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`3` support=`21.5%`
- `vtrac_box_confirmation::translation_sandbox:diagnostic_boxed_seed + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`3` support=`21.5%`
- `vtrac_box_confirmation::old_play_card:strategy:v0_2_default:B36:combos + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`3` support=`21.3%`
- `vtrac_box_confirmation::brain1:dominant_canonicals + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`3` support=`19.6%`
- `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:candidate_universe_union_combo` lane=`vtrac` windows=`3` support=`18.2%`
- `brain1:watchlist_indices` lane=`vtrac` windows=`3` support=`18.2%`

## Top Negative Controls

- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack:PackB_mirror3rd` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack:aux_vtrac_index_overdue` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack_method:PackB_mirror3rd:canonical` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + shadow_policy:primary_cluster_survivor_frontier` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + due_doubles:example_canonicals` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack:PackB_mirror3rd` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack:due_doubles` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:PackA_vt8:canonical` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:PackB_mirror3rd:canonical` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:due_doubles:canonical` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:due_doubles_mirror_double:canonical` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:due_doubles_mirror_single:canonical` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_play_card:strategy:v0_2_default:B24:boxed_canonicals` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + shadow_policy:primary_cluster_survivor_frontier` false_proxy=`100.0%` role=`negative_control`

## Evidence Utilization Read

- `arena` -> `translator_teaching_surface`; used `23`, underused `2`, wrong-lane `15`, decay `19`.
- `translation_sandbox` -> `translator_teaching_surface`; used `23`, underused `2`, wrong-lane `15`, decay `19`.
- `old_candidate_universe` -> `support_gate_surface`; used `23`, underused `2`, wrong-lane `9`, decay `5`.
- `brain1` -> `translator_teaching_surface`; used `20`, underused `2`, wrong-lane `15`, decay `14`.
- `old_play_card` -> `support_gate_surface`; used `15`, underused `2`, wrong-lane `5`, decay `3`.
- `shadow_policy` -> `support_gate_surface`; used `9`, underused `2`, wrong-lane `9`, decay `1`.
- `survivor` -> `support_gate_surface`; used `2`, underused `2`, wrong-lane `5`, decay `2`.
- `board_scoreboard` -> `support_gate_surface`; used `14`, underused `1`, wrong-lane `11`, decay `9`.
- `positional` -> `support_gate_surface`; used `6`, underused `1`, wrong-lane `5`, decay `6`.
- `blackapple` -> `support_gate_surface`; used `5`, underused `0`, wrong-lane `9`, decay `2`.
- `profit_alerts` -> `support_gate_surface`; used `5`, underused `0`, wrong-lane `3`, decay `0`.
- `due_doubles` -> `support_gate_surface`; used `4`, underused `0`, wrong-lane `1`, decay `1`.

## Generated Files

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_DECISION_WORKBENCH.json`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_PROMOTION_REGISTRY.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_REPLAY_QUEUE.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_NEGATIVE_CONTROL_MAP.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_EVIDENCE_UTILIZATION_MATRIX.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_DECAY_STRATIFICATION.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_FRESH_WINDOW_DECISION_READINESS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__STAGE3_CASEBOOK.md`

## Guardrail

- This workbench grants replay and interpretation permission only. It does not grant live scoring, candidate-formation, or budget permission.
