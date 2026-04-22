# Analysis Arena Stage 3 Decision Workbench

Purpose: convert Stage-2/Stage-2B evidence into disciplined promotion, replay, restraint, and readiness decisions.

## Executive Read

- Stage 3 is a decision surface, not a live scoring surface.
- Cross-window repeatability is now the main filter separating replay candidates from one-window noise.
- VTRAC/territory strength remains valuable, but it is explicitly watch/decay unless paired with bounded boxed/exact proof.
- Negative controls are promoted as restraint assets so future ranking/budget work learns what not to spend on.

## Corpus

- Cross-window windows: `4`
- Focus casebook window: `WINDOW_2026-01-15_to_2026-01-22`
- Registry rows: `4312`
- Replay rows: `1170`
- Negative-control rows: `3489`
- Evidence-family rows: `11`
- Decay rows: `10`
- Casebook rows: `0`

## Decision Role Mix

- `negative_control`: `2417`
- `watch_decay_only`: `601`
- `supporting_gate`: `584`
- `blocked_low_denominator`: `441`
- `needs_more_windows`: `97`
- `promote_candidate`: `84`
- `fixture_only`: `67`
- `needs_replay`: `21`

## Replay Queue Mix

- `P2_support_gate_replay`: `584`
- `P4_low_denominator_fixture_replay`: `441`
- `P1_boxed_translator_replay`: `84`
- `P3_vtrac_decay_watch_replay`: `40`
- `P4_diagnostic_replay`: `21`

## Top Boxed Translator Candidates

- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B12:combos` windows=`4` pool=`1.8` match=`2.3%` support=`1.8%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:conversion_box_first:B12:combos` windows=`4` pool=`1.8` match=`2.3%` support=`1.8%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B36` windows=`4` pool=`1.7` match=`2.3%` support=`1.4%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` windows=`4` pool=`1.7` match=`2.3%` support=`1.4%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` windows=`4` pool=`1.7` match=`2.3%` support=`1.4%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` windows=`4` pool=`1.7` match=`2.3%` support=`1.4%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B36` windows=`4` pool=`1.7` match=`2.3%` support=`1.4%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` windows=`4` pool=`1.7` match=`2.3%` support=`1.4%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` windows=`4` pool=`1.7` match=`2.3%` support=`1.4%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` windows=`4` pool=`1.7` match=`2.3%` support=`1.4%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B24:combos` windows=`4` pool=`1.7` match=`2.1%` support=`1.4%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:play_box_first:B24:boxed_canonicals` windows=`4` pool=`1.6` match=`2.0%` support=`1.4%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:play_box_first:B24:boxed_canonicals` windows=`4` pool=`1.6` match=`2.0%` support=`1.4%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B24` windows=`4` pool=`1.3` match=`3.3%` support=`1.3%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` windows=`4` pool=`1.3` match=`3.3%` support=`1.3%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` windows=`4` pool=`1.3` match=`3.3%` support=`1.3%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` windows=`4` pool=`1.3` match=`3.3%` support=`1.3%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B24` windows=`4` pool=`1.3` match=`3.3%` support=`1.3%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` windows=`4` pool=`1.3` match=`3.3%` support=`1.3%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` windows=`4` pool=`1.3` match=`3.3%` support=`1.3%`

## Top Support Gates

- `translation_sandbox:diagnostic_straight_seed` windows=`4` match=`0.2%` support=`28.1%`
- `old_play_card:strategy:conversion_box_first:B36:combos` windows=`4` match=`0.3%` support=`24.4%`
- `blackapple:recommended_canonicals` windows=`4` match=`1.1%` support=`22.8%`
- `positional:positional_combo` windows=`4` match=`0.2%` support=`22.2%`
- `old_play_card:strategy:analysis_prefix:B24:combos` windows=`4` match=`0.2%` support=`22.0%`
- `old_play_card:strategy:conversion_box_first:B24:combos` windows=`4` match=`0.3%` support=`20.7%`
- `old_play_card:strategy:play_box_first:B36:combos` windows=`4` match=`0.3%` support=`19.0%`
- `old_play_card:ranked_candidate_combo` windows=`4` match=`0.2%` support=`16.0%`
- `old_play_card:strategy:play_box_first:B24:boxed_canonicals` windows=`4` match=`1.0%` support=`14.5%`
- `old_play_card:strategy:play_box_first:B24:combos` windows=`4` match=`0.3%` support=`14.5%`
- `old_play_card:strategy_card:convergence_box_first:B24` windows=`4` match=`1.0%` support=`14.1%`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` windows=`4` match=`1.0%` support=`14.1%`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` windows=`4` match=`1.0%` support=`14.1%`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` windows=`4` match=`1.0%` support=`14.1%`
- `old_play_card:strategy:analysis_prefix:B12:combos` windows=`4` match=`0.2%` support=`13.2%`
- `old_play_card:strategy:v0_2_default:B12:combos` windows=`4` match=`0.2%` support=`13.2%`
- `old_candidate_universe:pack:R-perm-4` windows=`4` match=`1.3%` support=`10.6%`
- `old_candidate_universe:pack_method:R-perm-4:canonical` windows=`4` match=`1.3%` support=`10.6%`
- `old_candidate_universe:pack:aux_positional` windows=`4` match=`1.1%` support=`10.4%`
- `old_play_card:strategy:play_box_first:B12:combos` windows=`4` match=`0.2%` support=`9.4%`

