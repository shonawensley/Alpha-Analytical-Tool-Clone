# Stage 2 Signal False-Positive Scorecard

Purpose: add denominator discipline before promoting winner-aligned signals into scoring logic.

Important: `false_positive_proxy` means a value was exposed and did not match a same-day winner in this completed window. It is a denominator proxy, not proof the signal is useless.

## Denominators

- Seed state-days audited: `42`
- Winner events in audited state-days: `84`
- Signal exposure rows: `42685`
- Source scorecard rows: `88`
- Signal pools: `4147`
- Candidate-universe pack combos included: `False`

## Decision Mix

- `boxed_context_or_negative_control`: `45`
- `boxed_supporting_gate`: `18`
- `straight_context_or_negative_control`: `15`
- `vtrac_context_only`: `5`
- `vtrac_watch_decay_only_until_box_pairing`: `2`
- `sample_too_small`: `2`
- `denominator_only_broad_control`: `1`

## Top Fixture/Support Candidates

- `old_candidate_universe:pack:PackB_mirror3rd` lane=`boxed` active=`15` avg_pool=`3.0` lane_rate=`2.2%` lift=`2.44` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:aux_positional:canonical` lane=`boxed` active=`42` avg_pool=`9.9` lane_rate=`1.2%` lift=`1.33` decision=`boxed_supporting_gate`
- `positional:positional_canonical` lane=`boxed` active=`42` avg_pool=`7.9` lane_rate=`1.2%` lift=`1.32` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:convergence_box_first:B36` lane=`boxed` active=`42` avg_pool=`8.0` lane_rate=`1.2%` lift=`1.31` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` lane=`boxed` active=`42` avg_pool=`8.0` lane_rate=`1.2%` lift=`1.31` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` lane=`boxed` active=`42` avg_pool=`8.0` lane_rate=`1.2%` lift=`1.31` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` lane=`boxed` active=`42` avg_pool=`8.0` lane_rate=`1.2%` lift=`1.31` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:conversion_box_first:B36` lane=`boxed` active=`42` avg_pool=`7.5` lane_rate=`1.0%` lift=`1.05` decision=`boxed_supporting_gate`
- `old_play_card:strategy:conversion_box_first:B36:boxed_canonicals` lane=`boxed` active=`42` avg_pool=`7.7` lane_rate=`0.9%` lift=`1.02` decision=`boxed_supporting_gate`
- `old_play_card:strategy:play_box_first:B36:boxed_canonicals` lane=`boxed` active=`42` avg_pool=`8.5` lane_rate=`0.8%` lift=`0.92` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:stable_top:canonical` lane=`boxed` active=`42` avg_pool=`10.0` lane_rate=`0.7%` lift=`0.79` decision=`boxed_supporting_gate`
- `old_play_card:budgeted_canonicals_top` lane=`boxed` active=`42` avg_pool=`17.6` lane_rate=`0.7%` lift=`0.74` decision=`boxed_supporting_gate`
- `brain1:dominant_canonicals` lane=`boxed` active=`42` avg_pool=`12.0` lane_rate=`0.6%` lift=`0.65` decision=`boxed_supporting_gate`
- `old_candidate_universe:top_canonicals` lane=`boxed` active=`42` avg_pool=`12.0` lane_rate=`0.6%` lift=`0.65` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack:stable_top` lane=`boxed` active=`42` avg_pool=`19.5` lane_rate=`0.5%` lift=`0.54` decision=`boxed_supporting_gate`
- `translation_sandbox:diagnostic_boxed_seed` lane=`boxed` active=`42` avg_pool=`16.0` lane_rate=`0.4%` lift=`0.49` decision=`boxed_supporting_gate`
- `blackapple:recommended_canonicals` lane=`boxed` active=`42` avg_pool=`8.0` lane_rate=`0.3%` lift=`0.33` decision=`boxed_supporting_gate`
- `brain1:secondary_canonicals` lane=`boxed` active=`42` avg_pool=`12.0` lane_rate=`0.2%` lift=`0.22` decision=`boxed_supporting_gate`

## Broad Control / Context Sources

- `board_scoreboard:top_vtrac_indices` lane=`vtrac` exposures=`168` avg_pool=`4.0` false_proxy=`92.3%` decision=`vtrac_context_only`
- `brain1:dominant_vtrac_indices` lane=`vtrac` exposures=`366` avg_pool=`8.7` false_proxy=`93.4%` decision=`vtrac_context_only`
- `brain1:watchlist_indices` lane=`vtrac` exposures=`252` avg_pool=`6.0` false_proxy=`94.0%` decision=`vtrac_context_only`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` lane=`vtrac` exposures=`210` avg_pool=`8.8` false_proxy=`94.3%` decision=`vtrac_context_only`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` lane=`vtrac` exposures=`656` avg_pool=`2.5` false_proxy=`98.2%` decision=`vtrac_context_only`
- `old_candidate_universe:candidate_universe_union_combo` lane=`straight` exposures=`8708` avg_pool=`207.3` false_proxy=`94.1%` decision=`denominator_only_broad_control`

## Guardrail

- This scorecard is a promotion filter, not a scoring rewrite.
- A source can support a translator fixture without being safe as a standalone bet selector.
- VTRAC sources remain watch/decay territory until paired with narrower boxed or exact evidence.
