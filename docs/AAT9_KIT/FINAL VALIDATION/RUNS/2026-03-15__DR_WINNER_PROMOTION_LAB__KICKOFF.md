# DR Winner Promotion Lab Kickoff

Date: `2026-03-15`

## Purpose

Capture the first result after widening the winner-aware DR audit from a `top10`-style view to a broader audit-only `top20` view.

This is an instrumentation change only.

The live predictive DR writer is unchanged.

## Key Finding

The previous promotion-gap framing was directionally right, but it was still too coarse.

The remaining misses split into 2 groups:

1. **visible but under-promoted**
   - the winner lane already appears in the broader audit view
   - it is just losing badly to a compact attractor family

2. **truly buried**
   - the winner lane is not visible even in the broader audit view
   - these rows need stronger lane-isolation logic, not just a lighter top-band rerank

## Broadened Audit Read

Matched rows:

- DEV: `244`
- HOLDOUT: `110`

Cluster winner-lane visibility:

- DEV
  - `top3`: `21`
  - `top5`: `34`
  - `top8`: `50`
  - `top10`: `55`
  - `top20`: `64`

- HOLDOUT
  - `top3`: `9`
  - `top5`: `13`
  - `top8`: `21`
  - `top10`: `21`
  - `top20`: `23`

Best-surface winner-lane visibility:

- DEV
  - `top3`: `27`
  - `top5`: `40`
  - `top8`: `52`
  - `top10`: `57`
  - `top20`: `64`

- HOLDOUT
  - `top3`: `12`
  - `top5`: `18`
  - `top8`: `28`
  - `top10`: `29`
  - `top20`: `30`

## Meaning

This does **not** say the promotion problem was fake.

It says the problem is more specific:

- some winner lanes are already being isolated, but too low
- others are still getting buried entirely

So the next batch should not treat every miss the same.

## Immediate Implication

The next winner-artifact comparison pass should explicitly compare:

1. visible under-promoted anchors
2. fully buried anchors
3. successful promoted anchors

Then ask:

- what trait differences separate those groups?
- which traits deserve scoring changes?
- which rows only need better promotion of already-visible lanes?
- which rows need stronger cross-box / cross-variant lane isolation?
