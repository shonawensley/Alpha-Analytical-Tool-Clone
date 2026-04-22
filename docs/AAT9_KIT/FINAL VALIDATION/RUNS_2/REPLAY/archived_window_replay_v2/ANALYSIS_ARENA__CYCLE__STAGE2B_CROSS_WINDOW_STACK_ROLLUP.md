# Stage 2B Cross-Window Stack Rollup

Purpose: separate repeatable translator/stack candidates from one-window noise before any scoring rewrite.

## Executive Read

- The cross-window layer is a confirmation surface, not a live scoring surface.
- Recurring bounded box-overlap stacks are the best replay candidates.
- Recurring VTRAC stacks remain watch/decay unless a bounded box or exact confirmation source proves conversion.
- Recurring negative controls are useful because they define what not to promote.

## Window Coverage

- `WINDOW_2025-12-30_to_2026-01-09`: state_days=`154`, winners=`301`, stage2_exposures=`156360`, stage2b_stacks=`4028`
- `WINDOW_2026-01-15_to_2026-01-18`: state_days=`56`, winners=`109`, stage2_exposures=`56657`, stage2b_stacks=`3922`
- `WINDOW_2026-01-20_to_2026-01-22`: state_days=`42`, winners=`84`, stage2_exposures=`42685`, stage2b_stacks=`3904`

## Stack Status Mix

- `cross_window_low_denominator_fixture`: `1736`
- `watch_or_fixture_only`: `782`
- `cross_window_vtrac_watch_only`: `486`
- `recurring_negative_control`: `393`
- `cross_window_boxed_support_gate`: `387`
- `cross_window_boxed_translator_candidate`: `147`
- `single_window_only`: `101`

## Hypothesis Confirmation Mix

- `cross_window_low_denominator_fixture`: `130`
- `cross_window_boxed_translator_candidate`: `70`
- `recurring_negative_control`: `61`
- `cross_window_vtrac_watch_only`: `54`
- `not_in_stack_rollup`: `26`
- `watch_or_fixture_only`: `16`
- `cross_window_boxed_support_gate`: `9`
- `single_window_only`: `5`

## Cross-Window Boxed Translator Candidates

- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack:mirror_pair_closure` windows=`3` avg_pool=`1.3` match_rate=`5.3%` event_support=`1.2%`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack_method:mirror_pair_closure:canonical` windows=`3` avg_pool=`1.3` match_rate=`5.3%` event_support=`1.2%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:R-perm-4:canonical` windows=`3` avg_pool=`1.3` match_rate=`5.3%` event_support=`1.2%`
- `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + old_candidate_universe:pack_method:mirror_pair_closure:canonical` windows=`3` avg_pool=`1.3` match_rate=`5.3%` event_support=`1.2%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:convergence_box_first:B36` windows=`3` avg_pool=`1.4` match_rate=`4.2%` event_support=`1.8%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` windows=`3` avg_pool=`1.4` match_rate=`4.2%` event_support=`1.8%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` windows=`3` avg_pool=`1.4` match_rate=`4.2%` event_support=`1.8%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` windows=`3` avg_pool=`1.4` match_rate=`4.2%` event_support=`1.8%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:convergence_box_first:B36` windows=`3` avg_pool=`1.4` match_rate=`4.2%` event_support=`1.8%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` windows=`3` avg_pool=`1.4` match_rate=`4.2%` event_support=`1.8%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` windows=`3` avg_pool=`1.4` match_rate=`4.2%` event_support=`1.8%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` windows=`3` avg_pool=`1.4` match_rate=`4.2%` event_support=`1.8%`
- `box_overlap::blackapple:recommended_canonicals + old_play_card:strategy:analysis_prefix:B36:combos` windows=`3` avg_pool=`1.4` match_rate=`4.2%` event_support=`1.2%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` windows=`3` avg_pool=`1.4` match_rate=`4.2%` event_support=`1.2%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` windows=`3` avg_pool=`1.4` match_rate=`4.2%` event_support=`1.2%`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:ranked_candidate_canonical` windows=`3` avg_pool=`1.2` match_rate=`4.1%` event_support=`1.2%`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:ranked_candidate_combo` windows=`3` avg_pool=`1.2` match_rate=`4.1%` event_support=`1.2%`
- `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:ranked_candidate_canonical` windows=`3` avg_pool=`1.2` match_rate=`4.1%` event_support=`1.2%`
- `box_overlap::old_candidate_universe:pack_method:R-perm-4:canonical + old_play_card:ranked_candidate_combo` windows=`3` avg_pool=`1.2` match_rate=`4.1%` event_support=`1.2%`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:conversion_box_first:B12:combos` windows=`3` avg_pool=`1.2` match_rate=`4.0%` event_support=`1.0%`

## Cross-Window Boxed Support Gates

- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:v0_2_default:B24:combos` windows=`3` avg_pool=`2.5` match_rate=`2.4%` event_support=`2.8%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:v0_2_default:B24:combos` windows=`3` avg_pool=`2.5` match_rate=`2.4%` event_support=`2.8%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B36:combos` windows=`3` avg_pool=`2.7` match_rate=`2.1%` event_support=`2.8%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:analysis_prefix:B36:combos` windows=`3` avg_pool=`2.7` match_rate=`2.1%` event_support=`2.8%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:v0_2_default:B36:combos` windows=`3` avg_pool=`2.8` match_rate=`2.1%` event_support=`2.8%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:v0_2_default:B36:combos` windows=`3` avg_pool=`2.8` match_rate=`2.1%` event_support=`2.8%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B24:combos` windows=`3` avg_pool=`2.6` match_rate=`2.1%` event_support=`2.6%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:conversion_box_first:B24:combos` windows=`3` avg_pool=`2.6` match_rate=`2.1%` event_support=`2.6%`
- `box_overlap::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:top_canonicals` windows=`3` avg_pool=`2.7` match_rate=`2.0%` event_support=`1.2%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:v0_2_default:B36:combos` windows=`3` avg_pool=`2.5` match_rate=`2.0%` event_support=`2.4%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + positional:positional_canonical` windows=`3` avg_pool=`1.6` match_rate=`1.9%` event_support=`1.0%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + positional:positional_combo` windows=`3` avg_pool=`1.6` match_rate=`1.9%` event_support=`1.0%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + positional:positional_canonical` windows=`3` avg_pool=`1.6` match_rate=`1.9%` event_support=`1.0%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + positional:positional_combo` windows=`3` avg_pool=`1.6` match_rate=`1.9%` event_support=`1.0%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + translation_sandbox:diagnostic_boxed_seed` windows=`3` avg_pool=`1.9` match_rate=`1.9%` event_support=`1.6%`
- `box_overlap::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_play_card:strategy:play_box_first:B36:boxed_canonicals` windows=`3` avg_pool=`2.1` match_rate=`1.9%` event_support=`1.0%`
- `box_overlap::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_play_card:strategy:play_box_first:B36:combos` windows=`3` avg_pool=`2.1` match_rate=`1.9%` event_support=`1.0%`
- `box_overlap::brain1:dominant_canonicals + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` windows=`3` avg_pool=`2.0` match_rate=`1.9%` event_support=`1.6%`
- `box_overlap::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy:analysis_prefix:B36:combos` windows=`3` avg_pool=`2.5` match_rate=`1.8%` event_support=`1.2%`
- `box_overlap::old_candidate_universe:pack:R-perm-4 + old_play_card:strategy:v0_2_default:B36:combos` windows=`3` avg_pool=`2.8` match_rate=`1.8%` event_support=`2.6%`

## Cross-Window VTRAC Watch Only

- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack:mirror_pair_closure` windows=`3` avg_pool=`1.1` match_rate=`13.6%` event_support=`1.6%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:mirror_pair_closure:canonical` windows=`3` avg_pool=`1.1` match_rate=`13.6%` event_support=`1.6%`
- `vtrac_box_confirmation::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` windows=`3` avg_pool=`1.1` match_rate=`13.6%` event_support=`1.6%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_candidate_universe:pack_method:mirror_pair_closure:canonical` windows=`3` avg_pool=`1.1` match_rate=`13.6%` event_support=`1.6%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackA_vt8:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` windows=`3` avg_pool=`1.0` match_rate=`12.3%` event_support=`1.4%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackB_mirror3rd:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` windows=`3` avg_pool=`1.0` match_rate=`12.3%` event_support=`1.4%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` windows=`3` avg_pool=`1.1` match_rate=`11.8%` event_support=`3.2%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` windows=`3` avg_pool=`1.1` match_rate=`11.8%` event_support=`3.2%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` windows=`3` avg_pool=`1.1` match_rate=`11.0%` event_support=`3.2%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:convergence_box_first:B12` windows=`3` avg_pool=`1.1` match_rate=`10.3%` event_support=`3.2%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + profit_alerts:top_profit_alerts` windows=`3` avg_pool=`1.2` match_rate=`10.3%` event_support=`4.0%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + profit_alerts:implied_canonicals` windows=`3` avg_pool=`1.2` match_rate=`10.1%` event_support=`4.0%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:convergence_box_first:B36` windows=`3` avg_pool=`1.7` match_rate=`9.9%` event_support=`7.5%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` windows=`3` avg_pool=`1.7` match_rate=`9.9%` event_support=`7.5%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` windows=`3` avg_pool=`1.7` match_rate=`9.9%` event_support=`7.5%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` windows=`3` avg_pool=`1.7` match_rate=`9.9%` event_support=`7.5%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` windows=`3` avg_pool=`1.1` match_rate=`9.7%` event_support=`1.4%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` windows=`3` avg_pool=`1.1` match_rate=`9.7%` event_support=`1.4%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:combos` windows=`3` avg_pool=`1.4` match_rate=`9.6%` event_support=`4.7%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:v0_2_default:B12:combos` windows=`3` avg_pool=`1.4` match_rate=`9.6%` event_support=`4.7%`

## Recurring Negative Controls

- `box_overlap::old_play_card:strategy:v0_2_default:B36:combos + shadow_policy:primary_cluster_context` windows=`3` avg_pool=`2.8` match_rate=`1.0%` event_support=`1.4%`
- `box_overlap::brain1:secondary_canonicals + old_play_card:strategy:v0_2_default:B36:combos` windows=`3` avg_pool=`4.0` match_rate=`1.0%` event_support=`2.0%`
- `box_overlap::old_play_card:strategy:conversion_box_first:B24:boxed_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` windows=`3` avg_pool=`2.8` match_rate=`1.0%` event_support=`1.4%`
- `box_overlap::old_play_card:strategy_card:conversion_box_first:B24 + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` windows=`3` avg_pool=`2.8` match_rate=`1.0%` event_support=`1.4%`
- `box_overlap::old_play_card:strategy:conversion_box_first:B24:boxed_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` windows=`3` avg_pool=`2.8` match_rate=`1.0%` event_support=`1.4%`
- `box_overlap::old_play_card:strategy_card:conversion_box_first:B24 + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` windows=`3` avg_pool=`2.8` match_rate=`1.0%` event_support=`1.4%`
- `box_overlap::brain1:dominant_canonicals + old_play_card:strategy:v0_2_default:B36:combos` windows=`3` avg_pool=`6.4` match_rate=`1.0%` event_support=`3.2%`
- `box_overlap::old_play_card:strategy:analysis_prefix:B24:combos + translation_sandbox:diagnostic_straight_seed` windows=`3` avg_pool=`6.0` match_rate=`1.0%` event_support=`3.0%`
- `box_overlap::old_play_card:strategy:analysis_prefix:B12:combos + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` windows=`3` avg_pool=`2.8` match_rate=`1.0%` event_support=`1.4%`
- `box_overlap::old_play_card:strategy:v0_2_default:B12:combos + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` windows=`3` avg_pool=`2.8` match_rate=`1.0%` event_support=`1.4%`
- `box_overlap::old_play_card:strategy:analysis_prefix:B24:boxed_canonicals + old_play_card:strategy_card:convergence_box_first:B12` windows=`3` avg_pool=`2.4` match_rate=`1.0%` event_support=`1.2%`
- `box_overlap::old_play_card:strategy_card:analysis_prefix:B24 + old_play_card:strategy_card:convergence_box_first:B12` windows=`3` avg_pool=`2.4` match_rate=`1.0%` event_support=`1.2%`
- `box_overlap::old_play_card:strategy:analysis_prefix:B24:combos + old_play_card:strategy_card:convergence_box_first:B12` windows=`3` avg_pool=`3.2` match_rate=`1.0%` event_support=`1.6%`
- `box_overlap::old_play_card:strategy:analysis_prefix:B24:combos + translation_sandbox:diagnostic_boxed_seed` windows=`3` avg_pool=`6.9` match_rate=`1.0%` event_support=`3.4%`
- `box_overlap::brain1:dominant_canonicals + old_candidate_universe:candidate_universe_union_combo` windows=`3` avg_pool=`9.8` match_rate=`1.0%` event_support=`4.9%`
- `box_overlap::old_play_card:ranked_candidate_canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` windows=`3` avg_pool=`2.9` match_rate=`1.0%` event_support=`1.4%`
- `box_overlap::old_play_card:ranked_candidate_combo + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` windows=`3` avg_pool=`2.9` match_rate=`1.0%` event_support=`1.4%`
- `box_overlap::old_play_card:ranked_candidate_canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` windows=`3` avg_pool=`2.9` match_rate=`1.0%` event_support=`1.4%`
- `box_overlap::old_play_card:ranked_candidate_combo + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` windows=`3` avg_pool=`2.9` match_rate=`1.0%` event_support=`1.4%`
- `box_overlap::old_play_card:strategy:play_box_first:B24:boxed_canonicals + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` windows=`3` avg_pool=`2.9` match_rate=`1.0%` event_support=`1.4%`

## Cross-Window Low-Denominator Fixtures

- `vtrac_box_confirmation::board_scoreboard:top_vtrac_indices + old_candidate_universe:pack:PackB_mirror3rd` windows=`3` avg_pool=`1.0` match_rate=`22.2%` event_support=`0.4%`
- `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:pack:PackB_mirror3rd` windows=`3` avg_pool=`1.0` match_rate=`21.4%` event_support=`0.6%`
- `vtrac_box_confirmation::old_candidate_universe:pack:PackB_mirror3rd + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` windows=`3` avg_pool=`1.0` match_rate=`20.0%` event_support=`0.6%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:boxed_canonicals` windows=`3` avg_pool=`1.0` match_rate=`18.2%` event_support=`0.4%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:v0_2_default:B12:boxed_canonicals` windows=`3` avg_pool=`1.0` match_rate=`18.2%` event_support=`0.4%`
- `box_overlap::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:analysis_prefix:B12` windows=`3` avg_pool=`1.0` match_rate=`18.2%` event_support=`0.4%`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack:PackB_mirror3rd` windows=`3` avg_pool=`1.0` match_rate=`14.3%` event_support=`0.4%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B12:boxed_canonicals` windows=`3` avg_pool=`1.0` match_rate=`13.0%` event_support=`0.6%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:v0_2_default:B12:boxed_canonicals` windows=`3` avg_pool=`1.0` match_rate=`13.0%` event_support=`0.6%`
- `box_overlap::old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy_card:analysis_prefix:B12` windows=`3` avg_pool=`1.0` match_rate=`13.0%` event_support=`0.6%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:analysis_prefix:B12:boxed_canonicals` windows=`3` avg_pool=`1.0` match_rate=`13.0%` event_support=`0.6%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:v0_2_default:B12:boxed_canonicals` windows=`3` avg_pool=`1.0` match_rate=`13.0%` event_support=`0.6%`
- `box_overlap::old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy_card:analysis_prefix:B12` windows=`3` avg_pool=`1.0` match_rate=`13.0%` event_support=`0.6%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + shadow_policy:primary_cluster_context` windows=`3` avg_pool=`1.0` match_rate=`12.5%` event_support=`0.6%`
- `vtrac_box_confirmation::old_candidate_universe:pack:PackB_mirror3rd + translation_sandbox:diagnostic_vt_box_seed` windows=`3` avg_pool=`1.0` match_rate=`11.5%` event_support=`0.6%`
- `vtrac_box_confirmation::old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack:aux_vtrac_index_overdue` windows=`3` avg_pool=`1.1` match_rate=`10.9%` event_support=`1.0%`
- `vtrac_box_confirmation::old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` windows=`3` avg_pool=`1.1` match_rate=`10.9%` event_support=`1.0%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:R-perm-4:canonical` windows=`3` avg_pool=`1.1` match_rate=`10.9%` event_support=`1.0%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:R-perm-4:canonical + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` windows=`3` avg_pool=`1.1` match_rate=`10.9%` event_support=`1.0%`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:consensus_double_9:canonical` windows=`3` avg_pool=`1.3` match_rate=`10.5%` event_support=`0.8%`

## Stable Source Surfaces

- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` windows=`3` lane=`vtrac` lane_rate=`7.8%` event_support=`13.4%` decisions=`vtrac_context_only:2|vtrac_watch_decay_only_until_box_pairing:1`
- `board_scoreboard:top_vtrac_indices` windows=`3` lane=`vtrac` lane_rate=`6.5%` event_support=`13.6%` decisions=`vtrac_context_only:3`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` windows=`3` lane=`vtrac` lane_rate=`6.4%` event_support=`3.4%` decisions=`vtrac_context_only:3`
- `translation_sandbox:diagnostic_vt_box_seed` windows=`3` lane=`vtrac` lane_rate=`6.1%` event_support=`37.4%` decisions=`vtrac_watch_decay_only_until_box_pairing:3`
- `brain1:watchlist_indices` windows=`3` lane=`vtrac` lane_rate=`5.9%` event_support=`18.2%` decisions=`vtrac_context_only:3`
- `brain1:dominant_vtrac_indices` windows=`3` lane=`vtrac` lane_rate=`5.7%` event_support=`25.3%` decisions=`vtrac_context_only:3`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` windows=`3` lane=`vtrac` lane_rate=`3.1%` event_support=`4.7%` decisions=`vtrac_context_only:3`
- `old_candidate_universe:pack:R-perm-4` windows=`3` lane=`boxed` lane_rate=`1.6%` event_support=`12.3%` decisions=`boxed_context_or_negative_control:2|boxed_supporting_gate:1`
- `old_candidate_universe:pack:mirror_pair_closure` windows=`3` lane=`boxed` lane_rate=`1.6%` event_support=`15.0%` decisions=`boxed_context_or_negative_control:2|boxed_supporting_gate:1`
- `old_candidate_universe:pack_method:R-perm-4:canonical` windows=`3` lane=`boxed` lane_rate=`1.6%` event_support=`12.3%` decisions=`boxed_context_or_negative_control:2|boxed_supporting_gate:1`
- `old_candidate_universe:pack_method:mirror_pair_closure:canonical` windows=`3` lane=`boxed` lane_rate=`1.6%` event_support=`15.0%` decisions=`boxed_context_or_negative_control:2|boxed_supporting_gate:1`
- `old_play_card:strategy_card:convergence_box_first:B36` windows=`3` lane=`boxed` lane_rate=`1.2%` event_support=`19.0%` decisions=`boxed_supporting_gate:2|boxed_context_or_negative_control:1`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` windows=`3` lane=`boxed` lane_rate=`1.2%` event_support=`19.0%` decisions=`boxed_supporting_gate:2|boxed_context_or_negative_control:1`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` windows=`3` lane=`boxed` lane_rate=`1.2%` event_support=`19.0%` decisions=`boxed_supporting_gate:2|boxed_context_or_negative_control:1`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` windows=`3` lane=`boxed` lane_rate=`1.2%` event_support=`19.0%` decisions=`boxed_supporting_gate:2|boxed_context_or_negative_control:1`
- `old_candidate_universe:pack:PackB_mirror3rd` windows=`3` lane=`boxed` lane_rate=`1.2%` event_support=`0.8%` decisions=`boxed_context_or_negative_control:2|boxed_supporting_gate:1`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` windows=`3` lane=`boxed` lane_rate=`1.2%` event_support=`8.1%` decisions=`boxed_context_or_negative_control:3`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` windows=`3` lane=`boxed` lane_rate=`1.2%` event_support=`8.1%` decisions=`boxed_context_or_negative_control:3`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` windows=`3` lane=`boxed` lane_rate=`1.2%` event_support=`8.5%` decisions=`boxed_context_or_negative_control:3`
- `old_play_card:ranked_candidate_canonical` windows=`3` lane=`boxed` lane_rate=`1.2%` event_support=`14.6%` decisions=`boxed_context_or_negative_control:3`

## Generated Files

- Stack confirmation CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_STACK_CONFIRMATION.csv`
- Hypothesis confirmation CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_HYPOTHESIS_CONFIRMATION.csv`
- Source confirmation CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_SOURCE_CONFIRMATION.csv`
- Rollup JSON: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_STACK_ROLLUP.json`

## Guardrail

- A cross-window candidate is only permission to replay against fixtures. It is not a permission to alter live scoring or budgeting.
