# Analysis Arena Case Dossiers

These are representative March-window cases chosen to inspect how evidence moved from tools into Arena, candidates, play-card, frontier, and decay.

## 1. successful_straight_or_exact: 2026-01-22 OntarioCanada4 Evening winner `544`

- Outcome: `STRAIGHT`
- Evidence status: `CAPTURED_AND_USED`
- Board rank: `10`; sharp=`3`, territory=`4`, broad=`7`
- Frontier: `HIDDEN_COMPRESSED_FRONTIER` strength=`STRONG` score=`85.005`
- State-day decay first resolution: `same_day_carryforward` event=`2026-01-22 Evening 544`
- Exact sources: `candidate_universe_exact|play_card_exact_any|play_card_b24_exact|play_card_b36_exact`
- Box sources: `brain1_dominant_canonicals|diagnostic_boxed_seed|arena_box_rollup|candidate_universe_box|play_card_box_any|play_card_b24_box|play_card_b36_box|top_canonicals|dominant_canonicals|pack:stable_top|budgeted_canonicals_top|strategy_card:convergence_box_first:B24|strategy_card:convergence_box_first:B36|strategy_card:conversion_box_first:B36|strategy_card:conversion_box_first_conditional_lenient_presetA:B24|strategy_card:conversion_box_first_conditional_lenient_presetA:B36`
- VTRAC sources: `brain1_dominant_vtrac|diagnostic_vt_seed|top_canonicals|top_vtrac_indices|dominant_canonicals|context_reinforced_canonicals|secondary_canonicals|survivor_frontier_canonicals|dominant_vtrac_indices|watchlist_indices|recommended_canonicals|example_canonicals|implied_canonicals|top_profit_alerts|diagnostic_boxed_seed|diagnostic_straight_seed`
- Diagnosis: Evidence reached downstream conversion; preserve as positive translator example.

Top winner-aligned pre-draw signals:
- `arena:arena_box_rollup` value=`TRUE` mode=`BOX` tier=`A` stage=`arena`
- `arena:brain1_dominant_canonicals` value=`TRUE` mode=`BOX` tier=`A` stage=`arena`
- `board_scoreboard:top_canonicals` value=`445` mode=`BOX` tier=`A` stage=`brain2_board`
- `brain1:dominant_canonicals` value=`445` mode=`BOX` tier=`A` stage=`arena`
- `old_candidate_universe:pack:stable_top` value=`445` mode=`BOX` tier=`A` stage=`candidate_universe`
- `old_candidate_universe:top_canonicals` value=`445` mode=`BOX` tier=`A` stage=`candidate_universe`
- `old_play_card:budgeted_canonicals_top` value=`445` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b24_box` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b24_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:play_card_b36_box` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b36_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:play_card_box_any` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`

## 2. successful_straight_or_exact: 2026-01-21 Pennsylvania4 Evening winner `816`

- Outcome: `STRAIGHT`
- Evidence status: `CAPTURED_AND_USED`
- Board rank: `11`; sharp=`2`, territory=`4`, broad=`6`
- Frontier: `HIDDEN_COMPRESSED_FRONTIER` strength=`MEDIUM` score=`60.594`
- State-day decay first resolution: `direct_same_outcome` event=`2026-01-21 Midday 848`
- Exact sources: `diagnostic_straight_seed|arena_exact_rollup|candidate_universe_exact|play_card_exact_any|play_card_b12_exact|play_card_b24_exact|play_card_b36_exact|ranked_candidate_combo|straight_seed_decay_resolution`
- Box sources: `candidate_universe_box|play_card_box_any|play_card_b12_box|play_card_b24_box|play_card_b36_box|diagnostic_straight_seed|pack:mirror_pair_closure|budgeted_canonicals_top|ranked_candidate_combo|ranked_candidate_canonical|strategy_card:analysis_prefix:B12|strategy_card:analysis_prefix:B24|strategy_card:analysis_prefix:B36|strategy_card:convergence_box_first:B36|strategy_card:conversion_box_first:B12|strategy_card:conversion_box_first:B24`
- VTRAC sources: `brain1_dominant_vtrac|diagnostic_vt_seed|dominant_vtrac_indices|diagnostic_straight_seed|diagnostic_vt_box_seed|pack:stable_top|pack:mirror_pair_closure|budgeted_canonicals_top|ranked_candidate_combo|ranked_candidate_canonical|strategy_card:analysis_prefix:B12|strategy_card:analysis_prefix:B24|strategy_card:analysis_prefix:B36|strategy_card:convergence_box_first:B36|strategy_card:conversion_box_first:B12|strategy_card:conversion_box_first:B24`
- Diagnosis: Evidence reached downstream conversion; preserve as positive translator example.

Top winner-aligned pre-draw signals:
- `arena:arena_exact_rollup` value=`TRUE` mode=`EXACT` tier=`A` stage=`arena`
- `old_candidate_universe:pack:mirror_pair_closure` value=`168` mode=`BOX` tier=`A` stage=`candidate_universe`
- `old_play_card:budgeted_canonicals_top` value=`168` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b12_box` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b12_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:play_card_b24_box` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b24_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:play_card_b36_box` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b36_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:play_card_box_any` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_exact_any` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:ranked_candidate_canonical` value=`168` mode=`BOX` tier=`A` stage=`play_card`

## 3. successful_straight_or_exact: 2026-01-21 NewYork4 Evening winner `233`

