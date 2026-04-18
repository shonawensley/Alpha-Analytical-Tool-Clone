# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-15

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `f3121c8f08813a65`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 559, 689, 346, 044, 368, 344 | 24, 5, 23, 18, 25, 15, 34, 21 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 2 | Delaware4 | 559, 049, 599, 005, 007, 099, 239, 017 | 15, 5, 12, 35, 14, 3, 30, 1 | - | - | shared_host | Combined:WATCH/2, Evening:OFF/1, Midday:OFF/0 |
| 3 | Florida4 | 699, 224, 668, 006, 499, 469, 559, 126 | 25, 28, 10, 18, 35, 6, 19, 15 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:WATCH/2 |
| 4 | Indiana4 | 599, 224, 669, 005, 559, 667, 499, 299 | 15, 28, 31, 33, 27, 29, 34, 1 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 5 | Michigan4 | 455, 044, 008, 445, 088, 004, 688, 448 | 5, 15, 4, 3, 23, 14, 1, 35 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 244, 099, 004, 024, 167, 169 | 31, 15, 5, 28, 17, 35, 34, 25 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 7 | NewYork4 | 668, 039, 012, 559, 001, 003, 033, 002 | 18, 2, 14, 5, 3, 7, 21, 33 | - | - | shared_host | Midday:ALERT/3, Combined:OFF/1, Evening:OFF/1 |
| 8 | NorthCarolina4 | 388, 138, 368, 038, 003, 122, 036, 338 | 23, 8, 5, 29, 32, 13, 18, 4 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 9 | Ohio4 | 069, 099, 599, 338, 334, 449, 019, 299 | 15, 9, 35, 31, 32, 33, 34, 5 | - | - | shared_host | Midday:ALERT/3, Evening:OFF/1, Combined:OFF/0 |
| 10 | OntarioCanada4 | 449, 388, 368, 138, 223, 014, 238, 338 | 35, 23, 8, 21, 27, 29, 32, 31 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/0 |
| 11 | Pennsylvania4 | 366, 559, 244, 346, 224, 234, 259, 338 | 18, 5, 23, 19, 32, 31, 28, 8 | - | - | shared_host | Combined:OFF/1, Evening:OFF/1, Midday:OFF/0 |
| 12 | PuertoRico4 | 677, 445, 047, 224, 449, 077, 559, 067 | 20, 15, 12, 10, 28, 7, 35, 19 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 13 | SouthCarolina4 | 244, 559, 077, 344, 477, 022, 036, 003 | 10, 3, 5, 31, 2, 4, 28, 1 | - | - | shared_host | Evening:ALERT/3, Combined:WATCH/2, Midday:OFF/0 |
| 14 | Virginia4 | 559, 259, 599, 889, 688, 255, 002, 345 | 5, 12, 3, 15, 1, 23, 4, 32 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 281 | 35 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 383 | 45 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 209 | 25 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 336 | 38 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 294 | 36 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 344 | 40 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 249 | 31 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 233 | 27 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 288 | 35 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 278 | 33 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Indiana4 | NewJersey4 | shared_lane | lane/family | primary | 12, 15, 17, 18, 19, 23, 28, 31, 5 | - | 9 | 13 | False | True |
| NorthCarolina4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 004, 013, 068, 138, 368, 388 | 7 | 12 | False | True |
| Indiana4 | Pennsylvania4 | shared_lane | lane/family | primary | 12, 17, 18, 19, 23, 28, 31, 5 | - | 8 | 12 | False | True |
| NewJersey4 | Pennsylvania4 | shared_lane | lane/family | primary | 12, 17, 18, 19, 23, 28, 31, 5 | - | 8 | 12 | False | True |
| Delaware4 | Michigan4 | alert_implied_echo | lane/family | primary | 3, 5 | 007, 045, 059, 455, 559 | 5 | 11 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 005, 007, 008, 099, 559, 599 | 6 | 11 | False | True |
| Delaware4 | Michigan4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 008, 059, 559 | 6 | 11 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 005, 009, 014, 017, 099 | 6 | 11 | False | True |
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 009, 014, 049, 099, 599 | 6 | 11 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 007, 009, 014, 059, 559 | 6 | 11 | False | True |
| Delaware4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 017, 047, 599 | 6 | 11 | False | True |
| Delaware4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 005, 009, 059, 559, 599 | 6 | 11 | False | True |
| Michigan4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 059, 455, 559 | 6 | 11 | False | True |
| Virginia4 | Michigan4 | alert_implied_echo | lane/family | primary | 5 | 045, 059, 455, 559 | 4 | 10 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 005, 007, 008, 445, 559 | 5 | 10 | False | True |
| Indiana4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 005, 007, 224, 445, 599 | 5 | 10 | False | True |
| NewJersey4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 009, 014, 044, 099 | 5 | 10 | False | True |
| NewJersey4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 005, 017, 024, 445 | 5 | 10 | False | True |
| Ohio4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 004, 006, 014, 044, 449 | 5 | 10 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 007, 009, 244, 559 | 5 | 10 | False | True |
| Indiana4 | Virginia4 | shared_lane | lane/family | primary | 1, 12, 15, 23, 33, 5 | - | 6 | 10 | False | True |
| Delaware4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 3, 5 | 007, 059, 559 | 3 | 9 | False | True |
| Delaware4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 3, 7, 12 | 007, 017, 047 | 3 | 9 | False | True |
| Delaware4 | Virginia4 | alert_implied_echo | lane/family | primary | 5 | 059, 455, 559 | 3 | 9 | False | True |
| Indiana4 | NewJersey4 | alert_implied_echo | lane/family | primary | 1, 31, 15 | 005, 249, 445 | 3 | 9 | False | True |
| Indiana4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 1, 15 | 005, 445, 599 | 3 | 9 | False | True |
| OntarioCanada4 | Ohio4 | alert_implied_echo | lane/family | primary | 9, 15, 35 | 014, 044, 449 | 3 | 9 | False | True |
| Connecticut4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 013, 014, 044, 368 | 4 | 9 | False | True |
| Delaware4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 007, 009, 559 | 4 | 9 | False | True |
| Indiana4 | NewJersey4 | shared_box_family | lane/family | primary | - | 005, 099, 249, 445 | 4 | 9 | False | True |
| Indiana4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 007, 224, 559 | 4 | 9 | False | True |
| Michigan4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 005, 044, 445 | 4 | 9 | False | True |
| Michigan4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 004, 006, 044, 068 | 4 | 9 | False | True |
| Michigan4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 007, 059, 559 | 4 | 9 | False | True |
| Michigan4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 445 | 4 | 9 | False | True |
| Michigan4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 559 | 4 | 9 | False | True |
| NewJersey4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 009, 014, 244 | 4 | 9 | False | True |
| NewYork4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 136, 366, 559, 668 | 4 | 9 | False | True |
| Ohio4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 006, 009, 599 | 4 | 9 | False | True |
| Pennsylvania4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 009, 059, 559 | 4 | 9 | False | True |

## Strongest Overlap Pairs

- `Indiana4 ↔ NewJersey4` score=`39` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Michigan4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ PuertoRico4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Virginia4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Indiana4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ PuertoRico4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Pennsylvania4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ OntarioCanada4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NewJersey4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ PuertoRico4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
