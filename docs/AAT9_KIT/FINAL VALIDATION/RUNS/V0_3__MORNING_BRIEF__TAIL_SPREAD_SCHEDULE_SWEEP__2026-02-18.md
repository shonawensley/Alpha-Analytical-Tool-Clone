# Morning Brief — Tail Spread Schedule Sweep (B36, stable10) — 2026-02-18

Goal (selection-layer only; isolation-first):
- Test whether **micro-tuning the tail spread schedule** can beat the promoted baseline under locked invariants.

Why this lever class (quick justification):
- Winner-lane ranks are **shoulder-heavy** under `score_total_first` evidence ranking:
  - Jan (lane_present only): p50≈`12`, p75≈`21`, p90≈`24`, p95≈`26`
  - OOS (lane_present only): p50≈`13`, p75≈`21`, p90≈`25`, p95≈`26`
- The promoted baseline (`top14 + inject pos18/22`) is a controlled way to “buy shoulder coverage” without buying depth.
- This sweep asks: *is there a better shoulder schedule than (18,22) under the same geometry?*

## Locked invariants

- profile: `tool_only`
- experiment_tag: `stable10`
- budget: `B36` only (for decision metrics)
- analyzers/CU posture: unchanged (selection-layer only)
- geometry: `spinecap6` + `taper6644` (6/6/4/4 spine; 1-line/index tail)
- chooser: split indices (spine=`methods_first`, tail=`score_total_first`)

Baseline strategy (current default):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22`

## Candidates tested (single lever: schedule only)

All candidates keep the exact same invariants and change only `(keep_top, inject_positions)`:

- `..._tail_spread_top12_pos16_20` (keep top12; inject pos16/20)
- `..._tail_spread_top14_pos16_20` (keep top14; inject pos16/20)
- `..._tail_spread_top14_pos18_24` (keep top14; inject pos18/24)
- `..._tail_spread_top14_pos20_26` (keep top14; inject pos20/26)
- `..._tail_spread_top16_pos18_24` (keep top16; inject pos18/24)

## Jan precheck (fail-fast sweep)

Scoreboard (baseline + all candidates; B36-only):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAIL_SPREAD_SCHEDULE_SWEEP.md`

Result (decision):
- **No candidate beats the promoted baseline** on `hit_any_inclusive` or `CU_LANE_BUT_PLAY_MISS`.
- Baseline remains best:
  - `hit_any_inclusive`: **62.2%** (highest in sweep)
  - `CU_LANE_BUT_PLAY_MISS`: **15.0%** (tied-best)
  - `CU_EXACT_BUT_PLAY_MISS`: **1.6%** (tied-best)
  - strict `hit_any`: **4.7%** (unchanged across sweep)

Decision:
- ✅ Keep current default (`top14 + inject pos18/22`)
- ❌ Reject all schedule variants (do not proceed to OOS/holdouts; fail-fast triggered)

## Geometry / no-op / invariants (safety receipts)

Proves the sweep was “real” (not a no-op) and respects caps/taper:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAIL_SPREAD_SCHEDULE_SWEEP_JAN.md`

Highlights:
- `no_op_rate` is low for all candidates (lever is active).
- cap/taper violations: `0` for all candidates.

## Next lever recommendation (what’s most likely to move scoreboards now)

This sweep suggests the tail-spread schedule is **near-saturated** under current invariants.

Next highest-EV levers should change *which indices* enter the touched-set (not just the schedule),
while keeping posture/geometry locked, e.g.:
- “diverse chooser” for tail indices (multi-lens inclusion) to widen shoulder coverage beyond what `score_total_first` alone supplies, or
- a within-lane “smart 1–2 lines” representative chooser that improves strict conversion **without** buying depth.

