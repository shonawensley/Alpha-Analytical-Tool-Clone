# Predictive Portfolio — D=2026-01-03

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-03/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| PuertoRico4 | 27 | 246 | 13:022 | 022 033 088 199 | 2:022 225 | 10(6) | idx[20]:3,7,8,10…(36) |
| Pennsylvania4 | 27 | 198 | 12:007 | 007 228 255 277 | 2:007 057 | 3(6) | idx[20]:1,2,3,5…(36) |
| Delaware4 | 27 | 187 | 11:009 | 009 088 223 228 | 3:004 009 559 | 5(6) | idx[22]:1,2,5,6…(36) |
| Ohio4 | 27 | 159 | 10:009 | 009 066 113 114 | 1:009 | 3(6) | idx[20]:1,2,3,4…(36) |
| NewJersey4 | 27 | 171 | 10:022 | 022 114 155 339 | 3:022 077 225 | 10(6) | idx[20]:1,2,5,10…(36) |
| Florida4 | 27 | 191 | 10:003 | 003 008 009 011 | 2:003 008 | 23(6) | idx[20]:4,5,6,7…(36) |
| Indiana4 | 27 | 223 | 10:002 | 002 022 177 226 | 3:002 022 177 | 7(8) | idx[20]:2,3,5,6…(36) |
| Michigan4 | 27 | 172 | 9:112 | 112 119 155 199 | 3:112 155 199 | 6(6) | idx[20]:2,4,5,6…(36) |
| NorthCarolina4 | 27 | 193 | 9:001 | 001 009 044 225 | 3:001 009 044 | 12(8) | idx[20]:1,2,3,4…(36) |
| Virginia4 | 27 | 204 | 9:004 | 004 177 199 377 | 4:004 177 377 | 12(8) | idx[20]:2,3,5,6…(36) |
| SouthCarolina4 | 27 | 225 | 9:115 | 115 155 224 233 | 3:011 115 224 | 29(6) | idx[20]:2,3,5,6…(36) |
| Connecticut4 | 27 | 226 | 9:088 | 088 099 223 228 | 1:088 | 9(8) | idx[20]:1,2,4,5…(36) |
| NewYork4 | 27 | 238 | 9:001 | 001 007 011 066 | 2:001 066 | 6(6) | idx[20]:2,3,4,5…(36) |
| OntarioCanada4 | 27 | 238 | 9:004 | 004 044 144 244 | 2:004 244 | 18(6) | idx[20]:5,6,7,8…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

