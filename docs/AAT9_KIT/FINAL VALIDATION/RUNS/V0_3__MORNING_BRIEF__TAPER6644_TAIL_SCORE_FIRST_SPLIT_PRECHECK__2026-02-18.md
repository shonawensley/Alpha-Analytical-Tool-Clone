# Morning Brief — Split Chooser + Tail Score-First Precheck (B36, stable10) — 2026-02-18

Goal (selection-layer only; isolation-first with strict guardrails):
- Test a **within-tail representative quality lever** while freezing index selection + geometry.
- Fail fast if Jan precheck does not show a conversion win signal.

## Baseline verification (SSOT)

Baseline strategy (current default) was read from:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md:73`

Baseline:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`

## Lever under test

Candidate (single lever: **tail 1-line/index representative choice only**):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_score_first`
- Meaning: keep split chooser (`spine=methods_first`, `tail=score_total_first`) and taper6644 geometry, but set `tail_pick_mode=score_first`.

Locked invariants:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: `B36`
- Geometry: `taper6644` + `spinecap6`
- Scope: selection-layer only (no analyzer edits)

## Precheck 1: geometry / “is the lever real?” (Jan roster)

Geometry report:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAPER6644_TAIL_SCORE_FIRST_SPLIT_PRECHECK.md`

Key results (rows=193):
- Candidate `no_op_rate`: `0.2694` (active)
- Candidate `diff_new_lines` mean/p90: `1.114` / `2.0`
- Cap/taper violations: `0`

## Precheck 2: Jan scoreboard (stop/continue)

Scoreboard:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6644_TAIL_SCORE_FIRST_SPLIT_PRECHECK.md`

Results (rows=193):
- strict `hit_any`: `4.7% → 4.7%` (unchanged)
- `hit_any_inclusive`: `59.1% → 59.1%` (unchanged)
- `CU_LANE_BUT_PLAY_MISS`: `17.6% → 17.6%` (unchanged)
- `CU_EXACT_BUT_PLAY_MISS`: `2.1% → 2.1%` (unchanged)
- `pack_box_hit`: `21.2% → 20.2%` (regresses)

Decision: **reject / not promoted**.
- The lever changes lines, but does not produce any measurable conversion win on Jan.
- Per fail-fast discipline, **OOS/holdouts were not run** for this lever.

