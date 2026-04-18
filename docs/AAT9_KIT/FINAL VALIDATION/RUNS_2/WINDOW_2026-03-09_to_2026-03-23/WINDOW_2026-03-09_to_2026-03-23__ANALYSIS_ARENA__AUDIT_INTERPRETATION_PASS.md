# Analysis Arena Audit Interpretation Pass

Purpose: convert the March post-run audit into practical translator, Brain, and cadence decisions.

## 1. Executive Read

- PRO_92 reinforces the same conclusion as the audit: this branch is now a serious upstream evidence engine, not yet a finished combo/budget engine.
- The core bottleneck is downstream expression: the system often preserves winner-relevant evidence before the old final candidate layer expresses it correctly.
- This interpretation pass keeps scoring changes blocked until Stage 2 adds false-positive/exposure denominators.

## 2. Denominators

- Winner events audited: `414`
- Signal attribution rows: `13559`
- Pre-draw winner-aligned rows: `10990`
- Post-result explanatory rows: `2569`
- Priority fixture candidates exported: `67`

## 3. Cross-Window Context

- Cross-window sample: `5` windows, `1045` winner events, `692` credited hits.
- March candidate-like rate: `40.6%` vs cross-window average `40.8%`.
- March finalist-supported hit rate: `83.6%` vs cross-window average `81.7%`.
- March play-card any-box rate: `7.0%` vs cross-window average `7.5%`.
- March opportunity-gap box rate: `5.1%` vs cross-window average `4.1%`.

## 4. Audit Cohort Read

- Captured-and-used: `97`. These are positive fixtures for evidence reaching action.
- Captured-but-underused: `23`. These are highest-priority translator teaching cases.
- Captured-but-wrong-lane: `66`. These are VTRAC/territory cases that need restraint or sharper boxed/straight gates.
- Decay-validated: `103`. These should feed carryforward/watch logic, not be flattened into same-day misses.
- Captured-but-not-promoted: `125`. These need Stage-2 exposure testing before promotion.

Gap cohort source read:
- exact: `old_candidate_universe:candidate_universe_exact` x12, `translation_sandbox:diagnostic_straight_seed` x4, `old_play_card:play_card_exact_any` x3, `old_play_card:play_card_b36_exact` x3, `translation_sandbox:straight_seed_decay_resolution` x3, `arena:arena_exact_rollup` x2, `positional:positional_combo` x2, `frontier:c1_c2_signature` x1
- box: `translation_sandbox:diagnostic_boxed_seed` x30, `arena:arena_box_rollup` x21, `arena:box_total_decay_resolution` x21, `brain1:box_core_decay_resolution` x19, `translation_sandbox:boxed_seed_decay_resolution` x17, `arena:brain1_dominant_canonicals` x16, `brain1:dominant_canonicals` x16, `old_candidate_universe:candidate_universe_box` x14
- vtrac: `brain1:dominant_canonicals` x44, `translation_sandbox:diagnostic_boxed_seed` x39, `old_candidate_universe:pack:stable_top` x32, `brain1:secondary_canonicals` x31, `profit_alerts:implied_canonicals` x27, `translation_sandbox:diagnostic_straight_seed` x25, `old_play_card:ranked_candidate_combo` x25, `old_play_card:ranked_candidate_canonical` x25
- tier_a: `frontier:fired_test` x76, `translation_sandbox:diagnostic_boxed_seed` x30, `arena:arena_box_rollup` x21, `translation_sandbox:boxed_seed_decay_resolution` x17, `arena:brain1_dominant_canonicals` x16, `brain1:dominant_canonicals` x16, `survivor:survivor_frontier_canonicals` x10, `frontier:c1_c2_signature` x10
- families: `old_play_card` x206, `frontier` x169, `brain1` x167, `translation_sandbox` x162, `tracker` x153, `arena` x103, `old_candidate_universe` x90, `board_scoreboard` x52

