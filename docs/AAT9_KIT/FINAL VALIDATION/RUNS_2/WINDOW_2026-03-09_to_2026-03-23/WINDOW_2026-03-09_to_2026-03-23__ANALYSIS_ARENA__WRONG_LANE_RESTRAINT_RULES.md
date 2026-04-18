# Wrong-Lane Restraint Rules

Purpose: prevent VTRAC/territory evidence from being over-promoted into boxed/straight action.

- Wrong-lane cases: `66`
- VTRAC-related stack rows: `574`

## Rules

- VTRAC-only evidence may mark territory/watch/carryforward, but should not create a boxed/straight spend by itself.
- A VTRAC source needs a bounded boxed or exact confirmation source before translator promotion.
- Broad VTRAC stacks with high false-positive proxy stay negative-control/context surfaces.
- Wrong-lane cases must be included as regression tests before any translator promotion.

## Highest-Support VTRAC Stacks

- `vtrac_box_confirmation::old_candidate_universe:candidate_universe_union_combo + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`35.0%` wrong_lane_events=`64`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:stable_top:canonical + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`29.0%` wrong_lane_events=`49`
- `vtrac_overlap::brain1:dominant_vtrac_indices + translation_sandbox:diagnostic_vt_box_seed` decision=`context_stack` event_support=`28.0%` wrong_lane_events=`43`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:candidate_universe_union_combo` decision=`vtrac_box_confirmation_watch` event_support=`26.8%` wrong_lane_events=`43`
- `vtrac_box_confirmation::old_candidate_universe:pack:stable_top + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`26.6%` wrong_lane_events=`45`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack_method:stable_top:canonical` decision=`vtrac_box_confirmation_watch` event_support=`24.4%` wrong_lane_events=`40`
- `vtrac_box_confirmation::translation_sandbox:diagnostic_boxed_seed + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`23.9%` wrong_lane_events=`34`
- `vtrac_box_confirmation::brain1:secondary_canonicals + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`22.7%` wrong_lane_events=`38`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack:stable_top` decision=`vtrac_box_confirmation_watch` event_support=`22.7%` wrong_lane_events=`36`
- `vtrac_box_confirmation::old_play_card:strategy:v0_2_default:B36:combos + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`21.5%` wrong_lane_events=`24`
- `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:candidate_universe_union_combo` decision=`vtrac_box_confirmation_watch` event_support=`20.0%` wrong_lane_events=`27`
- `vtrac_box_confirmation::brain1:dominant_canonicals + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`19.8%` wrong_lane_events=`24`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + translation_sandbox:diagnostic_boxed_seed` decision=`vtrac_box_confirmation_watch` event_support=`19.1%` wrong_lane_events=`25`
- `vtrac_overlap::brain1:watchlist_indices + translation_sandbox:diagnostic_vt_box_seed` decision=`context_stack` event_support=`18.8%` wrong_lane_events=`26`
- `vtrac_box_confirmation::old_play_card:strategy:v0_2_default:B24:combos + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`18.6%` wrong_lane_events=`15`
- `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:pack_method:stable_top:canonical` decision=`vtrac_box_confirmation_watch` event_support=`18.6%` wrong_lane_events=`25`
- `vtrac_box_confirmation::brain1:dominant_canonicals + brain1:dominant_vtrac_indices` decision=`vtrac_box_confirmation_watch` event_support=`18.6%` wrong_lane_events=`22`
- `vtrac_box_confirmation::shadow_policy:primary_cluster_canonicals + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`18.1%` wrong_lane_events=`22`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + shadow_policy:primary_cluster_canonicals` decision=`vtrac_box_confirmation_watch` event_support=`18.1%` wrong_lane_events=`22`
- `vtrac_box_confirmation::old_play_card:strategy:analysis_prefix:B36:combos + translation_sandbox:diagnostic_vt_box_seed` decision=`vtrac_box_confirmation_watch` event_support=`18.1%` wrong_lane_events=`14`
