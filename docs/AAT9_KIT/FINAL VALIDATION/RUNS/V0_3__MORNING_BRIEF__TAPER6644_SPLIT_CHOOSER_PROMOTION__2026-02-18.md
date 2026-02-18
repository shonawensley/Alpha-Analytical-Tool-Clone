# Morning Brief — Taper6644 Split Chooser Promotion (B36, stable10) — 2026-02-18

Context:
- `split chooser` was evaluated on 2026-02-16 and rejected due to a **1-hit strict drop** on the small-N Holdout B window.
- The Crossroads policy now uses a **count-based** strict material-regress gate on robustness windows (to avoid small-N false vetoes).

Goal (isolation-first, selection-layer only):
- Improve `hit_any_inclusive` / reduce `CU_LANE_BUT_PLAY_MISS` while preserving the **OOS strict guardrail**.

Locked invariants:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: `B36`
- Geometry: `taper6644` + `spinecap6`
- Scope: selection-layer only (no analyzer edits)

## Strategies

Baseline (current default):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first`

Candidate (single lever — split chooser):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`
- Meaning: choose top-4 spine indices by `methods_first`, then choose remaining tail indices by `score_total_first`.

## Results (B36 only; exclude `winner_missing=1`)

| Window | outcomes_n | strict_hit_any (base→cand) | hit_any_inclusive (base→cand) | CU_LANE_BUT_PLAY_MISS (base→cand) | CU_EXACT_BUT_PLAY_MISS (base→cand) |
|---|---:|---:|---:|---:|---:|
| Jan 2026-01-15..22 | 193 | 4.7% (9→9) | 58.0% (112→114) | 18.1% (35→34) | 2.6% (5→4) |
| OOS 2026-01-01..09 | 245 | 4.1% (10→10) | 53.1% (130→130) | 14.7% (36→36) | 3.3% (8→8) |
| Holdout A 2025-12-30..2026-01-04 | 163 | 3.7% (6→7) | 56.4% (92→92) | 14.7% (24→24) | 3.7% (6→6) |
| Holdout B 2025-06-21..23 | 81 | 3.7% (3→2) | 50.6% (41→42) | 13.6% (11→10) | 1.2% (1→1) |

## Gate decision

Decision: **PROMOTED** (new B36 default for stable10/tool_only).

Why (under the Crossroads v0.3 policy gates):
- OOS hard gates pass: strict and inclusive are unchanged vs baseline.
- Jan semi-hard gates pass: inclusive improves (+2 outcomes) and lane miss improves (-1 outcome).
- Robustness strict no longer false-vetoes small-N: Holdout B strict drops by 1 hit on `n=81`, which is **not** a material regress under the count-based rule.

## References

- Prior eval brief (rejected under the old robustness strict rule): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SPLIT_CHOOSER_EVAL__2026-02-16.md`
- Scoreboards (baseline vs candidate):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPLIT_CHOOSER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPLIT_CHOOSER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPLIT_CHOOSER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPLIT_CHOOSER.md`
