# Analysis Arena Stage 3 Decision Workbench

Purpose: convert Stage-2/Stage-2B evidence into disciplined promotion, replay, restraint, and readiness decisions.

## Executive Read

- Stage 3 is a decision surface, not a live scoring surface.
- Cross-window repeatability is now the main filter separating replay candidates from one-window noise.
- VTRAC/territory strength remains valuable, but it is explicitly watch/decay unless paired with bounded boxed/exact proof.
- Negative controls are promoted as restraint assets so future ranking/budget work learns what not to spend on.

## Corpus

- Cross-window windows: `5`
- Focus casebook window: `WINDOW_2026-03-09_to_2026-03-23`
- Registry rows: `4312`
- Replay rows: `1135`
- Negative-control rows: `3360`
- Evidence-family rows: `15`
- Decay rows: `10`
- Casebook rows: `67`

## Decision Role Mix

- `negative_control`: `2342`
- `watch_decay_only`: `601`
- `supporting_gate`: `562`
- `blocked_low_denominator`: `303`
- `fixture_only`: `182`
- `promote_candidate`: `164`
- `needs_more_windows`: `92`
- `needs_replay`: `66`

## Replay Queue Mix

- `P2_support_gate_replay`: `562`
- `P4_low_denominator_fixture_replay`: `303`
- `P1_boxed_translator_replay`: `164`
- `P4_diagnostic_replay`: `66`
- `P3_vtrac_decay_watch_replay`: `40`

## Top Boxed Translator Candidates

- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:budgeted_canonicals_top` windows=`5` pool=`2.4` match=`2.2%` support=`2.6%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:budgeted_canonicals_top` windows=`5` pool=`2.4` match=`2.2%` support=`2.6%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B24:combos` windows=`5` pool=`2.5` match=`2.2%` support=`2.6%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:analysis_prefix:B24:combos` windows=`5` pool=`2.5` match=`2.2%` support=`2.6%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:play_box_first:B36:boxed_canonicals` windows=`5` pool=`2.3` match=`2.3%` support=`2.5%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:play_box_first:B36:combos` windows=`5` pool=`2.3` match=`2.3%` support=`2.5%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:play_box_first:B36:boxed_canonicals` windows=`5` pool=`2.3` match=`2.3%` support=`2.5%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:play_box_first:B36:combos` windows=`5` pool=`2.3` match=`2.3%` support=`2.5%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B12:combos` windows=`5` pool=`1.8` match=`2.6%` support=`2.1%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:conversion_box_first:B12:combos` windows=`5` pool=`1.8` match=`2.6%` support=`2.1%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals` windows=`5` pool=`2.0` match=`2.3%` support=`2.1%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals` windows=`5` pool=`2.0` match=`2.3%` support=`2.1%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + translation_sandbox:diagnostic_straight_seed` windows=`5` pool=`2.0` match=`2.5%` support=`2.0%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + translation_sandbox:diagnostic_straight_seed` windows=`5` pool=`2.0` match=`2.5%` support=`2.0%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first:B36` windows=`5` pool=`2.0` match=`2.2%` support=`2.0%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first:B36` windows=`5` pool=`2.0` match=`2.2%` support=`2.0%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:ranked_candidate_canonical` windows=`5` pool=`2.0` match=`2.2%` support=`1.9%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:ranked_candidate_combo` windows=`5` pool=`2.0` match=`2.2%` support=`1.9%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:ranked_candidate_canonical` windows=`5` pool=`2.0` match=`2.2%` support=`1.9%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:ranked_candidate_combo` windows=`5` pool=`2.0` match=`2.2%` support=`1.9%`

## Top Support Gates

- `translation_sandbox:diagnostic_straight_seed` windows=`5` match=`0.2%` support=`28.4%`
- `old_play_card:strategy:conversion_box_first:B36:combos` windows=`5` match=`0.3%` support=`24.0%`
- `blackapple:recommended_canonicals` windows=`5` match=`1.1%` support=`23.0%`
- `positional:positional_combo` windows=`5` match=`0.2%` support=`22.8%`
- `old_play_card:strategy:analysis_prefix:B24:combos` windows=`5` match=`0.2%` support=`22.0%`
- `old_play_card:strategy:conversion_box_first:B24:combos` windows=`5` match=`0.3%` support=`20.5%`
- `old_play_card:strategy:play_box_first:B36:combos` windows=`5` match=`0.3%` support=`19.0%`
- `old_play_card:strategy_card:convergence_box_first:B36` windows=`5` match=`1.0%` support=`18.3%`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` windows=`5` match=`1.0%` support=`18.3%`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` windows=`5` match=`1.0%` support=`18.3%`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` windows=`5` match=`1.0%` support=`18.3%`
- `old_play_card:ranked_candidate_canonical` windows=`5` match=`1.0%` support=`16.1%`
- `old_play_card:ranked_candidate_combo` windows=`5` match=`0.2%` support=`16.1%`
- `old_play_card:strategy:play_box_first:B24:boxed_canonicals` windows=`5` match=`1.1%` support=`14.4%`
- `old_play_card:strategy:play_box_first:B24:combos` windows=`5` match=`0.3%` support=`14.4%`
- `old_play_card:strategy_card:convergence_box_first:B24` windows=`5` match=`1.1%` support=`14.2%`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` windows=`5` match=`1.1%` support=`14.2%`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` windows=`5` match=`1.1%` support=`14.2%`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` windows=`5` match=`1.1%` support=`14.2%`
- `old_play_card:strategy:analysis_prefix:B12:combos` windows=`5` match=`0.2%` support=`13.3%`

## Top Watch/Decay Surfaces

- `translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`5` support=`38.4%`
- `vtrac_box_confirmation::old_candidate_universe:candidate_universe_union_combo + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`5` support=`32.9%`
- `brain1:dominant_vtrac_indices` lane=`vtrac` windows=`5` support=`26.7%`
- `vtrac_overlap::brain1:dominant_vtrac_indices + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`5` support=`26.6%`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:candidate_universe_union_combo` lane=`vtrac` windows=`5` support=`24.9%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:stable_top:canonical + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`5` support=`23.4%`
- `vtrac_box_confirmation::translation_sandbox:diagnostic_boxed_seed + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`5` support=`22.7%`
- `vtrac_box_confirmation::brain1:secondary_canonicals + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`5` support=`22.3%`
- `vtrac_box_confirmation::old_play_card:strategy:v0_2_default:B36:combos + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`5` support=`21.0%`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack_method:stable_top:canonical` lane=`vtrac` windows=`5` support=`20.2%`
- `vtrac_box_confirmation::brain1:dominant_canonicals + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`5` support=`19.9%`
- `brain1:watchlist_indices` lane=`vtrac` windows=`5` support=`19.1%`
- `vtrac_box_confirmation::old_candidate_universe:pack:stable_top + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`5` support=`19.0%`
- `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:candidate_universe_union_combo` lane=`vtrac` windows=`5` support=`18.8%`
- `vtrac_box_confirmation::brain1:dominant_canonicals + brain1:dominant_vtrac_indices` lane=`vtrac` windows=`5` support=`18.4%`

