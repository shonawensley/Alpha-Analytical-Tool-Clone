# Morning Brief — Taper6644 Constraint Chooser Eval (B36, stable10) — 2026-02-17

Goal (isolation-first, selection-layer only):
- Improve `hit_any_inclusive` / reduce `CU_LANE_BUT_PLAY_MISS` without violating the OOS strict guardrail.
- One lever only (no analyzer edits, no CU posture change).

Locked invariants:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: `B36`
- Geometry: `taper6644` + `spinecap6`

## Strategies

Baseline (current default):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first`

Candidate (single lever — constraint chooser):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_constraint_spine_methods2_or_var1_sort_score_total_first`
- Meaning: keep `score_total_first` ranking and taper6644 geometry, but constrain the **top-4 spine indices** to lanes with corroboration:
  - `methods_count >= 2` OR `variants_non_unknown >= 1`
  - If fewer than 4 qualify, fill remaining spine slots from the unconstrained ranking.

## Results (B36 only; exclude `winner_missing=1`)

| Window | outcomes_n | strict_hit_any (base→cand) | hit_any_inclusive (base→cand) | CU_LANE_BUT_PLAY_MISS (base→cand) | CU_EXACT_BUT_PLAY_MISS (base→cand) |
|---|---:|---:|---:|---:|---:|
| Jan 2026-01-15..22 | 193 | 4.7% (9→9) | 58.0% (112→112) | 18.1% (35→35) | 2.6% (5→5) |
| OOS 2026-01-01..09 | 245 | 4.1% (10→10) | 53.1% (130→130) | 14.7% (36→36) | 3.3% (8→8) |
| Holdout A 2025-12-30..2026-01-04 | 163 | 3.7% (6→6) | 56.4% (92→92) | 14.7% (24→24) | 3.7% (6→6) |
| Holdout B 2025-06-21..23 | 81 | 3.7% (3→3) | 50.6% (41→41) | 13.6% (11→11) | 1.2% (1→1) |

## Gate decision

Decision: **NOT promoted**.

Why:
- No measurable improvement on the Jan semi-hard gate (`hit_any_inclusive` and `CU_LANE_BUT_PLAY_MISS` are unchanged).
- OOS hard guardrails hold (strict + inclusive unchanged).
- Robustness windows are unchanged.

Additional note:
- This lever is mostly a no-op in practice under `score_total_first` ordering:
  - Jan geometry shows a small line diff in ~3% of outcomes, but it did not change any bucket outcomes.
  - OOS geometry shows an even smaller diff rate (<1%).

## Artifacts

Scoreboards (baseline vs candidate):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CONVERSION_SCOREBOARD__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CONVERSION_SCOREBOARD__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`

Geometry invariants (baseline vs candidate):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`

Winner lane rank (Jan + OOS; baseline vs candidate):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__CONSTRAINT_CHOOSER.md:1`

Lane allocation (explicit, no overwrite collisions):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__CONSTRAINT_CHOOSER__BASE.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__CONSTRAINT_CHOOSER__CAND.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__CONSTRAINT_CHOOSER__BASE.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__CONSTRAINT_CHOOSER__CAND.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__LANE_ALLOCATION__tool_only__stable10__B36__CONSTRAINT_CHOOSER__BASE.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__LANE_ALLOCATION__tool_only__stable10__B36__CONSTRAINT_CHOOSER__CAND.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__LANE_ALLOCATION__tool_only__stable10__B36__CONSTRAINT_CHOOSER__BASE.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__LANE_ALLOCATION__tool_only__stable10__B36__CONSTRAINT_CHOOSER__CAND.md:1`

