# Stage 2B Cross-Window Stack Rollup

Purpose: separate repeatable translator/stack candidates from one-window noise before any scoring rewrite.

## Executive Read

- The cross-window layer is a confirmation surface, not a live scoring surface.
- Recurring bounded box-overlap stacks are the best replay candidates.
- Recurring VTRAC stacks remain watch/decay unless a bounded box or exact confirmation source proves conversion.
- Recurring negative controls are useful because they define what not to promote.

## Window Coverage

- `WINDOW_2025-12-30_to_2026-01-04`: state_days=`84`, winners=`163`, stage2_exposures=`79778`, stage2b_stacks=`4105`
- `WINDOW_2026-01-05_to_2026-01-09`: state_days=`70`, winners=`138`, stage2_exposures=`71030`, stage2b_stacks=`4006`
- `WINDOW_2026-01-15_to_2026-01-18`: state_days=`56`, winners=`109`, stage2_exposures=`52585`, stage2b_stacks=`4106`
- `WINDOW_2026-01-15_to_2026-01-22`: state_days=`112`, winners=`221`, stage2_exposures=`105332`, stage2b_stacks=`4213`
- `WINDOW_2026-03-09_to_2026-03-23`: state_days=`210`, winners=`414`, stage2_exposures=`211689`, stage2b_stacks=`4025`

## Stack Status Mix

- `cross_window_low_denominator_fixture`: `1314`
- `recurring_negative_control`: `887`
- `watch_or_fixture_only`: `680`
- `cross_window_vtrac_watch_only`: `540`
- `cross_window_boxed_support_gate`: `537`
- `cross_window_boxed_translator_candidate`: `164`
- `single_window_only`: `101`

## Hypothesis Confirmation Mix

- `cross_window_low_denominator_fixture`: `180`
- `recurring_negative_control`: `91`
- `cross_window_vtrac_watch_only`: `87`
- `cross_window_boxed_translator_candidate`: `79`
- `cross_window_boxed_support_gate`: `31`
- `not_in_stack_rollup`: `29`
- `watch_or_fixture_only`: `24`

## Cross-Window Boxed Translator Candidates

- `box_overlap::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack:mirror_pair_closure` windows=`5` avg_pool=`1.3` match_rate=`3.9%` event_support=`0.5%`
- `box_overlap::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:mirror_pair_closure:canonical` windows=`5` avg_pool=`1.3` match_rate=`3.9%` event_support=`0.5%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` windows=`5` avg_pool=`1.3` match_rate=`3.9%` event_support=`0.5%`
- `box_overlap::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_candidate_universe:pack_method:mirror_pair_closure:canonical` windows=`5` avg_pool=`1.3` match_rate=`3.9%` event_support=`0.5%`
- `box_overlap::brain1:secondary_canonicals + old_candidate_universe:pack:mirror_pair_closure` windows=`5` avg_pool=`1.4` match_rate=`3.9%` event_support=`1.3%`
- `box_overlap::brain1:secondary_canonicals + old_candidate_universe:pack_method:mirror_pair_closure:canonical` windows=`5` avg_pool=`1.4` match_rate=`3.9%` event_support=`1.3%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B24` windows=`5` avg_pool=`1.3` match_rate=`3.9%` event_support=`1.5%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` windows=`5` avg_pool=`1.3` match_rate=`3.9%` event_support=`1.5%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` windows=`5` avg_pool=`1.3` match_rate=`3.9%` event_support=`1.5%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` windows=`5` avg_pool=`1.3` match_rate=`3.9%` event_support=`1.5%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B24` windows=`5` avg_pool=`1.3` match_rate=`3.9%` event_support=`1.5%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` windows=`5` avg_pool=`1.3` match_rate=`3.9%` event_support=`1.5%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` windows=`5` avg_pool=`1.3` match_rate=`3.9%` event_support=`1.5%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` windows=`5` avg_pool=`1.3` match_rate=`3.9%` event_support=`1.5%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` windows=`5` avg_pool=`1.4` match_rate=`3.6%` event_support=`1.1%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` windows=`5` avg_pool=`1.4` match_rate=`3.6%` event_support=`1.1%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` windows=`5` avg_pool=`1.1` match_rate=`3.6%` event_support=`0.8%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first:B24` windows=`5` avg_pool=`1.1` match_rate=`3.6%` event_support=`0.8%`
- `box_overlap::old_candidate_universe:pack_method:aux_positional:canonical + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` windows=`5` avg_pool=`1.5` match_rate=`3.4%` event_support=`0.6%`
- `box_overlap::board_scoreboard:top_canonicals + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` windows=`5` avg_pool=`1.2` match_rate=`2.8%` event_support=`0.8%`

