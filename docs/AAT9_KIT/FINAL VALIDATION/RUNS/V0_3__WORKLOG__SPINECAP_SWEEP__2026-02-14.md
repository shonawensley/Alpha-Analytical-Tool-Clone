# Worklog — Spinecap Sweep (anti-spike) — 2026-02-14

Purpose
- Track the end-to-end Crossroads iteration (selection-layer only) so progress survives power-offs and chat resets.
- Experiment family: **anti-spike spine cap** on `v0_2_default_multi_pack_packheavy_spine4_index_tail` (B36).

Repo state
- Branch: `checkpoint/v0_3-stable10-shoulder-depth`
- Tip: `878d3361` (run `git log -1 --oneline` to confirm)

Locked posture (SSOT)
- Profile: `tool_only`
- Experiment tag: `stable10`
- Budget surface: **B36-only**
- Objective: **isolation-first** (reduce `CU_LANE_BUT_PLAY_MISS`)
- Guardrail: **OOS strict `hit_any` must not regress** (baseline `4.1%`)
- No analyzer edits (selection-layer only).

Baseline (current promoted) strategy
- `v0_2_default_multi_pack_packheavy_spine4_index_tail`

## Baseline scoreboard anchors (what we must beat / not regress)

Jan gold window (in-sample)
- Scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`
- CU lane recall (`CU union vtrac_index_hit`): `78.8%`
- Play Card inclusive (`hit_any_inclusive`): `47.2%`
- Play Card strict (`hit_any`): `5.7%`
- `CU_LANE_BUT_PLAY_MISS`: `26.9%`
- `CU_EXACT_BUT_PLAY_MISS`: `4.7%`

OOS window (guardrail)
- Scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`
- CU lane recall (`CU union vtrac_index_hit`): `71.0%`
- Play Card inclusive (`hit_any_inclusive`): `42.0%`
- Play Card strict (`hit_any`): `4.1%`  ← **guardrail floor**
- `CU_LANE_BUT_PLAY_MISS`: `24.1%`
- `CU_EXACT_BUT_PLAY_MISS`: `4.9%`

## Derived “shoe squeeze” ratios (baseline; from FEB14_PRO)

Lane retention given lane was available:
- Jan: `47.2 / 78.8 ≈ 0.599` (≈ `59.9%`)
- OOS: `42.0 / 71.0 ≈ 0.592` (≈ `59.2%`)

Meaning: ~`40%` of lane-available outcomes are lost at the **B36 CU → Play Card** compression step.

## Promotion gates (hard)

To promote a new B36 selection policy:
- Jan: `CU_LANE_BUT_PLAY_MISS < 26.9%` AND `hit_any_inclusive ≥ 47.2%`
- OOS: strict `hit_any ≥ 4.1%`

## Next experiment (spinecap sweep)

Candidate variants (one lever; no stacking):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap7`

Intent:
- Cap overspend in the 4-pack spine (some traces show “8 lines in one index” spikes),
- reallocate freed lines to tail/breadth,
- reduce `CU_LANE_BUT_PLAY_MISS` without repeating the “shoulder-depth” regression.

## Results (promotion decision)

Sweep scoreboards:
- Jan: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP_SWEEP.md`
- OOS: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP_SWEEP.md`

### v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6 (PROMOTED)

Jan:
- `hit_any_inclusive`: `49.7%` (baseline `47.2%`)
- `CU_LANE_BUT_PLAY_MISS`: `25.9%` (baseline `26.9%`)
- `CU_EXACT_BUT_PLAY_MISS`: `3.1%` (baseline `4.7%`)

OOS:
- strict `hit_any`: `4.1%` (baseline `4.1%`) ✅ guardrail held
- `hit_any_inclusive`: `44.9%` (baseline `42.0%`)
- `CU_LANE_BUT_PLAY_MISS`: `22.4%` (baseline `24.1%`)
- `CU_EXACT_BUT_PLAY_MISS`: `3.7%` (baseline `4.9%`)

Derived retention ratio (`hit_any_inclusive / CU vtrac_index_hit`):
- Jan: `49.7 / 78.8 ≈ 0.631` (baseline `0.599`)
- OOS: `44.9 / 71.0 ≈ 0.632` (baseline `0.592`)

Key mechanical shift (lane allocation):
- Baseline max lines on any index: `8` → cap6 forces max `6` and increases indices touched.
  - Jan lane allocation (baseline): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`
  - Jan lane allocation (cap6): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6.md`

Decision:
- Promote `...spinecap6` as the B36 conversion default (policy updated).

### v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap7 (NOT promoted)

- Strict held, but Jan `CU_LANE_BUT_PLAY_MISS` did not improve (remains `26.9%`), so it does not pass the isolation-first gate.
