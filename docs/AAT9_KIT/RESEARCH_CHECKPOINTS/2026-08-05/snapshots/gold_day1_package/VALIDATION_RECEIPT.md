# 2026-03-09 Deep Review Package Validation Receipt

## Result

`PASS`

## Structural Checks

| Check | Observed | Expected | Status |
| --- | --- | --- | --- |
| State reports | 14 | 14 | PASS |
| AUX state reports | 14 | 14 | PASS |
| Frozen predictive reports embedded | 14 | 14 | PASS |
| Result-aware autopsies embedded | 28 | 28 | PASS |
| Full predictive narratives preserved | 14 | 14 | PASS |
| Full post-result narratives preserved | 28 | 28 | PASS |
| Full AUX pre-result narratives preserved | 14 | 14 | PASS |
| Full AUX post-result joins preserved | 28 | 28 | PASS |
| Winner HTML articles | 28 | 28 | PASS |
| Winner HTML bodies preserved verbatim | 28 | 28 | PASS |
| Winner HTML tables | 196 | 196 | PASS |
| External script/link dependencies | 0 | 0 | PASS |
| Frozen V2 backlog items | 21 | 21 | PASS |
| Source artifacts unchanged | true | true | PASS |

## Zone-Coverage Recalculation

| Relation inside Zone 1 or 2 | Any variant | Target or Combined |
| --- | --- | --- |
| BOXED_VTRAC | 26 | 25 |
| CANONICAL_BOX | 23 | 21 |
| ORDERED_VTRAC | 19 | 19 |
| EXACT_LITERAL | 11 | 11 |

The calculation reads every post-result autopsy's candidate-symmetric secondary scan and requires an occurrence explicitly tagged Zone 1 or Zone 2. It is retrospective availability, not predictive credit.

## Cleaned Draw Source Gate

Validated **42** `data/cleaned/draws/*_draws.csv` files across 14 states and three variants. Row-count distribution: 1000 rows=42 files. These files are validation references only; the package does not recompute analytics from them.

## HTML Preservation

The stacked HTML contains **28** source bodies, **196** source tables, and **4** deduplicated source style blocks. Every article records its original source path and SHA-256.

## Boundary Checks

- Predictive and post-result sections remain visibly separated.
- Full state narratives are preserved rather than replaced by short summaries.
- AUX full pre-result evidence appears once per state; winner joins remain explicitly post-result.
- Large decay negatives are preserved in the source JSON while reports retain route denominators and every qualifying convey row.
- No existing analytical artifact was modified during generation.
- No runtime, template, Analysis Arena, scoring, ranking, or combination-forming code was changed.
