# Morning Brief — Split Chooser + Tail Rank5 Depth2 Precheck (B36, stable10) — 2026-02-18

Goal (selection-layer only; isolation-first with strict guardrails):
- Test a **micro shoulder-depth** lever: buy 1 extra line of depth in the highest-ranked tail lane (rank 5)
  while keeping taper6644 spine geometry fixed.
- Fail fast if Jan precheck regresses inclusive or does not improve strict conversion.

## Baseline verification (SSOT)

Baseline strategy (current default) was read from:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md:73`

Baseline:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`

## Lever under test

Candidate (single lever: **tail depth schedule** only):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_rank5_depth2`
- Meaning: keep split chooser (`spine=methods_first`, `tail=score_total_first`) and taper6644 geometry, but allocate 2 tail lines to the first tail index (rank 5) when possible (dropping the lowest-ranked tail lane under fixed B36).

Locked invariants:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: `B36`
- Geometry: `taper6644` + `spinecap6`
- Scope: selection-layer only (no analyzer edits)

## Precheck 1: geometry / “is the lever real?” (Jan roster)

Geometry report:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAPER6644_TAIL_RANK5_DEPTH2_PRECHECK.md`

Key results (rows=193):
- Candidate `no_op_rate`: `0.0` (active; always changes at least 1 line)
- `indices_touched_count` mean: `20.321 → 19.332` (expected breadth loss from buying 1 extra tail line)
- Cap/taper violations: `0`

## Precheck 2: Jan scoreboard (stop/continue)

Scoreboard:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6644_TAIL_RANK5_DEPTH2_PRECHECK.md`

Results (rows=193):
- strict `hit_any`: `4.7% → 4.7%` (unchanged)
- `hit_any_inclusive`: `59.1% → 58.5%` (regresses)
- `CU_LANE_BUT_PLAY_MISS`: `17.6% → 17.6%` (unchanged)
- `CU_EXACT_BUT_PLAY_MISS`: `2.1% → 2.6%` (worsens)

Strict miss anatomy (Jan; conditional conversion check):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__STRICT_MISS_ANATOMY__tool_only__stable10__B36__TAPER6644_TAIL_RANK5_DEPTH2_PRECHECK.md`
- `strict_given_lane_retained`: `7.9% → 8.0%` (tiny; not enough to offset breadth loss)

Decision: **reject / not promoted**.
- This lever buys depth at the cost of lane breadth; in this window it does not improve strict and it regresses inclusive.
- Per fail-fast discipline, **OOS/holdouts were not run** for this lever.

