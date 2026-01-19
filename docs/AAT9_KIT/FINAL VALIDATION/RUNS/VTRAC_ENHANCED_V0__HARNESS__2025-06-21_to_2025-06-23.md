# VTRAC Enhanced Harness — 2025-06-21_to_2025-06-23

This is a reporting-only harness. It measures VTRAC Enhanced as a straight caller and as an index gateway lens.

Winner type handling:
- `unique` and `double` are included for index metrics.
- `triple` has `winner_index_missing=1` by design (legacy behavior: no vtrac_index for triples).

## ALL (winner present)

- opportunities: `81` (missing enhanced JSON: `0`)

| top_n | straight_hit | canonical_hit (BOX-eq) | index_hit_via_top_straights | index_in_top5_indices_ranked |
|---:|---:|---:|---:|---:|
| 8 | 0 (0.0000) | 4 (0.0494) | 11 (0.1358) | 13 (0.1605) |
| 12 | 0 (0.0000) | 4 (0.0494) | 15 (0.1852) | 13 (0.1605) |
| 20 | 0 (0.0000) | 6 (0.0741) | 21 (0.2593) | 13 (0.1605) |

## UNIQUE

- opportunities: `59` (missing enhanced JSON: `0`)

| top_n | straight_hit | canonical_hit (BOX-eq) | index_hit_via_top_straights | index_in_top5_indices_ranked |
|---:|---:|---:|---:|---:|
| 8 | 0 (0.0000) | 4 (0.0678) | 10 (0.1695) | 9 (0.1525) |
| 12 | 0 (0.0000) | 4 (0.0678) | 13 (0.2203) | 9 (0.1525) |
| 20 | 0 (0.0000) | 6 (0.1017) | 17 (0.2881) | 9 (0.1525) |

## DOUBLE

- opportunities: `22` (missing enhanced JSON: `0`)

| top_n | straight_hit | canonical_hit (BOX-eq) | index_hit_via_top_straights | index_in_top5_indices_ranked |
|---:|---:|---:|---:|---:|
| 8 | 0 (0.0000) | 0 (0.0000) | 1 (0.0455) | 4 (0.1818) |
| 12 | 0 (0.0000) | 0 (0.0000) | 2 (0.0909) | 4 (0.1818) |
| 20 | 0 (0.0000) | 0 (0.0000) | 4 (0.1818) | 4 (0.1818) |
