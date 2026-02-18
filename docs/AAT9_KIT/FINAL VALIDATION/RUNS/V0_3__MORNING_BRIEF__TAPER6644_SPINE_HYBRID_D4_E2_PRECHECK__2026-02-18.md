# Morning Brief — Split Chooser + Spine Hybrid d4/e2 Precheck (B36, stable10) — 2026-02-18

Goal (selection-layer only; isolation-first with strict guardrails):
- Test a **within-spine conversion lever** while freezing index selection + geometry.
- Fail fast if Jan precheck regresses strict/inclusive or does not show a conversion win signal.

## Baseline verification (SSOT)

Baseline strategy (current default) was read from:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md:73`

Baseline:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`

## Lever under test

Candidate (single lever: within-spine member choice only):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_spine_hybrid_d4_e2`
- Meaning: keep split chooser (`spine=methods_first`, `tail=score_total_first`) and taper6644 geometry, but set `spine_pick_mode=hybrid_d4_e2`:
  - Anchor with 4 display members (baseline order),
  - then add up to 2 evidence-backed combos inside the lane,
  - then fill remaining capacity with display.

Locked invariants:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: `B36`
- Geometry: `taper6644` + `spinecap6`
- Scope: selection-layer only (no analyzer edits)

## Precheck 1: geometry / “is the lever real?” (Jan roster)

Geometry report:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAPER6644_SPINE_HYBRID_D4_E2_PRECHECK.md`

Key results (rows=193):
- Candidate `no_op_rate`: `0.0` (active)
- Candidate `diff_new_lines` mean/p90: `3.575` / `4.0`
- Candidate `spine_pack_display_share` mean: `0.818` (evidence rows are actually being used)
- Cap/taper violations: `0`

## Precheck 2: Jan scoreboard (stop/continue)

Scoreboard:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6644_SPINE_HYBRID_D4_E2_PRECHECK.md`

Results (rows=193):
- strict `hit_any`: `4.7% → 4.7%` (unchanged)
- `hit_any_inclusive`: `59.1% → 59.1%` (unchanged)
- `CU_LANE_BUT_PLAY_MISS`: `17.6% → 17.6%` (unchanged)
- `CU_EXACT_BUT_PLAY_MISS`: `2.1% → 2.1%` (unchanged)
- `pack_box_hit`: `21.2% → 19.7%` (regresses)

Strict miss anatomy (Jan; lane-drop vs within-lane miss):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__STRICT_MISS_ANATOMY__tool_only__stable10__B36__TAPER6644_SPINE_HYBRID_D4_E2_PRECHECK.md`
- No meaningful change vs baseline.

Decision: **reject / not promoted**.
- The lever is active, but it does not lift any key conversion metrics and it regresses `pack_box_hit`.
- Per fail-fast discipline, **OOS/holdouts were not run** for this lever.

