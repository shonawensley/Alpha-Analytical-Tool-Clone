# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-16

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `4025127909ad0e9b`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 899, 599, 389, 089, 559, 299, 889 | 34, 15, 33, 14, 31, 30, 5, 32 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 2 | Delaware4 | 009, 249, 059, 017, 559, 177, 299, 259 | 5, 31, 15, 14, 12, 35, 7, 17 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/0 |
| 3 | Florida4 | 225, 577, 255, 177, 178, 377, 223, 257 | 10, 27, 20, 3, 5, 11, 32, 26 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 4 | Indiana4 | 368, 599, 366, 077, 339, 559, 459, 066 | 23, 18, 15, 6, 33, 8, 5, 10 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 5 | Michigan4 | 344, 245, 559, 114, 011, 255, 014, 115 | 12, 6, 34, 2, 5, 17, 8, 19 | - | - | shared_host | Midday:ALERT/3, Combined:OFF/1, Evening:OFF/0 |
| 6 | NewJersey4 | 001, 008, 019, 179, 018, 136, 088, 449 | 18, 9, 4, 13, 8, 35, 2, 22 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/0 |
| 7 | NewYork4 | 337, 377, 334, 336, 009, 677, 338 | 29, 23, 33, 27, 12, 15, 21, 18 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 8 | NorthCarolina4 | 224, 344, 255, 244, 000, 225, 348, 278 | 28, 34, 27, 3, 15, 5, 31, 10 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 9 | Ohio4 | 599, 009, 049, 677, 349, 499 | 15, 5, 34, 14, 35, 20, 23, 3 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 10 | OntarioCanada4 | 003, 039, 049, 044, 255, 336, 223 | 15, 14, 4, 10, 12, 5, 3, 1 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 11 | Pennsylvania4 | 244, 344, 044, 689, 446, 889, 003, 249 | 31, 34, 15, 24, 25, 23, 33, 35 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:WATCH/2 |
| 12 | PuertoRico4 | 244, 334, 224, 024, 014, 018, 088, 004 | 31, 33, 8, 28, 12, 23, 5, 13 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/0 |
| 13 | SouthCarolina4 | 677, 678, 014, 067, 255, 005, 006, 344 | 9, 5, 3, 21, 20, 7, 1, 31 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 14 | Virginia4 | 449, 599, 033, 559, 339, 459, 335, 259 | 15, 35, 5, 13, 25, 33, 12, 23 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 234 | 29 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 320 | 39 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 156 | 19 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 278 | 31 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 258 | 32 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 205 | 24 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 346 | 43 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 301 | 38 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 264 | 31 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 306 | 37 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Indiana4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 006, 009, 133, 336, 368 | 6 | 11 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 001, 009, 013, 559, 599 | 5 | 10 | False | True |
| Delaware4 | Virginia4 | shared_box_family | lane/family | primary | - | 013, 017, 059, 559, 599 | 5 | 10 | False | True |
| NewYork4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 014, 334 | 5 | 10 | False | True |
| Ohio4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 004, 009, 049, 459, 599 | 5 | 10 | False | True |
| OntarioCanada4 | Virginia4 | shared_box_family | lane/family | primary | - | 011, 049, 445, 459, 599 | 5 | 10 | False | True |
| Pennsylvania4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 006, 244, 299, 889 | 5 | 10 | False | True |
| Connecticut4 | Ohio4 | shared_lane | lane/family | primary | 14, 15, 23, 33, 34, 5 | - | 6 | 10 | False | True |
| Pennsylvania4 | Virginia4 | shared_lane | lane/family | primary | 15, 23, 24, 25, 31, 33 | - | 6 | 10 | False | True |
| Delaware4 | Ohio4 | alert_implied_echo | lane/family | primary | 5, 15 | 004, 009, 599 | 3 | 9 | False | True |
| Delaware4 | OntarioCanada4 | alert_implied_echo | lane/family | primary | 5, 15 | 004, 009, 599 | 3 | 9 | False | True |
| NewYork4 | NewJersey4 | alert_implied_echo | lane/family | primary | 2, 9 | 001, 014, 019 | 3 | 9 | False | True |
| Pennsylvania4 | Connecticut4 | alert_implied_echo | lane/family | primary | 15, 34 | 044, 349, 399 | 3 | 9 | False | True |
| Virginia4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 5 | 059, 455, 559 | 3 | 9 | False | True |
| Connecticut4 | Ohio4 | shared_box_family | lane/family | primary | - | 034, 349, 459, 599 | 4 | 9 | False | True |
| Delaware4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 017 | 4 | 9 | False | True |
| Delaware4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 599 | 4 | 9 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 009, 249, 299 | 4 | 9 | False | True |
| Delaware4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 013, 299 | 4 | 9 | False | True |
| Delaware4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 007, 059, 559 | 4 | 9 | False | True |
| Florida4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 177, 178, 225, 255 | 4 | 9 | False | True |
| Indiana4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 009, 336, 599 | 4 | 9 | False | True |
| Indiana4 | Virginia4 | shared_box_family | lane/family | primary | - | 013, 339, 559, 599 | 4 | 9 | False | True |
| Michigan4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 011, 044, 255 | 4 | 9 | False | True |
| Michigan4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 014, 255, 559 | 4 | 9 | False | True |
| NewJersey4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 014, 018, 088 | 4 | 9 | False | True |
| NewYork4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 006, 009, 677 | 4 | 9 | False | True |
| NewYork4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 336 | 4 | 9 | False | True |
| NewYork4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 006, 014, 677 | 4 | 9 | False | True |
| NorthCarolina4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 244, 344, 489 | 4 | 9 | False | True |
| NorthCarolina4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 224, 244 | 4 | 9 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 677 | 4 | 9 | False | True |
| Ohio4 | Virginia4 | shared_box_family | lane/family | primary | - | 049, 099, 459, 599 | 4 | 9 | False | True |
| PuertoRico4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 014 | 4 | 9 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 014, 059, 455, 559 | 4 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_lane | lane/family | primary | 14, 15, 31, 33, 5 | - | 5 | 9 | False | True |
| Connecticut4 | NorthCarolina4 | shared_lane | lane/family | primary | 15, 23, 31, 33, 34 | - | 5 | 9 | False | True |
| Connecticut4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 23, 31, 33, 34 | - | 5 | 9 | False | True |
| Connecticut4 | Virginia4 | shared_lane | lane/family | primary | 15, 23, 31, 33, 5 | - | 5 | 9 | False | True |
| Delaware4 | Ohio4 | shared_lane | lane/family | primary | 14, 15, 20, 33, 5 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `Delaware4 ↔ Virginia4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ NewYork4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ SouthCarolina4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NewYork4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ PuertoRico4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ SouthCarolina4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Virginia4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ OntarioCanada4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ Pennsylvania4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `SouthCarolina4 ↔ Virginia4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
