# Predictive Portfolio — D=2026-01-15

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-15/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| Delaware4 | 27 | 203 | 12:009 | 009 088 117 223 | 3:004 009 559 | 5(6) | idx[20]:2,3,4,5…(36) |
| Virginia4 | 27 | 183 | 11:004 | 004 177 199 445 | 3:004 445 499 | 5(6) | idx[22]:1,5,6,7…(36) |
| OntarioCanada4 | 27 | 209 | 11:004 | 004 044 144 228 | 2:004 009 | 12(8) | idx[20]:3,4,5,8…(36) |
| Ohio4 | 27 | 198 | 10:009 | 009 066 113 118 | 2:009 559 | 14(8) | idx[20]:3,4,5,6…(36) |
| NewYork4 | 27 | 200 | 10:001 | 001 007 011 066 | 3:001 011 377 | 8(8) | idx[20]:2,3,6,7…(36) |
| Pennsylvania4 | 27 | 208 | 10:007 | 007 066 228 255 | 3:007 244 344 | 23(6) | idx[20]:1,3,4,6…(36) |
| PuertoRico4 | 27 | 217 | 10:022 | 022 033 088 112 | 2:022 033 | 10(6) | idx[20]:1,2,3,4…(36) |
| Florida4 | 27 | 179 | 9:003 | 003 009 011 077 | 2:003 077 | 10(6) | idx[20]:2,3,4,5…(36) |
| Connecticut4 | 27 | 184 | 9:088 | 088 099 223 228 | 2:088 389 | 34(6) | idx[20]:3,5,6,7…(36) |
| Michigan4 | 27 | 191 | 9:112 | 112 119 155 199 | 2:112 155 | 2(6) | idx[20]:1,2,3,4…(36) |
| SouthCarolina4 | 27 | 198 | 9:115 | 115 155 224 233 | 3:115 224 334 | 9(8) | idx[20]:2,5,6,7…(36) |
| NewJersey4 | 27 | 202 | 9:022 | 022 114 155 339 | 1:022 | 22(8) | idx[20]:1,2,3,4…(36) |
| NorthCarolina4 | 27 | 226 | 9:001 | 001 009 044 225 | 2:001 225 | 12(8) | idx[20]:1,2,3,4…(36) |
| Indiana4 | 27 | 229 | 9:002 | 002 022 177 226 | 1:002 | 23(6) | idx[20]:1,3,5,6…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