- Outcome: `STRAIGHT`
- Evidence status: `CAPTURED_AND_USED`
- Board rank: `7`; sharp=`2`, territory=`4`, broad=`6`
- Frontier: `HIDDEN_COMPRESSED_FRONTIER` strength=`STRONG` score=`83.304`
- State-day decay first resolution: `same_day_carryforward` event=`2026-01-21 Evening 233`
- Exact sources: `candidate_universe_exact|play_card_exact_any|play_card_b12_exact|play_card_b24_exact|play_card_b36_exact|straight_seed_decay_resolution`
- Box sources: `brain1_context_canonicals|diagnostic_boxed_seed|arena_box_rollup|candidate_universe_box|play_card_box_any|play_card_b12_box|play_card_b24_box|play_card_b36_box|context_reinforced_canonicals|positional_combo|positional_canonical|diagnostic_straight_seed|top_canonicals|pack:stable_top|budgeted_canonicals_top|strategy_card:convergence_box_first:B12`
- VTRAC sources: `brain1_dominant_vtrac|diagnostic_vt_seed|top_canonicals|top_vtrac_indices|dominant_canonicals|context_reinforced_canonicals|secondary_canonicals|dominant_vtrac_indices|watchlist_indices|example_canonicals|implied_canonicals|top_profit_alerts|positional_combo|positional_canonical|diagnostic_boxed_seed|diagnostic_straight_seed`
- Diagnosis: Evidence reached downstream conversion; preserve as positive translator example.

Top winner-aligned pre-draw signals:
- `arena:arena_box_rollup` value=`TRUE` mode=`BOX` tier=`A` stage=`arena`
- `arena:brain1_context_canonicals` value=`TRUE` mode=`BOX` tier=`A` stage=`arena`
- `brain1:context_reinforced_canonicals` value=`233` mode=`BOX` tier=`A` stage=`arena`
- `old_candidate_universe:pack:stable_top` value=`233` mode=`BOX` tier=`A` stage=`candidate_universe`
- `old_candidate_universe:top_canonicals` value=`233` mode=`BOX` tier=`A` stage=`candidate_universe`
- `old_play_card:budgeted_canonicals_top` value=`233` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b12_box` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b12_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:play_card_b24_box` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b24_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:play_card_b36_box` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b36_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`

## 4. successful_straight_or_exact: 2026-01-20 Virginia4 Midday winner `260`

- Outcome: `STRAIGHT`
- Evidence status: `CAPTURED_AND_USED`
- Board rank: `14`; sharp=`0`, territory=`2`, broad=`7`
- Frontier: `FEEDER_TO_FRONTIER` strength=`MEDIUM` score=`54.887`
- State-day decay first resolution: `future_day_decay` event=`2026-01-21 Midday 314`
- Exact sources: `candidate_universe_exact|play_card_exact_any|play_card_b24_exact|play_card_b36_exact`
- Box sources: `candidate_universe_box|play_card_box_any|play_card_b24_box|play_card_b36_box|top_canonicals|budgeted_canonicals_top|strategy_card:convergence_box_first:B24|strategy_card:convergence_box_first:B36|strategy_card:conversion_box_first_conditional_lenient_presetA:B24|strategy_card:conversion_box_first_conditional_lenient_presetA:B36|strategy_card:conversion_box_first_conditional_lenient_presetB:B24|strategy_card:conversion_box_first_conditional_lenient_presetB:B36|strategy_card:conversion_box_first_conditional_strict_presetA:B24|strategy_card:conversion_box_first_conditional_strict_presetA:B36|box_core_decay_resolution|boxed_seed_decay_resolution`
- VTRAC sources: `context_reinforced_canonicals|positional_combo|positional_canonical|diagnostic_boxed_seed|diagnostic_straight_seed|top_canonicals|budgeted_canonicals_top|strategy_card:convergence_box_first:B24|strategy_card:convergence_box_first:B36|strategy_card:conversion_box_first_conditional_lenient_presetA:B24|strategy_card:conversion_box_first_conditional_lenient_presetA:B36|strategy_card:conversion_box_first_conditional_lenient_presetB:B24|strategy_card:conversion_box_first_conditional_lenient_presetB:B36|strategy_card:conversion_box_first_conditional_strict_presetA:B24|strategy_card:conversion_box_first_conditional_strict_presetA:B36|primary_cluster_context`
- Diagnosis: Evidence reached downstream conversion; preserve as positive translator example.

Top winner-aligned pre-draw signals:
- `old_candidate_universe:top_canonicals` value=`026` mode=`BOX` tier=`A` stage=`candidate_universe`
- `old_play_card:budgeted_canonicals_top` value=`026` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b24_box` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b24_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:play_card_b36_box` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b36_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:play_card_box_any` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_exact_any` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:strategy_card:convergence_box_first:B24` value=`026` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:strategy_card:convergence_box_first:B36` value=`026` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` value=`026` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` value=`026` mode=`BOX` tier=`A` stage=`play_card`

## 5. successful_box_conversion: 2026-01-21 Ohio4 Evening winner `740`

- Outcome: `BOX_ANY`
- Evidence status: `CAPTURED_AND_USED`
- Board rank: `9`; sharp=`0`, territory=`2`, broad=`5`
- Frontier: `HIDDEN_COMPRESSED_FRONTIER` strength=`STRONG` score=`76.989`
- State-day decay first resolution: `future_day_decay` event=`2026-01-22 Midday 217`
- Exact sources: `candidate_universe_exact`
- Box sources: `candidate_universe_box|pack:R-perm-4|box_core_decay_resolution|boxed_seed_decay_resolution|preserved_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `top_canonicals|pack:R-perm-4|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution|c1_c2_signature`
- Diagnosis: Evidence reached downstream conversion; preserve as positive translator example.

Top winner-aligned pre-draw signals:
- `old_candidate_universe:pack:R-perm-4` value=`047` mode=`BOX` tier=`A` stage=`candidate_universe`
- `translation_sandbox:boxed_seed_decay_resolution` value=`2026-01-23 Evening 242` mode=`BOX` tier=`A` stage=`decay_scorecard`
- `arena:box_total_decay_resolution` value=`2026-01-23 Midday 709` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:vtrac_total_decay_resolution` value=`2026-01-22 Midday 217` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-23 Evening 242` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-24 Evening 484` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `control_arm:preserved_decay_resolution` value=`2026-01-23 Midday 709` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `old_candidate_universe:candidate_universe_box` value=`TRUE` mode=`BOX` tier=`B` stage=`candidate_universe`
- `old_candidate_universe:candidate_universe_exact` value=`TRUE` mode=`EXACT` tier=`B` stage=`candidate_universe`
- `old_candidate_universe:pack:R-perm-4` value=`079` mode=`VTRAC_BOX` tier=`B` stage=`candidate_universe`
- `old_candidate_universe:top_canonicals` value=`079` mode=`VTRAC_BOX` tier=`B` stage=`candidate_universe`
- `tracker:blackapple_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`

