# Morning Brief — Spinecap6 “Taper 6633” Evaluation (B36 • stable10 • tool_only) — 2026-02-15

This is a single-lever follow-up on the promoted B36 default (`...spine_taper_6644`).

## What changed (single lever)

- Baseline (current B36 default): `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644`
- Candidate: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6633`
- Change: taper the last 2 spine indices to **3 lines** each (vs **4**), freeing **2** more lines for tail breadth.
- No analyzer edits. CU posture remains `stable10`. Budget remains **B36**.

## The only four numbers you need (promotion gates)

Baseline = `...spine_taper_6644`  
Candidate = `...spine_taper_6633`

Jan (2026-01-15..01-22):
- `CU_LANE_BUT_PLAY_MISS`: **19.7% → 14.5%** ✅
- `hit_any_inclusive`: **57.0% → 63.2%** ✅

OOS (2026-01-01..01-09):
- strict `hit_any`: **4.1% → 3.7%** ❌ guardrail failed (regression)
- `hit_any_inclusive`: **51.8% → 57.1%** ✅

## Decision

- **Not promoted.** The OOS strict guardrail regressed (`4.1% → 3.7%`).
- Keep B36 default: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644`.

## What we learned (useful, even without promotion)

- More taper (more breadth) continues to reduce:
  - `CU_LANE_BUT_PLAY_MISS` (lane retention improves),
  - `CU_EXACT_BUT_PLAY_MISS` (exact-in-CU misses shrink),
  - and lifts `hit_any_inclusive`.
- But pushing the spine below **4 lines** on ranks 3–4 is enough to measurably lower OOS strict hits in the current windows.

## Key artifacts (clickable)

Scoreboards (baseline vs candidate):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6633_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6633_SWEEP.md:1`

Geometry invariants (cap proof + taper metadata):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_TAPER6633_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_TAPER6633_SWEEP.md:1`

Winner lane rank sweep:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_TAPER6633_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_TAPER6633_SWEEP.md:1`

Casebooks (B36-only; concrete examples):
- Jan candidate: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6633__stable10__B36.md:1`
- OOS candidate: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6633__stable10__B36.md:1`

Worklog (repro + outputs):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_TAPER6633_EVAL__2026-02-15.md:1`

