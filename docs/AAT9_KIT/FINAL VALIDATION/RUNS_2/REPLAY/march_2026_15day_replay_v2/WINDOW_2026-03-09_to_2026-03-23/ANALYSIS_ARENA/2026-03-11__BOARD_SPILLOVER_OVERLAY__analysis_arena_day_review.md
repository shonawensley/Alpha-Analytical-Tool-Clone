# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-11

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `0a227731ffa51c4a`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 368, 168, 338, 006, 189, 244, 099 | 23, 18, 24, 2, 31, 15, 21, 32 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/0 |
| 2 | Delaware4 | 599, 117, 499, 119, 179, 129, 199 | 15, 22, 35, 12, 28, 17, 31, 9 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 3 | Florida4 | 224, 077, 066, 022, 778, 499, 046, 014 | 28, 10, 6, 9, 35, 12, 15, 27 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 4 | Indiana4 | 255, 788, 113, 117, 007, 677, 559, 115 | 3, 29, 18, 11, 6, 27, 17, 10 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 5 | Michigan4 | 559, 599, 455, 688, 334, 258, 244, 255 | 5, 23, 11, 33, 15, 3, 18, 29 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 177, 009, 244, 006, 388, 459, 559, 455 | 5, 20, 15, 2, 31, 9, 17, 6 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 7 | NewYork4 | 368, 224, 559, 455, 567, 689, 255, 336 | 23, 5, 28, 24, 7, 18, 21, 33 | - | - | shared_host | Combined:ALERT/3, Midday:WATCH/2, Evening:OFF/0 |
| 8 | NorthCarolina4 | 344, 388, 003, 099, 007, 009 | 34, 15, 4, 35, 23, 2, 32, 5 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 9 | Ohio4 | 113, 599, 069, 003, 059, 136, 011, 334 | 18, 4, 15, 5, 9, 6, 19, 33 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:WATCH/2 |
| 10 | OntarioCanada4 | 449, 244, 224, 077, 008, 047, 447, 044 | 31, 35, 28, 4, 34, 15, 12, 10 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 11 | Pennsylvania4 | 559, 224, 008, 002, 238, 223, 259, 225 | 5, 3, 12, 29, 4, 28, 32, 1 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/0 |
| 12 | PuertoRico4 | 559, 449, 499, 599, 157, 359, 557, 117 | 5, 35, 19, 17, 15, 7, 14, 3 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 13 | SouthCarolina4 | 667, 069, 224, 669, 029, 678, 019, 599 | 17, 9, 28, 18, 12, 15, 20, 5 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:WATCH/2 |
| 14 | Virginia4 | 599, 559, 039, 055, 009, 369, 005, 299 | 15, 5, 1, 14, 24, 9, 31, 32 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:WATCH/2 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 249 | 31 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 229 | 28 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 239 | 33 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 260 | 33 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 289 | 36 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 269 | 33 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 291 | 35 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 281 | 34 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 297 | 38 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 269 | 32 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Connecticut4 | NewYork4 | shared_box_family | lane/family | primary | - | 006, 138, 336, 368, 688, 689 | 6 | 11 | False | True |
| Delaware4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 011, 017, 119, 499, 557, 599 | 6 | 11 | False | True |
| Indiana4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 002, 005, 007, 008, 255, 559 | 6 | 11 | False | True |
| Delaware4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 17, 18, 19, 21, 23, 28 | - | 7 | 11 | False | True |
| NorthCarolina4 | OntarioCanada4 | shared_lane | lane/family | primary | 15, 23, 31, 33, 34, 35, 4 | - | 7 | 11 | False | True |
| PuertoRico4 | NewJersey4 | alert_implied_echo | lane/family | primary | 5 | 045, 059, 455, 559 | 4 | 10 | False | True |
| Michigan4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 009, 244, 455, 559 | 5 | 10 | False | True |
| NewJersey4 | NewYork4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 455, 559 | 5 | 10 | False | True |
| NorthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 099, 599 | 5 | 10 | False | True |
| Connecticut4 | NewJersey4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 31, 32 | - | 6 | 10 | False | True |
| Delaware4 | OntarioCanada4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 28, 35 | - | 6 | 10 | False | True |
| Delaware4 | Virginia4 | alert_implied_echo | lane/family | primary | 15 | 445, 459, 599 | 3 | 9 | False | True |
| Connecticut4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 188, 244, 688 | 4 | 9 | False | True |
| Florida4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 004, 007, 224 | 4 | 9 | False | True |
| Michigan4 | NewYork4 | shared_box_family | lane/family | primary | - | 004, 455, 559, 688 | 4 | 9 | False | True |
| Michigan4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 009, 011, 599 | 4 | 9 | False | True |
| Michigan4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 004, 009, 559 | 4 | 9 | False | True |
| Michigan4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 011, 455, 559, 599 | 4 | 9 | False | True |
| Michigan4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 009, 559, 599 | 4 | 9 | False | True |
| NewJersey4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 009, 559 | 4 | 9 | False | True |
| NewJersey4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 009, 459, 559 | 4 | 9 | False | True |
| NewYork4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 224, 559 | 4 | 9 | False | True |
| NorthCarolina4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 005, 007, 009 | 4 | 9 | False | True |
| Ohio4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 011, 017, 059, 599 | 4 | 9 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 001, 007, 009, 224 | 4 | 9 | False | True |
| Pennsylvania4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 559 | 4 | 9 | False | True |
| Delaware4 | NewYork4 | shared_lane | lane/family | primary | 12, 17, 18, 23, 28 | - | 5 | 9 | False | True |
| Delaware4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 17, 18, 19, 35 | - | 5 | 9 | False | True |
| Florida4 | OntarioCanada4 | shared_lane | lane/family | primary | 10, 15, 23, 28, 35 | - | 5 | 9 | False | True |
| NewJersey4 | NorthCarolina4 | shared_lane | lane/family | primary | 15, 23, 31, 32, 5 | - | 5 | 9 | False | True |
| NewJersey4 | Ohio4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 5 | - | 5 | 9 | False | True |
| NewJersey4 | OntarioCanada4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 31 | - | 5 | 9 | False | True |
| NewYork4 | SouthCarolina4 | shared_lane | lane/family | primary | 12, 17, 18, 23, 28 | - | 5 | 9 | False | True |
| Ohio4 | OntarioCanada4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 4 | - | 5 | 9 | False | True |
| Delaware4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 3, 15 | 557, 599 | 2 | 8 | False | True |
| Indiana4 | Michigan4 | alert_implied_echo | lane/family | primary | 11 | 258, 578 | 2 | 8 | False | True |
| Ohio4 | Connecticut4 | alert_implied_echo | lane/family | primary | 6, 18 | 066, 168 | 2 | 8 | False | True |
| PuertoRico4 | Michigan4 | alert_implied_echo | lane/family | primary | 5 | 455, 559 | 2 | 8 | False | True |
| PuertoRico4 | NewYork4 | alert_implied_echo | lane/family | primary | 5 | 455, 559 | 2 | 8 | False | True |
| Virginia4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 14, 15 | 359, 599 | 2 | 8 | False | True |

## Strongest Overlap Pairs

- `Connecticut4 ↔ NewYork4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Pennsylvania4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ OntarioCanada4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Virginia4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ Pennsylvania4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ Virginia4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `PuertoRico4 ↔ Virginia4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Ohio4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ SouthCarolina4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ Ohio4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
