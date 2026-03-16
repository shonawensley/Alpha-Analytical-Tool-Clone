# DR Promotion Batch 3

Date: `2026-03-15`

## Change Tested

Tested a bounded predictive-side reranker built on top of `dr_vtrac_cluster_strength`:

- `dr_vtrac_promotion_candidates`

Purpose:
- reward cross-surface agreement inside the same `VTRAC` neighborhood
- give extra weight to current corridor agreement and concentrated family structure
- measure whether a lightweight reranker could outperform raw cluster ordering on the frozen gold-day audits

## Result

It did **not** earn a permanent place in the predictive schema.

### Top-3 winner VTRAC rank

Development matched rows:
- cluster: `22 / 244`
- promotion candidates: `20 / 244`

Holdout matched rows:
- cluster: `9 / 110`
- promotion candidates: `9 / 110`

### Top-5 winner VTRAC rank

Development matched rows:
- cluster: `36 / 244`
- promotion candidates: `36 / 244`

Holdout matched rows:
- cluster: `13 / 110`
- promotion candidates: `14 / 110`

### Unique lifts

Top-3:
- `2026-01-04 / NewJersey4 / Midday / 275` moved from rank `4` to rank `3`

Top-5:
- `2026-01-07 / Virginia4 / Evening / 990` moved from rank `6` to rank `5`

## Interpretation

The reranker was too marginal.

What it did well:
- rescued one extra development row into the union `top-3`
- rescued one extra holdout row into `top-5`

Why it was not kept:
- it did **not** improve aggregate `top-3` promotion
- it added another top-level predictive surface without enough lift to justify the extra schema weight
- the better-performing bounded keeper is still `dr_vtrac_cluster_strength`

## Decision

`dr_vtrac_promotion_candidates` was tested and then removed from the predictive writer.

The right next move is **not** more generic reranking.
The right next move is:

1. richer permutation-family support inside the already-correct `VTRAC` neighborhood
2. promotion weighting tied to assigned-box / corridor truth, not just another index-level reorder
3. continued use of the same frozen dev + holdout gold-day audits as the gate
