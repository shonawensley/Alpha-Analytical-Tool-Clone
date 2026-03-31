# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-07

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `cd0f4cf241b0d7d6`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 224, 244, 229, 448, 478, 248 | 28, 31, 30, 34, 25, 27, 15, 9 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 2 | Delaware4 | 334, 003, 044, 118, 033, 011, 389 | 33, 15, 4, 23, 5, 31, 13, 18 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 3 | Florida4 | 334, 346, 336, 445, 233, 033, 244, 559 | 33, 24, 23, 31, 13, 5, 15, 10 | - | - | shared_host | Combined:ALERT/3, Midday:WATCH/2, Evening:WATCH/2 |
| 4 | Indiana4 | 244, 066, 004, 669, 366, 006, 024, 003 | 31, 6, 18, 5, 12, 19, 9, 20 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/0 |
| 5 | Michigan4 | 668, 011, 001, 168, 344, 016, 599, 018 | 6, 18, 15, 2, 8, 35, 34, 31 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 778, 189, 088, 788, 078, 889, 188, 119 | 24, 27, 13, 4, 1, 33, 23, 8 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/0 |
| 7 | NewYork4 | 008, 001, 667, 066, 224, 005, 025, 016 | 6, 4, 2, 3, 18, 17, 5, 12 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 8 | NorthCarolina4 | 299, 244, 229, 224, 246, 006, 559, 446 | 31, 28, 25, 5, 22, 15, 19, 2 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 9 | Ohio4 | 559, 088, 299, 889, 599, 055, 788, 899 | 5, 13, 1, 31, 33, 10, 15, 3 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 10 | OntarioCanada4 | 559, 244, 015, 224, 246, 677, 066, 044 | 28, 5, 31, 20, 2, 22, 15, 21 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/0 |
| 11 | Pennsylvania4 | 000, 001, 009, 445, 455, 059, 559, 113 | 5, 17, 18, 15, 20, 2, 31, 9 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 12 | PuertoRico4 | 068, 006, 003, 244, 344, 245, 138 | 8, 23, 2, 4, 31, 18, 12, 10 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/1 |
| 13 | SouthCarolina4 | 599, 224, 399, 007, 005, 667, 559, 566 | 15, 28, 5, 11, 3, 17, 34, 31 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 14 | Virginia4 | 559, 224, 009, 024, 189, 001, 244, 134 | 5, 24, 12, 28, 31, 3, 25, 2 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/0 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 265 | 34 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 291 | 33 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 189 | 21 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 329 | 38 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 281 | 36 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 201 | 23 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 327 | 39 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 342 | 41 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 238 | 30 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 311 | 39 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Delaware4 | Florida4 | shared_box_family | lane/family | primary | - | 014, 033, 044, 334, 339, 348, 389, 445 | 8 | 13 | False | True |
| Virginia4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 2, 5 | 001, 009, 045, 059, 455, 559 | 6 | 12 | False | True |
| Florida4 | Delaware4 | alert_implied_echo | lane/family | primary | 13, 33 | 033, 334, 339, 348, 389 | 5 | 11 | False | True |
| Indiana4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 004, 006, 066, 244, 249, 299 | 6 | 11 | False | True |
| Michigan4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 006, 011, 016, 066, 566 | 6 | 11 | False | True |
| NewYork4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 007, 066, 245 | 6 | 11 | False | True |
| NewYork4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 224, 566, 667 | 6 | 11 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 009, 559, 599 | 6 | 11 | False | True |
| Florida4 | NewJersey4 | shared_lane | lane/family | primary | 13, 15, 23, 24, 29, 31, 33 | - | 7 | 11 | False | True |
| NewYork4 | SouthCarolina4 | shared_lane | lane/family | primary | 1, 12, 17, 18, 23, 28, 3 | - | 7 | 11 | False | True |
| NorthCarolina4 | OntarioCanada4 | shared_lane | lane/family | primary | 15, 18, 2, 22, 28, 31, 5 | - | 7 | 11 | False | True |
| Connecticut4 | Indiana4 | shared_box_family | lane/family | primary | - | 017, 244, 249, 299, 447 | 5 | 10 | False | True |
| Connecticut4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 224, 229, 244, 249, 299 | 5 | 10 | False | True |
| Connecticut4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 014, 017, 224, 229, 244 | 5 | 10 | False | True |
| Indiana4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 003, 004, 006, 066, 244 | 5 | 10 | False | True |
| NewJersey4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 007, 088, 788, 889 | 5 | 10 | False | True |
| NewYork4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 066, 224 | 5 | 10 | False | True |
| NorthCarolina4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 004, 224, 229, 244, 246 | 5 | 10 | False | True |
| Indiana4 | NewYork4 | shared_lane | lane/family | primary | 12, 17, 18, 2, 23, 6 | - | 6 | 10 | False | True |
| Indiana4 | PuertoRico4 | shared_lane | lane/family | primary | 12, 17, 18, 2, 23, 31 | - | 6 | 10 | False | True |
| Indiana4 | Virginia4 | shared_lane | lane/family | primary | 12, 18, 2, 23, 31, 5 | - | 6 | 10 | False | True |
| NewJersey4 | Ohio4 | shared_lane | lane/family | primary | 1, 12, 13, 15, 31, 33 | - | 6 | 10 | False | True |
| NewYork4 | PuertoRico4 | shared_lane | lane/family | primary | 12, 17, 18, 2, 23, 4 | - | 6 | 10 | False | True |
| Indiana4 | NorthCarolina4 | alert_implied_echo | lane/family | primary | 5, 31 | 004, 009, 244 | 3 | 9 | False | True |
| Indiana4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 5 | 009, 045, 059 | 3 | 9 | False | True |
| Michigan4 | NewYork4 | alert_implied_echo | lane/family | primary | 2, 6 | 001, 006, 016 | 3 | 9 | False | True |
| NorthCarolina4 | Indiana4 | alert_implied_echo | lane/family | primary | 6, 31 | 016, 066, 244 | 3 | 9 | False | True |
| NorthCarolina4 | Michigan4 | alert_implied_echo | lane/family | primary | 6 | 011, 016, 066 | 3 | 9 | False | True |
| NorthCarolina4 | NewYork4 | alert_implied_echo | lane/family | primary | 6 | 011, 016, 066 | 3 | 9 | False | True |
| NorthCarolina4 | OntarioCanada4 | alert_implied_echo | lane/family | primary | 6, 31, 22 | 011, 244, 246 | 3 | 9 | False | True |
| Pennsylvania4 | Ohio4 | alert_implied_echo | lane/family | primary | 5, 15 | 009, 059, 599 | 3 | 9 | False | True |
| Pennsylvania4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 5, 15 | 009, 445, 599 | 3 | 9 | False | True |
| PuertoRico4 | Indiana4 | alert_implied_echo | lane/family | primary | 4, 6 | 003, 016, 066 | 3 | 9 | False | True |
| PuertoRico4 | Michigan4 | alert_implied_echo | lane/family | primary | 6 | 011, 016, 066 | 3 | 9 | False | True |
| PuertoRico4 | NewYork4 | alert_implied_echo | lane/family | primary | 6 | 011, 016, 066 | 3 | 9 | False | True |
| Virginia4 | Ohio4 | alert_implied_echo | lane/family | primary | 5 | 009, 059, 559 | 3 | 9 | False | True |
| Indiana4 | NewYork4 | shared_box_family | lane/family | primary | - | 004, 006, 016, 066 | 4 | 9 | False | True |
| NewJersey4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 134, 148, 189 | 4 | 9 | False | True |
| NewYork4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 004, 011, 224 | 4 | 9 | False | True |
| NorthCarolina4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 006, 066, 244 | 4 | 9 | False | True |

## Strongest Overlap Pairs

- `Delaware4 ↔ Florida4` score=`40` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ PuertoRico4` score=`38` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ NorthCarolina4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ PuertoRico4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ OntarioCanada4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Pennsylvania4 ↔ Virginia4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ NewYork4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ PuertoRico4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ NewYork4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ NorthCarolina4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