### B12 (`analysis_prefix`)
- **Delaware4**: `090 009 900 040 595 004 400 559 955 095 590 059`
- **Virginia4**: `040 004 400 499 949 994 445 454 544 249 294 429`
- **OntarioCanada4**: `004 040 400 009 090 900 025 038 052 083 205 250`
- **Ohio4**: `009 090 900 349 983 559 595 955 394 439 493 934`
- **NewYork4**: `001 010 100 377 011 101 110 660 737 773 177 717`
- **Pennsylvania4**: `007 070 700 443 244 424 442 344 434 688 404 446`
- **PuertoRico4**: `022 202 220 303 080 300 138 183 831 033 088 330`
- **Florida4**: `003 030 300 752 737 257 077 707 770 727 355 535`
- **Connecticut4**: `088 808 880 389 998 892 899 398 893 983 839 938`
- **Michigan4**: `155 112 121 211 515 551 150 015 105 501 117 171`
- **SouthCarolina4**: `115 151 511 224 242 422 641 334 343 433 683 647`
- **NewJersey4**: `022 202 220 136 016 613 631 719 179 061 106 138`
- **NorthCarolina4**: `001 010 100 225 252 522 344 724 725 729 749 245`
- **Indiana4**: `002 020 200 633 830 038 083 833 803 386 683 338`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-15/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`045 059 004 009 455 559 024 029 047 079 245 259 249 479 244 299 146 169 114 119 459 117 001 344 149 011 224 179 088 223 007 177 339 140 739 035` (src: `sharepacks/_predictive/2026-01-15/Delaware4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-15/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:1,5,6,7…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 149 469 144 199 449 499 249 349 169 016 126 033 359 005 177 224 336 338 339 227 017 587 624 609` (src: `sharepacks/_predictive/2026-01-15/Virginia4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-15/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,4,5,8…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 237 278 223 228 025 057 002 007 850 389 344 038 029 233 390 022 239 449 144 244 310 224 226 014` (src: `sharepacks/_predictive/2026-01-15/OntarioCanada4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=14(8)` pack=`034 039 048 089 345 359 458 589` (src: `sharepacks/_predictive/2026-01-15/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,4,5,6…(36)` pack=`034 039 048 089 345 359 349 489 344 399 448 899 045 059 004 009 238 378 233 288 983 022 386 249 032 099 113 379 066 677 116 388 007 003 126 129` (src: `sharepacks/_predictive/2026-01-15/Ohio4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=8(8)` pack=`013 018 036 068 135 158 356 568` (src: `sharepacks/_predictive/2026-01-15/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,6,7…(36)` pack=`016 156 011 066 115 566 015 056 001 006 155 556 127 267 122 177 237 278 223 228 136 563 027 249 017 167 334 079 224 346 347 367 007 336 599 337` (src: `sharepacks/_predictive/2026-01-15/NewYork4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=23(6)` pack=`138 368 133 188 336 688` (src: `sharepacks/_predictive/2026-01-15/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,3,4,6…(36)` pack=`025 057 002 007 255 557 349 489 344 399 448 899 049 459 044 099 249 479 244 299 234 688 446 668 066 466 028 228 036 339 388 233 005 224 403 003` (src: `sharepacks/_predictive/2026-01-15/Pennsylvania4/play_card__tool_only__stable10.json`)
- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-15/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`038 358 033 088 335 588 035 058 003 008 355 558 027 257 022 077 015 056 001 006 138 013 238 034 028 004 334 338 112 005 244 002 224 227 449 177` (src: `sharepacks/_predictive/2026-01-15/PuertoRico4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-15/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`027 257 022 077 225 577 237 278 223 228 377 778 023 028 037 078 035 058 003 008 255 177 334 056 009 727 178 368 378 349 338 011 224 599 169 244` (src: `sharepacks/_predictive/2026-01-15/Florida4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=34(6)` pack=`349 489 344 399 448 899` (src: `sharepacks/_predictive/2026-01-15/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,5,6,7…(36)` pack=`349 489 344 399 448 899 038 358 033 088 335 588 348 389 334 339 034 039 048 089 995 892 368 144 244 223 233 559 338 224 255 116 227 968 016 125` (src: `sharepacks/_predictive/2026-01-15/Connecticut4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-15/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`015 056 001 006 155 556 126 167 112 117 266 667 146 169 114 119 014 019 046 069 016 131 124 244 355 199 245 013 559 055 348 255 445 138 227 344` (src: `sharepacks/_predictive/2026-01-15/Michigan4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-15/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,5,6,7…(36)` pack=`014 019 046 069 145 159 016 156 011 066 115 566 138 368 133 188 136 168 113 118 334 224 687 049 641 344 449 068 468 358 647 004 155 233 446 567` (src: `sharepacks/_predictive/2026-01-15/SouthCarolina4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=22(8)` pack=`124 129 147 179 246 269 467 679` (src: `sharepacks/_predictive/2026-01-15/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`124 129 147 179 246 269 136 168 113 118 366 668 016 156 011 066 126 167 112 117 138 022 119 344 013 012 144 449 001 019 378 339 055 003 029 025` (src: `sharepacks/_predictive/2026-01-15/NewJersey4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-15/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`027 257 022 077 225 577 024 029 047 079 245 259 247 279 224 229 045 059 004 009 001 749 344 044 144 334 052 223 003 134 277 178 177 133 156 005` (src: `sharepacks/_predictive/2026-01-15/NorthCarolina4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=23(6)` pack=`138 368 133 188 336 688` (src: `sharepacks/_predictive/2026-01-15/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,3,5,6…(36)` pack=`138 368 133 188 336 688 038 358 033 088 335 588 013 018 036 068 136 168 113 118 906 002 177 334 833 066 022 599 009 114 678 667 399 116 278 005` (src: `sharepacks/_predictive/2026-01-15/Indiana4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **Delaware4**: `045 059 004 009 455 559 079 459 149 749 119 088 117 223 249 294 299 429 492 709 790 907 924 929`
- **Virginia4**: `045 059 004 009 455 559 499 449 594 599 445 249 005 349 909 946 964 049 094 490 940 540 177 199`
- **OntarioCanada4**: `024 029 047 079 245 259 457 579 004 009 449 025 038 389 002 390 022 225 049 094 490 940 344 434`
- **Ohio4**: `034 039 048 089 345 359 458 589 009 349 983 559 399 099 386 837 379 397 793 973 116 388 328 032`
- **NewYork4**: `013 018 036 068 135 158 356 568 001 377 660 011 677 334 336 177 717 771 136 163 316 361 613 631`
- **Pennsylvania4**: `138 368 133 188 336 688 007 443 028 244 388 446 234 293 005 055 404 023 073 082 280 820 066 228`
- **PuertoRico4**: `027 257 022 077 225 577 303 080 300 138 380 028 088 001 338 383 833 318 381 813 005 006 013 386`
- **Florida4**: `027 257 022 077 225 577 727 003 737 073 177 355 338 537 237 273 372 732 023 028 037 370 730 009`
- **Connecticut4**: `349 489 344 399 448 899 389 892 088 858 995 089 338 368 895 898 598 928 289 982 948 233 238 283`
- **Michigan4**: `015 056 001 006 155 556 112 154 344 117 131 255 141 014 055 348 145 245 254 451 452 542 506 355`
- **SouthCarolina4**: `014 019 046 069 145 159 456 569 115 641 224 449 499 687 334 647 049 677 041 104 401 640 683 146`
- **NewJersey4**: `124 129 147 179 246 269 467 679 136 022 016 449 019 499 138 368 381 386 601 610 638 683 813 831`
- **NorthCarolina4**: `024 029 047 079 245 259 457 579 225 001 344 277 144 000 134 724 725 729 749 052 250 520 074 009`
- **Indiana4**: `138 368 133 188 336 688 830 086 002 833 838 668 635 636 906 631 630 031 036 022 177 202 220 226`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`)

- **Delaware4**: `045 059 004 009 455 559 024 029 047 079 245 259 249 479 244 299 146 169 114 119 459 117 001 344 149 011 224 179 088 223 007 177 339 140 739 035`
- **Virginia4**: `045 059 004 009 455 559 049 459 044 099 445 599 149 469 144 199 449 499 249 349 169 016 126 033 359 005 177 224 336 338 339 227 017 587 624 609`
- **OntarioCanada4**: `045 059 004 009 455 559 049 459 044 099 445 599 237 278 223 228 025 057 002 007 850 389 344 038 029 233 390 022 239 449 144 244 310 224 226 014`
- **Ohio4**: `034 039 048 089 345 359 349 489 344 399 448 899 045 059 004 009 238 378 233 288 983 022 386 249 032 099 113 379 066 677 116 388 007 003 126 129`
- **NewYork4**: `016 156 011 066 115 566 015 056 001 006 155 556 127 267 122 177 237 278 223 228 136 563 027 249 017 167 334 079 224 346 347 367 007 336 599 337`
- **Pennsylvania4**: `025 057 002 007 255 557 349 489 344 399 448 899 049 459 044 099 249 479 244 299 234 688 446 668 066 466 028 228 036 339 388 233 005 224 403 003`
- **PuertoRico4**: `038 358 033 088 335 588 035 058 003 008 355 558 027 257 022 077 015 056 001 006 138 013 238 034 028 004 334 338 112 005 244 002 224 227 449 177`
- **Florida4**: `027 257 022 077 225 577 237 278 223 228 377 778 023 028 037 078 035 058 003 008 255 177 334 056 009 727 178 368 378 349 338 011 224 599 169 244`
- **Connecticut4**: `349 489 344 399 448 899 038 358 033 088 335 588 348 389 334 339 034 039 048 089 995 892 368 144 244 223 233 559 338 224 255 116 227 968 016 125`
- **Michigan4**: `015 056 001 006 155 556 126 167 112 117 266 667 146 169 114 119 014 019 046 069 016 131 124 244 355 199 245 013 559 055 348 255 445 138 227 344`
- **SouthCarolina4**: `014 019 046 069 145 159 016 156 011 066 115 566 138 368 133 188 136 168 113 118 334 224 687 049 641 344 449 068 468 358 647 004 155 233 446 567`
- **NewJersey4**: `124 129 147 179 246 269 136 168 113 118 366 668 016 156 011 066 126 167 112 117 138 022 119 344 013 012 144 449 001 019 378 339 055 003 029 025`
- **NorthCarolina4**: `027 257 022 077 225 577 024 029 047 079 245 259 247 279 224 229 045 059 004 009 001 749 344 044 144 334 052 223 003 134 277 178 177 133 156 005`
- **Indiana4**: `138 368 133 188 336 688 038 358 033 088 335 588 013 018 036 068 136 168 113 118 906 002 177 334 833 066 022 599 009 114 678 667 399 116 278 005`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-15/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-15/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-15/<STATE>/play_card__tool_only*.json` (budgeted cuts)
