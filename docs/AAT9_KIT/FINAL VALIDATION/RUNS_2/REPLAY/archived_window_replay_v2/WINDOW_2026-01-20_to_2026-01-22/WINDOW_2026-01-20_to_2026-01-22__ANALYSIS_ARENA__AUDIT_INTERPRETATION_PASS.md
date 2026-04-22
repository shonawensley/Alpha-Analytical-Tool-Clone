# Analysis Arena Audit Interpretation Pass

Purpose: convert the March post-run audit into practical translator, Brain, and cadence decisions.

## 1. Executive Read

- PRO_92 reinforces the same conclusion as the audit: this branch is now a serious upstream evidence engine, not yet a finished combo/budget engine.
- The core bottleneck is downstream expression: the system often preserves winner-relevant evidence before the old final candidate layer expresses it correctly.
- This interpretation pass keeps scoring changes blocked until Stage 2 adds false-positive/exposure denominators.

## 2. Denominators

- Winner events audited: `84`
- Signal attribution rows: `2689`
- Pre-draw winner-aligned rows: `2170`
- Post-result explanatory rows: `519`
- Priority fixture candidates exported: `46`

## 3. Cross-Window Context

- Cross-window rollup unavailable for this interpretation run.

## 4. Audit Cohort Read

- Captured-and-used: `23`. These are positive fixtures for evidence reaching action.
- Captured-but-underused: `2`. These are highest-priority translator teaching cases.
- Captured-but-wrong-lane: `15`. These are VTRAC/territory cases that need restraint or sharper boxed/straight gates.
- Decay-validated: `19`. These should feed carryforward/watch logic, not be flattened into same-day misses.
- Captured-but-not-promoted: `25`. These need Stage-2 exposure testing before promotion.

Gap cohort source read:
- exact: `old_candidate_universe:candidate_universe_exact` x1, `old_play_card:play_card_exact_any` x1, `old_play_card:play_card_b24_exact` x1, `old_play_card:play_card_b36_exact` x1
- box: `arena:brain1_dominant_canonicals` x2, `arena:arena_box_rollup` x2, `brain1:dominant_canonicals` x2, `brain1:box_core_decay_resolution` x2, `arena:box_total_decay_resolution` x2, `translation_sandbox:diagnostic_boxed_seed` x2, `old_candidate_universe:candidate_universe_box` x1, `survivor:survivor_frontier_canonicals` x1
- vtrac: `translation_sandbox:diagnostic_boxed_seed` x5, `old_play_card:ranked_candidate_combo` x4, `old_play_card:ranked_candidate_canonical` x4, `brain1:dominant_canonicals` x3, `survivor:survivor_frontier_canonicals` x3, `translation_sandbox:diagnostic_straight_seed` x3, `shadow_policy:primary_cluster_survivor_frontier` x3, `old_candidate_universe:pack:stable_top` x2
- tier_a: `arena:brain1_dominant_canonicals` x2, `arena:arena_box_rollup` x2, `brain1:dominant_canonicals` x2, `translation_sandbox:diagnostic_boxed_seed` x2, `old_play_card:play_card_exact_any` x1, `old_play_card:play_card_b24_exact` x1, `old_play_card:play_card_b36_exact` x1, `survivor:survivor_frontier_canonicals` x1
- families: `old_play_card` x29, `frontier` x17, `tracker` x16, `translation_sandbox` x13, `old_candidate_universe` x9, `arena` x8, `brain1` x8, `shadow_policy` x4

Wrong-lane source read:
- exact: `translation_sandbox:straight_seed_decay_resolution` x1
- box: `arena:box_total_decay_resolution` x7, `brain1:box_core_decay_resolution` x6, `translation_sandbox:boxed_seed_decay_resolution` x4, `blackapple:recommended_canonicals` x1, `control_arm:preserved_decay_resolution` x1, `old_candidate_universe:candidate_universe_box` x1, `board_scoreboard:top_canonicals_decay_resolution` x1
- vtrac: `brain1:vtrac_core_decay_resolution` x15, `translation_sandbox:vt_seed_decay_resolution` x15, `arena:vtrac_total_decay_resolution` x15, `frontier:c1_c2_signature` x15, `translation_sandbox:diagnostic_vt_seed` x14, `translation_sandbox:diagnostic_vt_box_seed` x14, `brain1:secondary_canonicals` x13, `blackapple:recommended_canonicals` x13
- tier_a: `frontier:fired_test` x8, `translation_sandbox:boxed_seed_decay_resolution` x4, `blackapple:recommended_canonicals` x1, `translation_sandbox:straight_seed_decay_resolution` x1, `frontier:c1_c2_signature` x1
- families: `tracker` x101, `frontier` x93, `brain1` x68, `translation_sandbox` x67, `arena` x33, `board_scoreboard` x20, `old_play_card` x19, `old_candidate_universe` x17

## 5. Signal Decisions

