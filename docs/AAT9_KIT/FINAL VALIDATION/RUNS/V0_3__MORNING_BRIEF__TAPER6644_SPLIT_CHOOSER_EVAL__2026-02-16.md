# Morning Brief — Taper6644 Split Chooser Eval (B36, stable10) — 2026-02-16

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

Candidate (single lever — split chooser):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`
- Meaning: choose top-4 spine indices by `methods_first`, but choose the remaining tail indices by `score_total_first`.

## Results (B36 only; exclude `winner_missing=1`)

| Window | outcomes_n | strict_hit_any (base→cand) | hit_any_inclusive (base→cand) | CU_LANE_BUT_PLAY_MISS (base→cand) | CU_EXACT_BUT_PLAY_MISS (base→cand) |
|---|---:|---:|---:|---:|---:|
| Jan 2026-01-15..22 | 193 | 4.7% (9→9) | 58.0% (112→114) | 18.1% (35→34) | 2.6% (5→4) |
| OOS 2026-01-01..09 | 245 | 4.1% (10→10) | 53.1% (130→130) | 14.7% (36→36) | 3.3% (8→8) |
| Holdout A 2025-12-30..2026-01-04 | 163 | 3.7% (6→7) | 56.4% (92→92) | 14.7% (24→24) | 3.7% (6→6) |
| Holdout B 2025-06-21..23 | 81 | 3.7% (3→2) | 50.6% (41→42) | 13.6% (11→10) | 1.2% (1→1) |

## Gate decision

Decision: **NOT promoted**.

Why:
- OOS guardrails pass (strict + inclusive unchanged).
- Jan improves (inclusive +2 outcomes; lane miss -1 outcome).
- But robustness strict fails on Holdout B (strict drops by 1 hit: `3 → 2`, a `-1.2pp` change on `n=81`).

## Artifacts

Scoreboards (baseline vs candidate):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPLIT_CHOOSER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPLIT_CHOOSER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPLIT_CHOOSER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPLIT_CHOOSER.md`

Geometry invariants (baseline vs candidate):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPLIT_CHOOSER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPLIT_CHOOSER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPLIT_CHOOSER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPLIT_CHOOSER.md`

Winner lane rank (Jan + OOS; baseline vs candidate):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__SPLIT_CHOOSER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__SPLIT_CHOOSER.md`

Lane allocation (explicit, no overwrite collisions):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPLIT_CHOOSER__BASE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPLIT_CHOOSER__CAND.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPLIT_CHOOSER__BASE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPLIT_CHOOSER__CAND.md`

