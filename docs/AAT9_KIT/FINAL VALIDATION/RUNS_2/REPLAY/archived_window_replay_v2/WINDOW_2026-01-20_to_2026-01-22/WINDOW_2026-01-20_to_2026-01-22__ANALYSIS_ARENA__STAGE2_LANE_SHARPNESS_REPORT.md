# Stage 2 Lane Sharpness Report

Purpose: separate straight, boxed, VTRAC, and context evidence so broad territory is not mistaken for precise conversion.

## Lane Panels

- `straight`: sources=`16`, exposures=`22442`, lane_hit_rate=`0.1%`, avg_source_pool=`33.4`
- `boxed`: sources=`65`, exposures=`17898`, lane_hit_rate=`0.7%`, avg_source_pool=`6.2`
- `vtrac`: sources=`7`, exposures=`2345`, lane_hit_rate=`5.4%`, avg_source_pool=`6.6`

## Best Per-Lane Sources

### Straight
- `old_play_card:strategy:analysis_prefix:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`19.0%` avg_pool=`12.0` lift=`0.99`
- `old_play_card:strategy:conversion_box_first:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`15.5%` avg_pool=`12.0` lift=`0.99`
- `old_play_card:strategy:play_box_first:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`11.9%` avg_pool=`12.0` lift=`0.99`
- `old_play_card:strategy:v0_2_default:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`19.0%` avg_pool=`12.0` lift=`0.99`
- `old_play_card:strategy:play_box_first:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`17.9%` avg_pool=`24.0` lift=`0.99`
- `old_play_card:strategy:conversion_box_first:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`27.4%` avg_pool=`36.0` lift=`0.99`
- `old_play_card:strategy:play_box_first:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`25.0%` avg_pool=`36.0` lift=`0.99`
- `old_candidate_universe:candidate_universe_union_combo` decision=`denominator_only_broad_control` lane_rate=`0.2%` event_support=`76.2%` avg_pool=`207.3` lift=`0.80`
- `old_play_card:ranked_candidate_combo` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`19.0%` avg_pool=`15.0` lift=`0.79`
- `translation_sandbox:diagnostic_straight_seed` decision=`straight_context_or_negative_control` lane_rate=`0.1%` event_support=`35.7%` avg_pool=`16.0` lift=`0.74`

### Boxed
- `old_candidate_universe:pack:PackB_mirror3rd` decision=`boxed_supporting_gate` lane_rate=`2.2%` event_support=`3.3%` avg_pool=`3.0` lift=`2.44`
- `old_candidate_universe:pack:R-perm-4` decision=`boxed_context_or_negative_control` lane_rate=`1.8%` event_support=`13.1%` avg_pool=`4.0` lift=`1.96`
- `old_candidate_universe:pack_method:R-perm-4:canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.8%` event_support=`13.1%` avg_pool=`4.0` lift=`1.96`
- `old_candidate_universe:pack_method:aux_positional:canonical` decision=`boxed_supporting_gate` lane_rate=`1.2%` event_support=`28.6%` avg_pool=`9.9` lift=`1.33`
- `positional:positional_canonical` decision=`boxed_supporting_gate` lane_rate=`1.2%` event_support=`27.4%` avg_pool=`7.9` lift=`1.32`
- `old_play_card:strategy_card:convergence_box_first:B36` decision=`boxed_supporting_gate` lane_rate=`1.2%` event_support=`21.4%` avg_pool=`8.0` lift=`1.31`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` decision=`boxed_supporting_gate` lane_rate=`1.2%` event_support=`21.4%` avg_pool=`8.0` lift=`1.31`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` decision=`boxed_supporting_gate` lane_rate=`1.2%` event_support=`21.4%` avg_pool=`8.0` lift=`1.31`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` decision=`boxed_supporting_gate` lane_rate=`1.2%` event_support=`21.4%` avg_pool=`8.0` lift=`1.31`
- `old_candidate_universe:pack_method:mirror_pair_closure:canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.2%` event_support=`17.9%` avg_pool=`3.0` lift=`1.31`

### Vtrac
- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`vtrac_watch_decay_only_until_box_pairing` lane_rate=`10.6%` event_support=`16.7%` avg_pool=`4.5` lift=`1.85`
- `board_scoreboard:top_vtrac_indices` decision=`vtrac_context_only` lane_rate=`7.7%` event_support=`15.5%` avg_pool=`4.0` lift=`1.35`
- `brain1:dominant_vtrac_indices` decision=`vtrac_context_only` lane_rate=`6.6%` event_support=`28.6%` avg_pool=`8.7` lift=`1.15`
- `brain1:watchlist_indices` decision=`vtrac_context_only` lane_rate=`6.0%` event_support=`17.9%` avg_pool=`6.0` lift=`1.04`
- `translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_watch_decay_only_until_box_pairing` lane_rate=`6.0%` event_support=`35.7%` avg_pool=`12.0` lift=`1.04`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` decision=`vtrac_context_only` lane_rate=`5.7%` event_support=`4.2%` avg_pool=`8.8` lift=`1.00`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`vtrac_context_only` lane_rate=`1.8%` event_support=`2.4%` avg_pool=`2.5` lift=`0.32`
