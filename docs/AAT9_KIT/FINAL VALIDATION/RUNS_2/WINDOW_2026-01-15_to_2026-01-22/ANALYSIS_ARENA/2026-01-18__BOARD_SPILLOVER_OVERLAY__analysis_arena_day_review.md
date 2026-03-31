# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-18

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `6dcfd79a2d96d386`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 088, 559, 599, 008, 068, 688, 255 | 13, 29, 15, 3, 4, 5, 8, 21 | - | - | shared_host | Combined:WATCH/2, Evening:OFF/1, Midday:OFF/0 |
| 2 | Delaware4 | 259, 007, 559, 249, 579, 599, 047, 034 | 12, 5, 15, 31, 3, 35, 2, 17 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 3 | Florida4 | 225, 255, 559, 599, 378, 388, 178, 258 | 10, 3, 11, 5, 32, 27, 29, 21 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 4 | Indiana4 | 077, 368, 559, 005, 113, 139, 007 | 18, 9, 6, 23, 5, 15, 10, 8 | - | - | shared_host | Combined:ALERT/4, Midday:OFF/1, Evening:OFF/1 |
| 5 | Michigan4 | 224, 177, 011, 259, 117, 001, 017, 344 | 20, 17, 10, 28, 12, 2, 7, 15 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 6 | NewJersey4 | 019, 009, 004, 001, 559, 499, 259, 378 | 5, 9, 35, 12, 13, 2, 11, 33 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/0 |
| 7 | NewYork4 | 377, 339, 368, 237, 177, 007, 337 | 27, 23, 10, 33, 29, 18, 21, 20 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 8 | NorthCarolina4 | 244, 778, 225, 255, 237, 024, 238 | 27, 31, 10, 12, 29, 3, 26, 23 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 9 | Ohio4 | 009, 004, 049, 077, 007, 003, 599, 559 | 5, 15, 10, 3, 28, 35, 25, 34 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 10 | OntarioCanada4 | 244, 236, 344, 044, 014, 346, 001 | 31, 21, 34, 15, 12, 5, 9, 24 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/0 |
| 11 | Pennsylvania4 | 344, 004, 244, 224, 024, 668, 003, 034 | 34, 5, 31, 33, 18, 15, 28, 12 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 12 | PuertoRico4 | 334, 014, 148, 044, 244, 018, 336, 445 | 15, 33, 24, 8, 9, 31, 18, 23 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 13 | SouthCarolina4 | 005, 677, 007, 099, 006, 067 | 1, 15, 3, 2, 20, 7, 35, 5 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 14 | Virginia4 | 339, 016, 449, 559, 125, 015, 033, 001 | 6, 33, 2, 35, 5, 7, 25, 18 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 256 | 29 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 280 | 35 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 293 | 33 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 310 | 35 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 257 | 33 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 351 | 41 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 322 | 37 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 215 | 27 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 322 | 37 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 284 | 36 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Indiana4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 011, 014, 017, 368 | 7 | 12 | False | True |
| OntarioCanada4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 013, 014, 044, 244, 346 | 7 | 12 | False | True |
| Indiana4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 014, 017, 559 | 6 | 11 | False | True |
| Michigan4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 005, 011, 014, 017, 177 | 6 | 11 | False | True |
| Connecticut4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 006, 007, 024, 559 | 5 | 10 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 005, 011, 014, 017 | 5 | 10 | False | True |
| Indiana4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 006, 009, 011, 559 | 5 | 10 | False | True |
| NewJersey4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 014, 017 | 5 | 10 | False | True |
| NewYork4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 177, 237, 278, 377, 778 | 5 | 10 | False | True |
| Ohio4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 006, 007, 009, 559 | 5 | 10 | False | True |
| OntarioCanada4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 007, 244, 344, 349 | 5 | 10 | False | True |
| Connecticut4 | NewYork4 | shared_lane | lane/family | primary | 12, 23, 29, 3, 33, 5 | - | 6 | 10 | False | True |
| Connecticut4 | Ohio4 | shared_lane | lane/family | primary | 15, 23, 3, 33, 4, 5 | - | 6 | 10 | False | True |
| Florida4 | NewYork4 | shared_lane | lane/family | primary | 10, 20, 23, 29, 3, 5 | - | 6 | 10 | False | True |
| Indiana4 | NewYork4 | shared_lane | lane/family | primary | 1, 10, 18, 23, 33, 5 | - | 6 | 10 | False | True |
| Indiana4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 23, 24, 33, 9 | - | 6 | 10 | False | True |
| Indiana4 | Virginia4 | shared_lane | lane/family | primary | 15, 23, 24, 33, 5, 6 | - | 6 | 10 | False | True |
| Michigan4 | NewYork4 | shared_lane | lane/family | primary | 10, 12, 17, 18, 20, 5 | - | 6 | 10 | False | True |
| NewYork4 | NorthCarolina4 | shared_lane | lane/family | primary | 10, 12, 23, 27, 29, 3 | - | 6 | 10 | False | True |
| OntarioCanada4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 23, 24, 31, 33, 9 | - | 6 | 10 | False | True |
| Florida4 | NewJersey4 | alert_implied_echo | lane/family | primary | 9, 29 | 014, 019, 378 | 3 | 9 | False | True |
| NewJersey4 | Indiana4 | alert_implied_echo | lane/family | primary | 1, 5, 9 | 005, 009, 014 | 3 | 9 | False | True |
| NewJersey4 | NewYork4 | alert_implied_echo | lane/family | primary | 1, 5, 9 | 005, 009, 014 | 3 | 9 | False | True |
| Ohio4 | NewJersey4 | alert_implied_echo | lane/family | primary | 5 | 004, 009, 059 | 3 | 9 | False | True |
| Pennsylvania4 | OntarioCanada4 | alert_implied_echo | lane/family | primary | 5, 34 | 004, 344, 349 | 3 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_box_family | lane/family | primary | - | 004, 007, 559, 599 | 4 | 9 | False | True |
| Connecticut4 | Florida4 | shared_box_family | lane/family | primary | - | 007, 378, 559, 599 | 4 | 9 | False | True |
| Connecticut4 | Indiana4 | shared_box_family | lane/family | primary | - | 006, 038, 068, 559 | 4 | 9 | False | True |
| Connecticut4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 006, 007, 559 | 4 | 9 | False | True |
| Delaware4 | Florida4 | shared_box_family | lane/family | primary | - | 007, 017, 559, 599 | 4 | 9 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 009, 017, 559 | 4 | 9 | False | True |
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 007, 009, 559 | 4 | 9 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 007, 009, 559 | 4 | 9 | False | True |
| Florida4 | NewJersey4 | shared_box_family | lane/family | primary | - | 013, 017, 378, 559 | 4 | 9 | False | True |
| Indiana4 | Ohio4 | shared_box_family | lane/family | primary | - | 006, 009, 077, 559 | 4 | 9 | False | True |
| Indiana4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 006, 009, 559, 668 | 4 | 9 | False | True |
| Indiana4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 006, 011, 014 | 4 | 9 | False | True |
| Michigan4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 005, 014, 017 | 4 | 9 | False | True |
| NewJersey4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 009, 455, 559 | 4 | 9 | False | True |
| NewJersey4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 004, 013, 014 | 4 | 9 | False | True |

## Strongest Overlap Pairs

- `Indiana4 ↔ NewYork4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `OntarioCanada4 ↔ PuertoRico4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ NewJersey4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ NewYork4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `OntarioCanada4 ↔ Pennsylvania4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ NewYork4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Michigan4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ Pennsylvania4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Ohio4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ PuertoRico4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
