# Stage 2 Lane Sharpness Report

Purpose: separate straight, boxed, VTRAC, and context evidence so broad territory is not mistaken for precise conversion.

## Lane Panels

- `straight`: sources=`16`, exposures=`37012`, lane_hit_rate=`0.3%`, avg_source_pool=`33.1`
- `boxed`: sources=`65`, exposures=`29914`, lane_hit_rate=`1.1%`, avg_source_pool=`6.2`
- `vtrac`: sources=`7`, exposures=`4104`, lane_hit_rate=`5.3%`, avg_source_pool=`6.9`

## Best Per-Lane Sources

### Straight
- `old_play_card:ranked_candidate_combo` decision=`straight_context_or_negative_control` lane_rate=`0.4%` event_support=`16.7%` avg_pool=`15.0` lift=`1.93`
- `old_play_card:strategy:analysis_prefix:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.4%` event_support=`11.6%` avg_pool=`12.0` lift=`1.81`
- `old_play_card:strategy:play_box_first:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.4%` event_support=`9.4%` avg_pool=`12.0` lift=`1.81`
- `old_play_card:strategy:v0_2_default:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.4%` event_support=`11.6%` avg_pool=`12.0` lift=`1.81`
- `old_play_card:strategy:play_box_first:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.4%` event_support=`13.8%` avg_pool=`24.0` lift=`1.81`
- `old_play_card:strategy:conversion_box_first:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.4%` event_support=`27.5%` avg_pool=`36.0` lift=`1.81`
- `old_play_card:strategy:play_box_first:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.4%` event_support=`21.0%` avg_pool=`36.0` lift=`1.81`
- `old_play_card:strategy:analysis_prefix:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`31.9%` avg_pool=`36.0` lift=`1.61`
- `old_play_card:strategy:analysis_prefix:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`24.6%` avg_pool=`24.0` lift=`1.51`
- `translation_sandbox:diagnostic_straight_seed` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`25.4%` avg_pool=`16.0` lift=`1.36`

### Boxed
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` decision=`boxed_supporting_gate` lane_rate=`2.2%` event_support=`10.9%` avg_pool=`3.3` lift=`2.44`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` decision=`boxed_supporting_gate` lane_rate=`2.2%` event_support=`10.9%` avg_pool=`3.3` lift=`2.44`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` decision=`boxed_supporting_gate` lane_rate=`2.2%` event_support=`10.9%` avg_pool=`3.3` lift=`2.43`
- `old_play_card:strategy_card:convergence_box_first:B12` decision=`boxed_supporting_gate` lane_rate=`2.2%` event_support=`10.1%` avg_pool=`3.3` lift=`2.42`
- `old_candidate_universe:pack_method:due_doubles_mirror_single:canonical` decision=`boxed_supporting_gate` lane_rate=`2.1%` event_support=`2.9%` avg_pool=`2.0` lift=`2.39`
- `old_candidate_universe:pack_method:PackB_mirror3rd:canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.9%` event_support=`6.5%` avg_pool=`3.0` lift=`2.13`
- `old_play_card:strategy_card:convergence_box_first:B24` decision=`boxed_context_or_negative_control` lane_rate=`1.8%` event_support=`16.7%` avg_pool=`6.4` lift=`1.99`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` decision=`boxed_context_or_negative_control` lane_rate=`1.8%` event_support=`16.7%` avg_pool=`6.4` lift=`1.99`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` decision=`boxed_context_or_negative_control` lane_rate=`1.8%` event_support=`16.7%` avg_pool=`6.4` lift=`1.99`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` decision=`boxed_context_or_negative_control` lane_rate=`1.8%` event_support=`16.7%` avg_pool=`6.4` lift=`1.99`

### Vtrac
- `old_candidate_universe:pack:aux_vtrac_index_overdue` decision=`vtrac_context_only` lane_rate=`6.6%` event_support=`5.1%` avg_pool=`9.0` lift=`1.19`
- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`vtrac_context_only` lane_rate=`6.6%` event_support=`11.6%` avg_pool=`4.5` lift=`1.17`
- `translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_context_only` lane_rate=`5.7%` event_support=`34.8%` avg_pool=`12.0` lift=`1.02`
- `brain1:watchlist_indices` decision=`vtrac_context_only` lane_rate=`5.5%` event_support=`16.7%` avg_pool=`6.0` lift=`0.97`
- `brain1:dominant_vtrac_indices` decision=`vtrac_context_only` lane_rate=`5.1%` event_support=`22.5%` avg_pool=`8.7` lift=`0.91`
- `board_scoreboard:top_vtrac_indices` decision=`vtrac_context_only` lane_rate=`5.0%` event_support=`10.1%` avg_pool=`4.0` lift=`0.89`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`vtrac_context_only` lane_rate=`4.2%` event_support=`6.5%` avg_pool=`2.9` lift=`0.75`
