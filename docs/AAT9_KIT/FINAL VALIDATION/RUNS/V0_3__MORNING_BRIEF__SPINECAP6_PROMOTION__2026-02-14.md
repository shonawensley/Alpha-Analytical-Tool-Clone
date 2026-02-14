# Morning Brief — Spinecap6 Promotion (B36 • stable10 • tool_only) — 2026-02-14

This is the “read this first” summary of the overnight Crossroads iteration.

## What changed (single lever)

- Added two selection-geometry variants of the promoted B36 baseline:
  - `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`
  - `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap7`
- **Promoted** `...spinecap6` as the new **B36 conversion default** (policy updated).
- No analyzer edits. Candidate Universe posture remains `stable10`.

## The only four numbers you need (promotion gates)

Baseline = `v0_2_default_multi_pack_packheavy_spine4_index_tail`  
Candidate = `...spinecap6`

Jan (2026-01-15..01-22):
- `CU_LANE_BUT_PLAY_MISS`: **26.9% → 25.9%** ✅
- `hit_any_inclusive`: **47.2% → 49.7%** ✅

OOS (2026-01-01..01-09):
- strict `hit_any`: **4.1% → 4.1%** ✅ guardrail held
- `hit_any_inclusive`: **42.0% → 44.9%** ✅

## Why it worked (mechanics, not vibes)

The baseline sometimes overspends the top “spine” indices (up to 8 lines on one index), which reduces the number of lanes touched (breadth).

`spinecap6` caps the per-index spend in the spine to **6 lines**, and reallocates freed lines to the tail. Measured effect:
- more indices touched (breadth increases),
- winner-lane present rate increases,
- `CU_LANE_BUT_PLAY_MISS` decreases.

## Key artifacts (clickable)

Scoreboards (baseline vs cap6 vs cap7):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP_SWEEP.md:1`

Lane allocation (what changed in breadth/spikiness):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6.md:1`

Winner lane rank (confirms “winner lane is shoulder-heavy”; shows retention lift):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP_SWEEP.md:1`

Casebooks (example-level buckets for debugging):
- Jan cap6: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6__stable10__B36.md:1`
- OOS cap6: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6__stable10__B36.md:1`

Policy SSOT (now updated to make cap6 the default B36 posture):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md:1`

Worklog (baseline anchors + decision receipts):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP_SWEEP__2026-02-14.md:1`

## What not to do next (spiral prevention)

- Do not stack a second lever immediately.
- First let this promoted geometry be the new baseline; then iterate one change at a time again.

## Next highest-EV question (after you review this)

Now that lane retention improved, the next bottleneck is “within-lane conversion without destroying breadth” (making 1–2 lines per retained lane smarter).

