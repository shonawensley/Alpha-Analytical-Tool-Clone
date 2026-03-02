# v0.3 Bottleneck Dashboard (tool_only, stable10, B36)

Purpose: a plain-English, numbers-first answer to:
> “Are we failing because tools don’t see wins — or because selection loses them?”

This page only summarizes **existing** truth-layer reports (no new runs).

## Key definitions (minimal)

- **Strict hit (B36)** here means: `hit_any = 1` on the Play Card (either `straight_hit` OR `box_hit`).
- **Lane retained** means: `vtrac_index_hit = 1` on the Play Card (B36 touched the winner’s VTRAC index at least once).
- **Strict given lane retained** means: among outcomes where we touched the correct lane, how often we still got a strict hit.

Receipts for the full definitions:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__STRICT_MISS_ANATOMY__tool_only__stable10__B36.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__STRICT_MISS_ANATOMY__tool_only__stable10__B36.md`

## Main windows (baseline strategy)

Baseline strategy:
`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first`

| Window | Outcomes | Strict hits | Lane retained | P(lane retained) | P(strict \| lane retained) | Strict-miss: lane dropped | Strict-miss: lane retained |
|---|---:|---:|---:|---:|---:|---:|---:|
| OOS (`2026-01-01..2026-01-09`) | 245 | 10 | 130 | 53.1% | 7.7% | 48.9% (115) | 51.1% (120) |
| Jan (`2026-01-15..2026-01-22`) | 193 | 9 | 114 | 59.1% | 7.9% | 42.9% (79) | 57.1% (105) |

Where the numbers come from:
- OOS: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__STRICT_MISS_ANATOMY__tool_only__stable10__B36.md`
- Jan: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__STRICT_MISS_ANATOMY__tool_only__stable10__B36.md`

## What this means (the bottleneck in one paragraph)

Even before we worry about “which canonical inside the lane”, the system only *touches the correct lane* about **~53–59%** of the time at B36. Once it *does* touch the lane, strict conversion is still only **~8%**. So the miss mass is split:

- ~**43–49%** of strict misses are **lane drops** (we never bought the correct lane at all).
- ~**51–57%** of strict misses are **within-lane misses** (we touched the lane but didn’t buy the winning member/permutation).

That’s why you keep seeing the same story in different language: **recall exists upstream, but fixed-budget conversion is lossy**.

## The fastest way to act on this (no code required)

Pick one case from each bucket:
- **Lane drop**: `C035` in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MASTER_EVIDENCE_EXTRACTION__WINS.md`
- **Lane retained but shallow**: `C036` in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MASTER_EVIDENCE_EXTRACTION__WINS.md`
- **Conversion improved (BASE→dc1)**: `C031` in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MASTER_EVIDENCE_EXTRACTION__WINS.md`

Then open their receipts (MV report + Winners HTML/JSON + predictive CU + predictive play card + results) and confirm:
- Did the winner lane exist in CU with meaningful support?
- Did B36 allocate 0 lines to it (lane drop)?
- If B36 allocated 1 line, did we miss because depth was too shallow?