- `play_card_any_box` -> `boxed_lane_fixture`; present `5`, converted `5`, gaps `0`.
- `sandbox_exact_seed` -> `straight_lane_fixture`; present `1`, converted `1`, gaps `0`.
- `arena_exact_signal` -> `straight_lane_fixture`; present `1`, converted `1`, gaps `0`.
- `play_card_any_exact` -> `straight_lane_fixture`; present `13`, converted `12`, gaps `1`.
- `sandbox_box_seed` -> `boxed_lane_fixture`; present `3`, converted `2`, gaps `1`.
- `arena_box_signal` -> `boxed_lane_fixture`; present `4`, converted `2`, gaps `2`.
- `arena_primary_box` -> `boxed_lane_fixture`; present `3`, converted `1`, gaps `2`.
- `cu_exact` -> `supporting_gate_not_standalone`; present `14`, converted `13`, gaps `1`.
- `cu_box` -> `supporting_gate_not_standalone`; present `20`, converted `18`, gaps `1`.
- `arena_primary_vt` -> `vtrac_decay_lane_only_until_paired`; present `24`, converted `11`, gaps `1`.
- `sandbox_vt_seed` -> `vtrac_decay_lane_only_until_paired`; present `30`, converted `11`, gaps `1`.

## 6. Decay Interpretation

- `arena_box_total`: same-day `9.5%`, horizon `50.0%`, incremental lift `17`.
- `brain1_vt_core`: same-day `47.6%`, horizon `85.7%`, incremental lift `16`.
- `arena_vt_total`: same-day `61.9%`, horizon `97.6%`, incremental lift `15`.
- `sandbox_vt_seed`: same-day `61.9%`, horizon `97.6%`, incremental lift `15`.
- `brain1_box_core`: same-day `9.5%`, horizon `42.9%`, incremental lift `14`.
- `board_top_vt_core`: same-day `28.6%`, horizon `59.5%`, incremental lift `13`.

Interpretation: broad VTRAC/territory decay is strong evidence of state-day resolution, but boxed/straight scoring should use narrower exact/box evidence before spending budget.

## 7. Frontier Interpretation

- Signature mix: `FEEDER_TO_FRONTIER` x30, `HIDDEN_COMPRESSED_FRONTIER` x28, `VTRAC_FRONTIER` x21, `FAMILY_FRONTIER` x5
- Strength mix: `MEDIUM` x60, `WEAK` x15, `STRONG` x9
- Sharp frontier candidates retained: `12`.
- Read: literal/family/strong/double-anchor frontier should become translator fixtures; generic VTRAC frontier remains territory context.

## 8. Priority Cases

- Priority cases CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PRIORITY_CASES.csv`
- Fixture priority 1 contains all gap teachers; priority 2 positive conversions; priority 3 wrong-lane VTRAC; priority 4 decay teachers; priority 5 not-promoted probes.

### Gap Teachers

- `2026-01-22` `Virginia4` `Evening` winner=`100` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`14` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-01-21` `NorthCarolina4` `Evening` winner=`577` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`8` sharp=`2` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`

### Positive Conversions

- `2026-01-22` `OntarioCanada4` `Evening` winner=`544` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`10` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-01-21` `Pennsylvania4` `Evening` winner=`816` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`11` sharp=`2` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-21` `NewYork4` `Evening` winner=`233` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`7` sharp=`2` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-01-20` `Virginia4` `Midday` winner=`260` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`14` sharp=`0` frontier=`FEEDER_TO_FRONTIER` decay=`future_day_decay`
- `2026-01-21` `Ohio4` `Evening` winner=`740` outcome=`BOX_ANY` status=`CAPTURED_AND_USED` rank=`9` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`future_day_decay`
- `2026-01-21` `OntarioCanada4` `Evening` winner=`199` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`10` sharp=`0` frontier=`FAMILY_FRONTIER` decay=`direct_same_outcome`
- `2026-01-20` `Pennsylvania4` `Midday` winner=`218` outcome=`BOX_ANY` status=`CAPTURED_AND_USED` rank=`11` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`future_day_decay`
- `2026-01-21` `PuertoRico4` `Midday` winner=`328` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`12` sharp=`0` frontier=`FEEDER_TO_FRONTIER` decay=`future_day_decay`

### Wrong-Lane VTRAC

- `2026-01-21` `OntarioCanada4` `Midday` winner=`197` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`10` sharp=`0` frontier=`VTRAC_FRONTIER` decay=`direct_same_outcome`
- `2026-01-21` `Virginia4` `Midday` winner=`314` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`14` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-20` `SouthCarolina4` `Midday` winner=`786` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`13` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-22` `Michigan4` `Evening` winner=`652` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`5` sharp=`0` frontier=`FEEDER_TO_FRONTIER` decay=`same_day_carryforward`
- `2026-01-20` `NewYork4` `Evening` winner=`406` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`7` sharp=`0` frontier=`VTRAC_FRONTIER` decay=`same_day_carryforward`
- `2026-01-20` `Ohio4` `Evening` winner=`843` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`9` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-01-21` `NorthCarolina4` `Midday` winner=`767` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`8` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-01-20` `Indiana4` `Evening` winner=`208` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`4` sharp=`0` frontier=`FEEDER_TO_FRONTIER` decay=`same_day_carryforward`

## 9. Next Actions

1. Build Stage-2 Signal Exposure / False-Positive Ledger before assigning new scoring weights.
2. Use all 23 gap rows as boxed/straight translator training fixtures.
3. Use wrong-lane cases to define when VTRAC territory may promote and when it must remain watch-only.
4. Preserve captured-and-used cases as regression positives for future translator changes.
5. Treat captured-but-not-promoted cases as hypothesis probes, not automatic promotions.
6. Keep Brain2 static-rank diagnostics active before trusting top-primary metrics as dynamic selection.

## 10. Generated Files

- Interpretation JSON: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PASS.json`
- Priority cases CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PRIORITY_CASES.csv`
- Signal decisions CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__AUDIT_INTERPRETATION_SIGNAL_DECISIONS.csv`
