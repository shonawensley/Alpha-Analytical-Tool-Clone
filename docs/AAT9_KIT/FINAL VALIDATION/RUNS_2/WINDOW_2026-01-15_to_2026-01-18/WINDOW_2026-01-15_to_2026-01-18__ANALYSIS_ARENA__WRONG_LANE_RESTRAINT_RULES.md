# Wrong-Lane Restraint Rules

Purpose: prevent VTRAC/territory evidence from being over-promoted into boxed/straight action.

- Wrong-lane cases: `0`
- VTRAC-related stack rows: `585`

## Rules

- VTRAC-only evidence may mark territory/watch/carryforward, but should not create a boxed/straight spend by itself.
- A VTRAC source needs a bounded boxed or exact confirmation source before translator promotion.
- Broad VTRAC stacks with high false-positive proxy stay negative-control/context surfaces.
- Wrong-lane cases must be included as regression tests before any translator promotion.

## Highest-Support VTRAC Stacks

- `vtrac_box_confirmation::old_candidate_universe:pack:aux_positional + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:consensus_double_9:canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:consensus_double_9 + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + positional:positional_canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + positional:positional_combo` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + positional:positional_canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + positional:positional_combo` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:aux_positional:canonical + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack:mirror_pair_closure` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:mirror_pair_closure:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_candidate_universe:pack_method:mirror_pair_closure:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:aux_positional:canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + profit_alerts:implied_canonicals` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + profit_alerts:top_profit_alerts` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + shadow_policy:primary_cluster_context` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy:analysis_prefix:B24:boxed_canonicals` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:analysis_prefix:B24` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::board_scoreboard:top_vtrac_indices + old_candidate_universe:pack:PackB_mirror3rd` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy:play_box_first:B36:boxed_canonicals` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