## 6. successful_box_conversion: 2026-01-20 Pennsylvania4 Midday winner `218`

- Outcome: `BOX_ANY`
- Evidence status: `CAPTURED_AND_USED`
- Board rank: `11`; sharp=`0`, territory=`1`, broad=`7`
- Frontier: `HIDDEN_COMPRESSED_FRONTIER` strength=`MEDIUM` score=`61.236`
- State-day decay first resolution: `future_day_decay` event=`2026-01-21 Midday 848`
- Exact sources: `-`
- Box sources: `candidate_universe_box|positional_combo|positional_canonical|diagnostic_straight_seed|box_core_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `positional_combo|positional_canonical|diagnostic_straight_seed|pack:stable_top|top_vtrac_indices_decay_resolution|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution|c1_c2_signature`
- Diagnosis: Evidence reached downstream conversion; preserve as positive translator example.

Top winner-aligned pre-draw signals:
- `positional:positional_canonical` value=`128` mode=`BOX` tier=`A` stage=`tracker`
- `positional:positional_combo` value=`128` mode=`BOX` tier=`A` stage=`tracker`
- `translation_sandbox:diagnostic_straight_seed` value=`128` mode=`BOX` tier=`A` stage=`arena`
- `arena:box_total_decay_resolution` value=`2026-01-24 Midday 984` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:vtrac_total_decay_resolution` value=`2026-01-21 Midday 848` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_vtrac_indices_decay_resolution` value=`2026-01-24 Midday 984` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-24 Midday 984` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-21 Midday 848` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `old_candidate_universe:candidate_universe_box` value=`TRUE` mode=`BOX` tier=`B` stage=`candidate_universe`
- `old_candidate_universe:pack:stable_top` value=`178` mode=`VTRAC_BOX` tier=`B` stage=`candidate_universe`
- `positional:positional_canonical` value=`123` mode=`VTRAC_BOX` tier=`B` stage=`tracker`
- `positional:positional_combo` value=`123` mode=`VTRAC_BOX` tier=`B` stage=`tracker`

## 7. successful_box_conversion: 2026-01-21 Michigan4 Midday winner `220`

- Outcome: `BOX_ANY`
- Evidence status: `CAPTURED_AND_USED`
- Board rank: `5`; sharp=`0`, territory=`2`, broad=`6`
- Frontier: `FAMILY_FRONTIER` strength=`STRONG` score=`72.884`
- State-day decay first resolution: `direct_same_outcome` event=`2026-01-21 Midday 220`
- Exact sources: `-`
- Box sources: `top_canonicals_decay_resolution|box_core_decay_resolution|boxed_seed_decay_resolution|box_total_decay_resolution|c1_c2_signature`
- VTRAC sources: `brain1_dominant_vtrac|diagnostic_vt_seed|top_vtrac_indices|context_reinforced_canonicals|secondary_canonicals|dominant_vtrac_indices|watchlist_indices|recommended_canonicals|diagnostic_boxed_seed|diagnostic_vt_box_seed|pack:stable_top|primary_cluster_context|top_vtrac_indices_decay_resolution|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution`
- Diagnosis: Evidence reached downstream conversion; preserve as positive translator example.

Top winner-aligned pre-draw signals:
- `translation_sandbox:boxed_seed_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`A` stage=`decay_scorecard`
- `arena:box_total_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:brain1_dominant_vtrac` value=`TRUE` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `arena:vtrac_total_decay_resolution` value=`2026-01-21 Midday 220` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `blackapple:recommended_canonicals` value=`027` mode=`VTRAC_BOX` tier=`B` stage=`tracker`
- `board_scoreboard:top_canonicals_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_vtrac_indices` value=`10` mode=`VTRAC_BOX` tier=`B` stage=`brain2_board`
- `board_scoreboard:top_vtrac_indices_decay_resolution` value=`2026-01-21 Midday 220` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:context_reinforced_canonicals` value=`077` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:dominant_vtrac_indices` value=`10` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:secondary_canonicals` value=`027` mode=`VTRAC_BOX` tier=`B` stage=`arena`

## 8. successful_box_conversion: 2026-01-21 Florida4 Midday winner `350`

- Outcome: `BOX_ANY`
- Evidence status: `CAPTURED_AND_USED`
- Board rank: `3`; sharp=`0`, territory=`4`, broad=`7`
- Frontier: `VTRAC_FRONTIER` strength=`MEDIUM` score=`57.814`
- State-day decay first resolution: `direct_same_outcome` event=`2026-01-21 Midday 350`
- Exact sources: `candidate_universe_exact`
- Box sources: `candidate_universe_box|positional_combo|positional_canonical|diagnostic_straight_seed|pack:mirror_pair_closure`
- VTRAC sources: `brain1_dominant_vtrac|diagnostic_vt_seed|top_canonicals|dominant_canonicals|context_reinforced_canonicals|secondary_canonicals|dominant_vtrac_indices|implied_canonicals|top_profit_alerts|positional_combo|positional_canonical|diagnostic_boxed_seed|diagnostic_straight_seed|diagnostic_vt_box_seed|pack:stable_top|pack:mirror_pair_closure`
- Diagnosis: Evidence reached downstream conversion; preserve as positive translator example.

Top winner-aligned pre-draw signals:
- `old_candidate_universe:pack:mirror_pair_closure` value=`035` mode=`BOX` tier=`A` stage=`candidate_universe`
- `positional:positional_canonical` value=`035` mode=`BOX` tier=`A` stage=`tracker`
- `positional:positional_combo` value=`035` mode=`BOX` tier=`A` stage=`tracker`
- `translation_sandbox:diagnostic_straight_seed` value=`035` mode=`BOX` tier=`A` stage=`arena`
- `arena:brain1_dominant_vtrac` value=`TRUE` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `arena:vtrac_total_decay_resolution` value=`2026-01-21 Midday 350` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_canonicals` value=`008` mode=`VTRAC_BOX` tier=`B` stage=`brain2_board`
- `brain1:context_reinforced_canonicals` value=`008` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:dominant_canonicals` value=`008` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:dominant_vtrac_indices` value=`4` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:secondary_canonicals` value=`008` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-21 Midday 350` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`

## 9. box_gap: 2026-01-22 Virginia4 Evening winner `100`

- Outcome: `BOX_GAP`
- Evidence status: `CAPTURED_BUT_UNDERUSED`
- Board rank: `14`; sharp=`3`, territory=`0`, broad=`7`
- Frontier: `HIDDEN_COMPRESSED_FRONTIER` strength=`MEDIUM` score=`59.246`
- State-day decay first resolution: `same_day_carryforward` event=`2026-01-22 Evening 100`
- Exact sources: `-`
- Box sources: `brain1_dominant_canonicals|diagnostic_boxed_seed|arena_box_rollup|dominant_canonicals|survivor_frontier_canonicals|primary_cluster_survivor_frontier|box_core_decay_resolution|boxed_seed_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `dominant_canonicals|survivor_frontier_canonicals|positional_combo|positional_canonical|diagnostic_boxed_seed|diagnostic_straight_seed|pack:mirror_pair_closure|pack:aux_positional|budgeted_canonicals_top|ranked_candidate_combo|ranked_candidate_canonical|strategy_card:conversion_box_first:B24|strategy_card:conversion_box_first:B36|primary_cluster_survivor_frontier|c1_c2_signature`
- Diagnosis: High-value training case: evidence existed but old final selection did not budget/select it cleanly.