## Cross-Window Boxed Support Gates

- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + profit_alerts:implied_canonicals` windows=`5` avg_pool=`1.1` match_rate=`5.3%` event_support=`0.7%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + profit_alerts:implied_canonicals` windows=`5` avg_pool=`1.1` match_rate=`5.3%` event_support=`0.7%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:analysis_prefix:B36:combos` windows=`5` avg_pool=`1.4` match_rate=`2.5%` event_support=`0.8%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:conversion_box_first:B24:combos` windows=`5` avg_pool=`1.3` match_rate=`2.4%` event_support=`0.6%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:conversion_box_first:B36:combos` windows=`5` avg_pool=`1.4` match_rate=`2.1%` event_support=`0.7%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:v0_2_default:B24:combos` windows=`5` avg_pool=`2.7` match_rate=`2.1%` event_support=`2.7%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:v0_2_default:B24:combos` windows=`5` avg_pool=`2.7` match_rate=`2.1%` event_support=`2.7%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:v0_2_default:B36:combos` windows=`5` avg_pool=`2.9` match_rate=`2.0%` event_support=`2.9%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:v0_2_default:B36:combos` windows=`5` avg_pool=`2.9` match_rate=`2.0%` event_support=`2.9%`
- `box_overlap::blackapple:recommended_canonicals + brain1:dominant_canonicals` windows=`5` avg_pool=`1.4` match_rate=`2.0%` event_support=`0.7%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + positional:positional_canonical` windows=`5` avg_pool=`1.7` match_rate=`2.0%` event_support=`1.1%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + positional:positional_combo` windows=`5` avg_pool=`1.7` match_rate=`2.0%` event_support=`1.1%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + positional:positional_canonical` windows=`5` avg_pool=`1.7` match_rate=`2.0%` event_support=`1.1%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + positional:positional_combo` windows=`5` avg_pool=`1.7` match_rate=`2.0%` event_support=`1.1%`
- `box_overlap::blackapple:recommended_canonicals + survivor:survivor_frontier_canonicals` windows=`5` avg_pool=`1.5` match_rate=`2.0%` event_support=`0.6%`
- `box_overlap::old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12 + profit_alerts:implied_canonicals` windows=`5` avg_pool=`1.2` match_rate=`2.0%` event_support=`0.6%`
- `box_overlap::brain1:secondary_canonicals + positional:positional_canonical` windows=`5` avg_pool=`1.4` match_rate=`2.0%` event_support=`0.8%`
- `box_overlap::brain1:secondary_canonicals + positional:positional_combo` windows=`5` avg_pool=`1.4` match_rate=`2.0%` event_support=`0.8%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:aux_positional:canonical` windows=`5` avg_pool=`1.7` match_rate=`2.0%` event_support=`1.3%`
- `box_overlap::old_candidate_universe:pack_method:aux_positional:canonical + old_candidate_universe:pack_method:mirror_pair_closure:canonical` windows=`5` avg_pool=`1.7` match_rate=`2.0%` event_support=`1.3%`

## Cross-Window VTRAC Watch Only

- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack:mirror_pair_closure` windows=`5` avg_pool=`1.1` match_rate=`12.6%` event_support=`1.2%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:mirror_pair_closure:canonical` windows=`5` avg_pool=`1.1` match_rate=`12.6%` event_support=`1.2%`
- `vtrac_box_confirmation::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` windows=`5` avg_pool=`1.1` match_rate=`12.6%` event_support=`1.2%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_candidate_universe:pack_method:mirror_pair_closure:canonical` windows=`5` avg_pool=`1.1` match_rate=`12.6%` event_support=`1.2%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + positional:positional_canonical` windows=`5` avg_pool=`1.0` match_rate=`11.0%` event_support=`0.8%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + positional:positional_combo` windows=`5` avg_pool=`1.0` match_rate=`11.0%` event_support=`0.8%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + profit_alerts:top_profit_alerts` windows=`5` avg_pool=`1.2` match_rate=`10.6%` event_support=`4.4%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + profit_alerts:implied_canonicals` windows=`5` avg_pool=`1.2` match_rate=`10.3%` event_support=`4.4%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` windows=`5` avg_pool=`1.1` match_rate=`9.9%` event_support=`2.6%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` windows=`5` avg_pool=`1.1` match_rate=`9.9%` event_support=`2.6%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:aux_positional:canonical` windows=`5` avg_pool=`1.0` match_rate=`9.9%` event_support=`0.8%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + positional:positional_canonical` windows=`5` avg_pool=`1.1` match_rate=`9.8%` event_support=`1.1%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + positional:positional_combo` windows=`5` avg_pool=`1.1` match_rate=`9.8%` event_support=`1.1%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` windows=`5` avg_pool=`1.1` match_rate=`9.5%` event_support=`2.6%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + shadow_policy:primary_cluster_context` windows=`5` avg_pool=`1.5` match_rate=`9.4%` event_support=`6.0%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy:analysis_prefix:B24:boxed_canonicals` windows=`5` avg_pool=`1.1` match_rate=`9.4%` event_support=`1.2%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:analysis_prefix:B24` windows=`5` avg_pool=`1.1` match_rate=`9.4%` event_support=`1.2%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:convergence_box_first:B36` windows=`5` avg_pool=`1.6` match_rate=`9.2%` event_support=`6.2%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` windows=`5` avg_pool=`1.6` match_rate=`9.2%` event_support=`6.2%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` windows=`5` avg_pool=`1.6` match_rate=`9.2%` event_support=`6.2%`

