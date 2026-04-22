# Stage 2 Signal False-Positive Scorecard

Purpose: add denominator discipline before promoting winner-aligned signals into scoring logic.

Important: `false_positive_proxy` means a value was exposed and did not match a same-day winner in this completed window. It is a denominator proxy, not proof the signal is useless.

## Denominators

- Seed state-days audited: `56`
- Winner events in audited state-days: `109`
- Signal exposure rows: `56657`
- Source scorecard rows: `88`
- Signal pools: `5511`
- Candidate-universe pack combos included: `False`

## Decision Mix

- `boxed_context_or_negative_control`: `44`
- `boxed_supporting_gate`: `19`
- `straight_context_or_negative_control`: `15`
- `vtrac_context_only`: `6`
- `sample_too_small`: `2`
- `vtrac_watch_decay_only_until_box_pairing`: `1`
- `denominator_only_broad_control`: `1`

## Top Fixture/Support Candidates

- `old_candidate_universe:pack_method:mirror_pair_closure:canonical` lane=`boxed` active=`56` avg_pool=`3.0` lane_rate=`3.0%` lift=`3.36` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack:mirror_pair_closure` lane=`boxed` active=`56` avg_pool=`6.0` lane_rate=`3.0%` lift=`3.36` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack:R-perm-4` lane=`boxed` active=`56` avg_pool=`4.0` lane_rate=`2.7%` lift=`3.03` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:R-perm-4:canonical` lane=`boxed` active=`56` avg_pool=`4.0` lane_rate=`2.7%` lift=`3.03` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:convergence_box_first:B36` lane=`boxed` active=`56` avg_pool=`8.0` lane_rate=`2.0%` lift=`2.27` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` lane=`boxed` active=`56` avg_pool=`8.0` lane_rate=`2.0%` lift=`2.27` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` lane=`boxed` active=`56` avg_pool=`8.0` lane_rate=`2.0%` lift=`2.27` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` lane=`boxed` active=`56` avg_pool=`8.0` lane_rate=`2.0%` lift=`2.27` decision=`boxed_supporting_gate`
- `brain1:dominant_canonicals` lane=`boxed` active=`56` avg_pool=`12.0` lane_rate=`1.3%` lift=`1.52` decision=`boxed_supporting_gate`
- `brain1:secondary_canonicals` lane=`boxed` active=`56` avg_pool=`12.0` lane_rate=`1.2%` lift=`1.35` decision=`boxed_supporting_gate`
- `positional:positional_canonical` lane=`boxed` active=`56` avg_pool=`7.9` lane_rate=`1.1%` lift=`1.28` decision=`boxed_supporting_gate`
- `blackapple:recommended_canonicals` lane=`boxed` active=`56` avg_pool=`8.0` lane_rate=`1.1%` lift=`1.26` decision=`boxed_supporting_gate`
- `translation_sandbox:diagnostic_boxed_seed` lane=`boxed` active=`56` avg_pool=`16.0` lane_rate=`1.1%` lift=`1.26` decision=`boxed_supporting_gate`
- `old_play_card:budgeted_canonicals_top` lane=`boxed` active=`56` avg_pool=`17.6` lane_rate=`1.1%` lift=`1.26` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack:stable_top` lane=`boxed` active=`56` avg_pool=`18.8` lane_rate=`1.0%` lift=`1.18` decision=`boxed_supporting_gate`
- `brain1:context_reinforced_canonicals` lane=`boxed` active=`56` avg_pool=`5.8` lane_rate=`0.9%` lift=`1.05` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:aux_positional:canonical` lane=`boxed` active=`56` avg_pool=`9.7` lane_rate=`0.9%` lift=`1.04` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:stable_top:canonical` lane=`boxed` active=`56` avg_pool=`10.0` lane_rate=`0.8%` lift=`0.94` decision=`boxed_supporting_gate`
- `old_candidate_universe:top_canonicals` lane=`boxed` active=`56` avg_pool=`12.0` lane_rate=`0.7%` lift=`0.84` decision=`boxed_supporting_gate`

## Broad Control / Context Sources

- `old_candidate_universe:pack:aux_vtrac_index_overdue` lane=`vtrac` exposures=`308` avg_pool=`8.8` false_proxy=`90.3%` decision=`vtrac_context_only`
- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`vtrac` exposures=`260` avg_pool=`4.6` false_proxy=`91.5%` decision=`vtrac_context_only`
- `board_scoreboard:top_vtrac_indices` lane=`vtrac` exposures=`224` avg_pool=`4.0` false_proxy=`92.0%` decision=`vtrac_context_only`
- `brain1:watchlist_indices` lane=`vtrac` exposures=`336` avg_pool=`6.0` false_proxy=`93.2%` decision=`vtrac_context_only`
- `brain1:dominant_vtrac_indices` lane=`vtrac` exposures=`484` avg_pool=`8.6` false_proxy=`93.4%` decision=`vtrac_context_only`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` lane=`vtrac` exposures=`896` avg_pool=`2.7` false_proxy=`96.0%` decision=`vtrac_context_only`
- `old_candidate_universe:candidate_universe_union_combo` lane=`straight` exposures=`11381` avg_pool=`203.2` false_proxy=`93.3%` decision=`denominator_only_broad_control`

## Guardrail

- This scorecard is a promotion filter, not a scoring rewrite.
- A source can support a translator fixture without being safe as a standalone bet selector.
- VTRAC sources remain watch/decay territory until paired with narrower boxed or exact evidence.
