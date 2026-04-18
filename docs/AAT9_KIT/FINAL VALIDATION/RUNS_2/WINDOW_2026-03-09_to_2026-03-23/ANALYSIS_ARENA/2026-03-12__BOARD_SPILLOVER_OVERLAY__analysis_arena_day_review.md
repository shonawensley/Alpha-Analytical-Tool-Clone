# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-12

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `0907f4e800d6322e`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 368, 168, 006, 668, 068, 338, 348 | 23, 18, 24, 15, 8, 33, 2, 34 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/0 |
| 2 | Delaware4 | 499, 599, 047, 117, 119, 344, 129, 179 | 35, 22, 12, 15, 31, 17, 34, 19 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 3 | Florida4 | 224, 077, 499, 022, 066, 778, 024, 012 | 28, 10, 12, 31, 35, 20, 6, 27 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 4 | Indiana4 | 788, 015, 688, 559, 228, 117, 677, 113 | 29, 17, 27, 23, 2, 18, 6, 5 | - | - | shared_host | Evening:ALERT/3, Combined:OFF/1, Midday:OFF/1 |
| 5 | Michigan4 | 455, 688, 488, 559, 334, 058, 014, 088 | 5, 33, 23, 4, 2, 3, 21, 35 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 177, 244, 006, 388, 245, 024, 029, 677 | 12, 31, 20, 15, 2, 17, 28, 5 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/1 |
| 7 | NewYork4 | 224, 368, 559, 366, 455, 255, 599, 668 | 23, 5, 18, 28, 24, 33, 15, 32 | - | - | shared_host | Combined:ALERT/3, Midday:WATCH/2, Evening:OFF/0 |
| 8 | NorthCarolina4 | 009, 344, 388, 346, 134, 339, 445 | 5, 24, 34, 23, 15, 33, 32, 2 | - | - | shared_host | Combined:ALERT/3, Evening:WATCH/2, Midday:OFF/1 |
| 9 | Ohio4 | 033, 338, 013, 599, 059, 334, 003, 069 | 13, 15, 5, 4, 8, 32, 18, 14 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/1 |
| 10 | OntarioCanada4 | 449, 244, 388, 224, 008, 189, 238, 249 | 31, 35, 28, 4, 9, 24, 32, 29 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 11 | Pennsylvania4 | 559, 233, 224, 259, 002, 005, 008, 238 | 29, 5, 12, 28, 3, 1, 32, 33 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/0 |
| 12 | PuertoRico4 | 559, 449, 667, 599, 677, 159, 555 | 5, 19, 35, 9, 15, 17, 6, 25 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 13 | SouthCarolina4 | 029, 667, 069, 229, 168, 244, 066, 678 | 12, 17, 28, 20, 18, 31, 7, 5 | - | - | shared_host | Evening:ALERT/3, Combined:WATCH/2, Midday:WATCH/2 |
| 14 | Virginia4 | 599, 559, 099, 299, 009, 055, 005, 369 | 15, 5, 1, 31, 24, 32, 23, 25 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 224 | 27 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 219 | 28 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 233 | 29 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 186 | 22 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 228 | 30 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 283 | 35 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 223 | 27 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 248 | 31 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 264 | 32 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 300 | 37 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| NewJersey4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 009, 029, 244, 259, 677 | 6 | 11 | False | True |
| Connecticut4 | NewYork4 | shared_box_family | lane/family | primary | - | 138, 336, 366, 368, 668 | 5 | 10 | False | True |
| Delaware4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 017, 114, 119, 557, 599 | 5 | 10 | False | True |
| Florida4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 004, 007, 024, 224 | 5 | 10 | False | True |
| Indiana4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 007, 008, 378, 559 | 5 | 10 | False | True |
| Connecticut4 | NorthCarolina4 | shared_lane | lane/family | primary | 15, 18, 23, 24, 32, 33 | - | 6 | 10 | False | True |
| Connecticut4 | Ohio4 | shared_lane | lane/family | primary | 15, 18, 23, 32, 33, 8 | - | 6 | 10 | False | True |
| Connecticut4 | OntarioCanada4 | shared_lane | lane/family | primary | 15, 18, 23, 24, 32, 33 | - | 6 | 10 | False | True |
| NorthCarolina4 | Ohio4 | shared_lane | lane/family | primary | 15, 18, 23, 32, 33, 5 | - | 6 | 10 | False | True |
| NorthCarolina4 | OntarioCanada4 | shared_lane | lane/family | primary | 15, 18, 23, 24, 32, 33 | - | 6 | 10 | False | True |
| Ohio4 | OntarioCanada4 | shared_lane | lane/family | primary | 15, 18, 23, 32, 33, 4 | - | 6 | 10 | False | True |
| OntarioCanada4 | Connecticut4 | alert_implied_echo | lane/family | primary | 9, 32 | 019, 069, 338 | 3 | 9 | False | True |
| PuertoRico4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 17, 21 | 266, 667, 678 | 3 | 9 | False | True |
| Florida4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 001, 004, 007, 009 | 4 | 9 | False | True |
| Michigan4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 006, 009, 178 | 4 | 9 | False | True |
| Michigan4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 004, 009, 059, 559 | 4 | 9 | False | True |
| Michigan4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 011, 059, 334 | 4 | 9 | False | True |
| NorthCarolina4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 004, 007, 559 | 4 | 9 | False | True |
| PuertoRico4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 055, 559, 599 | 4 | 9 | False | True |
| Connecticut4 | NewJersey4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 32 | - | 5 | 9 | False | True |
| Delaware4 | Florida4 | shared_lane | lane/family | primary | 12, 15, 23, 31, 35 | - | 5 | 9 | False | True |
| Delaware4 | NewJersey4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 31 | - | 5 | 9 | False | True |
| Delaware4 | OntarioCanada4 | shared_lane | lane/family | primary | 15, 18, 23, 31, 35 | - | 5 | 9 | False | True |
| Delaware4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 17, 18, 19, 35 | - | 5 | 9 | False | True |
| Delaware4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 17, 18, 23, 31 | - | 5 | 9 | False | True |
| Florida4 | NewJersey4 | shared_lane | lane/family | primary | 12, 15, 20, 23, 31 | - | 5 | 9 | False | True |
| Florida4 | OntarioCanada4 | shared_lane | lane/family | primary | 15, 23, 28, 31, 35 | - | 5 | 9 | False | True |
| Florida4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 20, 23, 28, 31 | - | 5 | 9 | False | True |
| Michigan4 | Ohio4 | shared_lane | lane/family | primary | 15, 23, 33, 4, 5 | - | 5 | 9 | False | True |
| NewJersey4 | Ohio4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 32 | - | 5 | 9 | False | True |
| NewJersey4 | OntarioCanada4 | shared_lane | lane/family | primary | 15, 18, 23, 31, 32 | - | 5 | 9 | False | True |
| NewJersey4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 18, 20, 23, 31 | - | 5 | 9 | False | True |
| NewYork4 | Pennsylvania4 | shared_lane | lane/family | primary | 12, 23, 28, 3, 5 | - | 5 | 9 | False | True |
| NewYork4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 17, 18, 23, 28 | - | 5 | 9 | False | True |
| NorthCarolina4 | Virginia4 | shared_lane | lane/family | primary | 15, 18, 23, 24, 5 | - | 5 | 9 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_lane | lane/family | primary | 18, 23, 28, 31, 9 | - | 5 | 9 | False | True |
| OntarioCanada4 | Virginia4 | shared_lane | lane/family | primary | 15, 18, 23, 24, 31 | - | 5 | 9 | False | True |
| Connecticut4 | NewJersey4 | alert_implied_echo | lane/family | primary | 2, 8 | 006, 068 | 2 | 8 | False | True |
| NewJersey4 | Connecticut4 | alert_implied_echo | lane/family | primary | 2, 8 | 006, 068 | 2 | 8 | False | True |
| NewJersey4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 2, 31 | 006, 244 | 2 | 8 | False | True |

## Strongest Overlap Pairs

- `NewJersey4 ↔ SouthCarolina4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ Ohio4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ OntarioCanada4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ NewJersey4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `PuertoRico4 ↔ SouthCarolina4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Ohio4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ NewJersey4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ OntarioCanada4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `OntarioCanada4 ↔ PuertoRico4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Florida4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
