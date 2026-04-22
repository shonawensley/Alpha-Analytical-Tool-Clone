# Stage 2 Signal False-Positive Scorecard

Purpose: add denominator discipline before promoting winner-aligned signals into scoring logic.

Important: `false_positive_proxy` means a value was exposed and did not match a same-day winner in this completed window. It is a denominator proxy, not proof the signal is useless.

## Denominators

- Seed state-days audited: `210`
- Winner events in audited state-days: `414`
- Signal exposure rows: `211689`
- Source scorecard rows: `88`
- Signal pools: `20703`
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

- `old_candidate_universe:pack:aux_positional` lane=`boxed` active=`39` avg_pool=`8.0` lane_rate=`1.9%` lift=`2.12` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:aux_positional:canonical` lane=`boxed` active=`210` avg_pool=`9.7` lane_rate=`1.1%` lift=`1.20` decision=`boxed_supporting_gate`
- `positional:positional_canonical` lane=`boxed` active=`210` avg_pool=`7.8` lane_rate=`1.0%` lift=`1.15` decision=`boxed_supporting_gate`
- `blackapple:recommended_canonicals` lane=`boxed` active=`210` avg_pool=`8.0` lane_rate=`1.0%` lift=`1.13` decision=`boxed_supporting_gate`
- `survivor:survivor_frontier_canonicals` lane=`boxed` active=`210` avg_pool=`8.0` lane_rate=`1.0%` lift=`1.13` decision=`boxed_supporting_gate`
- `brain1:dominant_canonicals` lane=`boxed` active=`210` avg_pool=`12.0` lane_rate=`1.0%` lift=`1.11` decision=`boxed_supporting_gate`
- `brain1:secondary_canonicals` lane=`boxed` active=`210` avg_pool=`12.0` lane_rate=`0.9%` lift=`0.97` decision=`boxed_supporting_gate`
- `translation_sandbox:diagnostic_boxed_seed` lane=`boxed` active=`210` avg_pool=`16.0` lane_rate=`0.8%` lift=`0.90` decision=`boxed_supporting_gate`
- `old_play_card:budgeted_canonicals_top` lane=`boxed` active=`210` avg_pool=`17.7` lane_rate=`0.8%` lift=`0.87` decision=`boxed_supporting_gate`
- `old_candidate_universe:top_canonicals` lane=`boxed` active=`210` avg_pool=`12.0` lane_rate=`0.7%` lift=`0.80` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:stable_top:canonical` lane=`boxed` active=`210` avg_pool=`10.0` lane_rate=`0.7%` lift=`0.76` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack:stable_top` lane=`boxed` active=`210` avg_pool=`19.7` lane_rate=`0.7%` lift=`0.76` decision=`boxed_supporting_gate`

## Broad Control / Context Sources

- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`vtrac` exposures=`975` avg_pool=`4.6` false_proxy=`91.3%` decision=`vtrac_context_only`
- `brain1:dominant_vtrac_indices` lane=`vtrac` exposures=`1762` avg_pool=`8.4` false_proxy=`93.5%` decision=`vtrac_context_only`
- `brain1:watchlist_indices` lane=`vtrac` exposures=`1259` avg_pool=`6.0` false_proxy=`93.6%` decision=`vtrac_context_only`
- `board_scoreboard:top_vtrac_indices` lane=`vtrac` exposures=`840` avg_pool=`4.0` false_proxy=`93.7%` decision=`vtrac_context_only`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` lane=`vtrac` exposures=`858` avg_pool=`8.8` false_proxy=`94.4%` decision=`vtrac_context_only`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` lane=`vtrac` exposures=`3100` avg_pool=`2.6` false_proxy=`97.7%` decision=`vtrac_context_only`
- `old_candidate_universe:candidate_universe_union_combo` lane=`straight` exposures=`42317` avg_pool=`201.5` false_proxy=`94.6%` decision=`denominator_only_broad_control`

## Guardrail

- This scorecard is a promotion filter, not a scoring rewrite.
- A source can support a translator fixture without being safe as a standalone bet selector.
- VTRAC sources remain watch/decay territory until paired with narrower boxed or exact evidence.
