# Stage 2 Lane Sharpness Report

Purpose: separate straight, boxed, VTRAC, and context evidence so broad territory is not mistaken for precise conversion.

## Lane Panels

- `straight`: sources=`16`, exposures=`27231`, lane_hit_rate=`0.3%`, avg_source_pool=`30.4`
- `boxed`: sources=`66`, exposures=`22174`, lane_hit_rate=`1.1%`, avg_source_pool=`5.8`
- `vtrac`: sources=`7`, exposures=`3180`, lane_hit_rate=`6.5%`, avg_source_pool=`6.9`

## Best Per-Lane Sources

### Straight
- `old_play_card:strategy:play_box_first:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.5%` event_support=`12.8%` avg_pool=`24.0` lift=`2.68`
- `old_play_card:strategy:conversion_box_first:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.4%` event_support=`9.2%` avg_pool=`12.0` lift=`2.29`
- `old_play_card:strategy:play_box_first:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.4%` event_support=`19.3%` avg_pool=`36.0` lift=`2.04`
- `old_play_card:strategy:conversion_box_first:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.4%` event_support=`18.3%` avg_pool=`24.0` lift=`1.91`
- `old_play_card:strategy:conversion_box_first:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`21.1%` avg_pool=`36.0` lift=`1.78`
- `old_play_card:strategy:analysis_prefix:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`13.8%` avg_pool=`12.0` lift=`1.53`
- `old_play_card:strategy:play_box_first:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`7.3%` avg_pool=`12.0` lift=`1.53`
- `old_play_card:strategy:v0_2_default:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`13.8%` avg_pool=`12.0` lift=`1.53`
- `old_play_card:strategy:analysis_prefix:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.3%` event_support=`22.0%` avg_pool=`24.0` lift=`1.53`
- `old_candidate_universe:candidate_universe_union_combo` decision=`denominator_only_broad_control` lane_rate=`0.2%` event_support=`70.6%` avg_pool=`159.3` lift=`1.27`

### Boxed
- `old_candidate_universe:pack_method:mirror_pair_closure:canonical` decision=`boxed_supporting_gate` lane_rate=`3.0%` event_support=`16.5%` avg_pool=`3.0` lift=`3.36`
- `old_candidate_universe:pack:mirror_pair_closure` decision=`boxed_supporting_gate` lane_rate=`3.0%` event_support=`16.5%` avg_pool=`6.0` lift=`3.36`
- `old_candidate_universe:pack:stable_top` decision=`boxed_supporting_gate` lane_rate=`2.3%` event_support=`17.8%` avg_pool=`4.2` lift=`2.59`
- `old_play_card:strategy:play_box_first:B24:boxed_canonicals` decision=`boxed_supporting_gate` lane_rate=`2.1%` event_support=`12.8%` avg_pool=`6.0` lift=`2.35`
- `old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` decision=`boxed_context_or_negative_control` lane_rate=`1.8%` event_support=`11.0%` avg_pool=`5.0` lift=`2.02`
- `old_play_card:strategy_card:conversion_box_first:B24` decision=`boxed_context_or_negative_control` lane_rate=`1.8%` event_support=`11.0%` avg_pool=`5.0` lift=`2.02`
- `old_play_card:ranked_candidate_canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.7%` event_support=`16.5%` avg_pool=`7.4` lift=`1.92`
- `old_play_card:strategy_card:conversion_box_first:B36` decision=`boxed_context_or_negative_control` lane_rate=`1.7%` event_support=`12.8%` avg_pool=`7.5` lift=`1.89`
- `old_play_card:strategy:conversion_box_first:B36:boxed_canonicals` decision=`boxed_context_or_negative_control` lane_rate=`1.6%` event_support=`13.8%` avg_pool=`7.6` lift=`1.85`
- `old_play_card:strategy:play_box_first:B36:boxed_canonicals` decision=`boxed_context_or_negative_control` lane_rate=`1.6%` event_support=`19.3%` avg_pool=`9.1` lift=`1.78`

### Vtrac
- `old_candidate_universe:pack:aux_vtrac_index_overdue` decision=`vtrac_context_only` lane_rate=`9.7%` event_support=`7.4%` avg_pool=`8.8` lift=`1.75`
- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`vtrac_context_only` lane_rate=`8.5%` event_support=`14.7%` avg_pool=`4.6` lift=`1.52`
- `board_scoreboard:top_vtrac_indices` decision=`vtrac_context_only` lane_rate=`8.0%` event_support=`16.5%` avg_pool=`4.0` lift=`1.44`
- `brain1:watchlist_indices` decision=`vtrac_context_only` lane_rate=`6.8%` event_support=`21.1%` avg_pool=`6.0` lift=`1.23`
- `translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_watch_decay_only_until_box_pairing` lane_rate=`6.7%` event_support=`42.2%` avg_pool=`12.0` lift=`1.20`
- `brain1:dominant_vtrac_indices` decision=`vtrac_context_only` lane_rate=`6.6%` event_support=`30.3%` avg_pool=`8.6` lift=`1.19`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`vtrac_context_only` lane_rate=`4.0%` event_support=`5.5%` avg_pool=`2.7` lift=`0.72`
