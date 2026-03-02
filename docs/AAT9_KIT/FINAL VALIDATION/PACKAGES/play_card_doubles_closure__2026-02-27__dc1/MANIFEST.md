# Play Card Doubles/Mirror‑Doubles Closure — Evidence Pack (dc1)

This pack is a **review hub** for the additive B36 conversion strategies:

- `v0_3_b36_doubles_closure_v1` (aggressive doubles-first)
- `v0_3_b36_doubles_closure_v2` (mixed; preserves singles when depth≥4, evidence-first when depth=1)

It is intentionally isolated under experiment tag `dc1` to avoid overwriting the baseline `stable10` artifacts.

## Specs / How it works
- Strategy spec: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PLAY_CARD_STRATEGY__B36__DOUBLES_CLOSURE.md`
- Implementation: `scripts/tools/create_play_card.py`

## Where to open the “closure trace” (human-auditable)
Example (Ohio, 2026‑01‑04):
- Play card JSON: `sharepacks/_predictive/2026-01-04/Ohio4/play_card__tool_only__dc1.json`
- Trace path inside JSON:
  - `strategies.v0_3_b36_doubles_closure_v2.B36.vtrac_pack.closure_trace`

## Top-line scoreboards (baseline vs v1 vs v2)
OOS window (2026‑01‑01..2026‑01‑09):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__dc1__B36__DOUBLES_CLOSURE_SWEEP.md`

Jan gold window (2026‑01‑15..2026‑01‑22):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__dc1__B36__DOUBLES_CLOSURE_SWEEP.md`

## Daily predictive portfolios (dc1, B36 closure v2)
These mirror the baseline predictive portfolios, but display B36 using `v0_3_b36_doubles_closure_v2` sourced from `play_card__tool_only__dc1.json`.

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-22__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`

## Full ladders + casebooks (debuggable examples)
OOS window:
- Baseline ladder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_LADDER__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22__dc1.md`
- v1 ladder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_LADDER__tool_only__v0_3_b36_doubles_closure_v1__dc1.md`
- v2 ladder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_LADDER__tool_only__v0_3_b36_doubles_closure_v2__dc1.md`
- OOS casebooks (B36):
  - Baseline: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22__dc1__B36.md`
  - v1: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_3_b36_doubles_closure_v1__dc1__B36.md`
  - v2: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_3_b36_doubles_closure_v2__dc1__B36.md`

Jan gold window:
- Baseline ladder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_LADDER__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22__dc1.md`
- v1 ladder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_LADDER__tool_only__v0_3_b36_doubles_closure_v1__dc1.md`
- v2 ladder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_LADDER__tool_only__v0_3_b36_doubles_closure_v2__dc1.md`
- Jan casebooks (B36):
  - Baseline: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22__dc1__B36.md`
  - v1: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_3_b36_doubles_closure_v1__dc1__B36.md`
  - v2: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_3_b36_doubles_closure_v2__dc1__B36.md`

## Lane allocation (did we change breadth/depth?)
OOS:
- Baseline: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_ta__1efd02cb__dc1__B36__baseline.md`
- v1: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__v0_3_b36_doubles_closure_v1__dc1__B36__closure_v1.md`
- v2: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__v0_3_b36_doubles_closure_v2__dc1__B36__closure_v2.md`

Jan:
- Baseline: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_ta__1efd02cb__dc1__B36__baseline.md`
- v1: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__v0_3_b36_doubles_closure_v1__dc1__B36__closure_v1.md`
- v2: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__v0_3_b36_doubles_closure_v2__dc1__B36__closure_v2.md`
