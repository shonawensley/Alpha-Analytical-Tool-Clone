# Wrong-Lane Restraint Rules

Purpose: prevent VTRAC/territory evidence from being over-promoted into boxed/straight action.

- Wrong-lane cases: `0`
- VTRAC-related stack rows: `578`

## Rules

- VTRAC-only evidence may mark territory/watch/carryforward, but should not create a boxed/straight spend by itself.
- A VTRAC source needs a bounded boxed or exact confirmation source before translator promotion.
- Broad VTRAC stacks with high false-positive proxy stay negative-control/context surfaces.
- Wrong-lane cases must be included as regression tests before any translator promotion.

## Highest-Support VTRAC Stacks

- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:PackA_vt8:canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:PackB_mirror3rd:canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackA_vt8:canonical + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackB_mirror3rd:canonical + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:consensus_double_9:canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack:mirror_pair_closure` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:mirror_pair_closure:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:mirror_pair_closure + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_candidate_universe:pack_method:mirror_pair_closure:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_positional + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack:aux_vtrac_index_overdue` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:R-perm-4 + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_candidate_universe:pack_method:R-perm-4:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:R-perm-4:canonical + old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackA_vt8:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:PackB_mirror3rd:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`vtrac_box_confirmation_watch` event_support=`0.0%` wrong_lane_events=`0`
- `vtrac_box_confirmation::board_scoreboard:top_vtrac_indices + old_play_card:strategy:v0_2_default:B24:boxed_canonicals` decision=`sample_too_small_stack` event_support=`0.0%` wrong_lane_events=`0`
