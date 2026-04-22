# Wrong-Lane Restraint Rules

Purpose: prevent VTRAC/territory evidence from being over-promoted into boxed/straight action.

- Wrong-lane cases: `51`
- VTRAC-related stack rows: `578`

## Rules

- VTRAC-only evidence may mark territory/watch/carryforward, but should not create a boxed/straight spend by itself.
- A VTRAC source needs a bounded boxed or exact confirmation source before translator promotion.
- Broad VTRAC stacks with high false-positive proxy stay negative-control/context surfaces.
- Wrong-lane cases must be included as regression tests before any translator promotion.

## Highest-Support VTRAC Stacks

- `vtrac_box_confirmation::old_candidate_universe:candidate_universe_union_combo + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`32.6%` wrong_lane_events=`45`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:stable_top:canonical + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`27.6%` wrong_lane_events=`38`
- `vtrac_box_confirmation::old_candidate_universe:pack:stable_top + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`26.2%` wrong_lane_events=`35`
- `vtrac_overlap::brain1:dominant_vtrac_indices + translation_sandbox:diagnostic_vt_box_seed` decision=`context_stack` event_support=`22.6%` wrong_lane_events=`27`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:candidate_universe_union_combo` decision=`vtrac_box_confirmation_watch` event_support=`21.9%` wrong_lane_events=`27`
- `vtrac_box_confirmation::old_play_card:strategy:v0_2_default:B36:combos + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`21.3%` wrong_lane_events=`22`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack_method:stable_top:canonical` decision=`vtrac_box_confirmation_watch` event_support=`20.9%` wrong_lane_events=`26`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack:stable_top` decision=`vtrac_box_confirmation_watch` event_support=`19.9%` wrong_lane_events=`24`
- `vtrac_box_confirmation::translation_sandbox:diagnostic_boxed_seed + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`19.9%` wrong_lane_events=`15`
- `vtrac_box_confirmation::brain1:dominant_canonicals + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`19.3%` wrong_lane_events=`20`
- `vtrac_box_confirmation::brain1:secondary_canonicals + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`18.9%` wrong_lane_events=`17`
- `vtrac_box_confirmation::old_play_card:strategy:analysis_prefix:B36:combos + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_context_stack` event_support=`17.9%` wrong_lane_events=`14`
- `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:candidate_universe_union_combo` decision=`vtrac_context_stack` event_support=`17.3%` wrong_lane_events=`18`
- `vtrac_box_confirmation::old_play_card:budgeted_canonicals_top + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_context_stack` event_support=`17.3%` wrong_lane_events=`14`
- `vtrac_overlap::brain1:watchlist_indices + translation_sandbox:diagnostic_vt_box_seed` decision=`context_stack` event_support=`16.9%` wrong_lane_events=`18`
- `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:pack_method:stable_top:canonical` decision=`vtrac_context_stack` event_support=`16.9%` wrong_lane_events=`18`
- `vtrac_box_confirmation::brain1:dominant_canonicals + brain1:dominant_vtrac_indices` decision=`vtrac_context_stack` event_support=`16.9%` wrong_lane_events=`17`
- `vtrac_box_confirmation::old_play_card:strategy:v0_2_default:B24:combos + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_context_stack` event_support=`16.9%` wrong_lane_events=`10`
- `vtrac_overlap::brain1:dominant_vtrac_indices + brain1:watchlist_indices` decision=`context_stack` event_support=`16.3%` wrong_lane_events=`17`
- `vtrac_box_confirmation::shadow_policy:primary_cluster_canonicals + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_context_stack` event_support=`15.9%` wrong_lane_events=`15`
