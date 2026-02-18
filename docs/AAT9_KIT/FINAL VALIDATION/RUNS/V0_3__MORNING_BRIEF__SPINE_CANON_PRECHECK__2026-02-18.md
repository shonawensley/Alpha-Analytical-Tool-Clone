# Morning Brief — Split Chooser + Spine Canon-Ranked Precheck (B36, stable10) — 2026-02-18

Goal (selection-layer only; isolation-first with strict guardrails):
- Test a **within-spine conversion lever** while freezing index selection + geometry.
- Fail fast if Jan precheck regresses strict or does not show a conversion win signal.

## Baseline verification (SSOT)

Baseline strategy (current default) was read from:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md:117`

Baseline:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`

## Lever under test

Candidate (single lever: within-spine member choice only):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_spine_display_canon_ranked`
- Meaning: keep split chooser (`spine=methods_first`, `tail=score_total_first`) and taper6644 geometry, but set `spine_pick_mode=display_canon_ranked`.

Locked invariants:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: `B36`
- Geometry: `taper6644` + `spinecap6`
- Scope: selection-layer only (no analyzer edits)

## Precheck 1: geometry / “is the lever real?” (Jan roster)

Geometry report:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINE_CANON_PRECHECK.md`

Key results (rows=193):
- Candidate `no_op_rate`: `0.1865` (active)
- Candidate `diff_new_lines` mean/p90: `1.772` / `~3.8`
- Cap/taper violations: `0`

## Precheck 2: Jan scoreboard (stop/continue)

Scoreboard:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE_CANON_PRECHECK.md`

Results (rows=193):
- strict `hit_any`: `4.7% → 3.1%` (regresses)
- `hit_any_inclusive`: `59.1% → 59.1%` (unchanged)
- `CU_LANE_BUT_PLAY_MISS`: `17.6% → 17.6%` (unchanged)
- `pack_box_hit`: `21.2% → 18.7%` (regresses)

Decision: **reject / not promoted**.
- Fails the Jan precheck rule (strict regresses and no conversion metric improves).
- Per fail-fast discipline, **OOS/holdouts were not run** for this lever.

