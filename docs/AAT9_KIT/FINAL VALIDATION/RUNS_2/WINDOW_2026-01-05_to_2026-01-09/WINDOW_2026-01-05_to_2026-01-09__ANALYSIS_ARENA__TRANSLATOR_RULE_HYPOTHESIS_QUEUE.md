# Translator Rule Hypothesis Queue

Purpose: queue bounded translator experiments from Stage 2/2B evidence without changing live scoring prematurely.

## Status Mix

- `test_as_gate`: `36`
- `test_now`: `35`
- `watch_only_until_box_confirmed`: `25`
- `negative_control`: `25`
- `pair_before_promotion`: `19`

## Top Hypotheses

- `HYP-001` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_play_card:ranked_candidate_canonical` lane=`box_overlap` avg_pool=`1.3` match_rate=`5.8%`
- `HYP-002` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_play_card:ranked_candidate_combo` lane=`box_overlap` avg_pool=`1.3` match_rate=`5.8%`
- `HYP-003` [test_now]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:ranked_candidate_canonical` lane=`box_overlap` avg_pool=`1.3` match_rate=`5.8%`
- `HYP-004` [test_now]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:ranked_candidate_combo` lane=`box_overlap` avg_pool=`1.3` match_rate=`5.8%`
- `HYP-005` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:conversion_box_first:B12:combos` lane=`box_overlap` avg_pool=`1.1666666666666667` match_rate=`4.8%`
- `HYP-006` [test_now]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy:conversion_box_first:B12:combos` lane=`box_overlap` avg_pool=`1.1666666666666667` match_rate=`4.8%`
- `HYP-007` [test_now]: `old_candidate_universe:pack_method:PackA_vt8:canonical + old_play_card:strategy:conversion_box_first:B36:combos` lane=`box_overlap` avg_pool=`2.230769230769231` match_rate=`4.6%`
- `HYP-008` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` lane=`box_overlap` avg_pool=`1.4193548387096775` match_rate=`4.5%`
- `HYP-009` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:analysis_prefix:B36` lane=`box_overlap` avg_pool=`1.4193548387096775` match_rate=`4.5%`
- `HYP-010` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` lane=`box_overlap` avg_pool=`1.4193548387096775` match_rate=`4.5%`
- `HYP-011` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:analysis_prefix:B36` lane=`box_overlap` avg_pool=`1.4193548387096775` match_rate=`4.5%`
- `HYP-012` [test_now]: `old_candidate_universe:pack_method:aux_positional:canonical + old_candidate_universe:pack_method:consensus_double_9:canonical` lane=`box_overlap` avg_pool=`1.6923076923076923` match_rate=`4.5%`
- `HYP-013` [test_now]: `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12 + survivor:survivor_frontier_canonicals` lane=`box_overlap` avg_pool=`1.2972972972972974` match_rate=`4.2%`
- `HYP-014` [test_now]: `old_candidate_universe:pack_method:PackA_vt8:canonical + old_play_card:strategy:analysis_prefix:B36:combos` lane=`box_overlap` avg_pool=`2.2641509433962264` match_rate=`4.2%`
- `HYP-015` [test_now]: `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12 + survivor:survivor_frontier_canonicals` lane=`box_overlap` avg_pool=`1.3243243243243243` match_rate=`4.1%`
- `HYP-016` [test_now]: `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12 + survivor:survivor_frontier_canonicals` lane=`box_overlap` avg_pool=`1.3243243243243243` match_rate=`4.1%`
- `HYP-017` [test_now]: `old_play_card:strategy_card:convergence_box_first:B12 + survivor:survivor_frontier_canonicals` lane=`box_overlap` avg_pool=`1.3611111111111112` match_rate=`4.1%`
- `HYP-018` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack:mirror_pair_closure` lane=`box_overlap` avg_pool=`1.4411764705882353` match_rate=`4.1%`
- `HYP-019` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack_method:mirror_pair_closure:canonical` lane=`box_overlap` avg_pool=`1.4411764705882353` match_rate=`4.1%`
- `HYP-020` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:R-perm-4:canonical` lane=`box_overlap` avg_pool=`1.4411764705882353` match_rate=`4.1%`
- `HYP-021` [test_now]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_candidate_universe:pack_method:mirror_pair_closure:canonical` lane=`box_overlap` avg_pool=`1.4411764705882353` match_rate=`4.1%`
- `HYP-022` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:conversion_box_first:B36:combos` lane=`box_overlap` avg_pool=`1.6304347826086956` match_rate=`4.0%`
- `HYP-023` [test_now]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy:conversion_box_first:B36:combos` lane=`box_overlap` avg_pool=`1.6304347826086956` match_rate=`4.0%`
- `HYP-024` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:analysis_prefix:B36:combos` lane=`box_overlap` avg_pool=`1.7857142857142858` match_rate=`4.0%`
- `HYP-025` [test_now]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy:analysis_prefix:B36:combos` lane=`box_overlap` avg_pool=`1.7857142857142858` match_rate=`4.0%`
- `HYP-026` [test_now]: `old_candidate_universe:pack_method:PackB_mirror3rd:canonical + old_play_card:ranked_candidate_canonical` lane=`box_overlap` avg_pool=`1.5` match_rate=`3.9%`
- `HYP-027` [test_now]: `old_candidate_universe:pack_method:PackB_mirror3rd:canonical + old_play_card:ranked_candidate_combo` lane=`box_overlap` avg_pool=`1.5` match_rate=`3.9%`
- `HYP-028` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B24` lane=`box_overlap` avg_pool=`1.368421052631579` match_rate=`3.8%`
- `HYP-029` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` lane=`box_overlap` avg_pool=`1.368421052631579` match_rate=`3.8%`
- `HYP-030` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` lane=`box_overlap` avg_pool=`1.368421052631579` match_rate=`3.8%`
- `HYP-031` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` lane=`box_overlap` avg_pool=`1.368421052631579` match_rate=`3.8%`
- `HYP-032` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B24` lane=`box_overlap` avg_pool=`1.368421052631579` match_rate=`3.8%`
- `HYP-033` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` lane=`box_overlap` avg_pool=`1.368421052631579` match_rate=`3.8%`
- `HYP-034` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` lane=`box_overlap` avg_pool=`1.368421052631579` match_rate=`3.8%`
- `HYP-035` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` lane=`box_overlap` avg_pool=`1.368421052631579` match_rate=`3.8%`
- `HYP-036` [test_as_gate]: `blackapple:recommended_canonicals + old_candidate_universe:pack_method:hot_zones_top:canonical` lane=`box_overlap` avg_pool=`1.2727272727272727` match_rate=`14.3%`
- `HYP-037` [test_as_gate]: `old_candidate_universe:pack_method:PackA_vt8:canonical + old_candidate_universe:pack_method:hot_zones_top:canonical` lane=`box_overlap` avg_pool=`1.2` match_rate=`8.3%`
- `HYP-038` [test_as_gate]: `old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:PackA_vt8:canonical` lane=`box_overlap` avg_pool=`1.1818181818181819` match_rate=`7.7%`
- `HYP-039` [test_as_gate]: `old_candidate_universe:pack_method:PackA_vt8:canonical + old_candidate_universe:pack_method:mirror_pair_closure:canonical` lane=`box_overlap` avg_pool=`1.1818181818181819` match_rate=`7.7%`
- `HYP-040` [test_as_gate]: `old_candidate_universe:pack:aux_positional + shadow_policy:primary_cluster_context` lane=`box_overlap` avg_pool=`1.4` match_rate=`7.1%`

## Guardrail

- These are experiment hypotheses. They are not final scoring weights or budget rules.
