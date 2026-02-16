# Morning Brief — Taper6644 “Sort Preset” Promotion (B36 • stable10 • tool_only) — 2026-02-16

This is the “read this first” summary of the latest Crossroads iteration.

## What changed (single lever)

Freeze geometry at the promoted taper6644 allocation (spine taper `6,6,4,4`), and change only the **index chooser** sort preset:

- Baseline (current default): `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644` (sort preset: `methods_first`)
- Candidate: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first` (sort preset: `score_total_first`)
- Also evaluated (rejected): `..._sort_packs_first`

No analyzer edits. Candidate Universe posture remains `stable10`. Budget remains **B36**.

## The only four numbers you need (promotion gates)

Baseline = `...spine_taper_6644`  
Candidate = `...sort_score_total_first`

Jan (2026-01-15..01-22):
- `CU_LANE_BUT_PLAY_MISS`: **19.7% → 18.1%** ✅
- `hit_any_inclusive`: **57.0% → 58.0%** ✅

OOS (2026-01-01..01-09):
- strict `hit_any`: **4.1% → 4.1%** ✅ guardrail held
- `hit_any_inclusive`: **51.8% → 53.1%** ✅

## Decision

- **Promoted** `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first` as the new **B36 conversion default**.
- Rejected `..._sort_packs_first` (regresses OOS strict and inclusive).

## Notes (important nuance)

- `CU_EXACT_BUT_PLAY_MISS` regresses slightly under `score_total_first` (OOS: `2.4% → 3.3%`). This did **not** break the strict guardrail and is acceptable in the current isolation-first phase, but it should be watched.

## Key artifacts (clickable)

Scoreboards (baseline vs chooser variants):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6644_SORT_PRESET_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6644_SORT_PRESET_SWEEP.md:1`

Geometry invariants (proves geometry unchanged; only membership changes):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAPER6644_SORT_PRESET_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAPER6644_SORT_PRESET_SWEEP.md:1`

Casebooks (B36-only; examples):
- Jan candidate: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first__stable10__B36.md:1`
- OOS candidate: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first__stable10__B36.md:1`

Policy SSOT (now updated):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md:1`

Worklog (repro + outputs):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__WORKLOG__TAPER6644_SORT_PRESET_PROMOTION__2026-02-16.md:1`

