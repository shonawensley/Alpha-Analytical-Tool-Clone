# Translator Rule Hypothesis Queue

Purpose: queue bounded translator experiments from Stage 2/2B evidence without changing live scoring prematurely.

## Status Mix

- `test_now`: `35`
- `test_as_gate`: `35`
- `watch_only_until_box_confirmed`: `25`
- `negative_control`: `25`
- `pair_before_promotion`: `11`

## Top Hypotheses

- `HYP-001` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`box_overlap` avg_pool=`1.4193548387096775` match_rate=`6.8%`
- `HYP-002` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`box_overlap` avg_pool=`1.4193548387096775` match_rate=`6.8%`
- `HYP-003` [test_now]: `old_candidate_universe:pack:PackB_mirror3rd + old_candidate_universe:pack:R-perm-4` lane=`box_overlap` avg_pool=`1.0` match_rate=`5.4%`
- `HYP-004` [test_now]: `old_candidate_universe:pack:PackB_mirror3rd + old_candidate_universe:pack_method:R-perm-4:canonical` lane=`box_overlap` avg_pool=`1.0` match_rate=`5.4%`
- `HYP-005` [test_now]: `brain1:secondary_canonicals + old_candidate_universe:pack:mirror_pair_closure` lane=`box_overlap` avg_pool=`1.4` match_rate=`5.4%`
- `HYP-006` [test_now]: `brain1:secondary_canonicals + old_candidate_universe:pack_method:mirror_pair_closure:canonical` lane=`box_overlap` avg_pool=`1.4` match_rate=`5.4%`
- `HYP-007` [test_now]: `blackapple:recommended_canonicals + brain1:dominant_canonicals` lane=`box_overlap` avg_pool=`1.4146341463414633` match_rate=`5.2%`
- `HYP-008` [test_now]: `blackapple:recommended_canonicals + brain1:context_reinforced_canonicals` lane=`box_overlap` avg_pool=`1.21875` match_rate=`5.1%`
- `HYP-009` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:budgeted_canonicals_top` lane=`box_overlap` avg_pool=`1.4444444444444444` match_rate=`5.1%`
- `HYP-010` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B36:boxed_canonicals` lane=`box_overlap` avg_pool=`1.3958333333333333` match_rate=`4.5%`
- `HYP-011` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B36:combos` lane=`box_overlap` avg_pool=`1.3958333333333333` match_rate=`4.5%`
- `HYP-012` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack_method:PackB_mirror3rd:canonical` lane=`box_overlap` avg_pool=`1.0` match_rate=`4.3%`
- `HYP-013` [test_now]: `old_candidate_universe:pack_method:PackB_mirror3rd:canonical + old_candidate_universe:pack_method:R-perm-4:canonical` lane=`box_overlap` avg_pool=`1.0` match_rate=`4.3%`
- `HYP-014` [test_now]: `blackapple:recommended_canonicals + old_play_card:strategy:analysis_prefix:B36:combos` lane=`box_overlap` avg_pool=`1.5454545454545454` match_rate=`3.9%`
- `HYP-015` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B12:combos` lane=`box_overlap` avg_pool=`1.2222222222222223` match_rate=`3.6%`
- `HYP-016` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B24:combos` lane=`box_overlap` avg_pool=`1.4482758620689655` match_rate=`3.6%`
- `HYP-017` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:convergence_box_first:B36` lane=`box_overlap` avg_pool=`1.2127659574468086` match_rate=`3.5%`
- `HYP-018` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` lane=`box_overlap` avg_pool=`1.2127659574468086` match_rate=`3.5%`
- `HYP-019` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` lane=`box_overlap` avg_pool=`1.2127659574468086` match_rate=`3.5%`
- `HYP-020` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` lane=`box_overlap` avg_pool=`1.2127659574468086` match_rate=`3.5%`
- `HYP-021` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals` lane=`box_overlap` avg_pool=`1.2608695652173914` match_rate=`3.4%`
- `HYP-022` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first:B36` lane=`box_overlap` avg_pool=`1.2608695652173914` match_rate=`3.4%`
- `HYP-023` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:ranked_candidate_canonical` lane=`box_overlap` avg_pool=`1.2553191489361701` match_rate=`3.4%`
- `HYP-024` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:ranked_candidate_combo` lane=`box_overlap` avg_pool=`1.2553191489361701` match_rate=`3.4%`
- `HYP-025` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:combos` lane=`box_overlap` avg_pool=`1.4833333333333334` match_rate=`3.4%`
- `HYP-026` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:v0_2_default:B24:combos` lane=`box_overlap` avg_pool=`1.7971014492753623` match_rate=`3.2%`
- `HYP-027` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:v0_2_default:B36:combos` lane=`box_overlap` avg_pool=`1.7971014492753623` match_rate=`3.2%`
- `HYP-028` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:combos` lane=`box_overlap` avg_pool=`1.5714285714285714` match_rate=`3.0%`
- `HYP-029` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:combos` lane=`box_overlap` avg_pool=`1.596774193548387` match_rate=`3.0%`
- `HYP-030` [test_now]: `old_candidate_universe:pack:stable_top + old_play_card:strategy_card:convergence_box_first:B12` lane=`box_overlap` avg_pool=`1.09375` match_rate=`2.9%`
- `HYP-031` [test_now]: `brain1:dominant_canonicals + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`box_overlap` avg_pool=`1.9589041095890412` match_rate=`2.8%`
- `HYP-032` [test_now]: `old_candidate_universe:pack:stable_top + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` lane=`box_overlap` avg_pool=`1.125` match_rate=`2.8%`
- `HYP-033` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_play_card:strategy_card:convergence_box_first:B24` lane=`box_overlap` avg_pool=`1.121212121212121` match_rate=`2.7%`
- `HYP-034` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` lane=`box_overlap` avg_pool=`1.121212121212121` match_rate=`2.7%`
- `HYP-035` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` lane=`box_overlap` avg_pool=`1.121212121212121` match_rate=`2.7%`
- `HYP-036` [test_as_gate]: `blackapple:recommended_canonicals + old_play_card:strategy_card:convergence_box_first:B24` lane=`box_overlap` avg_pool=`1.0769230769230769` match_rate=`14.3%`
- `HYP-037` [test_as_gate]: `blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` lane=`box_overlap` avg_pool=`1.0769230769230769` match_rate=`14.3%`
- `HYP-038` [test_as_gate]: `blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` lane=`box_overlap` avg_pool=`1.0769230769230769` match_rate=`14.3%`
- `HYP-039` [test_as_gate]: `blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` lane=`box_overlap` avg_pool=`1.0769230769230769` match_rate=`14.3%`
- `HYP-040` [test_as_gate]: `old_candidate_universe:pack:R-perm-4 + shadow_policy:primary_cluster_context` lane=`box_overlap` avg_pool=`1.0` match_rate=`10.0%`

## Guardrail

- These are experiment hypotheses. They are not final scoring weights or budget rules.