### B12 (`analysis_prefix`)
- **PuertoRico4**: `022 202 220 225 252 522 237 273 372 732 226 236`
- **Pennsylvania4**: `007 070 700 057 075 507 570 750 755 759 705 557`
- **Delaware4**: `090 009 900 040 004 400 595 411 559 955 119 088`
- **Ohio4**: `090 009 900 075 570 057 750 055 257 527 725 752`
- **NewJersey4**: `202 022 220 252 225 522 707 182 077 770 279 889`
- **Florida4**: `003 030 300 008 080 800 386 683 732 737 633 634`
- **Indiana4**: `020 002 200 066 626 022 177 202 220 717 771 386`
- **Michigan4**: `112 121 211 168 368 155 199 515 551 919 991 186`
- **NorthCarolina4**: `001 010 100 044 404 440 009 090 900 290 522 500`
- **Virginia4**: `004 040 400 177 717 771 377 737 773 455 545 554`
- **SouthCarolina4**: `115 151 511 238 224 242 422 011 101 110 283 328`
- **Connecticut4**: `088 808 880 228 048 084 749 794 744 784 645 847`
- **NewYork4**: `001 010 100 606 066 660 011 600 540 110 500 062`
- **OntarioCanada4**: `004 040 400 244 424 442 267 167 176 617 671 716`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-03/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,7,8,10…(36)` pack=`027 257 022 077 225 577 149 469 144 199 446 699 237 278 223 228 247 279 224 229 236 036 233 136 226 073 344 244 134 033 002 026 688 334 449 219` (src: `sharepacks/_predictive/2026-01-03/PuertoRico4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-03/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,5…(36)` pack=`025 057 002 007 255 557 045 059 004 009 455 559 024 029 047 079 247 279 224 229 599 138 757 717 277 015 578 593 055 038 378 338 228 339 036 899` (src: `sharepacks/_predictive/2026-01-03/Pennsylvania4/play_card__tool_only__stable10.json`)
- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-03/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:1,2,5,6…(36)` pack=`045 059 004 009 455 559 149 469 144 199 446 699 146 169 114 119 449 499 249 459 345 001 126 434 223 088 014 389 011 224 005 338 179 431 067 337` (src: `sharepacks/_predictive/2026-01-03/Delaware4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-03/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`025 057 002 007 255 557 045 059 004 009 455 559 027 257 022 077 024 029 047 079 058 055 056 267 068 224 244 114 066 113 277 088 599 388 987 116` (src: `sharepacks/_predictive/2026-01-03/Ohio4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-03/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,5,10…(36)` pack=`027 257 022 077 225 577 247 279 224 229 477 779 348 389 334 339 249 479 244 299 259 238 778 289 127 138 182 599 155 114 989 227 199 559 449 005` (src: `sharepacks/_predictive/2026-01-03/NewJersey4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=23(6)` pack=`138 368 133 188 336 688` (src: `sharepacks/_predictive/2026-01-03/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:4,5,6,7…(36)` pack=`138 368 133 188 336 688 035 058 003 008 355 558 237 278 223 228 136 168 113 118 086 224 667 466 677 338 009 467 634 567 011 033 077 599 244 733` (src: `sharepacks/_predictive/2026-01-03/Florida4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=7(8)` pack=`012 017 026 067 125 157 256 567` (src: `sharepacks/_predictive/2026-01-03/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`025 057 002 007 255 557 127 267 122 177 226 677 126 167 112 117 016 156 011 066 386 224 668 015 076 146 022 096 447 079 038 367 246 144 099 559` (src: `sharepacks/_predictive/2026-01-03/Indiana4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-03/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,4,5,6…(36)` pack=`016 156 011 066 115 566 138 368 133 188 336 688 146 169 114 119 038 358 033 088 168 112 155 199 096 189 889 166 338 355 599 244 559 449 124 227` (src: `sharepacks/_predictive/2026-01-03/Michigan4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-03/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`024 029 047 079 245 259 049 459 044 099 445 599 045 059 004 009 249 479 244 299 522 001 242 199 344 500 003 033 449 223 226 233 227 502 034 932` (src: `sharepacks/_predictive/2026-01-03/NorthCarolina4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-03/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`045 059 004 009 455 559 024 029 047 079 245 259 127 267 122 177 027 257 022 077 399 377 057 117 224 561 015 169 227 178 233 334 244 599 133 537` (src: `sharepacks/_predictive/2026-01-03/Virginia4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=29(6)` pack=`238 378 233 288 337 788` (src: `sharepacks/_predictive/2026-01-03/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`238 378 233 288 337 788 016 156 011 066 115 566 138 368 133 188 123 128 137 178 135 136 015 079 012 002 087 224 033 126 169 389 559 599 227 098` (src: `sharepacks/_predictive/2026-01-03/SouthCarolina4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-03/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,4,5…(36)` pack=`014 019 046 069 145 159 237 278 223 228 377 778 247 279 224 229 049 459 044 099 088 744 784 048 144 257 348 388 864 489 368 001 116 559 003 055` (src: `sharepacks/_predictive/2026-01-03/Connecticut4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-03/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`016 156 011 066 115 566 015 056 001 006 155 556 136 168 113 118 045 059 004 009 489 062 469 599 007 068 088 244 368 058 266 488 788 224 227 640` (src: `sharepacks/_predictive/2026-01-03/NewYork4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=18(6)` pack=`136 168 113 118 366 668` (src: `sharepacks/_predictive/2026-01-03/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:5,6,7,8…(36)` pack=`045 059 004 009 455 559 146 169 114 119 466 669 136 168 113 118 127 267 122 177 188 167 488 484 257 014 044 189 244 239 017 378 678 011 047 180` (src: `sharepacks/_predictive/2026-01-03/OntarioCanada4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **PuertoRico4**: `027 257 022 077 225 577 237 073 226 236 134 136 144 223 344 023 028 037 370 730 033 088 199 303`
- **Pennsylvania4**: `025 057 002 007 255 557 059 055 759 559 599 277 338 717 593 709 907 099 079 097 579 790 795 970`
- **Delaware4**: `045 059 004 009 455 559 494 499 411 119 088 414 434 249 934 545 554 491 194 941 126 149 459 495`
- **Ohio4**: `025 057 002 007 255 557 090 055 257 592 559 027 077 577 225 252 522 058 085 507 508 580 705 805`
- **NewJersey4**: `027 257 022 077 225 577 182 279 242 989 299 227 292 889 289 812 924 928 982 799 259 295 592 952`
- **Florida4**: `138 368 133 188 336 688 003 086 008 338 388 366 634 467 668 732 737 377 031 036 068 680 860 009`
- **Indiana4**: `012 017 026 067 125 157 256 567 020 386 138 066 626 022 177 668 224 242 422 188 318 381 477 688`
- **Michigan4**: `016 156 011 066 115 566 112 168 368 155 199 338 096 133 335 355 358 361 868 165 561 196 151 119`
- **NorthCarolina4**: `024 029 047 079 245 259 457 579 044 009 001 500 522 244 242 229 005 050 055 199 505 550 919 991`
- **Virginia4**: `024 029 047 079 245 259 457 579 004 227 455 177 377 559 399 577 277 272 722 561 567 547 597 042`
- **SouthCarolina4**: `238 378 233 288 337 788 115 224 011 135 137 087 128 015 136 138 012 017 062 125 152 251 521 155`
- **Connecticut4**: `014 019 046 069 145 159 456 569 088 048 228 116 388 744 784 338 383 833 749 794 068 086 864 041`
- **NewYork4**: `016 156 011 066 115 566 001 600 366 168 500 062 067 489 116 068 086 680 860 899 540 061 561 007`
- **OntarioCanada4**: `136 168 113 118 366 668 004 267 244 167 114 189 188 239 161 484 164 257 014 019 064 145 154 451`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`)

- **PuertoRico4**: `027 257 022 077 225 577 149 469 144 199 446 699 237 278 223 228 247 279 224 229 236 036 233 136 226 073 344 244 134 033 002 026 688 334 449 219`
- **Pennsylvania4**: `025 057 002 007 255 557 045 059 004 009 455 559 024 029 047 079 247 279 224 229 599 138 757 717 277 015 578 593 055 038 378 338 228 339 036 899`
- **Delaware4**: `045 059 004 009 455 559 149 469 144 199 446 699 146 169 114 119 449 499 249 459 345 001 126 434 223 088 014 389 011 224 005 338 179 431 067 337`
- **Ohio4**: `025 057 002 007 255 557 045 059 004 009 455 559 027 257 022 077 024 029 047 079 058 055 056 267 068 224 244 114 066 113 277 088 599 388 987 116`
- **NewJersey4**: `027 257 022 077 225 577 247 279 224 229 477 779 348 389 334 339 249 479 244 299 259 238 778 289 127 138 182 599 155 114 989 227 199 559 449 005`
- **Florida4**: `138 368 133 188 336 688 035 058 003 008 355 558 237 278 223 228 136 168 113 118 086 224 667 466 677 338 009 467 634 567 011 033 077 599 244 733`
- **Indiana4**: `025 057 002 007 255 557 127 267 122 177 226 677 126 167 112 117 016 156 011 066 386 224 668 015 076 146 022 096 447 079 038 367 246 144 099 559`
- **Michigan4**: `016 156 011 066 115 566 138 368 133 188 336 688 146 169 114 119 038 358 033 088 168 112 155 199 096 189 889 166 338 355 599 244 559 449 124 227`
- **NorthCarolina4**: `024 029 047 079 245 259 049 459 044 099 445 599 045 059 004 009 249 479 244 299 522 001 242 199 344 500 003 033 449 223 226 233 227 502 034 932`
- **Virginia4**: `045 059 004 009 455 559 024 029 047 079 245 259 127 267 122 177 027 257 022 077 399 377 057 117 224 561 015 169 227 178 233 334 244 599 133 537`
- **SouthCarolina4**: `238 378 233 288 337 788 016 156 011 066 115 566 138 368 133 188 123 128 137 178 135 136 015 079 012 002 087 224 033 126 169 389 559 599 227 098`
- **Connecticut4**: `014 019 046 069 145 159 237 278 223 228 377 778 247 279 224 229 049 459 044 099 088 744 784 048 144 257 348 388 864 489 368 001 116 559 003 055`
- **NewYork4**: `016 156 011 066 115 566 015 056 001 006 155 556 136 168 113 118 045 059 004 009 489 062 469 599 007 068 088 244 368 058 266 488 788 224 227 640`
- **OntarioCanada4**: `045 059 004 009 455 559 146 169 114 119 466 669 136 168 113 118 127 267 122 177 188 167 488 484 257 014 044 189 244 239 017 378 678 011 047 180`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-03/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-03/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-03/<STATE>/play_card__tool_only*.json` (budgeted cuts)
