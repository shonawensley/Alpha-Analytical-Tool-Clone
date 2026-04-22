# Translator Rule Hypothesis Queue

Purpose: queue bounded translator experiments from Stage 2/2B evidence without changing live scoring prematurely.

## Status Mix

- `test_now`: `35`
- `test_as_gate`: `35`
- `watch_only_until_box_confirmed`: `25`
- `negative_control`: `25`
- `pair_before_promotion`: `13`

## Top Hypotheses

- `HYP-001` [test_now]: `blackapple:recommended_canonicals + old_play_card:strategy:conversion_box_first:B12:combos` lane=`box_overlap` avg_pool=`1.2424242424242424` match_rate=`4.9%`
- `HYP-002` [test_now]: `blackapple:recommended_canonicals + old_candidate_universe:top_canonicals` lane=`box_overlap` avg_pool=`1.2307692307692308` match_rate=`4.7%`
- `HYP-003` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B12` lane=`box_overlap` avg_pool=`1.0238095238095237` match_rate=`4.7%`
- `HYP-004` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B12` lane=`box_overlap` avg_pool=`1.0238095238095237` match_rate=`4.7%`
- `HYP-005` [test_now]: `blackapple:recommended_canonicals + old_candidate_universe:pack:stable_top` lane=`box_overlap` avg_pool=`1.3333333333333333` match_rate=`4.4%`
- `HYP-006` [test_now]: `blackapple:recommended_canonicals + old_play_card:strategy:analysis_prefix:B36:combos` lane=`box_overlap` avg_pool=`1.4838709677419355` match_rate=`4.3%`
- `HYP-007` [test_now]: `old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` lane=`box_overlap` avg_pool=`1.9189189189189189` match_rate=`4.2%`
- `HYP-008` [test_now]: `old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` lane=`box_overlap` avg_pool=`1.9189189189189189` match_rate=`4.2%`
- `HYP-009` [test_now]: `blackapple:recommended_canonicals + shadow_policy:primary_cluster_context` lane=`box_overlap` avg_pool=`1.065217391304348` match_rate=`4.1%`
- `HYP-010` [test_now]: `old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` lane=`box_overlap` avg_pool=`1.9473684210526316` match_rate=`4.1%`
- `HYP-011` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_play_card:ranked_candidate_canonical` lane=`box_overlap` avg_pool=`1.2692307692307692` match_rate=`4.0%`
- `HYP-012` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_play_card:ranked_candidate_combo` lane=`box_overlap` avg_pool=`1.2692307692307692` match_rate=`4.0%`
- `HYP-013` [test_now]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:ranked_candidate_canonical` lane=`box_overlap` avg_pool=`1.2692307692307692` match_rate=`4.0%`
- `HYP-014` [test_now]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:ranked_candidate_combo` lane=`box_overlap` avg_pool=`1.2692307692307692` match_rate=`4.0%`
- `HYP-015` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B24` lane=`box_overlap` avg_pool=`1.3076923076923077` match_rate=`3.9%`
- `HYP-016` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` lane=`box_overlap` avg_pool=`1.3076923076923077` match_rate=`3.9%`
- `HYP-017` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` lane=`box_overlap` avg_pool=`1.3076923076923077` match_rate=`3.9%`
- `HYP-018` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` lane=`box_overlap` avg_pool=`1.3076923076923077` match_rate=`3.9%`
- `HYP-019` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B24` lane=`box_overlap` avg_pool=`1.3076923076923077` match_rate=`3.9%`
- `HYP-020` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` lane=`box_overlap` avg_pool=`1.3076923076923077` match_rate=`3.9%`
- `HYP-021` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` lane=`box_overlap` avg_pool=`1.3076923076923077` match_rate=`3.9%`
- `HYP-022` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` lane=`box_overlap` avg_pool=`1.3076923076923077` match_rate=`3.9%`
- `HYP-023` [test_now]: `blackapple:recommended_canonicals + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`box_overlap` avg_pool=`1.2380952380952381` match_rate=`3.8%`
- `HYP-024` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + profit_alerts:implied_canonicals` lane=`box_overlap` avg_pool=`1.127659574468085` match_rate=`3.8%`
- `HYP-025` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + profit_alerts:implied_canonicals` lane=`box_overlap` avg_pool=`1.127659574468085` match_rate=`3.8%`
- `HYP-026` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack:mirror_pair_closure` lane=`box_overlap` avg_pool=`1.3442622950819672` match_rate=`3.7%`
- `HYP-027` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack_method:mirror_pair_closure:canonical` lane=`box_overlap` avg_pool=`1.3442622950819672` match_rate=`3.7%`
- `HYP-028` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:R-perm-4:canonical` lane=`box_overlap` avg_pool=`1.3442622950819672` match_rate=`3.7%`
- `HYP-029` [test_now]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_candidate_universe:pack_method:mirror_pair_closure:canonical` lane=`box_overlap` avg_pool=`1.3442622950819672` match_rate=`3.7%`
- `HYP-030` [test_now]: `old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:convergence_box_first:B24` lane=`box_overlap` avg_pool=`2.1666666666666665` match_rate=`3.5%`
- `HYP-031` [test_now]: `old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` lane=`box_overlap` avg_pool=`2.1666666666666665` match_rate=`3.5%`
- `HYP-032` [test_now]: `old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` lane=`box_overlap` avg_pool=`2.1666666666666665` match_rate=`3.5%`
- `HYP-033` [test_now]: `old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` lane=`box_overlap` avg_pool=`2.1666666666666665` match_rate=`3.5%`
- `HYP-034` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:conversion_box_first:B12:combos` lane=`box_overlap` avg_pool=`1.2285714285714286` match_rate=`3.5%`
- `HYP-035` [test_now]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy:conversion_box_first:B12:combos` lane=`box_overlap` avg_pool=`1.2285714285714286` match_rate=`3.5%`
- `HYP-036` [test_as_gate]: `old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` lane=`box_overlap` avg_pool=`1.0526315789473684` match_rate=`10.0%`
- `HYP-037` [test_as_gate]: `old_candidate_universe:pack:R-perm-4 + old_play_card:strategy_card:analysis_prefix:B36` lane=`box_overlap` avg_pool=`1.0526315789473684` match_rate=`10.0%`
- `HYP-038` [test_as_gate]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` lane=`box_overlap` avg_pool=`1.0526315789473684` match_rate=`10.0%`
- `HYP-039` [test_as_gate]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy_card:analysis_prefix:B36` lane=`box_overlap` avg_pool=`1.0526315789473684` match_rate=`10.0%`
- `HYP-040` [test_as_gate]: `blackapple:recommended_canonicals + old_play_card:strategy:play_box_first:B12:boxed_canonicals` lane=`box_overlap` avg_pool=`1.0` match_rate=`10.0%`

## Guardrail

- These are experiment hypotheses. They are not final scoring weights or budget rules.
