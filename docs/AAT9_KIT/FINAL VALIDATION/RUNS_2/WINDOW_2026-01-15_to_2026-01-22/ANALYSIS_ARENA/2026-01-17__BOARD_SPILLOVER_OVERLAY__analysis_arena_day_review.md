# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-17

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `aaebfced49cf3db8`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 559, 599, 899, 589, 225, 089, 399 | 15, 5, 14, 34, 3, 10, 29, 31 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 2 | Delaware4 | 167, 259, 007, 299, 006, 249, 009, 017 | 12, 31, 17, 15, 5, 3, 2, 25 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 3 | Florida4 | 255, 225, 559, 577, 177, 557, 378, 178 | 3, 10, 27, 11, 5, 33, 32, 29 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 4 | Indiana4 | 368, 077, 559, 159, 366, 139, 599, 049 | 23, 18, 5, 15, 24, 6, 9, 10 | - | - | shared_host | Combined:ALERT/3, Midday:WATCH/2, Evening:WATCH/2 |
| 5 | Michigan4 | 011, 559, 117, 255, 344, 115, 224, 125 | 6, 17, 7, 28, 5, 3, 12, 2 | - | - | shared_host | Midday:ALERT/3, Combined:OFF/1, Evening:OFF/0 |
| 6 | NewJersey4 | 001, 019, 499, 009, 004, 008, 449, 559 | 5, 35, 9, 2, 12, 4, 25, 19 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/0 |
| 7 | NewYork4 | 377, 339, 368, 337, 677, 007, 559 | 27, 23, 33, 10, 29, 21, 12, 18 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 8 | NorthCarolina4 | 224, 244, 225, 778, 477, 255, 278, 445 | 28, 31, 27, 10, 3, 15, 5, 30 | - | - | shared_host | Evening:ALERT/3, Midday:WATCH/2, Combined:OFF/1 |
| 9 | Ohio4 | 009, 599, 049, 499, 004, 007, 677 | 15, 5, 34, 28, 35, 14, 10, 33 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 10 | OntarioCanada4 | 244, 346, 044, 049, 014, 022, 255 | 15, 31, 24, 10, 21, 9, 3, 23 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 11 | Pennsylvania4 | 244, 668, 344, 003, 024, 234, 044, 034 | 31, 34, 18, 15, 12, 4, 30, 23 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 12 | PuertoRico4 | 334, 014, 018, 024, 244, 044, 011, 148 | 33, 15, 5, 23, 8, 9, 12, 18 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 13 | SouthCarolina4 | 677, 005, 006, 067, 014, 007, 099 | 20, 15, 1, 7, 2, 5, 3, 35 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 14 | Virginia4 | 449, 339, 033, 599, 559, 029, 229, 459 | 15, 35, 5, 13, 33, 2, 25, 12 | - | - | shared_host | Evening:ALERT/3, Combined:OFF/1, Midday:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 288 | 34 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 259 | 29 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 166 | 21 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 252 | 31 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 245 | 32 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 281 | 37 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 274 | 34 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 293 | 38 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 256 | 30 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 270 | 33 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| OntarioCanada4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 005, 014, 044, 244, 445, 459 | 8 | 13 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 007, 009, 049, 099, 459, 599 | 7 | 12 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 006, 009, 014, 099, 445, 459, 599 | 7 | 12 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 006, 007, 009, 249, 299 | 6 | 11 | False | True |
| NewJersey4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 009, 014, 449, 455, 559 | 6 | 11 | False | True |
| PuertoRico4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 014, 445, 459, 599 | 6 | 11 | False | True |
| PuertoRico4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 006, 014, 445, 459, 599 | 6 | 11 | False | True |
| Delaware4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 31 | 244, 249, 299, 447 | 4 | 10 | False | True |
| Ohio4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 004, 013, 044, 049, 459 | 5 | 10 | False | True |
| Ohio4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 006, 007, 009, 349 | 5 | 10 | False | True |
| Ohio4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 006, 044, 459, 599 | 5 | 10 | False | True |
| Ohio4 | Virginia4 | shared_box_family | lane/family | primary | - | 006, 009, 099, 459, 599 | 5 | 10 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 014, 049, 445, 459 | 5 | 10 | False | True |
| Connecticut4 | Delaware4 | shared_lane | lane/family | primary | 12, 15, 23, 3, 31, 5 | - | 6 | 10 | False | True |
| Connecticut4 | Ohio4 | shared_lane | lane/family | primary | 15, 23, 3, 33, 34, 5 | - | 6 | 10 | False | True |
| Connecticut4 | Pennsylvania4 | shared_lane | lane/family | primary | 12, 15, 23, 31, 33, 34 | - | 6 | 10 | False | True |
| Connecticut4 | PuertoRico4 | shared_lane | lane/family | primary | 12, 15, 23, 31, 33, 5 | - | 6 | 10 | False | True |
| Connecticut4 | Virginia4 | shared_lane | lane/family | primary | 12, 15, 23, 31, 33, 5 | - | 6 | 10 | False | True |
| Delaware4 | PuertoRico4 | shared_lane | lane/family | primary | 12, 15, 2, 23, 31, 5 | - | 6 | 10 | False | True |
| Florida4 | NewYork4 | shared_lane | lane/family | primary | 10, 20, 21, 23, 27, 3 | - | 6 | 10 | False | True |
| Indiana4 | OntarioCanada4 | shared_lane | lane/family | primary | 10, 15, 23, 24, 33, 9 | - | 6 | 10 | False | True |
| Indiana4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 23, 33, 5, 9 | - | 6 | 10 | False | True |
| NewJersey4 | PuertoRico4 | shared_lane | lane/family | primary | 12, 18, 2, 23, 5, 9 | - | 6 | 10 | False | True |
| Pennsylvania4 | PuertoRico4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 31, 33 | - | 6 | 10 | False | True |
| PuertoRico4 | Virginia4 | shared_lane | lane/family | primary | 12, 15, 23, 31, 33, 5 | - | 6 | 10 | False | True |
| NorthCarolina4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 31, 34 | 244, 344, 349 | 3 | 9 | False | True |
| Connecticut4 | Ohio4 | shared_box_family | lane/family | primary | - | 044, 099, 459, 599 | 4 | 9 | False | True |
| Connecticut4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 024, 044, 459, 599 | 4 | 9 | False | True |
| Connecticut4 | Virginia4 | shared_box_family | lane/family | primary | - | 099, 459, 559, 599 | 4 | 9 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 009, 014, 017 | 4 | 9 | False | True |
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 006, 007, 009 | 4 | 9 | False | True |
| Delaware4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 007, 009, 014 | 4 | 9 | False | True |
| Delaware4 | Virginia4 | shared_box_family | lane/family | primary | - | 006, 009, 014, 029 | 4 | 9 | False | True |
| Florida4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 177, 178, 225, 255 | 4 | 9 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 011, 066, 559 | 4 | 9 | False | True |
| Indiana4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 133, 336, 368 | 4 | 9 | False | True |
| Indiana4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 006, 009, 559 | 4 | 9 | False | True |
| Michigan4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 001, 144, 255, 344 | 4 | 9 | False | True |
| Michigan4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 005, 014, 255 | 4 | 9 | False | True |
| NewJersey4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 009, 013, 499 | 4 | 9 | False | True |

## Strongest Overlap Pairs

- `Connecticut4 ↔ Ohio4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Pennsylvania4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Virginia4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ Virginia4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ NewYork4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Virginia4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ NorthCarolina4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ PuertoRico4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Virginia4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ Virginia4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
