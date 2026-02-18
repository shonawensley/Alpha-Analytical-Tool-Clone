# Morning Brief — Taper6643 Split Chooser Eval (B36, stable10) — 2026-02-18

Goal (isolation-first, selection-layer only):
- Improve `hit_any_inclusive` / reduce `CU_LANE_BUT_PLAY_MISS` without violating the OOS strict guardrail.
- One lever only: change **spine taper geometry** (how many lines the 4 spine indices receive).

Locked invariants:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: `B36`
- Index chooser: split (spine=`methods_first`, tail=`score_total_first`)
- Scope: selection-layer only (no analyzer edits)

## Strategies

Baseline (current default):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`

Candidate (single lever — taper6643):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643_split_spine_methods_tail_score_total_first`
- Meaning: keep the split chooser, but taper spine allocations as `6/6/4/3` (free 1 tail line vs `6/6/4/4`).

## Precheck 1: geometry / “is the lever real?” (Jan roster)

- Geometry report (Jan):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAPER6643_SPLIT_PRECHECK.md`
- Key results (rows=193):
  - Candidate `no_op_rate`: `0.0829` (changes ~1 line per outcome, as expected)
  - indices touched increases (mean): `~21.2` (baseline is 20)

## Precheck 2: Jan scoreboard

- Scoreboard (Jan):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6643_SPLIT_PRECHECK.md`

Results (rows=193):
- strict `hit_any`: `4.7% → 4.7%` (unchanged)
- `hit_any_inclusive`: `59.1% → 62.2%` (improves)
- `CU_LANE_BUT_PLAY_MISS`: `17.6% → 14.5%` (improves)

## OOS hard guardrail check

- Scoreboard (OOS):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6643_SPLIT_PRECHECK.md`

Decision: **reject / not promoted**.
- OOS strict regresses (`4.1% → 3.7%`), failing the hard guardrail (even though OOS inclusive improves `53.1% → 55.5%`).

