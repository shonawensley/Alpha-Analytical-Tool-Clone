# Morning Brief — Spinecap6 “Taper 6643” Evaluation (B36 • stable10 • tool_only) — 2026-02-15

This is a single-lever micro-taper follow-up on the promoted B36 default (`...spine_taper_6644`).

## What changed (single lever)

- Baseline (current B36 default): `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644`
- Candidate: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643`
- Change: taper only the 4th spine index from **4 → 3** lines (free **+1** tail line).
- No analyzer edits. CU posture remains `stable10`. Budget remains **B36**.

## The only four numbers you need (promotion gates)

Baseline = `...spine_taper_6644`  
Candidate = `...spine_taper_6643`

Jan (2026-01-15..01-22):
- `CU_LANE_BUT_PLAY_MISS`: **19.7% → 16.6%** ✅
- `hit_any_inclusive`: **57.0% → 60.6%** ✅

OOS (2026-01-01..01-09):
- strict `hit_any`: **4.1% → 3.7%** ❌ guardrail failed (regression)
- `hit_any_inclusive`: **51.8% → 54.3%** ✅

## Decision

- **Not promoted.** The OOS strict guardrail regressed (`4.1% → 3.7%`).
- Keep B36 default: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644`.

## Key artifacts (clickable)

Scoreboards (baseline vs candidate):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1`

Geometry invariants:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1`

Winner lane rank sweep:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1`

Worklog (repro + outputs):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__SPINECAP6_TAPER6643_EVAL__2026-02-15.md:1`

