# VTRAC Enhanced Harness — 2026-01-05_to_2026-01-09

This is a reporting-only harness. It measures VTRAC Enhanced as a straight caller and as an index gateway lens.

Winner type handling:
- `unique` and `double` are included for index metrics.
- `triple` has `winner_index_missing=1` by design (legacy behavior: no vtrac_index for triples).

## ALL (winner present)

- opportunities: `138` (missing enhanced JSON: `0`)

| top_n | straight_hit | canonical_hit (BOX-eq) | index_hit_via_top_straights | index_in_top5_indices_ranked |
|---:|---:|---:|---:|---:|
| 8 | 1 (0.0072) | 2 (0.0145) | 16 (0.1159) | 17 (0.1232) |
| 12 | 1 (0.0072) | 4 (0.0290) | 22 (0.1594) | 17 (0.1232) |
| 20 | 2 (0.0145) | 7 (0.0507) | 28 (0.2029) | 17 (0.1232) |

## UNIQUE

- opportunities: `95` (missing enhanced JSON: `0`)

| top_n | straight_hit | canonical_hit (BOX-eq) | index_hit_via_top_straights | index_in_top5_indices_ranked |
|---:|---:|---:|---:|---:|
| 8 | 1 (0.0105) | 2 (0.0211) | 13 (0.1368) | 12 (0.1263) |
| 12 | 1 (0.0105) | 4 (0.0421) | 18 (0.1895) | 12 (0.1263) |
| 20 | 2 (0.0211) | 7 (0.0737) | 23 (0.2421) | 12 (0.1263) |

## DOUBLE

- opportunities: `41` (missing enhanced JSON: `0`)

| top_n | straight_hit | canonical_hit (BOX-eq) | index_hit_via_top_straights | index_in_top5_indices_ranked |
|---:|---:|---:|---:|---:|
| 8 | 0 (0.0000) | 0 (0.0000) | 3 (0.0732) | 5 (0.1220) |
| 12 | 0 (0.0000) | 0 (0.0000) | 4 (0.0976) | 5 (0.1220) |
| 20 | 0 (0.0000) | 0 (0.0000) | 5 (0.1220) | 5 (0.1220) |

## TRIPLE

- opportunities: `2` (missing enhanced JSON: `0`)

| top_n | straight_hit | canonical_hit (BOX-eq) | index_hit_via_top_straights | index_in_top5_indices_ranked |
|---:|---:|---:|---:|---:|
| 8 | 0 (0.0000) | 0 (0.0000) | 0 (0.0000) | 0 (0.0000) |
| 12 | 0 (0.0000) | 0 (0.0000) | 0 (0.0000) | 0 (0.0000) |
| 20 | 0 (0.0000) | 0 (0.0000) | 0 (0.0000) | 0 (0.0000) |
