# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-13

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `8206b5eaf3a06ad2`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 368, 668, 336, 559, 346, 066, 169, 069 | 23, 18, 24, 6, 9, 19, 15, 35 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 2 | Delaware4 | 499, 559, 005, 249, 007, 009, 259, 047 | 12, 5, 35, 31, 15, 22, 1, 28 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 3 | Florida4 | 224, 499, 226, 022, 024, 255, 267, 077 | 28, 20, 10, 35, 12, 25, 31, 22 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 4 | Indiana4 | 599, 788, 005, 889, 689, 117, 255 | 29, 15, 33, 24, 1, 6, 26, 27 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 5 | Michigan4 | 688, 455, 559, 008, 088, 459, 488 | 5, 23, 4, 15, 33, 13, 35, 14 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 244, 004, 167, 044, 446, 177, 667 | 31, 17, 5, 20, 15, 12, 19, 35 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:WATCH/2 |
| 7 | NewYork4 | 224, 039, 006, 559, 566, 668, 339, 336 | 5, 18, 28, 23, 2, 14, 6, 33 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/0 |
| 8 | NorthCarolina4 | 009, 388, 366, 368, 134, 003, 344 | 23, 5, 24, 18, 32, 8, 33, 4 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 9 | Ohio4 | 033, 338, 003, 599, 059, 069, 244, 334 | 13, 5, 15, 4, 32, 14, 31, 33 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:WATCH/2 |
| 10 | OntarioCanada4 | 449, 388, 049, 224, 688, 238, 008, 088 | 15, 35, 28, 31, 32, 13, 4, 29 | - | - | shared_host | Combined:OFF/1, Evening:OFF/1, Midday:OFF/0 |
| 11 | Pennsylvania4 | 559, 224, 003, 013, 233, 005, 259, 338 | 5, 29, 12, 4, 32, 3, 33, 28 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 12 | PuertoRico4 | 677, 559, 449, 066, 056, 114, 459, 077 | 5, 35, 20, 6, 19, 15, 17, 2 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 13 | SouthCarolina4 | 559, 029, 009, 226, 077, 027, 026, 255 | 5, 10, 20, 12, 7, 3, 31, 17 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 14 | Virginia4 | 559, 599, 259, 009, 059, 055, 299, 005 | 5, 15, 12, 1, 31, 2, 3, 14 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 233 | 30 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 325 | 39 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 239 | 30 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 270 | 32 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 277 | 34 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 264 | 32 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 288 | 35 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 240 | 30 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 308 | 37 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 271 | 33 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Florida4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 006, 007, 009, 022, 077, 226 | 7 | 12 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 007, 009, 024, 259, 559 | 6 | 11 | False | True |
| Delaware4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 005, 007, 017, 114, 499, 559 | 6 | 11 | False | True |
| Michigan4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 009, 059, 559 | 6 | 11 | False | True |
| Michigan4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 009, 059, 559 | 6 | 11 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 009, 059, 559 | 6 | 11 | False | True |
| Virginia4 | Michigan4 | alert_implied_echo | lane/family | primary | 5 | 045, 059, 455, 559 | 4 | 10 | False | True |
| Delaware4 | Michigan4 | shared_box_family | lane/family | primary | - | 005, 009, 014, 059, 559 | 5 | 10 | False | True |
| Delaware4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 007, 009, 059, 559 | 5 | 10 | False | True |
| Delaware4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 009, 059, 259, 559 | 5 | 10 | False | True |
| Ohio4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 059, 599 | 5 | 10 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 007, 009, 029, 559 | 5 | 10 | False | True |
| Pennsylvania4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 259, 559 | 5 | 10 | False | True |
| Delaware4 | Virginia4 | shared_lane | lane/family | primary | 1, 12, 15, 23, 31, 5 | - | 6 | 10 | False | True |
| Ohio4 | Pennsylvania4 | shared_lane | lane/family | primary | 12, 15, 23, 32, 4, 5 | - | 6 | 10 | False | True |
| OntarioCanada4 | Pennsylvania4 | shared_lane | lane/family | primary | 12, 15, 23, 28, 29, 32 | - | 6 | 10 | False | True |
| OntarioCanada4 | Ohio4 | alert_implied_echo | lane/family | primary | 13, 15, 9 | 038, 049, 069 | 3 | 9 | False | True |
| PuertoRico4 | Florida4 | alert_implied_echo | lane/family | primary | 20 | 226, 267, 677 | 3 | 9 | False | True |
| Virginia4 | NewYork4 | alert_implied_echo | lane/family | primary | 5 | 059, 455, 559 | 3 | 9 | False | True |
| Virginia4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 5 | 045, 455, 559 | 3 | 9 | False | True |
| Connecticut4 | NewYork4 | shared_box_family | lane/family | primary | - | 136, 366, 559, 668 | 4 | 9 | False | True |
| Delaware4 | Florida4 | shared_box_family | lane/family | primary | - | 007, 009, 024, 499 | 4 | 9 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 005, 007, 117, 559 | 4 | 9 | False | True |
| Florida4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 006, 009, 024 | 4 | 9 | False | True |
| Florida4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 007, 009, 024, 224 | 4 | 9 | False | True |
| Michigan4 | NewYork4 | shared_box_family | lane/family | primary | - | 006, 059, 455, 559 | 4 | 9 | False | True |
| Michigan4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 004, 009, 188, 688 | 4 | 9 | False | True |
| Michigan4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 009, 045, 559 | 4 | 9 | False | True |
| Michigan4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 005, 045, 455, 559 | 4 | 9 | False | True |
| NewYork4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 059, 226, 559 | 4 | 9 | False | True |
| NorthCarolina4 | Ohio4 | shared_box_family | lane/family | primary | - | 001, 003, 004, 009 | 4 | 9 | False | True |
| NorthCarolina4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 003, 007, 009 | 4 | 9 | False | True |
| Ohio4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 003, 009, 338 | 4 | 9 | False | True |
| Pennsylvania4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 005, 007, 045, 559 | 4 | 9 | False | True |
| Connecticut4 | Indiana4 | shared_lane | lane/family | primary | 17, 18, 23, 24, 33 | - | 5 | 9 | False | True |
| Connecticut4 | NewYork4 | shared_lane | lane/family | primary | 17, 18, 23, 5, 6 | - | 5 | 9 | False | True |
| Connecticut4 | NorthCarolina4 | shared_lane | lane/family | primary | 18, 23, 24, 33, 5 | - | 5 | 9 | False | True |
| Delaware4 | Florida4 | shared_lane | lane/family | primary | 12, 15, 23, 3, 35 | - | 5 | 9 | False | True |
| Delaware4 | Indiana4 | shared_lane | lane/family | primary | 1, 12, 15, 18, 23 | - | 5 | 9 | False | True |
| Delaware4 | NewJersey4 | shared_lane | lane/family | primary | 15, 18, 23, 31, 5 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `Delaware4 ↔ Virginia4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Pennsylvania4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ Pennsylvania4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Pennsylvania4 ↔ Virginia4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ Pennsylvania4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ OntarioCanada4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Indiana4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ Ohio4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ NorthCarolina4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NewJersey4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
