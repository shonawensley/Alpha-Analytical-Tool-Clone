# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-14

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `51b69b47f8956ded`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 559, 368, 689, 668, 168, 468, 599, 044 | 23, 24, 18, 5, 15, 35, 25, 33 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 2 | Delaware4 | 559, 049, 007, 059, 599, 009, 005, 147 | 15, 5, 12, 35, 31, 3, 22, 9 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 3 | Florida4 | 224, 226, 499, 022, 699, 225, 469, 229 | 28, 25, 10, 20, 35, 19, 31, 34 | - | - | shared_host | Midday:ALERT/3, Combined:OFF/1, Evening:OFF/1 |
| 4 | Indiana4 | 599, 788, 005, 899, 559, 889, 224 | 15, 29, 33, 1, 27, 28, 5, 34 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:WATCH/2 |
| 5 | Michigan4 | 008, 688, 455, 445, 088, 448, 559 | 5, 4, 23, 15, 13, 1, 8, 35 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 004, 244, 224, 024, 169, 299, 499, 167 | 31, 19, 5, 28, 12, 35, 17, 15 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/0 |
| 7 | NewYork4 | 668, 006, 039, 033, 259, 003, 339, 225 | 18, 14, 2, 12, 33, 24, 28, 5 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/0, Evening:OFF/0 |
| 8 | NorthCarolina4 | 388, 368, 009, 003, 038, 122, 223 | 23, 32, 4, 5, 13, 33, 18, 8 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 9 | Ohio4 | 049, 069, 338, 334, 009, 244, 003, 034 | 15, 5, 14, 35, 32, 9, 33, 31 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:WATCH/2 |
| 10 | OntarioCanada4 | 449, 368, 388, 223, 049, 014, 238 | 35, 31, 23, 15, 27, 29, 4, 32 | - | - | shared_host | Evening:OFF/1, Combined:OFF/0, Midday:OFF/0 |
| 11 | Pennsylvania4 | 559, 013, 224, 259, 005, 234, 008 | 8, 5, 18, 28, 32, 12, 23, 4 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 12 | PuertoRico4 | 677, 449, 445, 066, 559, 007, 057, 056 | 20, 15, 6, 19, 2, 18, 5, 35 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 13 | SouthCarolina4 | 244, 077, 003, 022, 027, 255, 477, 559 | 10, 31, 3, 4, 20, 5, 28, 7 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 14 | Virginia4 | 559, 259, 299, 599, 788, 009, 029 | 5, 12, 1, 15, 31, 23, 24, 3 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 267 | 34 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 364 | 42 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 193 | 26 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 274 | 31 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 335 | 38 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 304 | 35 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 262 | 31 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 284 | 35 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 305 | 34 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 301 | 39 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Delaware4 | Ohio4 | alert_implied_echo | lane/family | primary | 5, 3, 15 | 004, 007, 009, 049, 059 | 5 | 11 | False | True |
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 007, 009, 049, 059, 099, 599 | 6 | 11 | False | True |
| Indiana4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 007, 559, 599, 788, 889 | 6 | 11 | False | True |
| Michigan4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 005, 009, 011, 445, 559 | 6 | 11 | False | True |
| NewJersey4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 004, 013, 014, 244, 249, 299 | 6 | 11 | False | True |
| Ohio4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 006, 007, 009, 059, 599 | 6 | 11 | False | True |
| PuertoRico4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 009, 559, 599 | 6 | 11 | False | True |
| Delaware4 | Virginia4 | alert_implied_echo | lane/family | primary | 5, 3 | 004, 007, 009, 059 | 4 | 10 | False | True |
| Pennsylvania4 | NewYork4 | alert_implied_echo | lane/family | primary | 8, 14 | 013, 034, 039, 345 | 4 | 10 | False | True |
| Virginia4 | Connecticut4 | alert_implied_echo | lane/family | primary | 24, 5 | 346, 468, 559, 689 | 4 | 10 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 007, 009, 013, 117, 559 | 5 | 10 | False | True |
| Delaware4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 007, 009, 445, 559, 599 | 5 | 10 | False | True |
| Delaware4 | Virginia4 | shared_box_family | lane/family | primary | - | 007, 009, 059, 559, 599 | 5 | 10 | False | True |
| Indiana4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 005, 007, 445, 559, 599 | 5 | 10 | False | True |
| Michigan4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 009, 559 | 5 | 10 | False | True |
| Ohio4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 007, 009, 066, 599 | 5 | 10 | False | True |
| Pennsylvania4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 005, 007, 009, 559 | 5 | 10 | False | True |
| Pennsylvania4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 007, 009, 259, 559 | 5 | 10 | False | True |
| Delaware4 | OntarioCanada4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 31, 35 | - | 6 | 10 | False | True |
| Indiana4 | Michigan4 | shared_lane | lane/family | primary | 1, 12, 15, 23, 34, 5 | - | 6 | 10 | False | True |
| Indiana4 | Pennsylvania4 | shared_lane | lane/family | primary | 1, 12, 15, 18, 23, 5 | - | 6 | 10 | False | True |
| Indiana4 | Virginia4 | shared_lane | lane/family | primary | 1, 12, 15, 23, 29, 5 | - | 6 | 10 | False | True |
| Ohio4 | OntarioCanada4 | shared_lane | lane/family | primary | 15, 23, 31, 32, 35, 9 | - | 6 | 10 | False | True |
| Delaware4 | Michigan4 | alert_implied_echo | lane/family | primary | 5 | 004, 009, 045 | 3 | 9 | False | True |
| Delaware4 | NewJersey4 | alert_implied_echo | lane/family | primary | 5, 21 | 004, 009, 178 | 3 | 9 | False | True |
| Delaware4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 5, 3 | 004, 007, 009 | 3 | 9 | False | True |
| Michigan4 | Connecticut4 | alert_implied_echo | lane/family | primary | 24 | 346, 468, 689 | 3 | 9 | False | True |
| Michigan4 | Indiana4 | alert_implied_echo | lane/family | primary | 4, 24, 34 | 008, 134, 899 | 3 | 9 | False | True |
| Michigan4 | Virginia4 | alert_implied_echo | composite | secondary | 24 | 134, 139, 148, 189, 346, 369 | 6 | 9 | False | True |
| NewYork4 | Pennsylvania4 | alert_implied_echo | composite | secondary | 14 | 034, 039, 048, 089, 345, 359 | 6 | 9 | False | True |
| Virginia4 | Michigan4 | alert_implied_echo | lane/family | primary | 5 | 045, 455, 559 | 3 | 9 | False | True |
| Connecticut4 | Michigan4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 559 | 4 | 9 | False | True |
| Connecticut4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 013, 138, 336, 368 | 4 | 9 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 007, 445, 559, 599 | 4 | 9 | False | True |
| Delaware4 | Michigan4 | shared_box_family | lane/family | primary | - | 009, 014, 445, 559 | 4 | 9 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 005, 008, 445, 559 | 4 | 9 | False | True |
| Indiana4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 007, 008, 559 | 4 | 9 | False | True |
| Michigan4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 009, 014, 024 | 4 | 9 | False | True |
| Michigan4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 008, 009, 559 | 4 | 9 | False | True |
| NewYork4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 003, 006, 007, 013 | 4 | 9 | False | True |

## Strongest Overlap Pairs

- `Delaware4 ↔ Ohio4` score=`38` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Virginia4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ Virginia4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Virginia4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Michigan4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Pennsylvania4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ OntarioCanada4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ Pennsylvania4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ OntarioCanada4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Pennsylvania4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
