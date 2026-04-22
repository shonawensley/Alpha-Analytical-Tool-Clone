# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-04

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `c8a7b97b4bd39fd5`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 224, 456, 024, 668, 004, 447 | 28, 9, 31, 12, 14, 5, 18, 25 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/0 |
| 2 | Delaware4 | 449, 559, 004, 058, 055, 244, 599, 445 | 5, 35, 15, 4, 11, 31, 1, 13 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 3 | Florida4 | 344, 334, 033, 467, 445, 346, 559, 259 | 33, 23, 15, 24, 22, 32, 31, 34 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/0 |
| 4 | Indiana4 | 244, 668, 138, 368, 066, 016, 366 | 18, 23, 31, 6, 17, 16, 28, 10 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 5 | Michigan4 | 168, 668, 156, 169, 189, 013 | 18, 6, 19, 23, 8, 35, 2, 24 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 6 | NewJersey4 | 599, 299, 229, 289, 559, 778, 899 | 31, 15, 12, 28, 30, 24, 5, 27 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 7 | NewYork4 | 038, 005, 025, 008, 788, 667, 066, 889 | 3, 13, 33, 18, 6, 4, 17, 5 | - | - | shared_host | Evening:WATCH/2, Midday:OFF/1, Combined:OFF/0 |
| 8 | NorthCarolina4 | 229, 299, 044, 224, 029 | 28, 15, 31, 12, 5, 25, 4, 26 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 9 | Ohio4 | 559, 599, 259, 008, 255, 088, 225, 299 | 5, 3, 12, 15, 10, 4, 13, 1 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 10 | OntarioCanada4 | 007, 047, 118, 225, 459, 477, 177, 244 | 20, 10, 3, 12, 15, 18, 17, 31 | - | - | shared_host | Combined:OFF/1, Midday:OFF/0, Evening:OFF/0 |
| 11 | Pennsylvania4 | 559, 599, 059, 055, 255, 007, 455 | 5, 15, 3, 1, 12, 34, 23, 18 | - | - | shared_host | Midday:WATCH/2, Evening:OFF/1, Combined:OFF/0 |
| 12 | PuertoRico4 | 344, 224, 268, 026, 003, 226, 002, 266 | 7, 21, 4, 10, 3, 28, 31, 34 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 13 | SouthCarolina4 | 002, 559, 007, 677, 224, 259, 599, 378 | 3, 5, 28, 10, 29, 4, 20, 18 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 14 | Virginia4 | 224, 229, 559, 377, 334, 002, 255, 259 | 28, 27, 3, 5, 23, 33, 29, 10 | - | - | shared_host | Midday:WATCH/2, Evening:OFF/1, Combined:OFF/0 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 267 | 32 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 339 | 41 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 251 | 31 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 190 | 23 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 162 | 19 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 241 | 29 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 239 | 28 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 237 | 28 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 281 | 35 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 270 | 32 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 011, 013, 014, 016, 066, 168, 366, 668 | 8 | 13 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_lane | lane/family | primary | 10, 12, 17, 18, 20, 23, 28, 3 | - | 8 | 12 | False | True |
| Delaware4 | Virginia4 | alert_implied_echo | lane/family | primary | 28 | 224, 229, 247, 279, 477 | 5 | 11 | False | True |
| NewJersey4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 001, 004, 005, 229, 299, 599 | 6 | 11 | False | True |
| NewYork4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 006, 008, 025, 088, 255 | 6 | 11 | False | True |
| Ohio4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 009, 059, 255, 559, 599 | 6 | 11 | False | True |
| OntarioCanada4 | PuertoRico4 | shared_lane | lane/family | primary | 10, 15, 18, 20, 23, 28, 3 | - | 7 | 11 | False | True |
| PuertoRico4 | SouthCarolina4 | shared_lane | lane/family | primary | 10, 18, 20, 21, 23, 28, 3 | - | 7 | 11 | False | True |
| SouthCarolina4 | Virginia4 | shared_lane | lane/family | primary | 10, 12, 18, 23, 28, 3, 5 | - | 7 | 11 | False | True |
| Delaware4 | NorthCarolina4 | alert_implied_echo | lane/family | primary | 5, 28, 15 | 004, 224, 229, 599 | 4 | 10 | False | True |
| Pennsylvania4 | Delaware4 | alert_implied_echo | lane/family | primary | 5, 1 | 045, 055, 455, 559 | 4 | 10 | False | True |
| SouthCarolina4 | OntarioCanada4 | alert_implied_echo | lane/family | primary | 3, 20 | 007, 226, 267, 677 | 4 | 10 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 045, 055, 455, 559 | 5 | 10 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 009, 059, 255, 259, 559 | 5 | 10 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 007, 009, 059, 255, 559 | 5 | 10 | False | True |
| Connecticut4 | NorthCarolina4 | shared_lane | lane/family | primary | 12, 15, 23, 28, 31, 5 | - | 6 | 10 | False | True |
| NewYork4 | Ohio4 | shared_lane | lane/family | primary | 1, 12, 13, 3, 4, 5 | - | 6 | 10 | False | True |
| NewYork4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 17, 18, 29, 3, 5 | - | 6 | 10 | False | True |
| OntarioCanada4 | Virginia4 | shared_lane | lane/family | primary | 10, 12, 18, 23, 28, 3 | - | 6 | 10 | False | True |
| Delaware4 | Connecticut4 | alert_implied_echo | lane/family | primary | 5, 28 | 004, 224, 229 | 3 | 9 | False | True |
| Delaware4 | NewJersey4 | alert_implied_echo | lane/family | primary | 5, 28, 15 | 004, 229, 599 | 3 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_box_family | lane/family | primary | - | 004, 011, 014, 017 | 4 | 9 | False | True |
| Connecticut4 | Indiana4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 668 | 4 | 9 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 244 | 4 | 9 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 014, 244, 559 | 4 | 9 | False | True |
| Florida4 | Indiana4 | shared_box_family | lane/family | primary | - | 014, 138, 368, 688 | 4 | 9 | False | True |
| Florida4 | NewYork4 | shared_box_family | lane/family | primary | - | 006, 007, 057, 889 | 4 | 9 | False | True |
| NewJersey4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 014, 559, 599 | 4 | 9 | False | True |
| NewJersey4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 559, 599 | 4 | 9 | False | True |
| NewYork4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 255 | 4 | 9 | False | True |
| NorthCarolina4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 009, 029, 599 | 4 | 9 | False | True |
| NorthCarolina4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 009, 599 | 4 | 9 | False | True |
| Connecticut4 | NewJersey4 | shared_lane | lane/family | primary | 12, 15, 28, 31, 5 | - | 5 | 9 | False | True |
| Connecticut4 | OntarioCanada4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 28 | - | 5 | 9 | False | True |
| Connecticut4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 18, 23, 28, 5 | - | 5 | 9 | False | True |
| Connecticut4 | Virginia4 | shared_lane | lane/family | primary | 12, 18, 23, 28, 5 | - | 5 | 9 | False | True |
| Delaware4 | Pennsylvania4 | shared_lane | lane/family | primary | 1, 15, 23, 34, 5 | - | 5 | 9 | False | True |
| NewJersey4 | NorthCarolina4 | shared_lane | lane/family | primary | 12, 15, 28, 31, 5 | - | 5 | 9 | False | True |
| NewYork4 | Virginia4 | shared_lane | lane/family | primary | 12, 18, 3, 33, 5 | - | 5 | 9 | False | True |
| Ohio4 | Pennsylvania4 | shared_lane | lane/family | primary | 1, 12, 15, 3, 5 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `OntarioCanada4 ↔ SouthCarolina4` score=`38` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Pennsylvania4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ Pennsylvania4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Delaware4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Pennsylvania4 ↔ SouthCarolina4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `SouthCarolina4 ↔ Virginia4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NorthCarolina4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ SouthCarolina4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Michigan4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NewJersey4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
