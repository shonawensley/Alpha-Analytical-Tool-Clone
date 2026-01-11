# Testing Competition Analysis — 2026-01-06 (H=2026-01-05 → D=2026-01-06)

Purpose: capture what happened in the time-boxed “prediction competition” (fast, pre-results) and what we can learn from it without over-reading the outcome.

This is **not** a Master Validation run report; it’s an “intermission” evaluation of quick-turn picks made under time pressure using partial artifacts (VTRAC enhanced CLI + spot checks), then graded against the posted evening results.

## Inputs (SSOT)

- Competition log: `tasks/challenge_codex.txt`
- Challenge results scratchpad: `tasks/results_challenge.txt`
- Official results (grading): `data/results/2026-01-06.txt`
- VTRAC reference: `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`
- Partial “competition” sharepack (archived, not SSOT): `sharepacks/_scratch/2026-01-06__competition_20260107_051853/`

## Scorecard (Evening results, boxed-first lens)

Legend:
- **BoxHit**: winner’s canonical (sorted digits) is present in the suggested box list.
- **VTRACHit**: at least one suggested box is in the **same VTRAC index family** as the winner (lane hit, but not exact box).

| State | Evening Winner | Canon | VTRAC idx | BoxHit | VTRACHit | Notes |
|---|---:|---:|---:|---:|---:|---|
| Connecticut4 | 737 | 377 | 27 | ❌ | ❌ | Suggested boxes were from other lanes; no lane/box overlap. |
| OntarioCanada4 | 433 | 334 | 33 | ❌ | ❌ | Missed both exact box and winner’s VTRAC family. |
| Virginia4 | 958 | 589 | 14 | ❌ | ✅ | Winner family hit (index 14) via suggested 089; shows “lane correct, box miss”. |
| NewJersey4 | 942 | 249 | 31 | ✅ | ✅ | Box hit via tier-2 “double-pressure index picks” including 249 (covers 942 boxed). |
| NorthCarolina4 | 298 | 289 | 30 | ❌ | ❌ | Suggested cluster emphasized idx12/idx9; winner landed idx30. |
| NewYork4 | 342 | 234 | 30 | ❌ | ✅ | Lane hit (idx30) via suggested 248; exact box missed. |
| Florida4 | 160 | 016 | 6 | ❌ | ❌ | No overlap with the suggested lane closures/double hedges. |
| Indiana4 | 961 | 169 | 19 | ❌ | ❌ | No overlap with the suggested lane closures. |

## What this suggests (without overfitting)

1) **A “VTRAC family hit” happened even when box didn’t** (NY + VA).
   - This supports your intuition that sometimes we’re “right about the rail” but miss the exact canonical.
   - It also argues for a future **pack-builder closure rule** (“if you’re playing an index, include a bounded closure subset”) — but that’s a Fix‑Later tuning item, not something to change during pipeline hardening.

2) **The only boxed hit (NJ) came from the “double-pressure index” tier**, not the first-pass straight list.
   - This matches the mental model: doubles/mirror dynamics can be “more reliable” than trying to snipe a single straight.

3) **The competition method was intentionally constrained** (fast, not full workflow).
   - The choices were based on:
     - the most recent draw digits (digit-pool / mirror complements),
     - VTRAC enhanced CLI top lanes,
     - quick Aux overlap checks.
   - It did **not** consume the full SSOT day snapshot (tables + all tools + full sharepack freeze), so this outcome should not be used to judge tool quality.

## Concrete follow-ups (safe)

- Use this competition as a reference case when designing a future **predictive “portfolio brief”**:
  - keep boxed-first tiering,
  - track “lane hit” separately from “box hit”,
  - and explicitly log “closure size” (how many lane members were covered).
- Do not modify analyzers based on this single day.
- When we build the full gold day for `D=2026-01-06` properly, re-check whether the template-driven packs (post-results reverse engineering) would have included:
  - NJ boxed hit (likely yes),
  - NY/VA lane hits (and whether a bounded index-closure would have converted them into box hits).

