# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-21

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `df268be176ed4bdc`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 006, 255, 355, 005, 001, 055, 455 | 2, 3, 15, 5, 1, 4, 9, 18 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 2 | Delaware4 | 255, 559, 336, 259, 229, 355, 455, 055 | 5, 3, 23, 4, 12, 7, 10, 1 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/1 |
| 3 | Florida4 | 259, 378, 008, 388, 078, 559, 235, 788 | 29, 11, 3, 12, 5, 27, 10, 32 | - | - | shared_host | Evening:WATCH/2, Midday:OFF/1, Combined:OFF/0 |
| 4 | Indiana4 | 001, 077, 244, 017, 147, 224, 037, 014 | 10, 11, 31, 2, 9, 14, 6, 18 | - | - | shared_host | Midday:OFF/1, Evening:OFF/1, Combined:OFF/0 |
| 5 | Michigan4 | 224, 477, 017, 007, 778, 277, 249, 247 | 28, 10, 3, 17, 12, 7, 26, 27 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/0 |
| 6 | NewJersey4 | 001, 559, 004, 014, 009, 017, 011, 019 | 5, 9, 2, 6, 7, 15, 33, 20 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 7 | NewYork4 | 113, 337, 115, 377, 133, 378, 347 | 18, 29, 23, 27, 10, 6, 21, 30 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 8 | NorthCarolina4 | 778, 006, 366, 225, 166, 244, 255, 004 | 27, 10, 2, 18, 31, 29, 5, 12 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 9 | Ohio4 | 077, 007, 078, 008, 088, 009, 049 | 10, 3, 5, 15, 31, 14, 13, 34 | - | - | shared_host | Midday:ALERT/3, Evening:ALERT/3, Combined:OFF/1 |
| 10 | OntarioCanada4 | 244, 044, 004, 445, 468, 246, 449 | 31, 15, 5, 25, 21, 35, 2, 34 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:WATCH/2 |
| 11 | Pennsylvania4 | 559, 599, 178, 334, 344, 039, 005 | 5, 15, 33, 34, 14, 21, 4, 23 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 12 | PuertoRico4 | 168, 668, 336, 334, 138, 455, 118 | 18, 23, 33, 5, 32, 13, 6, 2 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 13 | SouthCarolina4 | 009, 599, 005, 003, 559, 039, 067, 007 | 5, 15, 1, 3, 4, 31, 7, 35 | - | - | shared_host | Combined:ALERT/3, Midday:OFF/1, Evening:OFF/1 |
| 14 | Virginia4 | 133, 339, 033, 002, 559, 016, 026, 145 | 23, 33, 7, 5, 6, 13, 32, 8 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 311 | 38 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 238 | 30 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 229 | 28 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 273 | 33 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 184 | 22 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 346 | 42 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 236 | 29 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 242 | 31 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 243 | 31 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 208 | 26 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 007, 009, 039, 059, 559, 599 | 7 | 12 | False | True |
| PuertoRico4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 006, 011, 138, 188, 336, 688 | 7 | 12 | False | True |
| NewJersey4 | Connecticut4 | alert_implied_echo | lane/family | primary | 2, 5 | 001, 004, 006, 015, 056 | 5 | 11 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 009, 013, 014, 455, 559 | 6 | 11 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 007, 009, 059, 255, 559 | 6 | 11 | False | True |
| Delaware4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 003, 007, 009, 045, 059, 559 | 6 | 11 | False | True |
| NewJersey4 | OntarioCanada4 | alert_implied_echo | lane/family | primary | 2, 5, 31 | 001, 004, 006, 249 | 4 | 10 | False | True |
| NewJersey4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 2, 5 | 001, 004, 006, 056 | 4 | 10 | False | True |
| Connecticut4 | Delaware4 | shared_box_family | lane/family | primary | - | 004, 007, 055, 255, 355 | 5 | 10 | False | True |
| Connecticut4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 056, 668 | 5 | 10 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 077, 224 | 5 | 10 | False | True |
| NewJersey4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 011, 455 | 5 | 10 | False | True |
| NewJersey4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 006, 011, 013, 559 | 5 | 10 | False | True |
| NewYork4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 011, 118, 366, 668 | 5 | 10 | False | True |
| Connecticut4 | SouthCarolina4 | shared_lane | lane/family | primary | 1, 15, 23, 3, 4, 5 | - | 6 | 10 | False | True |
| Indiana4 | NewJersey4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 7, 9 | - | 6 | 10 | False | True |
| NewJersey4 | Virginia4 | shared_lane | lane/family | primary | 12, 18, 23, 5, 6, 7 | - | 6 | 10 | False | True |
| NewYork4 | NorthCarolina4 | shared_lane | lane/family | primary | 10, 12, 18, 20, 23, 27 | - | 6 | 10 | False | True |
| Connecticut4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 255 | 4 | 9 | False | True |
| Connecticut4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 099 | 4 | 9 | False | True |
| Florida4 | NewYork4 | shared_box_family | lane/family | primary | - | 005, 133, 238, 378 | 4 | 9 | False | True |
| Florida4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 007, 008, 078 | 4 | 9 | False | True |
| Florida4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 007, 178, 559 | 4 | 9 | False | True |
| Indiana4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 011, 014, 017 | 4 | 9 | False | True |
| Indiana4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 011, 014, 017 | 4 | 9 | False | True |
| Michigan4 | Ohio4 | shared_box_family | lane/family | primary | - | 007, 057, 077, 224 | 4 | 9 | False | True |
| NewJersey4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 011, 014, 017 | 4 | 9 | False | True |
| NewJersey4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 004, 006, 249 | 4 | 9 | False | True |
| NewYork4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 005, 011, 133 | 4 | 9 | False | True |
| Ohio4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 009 | 4 | 9 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 006, 067, 559 | 4 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_lane | lane/family | primary | 12, 23, 3, 4, 5 | - | 5 | 9 | False | True |
| Connecticut4 | Florida4 | shared_lane | lane/family | primary | 12, 23, 3, 4, 5 | - | 5 | 9 | False | True |
| Connecticut4 | NewJersey4 | shared_lane | lane/family | primary | 12, 15, 2, 23, 5 | - | 5 | 9 | False | True |
| Delaware4 | Florida4 | shared_lane | lane/family | primary | 12, 23, 3, 4, 5 | - | 5 | 9 | False | True |
| Delaware4 | Virginia4 | shared_lane | lane/family | primary | 12, 18, 23, 3, 5 | - | 5 | 9 | False | True |
| Indiana4 | NorthCarolina4 | shared_lane | lane/family | primary | 10, 18, 2, 23, 31 | - | 5 | 9 | False | True |
| Indiana4 | Ohio4 | shared_lane | lane/family | primary | 10, 11, 15, 31, 33 | - | 5 | 9 | False | True |
| Indiana4 | Pennsylvania4 | shared_lane | lane/family | primary | 14, 15, 18, 23, 33 | - | 5 | 9 | False | True |
| Indiana4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 2, 23, 33 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `Connecticut4 ↔ NewJersey4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Virginia4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ NewJersey4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Michigan4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ Ohio4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Florida4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Pennsylvania4 ↔ PuertoRico4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ OntarioCanada4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ Ohio4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ NorthCarolina4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
