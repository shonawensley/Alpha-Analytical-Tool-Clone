# Morning Brief — Spinecap6 “Display Canon Ranked” Spine Chooser (B36 • stable10 • tool_only) — 2026-02-15

Purpose: test a **single** within-lane lever on top of the promoted `spinecap6` geometry:

- Keep: `tool_only` + `stable10` + **B36-only**
- No analyzer edits (selection-layer only)
- Baseline remains: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`

## What changed (single lever family)

Added one experimental B36 strategy variant that changes **how the 6 spine lines per index are chosen** while staying **display-only**:

- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_canon_ranked`
  - still uses VTRAC display members, but **ranks them by canonical/permutation evidence** (best convergence among any lane evidence row sharing that canonical), then takes the top 6.

Rationale: `...spine_display_ranked` often “no-ops” because evidence rows rarely match the *exact* display tokens; canonical-aware ranking should be a stronger (still deterministic) link between evidence and display.

## Decision

No promotion. Keep `...spinecap6` as the B36 default.

Reason: no measurable improvement vs baseline in the current Jan + OOS windows, and the canonical-aware ranking does **not** reduce the display-ranked no-op rate.

## The four numbers (baseline vs variants)

Baseline = `...spinecap6`

Jan window (2026-01-15..01-22):
- strict `hit_any`: baseline **5.2%**
  - `spine_display_ranked`: **5.2%** (no change)
  - `spine_display_canon_ranked`: **5.2%** (no change)
- `hit_any_inclusive`: baseline **49.7%**
  - both variants: **49.7%** (no change)

OOS window (2026-01-01..01-09):
- strict `hit_any`: baseline **4.1%**
  - both variants: **4.1%** (no change)
- `hit_any_inclusive`: baseline **44.9%**
  - both variants: **44.9%** (no change)

## Geometry / invariants check (what it *actually* changed)

All invariants held:
- spine cap violations: **0**
- spine display share: **1.0** (pure display; no evidence injection)

No-op rate vs baseline (`...spinecap6`) from the geometry invariants report:
- Jan:
  - `spine_display_ranked`: **0.5337**
  - `spine_display_canon_ranked`: **0.6891** (changes fewer lines than display_ranked)
- OOS:
  - `spine_display_ranked`: **0.6122**
  - `spine_display_canon_ranked`: **0.8898** (mostly a no-op)

Interpretation: this lever is dominated by the shape of `VTRAC_DISPLAY` itself (many indices have ≤6 display members, so a 6-line spine cap can’t meaningfully change membership), and canonical-aware ranking still tends to preserve the baseline membership set.

## Key artifacts

Scoreboards (Jan + OOS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md:1`

Geometry invariants (cap + display share + no-op detection):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md:1`

Winner lane rank sweep (lane ranking vs retention sanity):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md:1`

Lane allocation (breadth/depth sanity; one file per strategy label):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_BASE.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_DISPRANK.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_CANONRANK.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_BASE.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_DISPRANK.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_CANONRANK.md:1`

