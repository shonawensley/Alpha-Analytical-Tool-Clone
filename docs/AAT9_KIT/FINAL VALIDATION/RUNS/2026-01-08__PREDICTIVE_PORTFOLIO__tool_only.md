# Predictive Portfolio — D=2026-01-08

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| NewYork4 | 27 | 172 | 13:001 | 001 007 011 066 | 2:001 011 | 2(6) | idx[20]:1,2,3,4…(36) |
| PuertoRico4 | 27 | 253 | 13:022 | 022 033 199 299 | 3:022 033 225 | 10(6) | idx[16]:2,3,4,8…(36) |
| NewJersey4 | 27 | 183 | 11:022 | 022 114 155 339 | 3:022 077 088 | 10(6) | idx[16]:1,2,9,10…(36) |
| SouthCarolina4 | 27 | 186 | 11:115 | 115 155 224 233 | 2:115 224 | 6(6) | idx[16]:1,2,3,5…(36) |
| Delaware4 | 27 | 212 | 10:009 | 009 088 223 228 | 3:009 011 559 | 5(6) | idx[16]:2,4,5,6…(36) |
| OntarioCanada4 | 27 | 230 | 10:004 | 004 044 144 228 | 4:004 044 224 | 12(8) | idx[16]:1,2,3,5…(36) |
| Florida4 | 27 | 157 | 9:003 | 003 009 011 077 | 2:003 334 | 33(6) | idx[16]:4,5,6,8…(36) |
| Connecticut4 | 27 | 175 | 9:088 | 088 099 223 228 | 2:088 228 | 34(6) | idx[16]:5,10,13,15…(36) |
| NorthCarolina4 | 27 | 193 | 9:001 | 001 009 044 225 | 3:001 009 044 | 31(6) | idx[16]:2,3,4,5…(36) |
| Michigan4 | 27 | 198 | 9:112 | 112 119 155 199 | 3:112 117 119 | 9(8) | idx[16]:2,5,6,9…(36) |
| Ohio4 | 27 | 201 | 9:009 | 009 066 113 118 | 4:009 088 559 | 4(6) | idx[16]:1,4,5,6…(36) |
| Pennsylvania4 | 27 | 217 | 9:007 | 007 066 228 255 | 2:007 557 | 5(6) | idx[16]:2,3,5,6…(36) |
| Virginia4 | 27 | 231 | 9:004 | 004 177 199 377 | 2:004 136 | 9(8) | idx[16]:5,6,9,15…(36) |
| Indiana4 | 27 | 246 | 9:002 | 002 022 177 226 | 3:002 066 266 | 12(8) | idx[16]:3,5,6,9…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`

### B12 (`analysis_prefix`)
- **NewYork4**: `010 001 100 507 060 005 011 101 110 007 066 070`
- **PuertoRico4**: `220 022 202 225 252 522 028 280 033 303 330 207`
- **NewJersey4**: `022 220 202 077 770 189 707 088 788 808 878 880`
- **SouthCarolina4**: `151 115 511 059 224 242 422 665 095 509 590 905`
- **Delaware4**: `009 090 900 559 595 955 011 034 101 110 114 141`
- **OntarioCanada4**: `004 040 400 224 044 404 440 455 545 554 242 422`
- **Florida4**: `003 030 300 343 334 436 335 433 033 233 303 323`
- **Connecticut4**: `088 808 880 424 484 448 228 282 822 824 248 894`
- **NorthCarolina4**: `001 010 100 044 404 440 244 009 090 900 940 964`
- **Michigan4**: `112 121 211 119 191 911 155 117 171 711 051 141`
- **Ohio4**: `009 090 900 889 559 595 955 898 988 088 808 880`
- **Pennsylvania4**: `007 070 700 112 557 575 755 059 095 509 590 905`
- **Virginia4**: `004 040 400 361 349 059 136 163 316 613 631 114`
- **Indiana4**: `002 020 200 066 606 660 266 626 662 636 054 093`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **NewYork4**: B24 `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-08/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`015 056 001 006 155 556 016 156 011 066 115 566 025 057 002 007 255 557 005 055 008 668 256 808 559 802 449 224 599 227 667 244 245 378 804 169` (src: `sharepacks/_predictive/2026-01-08/NewYork4/play_card__tool_only__stable10.json`)
- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-08/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,3,4,8…(36)` pack=`027 257 022 077 225 577 023 028 037 078 235 258 038 358 033 088 335 588 025 057 002 007 255 557 800 245 278 668 199 299 068 006 224 388 238 688` (src: `sharepacks/_predictive/2026-01-08/PuertoRico4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-08/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,9,10…(36)` pack=`027 257 022 077 225 577 146 169 114 119 466 669 134 139 148 189 346 369 348 389 334 339 488 889 788 138 287 014 186 155 078 088 005 089 126 182` (src: `sharepacks/_predictive/2026-01-08/NewJersey4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-08/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,3,5…(36)` pack=`016 156 011 066 115 566 014 019 046 069 145 159 045 059 004 009 455 559 134 139 148 189 346 369 599 233 699 155 224 336 667 499 002 244 669 005` (src: `sharepacks/_predictive/2026-01-08/SouthCarolina4/play_card__tool_only__stable10.json`)
- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-08/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,4,5,6…(36)` pack=`045 059 004 009 455 559 034 039 048 089 345 359 016 156 011 066 115 566 136 168 113 118 366 668 044 053 114 414 088 344 334 338 105 133 814 801` (src: `sharepacks/_predictive/2026-01-08/Delaware4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-08/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,3,5…(36)` pack=`045 059 004 009 455 559 247 279 224 229 477 779 027 257 022 077 225 577 024 029 047 079 245 259 044 228 055 244 015 263 401 677 002 234 144 011` (src: `sharepacks/_predictive/2026-01-08/OntarioCanada4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=33(6)` pack=`348 389 334 339 488 889` (src: `sharepacks/_predictive/2026-01-08/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:4,5,6,8…(36)` pack=`348 389 334 339 488 889 038 358 033 088 335 588 138 368 133 188 336 688 016 156 011 066 115 566 003 436 034 023 224 338 009 234 233 316 029 536` (src: `sharepacks/_predictive/2026-01-08/Florida4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=34(6)` pack=`349 489 344 399 448 899` (src: `sharepacks/_predictive/2026-01-08/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:5,10,13,15…(36)` pack=`349 489 344 399 448 899 234 239 248 289 347 379 249 479 244 299 447 799 049 459 044 099 445 599 228 224 088 388 889 144 494 116 559 225 468 227` (src: `sharepacks/_predictive/2026-01-08/Connecticut4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=31(6)` pack=`249 479 244 299 447 799` (src: `sharepacks/_predictive/2026-01-08/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,3,4,5…(36)` pack=`049 459 044 099 445 599 249 479 244 299 447 799 149 469 144 199 446 699 015 056 001 006 155 556 466 920 009 899 225 066 003 025 944 648 227 224` (src: `sharepacks/_predictive/2026-01-08/NorthCarolina4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-08/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,5,6,9…(36)` pack=`126 167 112 117 266 667 014 019 046 069 145 159 015 056 001 006 155 556 146 169 114 119 466 669 194 181 471 151 559 599 277 161 449 244 344 338` (src: `sharepacks/_predictive/2026-01-08/Michigan4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=4(6)` pack=`035 058 003 008 355 558` (src: `sharepacks/_predictive/2026-01-08/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,4,5,6…(36)` pack=`045 059 004 009 455 559 348 389 334 339 488 889 035 058 003 008 355 558 038 358 033 088 335 588 098 899 788 929 066 599 022 005 113 116 388 188` (src: `sharepacks/_predictive/2026-01-08/Ohio4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-08/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,3,5,6…(36)` pack=`025 057 002 007 255 557 015 056 001 006 155 556 016 156 011 066 115 566 237 278 223 228 377 778 445 059 112 019 012 114 818 414 227 338 339 224` (src: `sharepacks/_predictive/2026-01-08/Pennsylvania4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-08/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:5,6,9,15…(36)` pack=`045 059 004 009 455 559 146 169 114 119 466 669 049 459 044 099 445 599 014 019 046 069 145 159 149 349 361 341 061 234 449 244 177 377 224 117` (src: `sharepacks/_predictive/2026-01-08/Virginia4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-08/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:3,5,6,9…(36)` pack=`146 169 114 119 466 669 126 167 112 117 266 667 024 029 047 079 245 259 127 267 122 177 226 677 002 224 609 636 788 476 054 447 066 093 448 334` (src: `sharepacks/_predictive/2026-01-08/Indiana4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **NewYork4**: `015 056 001 006 155 556 005 507 011 007 066 256 668 808 008 118 508 561 510 224 242 422 449 494`
- **PuertoRico4**: `027 257 022 077 225 577 028 033 388 200 800 068 238 205 023 073 199 299 919 929 991 992 244 424`
- **NewJersey4**: `027 257 022 077 225 577 189 088 788 078 005 089 119 186 138 183 126 287 782 072 572 114 141 155`
- **SouthCarolina4**: `016 156 011 066 115 566 059 599 595 224 499 699 906 936 336 369 005 050 500 695 596 106 601 651`
- **Delaware4**: `045 059 004 009 455 559 034 011 044 334 338 114 414 811 105 054 450 540 053 039 084 345 354 453`
- **OntarioCanada4**: `024 029 047 079 245 259 457 579 004 224 044 455 055 225 263 367 401 015 677 270 274 279 220 074`
- **Florida4**: `348 389 334 339 488 889 003 436 335 336 338 033 233 034 234 243 340 342 430 432 316 023 028 073`
- **Connecticut4**: `349 489 344 399 448 899 248 298 424 088 224 228 388 229 144 414 441 494 249 294 492 498 942 243`
- **NorthCarolina4**: `249 479 244 299 447 799 044 001 964 940 920 009 006 466 144 414 441 446 464 644 899 989 998 469`
- **Michigan4**: `014 019 046 069 145 159 456 569 112 119 155 117 181 471 668 277 051 141 151 154 194 941 591 951`
- **Ohio4**: `035 058 003 008 355 558 889 009 559 899 022 088 929 005 055 080 800 893 938 588 098 053 066 113`
- **Pennsylvania4**: `045 059 004 009 455 559 007 112 557 414 445 818 015 012 017 062 125 152 251 521 066 228 255 282`
- **Virginia4**: `014 019 046 069 145 159 456 569 004 361 349 059 114 061 341 344 146 169 149 194 491 941 041 049`
- **Indiana4**: `024 029 047 079 245 259 457 579 002 066 224 266 636 054 093 247 274 427 472 609 724 742 906 447`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`)

- **NewYork4**: `015 056 001 006 155 556 016 156 011 066 115 566 025 057 002 007 255 557 005 055 008 668 256 808 559 802 449 224 599 227 667 244 245 378 804 169`
- **PuertoRico4**: `027 257 022 077 225 577 023 028 037 078 235 258 038 358 033 088 335 588 025 057 002 007 255 557 800 245 278 668 199 299 068 006 224 388 238 688`
- **NewJersey4**: `027 257 022 077 225 577 146 169 114 119 466 669 134 139 148 189 346 369 348 389 334 339 488 889 788 138 287 014 186 155 078 088 005 089 126 182`
- **SouthCarolina4**: `016 156 011 066 115 566 014 019 046 069 145 159 045 059 004 009 455 559 134 139 148 189 346 369 599 233 699 155 224 336 667 499 002 244 669 005`
- **Delaware4**: `045 059 004 009 455 559 034 039 048 089 345 359 016 156 011 066 115 566 136 168 113 118 366 668 044 053 114 414 088 344 334 338 105 133 814 801`
- **OntarioCanada4**: `045 059 004 009 455 559 247 279 224 229 477 779 027 257 022 077 225 577 024 029 047 079 245 259 044 228 055 244 015 263 401 677 002 234 144 011`
- **Florida4**: `348 389 334 339 488 889 038 358 033 088 335 588 138 368 133 188 336 688 016 156 011 066 115 566 003 436 034 023 224 338 009 234 233 316 029 536`
- **Connecticut4**: `349 489 344 399 448 899 234 239 248 289 347 379 249 479 244 299 447 799 049 459 044 099 445 599 228 224 088 388 889 144 494 116 559 225 468 227`
- **NorthCarolina4**: `049 459 044 099 445 599 249 479 244 299 447 799 149 469 144 199 446 699 015 056 001 006 155 556 466 920 009 899 225 066 003 025 944 648 227 224`
- **Michigan4**: `126 167 112 117 266 667 014 019 046 069 145 159 015 056 001 006 155 556 146 169 114 119 466 669 194 181 471 151 559 599 277 161 449 244 344 338`
- **Ohio4**: `045 059 004 009 455 559 348 389 334 339 488 889 035 058 003 008 355 558 038 358 033 088 335 588 098 899 788 929 066 599 022 005 113 116 388 188`
- **Pennsylvania4**: `025 057 002 007 255 557 015 056 001 006 155 556 016 156 011 066 115 566 237 278 223 228 377 778 445 059 112 019 012 114 818 414 227 338 339 224`
- **Virginia4**: `045 059 004 009 455 559 146 169 114 119 466 669 049 459 044 099 445 599 014 019 046 069 145 159 149 349 361 341 061 234 449 244 177 377 224 117`
- **Indiana4**: `146 169 114 119 466 669 126 167 112 117 266 667 024 029 047 079 245 259 127 267 122 177 226 677 002 224 609 636 788 476 054 447 066 093 448 334`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-08/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-08/<STATE>/play_card__tool_only*.json` (budgeted cuts)
