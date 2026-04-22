# Analysis Arena Audit Interpretation Pass

Purpose: convert the March post-run audit into practical translator, Brain, and cadence decisions.

## 1. Executive Read

- PRO_92 reinforces the same conclusion as the audit: this branch is now a serious upstream evidence engine, not yet a finished combo/budget engine.
- The core bottleneck is downstream expression: the system often preserves winner-relevant evidence before the old final candidate layer expresses it correctly.
- This interpretation pass keeps scoring changes blocked until Stage 2 adds false-positive/exposure denominators.

## 2. Denominators

- Winner events audited: `301`
- Signal attribution rows: `9256`
- Pre-draw winner-aligned rows: `7400`
- Post-result explanatory rows: `1856`
- Priority fixture candidates exported: `56`

## 3. Cross-Window Context

- Cross-window rollup unavailable for this interpretation run.

## 4. Audit Cohort Read

- Captured-and-used: `63`. These are positive fixtures for evidence reaching action.
- Captured-but-underused: `12`. These are highest-priority translator teaching cases.
- Captured-but-wrong-lane: `51`. These are VTRAC/territory cases that need restraint or sharper boxed/straight gates.
- Decay-validated: `94`. These should feed carryforward/watch logic, not be flattened into same-day misses.
- Captured-but-not-promoted: `81`. These need Stage-2 exposure testing before promotion.

Gap cohort source read:
- exact: `old_candidate_universe:candidate_universe_exact` x8, `old_play_card:play_card_exact_any` x5, `old_play_card:play_card_b36_exact` x5, `old_play_card:play_card_b12_exact` x2, `old_play_card:play_card_b24_exact` x2, `translation_sandbox:straight_seed_decay_resolution` x1
- box: `translation_sandbox:diagnostic_boxed_seed` x18, `arena:arena_box_rollup` x12, `arena:box_total_decay_resolution` x12, `brain1:box_core_decay_resolution` x11, `old_candidate_universe:candidate_universe_box` x10, `translation_sandbox:boxed_seed_decay_resolution` x10, `arena:brain1_dominant_canonicals` x8, `brain1:dominant_canonicals` x8
- vtrac: `brain1:dominant_canonicals` x17, `translation_sandbox:diagnostic_boxed_seed` x16, `old_candidate_universe:pack:stable_top` x16, `brain1:vtrac_core_decay_resolution` x12, `translation_sandbox:vt_seed_decay_resolution` x12, `arena:vtrac_total_decay_resolution` x12, `translation_sandbox:diagnostic_straight_seed` x10, `board_scoreboard:top_vtrac_indices_decay_resolution` x10
- tier_a: `frontier:fired_test` x40, `translation_sandbox:diagnostic_boxed_seed` x18, `arena:arena_box_rollup` x12, `translation_sandbox:boxed_seed_decay_resolution` x10, `arena:brain1_dominant_canonicals` x8, `brain1:dominant_canonicals` x8, `frontier:c1_c2_signature` x6, `old_candidate_universe:pack:stable_top` x6
- families: `old_play_card` x103, `frontier` x87, `tracker` x84, `translation_sandbox` x76, `brain1` x75, `arena` x56, `old_candidate_universe` x45, `board_scoreboard` x24