## Recurring Negative Controls

- `box_overlap::old_play_card:strategy:analysis_prefix:B36:boxed_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` windows=`5` avg_pool=`2.7` match_rate=`1.0%` event_support=`1.3%`
- `box_overlap::board_scoreboard:top_canonicals + brain1:context_reinforced_canonicals` windows=`5` avg_pool=`2.3` match_rate=`1.0%` event_support=`1.1%`
- `box_overlap::board_scoreboard:top_canonicals + shadow_policy:primary_cluster_context` windows=`5` avg_pool=`2.3` match_rate=`1.0%` event_support=`1.1%`
- `box_overlap::old_candidate_universe:pack_method:hot_zones_top:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals` windows=`5` avg_pool=`1.8` match_rate=`1.0%` event_support=`0.7%`
- `box_overlap::old_candidate_universe:pack_method:PackA_vt8:canonical + old_play_card:ranked_candidate_canonical` windows=`5` avg_pool=`2.2` match_rate=`1.0%` event_support=`0.5%`
- `box_overlap::old_candidate_universe:pack_method:PackA_vt8:canonical + old_play_card:ranked_candidate_combo` windows=`5` avg_pool=`2.2` match_rate=`1.0%` event_support=`0.5%`
- `box_overlap::old_play_card:strategy:conversion_box_first:B12:combos + shadow_policy:primary_cluster_canonicals` windows=`5` avg_pool=`1.6` match_rate=`1.0%` event_support=`0.7%`
- `box_overlap::old_play_card:strategy:conversion_box_first:B24:combos + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` windows=`5` avg_pool=`3.0` match_rate=`1.0%` event_support=`1.5%`
- `box_overlap::old_candidate_universe:pack_method:PackA_vt8:canonical + old_candidate_universe:top_canonicals` windows=`5` avg_pool=`2.4` match_rate=`1.0%` event_support=`1.1%`
- `box_overlap::old_play_card:ranked_candidate_canonical + old_play_card:strategy:play_box_first:B24:boxed_canonicals` windows=`5` avg_pool=`5.7` match_rate=`1.0%` event_support=`2.9%`
- `box_overlap::old_play_card:ranked_candidate_combo + old_play_card:strategy:play_box_first:B24:boxed_canonicals` windows=`5` avg_pool=`5.7` match_rate=`1.0%` event_support=`2.9%`
- `box_overlap::old_play_card:ranked_candidate_canonical + old_play_card:strategy:play_box_first:B24:combos` windows=`5` avg_pool=`5.7` match_rate=`1.0%` event_support=`2.9%`
- `box_overlap::old_play_card:ranked_candidate_combo + old_play_card:strategy:play_box_first:B24:combos` windows=`5` avg_pool=`5.7` match_rate=`1.0%` event_support=`2.9%`
- `box_overlap::old_play_card:strategy_card:analysis_prefix:B36 + old_play_card:strategy_card:convergence_box_first:B12` windows=`5` avg_pool=`2.7` match_rate=`1.0%` event_support=`1.3%`
- `box_overlap::brain1:dominant_canonicals + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals` windows=`5` avg_pool=`3.0` match_rate=`1.0%` event_support=`1.4%`
- `box_overlap::old_play_card:strategy:conversion_box_first:B24:combos + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` windows=`5` avg_pool=`3.0` match_rate=`1.0%` event_support=`1.5%`
- `box_overlap::old_candidate_universe:pack:stable_top + old_play_card:strategy:conversion_box_first:B24:combos` windows=`5` avg_pool=`3.7` match_rate=`1.0%` event_support=`1.6%`
- `box_overlap::board_scoreboard:top_canonicals + translation_sandbox:diagnostic_boxed_seed` windows=`5` avg_pool=`3.4` match_rate=`1.0%` event_support=`1.7%`
- `box_overlap::old_play_card:strategy_card:convergence_box_first:B24 + profit_alerts:top_profit_alerts` windows=`5` avg_pool=`1.4` match_rate=`1.0%` event_support=`0.5%`
- `box_overlap::old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24 + profit_alerts:top_profit_alerts` windows=`5` avg_pool=`1.4` match_rate=`1.0%` event_support=`0.5%`

