# Stage 2 Signal False-Positive Scorecard

Purpose: add denominator discipline before promoting winner-aligned signals into scoring logic.

Important: `false_positive_proxy` means a value was exposed and did not match a same-day winner in this completed window. It is a denominator proxy, not proof the signal is useless.

## Denominators

- Seed state-days audited: `84`
- Winner events in audited state-days: `163`
- Signal exposure rows: `79778`
- Source scorecard rows: `88`
- Signal pools: `8377`
- Candidate-universe pack combos included: `False`

## Decision Mix

- `boxed_context_or_negative_control`: `55`
- `straight_context_or_negative_control`: `15`
- `boxed_supporting_gate`: `10`
- `vtrac_context_only`: `6`
- `vtrac_watch_decay_only_until_box_pairing`: `1`
- `denominator_only_broad_control`: `1`

## Top Fixture/Support Candidates

- `old_candidate_universe:pack:PackB_mirror3rd` lane=`boxed` active=`56` avg_pool=`3.0` lane_rate=`2.4%` lift=`2.64` decision=`boxed_supporting_gate`
- `brain1:dominant_canonicals` lane=`boxed` active=`84` avg_pool=`11.9` lane_rate=`0.9%` lift=`1.02` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:hot_zones_top:canonical` lane=`boxed` active=`84` avg_pool=`8.0` lane_rate=`0.7%` lift=`0.84` decision=`boxed_supporting_gate`
- `brain1:secondary_canonicals` lane=`boxed` active=`84` avg_pool=`12.0` lane_rate=`0.7%` lift=`0.79` decision=`boxed_supporting_gate`
- `old_play_card:budgeted_canonicals_top` lane=`boxed` active=`84` avg_pool=`17.6` lane_rate=`0.7%` lift=`0.77` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack:aux_positional` lane=`boxed` active=`60` avg_pool=`8.0` lane_rate=`0.6%` lift=`0.69` decision=`boxed_supporting_gate`
- `old_candidate_universe:top_canonicals` lane=`boxed` active=`84` avg_pool=`12.0` lane_rate=`0.6%` lift=`0.67` decision=`boxed_supporting_gate`
- `translation_sandbox:diagnostic_boxed_seed` lane=`boxed` active=`84` avg_pool=`16.0` lane_rate=`0.5%` lift=`0.59` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:aux_positional:canonical` lane=`boxed` active=`84` avg_pool=`9.7` lane_rate=`0.5%` lift=`0.56` decision=`boxed_supporting_gate`
- `positional:positional_canonical` lane=`boxed` active=`84` avg_pool=`7.8` lane_rate=`0.5%` lift=`0.52` decision=`boxed_supporting_gate`

## Broad Control / Context Sources

- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`vtrac` exposures=`370` avg_pool=`4.4` false_proxy=`93.0%` decision=`vtrac_context_only`
- `board_scoreboard:top_vtrac_indices` lane=`vtrac` exposures=`336` avg_pool=`4.0` false_proxy=`93.8%` decision=`vtrac_context_only`
- `brain1:watchlist_indices` lane=`vtrac` exposures=`503` avg_pool=`6.0` false_proxy=`94.4%` decision=`vtrac_context_only`
- `brain1:dominant_vtrac_indices` lane=`vtrac` exposures=`699` avg_pool=`8.3` false_proxy=`94.8%` decision=`vtrac_context_only`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` lane=`vtrac` exposures=`624` avg_pool=`10.4` false_proxy=`95.2%` decision=`vtrac_context_only`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` lane=`vtrac` exposures=`1464` avg_pool=`3.0` false_proxy=`97.8%` decision=`vtrac_context_only`
- `old_candidate_universe:candidate_universe_union_combo` lane=`straight` exposures=`13792` avg_pool=`164.2` false_proxy=`94.7%` decision=`denominator_only_broad_control`

## Guardrail

- This scorecard is a promotion filter, not a scoring rewrite.
- A source can support a translator fixture without being safe as a standalone bet selector.
- VTRAC sources remain watch/decay territory until paired with narrower boxed or exact evidence.
