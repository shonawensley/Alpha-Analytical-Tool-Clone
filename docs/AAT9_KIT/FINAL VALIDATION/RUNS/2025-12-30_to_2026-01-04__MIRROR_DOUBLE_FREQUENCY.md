# Mirror‑Double Frequency — 2025-12-30 → 2026-01-04

This report measures how often winners show *repeat structure* in VTRAC‑space even when they are not literal doubles.

- metrics: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_tool_metrics.csv`
- total outcomes: **163** (state×period rows)

## Literal winner composition

| Type | Count | % |
|---|---:|---:|
| single | 121 | 74.2% |
| double | 41 | 25.2% |
| triple | 1 | 0.6% |

## VTRAC‑signature repeats (mirror‑double‑ish)

- signature has repeats: **75/163** (46.0%)
- mirror‑repeat but literal SINGLE: **33/163** (20.2%)

## Per‑state frequency (mirror‑repeat)

| State | Outcomes | mirror_repeat | % | literal_double | % |
|---|---:|---:|---:|---:|---:|
| Connecticut4 | 12 | 6 | 50.0% | 4 | 33.3% |
| Delaware4 | 12 | 6 | 50.0% | 3 | 25.0% |
| Florida4 | 12 | 4 | 33.3% | 4 | 33.3% |
| Indiana4 | 12 | 7 | 58.3% | 4 | 33.3% |
| Michigan4 | 12 | 4 | 33.3% | 1 | 8.3% |
| NewJersey4 | 12 | 7 | 58.3% | 4 | 33.3% |
| NewYork4 | 12 | 6 | 50.0% | 3 | 25.0% |
| NorthCarolina4 | 12 | 7 | 58.3% | 4 | 33.3% |
| Ohio4 | 12 | 7 | 58.3% | 4 | 33.3% |
| OntarioCanada4 | 12 | 5 | 41.7% | 0 | 0.0% |
| Pennsylvania4 | 12 | 6 | 50.0% | 4 | 33.3% |
| PuertoRico4 | 8 | 1 | 12.5% | 1 | 12.5% |
| SouthCarolina4 | 11 | 3 | 27.3% | 1 | 9.1% |
| Virginia4 | 12 | 6 | 50.0% | 4 | 33.3% |

## Examples (mirror‑repeat but not literal double)

| date | state | period | winner | canonical | vtrac_sig | vtrac_index |
|---|---|---|---|---|---|---:|
| 2025-12-30 | Connecticut4 | Midday | 095 | 059 | 004 | 5 |
| 2025-12-30 | Michigan4 | Midday | 250 | 025 | 002 | 3 |
| 2025-12-30 | NewYork4 | Midday | 051 | 015 | 001 | 2 |
| 2025-12-30 | Ohio4 | Evening | 327 | 237 | 223 | 27 |
| 2025-12-30 | OntarioCanada4 | Evening | 372 | 237 | 223 | 27 |
| 2025-12-30 | OntarioCanada4 | Midday | 409 | 049 | 044 | 15 |
| 2025-12-30 | Pennsylvania4 | Midday | 186 | 168 | 113 | 18 |
| 2025-12-31 | Connecticut4 | Evening | 361 | 136 | 113 | 18 |
| 2025-12-31 | Michigan4 | Midday | 583 | 358 | 033 | 13 |
| 2025-12-31 | NewYork4 | Midday | 419 | 149 | 144 | 25 |
| 2025-12-31 | NorthCarolina4 | Evening | 057 | 057 | 002 | 3 |
| 2026-01-01 | Delaware4 | Midday | 149 | 149 | 144 | 25 |
| 2026-01-01 | NewJersey4 | Evening | 504 | 045 | 004 | 5 |
| 2026-01-01 | NorthCarolina4 | Evening | 053 | 035 | 003 | 4 |
| 2026-01-01 | NorthCarolina4 | Midday | 416 | 146 | 114 | 19 |
| 2026-01-01 | Ohio4 | Evening | 416 | 146 | 114 | 19 |
| 2026-01-01 | Pennsylvania4 | Evening | 328 | 238 | 233 | 29 |
| 2026-01-02 | Delaware4 | Midday | 126 | 126 | 112 | 17 |
| 2026-01-02 | Indiana4 | Midday | 974 | 479 | 244 | 31 |
| 2026-01-02 | OntarioCanada4 | Evening | 816 | 168 | 113 | 18 |
| 2026-01-02 | OntarioCanada4 | Midday | 053 | 035 | 003 | 4 |
| 2026-01-02 | SouthCarolina4 | Midday | 308 | 038 | 033 | 13 |
| 2026-01-03 | Indiana4 | Midday | 527 | 257 | 022 | 10 |
| 2026-01-03 | Michigan4 | Evening | 479 | 479 | 244 | 31 |
| 2026-01-03 | SouthCarolina4 | Evening | 051 | 015 | 001 | 2 |
| 2026-01-04 | Delaware4 | Midday | 057 | 057 | 002 | 3 |
| 2026-01-04 | Indiana4 | Midday | 813 | 138 | 133 | 23 |
| 2026-01-04 | NewJersey4 | Evening | 261 | 126 | 112 | 17 |
| 2026-01-04 | NewJersey4 | Midday | 275 | 257 | 022 | 10 |
| 2026-01-04 | NewYork4 | Evening | 489 | 489 | 344 | 34 |
| 2026-01-04 | Ohio4 | Evening | 492 | 249 | 244 | 31 |
| 2026-01-04 | OntarioCanada4 | Evening | 382 | 238 | 233 | 29 |
| 2026-01-04 | Virginia4 | Evening | 217 | 127 | 122 | 20 |

