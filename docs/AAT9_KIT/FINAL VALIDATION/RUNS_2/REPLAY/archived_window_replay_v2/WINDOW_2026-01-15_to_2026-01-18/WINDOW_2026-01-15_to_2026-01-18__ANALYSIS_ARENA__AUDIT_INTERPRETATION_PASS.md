# Analysis Arena Audit Interpretation Pass

Purpose: convert the March post-run audit into practical translator, Brain, and cadence decisions.

## 1. Executive Read

- PRO_92 reinforces the same conclusion as the audit: this branch is now a serious upstream evidence engine, not yet a finished combo/budget engine.
- The core bottleneck is downstream expression: the system often preserves winner-relevant evidence before the old final candidate layer expresses it correctly.
- This interpretation pass keeps scoring changes blocked until Stage 2 adds false-positive/exposure denominators.

## 2. Denominators

- Winner events audited: `109`
- Signal attribution rows: `3433`
- Pre-draw winner-aligned rows: `2743`
- Post-result explanatory rows: `690`
- Priority fixture candidates exported: `48`

## 3. Cross-Window Context

- Cross-window sample: `5` windows, `1045` winner events, `692` credited hits.
- March candidate-like rate: `45.9%` vs cross-window average `40.8%`.
- March finalist-supported hit rate: `82.3%` vs cross-window average `81.7%`.
- March play-card any-box rate: `10.1%` vs cross-window average `7.5%`.
- March opportunity-gap box rate: `3.7%` vs cross-window average `4.1%`.

## 4. Audit Cohort Read

- Captured-and-used: `30`. These are positive fixtures for evidence reaching action.
- Captured-but-underused: `4`. These are highest-priority translator teaching cases.
- Captured-but-wrong-lane: `22`. These are VTRAC/territory cases that need restraint or sharper boxed/straight gates.
- Decay-validated: `30`. These should feed carryforward/watch logic, not be flattened into same-day misses.
- Captured-but-not-promoted: `23`. These need Stage-2 exposure testing before promotion.

Gap cohort source read:
- exact: `old_candidate_universe:candidate_universe_exact` x3, `old_play_card:play_card_exact_any` x1, `old_play_card:play_card_b36_exact` x1, `translation_sandbox:straight_seed_decay_resolution` x1
- box: `arena:brain1_dominant_canonicals` x4, `arena:arena_box_rollup` x4, `brain1:dominant_canonicals` x4, `brain1:box_core_decay_resolution` x4, `arena:box_total_decay_resolution` x4, `translation_sandbox:diagnostic_boxed_seed` x4, `old_candidate_universe:candidate_universe_box` x3, `translation_sandbox:boxed_seed_decay_resolution` x3
- vtrac: `brain1:dominant_canonicals` x13, `old_candidate_universe:pack:stable_top` x10, `translation_sandbox:diagnostic_boxed_seed` x8, `brain1:secondary_canonicals` x4, `survivor:survivor_frontier_canonicals` x4, `brain1:vtrac_core_decay_resolution` x4, `translation_sandbox:vt_seed_decay_resolution` x4, `arena:vtrac_total_decay_resolution` x4
- tier_a: `frontier:fired_test` x8, `arena:brain1_dominant_canonicals` x4, `arena:arena_box_rollup` x4, `brain1:dominant_canonicals` x4, `translation_sandbox:diagnostic_boxed_seed` x4, `translation_sandbox:boxed_seed_decay_resolution` x3, `old_candidate_universe:pack:stable_top` x3, `survivor:survivor_frontier_canonicals` x2
- families: `brain1` x33, `frontier` x29, `tracker` x28, `translation_sandbox` x25, `old_candidate_universe` x21, `arena` x19, `board_scoreboard` x9, `shadow_policy` x8

Wrong-lane source read:
- exact: `translation_sandbox:straight_seed_decay_resolution` x3
- box: `arena:box_total_decay_resolution` x10, `brain1:box_core_decay_resolution` x9, `translation_sandbox:boxed_seed_decay_resolution` x8, `old_candidate_universe:candidate_universe_box` x5, `board_scoreboard:top_canonicals_decay_resolution` x3, `frontier:c1_c2_signature` x1
- vtrac: `old_candidate_universe:pack:stable_top` x24, `frontier:c1_c2_signature` x21, `translation_sandbox:vt_seed_decay_resolution` x20, `arena:vtrac_total_decay_resolution` x20, `translation_sandbox:diagnostic_vt_seed` x18, `translation_sandbox:diagnostic_vt_box_seed` x18, `brain1:vtrac_core_decay_resolution` x17, `board_scoreboard:top_vtrac_indices_decay_resolution` x14
- tier_a: `translation_sandbox:boxed_seed_decay_resolution` x8, `frontier:fired_test` x6, `translation_sandbox:straight_seed_decay_resolution` x3, `frontier:c1_c2_signature` x1
- families: `tracker` x147, `frontier` x141, `translation_sandbox` x77, `brain1` x66, `old_candidate_universe` x48, `arena` x42, `board_scoreboard` x26, `shadow_policy` x11

## 5. Signal Decisions

