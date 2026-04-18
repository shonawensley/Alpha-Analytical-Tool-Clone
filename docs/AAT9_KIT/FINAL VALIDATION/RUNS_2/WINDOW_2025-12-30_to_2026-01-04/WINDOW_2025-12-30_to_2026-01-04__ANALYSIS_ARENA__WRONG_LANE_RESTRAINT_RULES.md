# Wrong-Lane Restraint Rules

Purpose: prevent VTRAC/territory evidence from being over-promoted into boxed/straight action.

- Wrong-lane cases: `0`
- VTRAC-related stack rows: `584`

## Rules

- VTRAC-only evidence may mark territory/watch/carryforward, but should not create a boxed/straight spend by itself.
- A VTRAC source needs a bounded boxed or exact confirmation source before translator promotion.
- Broad VTRAC stacks with high false-positive proxy stay negative-control/context surfaces.
- Wrong-lane cases must be included as regression tests before any translator promotion.

## Highest-Support VTRAC Stacks

- `vtrac_box_confirmation::old_candidate_universe:pack:PackB_mirror3rd + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::board_scoreboard:top_canonicals + old_candidate_universe:pack:aux_vtrac_index_overdue` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:PackB_mirror3rd + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:hot_zones_top:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + shadow_policy:primary_cluster_context` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackA_vt8:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackB_mirror3rd:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_overlap::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_overlap::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:pack:PackB_mirror3rd` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_overlap::board_scoreboard:top_vtrac_indices + old_candidate_universe:pack:aux_vtrac_index_overdue` decision=`context_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::brain1:context_reinforced_canonicals + old_candidate_universe:pack:aux_vtrac_index_overdue` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + translation_sandbox:diagnostic_boxed_seed` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + shadow_policy:primary_cluster_canonicals` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackA_vt8:canonical + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackB_mirror3rd:canonical + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + survivor:survivor_frontier_canonicals` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::brain1:dominant_canonicals + old_candidate_universe:pack:aux_vtrac_index_overdue` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:convergence_box_first:B36` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
