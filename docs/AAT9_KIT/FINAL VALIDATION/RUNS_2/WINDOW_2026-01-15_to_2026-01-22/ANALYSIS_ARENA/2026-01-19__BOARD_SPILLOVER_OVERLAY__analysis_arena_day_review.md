# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-19

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `c9a60330ac524bd5`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 599, 058, 559, 006, 005, 025, 088, 455 | 4, 3, 15, 5, 2, 13, 1, 8 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 2 | Delaware4 | 559, 259, 007, 467, 567, 224, 157, 177 | 5, 12, 7, 31, 3, 22, 20, 15 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 3 | Florida4 | 388, 255, 378, 235, 559, 358, 158, 889 | 32, 3, 29, 8, 11, 5, 10, 33 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 4 | Indiana4 | 077, 007, 038, 005, 599, 368, 011, 017 | 10, 6, 23, 9, 18, 3, 15, 1 | - | - | shared_host | Combined:OFF/1, Evening:OFF/1, Midday:OFF/0 |
| 5 | Michigan4 | 224, 011, 017, 778, 225, 117, 115 | 28, 10, 6, 3, 17, 7, 20, 27 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 004, 014, 019, 000, 001, 009, 559, 348 | 5, 9, 2, 25, 15, 33, 12, 26 | - | - | shared_host | Combined:ALERT/3, Midday:WATCH/2, Evening:OFF/0 |
| 7 | NewYork4 | 377, 337, 177, 339, 668, 115 | 27, 18, 10, 21, 29, 20, 23, 6 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/0 |
| 8 | NorthCarolina4 | 778, 244, 225, 238, 024, 378, 237 | 27, 31, 29, 10, 12, 5, 3, 23 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 9 | Ohio4 | 004, 009, 077, 007, 003, 049, 008 | 5, 15, 10, 3, 4, 35, 14, 24 | - | - | shared_host | Evening:ALERT/3, Combined:WATCH/2, Midday:OFF/1 |
| 10 | OntarioCanada4 | 244, 044, 236, 344, 001, 224 | 31, 21, 15, 12, 2, 34, 11, 25 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/0 |
| 11 | Pennsylvania4 | 344, 004, 224, 034, 668, 044, 244, 249 | 34, 31, 5, 14, 28, 12, 18, 15 | - | - | shared_host | Evening:ALERT/3, Combined:OFF/1, Midday:OFF/1 |
| 12 | PuertoRico4 | 334, 014, 148, 044, 244, 018, 336, 445 | 15, 33, 24, 8, 9, 31, 18, 23 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 13 | SouthCarolina4 | 005, 099, 399, 009, 677, 003, 599 | 1, 15, 5, 2, 35, 3, 4, 17 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 14 | Virginia4 | 339, 133, 002, 559, 449, 006, 033, 016 | 33, 23, 6, 2, 5, 35, 22, 3 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 280 | 34 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 290 | 36 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 204 | 25 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 334 | 42 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 245 | 32 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 330 | 42 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 297 | 36 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 211 | 27 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 302 | 35 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 293 | 36 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| OntarioCanada4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 007, 044, 224, 244, 249, 344 | 7 | 12 | False | True |
| OntarioCanada4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 014, 044, 244, 445 | 7 | 12 | False | True |
| Connecticut4 | SouthCarolina4 | shared_lane | lane/family | primary | 1, 15, 2, 21, 23, 3, 4, 5 | - | 8 | 12 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 009, 017, 059, 455, 559 | 6 | 11 | False | True |
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 007, 009, 455, 559 | 5 | 10 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 027, 077 | 5 | 10 | False | True |
| Indiana4 | NewYork4 | shared_box_family | lane/family | primary | - | 007, 011, 014, 017, 368 | 5 | 10 | False | True |
| Michigan4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 011, 014, 017, 115 | 5 | 10 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 003, 006, 007, 009, 049 | 5 | 10 | False | True |
| Connecticut4 | Ohio4 | shared_lane | lane/family | primary | 15, 23, 3, 33, 4, 5 | - | 6 | 10 | False | True |
| Florida4 | NewYork4 | shared_lane | lane/family | primary | 10, 11, 20, 21, 23, 29 | - | 6 | 10 | False | True |
| OntarioCanada4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 23, 28, 31, 34 | - | 6 | 10 | False | True |
| Ohio4 | Delaware4 | alert_implied_echo | lane/family | primary | 5 | 004, 009, 059 | 3 | 9 | False | True |
| Ohio4 | NewJersey4 | alert_implied_echo | lane/family | primary | 5 | 004, 009, 059 | 3 | 9 | False | True |
| Ohio4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 4, 5, 15 | 003, 009, 049 | 3 | 9 | False | True |
| PuertoRico4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 31 | 244, 249, 447 | 3 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_box_family | lane/family | primary | - | 004, 007, 224, 559 | 4 | 9 | False | True |
| Connecticut4 | Indiana4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 599 | 4 | 9 | False | True |
| Connecticut4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 006, 007, 559 | 4 | 9 | False | True |
| Connecticut4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 004, 006, 007, 224 | 4 | 9 | False | True |
| Connecticut4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 224 | 4 | 9 | False | True |
| Connecticut4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 599 | 4 | 9 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 007, 009, 224 | 4 | 9 | False | True |
| Indiana4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 006, 007, 014, 368 | 4 | 9 | False | True |
| Indiana4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 599 | 4 | 9 | False | True |
| NewJersey4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 009, 455, 559 | 4 | 9 | False | True |
| NewJersey4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 013, 014 | 4 | 9 | False | True |
| NewYork4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 177, 237, 278, 377 | 4 | 9 | False | True |
| NewYork4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 007, 014, 368 | 4 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_lane | lane/family | primary | 12, 15, 23, 3, 5 | - | 5 | 9 | False | True |
| Connecticut4 | Indiana4 | shared_lane | lane/family | primary | 1, 15, 23, 3, 33 | - | 5 | 9 | False | True |
| Connecticut4 | OntarioCanada4 | shared_lane | lane/family | primary | 12, 15, 2, 21, 23 | - | 5 | 9 | False | True |
| Connecticut4 | Virginia4 | shared_lane | lane/family | primary | 2, 23, 3, 33, 5 | - | 5 | 9 | False | True |
| Delaware4 | OntarioCanada4 | shared_lane | lane/family | primary | 12, 15, 23, 28, 31 | - | 5 | 9 | False | True |
| Delaware4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 23, 28, 31, 5 | - | 5 | 9 | False | True |
| Florida4 | SouthCarolina4 | shared_lane | lane/family | primary | 20, 21, 23, 3, 5 | - | 5 | 9 | False | True |
| Indiana4 | Michigan4 | shared_lane | lane/family | primary | 10, 15, 18, 3, 6 | - | 5 | 9 | False | True |
| Indiana4 | NewYork4 | shared_lane | lane/family | primary | 10, 18, 23, 33, 6 | - | 5 | 9 | False | True |
| Indiana4 | Ohio4 | shared_lane | lane/family | primary | 10, 15, 23, 3, 33 | - | 5 | 9 | False | True |
| Indiana4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 23, 33, 9 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `OntarioCanada4 ↔ Pennsylvania4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `OntarioCanada4 ↔ PuertoRico4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Ohio4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Michigan4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ NewYork4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NewJersey4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ NewYork4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Ohio4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ PuertoRico4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Delaware4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
