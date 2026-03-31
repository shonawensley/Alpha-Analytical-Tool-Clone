# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-05

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `cb19eb740fcf8dd2`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 224, 447, 024, 044, 244, 468, 004 | 28, 31, 12, 5, 9, 18, 34, 15 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 2 | Delaware4 | 449, 244, 004, 055, 388, 144, 559, 058 | 5, 31, 35, 15, 33, 32, 4, 13 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 3 | Florida4 | 344, 033, 334, 445, 336, 346, 034, 044 | 33, 15, 34, 23, 13, 24, 31, 12 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 4 | Indiana4 | 244, 668, 066, 366, 368, 138 | 31, 18, 23, 6, 17, 28, 10, 12 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 5 | Michigan4 | 168, 118, 668, 011, 156, 166, 016 | 18, 6, 23, 2, 8, 17, 7, 16 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 778, 008, 599, 289, 299, 899, 488, 148 | 4, 27, 15, 31, 30, 34, 12, 28 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 7 | NewYork4 | 025, 008, 005, 066, 056, 088, 067, 255 | 3, 6, 7, 2, 4, 1, 18, 17 | - | - | shared_host | Evening:ALERT/3, Combined:WATCH/2, Midday:OFF/1 |
| 8 | NorthCarolina4 | 229, 224, 299, 044, 599, 559, 244, 004 | 28, 15, 31, 5, 22, 25, 12, 9 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 9 | Ohio4 | 088, 599, 008, 559, 058, 225, 259 | 13, 4, 5, 15, 10, 3, 1, 12 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 10 | OntarioCanada4 | 477, 177, 459, 244, 014, 147, 255 | 20, 28, 15, 21, 22, 31, 18, 17 | - | - | shared_host | Combined:ALERT/3, Midday:OFF/1, Evening:OFF/1 |
| 11 | Pennsylvania4 | 559, 059, 599, 005, 007, 055, 255 | 5, 15, 3, 1, 14, 9, 2, 34 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 12 | PuertoRico4 | 344, 224, 268, 026, 003, 226, 002, 266 | 7, 21, 4, 10, 3, 28, 31, 34 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 13 | SouthCarolina4 | 677, 007, 599, 259, 267, 224, 559 | 20, 3, 15, 4, 28, 12, 29, 18 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 14 | Virginia4 | 224, 559, 377, 008, 229, 259, 002, 599 | 28, 27, 5, 12, 33, 4, 23, 15 | - | - | shared_host | Evening:ALERT/3, Midday:WATCH/2, Combined:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 282 | 34 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 262 | 33 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 229 | 28 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 262 | 33 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 208 | 28 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 241 | 31 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 257 | 33 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 215 | 27 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 260 | 31 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 212 | 26 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Connecticut4 | Indiana4 | shared_box_family | lane/family | primary | - | 011, 014, 244, 249, 299, 447 | 6 | 11 | False | True |
| PuertoRico4 | SouthCarolina4 | shared_lane | lane/family | primary | 15, 18, 20, 23, 28, 3, 4 | - | 7 | 11 | False | True |
| Connecticut4 | Michigan4 | alert_implied_echo | lane/family | primary | 18 | 118, 136, 168, 668 | 4 | 10 | False | True |
| Connecticut4 | Delaware4 | shared_box_family | lane/family | primary | - | 011, 014, 044, 244, 447 | 5 | 10 | False | True |
| NewJersey4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 004, 005, 099, 299, 599 | 5 | 10 | False | True |
| NewJersey4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 445, 599 | 5 | 10 | False | True |
| NorthCarolina4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 009, 559, 599 | 5 | 10 | False | True |
| NorthCarolina4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 001, 009, 224, 559, 599 | 5 | 10 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 011, 224, 259, 559, 599 | 5 | 10 | False | True |
| Connecticut4 | OntarioCanada4 | shared_lane | lane/family | primary | 12, 15, 18, 28, 31, 9 | - | 6 | 10 | False | True |
| SouthCarolina4 | OntarioCanada4 | alert_implied_echo | lane/family | primary | 20 | 226, 267, 677 | 3 | 9 | False | True |
| Connecticut4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 044, 224, 229, 299 | 4 | 9 | False | True |
| Connecticut4 | Virginia4 | shared_box_family | lane/family | primary | - | 011, 014, 224, 229 | 4 | 9 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 011, 014, 244, 447 | 4 | 9 | False | True |
| Florida4 | NewJersey4 | shared_box_family | lane/family | primary | - | 007, 014, 445, 599 | 4 | 9 | False | True |
| Indiana4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 244 | 4 | 9 | False | True |
| Michigan4 | NewYork4 | shared_box_family | lane/family | primary | - | 005, 006, 011, 566 | 4 | 9 | False | True |
| NewJersey4 | NewYork4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 008 | 4 | 9 | False | True |
| NewJersey4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 008, 035, 599 | 4 | 9 | False | True |
| NewYork4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 006, 008, 088 | 4 | 9 | False | True |
| NewYork4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 007, 011, 057, 255 | 4 | 9 | False | True |
| NorthCarolina4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 009, 559, 599 | 4 | 9 | False | True |
| NorthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 224, 229, 559, 599 | 4 | 9 | False | True |
| Ohio4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 009, 559, 599 | 4 | 9 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 009, 259, 559, 599 | 4 | 9 | False | True |
| Ohio4 | Virginia4 | shared_box_family | lane/family | primary | - | 008, 259, 559, 599 | 4 | 9 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 011, 255, 267, 677 | 4 | 9 | False | True |
| OntarioCanada4 | Virginia4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 477 | 4 | 9 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 007, 009, 559, 599 | 4 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_lane | lane/family | primary | 15, 18, 23, 31, 5 | - | 5 | 9 | False | True |
| Connecticut4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 28 | - | 5 | 9 | False | True |
| Delaware4 | Pennsylvania4 | shared_lane | lane/family | primary | 1, 15, 18, 23, 5 | - | 5 | 9 | False | True |
| NewYork4 | Ohio4 | shared_lane | lane/family | primary | 1, 13, 3, 4, 5 | - | 5 | 9 | False | True |
| OntarioCanada4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 20, 21, 28 | - | 5 | 9 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 15, 18, 20, 28 | - | 5 | 9 | False | True |
| Connecticut4 | Indiana4 | alert_implied_echo | lane/family | primary | 18 | 366, 668 | 2 | 8 | False | True |
| Connecticut4 | Virginia4 | alert_implied_echo | lane/family | primary | 18, 12 | 113, 259 | 2 | 8 | False | True |
| Indiana4 | Connecticut4 | alert_implied_echo | lane/family | primary | 6, 31 | 011, 244 | 2 | 8 | False | True |
| Indiana4 | Delaware4 | alert_implied_echo | lane/family | primary | 6, 31 | 011, 244 | 2 | 8 | False | True |
| Indiana4 | Michigan4 | alert_implied_echo | lane/family | primary | 6 | 011, 016 | 2 | 8 | False | True |

## Strongest Overlap Pairs

- `Connecticut4 ↔ Indiana4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `OntarioCanada4 ↔ SouthCarolina4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ SouthCarolina4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ OntarioCanada4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ Virginia4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Michigan4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Virginia4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `PuertoRico4 ↔ SouthCarolina4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ OntarioCanada4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ NewYork4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