Wrong-lane source read:
- exact: `translation_sandbox:straight_seed_decay_resolution` x9, `old_candidate_universe:candidate_universe_exact` x5
- box: `arena:box_total_decay_resolution` x35, `translation_sandbox:boxed_seed_decay_resolution` x34, `brain1:box_core_decay_resolution` x28, `old_candidate_universe:candidate_universe_box` x8, `frontier:c1_c2_signature` x6, `board_scoreboard:top_canonicals_decay_resolution` x6, `blackapple:recommended_canonicals` x6, `brain1:secondary_canonicals` x5
- vtrac: `old_candidate_universe:pack:stable_top` x66, `translation_sandbox:vt_seed_decay_resolution` x66, `arena:vtrac_total_decay_resolution` x66, `translation_sandbox:diagnostic_vt_seed` x64, `brain1:secondary_canonicals` x64, `translation_sandbox:diagnostic_vt_box_seed` x64, `brain1:vtrac_core_decay_resolution` x63, `frontier:c1_c2_signature` x60
- tier_a: `frontier:fired_test` x59, `translation_sandbox:boxed_seed_decay_resolution` x34, `frontier:c1_c2_signature` x9, `translation_sandbox:straight_seed_decay_resolution` x9, `blackapple:recommended_canonicals` x6, `brain1:secondary_canonicals` x5, `survivor:survivor_frontier_canonicals` x2, `profit_alerts:implied_canonicals` x2
- families: `tracker` x469, `frontier` x428, `translation_sandbox` x287, `brain1` x286, `arena` x144, `old_candidate_universe` x97, `board_scoreboard` x78, `profit_alerts` x60

## 5. Signal Decisions

- `play_card_any_box` -> `boxed_lane_fixture`; present `29`, converted `29`, gaps `0`.
- `play_card_any_exact` -> `straight_lane_fixture`; present `54`, converted `51`, gaps `3`.
- `sandbox_exact_seed` -> `straight_lane_fixture`; present `9`, converted `7`, gaps `2`.
- `arena_exact_signal` -> `straight_lane_fixture`; present `9`, converted `7`, gaps `2`.
- `sandbox_box_seed` -> `boxed_lane_fixture`; present `27`, converted `12`, gaps `15`.
- `arena_box_signal` -> `boxed_lane_fixture`; present `35`, converted `14`, gaps `21`.
- `arena_primary_box` -> `boxed_lane_fixture`; present `25`, converted `9`, gaps `16`.
- `cu_exact` -> `supporting_gate_not_standalone`; present `80`, converted `62`, gaps `12`.
- `cu_box` -> `supporting_gate_not_standalone`; present `97`, converted `74`, gaps `14`.
- `arena_primary_vt` -> `vtrac_decay_lane_only_until_paired`; present `116`, converted `49`, gaps `16`.
- `sandbox_vt_seed` -> `vtrac_decay_lane_only_until_paired`; present `162`, converted `59`, gaps `19`.

## 6. Decay Interpretation

- `board_top_vt_core`: same-day `24.3%`, horizon `79.5%`, incremental lift `116`.
- `brain1_vt_core`: same-day `49.0%`, horizon `97.6%`, incremental lift `102`.
- `arena_box_total`: same-day `16.2%`, horizon `60.5%`, incremental lift `93`.
- `sandbox_box_seed`: same-day `12.9%`, horizon `53.3%`, incremental lift `85`.
- `arena_vt_total`: same-day `66.2%`, horizon `100.0%`, incremental lift `71`.
- `sandbox_vt_seed`: same-day `66.2%`, horizon `100.0%`, incremental lift `71`.

Interpretation: broad VTRAC/territory decay is strong evidence of state-day resolution, but boxed/straight scoring should use narrower exact/box evidence before spending budget.

## 7. Frontier Interpretation

- Signature mix: `HIDDEN_COMPRESSED_FRONTIER` x156, `FEEDER_TO_FRONTIER` x132, `VTRAC_FRONTIER` x103, `FAMILY_FRONTIER` x21, `LITERAL_FRONTIER` x2
- Strength mix: `MEDIUM` x329, `WEAK` x55, `STRONG` x30
- Sharp frontier candidates retained: `46`.
- Read: literal/family/strong/double-anchor frontier should become translator fixtures; generic VTRAC frontier remains territory context.

## 8. Priority Cases

