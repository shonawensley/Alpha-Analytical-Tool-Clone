# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-19

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `c41ef5f032ae402c`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 224, 113, 355, 559, 144, 344, 255, 133 | 18, 34, 5, 28, 24, 4, 25, 23 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 2 | Delaware4 | 099, 001, 069, 599, 229, 019, 066, 399 | 15, 9, 2, 5, 6, 34, 28, 35 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 3 | Florida4 | 006, 224, 244, 246, 114, 124, 146, 467 | 22, 28, 19, 2, 31, 3, 12, 18 | - | - | shared_host | Midday:WATCH/2, Evening:OFF/1, Combined:OFF/0 |
| 4 | Indiana4 | 559, 599, 455, 224, 145, 249, 024, 259 | 5, 15, 9, 12, 28, 31, 2, 8 | - | - | shared_host | Midday:OFF/1, Combined:OFF/0, Evening:OFF/0 |
| 5 | Michigan4 | 559, 001, 059, 009, 055, 557, 339, 004 | 5, 2, 15, 1, 3, 35, 20, 7 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 6 | NewJersey4 | 499, 559, 023, 013, 558, 199, 599, 049 | 5, 35, 25, 4, 15, 11, 3, 13 | - | - | shared_host | Evening:ALERT/3, Combined:WATCH/2, Midday:OFF/1 |
| 7 | NewYork4 | 036, 066, 366, 667, 035, 013, 559, 033 | 8, 6, 17, 18, 4, 5, 13, 2 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 8 | NorthCarolina4 | 299, 112, 117, 177, 889, 088, 178 | 17, 20, 31, 29, 28, 21, 18, 4 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:WATCH/2 |
| 9 | Ohio4 | 559, 006, 099, 259, 699, 004, 069, 024 | 5, 12, 9, 15, 35, 7, 25, 2 | - | - | shared_host | Midday:ALERT/3, Combined:OFF/1, Evening:OFF/1 |
| 10 | OntarioCanada4 | 368, 334, 223, 138, 455, 348, 344 | 23, 33, 27, 24, 5, 30, 34, 15 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/0 |
| 11 | Pennsylvania4 | 477, 067, 244, 478, 346, 677, 077 | 28, 31, 18, 30, 13, 3, 33, 10 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 12 | PuertoRico4 | 244, 006, 144, 029, 224, 445, 559, 229 | 31, 2, 12, 15, 25, 28, 10, 20 | - | - | shared_host | Combined:WATCH/2, Evening:OFF/1, Midday:OFF/0 |
| 13 | SouthCarolina4 | 344, 455, 559, 003, 355, 334, 236, 445 | 5, 34, 4, 31, 15, 14, 21, 33 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 14 | Virginia4 | 225, 255, 268, 559, 055, 224, 668, 259 | 10, 3, 21, 5, 1, 12, 23, 28 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/0 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 308 | 37 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 240 | 28 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 285 | 37 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 352 | 40 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 305 | 38 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 284 | 34 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 282 | 36 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 142 | 16 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 309 | 38 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 215 | 24 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 004, 007, 045, 059, 455, 559 | 7 | 12 | False | True |
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 009, 013, 019, 066, 069, 099 | 6 | 11 | False | True |
| Indiana4 | Michigan4 | alert_implied_echo | lane/family | primary | 5 | 045, 059, 455, 559 | 4 | 10 | False | True |
| NewYork4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 31 | 244, 299, 447, 479 | 4 | 10 | False | True |
| OntarioCanada4 | Florida4 | alert_implied_echo | lane/family | primary | 22 | 124, 147, 246, 467 | 4 | 10 | False | True |
| SouthCarolina4 | Indiana4 | alert_implied_echo | lane/family | primary | 5 | 045, 059, 455, 559 | 4 | 10 | False | True |
| SouthCarolina4 | Michigan4 | alert_implied_echo | lane/family | primary | 5 | 045, 059, 455, 559 | 4 | 10 | False | True |
| Connecticut4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 013, 344, 355, 559 | 5 | 10 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 009, 011, 013, 049 | 5 | 10 | False | True |
| Florida4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 006, 007, 224, 244 | 5 | 10 | False | True |
| Indiana4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 007, 224, 445 | 5 | 10 | False | True |
| Indiana4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 455, 559 | 5 | 10 | False | True |
| Michigan4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 009, 055, 455, 559 | 5 | 10 | False | True |
| Michigan4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 006, 009, 455, 559 | 5 | 10 | False | True |
| Michigan4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 007, 009, 455, 559 | 5 | 10 | False | True |
| NewJersey4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 009, 013, 455, 559 | 5 | 10 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 009, 013, 455, 559 | 5 | 10 | False | True |
| Pennsylvania4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 014, 017, 224, 244, 447 | 5 | 10 | False | True |
| Connecticut4 | NewJersey4 | shared_lane | lane/family | primary | 18, 23, 25, 33, 4, 5 | - | 6 | 10 | False | True |
| Delaware4 | Indiana4 | shared_lane | lane/family | primary | 15, 18, 23, 28, 5, 9 | - | 6 | 10 | False | True |
| Indiana4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 23, 24, 28, 31 | - | 6 | 10 | False | True |
| Indiana4 | PuertoRico4 | shared_lane | lane/family | primary | 12, 15, 23, 28, 31, 5 | - | 6 | 10 | False | True |
| NorthCarolina4 | Pennsylvania4 | shared_lane | lane/family | primary | 13, 18, 20, 23, 28, 31 | - | 6 | 10 | False | True |
| Ohio4 | PuertoRico4 | shared_lane | lane/family | primary | 12, 15, 2, 23, 25, 5 | - | 6 | 10 | False | True |
| Florida4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 2, 28 | 001, 006, 224 | 3 | 9 | False | True |
| Indiana4 | Ohio4 | alert_implied_echo | lane/family | primary | 12, 5 | 024, 455, 559 | 3 | 9 | False | True |
| Michigan4 | NewJersey4 | alert_implied_echo | lane/family | primary | 2, 5, 1 | 001, 009, 055 | 3 | 9 | False | True |
| NewYork4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 31 | 244, 249, 447 | 3 | 9 | False | True |
| Connecticut4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 014, 044, 113, 224 | 4 | 9 | False | True |
| Connecticut4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 014, 144, 224 | 4 | 9 | False | True |
| Indiana4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 005, 455, 559 | 4 | 9 | False | True |
| Indiana4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 024, 455, 559 | 4 | 9 | False | True |
| Indiana4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 024, 224, 559 | 4 | 9 | False | True |
| Michigan4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 007 | 4 | 9 | False | True |
| NewJersey4 | Ohio4 | shared_box_family | lane/family | primary | - | 009, 013, 455, 559 | 4 | 9 | False | True |
| NewJersey4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 013, 014, 455 | 4 | 9 | False | True |
| NewJersey4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 013, 055, 559 | 4 | 9 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 013, 334, 348, 455 | 4 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_lane | lane/family | primary | 18, 23, 28, 34, 5 | - | 5 | 9 | False | True |
| Connecticut4 | Indiana4 | shared_lane | lane/family | primary | 18, 23, 24, 28, 5 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `Delaware4 ↔ Ohio4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ PuertoRico4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Michigan4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ SouthCarolina4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Ohio4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ SouthCarolina4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ SouthCarolina4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ SouthCarolina4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ Ohio4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ NewJersey4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