Wrong-lane source read:
- exact: `translation_sandbox:straight_seed_decay_resolution` x9, `old_candidate_universe:candidate_universe_exact` x6
- box: `arena:box_total_decay_resolution` x25, `translation_sandbox:boxed_seed_decay_resolution` x20, `brain1:box_core_decay_resolution` x18, `old_candidate_universe:candidate_universe_box` x9, `board_scoreboard:top_canonicals_decay_resolution` x8, `control_arm:preserved_decay_resolution` x3, `brain1:secondary_canonicals` x3, `blackapple:recommended_canonicals` x3
- vtrac: `old_candidate_universe:pack:stable_top` x55, `translation_sandbox:vt_seed_decay_resolution` x51, `arena:vtrac_total_decay_resolution` x51, `frontier:c1_c2_signature` x50, `brain1:vtrac_core_decay_resolution` x49, `translation_sandbox:diagnostic_vt_seed` x45, `translation_sandbox:diagnostic_vt_box_seed` x45, `board_scoreboard:top_vtrac_indices_decay_resolution` x42
- tier_a: `frontier:fired_test` x42, `translation_sandbox:boxed_seed_decay_resolution` x20, `translation_sandbox:straight_seed_decay_resolution` x9, `frontier:c1_c2_signature` x6, `brain1:secondary_canonicals` x3, `blackapple:recommended_canonicals` x3, `old_candidate_universe:pack:aux_vtrac_index_overdue` x1, `positional:positional_combo` x1
- families: `tracker` x345, `frontier` x324, `translation_sandbox` x197, `brain1` x166, `arena` x103, `old_candidate_universe` x94, `board_scoreboard` x73, `old_play_card` x53

## 5. Signal Decisions

- `play_card_any_box` -> `boxed_lane_fixture`; present `21`, converted `21`, gaps `0`.
- `sandbox_exact_seed` -> `straight_lane_fixture`; present `4`, converted `4`, gaps `0`.
- `arena_exact_signal` -> `straight_lane_fixture`; present `4`, converted `4`, gaps `0`.
- `play_card_any_exact` -> `straight_lane_fixture`; present `39`, converted `34`, gaps `5`.
- `sandbox_box_seed` -> `boxed_lane_fixture`; present `19`, converted `10`, gaps `9`.
- `arena_primary_box` -> `boxed_lane_fixture`; present `15`, converted `7`, gaps `8`.
- `arena_box_signal` -> `boxed_lane_fixture`; present `22`, converted `10`, gaps `12`.
- `cu_exact` -> `supporting_gate_not_standalone`; present `57`, converted `43`, gaps `8`.
- `cu_box` -> `supporting_gate_not_standalone`; present `73`, converted `51`, gaps `10`.
- `arena_primary_vt` -> `vtrac_decay_lane_only_until_paired`; present `68`, converted `29`, gaps `9`.
- `sandbox_vt_seed` -> `vtrac_decay_lane_only_until_paired`; present `109`, converted `39`, gaps `9`.

## 6. Decay Interpretation

- `brain1_vt_core`: same-day `37.0%`, horizon `90.3%`, incremental lift `82`.
- `board_top_vt_core`: same-day `20.8%`, horizon `66.9%`, incremental lift `71`.
- `arena_vt_total`: same-day `57.1%`, horizon `98.1%`, incremental lift `63`.
- `sandbox_vt_seed`: same-day `57.1%`, horizon `98.1%`, incremental lift `63`.
- `arena_box_total`: same-day `14.3%`, horizon `53.9%`, incremental lift `61`.
- `sandbox_box_seed`: same-day `11.7%`, horizon `44.8%`, incremental lift `51`.

Interpretation: broad VTRAC/territory decay is strong evidence of state-day resolution, but boxed/straight scoring should use narrower exact/box evidence before spending budget.

## 7. Frontier Interpretation

- Signature mix: `HIDDEN_COMPRESSED_FRONTIER` x110, `VTRAC_FRONTIER` x88, `FEEDER_TO_FRONTIER` x86, `FAMILY_FRONTIER` x16, `LITERAL_FRONTIER` x1
- Strength mix: `MEDIUM` x230, `WEAK` x43, `STRONG` x28
- Sharp frontier candidates retained: `39`.
- Read: literal/family/strong/double-anchor frontier should become translator fixtures; generic VTRAC frontier remains territory context.

## 8. Priority Cases

