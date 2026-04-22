# Stage 2 Lane Sharpness Report

Purpose: separate straight, boxed, VTRAC, and context evidence so broad territory is not mistaken for precise conversion.

## Lane Panels

- `straight`: sources=`16`, exposures=`81706`, lane_hit_rate=`0.2%`, avg_source_pool=`33.2`
- `boxed`: sources=`65`, exposures=`65546`, lane_hit_rate=`0.8%`, avg_source_pool=`6.2`
- `vtrac`: sources=`7`, exposures=`9108`, lane_hit_rate=`4.9%`, avg_source_pool=`6.7`

## Best Per-Lane Sources

### Straight
- `old_play_card:ranked_candidate_combo` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`14.3%` avg_pool=`15.0` lift=`1.55`
- `old_play_card:strategy:analysis_prefix:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`11.6%` avg_pool=`12.0` lift=`1.38`
- `old_play_card:strategy:conversion_box_first:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`13.3%` avg_pool=`12.0` lift=`1.38`
- `old_play_card:strategy:play_box_first:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`9.0%` avg_pool=`12.0` lift=`1.38`
- `old_play_card:strategy:v0_2_default:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`11.6%` avg_pool=`12.0` lift=`1.38`
- `old_play_card:strategy:analysis_prefix:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`30.2%` avg_pool=`36.0` lift=`1.38`
- `old_play_card:strategy:conversion_box_first:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`26.6%` avg_pool=`36.0` lift=`1.29`
- `old_play_card:strategy:v0_2_default:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`37.5%` avg_pool=`36.0` lift=`1.29`
- `old_play_card:strategy:analysis_prefix:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`23.9%` avg_pool=`24.0` lift=`1.25`
- `old_play_card:strategy:play_box_first:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`14.6%` avg_pool=`24.0` lift=`1.25`

### Boxed
- `old_candidate_universe:pack:PackB_mirror3rd` decision=`boxed_context_or_negative_control` lane_rate=`1.5%` event_support=`2.3%` avg_pool=`3.0` lift=`1.71`
- `old_candidate_universe:pack_method:PackB_mirror3rd:canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.5%` event_support=`5.0%` avg_pool=`3.0` lift=`1.71`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` decision=`boxed_context_or_negative_control` lane_rate=`1.4%` event_support=`8.6%` avg_pool=`3.3` lift=`1.57`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` decision=`boxed_context_or_negative_control` lane_rate=`1.4%` event_support=`8.6%` avg_pool=`3.3` lift=`1.57`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` decision=`boxed_context_or_negative_control` lane_rate=`1.4%` event_support=`8.6%` avg_pool=`3.3` lift=`1.56`
- `old_play_card:strategy_card:convergence_box_first:B12` decision=`boxed_context_or_negative_control` lane_rate=`1.4%` event_support=`8.3%` avg_pool=`3.3` lift=`1.53`
- `old_candidate_universe:pack_method:PackA_vt8:canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.3%` event_support=`5.0%` avg_pool=`7.2` lift=`1.51`
- `old_play_card:ranked_candidate_canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.2%` event_support=`14.3%` avg_pool=`6.3` lift=`1.39`
- `blackapple:recommended_canonicals` decision=`boxed_supporting_gate` lane_rate=`1.2%` event_support=`22.3%` avg_pool=`8.0` lift=`1.37`
- `old_play_card:strategy_card:convergence_box_first:B24` decision=`boxed_context_or_negative_control` lane_rate=`1.2%` event_support=`15.3%` avg_pool=`6.4` lift=`1.36`

### Vtrac
- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`vtrac_context_only` lane_rate=`6.8%` event_support=`12.0%` avg_pool=`4.5` lift=`1.22`
- `translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_watch_decay_only_until_box_pairing` lane_rate=`5.9%` event_support=`36.2%` avg_pool=`12.0` lift=`1.05`
- `board_scoreboard:top_vtrac_indices` decision=`vtrac_context_only` lane_rate=`5.7%` event_support=`12.0%` avg_pool=`4.0` lift=`1.02`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` decision=`vtrac_context_only` lane_rate=`5.6%` event_support=`4.7%` avg_pool=`9.8` lift=`1.00`
- `brain1:watchlist_indices` decision=`vtrac_context_only` lane_rate=`5.5%` event_support=`17.3%` avg_pool=`6.0` lift=`0.99`
- `brain1:dominant_vtrac_indices` decision=`vtrac_context_only` lane_rate=`5.1%` event_support=`22.6%` avg_pool=`8.5` lift=`0.92`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`vtrac_context_only` lane_rate=`3.1%` event_support=`5.0%` avg_pool=`3.0` lift=`0.55`
