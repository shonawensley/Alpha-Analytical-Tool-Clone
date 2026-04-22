# Stage 2 Lane Sharpness Report

Purpose: separate straight, boxed, VTRAC, and context evidence so broad territory is not mistaken for precise conversion.

## Lane Panels

- `straight`: sources=`16`, exposures=`110987`, lane_hit_rate=`0.2%`, avg_source_pool=`33.1`
- `boxed`: sources=`65`, exposures=`89389`, lane_hit_rate=`0.9%`, avg_source_pool=`6.2`
- `vtrac`: sources=`7`, exposures=`11313`, lane_hit_rate=`5.4%`, avg_source_pool=`6.7`

## Best Per-Lane Sources

### Straight
- `positional:positional_combo` decision=`straight_context_or_negative_control` lane_rate=`0.4%` event_support=`21.7%` avg_pool=`8.0` lift=`1.81`
- `old_play_card:strategy:conversion_box_first:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.4%` event_support=`22.2%` avg_pool=`24.0` lift=`1.81`
- `old_play_card:strategy:conversion_box_first:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`14.5%` avg_pool=`12.0` lift=`1.61`
- `old_play_card:strategy:conversion_box_first:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`25.1%` avg_pool=`36.0` lift=`1.54`
- `old_play_card:strategy:analysis_prefix:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`22.7%` avg_pool=`24.0` lift=`1.51`
- `old_play_card:strategy:play_box_first:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`10.1%` avg_pool=`12.0` lift=`1.41`
- `old_play_card:strategy:play_box_first:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`15.9%` avg_pool=`24.0` lift=`1.41`
- `old_play_card:strategy:analysis_prefix:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`29.7%` avg_pool=`36.0` lift=`1.41`
- `translation_sandbox:diagnostic_straight_seed` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`28.5%` avg_pool=`16.0` lift=`1.36`
- `old_play_card:strategy:analysis_prefix:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`13.5%` avg_pool=`12.0` lift=`1.21`

### Boxed
- `old_candidate_universe:pack:aux_positional` decision=`boxed_supporting_gate` lane_rate=`1.9%` event_support=`26.9%` avg_pool=`8.0` lift=`2.12`
- `old_candidate_universe:pack:R-perm-4` decision=`boxed_context_or_negative_control` lane_rate=`1.3%` event_support=`11.4%` avg_pool=`4.0` lift=`1.46`
- `old_candidate_universe:pack_method:R-perm-4:canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.3%` event_support=`11.4%` avg_pool=`4.0` lift=`1.46`
- `old_candidate_universe:pack_method:mirror_pair_closure:canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.3%` event_support=`13.5%` avg_pool=`3.0` lift=`1.42`
- `old_candidate_universe:pack:mirror_pair_closure` decision=`boxed_context_or_negative_control` lane_rate=`1.3%` event_support=`13.5%` avg_pool=`6.0` lift=`1.42`
- `old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` decision=`boxed_context_or_negative_control` lane_rate=`1.1%` event_support=`12.6%` avg_pool=`5.0` lift=`1.28`
- `old_play_card:strategy_card:conversion_box_first:B24` decision=`boxed_context_or_negative_control` lane_rate=`1.1%` event_support=`12.6%` avg_pool=`5.0` lift=`1.28`
- `old_play_card:strategy_card:convergence_box_first:B24` decision=`boxed_context_or_negative_control` lane_rate=`1.1%` event_support=`14.3%` avg_pool=`6.4` lift=`1.24`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` decision=`boxed_context_or_negative_control` lane_rate=`1.1%` event_support=`14.3%` avg_pool=`6.4` lift=`1.24`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` decision=`boxed_context_or_negative_control` lane_rate=`1.1%` event_support=`14.3%` avg_pool=`6.4` lift=`1.24`

### Vtrac
- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`vtrac_context_only` lane_rate=`8.7%` event_support=`15.0%` avg_pool=`4.6` lift=`1.55`
- `brain1:dominant_vtrac_indices` decision=`vtrac_context_only` lane_rate=`6.5%` event_support=`28.0%` avg_pool=`8.4` lift=`1.16`
- `brain1:watchlist_indices` decision=`vtrac_context_only` lane_rate=`6.4%` event_support=`20.0%` avg_pool=`6.0` lift=`1.14`
- `translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_watch_decay_only_until_box_pairing` lane_rate=`6.3%` event_support=`39.1%` avg_pool=`12.0` lift=`1.12`
- `board_scoreboard:top_vtrac_indices` decision=`vtrac_context_only` lane_rate=`6.3%` event_support=`13.0%` avg_pool=`4.0` lift=`1.12`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` decision=`vtrac_context_only` lane_rate=`5.6%` event_support=`4.2%` avg_pool=`8.8` lift=`1.01`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`vtrac_context_only` lane_rate=`2.3%` event_support=`2.9%` avg_pool=`2.6` lift=`0.41`