Top winner-aligned pre-draw signals:
- `arena:arena_box_rollup` value=`TRUE` mode=`BOX` tier=`A` stage=`arena`
- `arena:brain1_dominant_canonicals` value=`TRUE` mode=`BOX` tier=`A` stage=`arena`
- `brain1:dominant_canonicals` value=`001` mode=`BOX` tier=`A` stage=`arena`
- `shadow_policy:primary_cluster_survivor_frontier` value=`001` mode=`BOX` tier=`A` stage=`shadow`
- `survivor:survivor_frontier_canonicals` value=`001` mode=`BOX` tier=`A` stage=`arena`
- `translation_sandbox:boxed_seed_decay_resolution` value=`2026-01-22 Evening 100` mode=`BOX` tier=`A` stage=`decay_scorecard`
- `translation_sandbox:diagnostic_boxed_seed` value=`TRUE` mode=`BOX` tier=`A` stage=`arena`
- `translation_sandbox:diagnostic_boxed_seed` value=`001` mode=`BOX` tier=`A` stage=`arena`
- `arena:box_total_decay_resolution` value=`2026-01-22 Evening 100` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-22 Evening 100` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `old_candidate_universe:pack:aux_positional` value=`015` mode=`VTRAC_BOX` tier=`B` stage=`candidate_universe`
- `old_candidate_universe:pack:mirror_pair_closure` value=`015` mode=`VTRAC_BOX` tier=`B` stage=`candidate_universe`

## 10. box_gap: 2026-01-21 NorthCarolina4 Evening winner `577`

- Outcome: `BOX_GAP`
- Evidence status: `CAPTURED_BUT_UNDERUSED`
- Board rank: `8`; sharp=`2`, territory=`4`, broad=`7`
- Frontier: `HIDDEN_COMPRESSED_FRONTIER` strength=`MEDIUM` score=`63.772`
- State-day decay first resolution: `direct_same_outcome` event=`2026-01-21 Midday 767`
- Exact sources: `candidate_universe_exact|play_card_exact_any|play_card_b24_exact|play_card_b36_exact`
- Box sources: `brain1_dominant_canonicals|arena_box_rollup|candidate_universe_box|dominant_canonicals|box_core_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `brain1_dominant_vtrac|diagnostic_vt_seed|top_canonicals|top_vtrac_indices|dominant_canonicals|survivor_frontier_canonicals|dominant_vtrac_indices|watchlist_indices|diagnostic_boxed_seed|diagnostic_straight_seed|diagnostic_vt_box_seed|pack:stable_top|pack:due_doubles|budgeted_canonicals_top|ranked_candidate_combo|ranked_candidate_canonical`
- Diagnosis: High-value training case: evidence existed but old final selection did not budget/select it cleanly.

Top winner-aligned pre-draw signals:
- `arena:arena_box_rollup` value=`TRUE` mode=`BOX` tier=`A` stage=`arena`
- `arena:brain1_dominant_canonicals` value=`TRUE` mode=`BOX` tier=`A` stage=`arena`
- `brain1:dominant_canonicals` value=`577` mode=`BOX` tier=`A` stage=`arena`
- `old_play_card:play_card_b24_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:play_card_b36_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:play_card_exact_any` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `arena:box_total_decay_resolution` value=`2026-01-21 Evening 577` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:brain1_dominant_vtrac` value=`TRUE` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `arena:vtrac_total_decay_resolution` value=`2026-01-21 Midday 767` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_canonicals` value=`225` mode=`VTRAC_BOX` tier=`B` stage=`brain2_board`
- `board_scoreboard:top_vtrac_indices` value=`10` mode=`VTRAC_BOX` tier=`B` stage=`brain2_board`
- `board_scoreboard:top_vtrac_indices_decay_resolution` value=`2026-01-21 Evening 577` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`

## 11. vtrac_only_wrong_lane: 2026-01-21 Michigan4 Evening winner `221`

- Outcome: `VTRAC_ONLY`
- Evidence status: `CAPTURED_BUT_NOT_PROMOTED`
- Board rank: `5`; sharp=`0`, territory=`0`, broad=`6`
- Frontier: `FEEDER_TO_FRONTIER` strength=`MEDIUM` score=`63.874`
- State-day decay first resolution: `direct_same_outcome` event=`2026-01-21 Midday 220`
- Exact sources: `-`
- Box sources: `top_canonicals_decay_resolution|box_core_decay_resolution|boxed_seed_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `secondary_canonicals|example_canonicals|pack:stable_top|pack:R-perm-4|top_vtrac_indices_decay_resolution|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution|c1_c2_signature`
- Diagnosis: Some useful evidence existed, but final promotion remains unclear.