- `play_card_any_box` -> `boxed_lane_fixture`; present `11`, converted `11`, gaps `0`.
- `sandbox_exact_seed` -> `straight_lane_fixture`; present `3`, converted `3`, gaps `0`.
- `arena_exact_signal` -> `straight_lane_fixture`; present `3`, converted `3`, gaps `0`.
- `play_card_any_exact` -> `straight_lane_fixture`; present `16`, converted `15`, gaps `1`.
- `sandbox_box_seed` -> `boxed_lane_fixture`; present `10`, converted `8`, gaps `2`.
- `arena_box_signal` -> `boxed_lane_fixture`; present `12`, converted `8`, gaps `4`.
- `arena_primary_box` -> `boxed_lane_fixture`; present `9`, converted `5`, gaps `4`.
- `cu_exact` -> `supporting_gate_not_standalone`; present `26`, converted `23`, gaps `3`.
- `cu_box` -> `supporting_gate_not_standalone`; present `33`, converted `25`, gaps `3`.
- `arena_primary_vt` -> `vtrac_decay_lane_only_until_paired`; present `33`, converted `18`, gaps `3`.
- `sandbox_vt_seed` -> `vtrac_decay_lane_only_until_paired`; present `46`, converted `20`, gaps `3`.

## 6. Decay Interpretation

- `brain1_vt_core`: same-day `46.4%`, horizon `89.3%`, incremental lift `24`.
- `arena_vt_total`: same-day `60.7%`, horizon `98.2%`, incremental lift `21`.
- `sandbox_vt_seed`: same-day `60.7%`, horizon `98.2%`, incremental lift `21`.
- `board_top_vt_core`: same-day `30.4%`, horizon `60.7%`, incremental lift `17`.
- `arena_box_total`: same-day `21.4%`, horizon `50.0%`, incremental lift `16`.
- `brain1_box_core`: same-day `16.1%`, horizon `44.6%`, incremental lift `16`.

Interpretation: broad VTRAC/territory decay is strong evidence of state-day resolution, but boxed/straight scoring should use narrower exact/box evidence before spending budget.

## 7. Frontier Interpretation

- Signature mix: `HIDDEN_COMPRESSED_FRONTIER` x50, `VTRAC_FRONTIER` x28, `FEEDER_TO_FRONTIER` x26, `FAMILY_FRONTIER` x4
- Strength mix: `MEDIUM` x85, `WEAK` x13, `STRONG` x10
- Sharp frontier candidates retained: `13`.
- Read: literal/family/strong/double-anchor frontier should become translator fixtures; generic VTRAC frontier remains territory context.

## 8. Priority Cases

- Priority cases CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PRIORITY_CASES.csv`
- Fixture priority 1 contains all gap teachers; priority 2 positive conversions; priority 3 wrong-lane VTRAC; priority 4 decay teachers; priority 5 not-promoted probes.

### Gap Teachers

- `2026-01-16` `Delaware4` `Evening` winner=`107` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`2` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-16` `Connecticut4` `Evening` winner=`431` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`1` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-01-18` `NewJersey4` `Evening` winner=`955` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`6` sharp=`2` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-01-15` `NorthCarolina4` `Midday` winner=`045` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`8` sharp=`2` frontier=`FEEDER_TO_FRONTIER` decay=`direct_same_outcome`

### Positive Conversions

- `2026-01-16` `Indiana4` `Evening` winner=`836` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`4` sharp=`7` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-16` `OntarioCanada4` `Evening` winner=`390` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`10` sharp=`5` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-01-18` `Connecticut4` `Midday` winner=`238` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`1` sharp=`5` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-18` `NorthCarolina4` `Evening` winner=`772` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`8` sharp=`4` frontier=`FEEDER_TO_FRONTIER` decay=`same_day_carryforward`
- `2026-01-16` `NewJersey4` `Evening` winner=`180` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`6` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-01-17` `NorthCarolina4` `Midday` winner=`414` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`8` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-17` `NewJersey4` `Midday` winner=`873` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`6` sharp=`2` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-17` `Indiana4` `Evening` winner=`065` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`4` sharp=`2` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`

### Wrong-Lane VTRAC

- `2026-01-15` `Indiana4` `Evening` winner=`094` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`4` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-16` `Indiana4` `Midday` winner=`954` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`4` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-15` `SouthCarolina4` `Midday` winner=`441` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`13` sharp=`0` frontier=`VTRAC_FRONTIER` decay=`direct_same_outcome`
- `2026-01-15` `NewJersey4` `Midday` winner=`419` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`6` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-15` `NewJersey4` `Evening` winner=`466` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`6` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-17` `SouthCarolina4` `Evening` winner=`512` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`13` sharp=`0` frontier=`FAMILY_FRONTIER` decay=`direct_same_outcome`
- `2026-01-18` `Connecticut4` `Evening` winner=`781` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`1` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-15` `Michigan4` `Midday` winner=`386` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`5` sharp=`0` frontier=`FEEDER_TO_FRONTIER` decay=`direct_same_outcome`

## 9. Next Actions

1. Build Stage-2 Signal Exposure / False-Positive Ledger before assigning new scoring weights.
2. Use all 23 gap rows as boxed/straight translator training fixtures.
3. Use wrong-lane cases to define when VTRAC territory may promote and when it must remain watch-only.
4. Preserve captured-and-used cases as regression positives for future translator changes.
5. Treat captured-but-not-promoted cases as hypothesis probes, not automatic promotions.
6. Keep Brain2 static-rank diagnostics active before trusting top-primary metrics as dynamic selection.

## 10. Generated Files

- Interpretation JSON: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PASS.json`
- Priority cases CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PRIORITY_CASES.csv`
- Signal decisions CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__AUDIT_INTERPRETATION_SIGNAL_DECISIONS.csv`
