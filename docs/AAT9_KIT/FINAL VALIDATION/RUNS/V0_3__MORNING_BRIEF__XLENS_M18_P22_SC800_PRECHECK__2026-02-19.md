# Morning Brief — XLens m18+p22 Scan‑Depth (sc800) Precheck (B36, stable10) — 2026-02-19

Goal (selection-layer only; isolation-first with strict guardrails):
- Test whether increasing the **index-ranking horizon** (`scan_limit`) can unlock additional shoulder lanes (reduce lane drops) under the current promoted baseline policy.

Locked invariants:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: `B36` only
- Scope: selection-layer only (no analyzer edits)
- Geometry: `taper6644` + `spinecap6` (spine 6/6/4/4; tail 1-line/index)

## Baseline (current default)

- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

## Candidate (single lever: scan depth only)

Strategy key (short alias to avoid ladder filename-length errors):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644__xlens_m18_p22_sc800`

Meaning:
- Same policy as the promoted baseline, but with `scan_limit=800` when ranking/selecting indices.

## Jan window (in-sample) — precheck

Scoreboard:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__XLENS_M18_P22_SC800_PRECHECK.md`

Result:
- Exact tie vs baseline (no metric movement).

Lever effectiveness (geometry; Jan):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__XLENS_M18_P22_SC800_PRECHECK_JAN.md`
  - `no_op_rate`: `1.0` (full no-op)
  - `diff_new_lines`: `0`

Decision: **reject / abort before OOS**.

Why this is expected (key diagnostic):
- Under stable10, the Candidate Universe union is often smaller than the original `scan_limit=350` horizon (e.g. Ontario 2026-01-15 has `union_combos_count=209`), so increasing scan depth cannot expose additional lanes.

Takeaway / next lever direction:
- “Scan depth” is not a lever under current stable10 CU width.
- Further isolation gains likely require a **posture-width lever** (e.g., stable10→stable15/20) or a **geometry-width lever** (more tail lanes at B36), both of which are larger-stage changes than the current selection-only micro-tuning.

