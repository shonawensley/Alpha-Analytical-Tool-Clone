# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-16

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `084f5de17cfaa687`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 559, 344, 044, 368, 346, 689, 569, 189 | 5, 24, 18, 15, 34, 23, 25, 35 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 2 | Delaware4 | 599, 559, 059, 399, 334, 019, 199, 159 | 15, 5, 34, 12, 9, 14, 35, 33 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 3 | Florida4 | 668, 006, 669, 255, 168, 699, 267, 126 | 18, 19, 3, 25, 15, 17, 10, 31 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 4 | Indiana4 | 599, 224, 559, 667, 799, 378, 699, 669 | 15, 28, 31, 27, 17, 26, 5, 10 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 5 | Michigan4 | 044, 067, 677, 455, 458, 558, 088, 122 | 15, 5, 20, 14, 7, 3, 1, 4 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 244, 099, 179, 001, 169, 019, 013 | 31, 2, 15, 25, 19, 3, 22, 9 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/0 |
| 7 | NewYork4 | 668, 003, 559, 599, 039, 007, 001 | 18, 15, 21, 4, 5, 14, 7, 3 | - | - | shared_host | Midday:OFF/1, Combined:OFF/0, Evening:OFF/0 |
| 8 | NorthCarolina4 | 138, 378, 366, 388, 338, 368, 334 | 23, 29, 18, 32, 8, 33, 4, 24 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 9 | Ohio4 | 069, 099, 338, 244, 046, 299, 334, 499 | 15, 9, 31, 35, 32, 5, 33, 4 | - | - | shared_host | Midday:ALERT/3, Combined:WATCH/2, Evening:WATCH/2 |
| 10 | OntarioCanada4 | 014, 138, 168, 223, 368, 001 | 23, 18, 9, 27, 21, 28, 29, 15 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 11 | Pennsylvania4 | 244, 599, 033, 224, 004, 006, 259, 008 | 5, 15, 23, 12, 13, 31, 32, 28 | - | - | shared_host | Combined:WATCH/2, Evening:OFF/0, Midday:OFF/0 |
| 12 | PuertoRico4 | 677, 445, 047, 224, 449, 077, 559, 067 | 20, 15, 12, 10, 28, 7, 35, 19 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 13 | SouthCarolina4 | 077, 455, 477, 022, 055, 559, 344, 244 | 10, 5, 3, 31, 1, 2, 4, 28 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/0 |
| 14 | Virginia4 | 559, 255, 259, 889, 599, 289, 688, 068 | 5, 3, 12, 15, 1, 8, 23, 7 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 267 | 35 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 315 | 39 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 189 | 23 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 314 | 39 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 269 | 34 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 238 | 30 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 307 | 36 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 202 | 26 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 289 | 34 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 173 | 22 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 005, 008, 334, 459, 559, 599 | 6 | 11 | False | True |
| NorthCarolina4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 004, 013, 133, 138, 336, 368 | 6 | 11 | False | True |
| Pennsylvania4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 259, 559, 599 | 6 | 11 | False | True |
| Indiana4 | Pennsylvania4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 28, 31, 5 | - | 7 | 11 | False | True |
| Delaware4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 009, 059, 559, 599 | 5 | 10 | False | True |
| Florida4 | NewYork4 | shared_box_family | lane/family | primary | - | 007, 136, 168, 668, 699 | 5 | 10 | False | True |
| Michigan4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 007, 559 | 5 | 10 | False | True |
| Michigan4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 445, 677 | 5 | 10 | False | True |
| Michigan4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 455, 559 | 5 | 10 | False | True |
| NewJersey4 | Ohio4 | shared_box_family | lane/family | primary | - | 009, 013, 099, 244, 299 | 5 | 10 | False | True |
| NewYork4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 007, 459, 559, 599 | 5 | 10 | False | True |
| Pennsylvania4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 224, 599 | 5 | 10 | False | True |
| Florida4 | NewJersey4 | shared_lane | lane/family | primary | 15, 18, 19, 2, 23, 25 | - | 6 | 10 | False | True |
| Indiana4 | NewYork4 | shared_lane | lane/family | primary | 12, 15, 17, 18, 23, 5 | - | 6 | 10 | False | True |
| Indiana4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 28, 15 | 224, 459, 599 | 3 | 9 | False | True |
| Indiana4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 28, 15 | 224, 445, 599 | 3 | 9 | False | True |
| Michigan4 | Ohio4 | alert_implied_echo | lane/family | primary | 15 | 044, 049, 099 | 3 | 9 | False | True |
| Virginia4 | Michigan4 | alert_implied_echo | lane/family | primary | 5 | 045, 455, 559 | 3 | 9 | False | True |
| Connecticut4 | NewJersey4 | shared_box_family | lane/family | primary | - | 011, 013, 014, 017 | 4 | 9 | False | True |
| Connecticut4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 013, 014, 368 | 4 | 9 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 009, 014, 019, 099 | 4 | 9 | False | True |
| Delaware4 | NewYork4 | shared_box_family | lane/family | primary | - | 019, 459, 559, 599 | 4 | 9 | False | True |
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 009, 049, 099, 599 | 4 | 9 | False | True |
| Indiana4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 017, 224, 445, 599 | 4 | 9 | False | True |
| Michigan4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 007, 455, 559 | 4 | 9 | False | True |
| NewJersey4 | NewYork4 | shared_box_family | lane/family | primary | - | 001, 013, 017, 019 | 4 | 9 | False | True |
| NewJersey4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 001, 011, 013, 014 | 4 | 9 | False | True |
| NorthCarolina4 | Ohio4 | shared_box_family | lane/family | primary | - | 004, 009, 013, 338 | 4 | 9 | False | True |
| Ohio4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 006, 244, 599 | 4 | 9 | False | True |
| Ohio4 | Virginia4 | shared_box_family | lane/family | primary | - | 004, 006, 009, 599 | 4 | 9 | False | True |
| OntarioCanada4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 004, 133, 336 | 4 | 9 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 009, 455, 559 | 4 | 9 | False | True |
| Delaware4 | Indiana4 | shared_lane | lane/family | primary | 12, 15, 18, 33, 5 | - | 5 | 9 | False | True |
| Florida4 | NewYork4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 3 | - | 5 | 9 | False | True |
| Florida4 | Pennsylvania4 | shared_lane | lane/family | primary | 12, 15, 18, 2, 23 | - | 5 | 9 | False | True |
| Indiana4 | NorthCarolina4 | shared_lane | lane/family | primary | 17, 18, 23, 29, 33 | - | 5 | 9 | False | True |
| Indiana4 | PuertoRico4 | shared_lane | lane/family | primary | 12, 15, 18, 28, 5 | - | 5 | 9 | False | True |
| Indiana4 | Virginia4 | shared_lane | lane/family | primary | 12, 15, 23, 33, 5 | - | 5 | 9 | False | True |
| Michigan4 | NewYork4 | shared_lane | lane/family | primary | 14, 15, 23, 4, 5 | - | 5 | 9 | False | True |
| NewJersey4 | Ohio4 | shared_lane | lane/family | primary | 15, 18, 23, 31, 9 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `Indiana4 ↔ PuertoRico4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Virginia4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ NewYork4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Ohio4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Pennsylvania4 ↔ Virginia4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Indiana4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ Virginia4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Delaware4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Pennsylvania4 ↔ PuertoRico4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NewJersey4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
