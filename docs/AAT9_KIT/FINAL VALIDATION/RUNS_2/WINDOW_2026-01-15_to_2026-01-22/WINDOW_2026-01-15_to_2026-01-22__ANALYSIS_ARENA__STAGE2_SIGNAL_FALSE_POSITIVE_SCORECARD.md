# Stage 2 Signal False-Positive Scorecard

Purpose: add denominator discipline before promoting winner-aligned signals into scoring logic.

Important: `false_positive_proxy` means a value was exposed and did not match a same-day winner in this completed window. It is a denominator proxy, not proof the signal is useless.

## Denominators

- Seed state-days audited: `112`
- Winner events in audited state-days: `221`
- Signal exposure rows: `105332`
- Source scorecard rows: `89`
- Signal pools: `11211`
- Candidate-universe pack combos included: `False`

## Decision Mix

- `boxed_context_or_negative_control`: `56`
- `straight_context_or_negative_control`: `15`
- `boxed_supporting_gate`: `10`
- `vtrac_context_only`: `6`
- `vtrac_watch_decay_only_until_box_pairing`: `1`
- `denominator_only_broad_control`: `1`

## Top Fixture/Support Candidates

- `old_candidate_universe:pack_method:mirror_pair_closure:canonical` lane=`boxed` active=`112` avg_pool=`3.0` lane_rate=`2.2%` lift=`2.49` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack:mirror_pair_closure` lane=`boxed` active=`112` avg_pool=`6.0` lane_rate=`2.2%` lift=`2.49` decision=`boxed_supporting_gate`
- `positional:positional_canonical` lane=`boxed` active=`112` avg_pool=`7.9` lane_rate=`1.0%` lift=`1.13` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack:aux_positional` lane=`boxed` active=`74` avg_pool=`8.0` lane_rate=`1.0%` lift=`1.12` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:aux_positional:canonical` lane=`boxed` active=`112` avg_pool=`9.8` lane_rate=`0.9%` lift=`1.02` decision=`boxed_supporting_gate`
- `brain1:dominant_canonicals` lane=`boxed` active=`112` avg_pool=`12.0` lane_rate=`0.9%` lift=`1.00` decision=`boxed_supporting_gate`
- `blackapple:recommended_canonicals` lane=`boxed` active=`112` avg_pool=`8.0` lane_rate=`0.9%` lift=`1.00` decision=`boxed_supporting_gate`
- `brain1:secondary_canonicals` lane=`boxed` active=`112` avg_pool=`12.0` lane_rate=`0.9%` lift=`1.00` decision=`boxed_supporting_gate`
- `translation_sandbox:diagnostic_boxed_seed` lane=`boxed` active=`112` avg_pool=`16.0` lane_rate=`0.8%` lift=`0.93` decision=`boxed_supporting_gate`
- `old_play_card:budgeted_canonicals_top` lane=`boxed` active=`112` avg_pool=`17.7` lane_rate=`0.6%` lift=`0.68` decision=`boxed_supporting_gate`

## Broad Control / Context Sources

- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`vtrac` exposures=`514` avg_pool=`4.6` false_proxy=`91.4%` decision=`vtrac_context_only`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` lane=`vtrac` exposures=`592` avg_pool=`8.8` false_proxy=`91.6%` decision=`vtrac_context_only`
- `board_scoreboard:top_vtrac_indices` lane=`vtrac` exposures=`448` avg_pool=`4.0` false_proxy=`92.6%` decision=`vtrac_context_only`
- `brain1:watchlist_indices` lane=`vtrac` exposures=`672` avg_pool=`6.0` false_proxy=`93.8%` decision=`vtrac_context_only`
- `brain1:dominant_vtrac_indices` lane=`vtrac` exposures=`979` avg_pool=`8.7` false_proxy=`93.8%` decision=`vtrac_context_only`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` lane=`vtrac` exposures=`1774` avg_pool=`2.6` false_proxy=`96.8%` decision=`vtrac_context_only`
- `old_candidate_universe:candidate_universe_union_combo` lane=`straight` exposures=`17932` avg_pool=`160.1` false_proxy=`94.2%` decision=`denominator_only_broad_control`

## Guardrail

- This scorecard is a promotion filter, not a scoring rewrite.
- A source can support a translator fixture without being safe as a standalone bet selector.
- VTRAC sources remain watch/decay territory until paired with narrower boxed or exact evidence.