## Top Watch/Decay Surfaces

- `translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`4` support=`37.9%`
- `vtrac_box_confirmation::old_candidate_universe:candidate_universe_union_combo + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`4` support=`32.8%`
- `brain1:dominant_vtrac_indices` lane=`vtrac` windows=`4` support=`26.3%`
- `vtrac_overlap::brain1:dominant_vtrac_indices + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`4` support=`26.2%`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:candidate_universe_union_combo` lane=`vtrac` windows=`4` support=`24.7%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:stable_top:canonical + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`4` support=`23.8%`
- `vtrac_box_confirmation::translation_sandbox:diagnostic_boxed_seed + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`4` support=`22.6%`
- `vtrac_box_confirmation::brain1:secondary_canonicals + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`4` support=`21.8%`
- `vtrac_box_confirmation::old_play_card:strategy:v0_2_default:B36:combos + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`4` support=`20.8%`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack_method:stable_top:canonical` lane=`vtrac` windows=`4` support=`20.3%`
- `vtrac_box_confirmation::old_candidate_universe:pack:stable_top + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`4` support=`19.6%`
- `vtrac_box_confirmation::brain1:dominant_canonicals + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`4` support=`19.6%`
- `brain1:watchlist_indices` lane=`vtrac` windows=`4` support=`18.9%`
- `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:candidate_universe_union_combo` lane=`vtrac` windows=`4` support=`18.7%`
- `vtrac_overlap::brain1:watchlist_indices + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`4` support=`18.1%`

## Top Negative Controls

- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack:PackB_mirror3rd` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack:aux_vtrac_index_overdue` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack_method:PackB_mirror3rd:canonical` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:analysis_prefix:B24:boxed_canonicals` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:conversion_box_first:B12:boxed_canonicals` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:play_box_first:B12:boxed_canonicals` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:play_box_first:B12:combos` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:analysis_prefix:B24` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:analysis_prefix:B36` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first:B12` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first:B24` false_proxy=`100.0%` role=`negative_control`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack:PackB_mirror3rd` false_proxy=`100.0%` role=`negative_control`

## Evidence Utilization Read

- `blackapple` -> `support_gate_surface`; used `0`, underused `0`, wrong-lane `0`, decay `0`.
- `brain1` -> `support_gate_surface`; used `0`, underused `0`, wrong-lane `0`, decay `0`.
- `due_doubles` -> `support_gate_surface`; used `0`, underused `0`, wrong-lane `0`, decay `0`.
- `old_play_card` -> `support_gate_surface`; used `0`, underused `0`, wrong-lane `0`, decay `0`.
- `positional` -> `support_gate_surface`; used `0`, underused `0`, wrong-lane `0`, decay `0`.
- `profit_alerts` -> `support_gate_surface`; used `0`, underused `0`, wrong-lane `0`, decay `0`.
- `shadow_policy` -> `support_gate_surface`; used `0`, underused `0`, wrong-lane `0`, decay `0`.
- `survivor` -> `support_gate_surface`; used `0`, underused `0`, wrong-lane `0`, decay `0`.
- `translation_sandbox` -> `support_gate_surface`; used `0`, underused `0`, wrong-lane `0`, decay `0`.
- `board_scoreboard` -> `restraint_or_denominator_surface`; used `0`, underused `0`, wrong-lane `0`, decay `0`.
- `old_candidate_universe` -> `restraint_or_denominator_surface`; used `0`, underused `0`, wrong-lane `0`, decay `0`.

## Generated Files

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_DECISION_WORKBENCH.json`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_PROMOTION_REGISTRY.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_REPLAY_QUEUE.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_NEGATIVE_CONTROL_MAP.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_EVIDENCE_UTILIZATION_MATRIX.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_DECAY_STRATIFICATION.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE3_FRESH_WINDOW_DECISION_READINESS.md`

## Guardrail

- This workbench grants replay and interpretation permission only. It does not grant live scoring, candidate-formation, or budget permission.
