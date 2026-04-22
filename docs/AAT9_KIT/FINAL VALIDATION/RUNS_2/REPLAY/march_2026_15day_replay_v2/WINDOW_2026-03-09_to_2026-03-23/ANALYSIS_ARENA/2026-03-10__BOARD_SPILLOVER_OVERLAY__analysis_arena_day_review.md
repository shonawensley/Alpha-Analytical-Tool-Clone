# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-10

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `162ea25d4e474ad3`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 168, 006, 368, 668, 068, 688, 189, 099 | 18, 23, 8, 15, 21, 24, 2, 32 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 2 | Delaware4 | 599, 117, 129, 006, 119, 224, 344, 047 | 12, 15, 7, 22, 17, 28, 24, 35 | - | - | shared_host | Combined:WATCH/2, Evening:OFF/0, Midday:OFF/0 |
| 3 | Florida4 | 224, 778, 066, 077, 004, 046, 048, 559 | 28, 10, 27, 6, 15, 5, 25, 9 | - | - | shared_host | Combined:ALERT/3, Midday:WATCH/2, Evening:WATCH/2 |
| 4 | Indiana4 | 255, 027, 113, 088, 225, 078, 559, 788 | 3, 10, 11, 27, 13, 18, 6, 17 | - | - | shared_host | Evening:WATCH/2, Midday:OFF/1, Combined:OFF/0 |
| 5 | Michigan4 | 224, 778, 118, 245, 559, 188, 334, 378 | 23, 28, 27, 12, 18, 29, 33, 5 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/0 |
| 6 | NewJersey4 | 009, 459, 117, 006, 177, 007, 559 | 5, 15, 17, 20, 9, 31, 2, 28 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 7 | NewYork4 | 559, 368, 224, 599, 269, 136, 336 | 5, 23, 28, 15, 18, 32, 21, 6 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/0 |
| 8 | NorthCarolina4 | 344, 003, 188, 034, 299, 099, 007, 009 | 15, 34, 4, 31, 5, 23, 14, 18 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 9 | Ohio4 | 003, 599, 069, 559, 569, 224, 002, 113 | 9, 4, 5, 15, 3, 28, 18, 13 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 10 | OntarioCanada4 | 189, 077, 449, 559, 049, 014, 244 | 31, 15, 28, 35, 25, 24, 5, 10 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/0 |
| 11 | Pennsylvania4 | 559, 008, 024, 002, 224, 288, 058, 388 | 5, 4, 3, 12, 1, 32, 29, 11 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 12 | PuertoRico4 | 559, 117, 359, 339, 557, 179, 599, 449 | 5, 17, 14, 19, 33, 15, 3, 22 | - | - | shared_host | Combined:ALERT/3, Midday:WATCH/2, Evening:WATCH/2 |
| 13 | SouthCarolina4 | 667, 069, 669, 224, 299, 778, 066 | 17, 9, 19, 7, 28, 20, 31, 12 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/1 |
| 14 | Virginia4 | 599, 039, 559, 009, 059, 005, 138, 339 | 15, 5, 14, 1, 8, 23, 4, 33 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 253 | 33 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 272 | 34 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 245 | 30 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 184 | 24 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 300 | 37 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 321 | 38 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 344 | 41 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 257 | 30 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 358 | 42 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 283 | 34 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Connecticut4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 006, 011, 017, 188, 368, 688 | 7 | 12 | False | True |
| NewJersey4 | NewYork4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 009, 059, 455, 559 | 7 | 12 | False | True |
| NewYork4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 005, 007, 009, 059, 224, 559 | 7 | 12 | False | True |
| NewYork4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 059, 138, 559, 599 | 7 | 12 | False | True |
| NorthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 099, 445, 459, 599 | 7 | 12 | False | True |
| NewJersey4 | NorthCarolina4 | alert_implied_echo | lane/family | primary | 1, 5, 15 | 005, 009, 445, 459, 599 | 5 | 11 | False | True |
| NewJersey4 | Virginia4 | alert_implied_echo | lane/family | primary | 1, 5, 15 | 005, 009, 445, 459, 599 | 5 | 11 | False | True |
| Michigan4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 006, 138, 224, 368, 559 | 6 | 11 | False | True |
| NewJersey4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 009, 059, 559 | 6 | 11 | False | True |
| NewJersey4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 009, 069, 117 | 6 | 11 | False | True |
| Delaware4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 17, 18, 19, 23, 28, 7 | - | 7 | 11 | False | True |
| Florida4 | OntarioCanada4 | shared_lane | lane/family | primary | 10, 15, 23, 28, 33, 5, 9 | - | 7 | 11 | False | True |
| Ohio4 | Pennsylvania4 | shared_lane | lane/family | primary | 12, 15, 23, 28, 3, 4, 5 | - | 7 | 11 | False | True |
| Virginia4 | NewJersey4 | alert_implied_echo | lane/family | primary | 5 | 004, 009, 045, 059 | 4 | 10 | False | True |
| Delaware4 | Michigan4 | shared_box_family | lane/family | primary | - | 006, 011, 017, 224, 245 | 5 | 10 | False | True |
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 224, 599 | 5 | 10 | False | True |
| Indiana4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 002, 005, 007, 008 | 5 | 10 | False | True |
| NewJersey4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 009, 059, 459, 559 | 5 | 10 | False | True |
| NewYork4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 001, 005, 007, 009, 599 | 5 | 10 | False | True |
| NewYork4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 009, 224 | 5 | 10 | False | True |
| Ohio4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 013, 014, 017, 019, 559 | 5 | 10 | False | True |
| Pennsylvania4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 059, 559 | 5 | 10 | False | True |
| Delaware4 | NewYork4 | shared_lane | lane/family | primary | 12, 15, 18, 22, 23, 28 | - | 6 | 10 | False | True |
| Michigan4 | NewYork4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 28, 5 | - | 6 | 10 | False | True |
| Michigan4 | Ohio4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 28, 5 | - | 6 | 10 | False | True |
| NewJersey4 | Ohio4 | shared_lane | lane/family | primary | 12, 15, 28, 3, 5, 9 | - | 6 | 10 | False | True |
| NewYork4 | Ohio4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 28, 5 | - | 6 | 10 | False | True |
| Ohio4 | OntarioCanada4 | shared_lane | lane/family | primary | 15, 18, 23, 28, 5, 9 | - | 6 | 10 | False | True |
| NewJersey4 | NewYork4 | alert_implied_echo | lane/family | primary | 1, 5, 15 | 005, 009, 599 | 3 | 9 | False | True |
| NewJersey4 | Ohio4 | alert_implied_echo | lane/family | primary | 5, 9, 15 | 009, 069, 599 | 3 | 9 | False | True |
| NewJersey4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 1, 5, 9 | 005, 009, 069 | 3 | 9 | False | True |
| Virginia4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 5 | 004, 009, 059 | 3 | 9 | False | True |
| Florida4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 224, 477, 778 | 4 | 9 | False | True |
| Florida4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 014, 046, 224 | 4 | 9 | False | True |
| Michigan4 | Ohio4 | shared_box_family | lane/family | primary | - | 011, 017, 224, 559 | 4 | 9 | False | True |
| NewJersey4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 005, 007, 009, 459 | 4 | 9 | False | True |
| NewJersey4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 009, 069, 559 | 4 | 9 | False | True |
| NewYork4 | Ohio4 | shared_box_family | lane/family | primary | - | 009, 224, 559, 599 | 4 | 9 | False | True |
| NorthCarolina4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 005, 007, 009 | 4 | 9 | False | True |
| NorthCarolina4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 007, 009, 299 | 4 | 9 | False | True |

## Strongest Overlap Pairs

- `NewJersey4 ↔ Virginia4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ NewYork4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ NewYork4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Ohio4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Pennsylvania4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ SouthCarolina4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ Pennsylvania4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ Virginia4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Pennsylvania4 ↔ Virginia4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Michigan4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
