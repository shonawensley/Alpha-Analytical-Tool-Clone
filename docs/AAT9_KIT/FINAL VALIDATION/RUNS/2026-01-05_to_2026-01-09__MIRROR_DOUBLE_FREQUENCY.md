# Mirror‑Double Frequency — 2026-01-05 → 2026-01-09

This report measures how often winners show *repeat structure* in VTRAC‑space even when they are not literal doubles.

- metrics: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_tool_metrics.csv`
- total outcomes: **138** (state×period rows)

## Literal winner composition

| Type | Count | % |
|---|---:|---:|
| single | 95 | 68.8% |
| double | 41 | 29.7% |
| triple | 2 | 1.4% |

## VTRAC‑signature repeats (mirror‑double‑ish)

- signature has repeats: **74/138** (53.6%)
- mirror‑repeat but literal SINGLE: **31/138** (22.5%)

## Per‑state frequency (mirror‑repeat)

| State | Outcomes | mirror_repeat | % | literal_double | % |
|---|---:|---:|---:|---:|---:|
| Connecticut4 | 10 | 6 | 60.0% | 4 | 40.0% |
| Delaware4 | 10 | 5 | 50.0% | 1 | 10.0% |
| Florida4 | 10 | 5 | 50.0% | 3 | 30.0% |
| Indiana4 | 10 | 4 | 40.0% | 2 | 20.0% |
| Michigan4 | 10 | 4 | 40.0% | 2 | 20.0% |
| NewJersey4 | 10 | 5 | 50.0% | 1 | 10.0% |
| NewYork4 | 10 | 7 | 70.0% | 4 | 40.0% |
| NorthCarolina4 | 10 | 4 | 40.0% | 4 | 40.0% |
| Ohio4 | 10 | 6 | 60.0% | 3 | 30.0% |
| OntarioCanada4 | 10 | 7 | 70.0% | 4 | 40.0% |
| Pennsylvania4 | 10 | 5 | 50.0% | 4 | 40.0% |
| PuertoRico4 | 8 | 6 | 75.0% | 2 | 25.0% |
| SouthCarolina4 | 10 | 5 | 50.0% | 4 | 40.0% |
| Virginia4 | 10 | 5 | 50.0% | 3 | 30.0% |

## Examples (mirror‑repeat but not literal double)

| date | state | period | winner | canonical | vtrac_sig | vtrac_index |
|---|---|---|---|---|---|---:|
| 2026-01-05 | Delaware4 | Evening | 267 | 267 | 122 | 20 |
| 2026-01-05 | NewJersey4 | Evening | 694 | 469 | 144 | 25 |
| 2026-01-05 | Ohio4 | Midday | 651 | 156 | 011 | 6 |
| 2026-01-05 | PuertoRico4 | Evening | 972 | 279 | 224 | 28 |
| 2026-01-05 | PuertoRico4 | Midday | 732 | 237 | 223 | 27 |
| 2026-01-05 | SouthCarolina4 | Evening | 712 | 127 | 122 | 20 |
| 2026-01-06 | Delaware4 | Midday | 165 | 156 | 011 | 6 |
| 2026-01-06 | Florida4 | Evening | 160 | 016 | 011 | 6 |
| 2026-01-06 | Indiana4 | Evening | 961 | 169 | 114 | 19 |
| 2026-01-06 | Michigan4 | Midday | 618 | 168 | 113 | 18 |
| 2026-01-06 | NewJersey4 | Evening | 942 | 249 | 244 | 31 |
| 2026-01-07 | Connecticut4 | Midday | 156 | 156 | 011 | 6 |
| 2026-01-07 | Indiana4 | Midday | 823 | 238 | 233 | 29 |
| 2026-01-07 | NewJersey4 | Midday | 361 | 136 | 113 | 18 |
| 2026-01-07 | NewYork4 | Midday | 916 | 169 | 114 | 19 |
| 2026-01-07 | Virginia4 | Midday | 275 | 257 | 022 | 10 |
| 2026-01-08 | Connecticut4 | Midday | 106 | 016 | 011 | 6 |
| 2026-01-08 | Florida4 | Midday | 429 | 249 | 244 | 31 |
| 2026-01-08 | NewYork4 | Evening | 732 | 237 | 223 | 27 |
| 2026-01-08 | Ohio4 | Evening | 580 | 058 | 003 | 4 |
| 2026-01-08 | Ohio4 | Midday | 681 | 168 | 113 | 18 |
| 2026-01-08 | OntarioCanada4 | Evening | 498 | 489 | 344 | 34 |
| 2026-01-08 | Pennsylvania4 | Midday | 750 | 057 | 002 | 3 |
| 2026-01-08 | PuertoRico4 | Evening | 479 | 479 | 244 | 31 |
| 2026-01-09 | Delaware4 | Evening | 681 | 168 | 113 | 18 |
| 2026-01-09 | Delaware4 | Midday | 843 | 348 | 334 | 33 |
| 2026-01-09 | Michigan4 | Evening | 273 | 237 | 223 | 27 |
| 2026-01-09 | NewJersey4 | Midday | 287 | 278 | 223 | 27 |
| 2026-01-09 | NewYork4 | Evening | 835 | 358 | 033 | 13 |
| 2026-01-09 | PuertoRico4 | Midday | 126 | 126 | 112 | 17 |
| 2026-01-09 | Virginia4 | Midday | 380 | 038 | 033 | 13 |