Top winner-aligned pre-draw signals:
- `translation_sandbox:boxed_seed_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`A` stage=`decay_scorecard`
- `arena:box_total_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:vtrac_total_decay_resolution` value=`2026-01-21 Midday 220` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_canonicals_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_vtrac_indices_decay_resolution` value=`2026-01-21 Midday 220` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:secondary_canonicals` value=`226` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-21 Midday 220` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `due_doubles:example_canonicals` value=`226` mode=`VTRAC_BOX` tier=`B` stage=`tracker`
- `old_candidate_universe:pack:R-perm-4` value=`127` mode=`VTRAC_BOX` tier=`B` stage=`candidate_universe`
- `old_candidate_universe:pack:stable_top` value=`177` mode=`VTRAC_BOX` tier=`B` stage=`candidate_universe`
- `tracker:blackapple_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`

## 12. vtrac_only_wrong_lane: 2026-01-20 Ohio4 Midday winner `556`

- Outcome: `VTRAC_ONLY`
- Evidence status: `CAPTURED_BUT_NOT_PROMOTED`
- Board rank: `9`; sharp=`0`, territory=`0`, broad=`7`
- Frontier: `FEEDER_TO_FRONTIER` strength=`MEDIUM` score=`59.644`
- State-day decay first resolution: `same_day_carryforward` event=`2026-01-20 Evening 843`
- Exact sources: `-`
- Box sources: `secondary_canonicals|example_canonicals|preserved_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `dominant_canonicals|secondary_canonicals|survivor_frontier_canonicals|example_canonicals|diagnostic_boxed_seed|primary_cluster_survivor_frontier|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution|c1_c2_signature`
- Diagnosis: Some useful evidence existed, but final promotion remains unclear.

Top winner-aligned pre-draw signals:
- `brain1:secondary_canonicals` value=`556` mode=`BOX` tier=`A` stage=`arena`
- `due_doubles:example_canonicals` value=`556` mode=`BOX` tier=`A` stage=`tracker`
- `arena:box_total_decay_resolution` value=`2026-01-23 Midday 709` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:vtrac_total_decay_resolution` value=`2026-01-20 Evening 843` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:dominant_canonicals` value=`006` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:secondary_canonicals` value=`001` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:secondary_canonicals` value=`155` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-20 Evening 843` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `control_arm:preserved_decay_resolution` value=`2026-01-23 Midday 709` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `due_doubles:example_canonicals` value=`001` mode=`VTRAC_BOX` tier=`B` stage=`tracker`
- `due_doubles:example_canonicals` value=`155` mode=`VTRAC_BOX` tier=`B` stage=`tracker`
- `shadow_policy:primary_cluster_survivor_frontier` value=`006` mode=`VTRAC_BOX` tier=`B` stage=`shadow`

## 13. vtrac_only_wrong_lane: 2026-01-21 OntarioCanada4 Midday winner `197`

- Outcome: `VTRAC_ONLY`
- Evidence status: `CAPTURED_BUT_WRONG_LANE`
- Board rank: `10`; sharp=`0`, territory=`2`, broad=`7`
- Frontier: `VTRAC_FRONTIER` strength=`MEDIUM` score=`51.822`
- State-day decay first resolution: `direct_same_outcome` event=`2026-01-21 Midday 197`
- Exact sources: `-`
- Box sources: `top_canonicals_decay_resolution|box_core_decay_resolution|boxed_seed_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `brain1_dominant_vtrac|diagnostic_vt_seed|dominant_canonicals|dominant_vtrac_indices|diagnostic_boxed_seed|diagnostic_vt_box_seed|budgeted_canonicals_top|strategy_card:convergence_box_first:B36|strategy_card:conversion_box_first_conditional_lenient_presetA:B36|strategy_card:conversion_box_first_conditional_lenient_presetB:B36|strategy_card:conversion_box_first_conditional_strict_presetA:B36|primary_cluster_canonicals|top_vtrac_indices_decay_resolution|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution`
- Diagnosis: Territory/VTRAC evidence was present, but boxed/straight conversion lane was not strong enough.

Top winner-aligned pre-draw signals:
- `translation_sandbox:boxed_seed_decay_resolution` value=`2026-01-22 Evening 544` mode=`BOX` tier=`A` stage=`decay_scorecard`
- `arena:box_total_decay_resolution` value=`2026-01-22 Evening 544` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:brain1_dominant_vtrac` value=`TRUE` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `arena:vtrac_total_decay_resolution` value=`2026-01-21 Midday 197` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_canonicals_decay_resolution` value=`2026-01-22 Evening 544` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_vtrac_indices_decay_resolution` value=`2026-01-21 Evening 199` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-22 Evening 544` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:dominant_canonicals` value=`246` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:dominant_vtrac_indices` value=`22` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-21 Midday 197` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `old_play_card:budgeted_canonicals_top` value=`246` mode=`VTRAC_BOX` tier=`B` stage=`play_card`
- `old_play_card:strategy_card:convergence_box_first:B36` value=`246` mode=`VTRAC_BOX` tier=`B` stage=`play_card`

## 14. vtrac_only_wrong_lane: 2026-01-21 Ohio4 Midday winner `649`