- Priority cases CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PRIORITY_CASES.csv`
- Fixture priority 1 contains all gap teachers; priority 2 positive conversions; priority 3 wrong-lane VTRAC; priority 4 decay teachers; priority 5 not-promoted probes.

### Gap Teachers

- `2026-01-09` `Pennsylvania4` `Midday` winner=`811` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`11` sharp=`3` frontier=`FAMILY_FRONTIER` decay=`direct_same_outcome`
- `2026-01-09` `Pennsylvania4` `Evening` winner=`014` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`11` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2025-12-31` `NewYork4` `Evening` winner=`116` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`7` sharp=`3` frontier=`FEEDER_TO_FRONTIER` decay=`same_day_carryforward`
- `2026-01-01` `NorthCarolina4` `Evening` winner=`053` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`8` sharp=`3` frontier=`FAMILY_FRONTIER` decay=`same_day_carryforward`
- `2026-01-02` `NorthCarolina4` `Midday` winner=`033` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`8` sharp=`3` frontier=`FEEDER_TO_FRONTIER` decay=`direct_same_outcome`
- `2026-01-04` `Virginia4` `Midday` winner=`200` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`14` sharp=`3` frontier=`VTRAC_FRONTIER` decay=`direct_same_outcome`
- `2026-01-08` `Ohio4` `Evening` winner=`580` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`9` sharp=`2` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2025-12-30` `Pennsylvania4` `Evening` winner=`173` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`11` sharp=`2` frontier=`FAMILY_FRONTIER` decay=`direct_same_outcome`

### Positive Conversions

- `2026-01-08` `NewJersey4` `Midday` winner=`089` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`6` sharp=`7` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2025-12-30` `Connecticut4` `Midday` winner=`095` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`1` sharp=`5` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-09` `Ohio4` `Evening` winner=`090` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`9` sharp=`5` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-01-03` `SouthCarolina4` `Evening` winner=`051` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`13` sharp=`5` frontier=`FEEDER_TO_FRONTIER` decay=`direct_same_outcome`
- `2026-01-05` `Florida4` `Midday` winner=`080` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`3` sharp=`4` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-05` `NewYork4` `Midday` winner=`080` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`7` sharp=`3` frontier=`LITERAL_FRONTIER` decay=`direct_same_outcome`
- `2026-01-06` `Michigan4` `Midday` winner=`618` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`5` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-04` `Indiana4` `Midday` winner=`813` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`4` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`

### Wrong-Lane VTRAC

- `2026-01-09` `Ohio4` `Midday` winner=`785` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`9` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-01-04` `NewYork4` `Evening` winner=`489` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`7` sharp=`0` frontier=`FEEDER_TO_FRONTIER` decay=`future_day_decay`
- `2026-01-09` `Florida4` `Midday` winner=`860` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`3` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-08` `NewJersey4` `Evening` winner=`055` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`6` sharp=`0` frontier=`VTRAC_FRONTIER` decay=`direct_same_outcome`
- `2026-01-07` `NewYork4` `Midday` winner=`916` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`7` sharp=`0` frontier=`VTRAC_FRONTIER` decay=`direct_same_outcome`
- `2026-01-05` `Michigan4` `Evening` winner=`772` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`5` sharp=`0` frontier=`FEEDER_TO_FRONTIER` decay=`direct_same_outcome`
- `2026-01-05` `Florida4` `Evening` winner=`994` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`3` sharp=`0` frontier=`FEEDER_TO_FRONTIER` decay=`direct_same_outcome`
- `2026-01-07` `Ohio4` `Evening` winner=`204` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`9` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`

## 9. Next Actions

1. Build Stage-2 Signal Exposure / False-Positive Ledger before assigning new scoring weights.
2. Use all 23 gap rows as boxed/straight translator training fixtures.
3. Use wrong-lane cases to define when VTRAC territory may promote and when it must remain watch-only.
4. Preserve captured-and-used cases as regression positives for future translator changes.
5. Treat captured-but-not-promoted cases as hypothesis probes, not automatic promotions.
6. Keep Brain2 static-rank diagnostics active before trusting top-primary metrics as dynamic selection.

## 10. Generated Files

- Interpretation JSON: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PASS.json`
- Priority cases CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PRIORITY_CASES.csv`
- Signal decisions CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__AUDIT_INTERPRETATION_SIGNAL_DECISIONS.csv`
