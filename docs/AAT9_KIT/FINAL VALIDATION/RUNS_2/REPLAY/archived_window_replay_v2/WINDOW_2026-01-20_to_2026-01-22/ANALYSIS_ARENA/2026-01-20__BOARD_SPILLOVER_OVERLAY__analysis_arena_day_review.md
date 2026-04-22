# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-20

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `2f47bcc79e4bfdfe`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 006, 005, 255, 355, 568, 559, 668, 055 | 3, 2, 1, 4, 8, 5, 18, 15 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 2 | Delaware4 | 559, 259, 007, 003, 055, 579, 336, 255 | 5, 12, 15, 3, 4, 1, 2, 23 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/1 |
| 3 | Florida4 | 378, 255, 259, 778, 559, 599, 388, 238 | 29, 3, 27, 10, 32, 5, 33, 11 | - | - | shared_host | Midday:WATCH/2, Evening:OFF/1, Combined:OFF/0 |
| 4 | Indiana4 | 077, 224, 007, 017, 001, 038, 368, 037 | 10, 28, 23, 11, 3, 6, 18, 7 | - | - | shared_host | Midday:OFF/1, Evening:OFF/1, Combined:OFF/0 |
| 5 | Michigan4 | 224, 778, 007, 559, 027, 017, 277 | 28, 10, 27, 17, 3, 26, 20, 7 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 001, 559, 004, 019, 009, 014, 348, 016 | 5, 9, 2, 33, 12, 13, 6, 26 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 7 | NewYork4 | 378, 377, 113, 337, 177, 133, 368, 115 | 29, 18, 27, 23, 10, 21, 17, 6 | - | - | shared_host | Combined:WATCH/2, Evening:OFF/1, Midday:OFF/0 |
| 8 | NorthCarolina4 | 778, 244, 368, 225, 257, 024, 006, 004 | 27, 31, 10, 12, 23, 2, 18, 3 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/0 |
| 9 | Ohio4 | 077, 008, 009, 004, 049, 007, 045, 244 | 5, 10, 15, 3, 31, 4, 35, 14 | - | - | shared_host | Evening:ALERT/3, Combined:WATCH/2, Midday:WATCH/2 |
| 10 | OntarioCanada4 | 244, 044, 236, 001, 446, 268, 344, 004 | 31, 21, 15, 5, 25, 34, 2, 23 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 11 | Pennsylvania4 | 344, 003, 034, 000, 599, 559, 224, 004 | 34, 15, 4, 5, 33, 32, 18, 24 | - | - | shared_host | Midday:WATCH/2, Evening:OFF/1, Combined:OFF/0 |
| 12 | PuertoRico4 | 334, 336, 013, 144, 244, 138, 455, 114 | 23, 18, 33, 8, 5, 24, 19, 31 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 13 | SouthCarolina4 | 005, 009, 599, 339, 067, 099, 015, 007 | 5, 15, 1, 3, 2, 17, 31, 33 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 14 | Virginia4 | 339, 133, 013, 002, 559, 001, 334, 033 | 33, 23, 8, 6, 2, 5, 3, 7 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/0 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 270 | 30 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 274 | 33 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 264 | 33 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 306 | 36 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 256 | 33 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 315 | 37 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 223 | 28 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 199 | 26 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 270 | 34 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 252 | 32 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 007, 011, 014, 017, 077, 224, 225, 229 | 9 | 14 | False | True |
| PuertoRico4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 006, 013, 133, 138, 334, 336 | 7 | 12 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 059, 455, 559 | 6 | 11 | False | True |
| NewJersey4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 006, 009, 013, 348, 559 | 6 | 11 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 003, 005, 007, 009, 559, 599 | 6 | 11 | False | True |
| OntarioCanada4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 25, 31, 5 | - | 7 | 11 | False | True |
| Virginia4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 8, 23 | 013, 133, 138, 188 | 4 | 10 | False | True |
| Connecticut4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 099, 559 | 5 | 10 | False | True |
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 007, 009, 045, 059 | 5 | 10 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 003, 004, 007, 009, 559 | 5 | 10 | False | True |
| Delaware4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 003, 007, 009, 059, 559 | 5 | 10 | False | True |
| OntarioCanada4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 244, 368 | 5 | 10 | False | True |
| Connecticut4 | Delaware4 | shared_lane | lane/family | primary | 1, 12, 23, 3, 4, 5 | - | 6 | 10 | False | True |
| Connecticut4 | SouthCarolina4 | shared_lane | lane/family | primary | 1, 2, 23, 3, 33, 5 | - | 6 | 10 | False | True |
| Connecticut4 | Virginia4 | shared_lane | lane/family | primary | 2, 23, 3, 33, 5, 8 | - | 6 | 10 | False | True |
| Florida4 | NewYork4 | shared_lane | lane/family | primary | 10, 12, 21, 23, 27, 29 | - | 6 | 10 | False | True |
| Indiana4 | SouthCarolina4 | shared_lane | lane/family | primary | 15, 2, 23, 3, 33, 7 | - | 6 | 10 | False | True |
| NewJersey4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 33, 5 | - | 6 | 10 | False | True |
| Ohio4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 31, 33, 34, 4, 5 | - | 6 | 10 | False | True |
| PuertoRico4 | SouthCarolina4 | shared_lane | lane/family | primary | 15, 2, 23, 31, 33, 5 | - | 6 | 10 | False | True |
| PuertoRico4 | Virginia4 | shared_lane | lane/family | primary | 18, 2, 23, 33, 5, 8 | - | 6 | 10 | False | True |
| NewYork4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 15 | 099, 459, 599 | 3 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_box_family | lane/family | primary | - | 001, 004, 007, 559 | 4 | 9 | False | True |
| Connecticut4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 559 | 4 | 9 | False | True |
| Connecticut4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 004, 005, 006 | 4 | 9 | False | True |
| Connecticut4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 559 | 4 | 9 | False | True |
| Delaware4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 007, 259, 559 | 4 | 9 | False | True |
| Florida4 | Michigan4 | shared_box_family | lane/family | primary | - | 007, 259, 559, 778 | 4 | 9 | False | True |
| Florida4 | NewYork4 | shared_box_family | lane/family | primary | - | 133, 177, 238, 378 | 4 | 9 | False | True |
| Indiana4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 006, 011, 368 | 4 | 9 | False | True |
| NewJersey4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 006, 009, 059 | 4 | 9 | False | True |
| NewJersey4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 013 | 4 | 9 | False | True |
| NewJersey4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 009, 059, 559 | 4 | 9 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 007, 009, 059 | 4 | 9 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 006, 009, 339, 559 | 4 | 9 | False | True |
| Connecticut4 | NewJersey4 | shared_lane | lane/family | primary | 12, 2, 23, 33, 5 | - | 5 | 9 | False | True |
| Connecticut4 | PuertoRico4 | shared_lane | lane/family | primary | 2, 23, 33, 5, 8 | - | 5 | 9 | False | True |
| Delaware4 | Florida4 | shared_lane | lane/family | primary | 12, 15, 23, 3, 5 | - | 5 | 9 | False | True |
| Delaware4 | SouthCarolina4 | shared_lane | lane/family | primary | 1, 15, 23, 3, 5 | - | 5 | 9 | False | True |
| Florida4 | Michigan4 | shared_lane | lane/family | primary | 10, 12, 27, 3, 5 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `PuertoRico4 ↔ Virginia4` score=`40` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Michigan4` score=`38` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Virginia4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ NewYork4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ PuertoRico4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `SouthCarolina4 ↔ Virginia4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Pennsylvania4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ Michigan4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Michigan4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Pennsylvania4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
