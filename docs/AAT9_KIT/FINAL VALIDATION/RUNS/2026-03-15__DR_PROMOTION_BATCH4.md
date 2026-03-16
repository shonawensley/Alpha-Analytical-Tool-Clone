# DR Promotion Batch 4

Date: `2026-03-15`

## Change Tested

Tested a bounded predictive-side family/permutation surface inside the already-correct `VTRAC` neighborhood:

- `dr_vtrac_permutation_support`

Purpose:
- reward concentrated family neighborhoods inside a `VTRAC` lane
- preserve multiple supporting permutations for the same family
- measure whether family/permutation concentration would outperform the simpler `dr_vtrac_cluster_strength` surface on the frozen gold-day audits

## Result

It did **not** outperform the cluster surface and was removed.

### Top-3 winner VTRAC rank

Development matched rows:
- cluster: `22 / 244`
- permutation support: `20 / 244`

Holdout matched rows:
- cluster: `9 / 110`
- permutation support: `9 / 110`

### Top-5 winner VTRAC rank

Development matched rows:
- cluster: `36 / 244`
- permutation support: `33 / 244`

Holdout matched rows:
- cluster: `13 / 110`
- permutation support: `11 / 110`

### Identifiable winner-lane ranks

Development matched rows:
- cluster: `55`
- permutation support: `51`

Holdout matched rows:
- cluster: `21`
- permutation support: `19`

## Interpretation

The family/permutation idea was directionally valid, but this implementation was not strong enough.

What it showed:
- index-only cluster scoring is already capturing more of the useful signal than this family/permutation surface
- family/permutation support should probably be used as a component inside future promotion weighting, not as another standalone predictive-side top surface

Why it was removed:
- weaker than cluster on development and holdout
- no aggregate `top-3` improvement
- no holdout `top-5` improvement
- not worth the extra schema weight

## Decision

`dr_vtrac_permutation_support` was tested and removed.

The next DR batch should not be another standalone family-only surface.
The better direction is:

1. keep `dr_vtrac_cluster_strength` as the strongest bounded promotion keeper
2. use family/permutation support only as an internal ingredient in future cluster/promotion weighting
3. focus the next change on assigned-box / corridor truth bridging into the already-correct `VTRAC` neighborhood
