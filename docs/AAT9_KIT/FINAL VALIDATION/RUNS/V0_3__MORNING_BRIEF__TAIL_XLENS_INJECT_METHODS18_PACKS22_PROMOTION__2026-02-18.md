# Morning Brief — Tail Cross-Lens Injection (methods@18 + packs@22) Promotion (B36, stable10) — 2026-02-18

Goal (selection-layer only; isolation-first with strict guardrails):
- Improve **lane retention under fixed B36** (reduce `CU_LANE_BUT_PLAY_MISS`) without buying depth (which collapses breadth).
- Preserve OOS strict `hit_any` as the hard guardrail.

## Baseline (SSOT prior default)

Baseline strategy (previous default):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22`

## Lever under test

Candidate strategy (single lever: tail touched-set composition only):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

Meaning:
- Keep the **same**:
  - posture: `tool_only` + `stable10`
  - budget: `B36`
  - geometry: `taper6644` + `spinecap6` (spine 6/6/4/4; tail 1-line/index)
  - spine index selection: `methods_first`
  - tail base ranking lens: `score_total_first` + the promoted tail-spread schedule (top14 + inject pos18/22)
- Change **only** the *source* of the injected shoulder indices:
  - keep first 14 tail indices from `score_total_first`
  - injected tail index at pos18 comes from `methods_first`
  - injected tail index at pos22 comes from `packs_first`

Rationale:
- Tail-spread schedule tuning saturated; next lever class is “cross-lens diversity” (reduce monoculture bias) without changing geometry or CU posture.

## Jan window (in-sample) — precheck

Scoreboard:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_INJECT_GATE.md`

Key deltas (rows=193):
- strict `hit_any`: `4.7% → 4.7%` (no regress)
- `hit_any_inclusive`: `62.2% → 63.7%` (**+1.5pp**)
- `CU_LANE_BUT_PLAY_MISS`: `15.0% → 13.5%` (**-1.5pp**)
- `CU_EXACT_BUT_PLAY_MISS`: `1.6% → 1.6%` (no change)

Geometry invariants (lever is real; no violations):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAIL_XLENS_INJECT_GATE_JAN.md`
  - candidate `no_op_rate`: `0.487`
  - cap/taper violations: `0`

Decision: **continue** to OOS + robustness windows.

## OOS window (hard gates)

Scoreboard:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_INJECT_GATE.md`

Key deltas (rows=245):
- strict `hit_any`: `4.5% → 4.5%` (hard gate passes)
- `hit_any_inclusive`: `53.9% → 55.1%` (**+1.2pp**; hard gate passes)
- `CU_LANE_BUT_PLAY_MISS`: `15.1% → 13.9%` (**-1.2pp**)
- `CU_EXACT_BUT_PLAY_MISS`: `2.0% → 2.0%` (soft gate passes)

Geometry invariants:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAIL_XLENS_INJECT_GATE_OOS.md`
  - candidate `no_op_rate`: `0.5796`
  - cap/taper violations: `0`

Decision: **passes OOS hard gates**.

## Robustness windows (count-based strict regress rule; inclusive must not materially regress)

Holdout A (rows=163):
- Scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_INJECT_GATE.md`
  - `hit_any_inclusive`: `56.4% → 56.4%` (no regress)
  - strict `hit_any`: `4.9% → 4.9%` (no regress)
  - note: `CU_EXACT_BUT_PLAY_MISS`: `2.5% → 3.1%` (+0.6pp; watch, not a gate)

Holdout B (rows=81):
- Scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_INJECT_GATE.md`
  - `hit_any_inclusive`: `54.3% → 54.3%` (no regress)
  - strict `hit_any`: `2.5% → 2.5%` (no regress)

Decision: **passes robustness**.

## Promotion decision

Promote candidate as the new default B36 strategy under stable10:
- ✅ improves isolation in-sample (`CU_LANE_BUT_PLAY_MISS` down; `hit_any_inclusive` up)
- ✅ improves OOS inclusive (hard gate)
- ✅ preserves OOS strict (hard gate)
- ✅ passes robustness windows under the count-based strict rule

New default (SSOT):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

