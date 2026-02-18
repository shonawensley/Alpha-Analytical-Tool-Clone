# Morning Brief — Taper6644 Spine Packs-First Precheck (B36, stable10) — 2026-02-18

Goal (isolation-first, selection-layer only):
- Improve `hit_any_inclusive` / reduce `CU_LANE_BUT_PLAY_MISS` without violating OOS guardrails.
- One lever only: change **spine index ordering** (what gets 6/6/4/4 lines).

Locked invariants:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: `B36`
- Geometry: `taper6644` + `spinecap6`
- Scope: selection-layer only (no analyzer edits)

## Strategies

Baseline (current default):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`

Candidate (single lever — spine packs-first):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_packs_tail_score_total_first`
- Meaning: choose top-4 spine indices by `packs_first`, keep tail indices by `score_total_first`.

## Precheck 1: geometry / “is the lever real?” (Jan roster)

- Geometry report:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINE_PACKS_PRECHECK.md`
- Key results (rows=193):
  - Candidate `no_op_rate`: `0.0933` (active; large change)
  - Candidate `diff_new_lines` mean/p90: `6.187` / `~10.8`

## Precheck 2: Jan scoreboard

- Scoreboard:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE_PACKS_PRECHECK.md`

Results (rows=193):
- `hit_any_inclusive`: `59.1% → 59.6%` (improves)
- `CU_LANE_BUT_PLAY_MISS`: `17.6% → 16.6%` (improves)
- strict `hit_any`: `4.7% → 3.6%` (regresses)

## OOS guardrail check

- OOS scoreboard:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE_PACKS_PRECHECK.md`

Result: **reject / not promoted**.
- OOS strict regresses (`4.1% → 3.3%`), failing the hard guardrail.