- Outcome: `VTRAC_ONLY`
- Evidence status: `DECAY_VALIDATED`
- Board rank: `9`; sharp=`0`, territory=`0`, broad=`5`
- Frontier: `FEEDER_TO_FRONTIER` strength=`WEAK` score=`45.539`
- State-day decay first resolution: `future_day_decay` event=`2026-01-22 Midday 217`
- Exact sources: `-`
- Box sources: `box_core_decay_resolution|boxed_seed_decay_resolution|preserved_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `positional_combo|positional_canonical|diagnostic_straight_seed|pack:mirror_pair_closure|budgeted_canonicals_top|strategy_card:convergence_box_first:B36|strategy_card:conversion_box_first:B36|strategy_card:conversion_box_first_conditional_lenient_presetA:B36|strategy_card:conversion_box_first_conditional_lenient_presetB:B36|strategy_card:conversion_box_first_conditional_strict_presetA:B36|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution|c1_c2_signature`
- Diagnosis: Same-day-only judgment would under-credit this state-day; keep in carryforward/decay lane.

Top winner-aligned pre-draw signals:
- `translation_sandbox:boxed_seed_decay_resolution` value=`2026-01-23 Evening 242` mode=`BOX` tier=`A` stage=`decay_scorecard`
- `arena:box_total_decay_resolution` value=`2026-01-23 Midday 709` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:vtrac_total_decay_resolution` value=`2026-01-22 Midday 217` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-23 Evening 242` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-24 Evening 484` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `control_arm:preserved_decay_resolution` value=`2026-01-23 Midday 709` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `old_candidate_universe:pack:mirror_pair_closure` value=`149` mode=`VTRAC_BOX` tier=`B` stage=`candidate_universe`
- `old_play_card:budgeted_canonicals_top` value=`149` mode=`VTRAC_BOX` tier=`B` stage=`play_card`
- `old_play_card:strategy_card:convergence_box_first:B36` value=`149` mode=`VTRAC_BOX` tier=`B` stage=`play_card`
- `old_play_card:strategy_card:conversion_box_first:B36` value=`149` mode=`VTRAC_BOX` tier=`B` stage=`play_card`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` value=`149` mode=`VTRAC_BOX` tier=`B` stage=`play_card`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` value=`149` mode=`VTRAC_BOX` tier=`B` stage=`play_card`

## 15. future_decay: 2026-01-21 PuertoRico4 Midday winner `328`

- Outcome: `STRAIGHT`
- Evidence status: `CAPTURED_AND_USED`
- Board rank: `12`; sharp=`0`, territory=`2`, broad=`5`
- Frontier: `FEEDER_TO_FRONTIER` strength=`WEAK` score=`41.402`
- State-day decay first resolution: `future_day_decay` event=`2026-01-24 Evening 269`
- Exact sources: `candidate_universe_exact|play_card_exact_any|play_card_b36_exact`
- Box sources: `candidate_universe_box|play_card_box_any|play_card_b36_box|pack:aux_vtrac_index_overdue|pack:R-perm-4|budgeted_canonicals_top`
- VTRAC sources: `pack:aux_vtrac_index_overdue|pack:R-perm-4|budgeted_canonicals_top|vt_seed_decay_resolution|vtrac_total_decay_resolution|c1_c2_signature`
- Diagnosis: Evidence reached downstream conversion; preserve as positive translator example.

Top winner-aligned pre-draw signals:
- `old_candidate_universe:pack:R-perm-4` value=`238` mode=`BOX` tier=`A` stage=`candidate_universe`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` value=`238` mode=`BOX` tier=`A` stage=`candidate_universe`
- `old_play_card:budgeted_canonicals_top` value=`238` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b36_box` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_b36_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:play_card_box_any` value=`TRUE` mode=`BOX` tier=`A` stage=`play_card`
- `old_play_card:play_card_exact_any` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `arena:vtrac_total_decay_resolution` value=`2026-01-24 Evening 269` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `old_candidate_universe:candidate_universe_box` value=`TRUE` mode=`BOX` tier=`B` stage=`candidate_universe`
- `old_candidate_universe:candidate_universe_exact` value=`TRUE` mode=`EXACT` tier=`B` stage=`candidate_universe`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` value=`233` mode=`VTRAC_BOX` tier=`B` stage=`candidate_universe`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` value=`288` mode=`VTRAC_BOX` tier=`B` stage=`candidate_universe`

## 16. future_decay: 2026-01-22 Ohio4 Evening winner `048`

- Outcome: `STRAIGHT`
- Evidence status: `CAPTURED_AND_USED`
- Board rank: `9`; sharp=`0`, territory=`2`, broad=`6`
- Frontier: `HIDDEN_COMPRESSED_FRONTIER` strength=`STRONG` score=`73.206`
- State-day decay first resolution: `future_day_decay` event=`2026-01-23 Midday 709`
- Exact sources: `candidate_universe_exact|play_card_exact_any|play_card_b36_exact`
- Box sources: `candidate_universe_box|pack:stable_top|box_core_decay_resolution|boxed_seed_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `pack:stable_top|pack:R-perm-4|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution|c1_c2_signature`
- Diagnosis: Evidence reached downstream conversion; preserve as positive translator example.

Top winner-aligned pre-draw signals:
- `old_candidate_universe:pack:stable_top` value=`048` mode=`BOX` tier=`A` stage=`candidate_universe`
- `old_play_card:play_card_b36_exact` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `old_play_card:play_card_exact_any` value=`TRUE` mode=`EXACT` tier=`A` stage=`play_card`
- `translation_sandbox:boxed_seed_decay_resolution` value=`2026-01-23 Evening 242` mode=`BOX` tier=`A` stage=`decay_scorecard`
- `arena:box_total_decay_resolution` value=`2026-01-23 Evening 242` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:vtrac_total_decay_resolution` value=`2026-01-23 Midday 709` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-23 Evening 242` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-23 Midday 709` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `old_candidate_universe:candidate_universe_box` value=`TRUE` mode=`BOX` tier=`B` stage=`candidate_universe`
- `old_candidate_universe:candidate_universe_exact` value=`TRUE` mode=`EXACT` tier=`B` stage=`candidate_universe`
- `old_candidate_universe:pack:R-perm-4` value=`089` mode=`VTRAC_BOX` tier=`B` stage=`candidate_universe`
- `tracker:blackapple_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`

## 17. future_decay: 2026-01-20 Michigan4 Evening winner `881`

- Outcome: `BOX_ANY`
- Evidence status: `CAPTURED_AND_USED`
- Board rank: `5`; sharp=`0`, territory=`1`, broad=`6`
- Frontier: `VTRAC_FRONTIER` strength=`MEDIUM` score=`53.808`
- State-day decay first resolution: `future_day_decay` event=`2026-01-21 Midday 220`
- Exact sources: `-`
- Box sources: `candidate_universe_box|top_canonicals_decay_resolution|box_core_decay_resolution|boxed_seed_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `pack:stable_top|top_vtrac_indices_decay_resolution|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution|c1_c2_signature`
- Diagnosis: Evidence reached downstream conversion; preserve as positive translator example.

