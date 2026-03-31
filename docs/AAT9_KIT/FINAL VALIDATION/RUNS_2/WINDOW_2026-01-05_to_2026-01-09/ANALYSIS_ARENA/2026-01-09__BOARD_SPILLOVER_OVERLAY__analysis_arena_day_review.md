# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-09

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `3e44f610dcd957e1`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 224, 448, 229, 244, 299, 044, 289 | 28, 34, 31, 15, 30, 33, 25, 12 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 2 | Delaware4 | 344, 033, 445, 144, 334, 044, 339 | 15, 34, 13, 33, 5, 14, 31, 35 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/0 |
| 3 | Florida4 | 255, 559, 224, 356, 033, 346, 557, 034 | 3, 5, 33, 8, 23, 24, 13, 28 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:OFF/0 |
| 4 | Indiana4 | 244, 669, 004, 066, 045, 344, 069, 169 | 5, 9, 19, 6, 18, 31, 15, 20 | - | - | shared_host | Midday:OFF/1, Evening:OFF/1, Combined:OFF/0 |
| 5 | Michigan4 | 334, 019, 059, 559, 144, 599, 001, 009 | 15, 5, 33, 9, 14, 34, 35, 2 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 6 | NewJersey4 | 778, 137, 014, 037, 003, 013, 017 | 4, 27, 12, 11, 21, 3, 28, 15 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/0 |
| 7 | NewYork4 | 005, 001, 255, 025, 008, 045, 455, 004 | 3, 5, 1, 2, 4, 6, 7, 12 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 8 | NorthCarolina4 | 299, 066, 446, 466, 099, 244, 366, 044 | 15, 31, 25, 19, 6, 5, 8, 18 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 9 | Ohio4 | 599, 559, 299, 399, 788, 359, 889, 255 | 15, 5, 14, 34, 33, 13, 31, 25 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 10 | OntarioCanada4 | 015, 006, 224, 367, 244, 347, 255, 066 | 2, 21, 6, 30, 31, 28, 5, 3 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 11 | Pennsylvania4 | 445, 019, 009, 113, 455, 559, 114, 119 | 5, 9, 18, 15, 19, 31, 3, 23 | - | - | shared_host | Midday:ALERT/3, Combined:OFF/1, Evening:OFF/0 |
| 12 | PuertoRico4 | 068, 008, 006, 688, 188, 088, 245, 011 | 8, 23, 4, 2, 5, 12, 13, 10 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/0 |
| 13 | SouthCarolina4 | 599, 559, 244, 059, 499, 004, 099, 224 | 15, 5, 31, 35, 28, 14, 4, 12 | - | - | shared_host | Midday:ALERT/3, Evening:OFF/1, Combined:OFF/0 |
| 14 | Virginia4 | 024, 559, 599, 346, 134, 334, 344 | 5, 24, 15, 12, 34, 23, 18, 33 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 281 | 33 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 308 | 35 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 284 | 35 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 321 | 39 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 260 | 31 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 189 | 22 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 315 | 38 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 283 | 36 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 303 | 36 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 314 | 41 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Florida4 | NewYork4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 007, 025, 045, 057, 255, 557 | 9 | 14 | False | True |
| Michigan4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 009, 044, 049, 059, 459, 559, 599 | 8 | 13 | False | True |
| NorthCarolina4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 006, 009, 044, 049, 099, 244, 445 | 8 | 13 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 009, 049, 059, 099, 559, 599 | 8 | 13 | False | True |
| NorthCarolina4 | Ohio4 | shared_box_family | lane/family | primary | - | 006, 009, 039, 049, 066, 099, 299 | 7 | 12 | False | True |
| Delaware4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 011, 044, 144, 334, 459 | 6 | 11 | False | True |
| Michigan4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 009, 049, 059, 559, 599 | 6 | 11 | False | True |
| Michigan4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 011, 059, 334, 559, 599 | 6 | 11 | False | True |
| Indiana4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 19, 23, 34, 5, 9 | - | 7 | 11 | False | True |
| NewYork4 | Florida4 | alert_implied_echo | lane/family | primary | 1, 2, 5, 3 | 005, 006, 045, 057 | 4 | 10 | False | True |
| NewYork4 | OntarioCanada4 | alert_implied_echo | lane/family | primary | 2 | 001, 006, 015, 056 | 4 | 10 | False | True |
| Delaware4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 004, 011, 014, 334 | 5 | 10 | False | True |
| Indiana4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 014, 017, 455, 559 | 5 | 10 | False | True |
| NewYork4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 007, 008 | 5 | 10 | False | True |
| NorthCarolina4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 009, 244 | 5 | 10 | False | True |
| Delaware4 | Michigan4 | shared_lane | lane/family | primary | 15, 18, 23, 25, 33, 5 | - | 6 | 10 | False | True |
| Delaware4 | Virginia4 | shared_lane | lane/family | primary | 15, 18, 23, 33, 34, 5 | - | 6 | 10 | False | True |
| Indiana4 | Ohio4 | shared_lane | lane/family | primary | 12, 15, 23, 31, 34, 5 | - | 6 | 10 | False | True |
| Indiana4 | Virginia4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 34, 5 | - | 6 | 10 | False | True |
| Ohio4 | Virginia4 | shared_lane | lane/family | primary | 12, 15, 23, 33, 34, 5 | - | 6 | 10 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 004, 013, 014, 344 | 4 | 9 | False | True |
| Delaware4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 001, 004, 044, 445 | 4 | 9 | False | True |
| Delaware4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 044, 445, 459 | 4 | 9 | False | True |
| Florida4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 559 | 4 | 9 | False | True |
| Florida4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 004, 006, 224, 255 | 4 | 9 | False | True |
| Florida4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 007 | 4 | 9 | False | True |
| Florida4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 559 | 4 | 9 | False | True |
| Indiana4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 014, 066, 455, 559 | 4 | 9 | False | True |
| Michigan4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 001, 009, 044, 049 | 4 | 9 | False | True |
| Michigan4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 009, 019, 059, 559 | 4 | 9 | False | True |
| NewYork4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 255 | 4 | 9 | False | True |
| Ohio4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 009, 059, 066, 559 | 4 | 9 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 006, 009, 244 | 4 | 9 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 009, 059, 445, 559 | 4 | 9 | False | True |
| Pennsylvania4 | Virginia4 | shared_box_family | lane/family | primary | - | 014, 059, 455, 559 | 4 | 9 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 059, 559, 599 | 4 | 9 | False | True |
| Delaware4 | Florida4 | shared_lane | lane/family | primary | 13, 15, 23, 33, 5 | - | 5 | 9 | False | True |
| Delaware4 | Indiana4 | shared_lane | lane/family | primary | 15, 18, 23, 34, 5 | - | 5 | 9 | False | True |
| Delaware4 | Ohio4 | shared_lane | lane/family | primary | 15, 23, 33, 34, 5 | - | 5 | 9 | False | True |
| Delaware4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 23, 34, 5 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `NewYork4 ↔ OntarioCanada4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ Ohio4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Indiana4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ Pennsylvania4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ PuertoRico4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Michigan4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Virginia4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ Pennsylvania4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ OntarioCanada4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ NorthCarolina4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
