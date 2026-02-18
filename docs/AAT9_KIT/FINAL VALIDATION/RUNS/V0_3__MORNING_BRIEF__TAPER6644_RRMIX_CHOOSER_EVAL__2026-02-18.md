# Morning Brief — Taper6644 Round‑Robin Mix Chooser Eval — 2026‑02‑18

Goal: run one **scoreboard-moving** selection-layer lever (index set changes) under locked posture, but stop early if it fails Jan gates.

## Invariants (locked)

- Profile: `tool_only`
- Candidate Universe posture: `stable10`
- Budget: `B36` only
- Scope: selection-layer only (no analyzer edits)
- Objective: isolation-first (improve `hit_any_inclusive` / reduce `CU_LANE_BUT_PLAY_MISS`)
- Guardrails: do not regress strict/inclusive in OOS (not reached in this eval because Jan precheck failed)

## Baseline (current default)

- Strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first`
- Geometry: `taper6644` + `spinecap6` (spine ranks 1–4 spend 6/6/4/4 lines; tail fills breadth)

## Candidate (one lever)

- Strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_rrmix_methods_packs_score_total`
- Lever: **deterministic round‑robin index ranking mix** (methods_first / packs_first / score_total_first), with backstop fill.
- Geometry unchanged: still `taper6644` + `spinecap6`, spine pick mode remains `display`.

## Precheck 1: “Is the lever actually moving index ordering?” (Jan geometry)

This replaces the prior “near-no-op” burn: prove the candidate materially changes the Play Card before running multi-window grading.

- Geometry report:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__RRMIX_PRECHECK.md`
- Key results (Jan roster; rows=193):
  - Candidate `no_op_rate`: `0.0622` (active; not a near-no-op)
  - Candidate `diff_new_lines` mean/p90: `5.865` / `10.0`
  - Index-level movement (paired-row analysis):
    - spine indices changed in `~96.9%` of outcomes
    - indices_touched_count changed in `~11.4%` of outcomes

Decision: **passes** precheck (lever is real).

## Precheck 2: Jan scoreboard (stop if it can’t be promoted)

Scoreboard (B36 only; baseline vs candidate):

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__RRMIX_PRECHECK.md`

Results (rows=193):

- `hit_any_inclusive`: `58.0% → 58.0%` (no lift)
- `CU_LANE_BUT_PLAY_MISS`: `18.1% → 19.2%` (worse)
- `CU_EXACT_BUT_PLAY_MISS`: `2.6% → 1.6%` (better)
- `hit_any` (strict): `4.7% → 2.6%` (worse)

Decision: **reject / not promoted** (fails isolation-first direction + strict regresses).

## Next step (recommended)

Move to the next single-lever candidate that *changes the touched lane set* but is more targeted than “full spine replacement”:

- Tail-only diversification (keep spine indices by `score_total_first`, diversify tail ranking list beyond a single lens), OR
- Scan-limit/horizon lever for ranked indices (if evidence rows are too shallow), OR
- A curated “diverse chooser” that increases unique lane recall without reshuffling the top-4 spine every time.

