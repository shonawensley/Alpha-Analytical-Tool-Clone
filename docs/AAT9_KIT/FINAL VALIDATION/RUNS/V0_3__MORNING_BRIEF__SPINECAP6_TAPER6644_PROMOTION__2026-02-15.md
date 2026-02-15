# Morning Brief — Spinecap6 “Taper 6644” Promotion (B36 • stable10 • tool_only) — 2026-02-15

This is the “read this first” summary of the latest Crossroads iteration.

## What changed (single lever)

- Added one allocation-geometry variant on top of the promoted B36 baseline:
  - Baseline: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`
  - Candidate: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644`
- **Promoted** `...spine_taper_6644` as the new **B36 conversion default** (policy updated).
- No analyzer edits. Candidate Universe posture remains `stable10`.

## The only four numbers you need (promotion gates)

Baseline = `...spinecap6`  
Candidate = `...spine_taper_6644`

Jan (2026-01-15..01-22):
- `CU_LANE_BUT_PLAY_MISS`: **25.9% → 19.7%** ✅
- `hit_any_inclusive`: **49.7% → 57.0%** ✅

OOS (2026-01-01..01-09):
- strict `hit_any`: **4.1% → 4.1%** ✅ guardrail held
- `hit_any_inclusive`: **44.9% → 51.8%** ✅

## Why it worked (mechanics, not vibes)

`spinecap6` spends 6 lines in each of the 4 spine indices (24 lines), leaving 12 tail lines.

The taper variant changes only the spine allocation:
- top 2 spine indices: **6** lines each
- next 2 spine indices: **4** lines each

This frees **4 lines** to extend the tail, increasing breadth (indices touched) by ~4 on average.

Measured effect (both windows):
- indices touched (mean): ~16 → ~20 (geometry report),
- `CU_LANE_BUT_PLAY_MISS` decreases materially,
- `hit_any_inclusive` increases materially,
- OOS strict guardrail holds.

## Key artifacts (clickable)

Scoreboards (baseline vs taper):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6644_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6644_SWEEP.md:1`

Geometry invariants (breadth + no-op deltas; taper metadata recorded):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_TAPER6644_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_TAPER6644_SWEEP.md:1`

Winner lane rank sweep (lane ranking vs retention sanity):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_TAPER6644_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_TAPER6644_SWEEP.md:1`

Casebooks (example buckets; B36-only):
- Jan taper: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644__stable10__B36.md:1`
- OOS taper: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644__stable10__B36.md:1`

Policy SSOT (now updated to make taper6644 the default B36 posture):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md:1`

Worklog (repro + outputs; includes lane-allocation filename hardening note):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_TAPER6644_PROMOTION__2026-02-15.md:1`

## Guardrail note

Jan strict `hit_any` regresses slightly (**5.2% → 4.7%**) while OOS strict holds; this is acceptable under the Crossroads gates (strict is an **OOS guardrail**, not the Jan objective in isolation-first phase).

