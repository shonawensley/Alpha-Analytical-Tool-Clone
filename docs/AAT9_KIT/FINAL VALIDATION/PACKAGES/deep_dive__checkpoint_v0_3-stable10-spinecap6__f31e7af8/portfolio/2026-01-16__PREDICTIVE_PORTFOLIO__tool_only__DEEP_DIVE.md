# Predictive Portfolio — D=2026-01-16

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-16/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| Delaware4 | 27 | 192 | 13:009 | 009 088 117 223 | 3:009 117 559 | 5(6) | idx[20]:1,2,3,5…(36) |
| Ohio4 | 27 | 205 | 12:009 | 009 066 113 118 | 3:004 009 559 | 5(6) | idx[22]:2,3,4,5…(36) |
| Virginia4 | 27 | 172 | 11:004 | 004 177 199 445 | 3:004 455 499 | 5(6) | idx[22]:1,3,5,6…(36) |
| OntarioCanada4 | 27 | 210 | 11:004 | 004 044 144 228 | 3:004 009 044 | 13(6) | idx[20]:2,3,4,5…(36) |
| NewYork4 | 27 | 199 | 10:001 | 001 007 011 066 | 3:001 011 377 | 8(8) | idx[20]:2,3,5,6…(36) |
| Pennsylvania4 | 27 | 214 | 10:007 | 007 066 228 255 | 3:007 044 344 | 23(6) | idx[20]:2,3,4,5…(36) |
| PuertoRico4 | 27 | 225 | 10:022 | 022 033 088 112 | 3:022 033 088 | 10(6) | idx[20]:1,2,3,4…(36) |
| Florida4 | 27 | 172 | 9:003 | 003 009 011 077 | 3:003 077 355 | 10(6) | idx[20]:3,4,5,6…(36) |
| Connecticut4 | 27 | 176 | 9:088 | 088 099 223 228 | 2:088 388 | 29(6) | idx[22]:5,6,11,13…(36) |
| SouthCarolina4 | 27 | 191 | 9:115 | 115 155 224 233 | 3:115 224 566 | 9(8) | idx[20]:1,2,5,6…(36) |
| Michigan4 | 27 | 200 | 9:112 | 112 119 155 199 | 4:112 117 155 | 2(6) | idx[20]:1,2,3,4…(36) |
| NorthCarolina4 | 27 | 221 | 9:001 | 001 009 044 225 | 2:001 225 | 26(2) | idx[22]:1,2,3,4…(36) |
| NewJersey4 | 27 | 228 | 9:022 | 022 114 155 339 | 1:022 | 7(8) | idx[20]:1,2,6,7…(36) |
| Indiana4 | 27 | 235 | 9:002 | 002 022 177 226 | 2:002 368 | 23(6) | idx[20]:2,3,5,6…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

