# Translator Rule Hypothesis Queue

Purpose: queue bounded translator experiments from Stage 2/2B evidence without changing live scoring prematurely.

## Status Mix

- `test_now`: `35`
- `test_as_gate`: `35`
- `watch_only_until_box_confirmed`: `25`
- `negative_control`: `25`
- `pair_before_promotion`: `20`

## Top Hypotheses

- `HYP-001` [test_now]: `old_candidate_universe:pack_method:stable_top:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`box_overlap` avg_pool=`2.096774193548387` match_rate=`3.1%`
- `HYP-002` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + translation_sandbox:diagnostic_straight_seed` lane=`box_overlap` avg_pool=`2.0303030303030303` match_rate=`3.0%`
- `HYP-003` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + translation_sandbox:diagnostic_straight_seed` lane=`box_overlap` avg_pool=`2.0303030303030303` match_rate=`3.0%`
- `HYP-004` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` lane=`box_overlap` avg_pool=`1.2` match_rate=`2.8%`
- `HYP-005` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first:B24` lane=`box_overlap` avg_pool=`1.2` match_rate=`2.8%`
- `HYP-006` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` lane=`box_overlap` avg_pool=`1.2` match_rate=`2.8%`
- `HYP-007` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first:B24` lane=`box_overlap` avg_pool=`1.2` match_rate=`2.8%`
- `HYP-008` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:combos` lane=`box_overlap` avg_pool=`2.108108108108108` match_rate=`2.6%`
- `HYP-009` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:combos` lane=`box_overlap` avg_pool=`2.2432432432432434` match_rate=`2.4%`
- `HYP-010` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:combos` lane=`box_overlap` avg_pool=`2.210526315789474` match_rate=`2.4%`
- `HYP-011` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_candidate_universe:top_canonicals` lane=`box_overlap` avg_pool=`1.5666666666666667` match_rate=`2.1%`
- `HYP-012` [test_now]: `old_play_card:strategy:conversion_box_first:B36:combos + positional:positional_canonical` lane=`box_overlap` avg_pool=`2.638888888888889` match_rate=`2.1%`
- `HYP-013` [test_now]: `old_play_card:strategy:conversion_box_first:B36:combos + positional:positional_combo` lane=`box_overlap` avg_pool=`2.638888888888889` match_rate=`2.1%`
- `HYP-014` [test_now]: `old_candidate_universe:pack:stable_top + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`box_overlap` avg_pool=`1.6` match_rate=`2.1%`
- `HYP-015` [test_now]: `board_scoreboard:top_canonicals + old_play_card:strategy:play_box_first:B24:boxed_canonicals` lane=`box_overlap` avg_pool=`1.5806451612903225` match_rate=`2.0%`
- `HYP-016` [test_now]: `board_scoreboard:top_canonicals + old_play_card:strategy:play_box_first:B24:combos` lane=`box_overlap` avg_pool=`1.5806451612903225` match_rate=`2.0%`
- `HYP-017` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:v0_2_default:B24:combos` lane=`box_overlap` avg_pool=`2.4634146341463414` match_rate=`2.0%`
- `HYP-018` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:v0_2_default:B36:combos` lane=`box_overlap` avg_pool=`2.4634146341463414` match_rate=`2.0%`
- `HYP-019` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B24:combos` lane=`box_overlap` avg_pool=`2.5853658536585367` match_rate=`1.9%`
- `HYP-020` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:conversion_box_first:B24:combos` lane=`box_overlap` avg_pool=`2.5853658536585367` match_rate=`1.9%`
- `HYP-021` [test_now]: `old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:convergence_box_first:B24` lane=`box_overlap` avg_pool=`1.65625` match_rate=`1.9%`
- `HYP-022` [test_now]: `old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` lane=`box_overlap` avg_pool=`1.65625` match_rate=`1.9%`
- `HYP-023` [test_now]: `old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` lane=`box_overlap` avg_pool=`1.65625` match_rate=`1.9%`
- `HYP-024` [test_now]: `old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` lane=`box_overlap` avg_pool=`1.65625` match_rate=`1.9%`
- `HYP-025` [test_now]: `old_play_card:strategy:analysis_prefix:B36:combos + positional:positional_canonical` lane=`box_overlap` avg_pool=`2.891891891891892` match_rate=`1.9%`
- `HYP-026` [test_now]: `old_play_card:strategy:analysis_prefix:B36:combos + positional:positional_combo` lane=`box_overlap` avg_pool=`2.891891891891892` match_rate=`1.9%`
- `HYP-027` [test_now]: `board_scoreboard:top_canonicals + old_candidate_universe:pack_method:hot_zones_top:canonical` lane=`box_overlap` avg_pool=`1.7419354838709677` match_rate=`1.9%`
- `HYP-028` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:v0_2_default:B36:combos` lane=`box_overlap` avg_pool=`2.619047619047619` match_rate=`1.8%`
- `HYP-029` [test_now]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy:v0_2_default:B36:combos` lane=`box_overlap` avg_pool=`2.619047619047619` match_rate=`1.8%`
- `HYP-030` [test_now]: `old_play_card:strategy:v0_2_default:B24:combos + positional:positional_canonical` lane=`box_overlap` avg_pool=`2.9210526315789473` match_rate=`1.8%`
- `HYP-031` [test_now]: `old_play_card:strategy:v0_2_default:B24:combos + positional:positional_combo` lane=`box_overlap` avg_pool=`2.9210526315789473` match_rate=`1.8%`
- `HYP-032` [test_now]: `old_candidate_universe:candidate_universe_union_combo + old_candidate_universe:pack:R-perm-4` lane=`box_overlap` avg_pool=`4.0` match_rate=`1.8%`
- `HYP-033` [test_now]: `old_candidate_universe:candidate_universe_union_combo + old_candidate_universe:pack_method:R-perm-4:canonical` lane=`box_overlap` avg_pool=`4.0` match_rate=`1.8%`
- `HYP-034` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack_method:R-perm-4:canonical` lane=`box_overlap` avg_pool=`4.0` match_rate=`1.8%`
- `HYP-035` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:convergence_box_first:B36` lane=`box_overlap` avg_pool=`1.6` match_rate=`1.8%`
- `HYP-036` [test_as_gate]: `old_play_card:strategy:conversion_box_first:B36:boxed_canonicals + old_play_card:strategy:v0_2_default:B36:boxed_canonicals` lane=`box_overlap` avg_pool=`1.0` match_rate=`10.0%`
- `HYP-037` [test_as_gate]: `old_play_card:strategy:v0_2_default:B36:boxed_canonicals + old_play_card:strategy_card:conversion_box_first:B36` lane=`box_overlap` avg_pool=`1.0` match_rate=`10.0%`
- `HYP-038` [test_as_gate]: `old_candidate_universe:pack_method:hot_zones_top:canonical + old_play_card:strategy:v0_2_default:B36:boxed_canonicals` lane=`box_overlap` avg_pool=`1.0` match_rate=`8.3%`
- `HYP-039` [test_as_gate]: `old_play_card:strategy:play_box_first:B36:boxed_canonicals + old_play_card:strategy:v0_2_default:B36:boxed_canonicals` lane=`box_overlap` avg_pool=`1.0909090909090908` match_rate=`8.3%`
- `HYP-040` [test_as_gate]: `old_play_card:strategy:play_box_first:B36:combos + old_play_card:strategy:v0_2_default:B36:boxed_canonicals` lane=`box_overlap` avg_pool=`1.0909090909090908` match_rate=`8.3%`

## Guardrail

- These are experiment hypotheses. They are not final scoring weights or budget rules.
