# Analysis Arena Audit Interpretation Pass

Purpose: convert the March post-run audit into practical translator, Brain, and cadence decisions.

## 1. Executive Read

- PRO_92 reinforces the same conclusion as the audit: this branch is now a serious upstream evidence engine, not yet a finished combo/budget engine.
- The core bottleneck is downstream expression: the system often preserves winner-relevant evidence before the old final candidate layer expresses it correctly.
- This interpretation pass keeps scoring changes blocked until Stage 2 adds false-positive/exposure denominators.

## 2. Denominators

- Winner events audited: `0`
- Signal attribution rows: `0`
- Pre-draw winner-aligned rows: `0`
- Post-result explanatory rows: `0`
- Priority fixture candidates exported: `0`

## 3. Cross-Window Context

- Cross-window sample: `5` windows, `1045` winner events, `692` credited hits.
- March candidate-like rate: `39.3%` vs cross-window average `40.8%`.
- March finalist-supported hit rate: `78.6%` vs cross-window average `81.7%`.
- March play-card any-box rate: `6.1%` vs cross-window average `7.5%`.
- March opportunity-gap box rate: `3.1%` vs cross-window average `4.1%`.

## 4. Audit Cohort Read

- Captured-and-used: `0`. These are positive fixtures for evidence reaching action.
- Captured-but-underused: `0`. These are highest-priority translator teaching cases.
- Captured-but-wrong-lane: `0`. These are VTRAC/territory cases that need restraint or sharper boxed/straight gates.
- Decay-validated: `0`. These should feed carryforward/watch logic, not be flattened into same-day misses.
- Captured-but-not-promoted: `0`. These need Stage-2 exposure testing before promotion.

Gap cohort source read:
- exact: _none_
- box: _none_
- vtrac: _none_
- tier_a: _none_
- families: _none_

Wrong-lane source read:
- exact: _none_
- box: _none_
- vtrac: _none_
- tier_a: _none_
- families: _none_

## 5. Signal Decisions


## 6. Decay Interpretation

- `brain1_vt_core`: same-day `38.1%`, horizon `92.9%`, incremental lift `46`.
- `arena_box_total`: same-day `15.5%`, horizon `57.1%`, incremental lift `35`.
- `arena_vt_total`: same-day `58.3%`, horizon `97.6%`, incremental lift `33`.
- `board_top_vt_core`: same-day `23.8%`, horizon `63.1%`, incremental lift `33`.
- `sandbox_vt_seed`: same-day `58.3%`, horizon `97.6%`, incremental lift `33`.
- `sandbox_box_seed`: same-day `8.3%`, horizon `39.3%`, incremental lift `26`.

Interpretation: broad VTRAC/territory decay is strong evidence of state-day resolution, but boxed/straight scoring should use narrower exact/box evidence before spending budget.

## 7. Frontier Interpretation

- Signature mix: `HIDDEN_COMPRESSED_FRONTIER` x62, `FEEDER_TO_FRONTIER` x49, `VTRAC_FRONTIER` x44, `FAMILY_FRONTIER` x8
- Strength mix: `MEDIUM` x125, `WEAK` x22, `STRONG` x16
- Sharp frontier candidates retained: `21`.
- Read: literal/family/strong/double-anchor frontier should become translator fixtures; generic VTRAC frontier remains territory context.

## 8. Priority Cases

- Priority cases CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/WINDOW_2025-12-30_to_2026-01-04__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PRIORITY_CASES.csv`
- Fixture priority 1 contains all gap teachers; priority 2 positive conversions; priority 3 wrong-lane VTRAC; priority 4 decay teachers; priority 5 not-promoted probes.

### Gap Teachers

- _No examples found._

### Positive Conversions

- _No examples found._

### Wrong-Lane VTRAC

- _No examples found._

## 9. Next Actions

1. Build Stage-2 Signal Exposure / False-Positive Ledger before assigning new scoring weights.
2. Use all 23 gap rows as boxed/straight translator training fixtures.
3. Use wrong-lane cases to define when VTRAC territory may promote and when it must remain watch-only.
4. Preserve captured-and-used cases as regression positives for future translator changes.
5. Treat captured-but-not-promoted cases as hypothesis probes, not automatic promotions.
6. Keep Brain2 static-rank diagnostics active before trusting top-primary metrics as dynamic selection.

## 10. Generated Files

- Interpretation JSON: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/WINDOW_2025-12-30_to_2026-01-04__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PASS.json`
- Priority cases CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/WINDOW_2025-12-30_to_2026-01-04__ANALYSIS_ARENA__AUDIT_INTERPRETATION_PRIORITY_CASES.csv`
- Signal decisions CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/WINDOW_2025-12-30_to_2026-01-04__ANALYSIS_ARENA__AUDIT_INTERPRETATION_SIGNAL_DECISIONS.csv`