### B12 (`analysis_prefix`)
- **Delaware4**: `009 090 900 095 590 595 059 559 955 117 171 711`
- **Ohio4**: `009 090 900 349 004 949 040 400 559 595 955 394`
- **Virginia4**: `040 004 400 909 455 545 554 499 949 994 059 940`
- **OntarioCanada4**: `004 040 400 830 044 404 440 009 090 900 038 083`
- **NewYork4**: `001 010 100 377 011 101 110 737 773 167 327 177`
- **Pennsylvania4**: `007 070 700 443 404 344 434 044 440 688 405 403`
- **PuertoRico4**: `022 202 220 033 088 303 330 808 880 003 008 030`
- **Florida4**: `003 030 300 752 077 707 770 753 355 535 553 237`
- **Connecticut4**: `088 808 880 838 893 983 898 938 389 398 388 883`
- **SouthCarolina4**: `115 151 511 224 242 422 677 566 656 665 466 646`
- **Michigan4**: `155 112 121 211 515 551 171 117 711 255 525 552`
- **NorthCarolina4**: `001 010 100 225 252 522 227 344 721 724 729 749`
- **NewJersey4**: `022 202 220 179 017 738 131 701 071 170 710 237`
- **Indiana4**: `002 020 200 386 683 638 633 836 368 863 835 833`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-16/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,5…(36)` pack=`045 059 004 009 455 559 024 029 047 079 245 259 126 167 112 117 034 039 048 089 015 110 249 146 007 599 017 224 449 088 223 177 577 005 136 688` (src: `sharepacks/_predictive/2026-01-16/Delaware4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-16/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:2,3,4,5…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 449 499 349 489 344 399 348 077 097 039 113 244 358 836 477 379 066 003 007 677 149 148 006 377` (src: `sharepacks/_predictive/2026-01-16/Ohio4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-16/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:1,3,5,6…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 149 469 144 199 449 499 249 092 169 145 016 126 224 335 359 177 336 338 255 225 608 339 227 005` (src: `sharepacks/_predictive/2026-01-16/Virginia4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=13(6)` pack=`038 358 033 088 335 588` (src: `sharepacks/_predictive/2026-01-16/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 237 278 223 228 035 058 003 008 830 344 029 025 336 233 093 346 334 014 022 449 144 244 001 126` (src: `sharepacks/_predictive/2026-01-16/OntarioCanada4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=8(8)` pack=`013 018 036 068 135 158 356 568` (src: `sharepacks/_predictive/2026-01-16/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`237 278 223 228 377 778 015 056 001 006 155 556 127 267 122 177 138 368 133 188 668 011 577 360 337 167 239 009 079 224 334 007 367 338 599 468` (src: `sharepacks/_predictive/2026-01-16/NewYork4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=23(6)` pack=`138 368 133 188 336 688` (src: `sharepacks/_predictive/2026-01-16/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`349 489 344 399 448 899 049 459 044 099 445 599 025 057 002 007 138 368 133 188 144 234 028 003 689 405 015 403 366 339 388 066 228 244 224 107` (src: `sharepacks/_predictive/2026-01-16/Pennsylvania4/play_card__tool_only__stable10.json`)
- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-16/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`027 257 022 077 225 577 023 028 037 078 235 258 038 358 033 088 045 059 004 009 013 205 003 238 138 001 127 204 034 148 338 224 044 112 449 005` (src: `sharepacks/_predictive/2026-01-16/PuertoRico4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-16/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,4,5,6…(36)` pack=`027 257 022 077 225 577 023 028 037 078 235 258 035 058 003 008 237 278 223 228 255 009 349 277 138 378 358 178 177 011 224 334 244 338 467 751` (src: `sharepacks/_predictive/2026-01-16/Florida4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=29(6)` pack=`238 378 233 288 337 788` (src: `sharepacks/_predictive/2026-01-16/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:5,6,11,13…(36)` pack=`238 378 233 288 337 788 348 389 334 339 488 889 038 358 033 088 338 388 136 089 144 223 368 869 099 169 899 244 932 224 559 116 037 227 862 016` (src: `sharepacks/_predictive/2026-01-16/Connecticut4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-16/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,5,6…(36)` pack=`016 156 011 066 115 566 136 168 113 118 366 668 138 368 133 188 014 019 046 069 244 233 224 667 088 559 687 466 155 099 067 499 005 677 344 573` (src: `sharepacks/_predictive/2026-01-16/SouthCarolina4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-16/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`015 056 001 006 155 556 126 167 112 117 266 667 149 469 144 199 146 169 114 119 101 035 249 254 131 129 138 559 348 255 224 445 014 344 055 125` (src: `sharepacks/_predictive/2026-01-16/Michigan4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=26(2)` pack=`227 277` (src: `sharepacks/_predictive/2026-01-16/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:1,2,3,4…(36)` pack=`247 279 224 229 477 779 024 029 047 079 245 259 227 277 045 059 004 009 144 001 424 344 287 225 334 721 044 134 003 678 255 133 156 233 338 005` (src: `sharepacks/_predictive/2026-01-16/NorthCarolina4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=7(8)` pack=`012 017 026 067 125 157 256 567` (src: `sharepacks/_predictive/2026-01-16/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,6,7…(36)` pack=`027 257 022 077 225 577 012 017 026 067 125 157 238 378 233 288 146 169 114 119 131 088 014 339 224 179 138 011 237 018 178 155 189 349 005 388` (src: `sharepacks/_predictive/2026-01-16/NewJersey4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=23(6)` pack=`138 368 133 188 336 688` (src: `sharepacks/_predictive/2026-01-16/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`138 368 133 188 336 688 013 018 036 068 135 158 136 168 113 118 038 358 033 088 014 566 002 177 339 833 022 599 678 369 778 559 667 114 600 399` (src: `sharepacks/_predictive/2026-01-16/Indiana4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **Delaware4**: `045 059 004 009 455 559 117 449 167 015 093 259 146 110 088 223 232 322 808 880 249 294 299 429`
- **Ohio4**: `045 059 004 009 455 559 949 349 097 077 049 449 836 003 007 348 042 047 079 790 970 066 113 118`
- **Virginia4**: `045 059 004 009 455 559 499 449 909 594 940 599 249 092 335 338 459 495 954 649 904 049 094 490`
- **OntarioCanada4**: `038 358 033 088 335 588 004 094 029 009 044 449 093 223 344 434 443 850 024 074 092 290 920 144`
- **NewYork4**: `013 018 036 068 135 158 356 568 001 377 011 363 338 668 337 136 163 316 361 613 631 009 167 327`
- **Pennsylvania4**: `138 368 133 188 336 688 007 443 404 028 388 403 689 055 405 023 073 082 280 820 066 228 255 282`
- **PuertoRico4**: `027 257 022 077 225 577 033 338 028 088 004 003 008 204 013 034 072 103 207 270 275 527 572 702`
- **Florida4**: `027 257 022 077 225 577 003 753 237 073 177 277 355 377 255 735 757 775 537 349 573 725 273 372`
- **Connecticut4**: `238 378 233 288 337 788 893 838 088 898 858 899 089 338 869 968 332 828 382 832 882 932 783 099`
- **SouthCarolina4**: `014 019 046 069 145 159 456 569 115 677 566 224 499 005 466 667 687 477 683 156 165 561 651 401`
- **Michigan4**: `015 056 001 006 155 556 171 112 129 141 255 101 131 151 254 524 138 348 249 294 492 942 150 941`
- **NorthCarolina4**: `227 277 001 344 245 224 225 424 144 149 287 948 721 724 729 749 247 045 024 029 074 254 452 542`
- **NewJersey4**: `012 017 026 067 125 157 256 567 022 179 449 018 131 738 237 027 072 270 720 062 114 141 155 339`
- **Indiana4**: `138 368 133 188 336 688 086 002 835 833 830 636 838 566 668 183 136 613 038 083 380 630 031 036`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`)

- **Delaware4**: `045 059 004 009 455 559 024 029 047 079 245 259 126 167 112 117 034 039 048 089 015 110 249 146 007 599 017 224 449 088 223 177 577 005 136 688`
- **Ohio4**: `045 059 004 009 455 559 049 459 044 099 445 599 449 499 349 489 344 399 348 077 097 039 113 244 358 836 477 379 066 003 007 677 149 148 006 377`
- **Virginia4**: `045 059 004 009 455 559 049 459 044 099 445 599 149 469 144 199 449 499 249 092 169 145 016 126 224 335 359 177 336 338 255 225 608 339 227 005`
- **OntarioCanada4**: `045 059 004 009 455 559 049 459 044 099 445 599 237 278 223 228 035 058 003 008 830 344 029 025 336 233 093 346 334 014 022 449 144 244 001 126`
- **NewYork4**: `237 278 223 228 377 778 015 056 001 006 155 556 127 267 122 177 138 368 133 188 668 011 577 360 337 167 239 009 079 224 334 007 367 338 599 468`
- **Pennsylvania4**: `349 489 344 399 448 899 049 459 044 099 445 599 025 057 002 007 138 368 133 188 144 234 028 003 689 405 015 403 366 339 388 066 228 244 224 107`
- **PuertoRico4**: `027 257 022 077 225 577 023 028 037 078 235 258 038 358 033 088 045 059 004 009 013 205 003 238 138 001 127 204 034 148 338 224 044 112 449 005`
- **Florida4**: `027 257 022 077 225 577 023 028 037 078 235 258 035 058 003 008 237 278 223 228 255 009 349 277 138 378 358 178 177 011 224 334 244 338 467 751`
- **Connecticut4**: `238 378 233 288 337 788 348 389 334 339 488 889 038 358 033 088 338 388 136 089 144 223 368 869 099 169 899 244 932 224 559 116 037 227 862 016`
- **SouthCarolina4**: `016 156 011 066 115 566 136 168 113 118 366 668 138 368 133 188 014 019 046 069 244 233 224 667 088 559 687 466 155 099 067 499 005 677 344 573`
- **Michigan4**: `015 056 001 006 155 556 126 167 112 117 266 667 149 469 144 199 146 169 114 119 101 035 249 254 131 129 138 559 348 255 224 445 014 344 055 125`
- **NorthCarolina4**: `247 279 224 229 477 779 024 029 047 079 245 259 227 277 045 059 004 009 144 001 424 344 287 225 334 721 044 134 003 678 255 133 156 233 338 005`
- **NewJersey4**: `027 257 022 077 225 577 012 017 026 067 125 157 238 378 233 288 146 169 114 119 131 088 014 339 224 179 138 011 237 018 178 155 189 349 005 388`
- **Indiana4**: `138 368 133 188 336 688 013 018 036 068 135 158 136 168 113 118 038 358 033 088 014 566 002 177 339 833 022 599 678 369 778 559 667 114 600 399`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-16/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-16/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-16/<STATE>/play_card__tool_only*.json` (budgeted cuts)
