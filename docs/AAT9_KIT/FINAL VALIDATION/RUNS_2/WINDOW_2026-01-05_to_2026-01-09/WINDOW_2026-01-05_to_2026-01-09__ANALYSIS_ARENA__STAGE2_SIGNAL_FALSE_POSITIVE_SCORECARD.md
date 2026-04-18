# Stage 2 Signal False-Positive Scorecard

Purpose: add denominator discipline before promoting winner-aligned signals into scoring logic.

Important: `false_positive_proxy` means a value was exposed and did not match a same-day winner in this completed window. It is a denominator proxy, not proof the signal is useless.

## Denominators

- Seed state-days audited: `70`
- Winner events in audited state-days: `138`
- Signal exposure rows: `71030`
- Source scorecard rows: `88`
- Signal pools: `6894`
- Candidate-universe pack combos included: `False`

## Decision Mix

- `boxed_context_or_negative_control`: `45`
- `boxed_supporting_gate`: `19`
- `straight_context_or_negative_control`: `15`
- `vtrac_context_only`: `7`
- `sample_too_small`: `1`
- `denominator_only_broad_control`: `1`

## Top Fixture/Support Candidates

- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` lane=`boxed` active=`70` avg_pool=`3.3` lane_rate=`2.2%` lift=`2.44` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12` lane=`boxed` active=`70` avg_pool=`3.3` lane_rate=`2.2%` lift=`2.44` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12` lane=`boxed` active=`70` avg_pool=`3.3` lane_rate=`2.2%` lift=`2.43` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:convergence_box_first:B12` lane=`boxed` active=`70` avg_pool=`3.3` lane_rate=`2.2%` lift=`2.42` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:due_doubles_mirror_single:canonical` lane=`boxed` active=`70` avg_pool=`2.0` lane_rate=`2.1%` lift=`2.39` decision=`boxed_supporting_gate`
- `blackapple:recommended_canonicals` lane=`boxed` active=`70` avg_pool=`8.0` lane_rate=`1.6%` lift=`1.79` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:convergence_box_first:B36` lane=`boxed` active=`70` avg_pool=`8.0` lane_rate=`1.4%` lift=`1.60` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` lane=`boxed` active=`70` avg_pool=`8.0` lane_rate=`1.4%` lift=`1.60` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` lane=`boxed` active=`70` avg_pool=`8.0` lane_rate=`1.4%` lift=`1.60` decision=`boxed_supporting_gate`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` lane=`boxed` active=`70` avg_pool=`8.0` lane_rate=`1.4%` lift=`1.60` decision=`boxed_supporting_gate`
- `old_play_card:strategy:play_box_first:B36:boxed_canonicals` lane=`boxed` active=`70` avg_pool=`9.1` lane_rate=`1.4%` lift=`1.57` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack:aux_positional` lane=`boxed` active=`10` avg_pool=`8.0` lane_rate=`1.2%` lift=`1.38` decision=`boxed_supporting_gate`
- `old_candidate_universe:top_canonicals` lane=`boxed` active=`70` avg_pool=`12.0` lane_rate=`1.2%` lift=`1.33` decision=`boxed_supporting_gate`
- `old_play_card:budgeted_canonicals_top` lane=`boxed` active=`70` avg_pool=`17.8` lane_rate=`1.0%` lift=`1.08` decision=`boxed_supporting_gate`
- `brain1:secondary_canonicals` lane=`boxed` active=`70` avg_pool=`12.0` lane_rate=`1.0%` lift=`1.06` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:aux_positional:canonical` lane=`boxed` active=`70` avg_pool=`9.8` lane_rate=`0.9%` lift=`0.97` decision=`boxed_supporting_gate`
- `translation_sandbox:diagnostic_boxed_seed` lane=`boxed` active=`70` avg_pool=`16.0` lane_rate=`0.8%` lift=`0.90` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack_method:stable_top:canonical` lane=`boxed` active=`70` avg_pool=`10.0` lane_rate=`0.7%` lift=`0.74` decision=`boxed_supporting_gate`
- `old_candidate_universe:pack:stable_top` lane=`boxed` active=`70` avg_pool=`18.7` lane_rate=`0.4%` lift=`0.43` decision=`boxed_supporting_gate`

## Broad Control / Context Sources

- `old_candidate_universe:pack:aux_vtrac_index_overdue` lane=`vtrac` exposures=`452` avg_pool=`9.0` false_proxy=`93.4%` decision=`vtrac_context_only`
- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` lane=`vtrac` exposures=`318` avg_pool=`4.5` false_proxy=`93.4%` decision=`vtrac_context_only`
- `translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` exposures=`838` avg_pool=`12.0` false_proxy=`94.3%` decision=`vtrac_context_only`
- `brain1:watchlist_indices` lane=`vtrac` exposures=`420` avg_pool=`6.0` false_proxy=`94.5%` decision=`vtrac_context_only`
- `brain1:dominant_vtrac_indices` lane=`vtrac` exposures=`606` avg_pool=`8.7` false_proxy=`94.9%` decision=`vtrac_context_only`
- `board_scoreboard:top_vtrac_indices` lane=`vtrac` exposures=`280` avg_pool=`4.0` false_proxy=`95.0%` decision=`vtrac_context_only`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` lane=`vtrac` exposures=`1190` avg_pool=`2.9` false_proxy=`95.8%` decision=`vtrac_context_only`
- `old_candidate_universe:candidate_universe_union_combo` lane=`straight` exposures=`14122` avg_pool=`201.7` false_proxy=`94.4%` decision=`denominator_only_broad_control`

## Guardrail

- This scorecard is a promotion filter, not a scoring rewrite.
- A source can support a translator fixture without being safe as a standalone bet selector.
- VTRAC sources remain watch/decay territory until paired with narrower boxed or exact evidence.
