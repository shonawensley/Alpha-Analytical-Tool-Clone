# Predictive Portfolio — D=2026-01-17

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-17/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| Delaware4 | 27 | 219 | 13:009 | 009 088 117 223 | 4:004 009 117 | 5(6) | idx[20]:1,2,3,4…(36) |
| Ohio4 | 27 | 193 | 12:009 | 009 066 113 118 | 3:004 009 499 | 5(6) | idx[20]:2,3,4,5…(36) |
| Virginia4 | 27 | 177 | 11:004 | 004 177 199 334 | 3:004 455 599 | 5(6) | idx[20]:1,2,3,5…(36) |
| Indiana4 | 27 | 254 | 11:002 | 002 022 177 226 | 3:002 066 566 | 3(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | 27 | 171 | 10:112 | 112 119 155 199 | 4:112 117 119 | 7(8) | idx[20]:1,2,3,4…(36) |
| Connecticut4 | 27 | 186 | 10:088 | 088 099 223 228 | 3:088 389 588 | 14(8) | idx[20]:3,4,5,10…(36) |
| OntarioCanada4 | 27 | 201 | 10:004 | 004 044 144 228 | 2:004 044 | 15(6) | idx[20]:2,5,9,10…(36) |
| Pennsylvania4 | 27 | 220 | 10:007 | 007 066 228 255 | 2:007 118 | 23(6) | idx[20]:2,3,4,5…(36) |
| PuertoRico4 | 27 | 241 | 10:022 | 022 033 088 112 | 2:022 033 | 10(6) | idx[20]:2,4,5,6…(36) |
| Florida4 | 27 | 163 | 9:003 | 003 009 011 077 | 2:003 355 | 10(6) | idx[20]:1,3,4,5…(36) |
| NewYork4 | 27 | 188 | 9:001 | 001 007 011 066 | 4:001 007 377 | 18(6) | idx[20]:2,3,5,6…(36) |
| SouthCarolina4 | 27 | 188 | 9:114 | 114 115 155 224 | 3:114 224 466 | 19(6) | idx[20]:1,2,5,6…(36) |
| NorthCarolina4 | 27 | 215 | 9:001 | 001 009 044 225 | 3:001 225 277 | 26(2) | idx[22]:1,2,3,4…(36) |
| NewJersey4 | 27 | 219 | 9:022 | 022 114 155 339 | 2:022 348 | 9(8) | idx[20]:1,2,3,4…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

### B12 (`analysis_prefix`)
- **Delaware4**: `090 009 900 040 004 400 595 559 955 117 171 711`
- **Ohio4**: `009 090 900 004 934 499 949 994 040 400 349 394`
- **Virginia4**: `040 004 400 909 455 545 554 049 599 959 995 099`
- **Indiana4**: `020 002 200 660 665 566 066 606 656 177 226 262`
- **Michigan4**: `121 155 112 211 515 551 117 119 191 911 171 711`
- **Connecticut4**: `088 808 880 858 983 588 885 389 398 839 893 938`
- **OntarioCanada4**: `004 040 400 044 404 440 822 144 094 364 401 436`
- **Pennsylvania4**: `007 070 700 386 683 836 118 181 811 105 106 146`
- **PuertoRico4**: `022 202 220 033 303 330 808 168 186 618 681 816`
- **Florida4**: `355 003 030 300 535 553 752 237 057 075 507 570`
- **NewYork4**: `001 010 100 377 677 007 070 700 737 767 773 776`
- **SouthCarolina4**: `114 141 411 466 646 664 224 242 422 667 677 663`
- **NorthCarolina4**: `001 010 100 277 774 724 727 772 225 252 522 247`
- **NewJersey4**: `022 202 220 348 384 438 483 834 843 738 014 101`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-17/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 024 029 047 079 025 057 002 007 006 117 039 244 223 577 224 058 017 005 088 133 116 366 446 746` (src: `sharepacks/_predictive/2026-01-17/Delaware4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-17/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 349 489 344 399 348 389 334 339 077 499 097 249 779 113 149 138 093 358 066 003 006 007 109 198` (src: `sharepacks/_predictive/2026-01-17/Ohio4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-17/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,5…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 149 469 144 199 127 267 122 177 749 092 229 499 334 027 359 033 336 399 001 255 338 227 768 005` (src: `sharepacks/_predictive/2026-01-17/Virginia4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-17/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`025 057 002 007 255 557 016 156 011 066 115 566 136 168 113 118 127 267 122 177 159 603 605 368 334 022 035 114 599 678 005 266 026 778 399 124` (src: `sharepacks/_predictive/2026-01-17/Indiana4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=7(8)` pack=`012 017 026 067 125 157 256 567` (src: `sharepacks/_predictive/2026-01-17/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`126 167 112 117 266 667 015 056 001 006 155 556 012 017 026 067 016 156 011 066 255 592 113 119 199 058 014 559 229 244 225 055 599 177 344 348` (src: `sharepacks/_predictive/2026-01-17/Michigan4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=14(8)` pack=`034 039 048 089 345 359 458 589` (src: `sharepacks/_predictive/2026-01-17/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,4,5,10…(36)` pack=`038 358 033 088 335 588 034 039 048 089 345 359 348 389 334 339 023 028 037 078 469 244 828 868 948 223 099 388 224 559 225 255 008 226 289 167` (src: `sharepacks/_predictive/2026-01-17/Connecticut4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=15(6)` pack=`049 459 044 099 445 599` (src: `sharepacks/_predictive/2026-01-17/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,5,9,10…(36)` pack=`049 459 044 099 445 599 237 278 223 228 377 778 045 059 004 009 348 389 334 339 233 144 336 344 023 244 364 039 236 401 033 022 449 366 001 224` (src: `sharepacks/_predictive/2026-01-17/OntarioCanada4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=23(6)` pack=`138 368 133 188 336 688` (src: `sharepacks/_predictive/2026-01-17/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`016 156 011 066 115 566 025 057 002 007 255 557 136 168 113 118 146 169 114 119 386 234 028 003 244 105 045 689 034 599 339 017 024 388 227 344` (src: `sharepacks/_predictive/2026-01-17/Pennsylvania4/play_card__tool_only__stable10.json`)
- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-17/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,4,5,6…(36)` pack=`038 358 033 088 335 588 027 257 022 077 225 577 035 058 003 008 023 028 037 078 133 168 011 018 238 405 401 024 015 404 841 338 112 224 344 177` (src: `sharepacks/_predictive/2026-01-17/PuertoRico4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-17/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,3,4,5…(36)` pack=`035 058 003 008 355 558 027 257 022 077 225 577 023 028 037 078 237 278 223 228 255 138 738 009 178 388 011 599 055 224 177 244 227 358 169 467` (src: `sharepacks/_predictive/2026-01-17/Florida4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=18(6)` pack=`136 168 113 118 366 668` (src: `sharepacks/_predictive/2026-01-17/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`237 278 223 228 377 778 127 267 122 177 226 677 136 168 113 118 013 018 036 068 001 011 577 363 167 007 373 224 334 079 227 367 338 559 244 359` (src: `sharepacks/_predictive/2026-01-17/NewYork4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=19(6)` pack=`146 169 114 119 466 669` (src: `sharepacks/_predictive/2026-01-17/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,5,6…(36)` pack=`146 169 114 119 466 669 014 019 046 069 145 159 016 156 011 066 126 167 112 117 663 224 088 559 244 099 368 155 378 067 499 005 677 446 344 603` (src: `sharepacks/_predictive/2026-01-17/SouthCarolina4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=26(2)` pack=`227 277` (src: `sharepacks/_predictive/2026-01-17/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:1,2,3,4…(36)` pack=`247 279 224 229 477 779 024 029 047 079 245 259 227 277 027 257 022 077 424 144 001 344 287 438 045 454 721 234 233 003 258 255 005 156 069 169` (src: `sharepacks/_predictive/2026-01-17/NorthCarolina4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-17/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`146 169 114 119 466 669 012 017 026 067 125 157 014 019 046 069 348 389 334 339 022 559 088 113 738 008 368 259 344 155 057 018 446 449 005 708` (src: `sharepacks/_predictive/2026-01-17/NewJersey4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **Delaware4**: `045 059 004 009 455 559 117 599 097 005 017 039 259 006 750 094 940 088 223 232 322 808 880 244`
- **Ohio4**: `045 059 004 009 455 559 499 934 094 097 077 449 099 399 093 003 779 049 490 398 983 042 047 079`
- **Virginia4**: `045 059 004 009 455 559 909 594 049 599 499 449 092 259 229 459 495 954 749 267 094 490 940 540`
- **Indiana4**: `025 057 002 007 255 557 660 665 159 177 226 368 005 677 603 663 668 366 750 160 605 056 065 560`
- **Michigan4**: `012 017 026 067 125 157 256 567 121 155 117 592 119 255 559 101 151 115 259 295 952 150 152 521`
- **Connecticut4**: `034 039 048 089 345 359 458 589 088 858 983 253 258 868 388 469 496 649 694 859 946 964 235 285`
- **OntarioCanada4**: `049 459 044 099 445 599 004 822 144 336 449 364 401 039 334 023 028 073 228 282 414 441 009 090`
- **Pennsylvania4**: `138 368 133 188 336 688 007 028 244 234 388 118 034 668 055 638 863 868 886 105 106 146 101 832`
- **PuertoRico4**: `027 257 022 077 225 577 028 808 033 338 168 003 404 018 024 081 240 401 810 841 334 238 283 382`
- **Florida4**: `027 257 022 077 225 577 355 003 587 237 087 388 738 255 057 075 507 570 705 750 757 758 725 728`
- **NewYork4**: `136 168 113 118 366 668 001 377 677 367 007 177 363 373 227 277 636 663 686 866 163 316 361 386`
- **SouthCarolina4**: `146 169 114 119 466 669 667 064 224 499 677 005 663 446 041 145 014 019 046 460 640 115 151 155`
- **NorthCarolina4**: `227 277 001 774 245 724 224 225 424 144 454 744 149 194 287 419 438 491 782 834 872 914 941 524`
- **NewJersey4**: `014 019 046 069 145 159 456 569 022 449 348 101 018 738 012 017 062 114 141 155 339 393 411 515`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`)

- **Delaware4**: `045 059 004 009 455 559 049 459 044 099 445 599 024 029 047 079 025 057 002 007 006 117 039 244 223 577 224 058 017 005 088 133 116 366 446 746`
- **Ohio4**: `045 059 004 009 455 559 049 459 044 099 445 599 349 489 344 399 348 389 334 339 077 499 097 249 779 113 149 138 093 358 066 003 006 007 109 198`
- **Virginia4**: `045 059 004 009 455 559 049 459 044 099 445 599 149 469 144 199 127 267 122 177 749 092 229 499 334 027 359 033 336 399 001 255 338 227 768 005`
- **Indiana4**: `025 057 002 007 255 557 016 156 011 066 115 566 136 168 113 118 127 267 122 177 159 603 605 368 334 022 035 114 599 678 005 266 026 778 399 124`
- **Michigan4**: `126 167 112 117 266 667 015 056 001 006 155 556 012 017 026 067 016 156 011 066 255 592 113 119 199 058 014 559 229 244 225 055 599 177 344 348`
- **Connecticut4**: `038 358 033 088 335 588 034 039 048 089 345 359 348 389 334 339 023 028 037 078 469 244 828 868 948 223 099 388 224 559 225 255 008 226 289 167`
- **OntarioCanada4**: `049 459 044 099 445 599 237 278 223 228 377 778 045 059 004 009 348 389 334 339 233 144 336 344 023 244 364 039 236 401 033 022 449 366 001 224`
- **Pennsylvania4**: `016 156 011 066 115 566 025 057 002 007 255 557 136 168 113 118 146 169 114 119 386 234 028 003 244 105 045 689 034 599 339 017 024 388 227 344`
- **PuertoRico4**: `038 358 033 088 335 588 027 257 022 077 225 577 035 058 003 008 023 028 037 078 133 168 011 018 238 405 401 024 015 404 841 338 112 224 344 177`
- **Florida4**: `035 058 003 008 355 558 027 257 022 077 225 577 023 028 037 078 237 278 223 228 255 138 738 009 178 388 011 599 055 224 177 244 227 358 169 467`
- **NewYork4**: `237 278 223 228 377 778 127 267 122 177 226 677 136 168 113 118 013 018 036 068 001 011 577 363 167 007 373 224 334 079 227 367 338 559 244 359`
- **SouthCarolina4**: `146 169 114 119 466 669 014 019 046 069 145 159 016 156 011 066 126 167 112 117 663 224 088 559 244 099 368 155 378 067 499 005 677 446 344 603`
- **NorthCarolina4**: `247 279 224 229 477 779 024 029 047 079 245 259 227 277 027 257 022 077 424 144 001 344 287 438 045 454 721 234 233 003 258 255 005 156 069 169`
- **NewJersey4**: `146 169 114 119 466 669 012 017 026 067 125 157 014 019 046 069 348 389 334 339 022 559 088 113 738 008 368 259 344 155 057 018 446 449 005 708`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-17/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-17/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-17/<STATE>/play_card__tool_only*.json` (budgeted cuts)
