# VTRAC Enhanced Harness — 2025-12-30_to_2026-01-04

This is a reporting-only harness. It measures VTRAC Enhanced as a straight caller and as an index gateway lens.

Winner type handling:
- `unique` and `double` are included for index metrics.
- `triple` has `winner_index_missing=1` by design (legacy behavior: no vtrac_index for triples).

## ALL (winner present)

- opportunities: `163` (missing enhanced JSON: `0`)

| top_n | straight_hit | canonical_hit (BOX-eq) | index_hit_via_top_straights | index_in_top5_indices_ranked |
|---:|---:|---:|---:|---:|
| 8 | 2 (0.0123) | 6 (0.0368) | 20 (0.1227) | 24 (0.1472) |
| 12 | 3 (0.0184) | 8 (0.0491) | 27 (0.1656) | 24 (0.1472) |
| 20 | 3 (0.0184) | 11 (0.0675) | 39 (0.2393) | 24 (0.1472) |

## UNIQUE

- opportunities: `121` (missing enhanced JSON: `0`)

| top_n | straight_hit | canonical_hit (BOX-eq) | index_hit_via_top_straights | index_in_top5_indices_ranked |
|---:|---:|---:|---:|---:|
| 8 | 2 (0.0165) | 6 (0.0496) | 18 (0.1488) | 15 (0.1240) |
| 12 | 3 (0.0248) | 8 (0.0661) | 22 (0.1818) | 15 (0.1240) |
| 20 | 3 (0.0248) | 11 (0.0909) | 32 (0.2645) | 15 (0.1240) |

## DOUBLE

- opportunities: `41` (missing enhanced JSON: `0`)

| top_n | straight_hit | canonical_hit (BOX-eq) | index_hit_via_top_straights | index_in_top5_indices_ranked |
|---:|---:|---:|---:|---:|
| 8 | 0 (0.0000) | 0 (0.0000) | 2 (0.0488) | 9 (0.2195) |
| 12 | 0 (0.0000) | 0 (0.0000) | 5 (0.1220) | 9 (0.2195) |
| 20 | 0 (0.0000) | 0 (0.0000) | 7 (0.1707) | 9 (0.2195) |

## TRIPLE

- opportunities: `1` (missing enhanced JSON: `0`)

| top_n | straight_hit | canonical_hit (BOX-eq) | index_hit_via_top_straights | index_in_top5_indices_ranked |
|---:|---:|---:|---:|---:|
| 8 | 0 (0.0000) | 0 (0.0000) | 0 (0.0000) | 0 (0.0000) |
| 12 | 0 (0.0000) | 0 (0.0000) | 0 (0.0000) | 0 (0.0000) |
| 20 | 0 (0.0000) | 0 (0.0000) | 0 (0.0000) | 0 (0.0000) |