- Priority cases CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PRIORITY_CASES.csv`
- Fixture priority 1 contains all gap teachers; priority 2 positive conversions; priority 3 wrong-lane VTRAC; priority 4 decay teachers; priority 5 not-promoted probes.

### Gap Teachers

- `2026-03-23` `Ohio4` `Midday` winner=`766` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`9` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-03-12` `OntarioCanada4` `Evening` winner=`401` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`10` sharp=`3` frontier=`VTRAC_FRONTIER` decay=`same_day_carryforward`
- `2026-03-09` `Connecticut4` `Evening` winner=`091` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`1` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-03-14` `SouthCarolina4` `Midday` winner=`202` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`13` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-03-21` `Pennsylvania4` `Evening` winner=`107` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`11` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-03-11` `NewJersey4` `Evening` winner=`388` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`6` sharp=`3` frontier=`LITERAL_FRONTIER` decay=`same_day_carryforward`
- `2026-03-20` `Virginia4` `Evening` winner=`259` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`14` sharp=`3` frontier=`VTRAC_FRONTIER` decay=`direct_same_outcome`
- `2026-03-23` `SouthCarolina4` `Evening` winner=`005` outcome=`BOX_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`13` sharp=`3` frontier=`VTRAC_FRONTIER` decay=`same_day_carryforward`
- `2026-03-12` `NewYork4` `Evening` winner=`865` outcome=`EXACT_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`7` sharp=`2` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-03-17` `Indiana4` `Evening` winner=`108` outcome=`EXACT_GAP` status=`CAPTURED_BUT_UNDERUSED` rank=`4` sharp=`2` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`

### Positive Conversions

- `2026-03-10` `SouthCarolina4` `Evening` winner=`690` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`13` sharp=`5` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-03-16` `SouthCarolina4` `Midday` winner=`077` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`13` sharp=`5` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-03-19` `NewYork4` `Midday` winner=`303` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`7` sharp=`4` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-03-12` `Virginia4` `Evening` winner=`400` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`14` sharp=`4` frontier=`FAMILY_FRONTIER` decay=`direct_same_outcome`
- `2026-03-19` `NorthCarolina4` `Midday` winner=`611` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`8` sharp=`4` frontier=`VTRAC_FRONTIER` decay=`direct_same_outcome`
- `2026-03-17` `NorthCarolina4` `Evening` winner=`383` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`8` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-03-22` `NewYork4` `Evening` winner=`618` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`7` sharp=`3` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`same_day_carryforward`
- `2026-03-20` `Indiana4` `Midday` winner=`515` outcome=`STRAIGHT` status=`CAPTURED_AND_USED` rank=`4` sharp=`3` frontier=`LITERAL_FRONTIER` decay=`direct_same_outcome`

### Wrong-Lane VTRAC

- `2026-03-09` `NewYork4` `Midday` winner=`900` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`7` sharp=`0` frontier=`FEEDER_TO_FRONTIER` decay=`direct_same_outcome`
- `2026-03-22` `NorthCarolina4` `Midday` winner=`532` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`8` sharp=`0` frontier=`FEEDER_TO_FRONTIER` decay=`direct_same_outcome`
- `2026-03-09` `SouthCarolina4` `Midday` winner=`455` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`13` sharp=`0` frontier=`FAMILY_FRONTIER` decay=`direct_same_outcome`
- `2026-03-18` `Connecticut4` `Midday` winner=`848` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`1` sharp=`0` frontier=`FEEDER_TO_FRONTIER` decay=`direct_same_outcome`
- `2026-03-16` `Indiana4` `Midday` winner=`279` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`4` sharp=`0` frontier=`FAMILY_FRONTIER` decay=`direct_same_outcome`
- `2026-03-16` `Pennsylvania4` `Midday` winner=`209` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`11` sharp=`0` frontier=`HIDDEN_COMPRESSED_FRONTIER` decay=`direct_same_outcome`
- `2026-03-13` `OntarioCanada4` `Midday` winner=`879` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`10` sharp=`0` frontier=`FEEDER_TO_FRONTIER` decay=`same_day_carryforward`
- `2026-03-21` `NorthCarolina4` `Evening` winner=`537` outcome=`VTRAC_ONLY` status=`CAPTURED_BUT_WRONG_LANE` rank=`8` sharp=`0` frontier=`FEEDER_TO_FRONTIER` decay=`same_day_carryforward`

## 9. Next Actions

1. Build Stage-2 Signal Exposure / False-Positive Ledger before assigning new scoring weights.
2. Use all 23 gap rows as boxed/straight translator training fixtures.
3. Use wrong-lane cases to define when VTRAC territory may promote and when it must remain watch-only.
4. Preserve captured-and-used cases as regression positives for future translator changes.
5. Treat captured-but-not-promoted cases as hypothesis probes, not automatic promotions.
6. Keep Brain2 static-rank diagnostics active before trusting top-primary metrics as dynamic selection.

## 10. Generated Files

- Interpretation JSON: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PASS.json`
- Priority cases CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PRIORITY_CASES.csv`
- Signal decisions CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__AUDIT_INTERPRETATION_SIGNAL_DECISIONS.csv`