Top winner-aligned pre-draw signals:
- `translation_sandbox:boxed_seed_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`A` stage=`decay_scorecard`
- `arena:box_total_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:vtrac_total_decay_resolution` value=`2026-01-21 Midday 220` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_canonicals_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_vtrac_indices_decay_resolution` value=`2026-01-21 Midday 220` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-21 Midday 220` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `old_candidate_universe:candidate_universe_box` value=`TRUE` mode=`BOX` tier=`B` stage=`candidate_universe`
- `old_candidate_universe:pack:stable_top` value=`688` mode=`VTRAC_BOX` tier=`B` stage=`candidate_universe`
- `tracker:blackapple_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:due_double_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:positional_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`

## 18. future_decay: 2026-01-22 Ohio4 Midday winner `217`

- Outcome: `BOX_ANY`
- Evidence status: `CAPTURED_AND_USED`
- Board rank: `9`; sharp=`0`, territory=`2`, broad=`6`
- Frontier: `VTRAC_FRONTIER` strength=`MEDIUM` score=`49.937`
- State-day decay first resolution: `future_day_decay` event=`2026-01-23 Midday 709`
- Exact sources: `candidate_universe_exact`
- Box sources: `candidate_universe_box|pack:mirror_pair_closure|box_core_decay_resolution|boxed_seed_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `pack:mirror_pair_closure|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution|c1_c2_signature`
- Diagnosis: Evidence reached downstream conversion; preserve as positive translator example.

Top winner-aligned pre-draw signals:
- `old_candidate_universe:pack:mirror_pair_closure` value=`127` mode=`BOX` tier=`A` stage=`candidate_universe`
- `translation_sandbox:boxed_seed_decay_resolution` value=`2026-01-23 Evening 242` mode=`BOX` tier=`A` stage=`decay_scorecard`
- `arena:box_total_decay_resolution` value=`2026-01-23 Evening 242` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:vtrac_total_decay_resolution` value=`2026-01-23 Midday 709` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-23 Evening 242` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-23 Midday 709` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `old_candidate_universe:candidate_universe_box` value=`TRUE` mode=`BOX` tier=`B` stage=`candidate_universe`
- `old_candidate_universe:candidate_universe_exact` value=`TRUE` mode=`EXACT` tier=`B` stage=`candidate_universe`
- `tracker:blackapple_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:due_double_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:positional_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:profit_alert_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`

## 19. frontier_promotion_candidate: 2026-01-22 Connecticut4 Midday winner `556`

- Outcome: `VTRAC_ONLY`
- Evidence status: `CAPTURED_BUT_WRONG_LANE`
- Board rank: `1`; sharp=`0`, territory=`2`, broad=`7`
- Frontier: `HIDDEN_COMPRESSED_FRONTIER` strength=`STRONG` score=`70.017`
- State-day decay first resolution: `direct_same_outcome` event=`2026-01-22 Midday 556`
- Exact sources: `-`
- Box sources: `-`
- VTRAC sources: `brain1_dominant_vtrac|diagnostic_vt_seed|top_canonicals|top_vtrac_indices|dominant_canonicals|secondary_canonicals|survivor_frontier_canonicals|dominant_vtrac_indices|watchlist_indices|recommended_canonicals|diagnostic_boxed_seed|diagnostic_vt_box_seed|pack:stable_top|budgeted_canonicals_top|primary_cluster_canonicals|primary_cluster_survivor_frontier`
- Diagnosis: Territory/VTRAC evidence was present, but boxed/straight conversion lane was not strong enough.

Top winner-aligned pre-draw signals:
- `arena:brain1_dominant_vtrac` value=`TRUE` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `arena:vtrac_total_decay_resolution` value=`2026-01-22 Midday 556` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `blackapple:recommended_canonicals` value=`015` mode=`VTRAC_BOX` tier=`B` stage=`tracker`
- `board_scoreboard:top_canonicals` value=`006` mode=`VTRAC_BOX` tier=`B` stage=`brain2_board`
- `board_scoreboard:top_vtrac_indices` value=`2` mode=`VTRAC_BOX` tier=`B` stage=`brain2_board`
- `board_scoreboard:top_vtrac_indices_decay_resolution` value=`2026-01-22 Midday 556` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:dominant_canonicals` value=`006` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:dominant_canonicals` value=`001` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:dominant_canonicals` value=`056` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:dominant_canonicals` value=`015` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:dominant_vtrac_indices` value=`2` mode=`VTRAC_BOX` tier=`B` stage=`arena`
- `brain1:secondary_canonicals` value=`015` mode=`VTRAC_BOX` tier=`B` stage=`arena`

## 20. no_conversion_control: 2026-01-22 NewYork4 Midday winner `981`