## Top Negative Controls

- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack:PackB_mirror3rd` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack:aux_vtrac_index_overdue` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack_method:PackB_mirror3rd:canonical` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:play_box_first:B12:boxed_canonicals` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:play_box_first:B12:combos` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:analysis_prefix:B36` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first:B24` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack:PackB_mirror3rd` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack:due_doubles` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:PackB_mirror3rd:canonical` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:due_doubles:canonical` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:due_doubles_mirror_double:canonical` false_proxy=`100.0%` role=`negative_control`

## Evidence Utilization Read

- `arena` -> `translator_teaching_surface`; used `97`, underused `23`, wrong-lane `66`, decay `103`.
- `translation_sandbox` -> `translator_teaching_surface`; used `97`, underused `23`, wrong-lane `66`, decay `103`.
- `brain1` -> `translator_teaching_surface`; used `95`, underused `23`, wrong-lane `66`, decay `101`.
- `board_scoreboard` -> `support_gate_surface`; used `82`, underused `21`, wrong-lane `50`, decay `78`.
- `old_candidate_universe` -> `support_gate_surface`; used `97`, underused `20`, wrong-lane `55`, decay `38`.
- `shadow_policy` -> `support_gate_surface`; used `47`, underused `19`, wrong-lane `31`, decay `5`.
- `old_play_card` -> `support_gate_surface`; used `75`, underused `13`, wrong-lane `11`, decay `16`.
- `survivor` -> `support_gate_surface`; used `28`, underused `12`, wrong-lane `15`, decay `13`.
- `profit_alerts` -> `support_gate_surface`; used `15`, underused `10`, wrong-lane `21`, decay `0`.
- `positional` -> `support_gate_surface`; used `39`, underused `9`, wrong-lane `8`, decay `20`.
- `blackapple` -> `support_gate_surface`; used `27`, underused `8`, wrong-lane `22`, decay `12`.
- `due_doubles` -> `support_gate_surface`; used `18`, underused `0`, wrong-lane `11`, decay `8`.

## Generated Files

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_DECISION_WORKBENCH.json`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_PROMOTION_REGISTRY.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_REPLAY_QUEUE.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_NEGATIVE_CONTROL_MAP.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_EVIDENCE_UTILIZATION_MATRIX.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_DECAY_STRATIFICATION.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_FRESH_WINDOW_DECISION_READINESS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__STAGE3_CASEBOOK.md`

## Guardrail

- This workbench grants replay and interpretation permission only. It does not grant live scoring, candidate-formation, or budget permission.
