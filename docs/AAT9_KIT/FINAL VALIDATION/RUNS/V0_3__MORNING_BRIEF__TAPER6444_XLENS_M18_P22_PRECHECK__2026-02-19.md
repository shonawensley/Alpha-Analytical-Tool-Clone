# Morning Brief — Taper6444 Geometry Width (XLens m18+p22) Precheck (B36, stable10) — 2026-02-19

Status: **exploratory / out-of-invariants** (not promotable under current Crossroads SSOT).

Why this exists:
- We hit diminishing returns on “touched-set micro-tuning” under locked `taper6644`.
- This precheck explores what happens if we *buy breadth* by reducing spine depth.

Important constraint (SSOT):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md:118` locks geometry to `taper6644` in this phase.
- Therefore: this lever is recorded for insight only; OOS/holdouts gates are intentionally not run.

## Baseline (current default; in-invariants)

- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

## Candidate (out-of-invariants lever: geometry width)

- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6__taper6444__xlens_m18_p22`

Meaning:
- Keep the promoted tail touched-set policy (methods@18 + packs@22),
- Change only spine taper from `6/6/4/4` → `6/4/4/4`, freeing **2 lines** to add **2 extra tail lanes** (breadth).

## Jan window (in-sample) — precheck

Scoreboard:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6444_XLENS_M18_P22_PRECHECK.md`

Key deltas (rows=193):
- `hit_any_inclusive`: `63.7% → 66.8%` (**+3.1pp**)
- `CU_LANE_BUT_PLAY_MISS`: `13.5% → 10.4%` (**-3.1pp**)
- strict `hit_any`: `4.7% → 4.1%` (**-0.6pp**)

Geometry receipts:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAPER6444_XLENS_M18_P22_PRECHECK_JAN.md`
  - `indices_touched_count` mean: `20.321 → 22.228` (expected breadth gain)
  - Note: small `spine_cap/taper` violations appear in the *total* view (top-up spillover), even though pack-level caps are respected.

Decision (for now):
- ❌ Not promotable under current Crossroads policy (geometry invariant violated).
- ✅ Valuable evidence: breadth buys isolation (inclusive up / lane-drop down), but it risks strict conversion and can introduce cap/taper spillover via top-up.

If/when we unlock geometry as a new phase:
- Re-run full gates (Jan + OOS + HoldoutA/B) and enforce “no violations” by tightening top-up behavior, or by using a less aggressive taper change (e.g., `6/5/4/4`).

