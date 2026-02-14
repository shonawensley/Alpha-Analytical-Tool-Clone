# Morning Brief — Spinecap6 “Spine Chooser” Sweep (B36 • stable10 • tool_only) — 2026-02-14

Purpose: test a **single** within-lane lever on top of the promoted `spinecap6` geometry:

- Keep: `tool_only` + `stable10` + **B36-only**
- No analyzer edits (selection-layer only)
- Baseline remains: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`

## What changed (single lever family)

Added two experimental B36 strategy variants that change **how the 6 spine lines per index are chosen**:

- `...spinecap6_spine_evidence`
  - spine lines come from the highest-convergence **evidence rows inside the lane** (fallback to VTRAC display members if short)
- `...spinecap6_spine_display_ranked`
  - still uses VTRAC display members, but **orders them by evidence strength** before taking the top 6

## Decision

No promotion. Keep `...spinecap6` as the B36 default.

Reason: neither variant produced a clean win under the promotion gates (no regressions, plus a measurable lift).

## The four numbers (baseline vs variants)

Baseline = `...spinecap6`

Jan window (2026-01-15..01-22):
- strict `hit_any`: baseline **5.2%**
  - `spine_evidence`: **3.6%** (regresses)
  - `spine_display_ranked`: **5.2%** (no change)
- `hit_any_inclusive`: baseline **49.7%**
  - both variants: **49.7%** (no change)

OOS window (2026-01-01..01-09):
- strict `hit_any`: baseline **4.1%**
  - `spine_evidence`: **4.9%** (improves)
  - `spine_display_ranked`: **4.1%** (no change)
- `hit_any_inclusive`: baseline **44.9%**
  - `spine_evidence`: **44.1%** (regresses)
  - `spine_display_ranked`: **44.9%** (no change)

## Why this is still a useful result

- `spine_display_ranked` appears to be effectively a no-op in current windows (same scoreboard outcomes as baseline).
- `spine_evidence` shows the expected trade: it can raise strict in OOS, but it reduces the “bridge”/coverage contract and increases lane/exact drop.
- This suggests the next “within-lane conversion” lever should not fully replace the bounded VTRAC display pack; it likely needs a **hybrid** approach (e.g., preserve display coverage, then use evidence to choose a small number of additional lines).

## Key artifacts

Scoreboard sweeps (Jan + OOS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_SPINECHOOSER_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_SPINECHOOSER_SWEEP.md:1`

Lane allocation (breadth/depth sanity):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_EVSPINE.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_DISPRANK.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_EVSPINE.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_DISPRANK.md:1`

Winner lane rank (lane ranking vs retention sanity):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_SPINECHOOSER_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_SPINECHOOSER_SWEEP.md:1`

