# Morning Brief — Tail Spread (top14 + inject pos18/22) Promotion (B36, stable10) — 2026-02-18

Goal (selection-layer only; isolation-first with strict guardrails):
- Improve **lane retention under fixed B36** (reduce `CU_LANE_BUT_PLAY_MISS`) without buying depth (which collapses breadth).
- Preserve/raise OOS strict `hit_any` as the hard guardrail.

## Baseline (SSOT prior default)

Baseline strategy (previous default):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`

## Lever under test

Candidate strategy (single lever: tail index ordering only):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22`

Meaning:
- Keep the **same**:
  - posture: `tool_only` + `stable10`
  - budget: `B36`
  - geometry: `taper6644` + `spinecap6` (spine 6/6/4/4; tail 1-line/index)
  - spine index selection: `methods_first`
  - tail base ranking lens: `score_total_first`
- Change **only** the *tail touched-set ordering*:
  - after choosing spine indices, take tail ranks **0..13**, then inject tail ranks **18** and **22** (0-based), then fill with remaining order.

## Jan window (in-sample) — precheck

Scoreboard:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_SPREAD_TOP14_POS18_22_PRECHECK.md`

Key deltas (rows=193):
- strict `hit_any`: `4.7% → 4.7%` (no regress)
- `hit_any_inclusive`: `59.1% → 62.2%` (**+3.1pp**)
- `CU_LANE_BUT_PLAY_MISS`: `17.6% → 15.0%` (**-2.6pp**)
- `CU_EXACT_BUT_PLAY_MISS`: `2.1% → 1.6%` (**-0.5pp**)
- `pack_box_hit`: `21.2% → 21.8%` (+0.6pp)

Geometry invariants (lever is real; no violations):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAIL_SPREAD_TOP14_POS18_22_PRECHECK.md`
  - candidate `no_op_rate`: `0.0725`
  - cap/taper violations: `0`
  - indices_touched_count mean: unchanged vs baseline

Strict miss anatomy (Jan):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__STRICT_MISS_ANATOMY__tool_only__stable10__B36__TAIL_SPREAD_TOP14_POS18_22_PRECHECK.md`

Decision: **continue** to OOS + robustness windows.

## OOS window (hard gates)

Scoreboard:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_SPREAD_TOP14_POS18_22_GATE.md`

Key deltas (rows=245):
- strict `hit_any`: `4.1% → 4.5%` (**+0.4pp**; hard gate passes)
- `hit_any_inclusive`: `53.1% → 53.9%` (**+0.8pp**; hard gate passes)
- `CU_EXACT_BUT_PLAY_MISS`: `3.3% → 2.0%` (**-1.3pp**; soft gate strongly passes)

Geometry invariants:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAIL_SPREAD_TOP14_POS18_22_GATE.md`

Strict miss anatomy (OOS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__STRICT_MISS_ANATOMY__tool_only__stable10__B36__TAIL_SPREAD_TOP14_POS18_22_GATE.md`

Decision: **passes OOS hard gates**.

## Robustness windows (count-based strict regress rule; inclusive must not materially regress)

Holdout A (rows=163):
- Scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_SPREAD_TOP14_POS18_22_HOLDOUT_A.md`
  - `hit_any_inclusive`: `56.4% → 56.4%` (no regress)
  - strict `hit_any`: `4.3% → 4.9%` (+0.6pp)

Holdout B (rows=81):
- Scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_SPREAD_TOP14_POS18_22_HOLDOUT_B.md`
  - `hit_any_inclusive`: `51.9% → 54.3%` (+2.4pp)
  - strict `hit_any`: `2.5% → 2.5%` (no regress)

Decision: **passes robustness**.

## Promotion decision

Promote candidate as the new default B36 strategy under stable10:
- ✅ improves isolation (`CU_LANE_BUT_PLAY_MISS`) in-sample
- ✅ improves OOS strict + inclusive (hard gates)
- ✅ improves OOS exact-miss (soft gate)
- ✅ passes robustness windows

New default (SSOT):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22`

