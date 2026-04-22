# Wrong-Lane Restraint Rules

Purpose: prevent VTRAC/territory evidence from being over-promoted into boxed/straight action.

- Wrong-lane cases: `15`
- VTRAC-related stack rows: `570`

## Rules

- VTRAC-only evidence may mark territory/watch/carryforward, but should not create a boxed/straight spend by itself.
- A VTRAC source needs a bounded boxed or exact confirmation source before translator promotion.
- Broad VTRAC stacks with high false-positive proxy stay negative-control/context surfaces.
- Wrong-lane cases must be included as regression tests before any translator promotion.

## Highest-Support VTRAC Stacks

- `vtrac_box_confirmation::old_candidate_universe:candidate_universe_union_combo + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`31.0%` wrong_lane_events=`14`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:candidate_universe_union_combo` decision=`vtrac_box_confirmation_watch` event_support=`27.4%` wrong_lane_events=`11`
- `vtrac_overlap::brain1:dominant_vtrac_indices + translation_sandbox:diagnostic_vt_box_seed` decision=`context_stack` event_support=`27.4%` wrong_lane_events=`10`
- `vtrac_box_confirmation::brain1:secondary_canonicals + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`23.8%` wrong_lane_events=`11`
- `vtrac_box_confirmation::translation_sandbox:diagnostic_boxed_seed + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`22.6%` wrong_lane_events=`9`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack_method:stable_top:canonical` decision=`vtrac_box_confirmation_watch` event_support=`22.6%` wrong_lane_events=`7`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:stable_top:canonical + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`22.6%` wrong_lane_events=`7`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack:stable_top` decision=`vtrac_box_confirmation_watch` event_support=`20.2%` wrong_lane_events=`5`
- `vtrac_box_confirmation::old_candidate_universe:pack:stable_top + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`20.2%` wrong_lane_events=`5`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_play_card:strategy:v0_2_default:B36:combos` decision=`vtrac_box_confirmation_watch` event_support=`19.0%` wrong_lane_events=`4`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + translation_sandbox:diagnostic_boxed_seed` decision=`vtrac_box_confirmation_watch` event_support=`19.0%` wrong_lane_events=`6`
- `vtrac_box_confirmation::old_play_card:strategy:v0_2_default:B36:combos + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`19.0%` wrong_lane_events=`4`
- `vtrac_box_confirmation::blackapple:recommended_canonicals + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`17.9%` wrong_lane_events=`9`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_play_card:budgeted_canonicals_top` decision=`vtrac_box_confirmation_watch` event_support=`17.9%` wrong_lane_events=`4`
- `vtrac_overlap::brain1:dominant_vtrac_indices + brain1:watchlist_indices` decision=`context_stack` event_support=`17.9%` wrong_lane_events=`6`
- `vtrac_box_confirmation::old_play_card:budgeted_canonicals_top + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`17.9%` wrong_lane_events=`4`
- `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:candidate_universe_union_combo` decision=`vtrac_box_confirmation_watch` event_support=`17.9%` wrong_lane_events=`6`
- `vtrac_box_confirmation::old_candidate_universe:candidate_universe_union_combo + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` decision=`vtrac_box_confirmation_watch` event_support=`16.7%` wrong_lane_events=`5`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + brain1:secondary_canonicals` decision=`vtrac_box_confirmation_watch` event_support=`16.7%` wrong_lane_events=`7`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_play_card:strategy:conversion_box_first:B24:combos` decision=`vtrac_box_confirmation_watch` event_support=`16.7%` wrong_lane_events=`3`