- Outcome: `NO_CONVERSION`
- Evidence status: `DECAY_VALIDATED`
- Board rank: `7`; sharp=`0`, territory=`0`, broad=`5`
- Frontier: `HIDDEN_COMPRESSED_FRONTIER` strength=`MEDIUM` score=`52.35`
- State-day decay first resolution: `future_day_decay` event=`2026-01-23 Evening 771`
- Exact sources: `straight_seed_decay_resolution`
- Box sources: `top_canonicals_decay_resolution|box_core_decay_resolution|boxed_seed_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `recommended_canonicals|top_vtrac_indices_decay_resolution|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution|c1_c2_signature`
- Diagnosis: Same-day-only judgment would under-credit this state-day; keep in carryforward/decay lane.

Top winner-aligned pre-draw signals:
- `translation_sandbox:boxed_seed_decay_resolution` value=`2026-01-23 Evening 771` mode=`BOX` tier=`A` stage=`decay_scorecard`
- `translation_sandbox:straight_seed_decay_resolution` value=`2026-01-25 Evening 183` mode=`EXACT` tier=`A` stage=`decay_scorecard`
- `arena:box_total_decay_resolution` value=`2026-01-23 Evening 771` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:vtrac_total_decay_resolution` value=`2026-01-23 Evening 771` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `blackapple:recommended_canonicals` value=`689` mode=`VTRAC_BOX` tier=`B` stage=`tracker`
- `board_scoreboard:top_canonicals_decay_resolution` value=`2026-01-23 Evening 771` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_vtrac_indices_decay_resolution` value=`2026-01-25 Evening 183` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-23 Evening 771` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-23 Evening 771` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `tracker:blackapple_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:due_double_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:positional_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`

## 21. no_conversion_control: 2026-01-22 OntarioCanada4 Midday winner `857`

- Outcome: `NO_CONVERSION`
- Evidence status: `CAPTURED_BUT_NOT_PROMOTED`
- Board rank: `10`; sharp=`0`, territory=`0`, broad=`7`
- Frontier: `VTRAC_FRONTIER` strength=`MEDIUM` score=`50.604`
- State-day decay first resolution: `same_day_carryforward` event=`2026-01-22 Evening 544`
- Exact sources: `-`
- Box sources: `top_canonicals_decay_resolution|box_core_decay_resolution|boxed_seed_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `positional_combo|positional_canonical|diagnostic_straight_seed|top_vtrac_indices_decay_resolution|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution|c1_c2_signature`
- Diagnosis: Some useful evidence existed, but final promotion remains unclear.

Top winner-aligned pre-draw signals:
- `translation_sandbox:boxed_seed_decay_resolution` value=`2026-01-22 Evening 544` mode=`BOX` tier=`A` stage=`decay_scorecard`
- `arena:box_total_decay_resolution` value=`2026-01-22 Evening 544` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:vtrac_total_decay_resolution` value=`2026-01-22 Evening 544` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_canonicals_decay_resolution` value=`2026-01-22 Evening 544` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_vtrac_indices_decay_resolution` value=`2026-01-22 Evening 544` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-22 Evening 544` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-22 Evening 544` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `positional:positional_canonical` value=`258` mode=`VTRAC_BOX` tier=`B` stage=`tracker`
- `positional:positional_combo` value=`825` mode=`VTRAC_BOX` tier=`B` stage=`tracker`
- `tracker:blackapple_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:compound_event_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:due_double_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`

## 22. no_conversion_control: 2026-01-20 Michigan4 Midday winner `616`

- Outcome: `NO_CONVERSION`
- Evidence status: `DECAY_VALIDATED`
- Board rank: `5`; sharp=`0`, territory=`0`, broad=`6`
- Frontier: `FEEDER_TO_FRONTIER` strength=`MEDIUM` score=`48.423`
- State-day decay first resolution: `future_day_decay` event=`2026-01-21 Midday 220`
- Exact sources: `-`
- Box sources: `top_canonicals_decay_resolution|box_core_decay_resolution|boxed_seed_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `top_vtrac_indices_decay_resolution|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution|c1_c2_signature`
- Diagnosis: Same-day-only judgment would under-credit this state-day; keep in carryforward/decay lane.

Top winner-aligned pre-draw signals:
- `translation_sandbox:boxed_seed_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`A` stage=`decay_scorecard`
- `arena:box_total_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:vtrac_total_decay_resolution` value=`2026-01-21 Midday 220` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_canonicals_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_vtrac_indices_decay_resolution` value=`2026-01-21 Midday 220` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-24 Midday 700` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-21 Midday 220` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `tracker:blackapple_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:due_double_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:positional_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:profit_alert_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:r_consensus_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`

## 23. no_conversion_control: 2026-01-20 NewJersey4 Evening winner `689`

- Outcome: `NO_CONVERSION`
- Evidence status: `CAPTURED_BUT_NOT_PROMOTED`
- Board rank: `6`; sharp=`0`, territory=`0`, broad=`7`
- Frontier: `HIDDEN_COMPRESSED_FRONTIER` strength=`MEDIUM` score=`52.136`
- State-day decay first resolution: `direct_same_outcome` event=`2026-01-20 Midday 866`
- Exact sources: `-`
- Box sources: `box_core_decay_resolution|boxed_seed_decay_resolution|box_total_decay_resolution`
- VTRAC sources: `top_vtrac_indices_decay_resolution|vtrac_core_decay_resolution|vt_seed_decay_resolution|vtrac_total_decay_resolution|c1_c2_signature`
- Diagnosis: Some useful evidence existed, but final promotion remains unclear.

Top winner-aligned pre-draw signals:
- `translation_sandbox:boxed_seed_decay_resolution` value=`2026-01-23 Evening 843` mode=`BOX` tier=`A` stage=`decay_scorecard`
- `arena:box_total_decay_resolution` value=`2026-01-23 Evening 843` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `arena:vtrac_total_decay_resolution` value=`2026-01-20 Midday 866` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `board_scoreboard:top_vtrac_indices_decay_resolution` value=`2026-01-23 Evening 843` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `brain1:box_core_decay_resolution` value=`2026-01-23 Evening 843` mode=`BOX` tier=`B` stage=`decay_scorecard`
- `brain1:vtrac_core_decay_resolution` value=`2026-01-20 Midday 866` mode=`VTRAC_BOX` tier=`B` stage=`decay_scorecard`
- `tracker:blackapple_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:compound_event_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:due_double_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:positional_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:profit_alert_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
- `tracker:r_consensus_support` value=`TRUE` mode=`CONTEXT` tier=`C` stage=`tracker`
