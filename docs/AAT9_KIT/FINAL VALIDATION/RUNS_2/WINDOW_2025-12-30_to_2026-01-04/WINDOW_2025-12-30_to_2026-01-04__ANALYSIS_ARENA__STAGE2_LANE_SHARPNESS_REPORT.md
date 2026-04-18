# Stage 2 Lane Sharpness Report

Purpose: separate straight, boxed, VTRAC, and context evidence so broad territory is not mistaken for precise conversion.

## Lane Panels

- `straight`: sources=`16`, exposures=`41260`, lane_hit_rate=`0.1%`, avg_source_pool=`30.7`
- `boxed`: sources=`65`, exposures=`33514`, lane_hit_rate=`0.6%`, avg_source_pool=`5.9`
- `vtrac`: sources=`7`, exposures=`5004`, lane_hit_rate=`4.7%`, avg_source_pool=`6.7`

## Best Per-Lane Sources

### Straight
- `old_play_card:strategy:v0_2_default:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`24.5%` avg_pool=`24.0` lift=`1.28`
- `old_candidate_universe:candidate_universe_union_combo` decision=`denominator_only_broad_control` lane_rate=`0.2%` event_support=`66.9%` avg_pool=`164.2` lift=`0.93`
- `old_play_card:strategy:play_box_first:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`17.8%` avg_pool=`36.0` lift=`0.85`
- `old_play_card:strategy:v0_2_default:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.2%` event_support=`31.9%` avg_pool=`36.0` lift=`0.85`
- `old_play_card:strategy:analysis_prefix:B24:combos` decision=`straight_context_or_negative_control` lane_rate=`0.1%` event_support=`19.6%` avg_pool=`24.0` lift=`0.77`
- `old_play_card:strategy:analysis_prefix:B36:combos` decision=`straight_context_or_negative_control` lane_rate=`0.1%` event_support=`24.5%` avg_pool=`36.0` lift=`0.68`
- `old_play_card:strategy:analysis_prefix:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.1%` event_support=`12.3%` avg_pool=`12.0` lift=`0.51`
- `old_play_card:strategy:conversion_box_first:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.1%` event_support=`11.0%` avg_pool=`12.0` lift=`0.51`
- `old_play_card:strategy:play_box_first:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.1%` event_support=`8.0%` avg_pool=`12.0` lift=`0.51`
- `old_play_card:strategy:v0_2_default:B12:combos` decision=`straight_context_or_negative_control` lane_rate=`0.1%` event_support=`12.3%` avg_pool=`12.0` lift=`0.51`

### Boxed
- `old_candidate_universe:pack:PackB_mirror3rd` decision=`boxed_supporting_gate` lane_rate=`2.4%` event_support=`6.3%` avg_pool=`3.0` lift=`2.64`
- `old_candidate_universe:pack_method:PackB_mirror3rd:canonical` decision=`boxed_context_or_negative_control` lane_rate=`2.0%` event_support=`4.9%` avg_pool=`3.0` lift=`2.25`
- `old_candidate_universe:pack_method:PackA_vt8:canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.3%` event_support=`4.9%` avg_pool=`7.2` lift=`1.50`
- `old_candidate_universe:pack_method:mirror_pair_closure:canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.2%` event_support=`15.3%` avg_pool=`3.0` lift=`1.35`
- `old_candidate_universe:pack:R-perm-4` decision=`boxed_context_or_negative_control` lane_rate=`1.2%` event_support=`9.2%` avg_pool=`4.0` lift=`1.35`
- `old_candidate_universe:pack_method:R-perm-4:canonical` decision=`boxed_context_or_negative_control` lane_rate=`1.2%` event_support=`9.2%` avg_pool=`4.0` lift=`1.35`
- `old_candidate_universe:pack:mirror_pair_closure` decision=`boxed_context_or_negative_control` lane_rate=`1.2%` event_support=`15.3%` avg_pool=`6.0` lift=`1.35`
- `shadow_policy:primary_cluster_canonicals` decision=`boxed_context_or_negative_control` lane_rate=`1.0%` event_support=`18.4%` avg_pool=`6.0` lift=`1.12`
- `brain1:dominant_canonicals` decision=`boxed_supporting_gate` lane_rate=`0.9%` event_support=`23.3%` avg_pool=`11.9` lift=`1.02`
- `blackapple:recommended_canonicals` decision=`boxed_context_or_negative_control` lane_rate=`0.9%` event_support=`19.6%` avg_pool=`8.0` lift=`1.01`

### Vtrac
- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`vtrac_context_only` lane_rate=`7.0%` event_support=`12.3%` avg_pool=`4.4` lift=`1.27`
- `board_scoreboard:top_vtrac_indices` decision=`vtrac_context_only` lane_rate=`6.2%` event_support=`13.5%` avg_pool=`4.0` lift=`1.13`
- `translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_watch_decay_only_until_box_pairing` lane_rate=`6.0%` event_support=`37.4%` avg_pool=`12.0` lift=`1.07`
- `brain1:watchlist_indices` decision=`vtrac_context_only` lane_rate=`5.6%` event_support=`17.8%` avg_pool=`6.0` lift=`1.00`
- `brain1:dominant_vtrac_indices` decision=`vtrac_context_only` lane_rate=`5.2%` event_support=`22.7%` avg_pool=`8.3` lift=`0.93`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` decision=`vtrac_context_only` lane_rate=`4.8%` event_support=`4.3%` avg_pool=`10.4` lift=`0.87`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`vtrac_context_only` lane_rate=`2.2%` event_support=`3.7%` avg_pool=`3.0` lift=`0.39`
