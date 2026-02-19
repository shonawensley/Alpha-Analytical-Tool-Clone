# Morning Brief — Tail Cross-Lens Injection Source Sweep (B36, stable10) — 2026-02-19

Goal (selection-layer only; isolation-first with strict guardrails):
- See if we can get an additional lift in `hit_any_inclusive` / `CU_LANE_BUT_PLAY_MISS` by changing **where** the two injected shoulder tail lanes come from, while keeping the promoted tail-spread schedule and geometry locked.

Locked invariants:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: `B36` only
- Scope: selection-layer only (no analyzer edits)
- Geometry: `taper6644` + `spinecap6` (spine 6/6/4/4; tail 1-line/index)

## Baseline (current default)

- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

Meaning:
- keep top14 tail indices from `score_total_first` (excluding spine)
- inject 1 tail index from `methods_first` @ pos18
- inject 1 tail index from `packs_first` @ pos22

## Candidates (single lever: injection source only; same schedule + geometry)

- `...tail_spread_top14_pos18_22__xlens_m18_m22` (methods@18 + methods@22)
- `...tail_spread_top14_pos18_22__xlens_p18_p22` (packs@18 + packs@22)
- `...tail_spread_top14_pos18_22__xlens_p18_m22` (packs@18 + methods@22)

## Jan window (in-sample) — precheck sweep

Scoreboard:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_SOURCE_SWEEP_PRECHECK.md`

Key result:
- `__xlens_m18_m22` showed a small Jan lift:
  - `hit_any_inclusive`: `63.7% → 64.2%` (+0.5pp)
  - `CU_LANE_BUT_PLAY_MISS`: `13.5% → 13.0%` (-0.5pp)
- Other source variants regressed Jan isolation.

Lever effectiveness (geometry; Jan):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAIL_XLENS_SOURCE_SWEEP_PRECHECK_JAN.md`
  - `__xlens_m18_m22` was near-no-op (`no_op_rate` ~0.93), so OOS gating was required to confirm signal vs noise.

Decision: run full gates only for `__xlens_m18_m22`.

## OOS window (hard gates)

Scoreboard:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_M18_M22_GATE.md`

Result:
- `hit_any_inclusive`: `55.1% → 54.7%` (**regress**, fails OOS hard gate)
- `CU_LANE_BUT_PLAY_MISS`: `13.9% → 14.3%` (worse)
- strict `hit_any`: `4.5% → 4.5%` (no regress, but not sufficient)

Decision: **reject / not promoted**.

## Robustness windows (for completeness)

Holdout A:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_M18_M22_GATE.md`

Holdout B:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_XLENS_M18_M22_GATE.md`

Both were ties vs baseline, but OOS already failed.

## Takeaway / next lever direction

This source-swap is too weak and does not survive OOS, so the next levers should be:
- touched-set diversity that is still **targeted** (like the promoted methods+packs injection), or
- move to a different lever class (e.g., add a 3rd injected shoulder lane under fixed B36 by trading 1 of the top14 tail lanes), while keeping geometry locked and using the same staircase gates.

