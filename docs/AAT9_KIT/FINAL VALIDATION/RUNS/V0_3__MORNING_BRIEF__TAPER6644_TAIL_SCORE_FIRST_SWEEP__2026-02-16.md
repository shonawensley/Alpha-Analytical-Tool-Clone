# Morning Brief — Taper6644 Tail Representative Sweep (B36 • stable10 • tool_only) — 2026-02-16

Goal: keep the **promoted** taper6644 + `score_total_first` chooser fixed, and test one small lever:
**how we pick the 1-line/index tail representative** inside each ranked tail lane.

Lock:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: **B36 only**
- Selection-layer only (no analyzer edits)

## What changed (single lever)

Baseline (current B36 default):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first`
  - tail pick: `convergence` (existing behavior: first convergence-ranked row per index)

Candidate:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first_tail_score_first`
  - tail pick: `score_first` (highest-score row first, then convergence tie-break)

Geometry and index membership are unchanged; only the **tail row choice** can differ.

## The only four numbers you need

Jan (2026-01-15..01-22):
- strict `hit_any`: **4.7% → 4.7%** (no change)
- `hit_any_inclusive`: **58.0% → 58.0%** (no change)
- `CU_LANE_BUT_PLAY_MISS`: **18.1% → 18.1%** (no change)
- `CU_EXACT_BUT_PLAY_MISS`: **2.6% → 2.6%** (no change)

OOS (2026-01-01..01-09):
- strict `hit_any`: **4.1% → 4.5%** ✅ guardrail held (tiny lift)
- `hit_any_inclusive`: **53.1% → 53.1%** (no change)

## Decision

- **Not promoted**.
- Rationale: the candidate does not produce any measurable in-sample lift, and the OOS strict lift
  is only +1 hit on this window (likely variance). Keep it as an available variant for future
  multi-window robustness checks.

## Key artifacts (clickable)

Scoreboards (baseline vs tail variant):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6644_TAIL_SCORE_FIRST_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6644_TAIL_SCORE_FIRST_SWEEP.md:1`

Geometry invariants (proves geometry unchanged; shows diff rate):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAPER6644_TAIL_SCORE_FIRST_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAPER6644_TAIL_SCORE_FIRST_SWEEP.md:1`

Casebooks (candidate; B36-only):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first_tail_score_first__stable10__B36.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first_tail_score_first__stable10__B36.md:1`

