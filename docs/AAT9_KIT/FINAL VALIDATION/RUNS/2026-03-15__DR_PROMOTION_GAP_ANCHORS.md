# DR Promotion Gap Anchors

Date: `2026-03-15`

## Purpose

After the bounded `cluster`, `reranker`, `family/permutation`, and `assigned-box bridge` batches, the right next step is not another blind promotion experiment.

This memo isolates the strongest remaining missed rows on the frozen gold-day audits:

- `winner_json_status = matched_literal`
- `vtrac_any > 0`
- `cluster_winner_vtrac_rank > 5` or not rankable

These are the rows where:
- DR is visibly alive on the winner lane
- the winners tables show strong assigned-box signal
- but the current promotion surfaces still do not elevate that lane enough

## Headline Pattern

The strongest missed rows are still dominated by a small set of compact attractors:

Development anchor leaders:
- top trace families: `559`, `259`, `599`, `299`, `229`, `255`
- top corridor families: `559`, `259`, `599`, `299`, `255`, `229`
- top double patterns: `559`, `592`, `599`, `552`, `992`, `922`

Holdout anchor leaders:
- top trace families: `559`, `259`, `599`, `445`, `299`, `255`, `229`
- top corridor families: `559`, `259`, `599`, `445`, `299`, `255`, `229`
- top double patterns: `559`, `592`, `599`, `992`, `544`, `922`, `552`

This is the clearest repeated gap pattern so far:

**strong assigned-box winner corridors are still being buried under compact attractor families like `559`, `259`, `299`, `229`, `445`, and their double-pattern shoulders.**

## Anchor Counts

Development rows meeting the gap condition:
- `181`

Holdout rows meeting the gap condition:
- `83`

Alignment mix inside those anchors:

Development:
- `vtrac_capture`: `106`
- `literal_capture`: `75`

Holdout:
- `vtrac_capture`: `52`
- `literal_capture`: `31`

This matters because the problem is not only “true misses.”
Many rows are already structurally alive enough to register as `literal_capture` or `vtrac_capture`, but the top predictive promotion surfaces still do not rank the correct lane strongly enough.

## Representative Development Anchors

- `2026-01-04 / Indiana4 / Midday / 813 / VT 23`
  - winner tables extremely strong
  - cluster not rankable
  - dominant attractor family: `259`

- `2025-12-31 / Virginia4 / Evening / 636 / VT 18`
  - winner tables extremely strong
  - cluster not rankable
  - dominant attractor family: `299`

- `2026-01-01 / Delaware4 / Midday / 149 / VT 25`
  - winner tables extremely strong
  - cluster rank `8`
  - dominant attractor family: `499`

- `2026-01-01 / NorthCarolina4 / Evening / 053 / VT 4`
  - winner tables extremely strong
  - cluster rank `9`
  - dominant attractor family: `055`

- `2025-06-23 / Connecticut4 / Evening / 938 / VT 33`
  - winner tables strong
  - cluster not rankable
  - dominant attractor family: `445`

## Representative Holdout Anchors

- `2026-01-06 / Michigan4 / Midday / 618 / VT 18`
  - winner tables extremely strong
  - cluster not rankable
  - dominant attractor family: `449`

- `2026-01-07 / Florida4 / Midday / 434 / VT 34`
  - winner tables very strong
  - cluster rank `8`
  - dominant attractor family: `259`

- `2026-01-09 / Pennsylvania4 / Midday / 811 / VT 18`
  - winner tables very strong
  - cluster not rankable
  - dominant attractor family: `559`

- `2026-01-09 / NorthCarolina4 / Evening / 960 / VT 9`
  - winner tables strong
  - cluster not rankable
  - dominant attractor family: `229`

- `2026-01-09 / NewJersey4 / Evening / 028 / VT 11`
  - winner tables strong
  - cluster rank `9`
  - dominant attractor family: `055`

## Interpretation

The current DR promotion gap is now clearer:

1. The issue is not that DR cannot see the winner lane.
2. The issue is not that the assigned-box corridor is absent.
3. The issue is that compact attractor families keep stealing the visible top surfaces even when:
   - winner-table assigned-box signal is strong
   - DR already has `vtrac_any`
   - the eventual lane is structurally alive

So the next coding batch should target:

- **compact attractor suppression**
- specifically in rows where assigned-box/corridor evidence is historically strong

## Recommended Next Batch

Do not add another standalone predictive surface first.

Instead, test one bounded change to the existing cluster/gateway promotion logic:

1. identify over-dominant attractor families (`559`, `259`, `299`, `229`, `445`, related doubles)
2. reduce their promotion advantage when:
   - corridor signal is broad but family-asymmetric
   - assigned-box-style corridor traits are strong
   - the same attractor keeps winning without enough cross-surface support
3. re-run the same frozen dev + holdout audits

This is the strongest evidence-backed next move after the failed rerank and family-only experiments.
