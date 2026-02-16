# Morning Brief — Robustness Windows (baseline) — 2026-02-16

Purpose:
- Add two extra holdout windows so Crossroads selection-geometry changes are not promoted based only on the Jan/OOS pair.
- Baseline only first (no new levers yet).

Locked invariants:
- Posture: `tool_only` + `stable10`
- Budget focus: `B36`
- Baseline strategy (current default): `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first`

Notes:
- Window metrics below exclude `winner_missing=1` (censored outcomes).
- Missing days are skipped automatically when grade artifacts are absent (expected; e.g., the known missing `sharepacks/_predictive/2026-01-19` gap inside the Jan window).

## Baseline rates (strict vs inclusive vs misses)

| Window | Date range | outcomes_n | strict_hit_any | hit_any_inclusive | CU_LANE_BUT_PLAY_MISS | CU_EXACT_BUT_PLAY_MISS |
|---|---|---:|---:|---:|---:|---:|
| Jan (in-sample) | 2026-01-15..2026-01-22 | 193 | 4.7% (9/193) | 58.0% (112/193) | 18.1% (35/193) | 2.6% (5/193) |
| OOS | 2026-01-01..2026-01-09 | 245 | 4.1% (10/245) | 53.1% (130/245) | 14.7% (36/245) | 3.3% (8/245) |
| Holdout A | 2025-12-30..2026-01-04 | 163 | 3.7% (6/163) | 56.4% (92/163) | 14.7% (24/163) | 3.7% (6/163) |
| Holdout B | 2025-06-21..2025-06-23 | 81 | 3.7% (3/81) | 50.6% (41/81) | 13.6% (11/81) | 1.2% (1/81) |

## Artifacts (baseline)

- Jan scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__BASELINE.md`
- OOS scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__BASELINE.md`
- Holdout A scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CONVERSION_SCOREBOARD__tool_only__stable10__B36__ROBUSTNESS_BASELINE.md`
- Holdout B scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CONVERSION_SCOREBOARD__tool_only__stable10__B36__ROBUSTNESS_BASELINE.md`

Ladders (B36 only):
- Jan ladder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_LADDER__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first__stable10.md`
- OOS ladder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_LADDER__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first__stable10.md`
- Holdout A ladder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CONVERSION_LADDER__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first__stable10.md`
- Holdout B ladder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CONVERSION_LADDER__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first__stable10.md`