## Cross-Window Low-Denominator Fixtures

- `vtrac_box_confirmation::old_candidate_universe:pack:aux_positional + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` windows=`5` avg_pool=`1.1` match_rate=`13.3%` event_support=`0.4%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:consensus_double_9:canonical` windows=`5` avg_pool=`1.2` match_rate=`12.5%` event_support=`0.6%`
- `vtrac_box_confirmation::board_scoreboard:top_vtrac_indices + old_candidate_universe:pack:PackB_mirror3rd` windows=`5` avg_pool=`1.0` match_rate=`9.3%` event_support=`0.4%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:boxed_canonicals` windows=`5` avg_pool=`1.0` match_rate=`8.7%` event_support=`0.2%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:v0_2_default:B12:boxed_canonicals` windows=`5` avg_pool=`1.0` match_rate=`8.7%` event_support=`0.2%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:analysis_prefix:B12` windows=`5` avg_pool=`1.0` match_rate=`8.7%` event_support=`0.2%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + shadow_policy:primary_cluster_context` windows=`5` avg_pool=`1.0` match_rate=`7.4%` event_support=`0.4%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + profit_alerts:implied_canonicals` windows=`5` avg_pool=`1.0` match_rate=`7.3%` event_support=`0.3%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + profit_alerts:top_profit_alerts` windows=`5` avg_pool=`1.0` match_rate=`7.3%` event_support=`0.3%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + survivor:survivor_frontier_canonicals` windows=`5` avg_pool=`1.0` match_rate=`6.4%` event_support=`0.3%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + shadow_policy:primary_cluster_survivor_frontier` windows=`5` avg_pool=`1.1` match_rate=`6.2%` event_support=`0.1%`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` windows=`5` avg_pool=`1.0` match_rate=`6.1%` event_support=`0.3%`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:strategy_card:analysis_prefix:B36` windows=`5` avg_pool=`1.0` match_rate=`6.1%` event_support=`0.3%`
- `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` windows=`5` avg_pool=`1.0` match_rate=`6.1%` event_support=`0.3%`
- `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:strategy_card:analysis_prefix:B36` windows=`5` avg_pool=`1.0` match_rate=`6.1%` event_support=`0.3%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:hot_zones_top:canonical` windows=`5` avg_pool=`1.0` match_rate=`5.9%` event_support=`0.4%`
- `box_overlap::old_candidate_universe:pack:aux_positional + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` windows=`5` avg_pool=`1.2` match_rate=`5.7%` event_support=`0.2%`
- `vtrac_box_confirmation::board_scoreboard:top_canonicals + old_candidate_universe:pack:aux_vtrac_index_overdue` windows=`5` avg_pool=`1.0` match_rate=`5.6%` event_support=`0.4%`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack:PackB_mirror3rd` windows=`5` avg_pool=`1.0` match_rate=`5.4%` event_support=`0.4%`
- `vtrac_overlap::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` windows=`5` avg_pool=`1.1` match_rate=`5.4%` event_support=`0.3%`

## Stable Source Surfaces

- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` windows=`5` lane=`vtrac` lane_rate=`8.1%` event_support=`13.9%` decisions=`vtrac_context_only:5`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` windows=`5` lane=`vtrac` lane_rate=`6.6%` event_support=`3.0%` decisions=`vtrac_context_only:5`
- `board_scoreboard:top_vtrac_indices` windows=`5` lane=`vtrac` lane_rate=`6.5%` event_support=`13.5%` decisions=`vtrac_context_only:5`
- `translation_sandbox:diagnostic_vt_box_seed` windows=`5` lane=`vtrac` lane_rate=`6.2%` event_support=`38.4%` decisions=`vtrac_watch_decay_only_until_box_pairing:4|vtrac_context_only:1`
- `brain1:watchlist_indices` windows=`5` lane=`vtrac` lane_rate=`6.2%` event_support=`19.1%` decisions=`vtrac_context_only:5`
- `brain1:dominant_vtrac_indices` windows=`5` lane=`vtrac` lane_rate=`6.1%` event_support=`26.7%` decisions=`vtrac_context_only:5`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` windows=`5` lane=`vtrac` lane_rate=`2.9%` event_support=`4.0%` decisions=`vtrac_context_only:5`
- `old_candidate_universe:pack:mirror_pair_closure` windows=`5` lane=`boxed` lane_rate=`1.6%` event_support=`14.6%` decisions=`boxed_context_or_negative_control:3|boxed_supporting_gate:2`
- `old_candidate_universe:pack_method:mirror_pair_closure:canonical` windows=`5` lane=`boxed` lane_rate=`1.6%` event_support=`14.6%` decisions=`boxed_context_or_negative_control:3|boxed_supporting_gate:2`
- `old_candidate_universe:pack:R-perm-4` windows=`5` lane=`boxed` lane_rate=`1.3%` event_support=`10.3%` decisions=`boxed_context_or_negative_control:5`
- `old_candidate_universe:pack_method:R-perm-4:canonical` windows=`5` lane=`boxed` lane_rate=`1.3%` event_support=`10.3%` decisions=`boxed_context_or_negative_control:5`
- `old_play_card:strategy:play_box_first:B24:boxed_canonicals` windows=`5` lane=`boxed` lane_rate=`1.1%` event_support=`14.4%` decisions=`boxed_context_or_negative_control:4|boxed_supporting_gate:1`
- `old_play_card:strategy_card:convergence_box_first:B24` windows=`5` lane=`boxed` lane_rate=`1.1%` event_support=`14.2%` decisions=`boxed_context_or_negative_control:5`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` windows=`5` lane=`boxed` lane_rate=`1.1%` event_support=`14.2%` decisions=`boxed_context_or_negative_control:5`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` windows=`5` lane=`boxed` lane_rate=`1.1%` event_support=`14.2%` decisions=`boxed_context_or_negative_control:5`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` windows=`5` lane=`boxed` lane_rate=`1.1%` event_support=`14.2%` decisions=`boxed_context_or_negative_control:5`
- `old_play_card:strategy:play_box_first:B36:boxed_canonicals` windows=`5` lane=`boxed` lane_rate=`1.1%` event_support=`19.0%` decisions=`boxed_context_or_negative_control:4|boxed_supporting_gate:1`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` windows=`5` lane=`boxed` lane_rate=`1.1%` event_support=`7.9%` decisions=`boxed_context_or_negative_control:4|boxed_supporting_gate:1`
- `blackapple:recommended_canonicals` windows=`5` lane=`boxed` lane_rate=`1.1%` event_support=`23.0%` decisions=`boxed_supporting_gate:4|boxed_context_or_negative_control:1`
- `old_play_card:strategy_card:conversion_box_first:B36` windows=`5` lane=`boxed` lane_rate=`1.1%` event_support=`16.1%` decisions=`boxed_context_or_negative_control:5`

## Generated Files

- Stack confirmation CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_STACK_CONFIRMATION.csv`
- Hypothesis confirmation CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_HYPOTHESIS_CONFIRMATION.csv`
- Source confirmation CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_SOURCE_CONFIRMATION.csv`
- Rollup JSON: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_STACK_ROLLUP.json`

## Guardrail

- A cross-window candidate is only permission to replay against fixtures. It is not a permission to alter live scoring or budgeting.
