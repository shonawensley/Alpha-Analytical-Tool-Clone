# Translator Rule Hypothesis Queue

Purpose: queue bounded translator experiments from Stage 2/2B evidence without changing live scoring prematurely.

## Status Mix

- `test_now`: `35`
- `test_as_gate`: `35`
- `watch_only_until_box_confirmed`: `25`
- `negative_control`: `25`
- `pair_before_promotion`: `11`

## Top Hypotheses

- `HYP-001` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` lane=`box_overlap` avg_pool=`1.0476190476190477` match_rate=`6.8%`
- `HYP-002` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first:B24` lane=`box_overlap` avg_pool=`1.0476190476190477` match_rate=`6.8%`
- `HYP-003` [test_now]: `brain1:secondary_canonicals + old_candidate_universe:pack:mirror_pair_closure` lane=`box_overlap` avg_pool=`1.278688524590164` match_rate=`5.1%`
- `HYP-004` [test_now]: `brain1:secondary_canonicals + old_candidate_universe:pack_method:mirror_pair_closure:canonical` lane=`box_overlap` avg_pool=`1.278688524590164` match_rate=`5.1%`
- `HYP-005` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`box_overlap` avg_pool=`1.3404255319148937` match_rate=`4.8%`
- `HYP-006` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`box_overlap` avg_pool=`1.3404255319148937` match_rate=`4.8%`
- `HYP-007` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:convergence_box_first:B36` lane=`box_overlap` avg_pool=`1.4098360655737705` match_rate=`4.7%`
- `HYP-008` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` lane=`box_overlap` avg_pool=`1.4098360655737705` match_rate=`4.7%`
- `HYP-009` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` lane=`box_overlap` avg_pool=`1.4098360655737705` match_rate=`4.7%`
- `HYP-010` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` lane=`box_overlap` avg_pool=`1.4098360655737705` match_rate=`4.7%`
- `HYP-011` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B24:boxed_canonicals` lane=`box_overlap` avg_pool=`1.2692307692307692` match_rate=`4.5%`
- `HYP-012` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B24:combos` lane=`box_overlap` avg_pool=`1.2692307692307692` match_rate=`4.5%`
- `HYP-013` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:ranked_candidate_canonical` lane=`box_overlap` avg_pool=`1.378787878787879` match_rate=`4.4%`
- `HYP-014` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:ranked_candidate_combo` lane=`box_overlap` avg_pool=`1.378787878787879` match_rate=`4.4%`
- `HYP-015` [test_now]: `old_play_card:strategy:analysis_prefix:B24:boxed_canonicals + positional:positional_canonical` lane=`box_overlap` avg_pool=`1.2432432432432432` match_rate=`4.3%`
- `HYP-016` [test_now]: `old_play_card:strategy:analysis_prefix:B24:boxed_canonicals + positional:positional_combo` lane=`box_overlap` avg_pool=`1.2432432432432432` match_rate=`4.3%`
- `HYP-017` [test_now]: `old_play_card:strategy_card:analysis_prefix:B24 + positional:positional_canonical` lane=`box_overlap` avg_pool=`1.2432432432432432` match_rate=`4.3%`
- `HYP-018` [test_now]: `old_play_card:strategy_card:analysis_prefix:B24 + positional:positional_combo` lane=`box_overlap` avg_pool=`1.2432432432432432` match_rate=`4.3%`
- `HYP-019` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B24` lane=`box_overlap` avg_pool=`1.3194444444444444` match_rate=`4.2%`
- `HYP-020` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` lane=`box_overlap` avg_pool=`1.3194444444444444` match_rate=`4.2%`
- `HYP-021` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` lane=`box_overlap` avg_pool=`1.3194444444444444` match_rate=`4.2%`
- `HYP-022` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` lane=`box_overlap` avg_pool=`1.3194444444444444` match_rate=`4.2%`
- `HYP-023` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B24` lane=`box_overlap` avg_pool=`1.3194444444444444` match_rate=`4.2%`
- `HYP-024` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` lane=`box_overlap` avg_pool=`1.3194444444444444` match_rate=`4.2%`
- `HYP-025` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` lane=`box_overlap` avg_pool=`1.3194444444444444` match_rate=`4.2%`
- `HYP-026` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` lane=`box_overlap` avg_pool=`1.3194444444444444` match_rate=`4.2%`
- `HYP-027` [test_now]: `old_candidate_universe:pack:stable_top + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`box_overlap` avg_pool=`1.2` match_rate=`4.2%`
- `HYP-028` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B36:boxed_canonicals` lane=`box_overlap` avg_pool=`1.4411764705882353` match_rate=`4.1%`
- `HYP-029` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B36:combos` lane=`box_overlap` avg_pool=`1.4411764705882353` match_rate=`4.1%`
- `HYP-030` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + profit_alerts:top_profit_alerts` lane=`box_overlap` avg_pool=`1.0416666666666667` match_rate=`4.0%`
- `HYP-031` [test_now]: `old_candidate_universe:pack_method:stable_top:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`box_overlap` avg_pool=`1.25` match_rate=`4.0%`
- `HYP-032` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:combos` lane=`box_overlap` avg_pool=`1.2881355932203389` match_rate=`3.9%`
- `HYP-033` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:v0_2_default:B12:combos` lane=`box_overlap` avg_pool=`1.2881355932203389` match_rate=`3.9%`
- `HYP-034` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B12:combos` lane=`box_overlap` avg_pool=`1.3166666666666667` match_rate=`3.8%`
- `HYP-035` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + positional:positional_canonical` lane=`box_overlap` avg_pool=`1.7142857142857142` match_rate=`3.8%`
- `HYP-036` [test_as_gate]: `old_candidate_universe:pack:mirror_pair_closure + profit_alerts:implied_canonicals` lane=`box_overlap` avg_pool=`1.0555555555555556` match_rate=`10.5%`
- `HYP-037` [test_as_gate]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + profit_alerts:implied_canonicals` lane=`box_overlap` avg_pool=`1.0555555555555556` match_rate=`10.5%`
- `HYP-038` [test_as_gate]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B12:boxed_canonicals` lane=`box_overlap` avg_pool=`1.0` match_rate=`9.1%`
- `HYP-039` [test_as_gate]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:v0_2_default:B12:boxed_canonicals` lane=`box_overlap` avg_pool=`1.0` match_rate=`9.1%`
- `HYP-040` [test_as_gate]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:analysis_prefix:B12` lane=`box_overlap` avg_pool=`1.0` match_rate=`9.1%`

## Guardrail

- These are experiment hypotheses. They are not final scoring weights or budget rules.
