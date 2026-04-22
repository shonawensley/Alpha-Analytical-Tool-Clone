# Stage 2B Cross-Window Stack Rollup

Purpose: separate repeatable translator/stack candidates from one-window noise before any scoring rewrite.

## Executive Read

- The cross-window layer is a confirmation surface, not a live scoring surface.
- Recurring bounded box-overlap stacks are the best replay candidates.
- Recurring VTRAC stacks remain watch/decay unless a bounded box or exact confirmation source proves conversion.
- Recurring negative controls are useful because they define what not to promote.

## Window Coverage

- `WINDOW_2026-03-09_to_2026-03-23`: state_days=`210`, winners=`414`, stage2_exposures=`211689`, stage2b_stacks=`4025`

## Stack Status Mix

- `single_window_only`: `4025`

## Hypothesis Confirmation Mix

- `single_window_only`: `132`
- `not_in_stack_rollup`: `13`

## Cross-Window Boxed Translator Candidates

- None.

## Cross-Window Boxed Support Gates

- None.

## Cross-Window VTRAC Watch Only

- None.

## Recurring Negative Controls

- None.

## Cross-Window Low-Denominator Fixtures

- None.

## Stable Source Surfaces

- `old_candidate_universe:pack_method:vtrac_enhanced_top:canonical` windows=`1` lane=`vtrac` lane_rate=`8.7%` event_support=`15.0%` decisions=`vtrac_context_only:1`
- `brain1:dominant_vtrac_indices` windows=`1` lane=`vtrac` lane_rate=`6.5%` event_support=`28.0%` decisions=`vtrac_context_only:1`
- `brain1:watchlist_indices` windows=`1` lane=`vtrac` lane_rate=`6.4%` event_support=`20.0%` decisions=`vtrac_context_only:1`
- `translation_sandbox:diagnostic_vt_box_seed` windows=`1` lane=`vtrac` lane_rate=`6.3%` event_support=`39.1%` decisions=`vtrac_watch_decay_only_until_box_pairing:1`
- `board_scoreboard:top_vtrac_indices` windows=`1` lane=`vtrac` lane_rate=`6.3%` event_support=`13.0%` decisions=`vtrac_context_only:1`
- `old_candidate_universe:pack:aux_vtrac_index_overdue` windows=`1` lane=`vtrac` lane_rate=`5.6%` event_support=`1.9%` decisions=`vtrac_context_only:1`
- `old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical` windows=`1` lane=`vtrac` lane_rate=`2.3%` event_support=`2.9%` decisions=`vtrac_context_only:1`
- `old_candidate_universe:pack:aux_positional` windows=`1` lane=`boxed` lane_rate=`1.9%` event_support=`5.1%` decisions=`boxed_supporting_gate:1`
- `old_candidate_universe:pack:R-perm-4` windows=`1` lane=`boxed` lane_rate=`1.3%` event_support=`11.4%` decisions=`boxed_context_or_negative_control:1`
- `old_candidate_universe:pack_method:R-perm-4:canonical` windows=`1` lane=`boxed` lane_rate=`1.3%` event_support=`11.4%` decisions=`boxed_context_or_negative_control:1`
- `old_candidate_universe:pack:mirror_pair_closure` windows=`1` lane=`boxed` lane_rate=`1.3%` event_support=`13.5%` decisions=`boxed_context_or_negative_control:1`
- `old_candidate_universe:pack_method:mirror_pair_closure:canonical` windows=`1` lane=`boxed` lane_rate=`1.3%` event_support=`13.5%` decisions=`boxed_context_or_negative_control:1`
- `old_play_card:strategy:conversion_box_first:B24:boxed_canonicals` windows=`1` lane=`boxed` lane_rate=`1.1%` event_support=`12.6%` decisions=`boxed_context_or_negative_control:1`
- `old_play_card:strategy_card:conversion_box_first:B24` windows=`1` lane=`boxed` lane_rate=`1.1%` event_support=`12.6%` decisions=`boxed_context_or_negative_control:1`
- `old_play_card:strategy_card:convergence_box_first:B24` windows=`1` lane=`boxed` lane_rate=`1.1%` event_support=`14.3%` decisions=`boxed_context_or_negative_control:1`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` windows=`1` lane=`boxed` lane_rate=`1.1%` event_support=`14.3%` decisions=`boxed_context_or_negative_control:1`
- `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` windows=`1` lane=`boxed` lane_rate=`1.1%` event_support=`14.3%` decisions=`boxed_context_or_negative_control:1`
- `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` windows=`1` lane=`boxed` lane_rate=`1.1%` event_support=`14.3%` decisions=`boxed_context_or_negative_control:1`
- `shadow_policy:primary_cluster_context` windows=`1` lane=`boxed` lane_rate=`1.1%` event_support=`12.8%` decisions=`boxed_context_or_negative_control:1`
- `old_play_card:strategy:play_box_first:B24:boxed_canonicals` windows=`1` lane=`boxed` lane_rate=`1.1%` event_support=`15.9%` decisions=`boxed_context_or_negative_control:1`

## Generated Files

- Stack confirmation CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_STACK_CONFIRMATION.csv`
- Hypothesis confirmation CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_HYPOTHESIS_CONFIRMATION.csv`
- Source confirmation CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_SOURCE_CONFIRMATION.csv`
- Rollup JSON: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_STACK_ROLLUP.json`

## Guardrail

- A cross-window candidate is only permission to replay against fixtures. It is not a permission to alter live scoring or budgeting.
