# Stage 2 Lane Sharpness Report

Purpose: separate straight, boxed, VTRAC, and context evidence so broad territory is not mistaken for precise conversion.

## Lane Panels

- `straight`: sources=`16`, exposures=`54556`, lane_hit_rate=`0.2%`, avg_source_pool=`30.4`
- `boxed`: sources=`66`, exposures=`44453`, lane_hit_rate=`0.8%`, avg_source_pool=`5.8`
- `vtrac`: sources=`7`, exposures=`6323`, lane_hit_rate=`5.8%`, avg_source_pool=`6.9`

## Best Per-Lane Sources

### Straight
- `old_play_card:strategy:conversion_box_first:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`11.3%` avg_pool=`12.0` lift=`1.51`
- `old_play_card:strategy:play_box_first:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`13.6%` avg_pool=`24.0` lift=`1.51`
- `old_play_card:strategy:play_box_first:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`18.6%` avg_pool=`36.0` lift=`1.38`
- `old_play_card:strategy:conversion_box_first:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`19.0%` avg_pool=`24.0` lift=`1.32`
- `old_play_card:strategy:conversion_box_first:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`22.6%` avg_pool=`36.0` lift=`1.26`
- `old_play_card:strategy:play_box_first:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`9.0%` avg_pool=`12.0` lift=`1.13`
- `old_candidate_universe:candidate_universe_union_combo` decision=`denominator_only_broad_control` lane_rate=`0.2%` event_support=`67.4%` avg_pool=`160.1` lift=`0.96`
- `old_play_card:strategy:analysis_prefix:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.1%` event_support=`14.5%` avg_pool=`12.0` lift=`0.75`
- `old_play_card:strategy:v0_2_default:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.1%` event_support=`14.5%` avg_pool=`12.0` lift=`0.75`
- `old_play_card:strategy:analysis_prefix:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.1%` event_support=`20.8%` avg_pool=`24.0` lift=`0.75`

### Boxed
- `old_candidate_universe:pack_method:mirror_pair_closure:canonical` decision=`boxed_supporting_gate` lane_rate=`2.2%` event_support=`17.2%` avg_pool=`3.0` lift=`2.49`
- `old_candidate_universe:pack:mirror_pair_closure` decision=`boxed_supporting_gate` lane_rate=`2.2%` event_support=`17.2%` avg_pool=`6.0` lift=`2.49`
- `old_candidate_universe:pack:stable_top` decision=`boxed_context_or_negative_control` lane_rate=`1.8%` event_support=`15.4%` avg_pool=`4.0` lift=`1.95`
- `old_candidate_universe:pack:R-perm-4` decision=`boxed_context_or_negative_control` lane_rate=`1.3%` event_support=`8.1%` avg_pool=`4.0` lift=`1.49`
- `old_candidate_universe:pack_method:R-perm-4:canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.3%` event_support=`8.1%` avg_pool=`4.0` lift=`1.49`
- `old_play_card:strategy:play_box_first:B24:boxed_canonicals` decision=`boxed_context_or_negative_control` lane_rate=`1.2%` event_support=`13.6%` avg_pool=`6.0` lift=`1.32`
- `old_play_card:ranked_candidate_canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.1%` event_support=`16.3%` avg_pool=`7.3` lift=`1.23`
- `old_play_card:strategy:play_box_first:B36:boxed_canonicals` decision=`boxed_context_or_negative_control` lane_rate=`1.1%` event_support=`18.6%` avg_pool=`9.1` lift=`1.21`
- `old_play_card:strategy_card:conversion_box_first:B36` decision=`boxed_context_or_negative_control` lane_rate=`1.1%` event_support=`14.9%` avg_pool=`7.4` lift=`1.20`
- `old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` decision=`boxed_context_or_negative_control` lane_rate=`1.1%` event_support=`11.3%` avg_pool=`5.0` lift=`1.20`

### Vtrac
- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`vtrac_context_only` lane_rate=`8.6%` event_support=`14.0%` avg_pool=`4.6` lift=`1.52`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` decision=`vtrac_context_only` lane_rate=`8.4%` event_support=`6.1%` avg_pool=`8.8` lift=`1.50`
- `board_scoreboard:top_vtrac_indices` decision=`vtrac_context_only` lane_rate=`7.4%` event_support=`14.9%` avg_pool=`4.0` lift=`1.31`
- `brain1:watchlist_indices` decision=`vtrac_context_only` lane_rate=`6.2%` event_support=`19.0%` avg_pool=`6.0` lift=`1.11`
- `brain1:dominant_vtrac_indices` decision=`vtrac_context_only` lane_rate=`6.2%` event_support=`28.1%` avg_pool=`8.7` lift=`1.11`
- `translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_watch_decay_only_until_box_pairing` lane_rate=`6.2%` event_support=`38.0%` avg_pool=`12.0` lift=`1.10`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`vtrac_context_only` lane_rate=`3.2%` event_support=`4.1%` avg_pool=`2.6` lift=`0.56`
