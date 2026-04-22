# Translator Rule Hypothesis Queue

Purpose: queue bounded translator experiments from Stage 2/2B evidence without changing live scoring prematurely.

## Status Mix

- `test_as_gate`: `45`
- `test_now`: `35`
- `watch_only_until_box_confirmed`: `25`
- `negative_control`: `25`
- `pair_before_promotion`: `20`

## Top Hypotheses

- `HYP-001` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B36` lane=`box_overlap` avg_pool=`1.4210526315789473` match_rate=`9.3%`
- `HYP-002` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` lane=`box_overlap` avg_pool=`1.4210526315789473` match_rate=`9.3%`
- `HYP-003` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` lane=`box_overlap` avg_pool=`1.4210526315789473` match_rate=`9.3%`
- `HYP-004` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` lane=`box_overlap` avg_pool=`1.4210526315789473` match_rate=`9.3%`
- `HYP-005` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B36` lane=`box_overlap` avg_pool=`1.4210526315789473` match_rate=`9.3%`
- `HYP-006` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` lane=`box_overlap` avg_pool=`1.4210526315789473` match_rate=`9.3%`
- `HYP-007` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` lane=`box_overlap` avg_pool=`1.4210526315789473` match_rate=`9.3%`
- `HYP-008` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` lane=`box_overlap` avg_pool=`1.4210526315789473` match_rate=`9.3%`
- `HYP-009` [test_now]: `brain1:secondary_canonicals + old_candidate_universe:pack:mirror_pair_closure` lane=`box_overlap` avg_pool=`1.3783783783783783` match_rate=`7.8%`
- `HYP-010` [test_now]: `brain1:secondary_canonicals + old_candidate_universe:pack_method:mirror_pair_closure:canonical` lane=`box_overlap` avg_pool=`1.3783783783783783` match_rate=`7.8%`
- `HYP-011` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:convergence_box_first:B36` lane=`box_overlap` avg_pool=`1.7105263157894737` match_rate=`7.7%`
- `HYP-012` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` lane=`box_overlap` avg_pool=`1.7105263157894737` match_rate=`7.7%`
- `HYP-013` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` lane=`box_overlap` avg_pool=`1.7105263157894737` match_rate=`7.7%`
- `HYP-014` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` lane=`box_overlap` avg_pool=`1.7105263157894737` match_rate=`7.7%`
- `HYP-015` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B12:combos` lane=`box_overlap` avg_pool=`1.358974358974359` match_rate=`7.5%`
- `HYP-016` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:ranked_candidate_canonical` lane=`box_overlap` avg_pool=`1.5405405405405406` match_rate=`7.0%`
- `HYP-017` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:ranked_candidate_combo` lane=`box_overlap` avg_pool=`1.5405405405405406` match_rate=`7.0%`
- `HYP-018` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B36:boxed_canonicals` lane=`box_overlap` avg_pool=`1.6744186046511629` match_rate=`6.9%`
- `HYP-019` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B36:combos` lane=`box_overlap` avg_pool=`1.6744186046511629` match_rate=`6.9%`
- `HYP-020` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:top_canonicals` lane=`box_overlap` avg_pool=`1.40625` match_rate=`6.7%`
- `HYP-021` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_candidate_universe:top_canonicals` lane=`box_overlap` avg_pool=`1.40625` match_rate=`6.7%`
- `HYP-022` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B12:combos` lane=`box_overlap` avg_pool=`1.641025641025641` match_rate=`6.2%`
- `HYP-023` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:v0_2_default:B12:combos` lane=`box_overlap` avg_pool=`1.641025641025641` match_rate=`6.2%`
- `HYP-024` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:analysis_prefix:B12:combos` lane=`box_overlap` avg_pool=`1.641025641025641` match_rate=`6.2%`
- `HYP-025` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:v0_2_default:B12:combos` lane=`box_overlap` avg_pool=`1.641025641025641` match_rate=`6.2%`
- `HYP-026` [test_now]: `old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:conversion_box_first:B36:combos` lane=`box_overlap` avg_pool=`1.5483870967741935` match_rate=`6.2%`
- `HYP-027` [test_now]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy:conversion_box_first:B36:combos` lane=`box_overlap` avg_pool=`1.5483870967741935` match_rate=`6.2%`
- `HYP-028` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B12:combos` lane=`box_overlap` avg_pool=`1.6875` match_rate=`6.2%`
- `HYP-029` [test_now]: `old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:conversion_box_first:B12:combos` lane=`box_overlap` avg_pool=`1.6875` match_rate=`6.2%`
- `HYP-030` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:convergence_box_first:B24` lane=`box_overlap` avg_pool=`1.4` match_rate=`6.1%`
- `HYP-031` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` lane=`box_overlap` avg_pool=`1.4` match_rate=`6.1%`
- `HYP-032` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` lane=`box_overlap` avg_pool=`1.4` match_rate=`6.1%`
- `HYP-033` [test_now]: `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` lane=`box_overlap` avg_pool=`1.4` match_rate=`6.1%`
- `HYP-034` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + positional:positional_canonical` lane=`box_overlap` avg_pool=`1.6341463414634145` match_rate=`6.0%`
- `HYP-035` [test_now]: `old_candidate_universe:pack:mirror_pair_closure + positional:positional_combo` lane=`box_overlap` avg_pool=`1.6341463414634145` match_rate=`6.0%`
- `HYP-036` [test_as_gate]: `old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack:mirror_pair_closure` lane=`box_overlap` avg_pool=`1.2` match_rate=`12.5%`
- `HYP-037` [test_as_gate]: `old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack_method:mirror_pair_closure:canonical` lane=`box_overlap` avg_pool=`1.2` match_rate=`12.5%`
- `HYP-038` [test_as_gate]: `old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:R-perm-4:canonical` lane=`box_overlap` avg_pool=`1.2` match_rate=`12.5%`
- `HYP-039` [test_as_gate]: `old_candidate_universe:pack_method:R-perm-4:canonical + old_candidate_universe:pack_method:mirror_pair_closure:canonical` lane=`box_overlap` avg_pool=`1.2` match_rate=`12.5%`
- `HYP-040` [test_as_gate]: `old_candidate_universe:pack:R-perm-4 + positional:positional_canonical` lane=`box_overlap` avg_pool=`1.4166666666666667` match_rate=`11.8%`

## Guardrail

- These are experiment hypotheses. They are not final scoring weights or budget rules.
