# Morning Brief — Taper6644 Spine Ranked Sweep (B36 • stable10 • tool_only) — 2026-02-15

This is a single-lever follow-up on the promoted B36 default (`...spine_taper_6644`).

## What changed (single lever)

Baseline:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644` (fixed display order inside the spine)

Candidates (same geometry; different spine member ordering):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_ranked`
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_canon_ranked`

Meaning: keep taper6644 allocation exactly the same, but choose the **4 spine lines** inside the tapered indices (ranks 3–4) using evidence-ranked display order.

## Results (no promotion)

Jan (2026-01-15..01-22):
- strict `hit_any`: **4.7% → 3.1%** ❌ (regression)
- `hit_any_inclusive`: **57.0% → 57.0%** (no change)

OOS (2026-01-01..01-09):
- strict `hit_any`: **4.1% → 4.1%** (no change)
- `hit_any_inclusive`: **51.8% → 51.8%** (no change)

Decision:
- **Not promoted.** These variants do not improve isolation metrics, and they regress Jan strict.

## Key artifacts (clickable)

Scoreboards (baseline vs ranked variants):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6644_SPINE_RANKED_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6644_SPINE_RANKED_SWEEP.md:1`

Casebooks (B36-only; examples):
- Jan display-ranked: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_ranked__stable10__B36.md:1`
- Jan canon-ranked: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_canon_ranked__stable10__B36.md:1`

Worklog (repro + outputs):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__TAPER6644_SPINE_RANKED_SWEEP__2026-02-15.md:1`

