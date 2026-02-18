# Morning Brief — Taper6644 Tail Packs-First Precheck (B36, stable10) — 2026-02-18

Goal (isolation-first, selection-layer only):
- Improve `hit_any_inclusive` / reduce `CU_LANE_BUT_PLAY_MISS` without violating OOS guardrails.
- One lever only: adjust **tail index ordering** while freezing the top-4 spine indices.

Locked invariants:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: `B36`
- Geometry: `taper6644` + `spinecap6`
- Scope: selection-layer only (no analyzer edits)

## Strategies

Baseline (current default):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`

Candidate (single lever — tail packs-first):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_packs_first`
- Meaning:
  - Spine indices: frozen to `methods_first` (top‑4), same as baseline.
  - Tail indices: chosen by `packs_first` ordering (instead of `score_total_first`).

## Precheck 1: geometry / “is the lever real?” (Jan roster)

- Geometry report:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAIL_PACKS_PRECHECK.md`
- Key results (rows=193):
  - Candidate `no_op_rate`: `0.2902` (lever is active)
  - Candidate `diff_new_lines` mean/p90: `1.373` / `3.0`
  - Geometry invariants: no cap violations; indices_touched_count distribution unchanged.

## Precheck 2: Jan scoreboard (stop if it can’t be promoted)

- Scoreboard (baseline vs candidate):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_PACKS_PRECHECK.md`

Results (rows=193):
- `hit_any_inclusive`: `59.1% → 57.0%` (regress)
- `CU_LANE_BUT_PLAY_MISS`: `17.6% → 18.1%` (worse)
- `CU_EXACT_BUT_PLAY_MISS`: `2.1% → 3.6%` (worse)
- strict `hit_any`: `4.7% → 4.7%` (unchanged)

Decision: **reject / not promoted** (fails isolation-first direction on Jan).

