# Stage 2B Signal Stack Scorecard

Purpose: identify which signal combinations are sharper than individual sources.

## Denominators

- Full pair/state-day denominator rows: `241384`
- Exported drill-down ledger rows: `12054`
- Stack scorecard rows: `4105`

## Decision Mix

- `negative_control_stack`: `2371`
- `boxed_support_stack`: `553`
- `vtrac_context_stack`: `338`
- `boxed_translator_stack_candidate`: `246`
- `sample_too_small_stack`: `209`
- `context_stack`: `208`
- `vtrac_box_confirmation_watch`: `180`

## Boxed Translator Candidates

- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` active=`31` avg_pool=`1.4` match_rate=`6.8%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` active=`31` avg_pool=`1.4` match_rate=`6.8%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack:PackB_mirror3rd + old_candidate_universe:pack:R-perm-4` active=`37` avg_pool=`1.0` match_rate=`5.4%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack:PackB_mirror3rd + old_candidate_universe:pack_method:R-perm-4:canonical` active=`37` avg_pool=`1.0` match_rate=`5.4%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::brain1:secondary_canonicals + old_candidate_universe:pack:mirror_pair_closure` active=`40` avg_pool=`1.4` match_rate=`5.4%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::brain1:secondary_canonicals + old_candidate_universe:pack_method:mirror_pair_closure:canonical` active=`40` avg_pool=`1.4` match_rate=`5.4%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::blackapple:recommended_canonicals + brain1:dominant_canonicals` active=`41` avg_pool=`1.4` match_rate=`5.2%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::blackapple:recommended_canonicals + brain1:context_reinforced_canonicals` active=`32` avg_pool=`1.2` match_rate=`5.1%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:budgeted_canonicals_top` active=`54` avg_pool=`1.4` match_rate=`5.1%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B36:boxed_canonicals` active=`48` avg_pool=`1.4` match_rate=`4.5%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B36:combos` active=`48` avg_pool=`1.4` match_rate=`4.5%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack_method:PackB_mirror3rd:canonical` active=`47` avg_pool=`1.0` match_rate=`4.3%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack_method:PackB_mirror3rd:canonical + old_candidate_universe:pack_method:R-perm-4:canonical` active=`47` avg_pool=`1.0` match_rate=`4.3%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:analysis_prefix:B36:combos` active=`33` avg_pool=`1.5` match_rate=`3.9%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B12:combos` active=`45` avg_pool=`1.2` match_rate=`3.6%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B24:combos` active=`58` avg_pool=`1.4` match_rate=`3.6%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:convergence_box_first:B36` active=`47` avg_pool=`1.2` match_rate=`3.5%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` active=`47` avg_pool=`1.2` match_rate=`3.5%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` active=`47` avg_pool=`1.2` match_rate=`3.5%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` active=`47` avg_pool=`1.2` match_rate=`3.5%` event_support=`0.0%` decision=`boxed_translator_stack_candidate`

## Boxed Support Stacks

- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:convergence_box_first:B24` active=`13` avg_pool=`1.1` match_rate=`14.3%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` active=`13` avg_pool=`1.1` match_rate=`14.3%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` active=`13` avg_pool=`1.1` match_rate=`14.3%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` active=`13` avg_pool=`1.1` match_rate=`14.3%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + shadow_policy:primary_cluster_context` active=`10` avg_pool=`1.0` match_rate=`10.0%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + shadow_policy:primary_cluster_context` active=`10` avg_pool=`1.0` match_rate=`10.0%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack:stable_top` active=`11` avg_pool=`1.0` match_rate=`9.1%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` active=`11` avg_pool=`1.0` match_rate=`9.1%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` active=`11` avg_pool=`1.0` match_rate=`9.1%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` active=`11` avg_pool=`1.0` match_rate=`9.1%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` active=`11` avg_pool=`1.0` match_rate=`9.1%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` active=`11` avg_pool=`1.0` match_rate=`9.1%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` active=`11` avg_pool=`1.0` match_rate=`9.1%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:convergence_box_first:B36` active=`18` avg_pool=`1.2` match_rate=`9.1%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` active=`18` avg_pool=`1.2` match_rate=`9.1%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` active=`18` avg_pool=`1.2` match_rate=`9.1%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` active=`18` avg_pool=`1.2` match_rate=`9.1%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::blackapple:recommended_canonicals + shadow_policy:primary_cluster_context` active=`24` avg_pool=`1.0` match_rate=`8.3%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::blackapple:recommended_canonicals + old_candidate_universe:pack_method:stable_top:canonical` active=`11` avg_pool=`1.1` match_rate=`8.3%` event_support=`0.0%` decision=`boxed_support_stack`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack:stable_top` active=`13` avg_pool=`1.0` match_rate=`7.7%` event_support=`0.0%` decision=`boxed_support_stack`

## VTRAC Confirmation Watch

- `vtrac_box_confirmation::old_candidate_universe:pack:PackB_mirror3rd + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` active=`16` avg_pool=`1.0` match_rate=`18.8%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::board_scoreboard:top_canonicals + old_candidate_universe:pack:aux_vtrac_index_overdue` active=`12` avg_pool=`1.0` match_rate=`16.7%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack:PackB_mirror3rd + translation_sandbox:diagnostic_vt_box_seed` active=`36` avg_pool=`1.0` match_rate=`16.7%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:hot_zones_top:canonical` active=`12` avg_pool=`1.0` match_rate=`16.7%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + shadow_policy:primary_cluster_context` active=`12` avg_pool=`1.0` match_rate=`16.7%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackA_vt8:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` active=`18` avg_pool=`1.0` match_rate=`16.7%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackB_mirror3rd:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` active=`18` avg_pool=`1.0` match_rate=`16.7%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:pack:PackB_mirror3rd` active=`15` avg_pool=`1.0` match_rate=`13.3%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::brain1:context_reinforced_canonicals + old_candidate_universe:pack:aux_vtrac_index_overdue` active=`15` avg_pool=`1.1` match_rate=`12.5%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + translation_sandbox:diagnostic_boxed_seed` active=`32` avg_pool=`1.0` match_rate=`12.1%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + shadow_policy:primary_cluster_canonicals` active=`17` avg_pool=`1.0` match_rate=`11.8%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackA_vt8:canonical + translation_sandbox:diagnostic_vt_box_seed` active=`53` avg_pool=`1.0` match_rate=`11.3%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackB_mirror3rd:canonical + translation_sandbox:diagnostic_vt_box_seed` active=`53` avg_pool=`1.0` match_rate=`11.3%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + survivor:survivor_frontier_canonicals` active=`41` avg_pool=`1.5` match_rate=`11.3%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::brain1:dominant_canonicals + old_candidate_universe:pack:aux_vtrac_index_overdue` active=`18` avg_pool=`1.0` match_rate=`11.1%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:convergence_box_first:B36` active=`60` avg_pool=`1.5` match_rate=`10.9%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` active=`60` avg_pool=`1.5` match_rate=`10.9%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` active=`60` avg_pool=`1.5` match_rate=`10.9%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` active=`60` avg_pool=`1.5` match_rate=`10.9%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + shadow_policy:primary_cluster_context` active=`15` avg_pool=`1.3` match_rate=`10.5%` event_support=`0.0%` decision=`vtrac_box_confirmation_watch`

## Straight Stack Probes

- None in this window.

## Negative Controls

- `box_overlap::shadow_policy:primary_cluster_canonicals + translation_sandbox:diagnostic_boxed_seed` active=`84` avg_pool=`4.8` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::board_scoreboard:top_canonicals + old_play_card:strategy:v0_2_default:B24:combos` active=`81` avg_pool=`2.5` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` active=`84` avg_pool=`2.4` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` active=`84` avg_pool=`2.4` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:strategy_card:conversion_box_first:B12 + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` active=`84` avg_pool=`2.4` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:strategy_card:conversion_box_first:B12 + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` active=`84` avg_pool=`2.4` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:ranked_candidate_canonical + old_play_card:strategy:v0_2_default:B24:combos` active=`84` avg_pool=`7.2` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:ranked_candidate_combo + old_play_card:strategy:v0_2_default:B24:combos` active=`84` avg_pool=`7.2` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_candidate_universe:pack:stable_top + old_play_card:strategy:v0_2_default:B36:combos` active=`56` avg_pool=`3.6` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_candidate_universe:candidate_universe_union_combo + old_play_card:ranked_candidate_canonical` active=`84` avg_pool=`7.3` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_candidate_universe:candidate_universe_union_combo + old_play_card:ranked_candidate_combo` active=`84` avg_pool=`7.3` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:ranked_candidate_canonical + old_play_card:ranked_candidate_combo` active=`84` avg_pool=`7.3` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:ranked_candidate_canonical + old_play_card:strategy:analysis_prefix:B24:combos` active=`84` avg_pool=`7.3` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:ranked_candidate_canonical + old_play_card:strategy:analysis_prefix:B36:combos` active=`84` avg_pool=`7.3` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:ranked_candidate_canonical + old_play_card:strategy:v0_2_default:B36:combos` active=`84` avg_pool=`7.3` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:ranked_candidate_combo + old_play_card:strategy:analysis_prefix:B24:combos` active=`84` avg_pool=`7.3` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:ranked_candidate_combo + old_play_card:strategy:analysis_prefix:B36:combos` active=`84` avg_pool=`7.3` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:ranked_candidate_combo + old_play_card:strategy:v0_2_default:B36:combos` active=`84` avg_pool=`7.3` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_candidate_universe:candidate_universe_union_combo + old_candidate_universe:pack_method:aux_positional:canonical` active=`84` avg_pool=`9.7` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`
- `box_overlap::old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` active=`84` avg_pool=`2.5` match_rate=`0.5%` event_support=`0.0%` decision=`negative_control_stack`

## Read

- Stack candidates are experiment inputs, not live-scoring weights.
- VTRAC confirmation stacks remain watch/decay unless paired with bounded boxed overlap.
- Negative-control stacks are valuable because they prevent broad over-promotion.
