# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-21

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `aad1f390bf5f85a2`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 113, 224, 355, 255, 123, 244, 114, 144 | 18, 28, 4, 21, 23, 25, 5, 3 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 2 | Delaware4 | 001, 599, 016, 011, 559, 006 | 2, 15, 6, 5, 35, 34, 16, 12 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 3 | Florida4 | 244, 246, 114, 066, 224, 124, 144, 667 | 31, 22, 19, 6, 28, 25, 17, 3 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 4 | Indiana4 | 559, 455, 002, 229, 155, 259, 224, 255 | 5, 3, 28, 12, 2, 10, 31, 15 | - | - | shared_host | Combined:OFF/0, Evening:OFF/0, Midday:OFF/0 |
| 5 | Michigan4 | 567, 001, 599, 445, 677, 556, 003, 559 | 5, 2, 15, 31, 7, 22, 1, 20 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 455, 559, 499, 003, 005, 445, 001, 344 | 5, 4, 1, 15, 35, 34, 13, 33 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 7 | NewYork4 | 066, 667, 013, 668, 366, 166, 025, 266 | 6, 17, 18, 8, 16, 3, 23, 33 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 8 | NorthCarolina4 | 499, 117, 889, 348, 599, 449, 299, 088 | 35, 33, 17, 15, 31, 20, 23, 18 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 9 | Ohio4 | 699, 002, 018, 299, 255, 024, 669, 258 | 3, 25, 31, 8, 12, 24, 5, 21 | - | - | shared_host | Combined:ALERT/3, Midday:ALERT/3, Evening:WATCH/2 |
| 10 | OntarioCanada4 | 368, 559, 055, 259, 599, 355, 399, 057 | 23, 5, 1, 12, 3, 4, 18, 31 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 11 | Pennsylvania4 | 446, 447, 478, 014, 677, 477, 144, 048 | 25, 30, 31, 14, 35, 20, 34, 33 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 12 | PuertoRico4 | 224, 244, 388, 368, 238, 007, 338 | 32, 31, 28, 23, 29, 3, 10, 15 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 13 | SouthCarolina4 | 559, 455, 155, 003, 255, 158, 344, 577 | 5, 4, 3, 8, 2, 1, 10, 23 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:WATCH/2 |
| 14 | Virginia4 | 225, 022, 255, 559, 259, 268, 224, 003 | 10, 3, 28, 11, 4, 21, 5, 12 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/0 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 296 | 32 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 335 | 39 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 296 | 35 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 341 | 40 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 330 | 40 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 311 | 37 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 243 | 31 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 235 | 27 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 266 | 31 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 335 | 41 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Delaware4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 006, 009, 015, 559, 599 | 6 | 11 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 011, 049, 559 | 6 | 11 | False | True |
| Indiana4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 014, 017, 057, 259, 455, 559 | 6 | 11 | False | True |
| Indiana4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 014, 155, 255, 455, 559 | 6 | 11 | False | True |
| NewJersey4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 003, 004, 005, 355, 455, 559 | 6 | 11 | False | True |
| Delaware4 | Michigan4 | alert_implied_echo | lane/family | primary | 2, 15 | 001, 006, 015, 599 | 4 | 10 | False | True |
| OntarioCanada4 | Connecticut4 | alert_implied_echo | lane/family | primary | 18 | 113, 136, 366, 668 | 4 | 10 | False | True |
| Indiana4 | Virginia4 | shared_box_family | lane/family | primary | - | 002, 022, 255, 259, 559 | 5 | 10 | False | True |
| Michigan4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 009, 445, 455, 559 | 5 | 10 | False | True |
| Connecticut4 | PuertoRico4 | shared_lane | lane/family | primary | 18, 21, 23, 28, 3, 31 | - | 6 | 10 | False | True |
| NorthCarolina4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 23, 31, 33, 35 | - | 6 | 10 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_lane | lane/family | primary | 15, 18, 23, 3, 4, 5 | - | 6 | 10 | False | True |
| Delaware4 | NewYork4 | alert_implied_echo | lane/family | primary | 2, 6 | 001, 006, 016 | 3 | 9 | False | True |
| Florida4 | NewYork4 | alert_implied_echo | lane/family | primary | 6 | 011, 016, 066 | 3 | 9 | False | True |
| Indiana4 | Virginia4 | alert_implied_echo | lane/family | primary | 3, 10, 5 | 002, 022, 559 | 3 | 9 | False | True |
| NewJersey4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 4, 5 | 003, 455, 559 | 3 | 9 | False | True |
| NorthCarolina4 | Michigan4 | alert_implied_echo | composite | secondary | 11 | 023, 028, 037, 078, 235, 258 | 6 | 9 | False | True |
| Ohio4 | Virginia4 | alert_implied_echo | lane/family | primary | 3, 8, 12 | 002, 018, 024 | 3 | 9 | False | True |
| SouthCarolina4 | Indiana4 | alert_implied_echo | lane/family | primary | 2, 5 | 155, 455, 559 | 3 | 9 | False | True |
| SouthCarolina4 | NewJersey4 | alert_implied_echo | lane/family | primary | 4, 5 | 003, 455, 559 | 3 | 9 | False | True |
| Connecticut4 | Florida4 | shared_box_family | lane/family | primary | - | 004, 114, 224, 244 | 4 | 9 | False | True |
| Connecticut4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 014, 255, 355 | 4 | 9 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 001, 004, 155, 559 | 4 | 9 | False | True |
| Delaware4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 006, 011, 016 | 4 | 9 | False | True |
| Florida4 | Ohio4 | shared_box_family | lane/family | primary | - | 001, 006, 244, 299 | 4 | 9 | False | True |
| Florida4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 006, 224, 244, 299 | 4 | 9 | False | True |
| Indiana4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 004, 455, 559 | 4 | 9 | False | True |
| Ohio4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 006, 009, 244, 299 | 4 | 9 | False | True |
| Ohio4 | Virginia4 | shared_box_family | lane/family | primary | - | 002, 018, 024, 255 | 4 | 9 | False | True |
| OntarioCanada4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 013, 014, 017, 368 | 4 | 9 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 014, 355, 455, 559 | 4 | 9 | False | True |
| Connecticut4 | Florida4 | shared_lane | lane/family | primary | 18, 19, 23, 28, 31 | - | 5 | 9 | False | True |
| Connecticut4 | NorthCarolina4 | shared_lane | lane/family | primary | 18, 23, 31, 33, 4 | - | 5 | 9 | False | True |
| Connecticut4 | Pennsylvania4 | shared_lane | lane/family | primary | 18, 23, 28, 31, 33 | - | 5 | 9 | False | True |
| Connecticut4 | Virginia4 | shared_lane | lane/family | primary | 21, 23, 28, 3, 4 | - | 5 | 9 | False | True |
| Delaware4 | SouthCarolina4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 5 | - | 5 | 9 | False | True |
| Indiana4 | OntarioCanada4 | shared_lane | lane/family | primary | 12, 15, 23, 3, 5 | - | 5 | 9 | False | True |
| Indiana4 | SouthCarolina4 | shared_lane | lane/family | primary | 15, 2, 23, 3, 5 | - | 5 | 9 | False | True |
| Indiana4 | Virginia4 | shared_lane | lane/family | primary | 12, 23, 28, 3, 5 | - | 5 | 9 | False | True |
| NewJersey4 | NorthCarolina4 | shared_lane | lane/family | primary | 15, 23, 33, 35, 4 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `Delaware4 ↔ Michigan4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ SouthCarolina4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ SouthCarolina4` score=`37` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ OntarioCanada4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Virginia4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NewJersey4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `OntarioCanada4 ↔ SouthCarolina4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ OntarioCanada4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ NewJersey4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ NewYork4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
