# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-23

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `e22a4735ab0d6f8a`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 113, 025, 117, 114, 003, 112, 224, 225 | 18, 17, 3, 19, 23, 10, 21, 4 | - | - | shared_host | Evening:ALERT/3, Combined:WATCH/2, Midday:WATCH/2 |
| 2 | Delaware4 | 011, 001, 038, 599, 116, 006 | 2, 6, 13, 16, 15, 18, 4, 5 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 3 | Florida4 | 224, 066, 114, 244, 124, 118, 012 | 19, 31, 28, 18, 12, 22, 6, 7 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/0 |
| 4 | Indiana4 | 559, 259, 004, 002, 001, 677, 455, 005 | 5, 12, 3, 2, 31, 1, 22, 28 | - | - | shared_host | Combined:WATCH/2, Evening:OFF/1, Midday:OFF/0 |
| 5 | Michigan4 | 344, 445, 055, 144, 244, 559, 001, 013 | 15, 25, 1, 5, 31, 2, 34, 35 | - | - | shared_host | Combined:ALERT/4, Evening:WATCH/2, Midday:OFF/1 |
| 6 | NewJersey4 | 244, 344, 001, 014, 005, 455, 149 | 5, 1, 2, 31, 25, 34, 15, 9 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 7 | NewYork4 | 066, 667, 006, 366, 668, 466, 136, 336 | 6, 18, 23, 17, 2, 33, 19, 21 | - | - | shared_host | Combined:ALERT/3, Midday:OFF/1, Evening:OFF/1 |
| 8 | NorthCarolina4 | 499, 889, 599, 116, 449, 489, 119 | 35, 15, 33, 34, 16, 24, 17, 19 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 9 | Ohio4 | 224, 667, 128, 002, 012, 011, 168, 266 | 28, 17, 21, 7, 3, 18, 31, 12 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 10 | OntarioCanada4 | 559, 368, 055, 077, 677, 599, 577, 257 | 5, 1, 23, 10, 3, 15, 13, 4 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 11 | Pennsylvania4 | 448, 449, 446, 044, 244, 468, 344, 477 | 34, 35, 31, 25, 24, 15, 33, 28 | - | - | shared_host | Combined:ALERT/3, Evening:OFF/1, Midday:OFF/0 |
| 12 | PuertoRico4 | 338, 224, 244, 007, 368, 788 | 32, 28, 23, 31, 3, 29, 21, 13 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 13 | SouthCarolina4 | 559, 255, 055, 558, 568, 455, 557, 577 | 5, 3, 2, 1, 4, 8, 23, 10 | - | - | shared_host | Evening:ALERT/3, Combined:WATCH/2, Midday:OFF/1 |
| 14 | Virginia4 | 225, 559, 133, 003, 038, 259, 255, 235 | 10, 23, 4, 5, 11, 3, 32, 8 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 212 | 27 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 280 | 37 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 230 | 29 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 270 | 36 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 290 | 36 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 319 | 39 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 259 | 33 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 187 | 24 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 244 | 30 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 289 | 34 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Indiana4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 004, 005, 014, 455, 559 | 6 | 11 | False | True |
| Indiana4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 005, 017, 055, 455, 559, 677 | 6 | 11 | False | True |
| NewJersey4 | Delaware4 | alert_implied_echo | lane/family | primary | 2 | 001, 006, 015, 056 | 4 | 10 | False | True |
| NewYork4 | Florida4 | alert_implied_echo | lane/family | primary | 6, 19 | 066, 146, 169, 466 | 4 | 10 | False | True |
| OntarioCanada4 | NewJersey4 | alert_implied_echo | lane/family | primary | 5 | 045, 059, 455, 559 | 4 | 10 | False | True |
| Connecticut4 | Florida4 | shared_box_family | lane/family | primary | - | 001, 004, 011, 114, 118 | 5 | 10 | False | True |
| Florida4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 011, 244 | 5 | 10 | False | True |
| Indiana4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 005, 055, 455, 559 | 5 | 10 | False | True |
| Indiana4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 014, 017, 259, 559 | 5 | 10 | False | True |
| Michigan4 | NewJersey4 | shared_box_family | lane/family | primary | - | 011, 014, 244, 344, 559 | 5 | 10 | False | True |
| Michigan4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 014, 017, 044, 244, 344 | 5 | 10 | False | True |
| NewJersey4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 005, 045, 455, 559 | 5 | 10 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 007, 055, 455, 559 | 5 | 10 | False | True |
| Michigan4 | NewJersey4 | shared_lane | lane/family | primary | 1, 15, 25, 31, 34, 5 | - | 6 | 10 | False | True |
| NorthCarolina4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 23, 31, 34, 35 | - | 6 | 10 | False | True |
| OntarioCanada4 | Indiana4 | alert_implied_echo | lane/family | primary | 5, 20 | 455, 559, 677 | 3 | 9 | False | True |
| OntarioCanada4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 5 | 045, 455, 559 | 3 | 9 | False | True |
| Florida4 | Ohio4 | shared_box_family | lane/family | primary | - | 001, 011, 012, 224 | 4 | 9 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 014, 017, 055, 559 | 4 | 9 | False | True |
| Michigan4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 011, 044, 445, 599 | 4 | 9 | False | True |
| Michigan4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 017, 055, 559, 599 | 4 | 9 | False | True |
| Michigan4 | Virginia4 | shared_box_family | lane/family | primary | - | 013, 014, 017, 559 | 4 | 9 | False | True |
| NewJersey4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 005, 059, 455, 559 | 4 | 9 | False | True |
| OntarioCanada4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 006, 007, 017, 368 | 4 | 9 | False | True |
| Connecticut4 | SouthCarolina4 | shared_lane | lane/family | primary | 17, 18, 23, 3, 4 | - | 5 | 9 | False | True |
| Florida4 | NewYork4 | shared_lane | lane/family | primary | 17, 18, 19, 22, 6 | - | 5 | 9 | False | True |
| Michigan4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 25, 31, 34 | - | 5 | 9 | False | True |
| NewJersey4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 23, 25, 31, 34 | - | 5 | 9 | False | True |
| Indiana4 | Virginia4 | alert_implied_echo | lane/family | primary | 1, 12 | 005, 259 | 2 | 8 | False | True |
| NewYork4 | Delaware4 | alert_implied_echo | lane/family | primary | 2, 6 | 006, 066 | 2 | 8 | False | True |
| Ohio4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 9 | 014, 019 | 2 | 8 | False | True |
| Pennsylvania4 | NorthCarolina4 | alert_implied_echo | lane/family | primary | 15, 34 | 044, 489 | 2 | 8 | False | True |
| PuertoRico4 | OntarioCanada4 | alert_implied_echo | lane/family | primary | 3, 23 | 007, 368 | 2 | 8 | False | True |
| Virginia4 | Delaware4 | alert_implied_echo | lane/family | primary | 1, 13 | 005, 038 | 2 | 8 | False | True |
| Connecticut4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 004, 011 | 3 | 8 | False | True |
| Connecticut4 | NewYork4 | shared_box_family | lane/family | primary | - | 011, 366, 668 | 3 | 8 | False | True |
| Connecticut4 | Ohio4 | shared_box_family | lane/family | primary | - | 001, 011, 266 | 3 | 8 | False | True |
| Connecticut4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 003, 004, 007 | 3 | 8 | False | True |
| Connecticut4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 007, 118 | 3 | 8 | False | True |
| Delaware4 | Florida4 | shared_box_family | lane/family | primary | - | 001, 011, 066 | 3 | 8 | False | True |

## Strongest Overlap Pairs

- `Indiana4 ↔ OntarioCanada4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ OntarioCanada4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `OntarioCanada4 ↔ SouthCarolina4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ Pennsylvania4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NewJersey4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ NewJersey4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ SouthCarolina4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Virginia4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `OntarioCanada4 ↔ PuertoRico4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ NewJersey4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
