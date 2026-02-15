# Morning Brief — Spinecap6 Hybrid Spine Chooser (B36 • stable10 • tool_only) — 2026-02-15

Goal: test a constrained **within-lane** lever on top of the promoted `...spinecap6` geometry:
- preserve bounded VTRAC display coverage,
- add a small number of evidence lines,
- keep the per-index spine cap at 6.

Lock:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: **B36 only**
- No analyzer edits (selection-layer only)

## What changed (single lever)

New experimental strategy:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_hybrid_d4_e2`
  - Spine per-index cap = 6
  - Hybrid chooser: **min 4 display lines**, then **max 2 evidence lines**, then fill remaining with display (`hybrid_d4_e2`).

Baseline for comparison:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`

## Promotion outcome

**Not promoted.**

Reason: the hybrid chooser improves OOS strict slightly, but **regresses OOS coverage/bridge** and regresses Jan strict.

## The only numbers you need (baseline → hybrid)

Jan (2026-01-15..01-22):
- strict `hit_any`: **5.2% → 4.7%** ❌
- `hit_any_inclusive`: **49.7% → 49.7%** (flat)

OOS (2026-01-01..01-09):
- strict `hit_any`: **4.1% → 4.5%** ✅
- `hit_any_inclusive`: **44.9% → 44.1%** ❌
- `CU_LANE_BUT_PLAY_MISS`: **22.4% → 22.9%** ❌
- `CU_EXACT_BUT_PLAY_MISS`: **3.7% → 4.1%** ❌

## Geometry invariants (prove it’s not a silent cap bug)

From the geometry report (Jan + OOS):
- spine cap violations: **0** (pack-level and total-card)
- display share inside the spine pack (OOS mean):
  - baseline: **1.00**
  - hybrid: **~0.70**
  - evidence: **~0.34**
- `display_ranked` is mostly a **no-op** vs baseline (OOS no-op rate ~61%).

## Key artifacts (clickable)

Scoreboard sweeps:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_HYBRID_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_HYBRID_SWEEP.md:1`

Geometry invariants (diff/no-op + cap checks):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_HYBRID_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_HYBRID_SWEEP.md:1`

Lane allocation (breadth/depth sanity):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__HYBRID.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__HYBRID.md:1`

Winner lane rank sweeps:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_HYBRID_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_HYBRID_SWEEP.md:1`

Casebooks (bucket examples; B36):
- Jan hybrid: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_hybrid_d4_e2__stable10__B36.md:1`
- OOS hybrid: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_hybrid_d4_e2__stable10__B36.md:1`

## Takeaway

Within-lane evidence injection (even when constrained) still appears to trade strict lift for bridge/coverage regression under the current B36 contract.

Next within-lane levers should be designed to **not reduce** `pack_any_correct` / `hit_any_inclusive` (e.g., improve strict via choices that keep the display-anchored bridge intact, or shift levers to tail choice where lane-retention is invariant).

