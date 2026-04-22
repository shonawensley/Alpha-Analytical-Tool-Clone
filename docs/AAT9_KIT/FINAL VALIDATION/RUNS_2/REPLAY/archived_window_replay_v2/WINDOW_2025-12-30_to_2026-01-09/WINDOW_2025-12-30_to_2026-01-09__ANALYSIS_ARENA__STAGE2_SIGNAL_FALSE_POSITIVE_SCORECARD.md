# Stage 2 Signal False-Positive Scorecard

Purpose: add denominator discipline before promoting winner-aligned signals into scoring logic.

Important: `false_positive_proxy` means a value was exposed and did not match a same-day winner in this completed window. It is a denominator proxy, not proof the signal is useless.

## Denominators

- Seed state-days audited: `154`
- Winner events in audited state-days: `301`
- Signal exposure rows: `156360`
- Source scorecard rows: `88`
- Signal pools: `15164`
- Candidate-universe pack combos included: `False`

## Decision Mix

- `boxed_context_or_negative_control`: `52`
- `straight_context_or_negative_control`: `15`
- `boxed_supporting_gate`: `12`
- `vtrac_context_only`: `6`
- `vtrac_watch_decay_only_until_box_pairing`: `1`
- `sample_too_small`: `1`
- `denominator_only_broad_control`: `1`

## Top Fixture/Support Candidates

- `blackapple:recommended_canonicals` lane=`boxed` active=`154` avg_pool=`8.0` lane_rate=`1.2%` lift=`1.37` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack:aux_positional` lane=`boxed` active=`22` avg_pool=`8.0` lane_rate=`1.1%` lift=`1.25` decision=`boxed_supporting_gate`
- `old_play_card:strategy:play_box_first:B36:boxed_canonicals` lane=`boxed` active=`154` avg_pool=`9.1` lane_rate=`0.9%` lift=`1.04` decision=`boxed_supporting_gate`
- `old_candidate_universe:top_canonicals` lane=`boxed` active=`154` avg_pool=`12.0` lane_rate=`0.9%` lift=`1.04` decision=`boxed_supporting_gate`
- `brain1:dominant_canonicals` lane=`boxed` active=`154` avg_pool=`11.9` lane_rate=`0.8%` lift=`0.92` decision=`boxed_supporting_gate`
- `brain1:secondary_canonicals` lane=`boxed` active=`154` avg_pool=`12.0` lane_rate=`0.8%` lift=`0.91` decision=`boxed_supporting_gate`
- `old_play_card:budgeted_canonicals_top` lane=`boxed` active=`154` avg_pool=`17.6` lane_rate=`0.8%` lift=`0.87` decision=`boxed_supporting_gate`
- `translation_sandbox:diagnostic_boxed_seed` lane=`boxed` active=`154` avg_pool=`16.0` lane_rate=`0.8%` lift=`0.87` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:aux_positional:canonical` lane=`boxed` active=`154` avg_pool=`9.8` lane_rate=`0.7%` lift=`0.75` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:stable_top:canonical` lane=`boxed` active=`154` avg_pool=`10.0` lane_rate=`0.6%` lift=`0.71` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack:stable_top` lane=`boxed` active=`154` avg_pool=`18.8` lane_rate=`0.6%` lift=`0.66` decision=`boxed_supporting_gate`
- `positional:positional_canonical` lane=`boxed` active=`154` avg_pool=`7.8` lane_rate=`0.6%` lift=`0.65` decision=`boxed_supporting_gate`

## Broad Control / Context Sources

- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`vtrac` exposures=`688` avg_pool=`4.5` false_proxy=`93.2%` decision=`vtrac_context_only`
- `board_scoreboard:top_vtrac_indices` lane=`vtrac` exposures=`616` avg_pool=`4.0` false_proxy=`94.3%` decision=`vtrac_context_only`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` lane=`vtrac` exposures=`1076` avg_pool=`9.8` false_proxy=`94.4%` decision=`vtrac_context_only`
- `brain1:watchlist_indices` lane=`vtrac` exposures=`923` avg_pool=`6.0` false_proxy=`94.5%` decision=`vtrac_context_only`
- `brain1:dominant_vtrac_indices` lane=`vtrac` exposures=`1305` avg_pool=`8.5` false_proxy=`94.9%` decision=`vtrac_context_only`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` lane=`vtrac` exposures=`2654` avg_pool=`3.0` false_proxy=`96.9%` decision=`vtrac_context_only`
- `old_candidate_universe:candidate_universe_union_combo` lane=`straight` exposures=`31348` avg_pool=`203.6` false_proxy=`94.6%` decision=`denominator_only_broad_control`

## Guardrail

- This scorecard is a promotion filter, not a scoring rewrite.
- A source can support a translator fixture without being safe as a standalone bet selector.
- VTRAC sources remain watch/decay territory until paired with narrower boxed or exact evidence.
