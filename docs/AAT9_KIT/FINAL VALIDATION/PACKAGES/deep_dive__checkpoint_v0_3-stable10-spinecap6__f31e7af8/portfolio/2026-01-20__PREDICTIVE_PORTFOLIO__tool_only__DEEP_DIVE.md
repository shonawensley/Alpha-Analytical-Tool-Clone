# Predictive Portfolio — D=2026-01-20

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-20/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| Delaware4 | 27 | 211 | 12:009 | 009 088 117 223 | 2:009 559 | 5(6) | idx[20]:1,2,3,4…(36) |
| OntarioCanada4 | 27 | 190 | 11:004 | 004 044 144 228 | 3:004 044 144 | 5(6) | idx[20]:5,6,8,11…(36) |
| Connecticut4 | 27 | 208 | 11:088 | 088 099 223 228 | 2:088 588 | 3(6) | idx[20]:1,2,3,4…(36) |
| Ohio4 | 27 | 214 | 11:009 | 009 066 113 118 | 4:004 009 099 | 5(6) | idx[22]:3,4,5,6…(36) |
| Virginia4 | 27 | 210 | 10:004 | 004 177 199 334 | 4:003 004 009 | 14(8) | idx[20]:2,3,4,5…(36) |
| PuertoRico4 | 27 | 246 | 10:022 | 022 033 088 112 | 2:022 033 | 10(6) | idx[20]:2,4,5,6…(36) |
| Michigan4 | 27 | 159 | 9:066 | 066 112 119 155 | 3:011 066 155 | 17(6) | idx[20]:2,3,5,6…(36) |
| Florida4 | 27 | 195 | 9:003 | 003 009 011 077 | 3:003 008 077 | 11(8) | idx[20]:3,4,5,6…(36) |
| SouthCarolina4 | 27 | 198 | 9:114 | 114 115 155 233 | 3:114 233 466 | 8(8) | idx[20]:1,2,3,5…(36) |
| NewJersey4 | 27 | 200 | 9:022 | 022 114 155 339 | 4:001 004 022 | 2(6) | idx[20]:2,3,5,6…(36) |
| NewYork4 | 27 | 202 | 9:001 | 001 007 011 066 | 2:001 378 | 27(6) | idx[20]:2,3,6,8…(36) |
| NorthCarolina4 | 27 | 222 | 9:001 | 001 009 044 225 | 3:001 225 228 | 27(6) | idx[22]:2,3,5,6…(36) |
| Pennsylvania4 | 27 | 233 | 9:007 | 007 066 228 255 | 3:007 168 338 | 32(2) | idx[24]:1,3,4,5…(36) |
| Indiana4 | 27 | 244 | 9:002 | 002 022 177 226 | 3:002 007 226 | 6(6) | idx[20]:2,3,4,5…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

### B12 (`analysis_prefix`)
- **Delaware4**: `090 009 900 595 034 559 955 040 055 037 940 004`
- **OntarioCanada4**: `004 040 400 044 144 836 404 440 414 441 368 386`
- **Connecticut4**: `088 808 880 238 588 822 858 885 850 283 328 382`
- **Ohio4**: `009 090 900 004 499 949 994 040 400 099 909 990`
- **Virginia4**: `004 040 400 334 343 433 009 090 900 003 030 300`
- **PuertoRico4**: `022 202 220 138 183 033 303 330 808 318 381 813`
- **Michigan4**: `066 606 660 155 121 515 551 011 101 110 255 525`
- **Florida4**: `003 030 300 725 787 077 707 770 008 080 800 257`
- **SouthCarolina4**: `114 141 411 233 323 332 167 466 646 664 005 683`
- **NewJersey4**: `022 202 220 001 077 707 770 010 100 004 040 400`
- **NewYork4**: `001 010 100 378 377 177 387 783 837 873 738 717`
- **NorthCarolina4**: `001 010 100 225 252 522 228 257 282 822 287 782`
- **Pennsylvania4**: `007 070 700 186 681 338 383 833 168 618 816 861`
- **Indiana4**: `002 020 200 610 007 070 700 017 177 226 262 622`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-20/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 034 039 048 089 038 358 033 088 015 334 133 244 259 037 030 149 349 055 255 567 224 117 011 223` (src: `sharepacks/_predictive/2026-01-20/Delaware4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-20/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:5,6,8,11…(36)` pack=`045 059 004 009 455 559 023 028 037 078 235 258 149 469 144 199 237 278 223 228 836 846 834 238 224 263 024 624 044 267 844 068 449 088 011 845` (src: `sharepacks/_predictive/2026-01-20/OntarioCanada4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-20/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`038 358 033 088 335 588 025 057 002 007 255 557 035 058 003 008 238 378 233 288 099 068 699 822 168 234 348 249 489 005 559 001 852 224 840 688` (src: `sharepacks/_predictive/2026-01-20/Connecticut4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-20/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:3,4,5,6…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 024 029 047 079 449 499 244 077 034 088 113 149 138 389 489 008 078 234 388 066 477 109 007 788` (src: `sharepacks/_predictive/2026-01-20/Ohio4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=14(8)` pack=`034 039 048 089 345 359 458 589` (src: `sharepacks/_predictive/2026-01-20/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`045 059 004 009 455 559 034 039 048 089 345 359 127 267 122 177 348 389 334 339 702 003 705 105 136 206 244 013 344 338 016 199 099 133 224 736` (src: `sharepacks/_predictive/2026-01-20/Virginia4/play_card__tool_only__stable10.json`)
- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-20/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,4,5,6…(36)` pack=`038 358 033 088 335 588 138 368 133 188 336 688 027 257 022 077 035 058 003 008 668 238 148 028 559 013 015 014 338 112 011 244 344 224 334 804` (src: `sharepacks/_predictive/2026-01-20/PuertoRico4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=17(6)` pack=`126 167 112 117 266 667` (src: `sharepacks/_predictive/2026-01-20/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`126 167 112 117 266 667 016 156 011 066 115 566 015 056 001 006 025 057 002 007 172 277 119 224 225 688 599 244 559 778 788 449 338 120 469 154` (src: `sharepacks/_predictive/2026-01-20/Michigan4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=11(8)` pack=`023 028 037 078 235 258 357 578` (src: `sharepacks/_predictive/2026-01-20/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,4,5,6…(36)` pack=`035 058 003 008 355 558 237 278 223 228 377 778 023 028 037 078 027 257 022 077 345 387 255 178 188 009 259 388 011 727 599 224 177 889 038 046` (src: `sharepacks/_predictive/2026-01-20/Florida4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=8(8)` pack=`013 018 036 068 135 158 356 568` (src: `sharepacks/_predictive/2026-01-20/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,5…(36)` pack=`146 169 114 119 466 669 013 018 036 068 135 158 126 167 112 117 238 378 233 288 683 339 005 002 155 670 115 009 467 136 599 033 244 166 677 970` (src: `sharepacks/_predictive/2026-01-20/SouthCarolina4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-20/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`015 056 001 006 155 556 014 019 046 069 145 159 045 059 004 009 027 257 022 077 794 599 339 057 012 149 378 224 038 138 114 101 338 704 166 667` (src: `sharepacks/_predictive/2026-01-20/NewJersey4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=27(6)` pack=`237 278 223 228 377 778` (src: `sharepacks/_predictive/2026-01-20/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,6,8…(36)` pack=`237 278 223 228 377 778 238 378 233 288 337 788 127 267 122 177 123 128 137 178 001 133 113 334 239 013 077 011 007 353 357 224 117 388 019 449` (src: `sharepacks/_predictive/2026-01-20/NewYork4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=27(6)` pack=`237 278 223 228 377 778` (src: `sharepacks/_predictive/2026-01-20/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:2,3,5,6…(36)` pack=`237 278 223 228 377 778 027 257 022 077 225 577 015 056 001 006 227 277 168 344 009 011 368 388 020 127 126 026 068 024 038 234 244 169 044 258` (src: `sharepacks/_predictive/2026-01-20/NorthCarolina4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=32(2)` pack=`338 388` (src: `sharepacks/_predictive/2026-01-20/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[24]:1,3,4,5…(36)` pack=`238 378 233 288 337 788 338 388 025 057 002 007 138 368 133 188 186 334 003 034 028 088 244 178 146 599 004 259 344 066 005 103 228 225 117 224` (src: `sharepacks/_predictive/2026-01-20/Pennsylvania4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-20/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`025 057 002 007 255 557 016 156 011 066 115 566 027 257 022 077 012 017 026 067 177 617 124 001 559 119 778 019 688 703 137 139 038 166 003 334` (src: `sharepacks/_predictive/2026-01-20/Indiana4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **Delaware4**: `045 059 004 009 455 559 034 055 037 940 030 259 015 556 594 088 117 171 223 232 322 711 808 880`
- **OntarioCanada4**: `045 059 004 009 455 559 044 144 836 244 449 844 846 023 263 362 624 001 246 264 462 642 834 278`
- **Connecticut4**: `025 057 002 007 255 557 088 238 850 588 822 005 068 568 699 249 852 020 075 520 570 099 223 228`
- **Ohio4**: `045 059 004 009 455 559 499 097 077 449 008 099 388 149 094 940 042 047 079 790 970 066 113 118`
- **Virginia4**: `034 039 048 089 345 359 458 589 004 009 334 003 013 136 206 339 539 105 702 705 084 093 390 930`
- **PuertoRico4**: `027 257 022 077 225 577 138 028 808 033 344 338 668 238 803 805 800 038 083 380 830 023 073 082`
- **Michigan4**: `126 167 112 117 266 667 155 066 277 011 227 255 599 150 250 015 162 261 172 271 761 119 191 911`
- **Florida4**: `023 028 037 078 235 258 357 578 003 387 725 787 077 727 388 008 080 800 738 837 257 275 527 572`
- **SouthCarolina4**: `013 018 036 068 135 158 356 568 114 005 167 233 466 009 055 670 467 360 630 683 617 671 115 151`
- **NewJersey4**: `015 056 001 006 155 556 022 014 077 101 559 004 019 009 338 378 794 012 017 062 114 141 339 393`
- **NewYork4**: `237 278 223 228 377 778 378 177 001 137 373 113 668 077 323 353 173 371 731 327 732 832 013 018`
- **NorthCarolina4**: `237 278 223 228 377 778 225 001 227 257 258 006 388 168 277 338 383 833 527 725 752 020 025 075`
- **Pennsylvania4**: `338 388 007 186 028 138 000 003 133 823 136 146 023 073 082 280 820 066 228 255 282 525 552 606`
- **Indiana4**: `016 156 011 066 115 566 017 002 166 007 177 226 077 038 703 001 606 660 127 172 271 721 101 110`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`)

- **Delaware4**: `045 059 004 009 455 559 049 459 044 099 445 599 034 039 048 089 038 358 033 088 015 334 133 244 259 037 030 149 349 055 255 567 224 117 011 223`
- **OntarioCanada4**: `045 059 004 009 455 559 023 028 037 078 235 258 149 469 144 199 237 278 223 228 836 846 834 238 224 263 024 624 044 267 844 068 449 088 011 845`
- **Connecticut4**: `038 358 033 088 335 588 025 057 002 007 255 557 035 058 003 008 238 378 233 288 099 068 699 822 168 234 348 249 489 005 559 001 852 224 840 688`
- **Ohio4**: `045 059 004 009 455 559 049 459 044 099 445 599 024 029 047 079 449 499 244 077 034 088 113 149 138 389 489 008 078 234 388 066 477 109 007 788`
- **Virginia4**: `045 059 004 009 455 559 034 039 048 089 345 359 127 267 122 177 348 389 334 339 702 003 705 105 136 206 244 013 344 338 016 199 099 133 224 736`
- **PuertoRico4**: `038 358 033 088 335 588 138 368 133 188 336 688 027 257 022 077 035 058 003 008 668 238 148 028 559 013 015 014 338 112 011 244 344 224 334 804`
- **Michigan4**: `126 167 112 117 266 667 016 156 011 066 115 566 015 056 001 006 025 057 002 007 172 277 119 224 225 688 599 244 559 778 788 449 338 120 469 154`
- **Florida4**: `035 058 003 008 355 558 237 278 223 228 377 778 023 028 037 078 027 257 022 077 345 387 255 178 188 009 259 388 011 727 599 224 177 889 038 046`
- **SouthCarolina4**: `146 169 114 119 466 669 013 018 036 068 135 158 126 167 112 117 238 378 233 288 683 339 005 002 155 670 115 009 467 136 599 033 244 166 677 970`
- **NewJersey4**: `015 056 001 006 155 556 014 019 046 069 145 159 045 059 004 009 027 257 022 077 794 599 339 057 012 149 378 224 038 138 114 101 338 704 166 667`
- **NewYork4**: `237 278 223 228 377 778 238 378 233 288 337 788 127 267 122 177 123 128 137 178 001 133 113 334 239 013 077 011 007 353 357 224 117 388 019 449`
- **NorthCarolina4**: `237 278 223 228 377 778 027 257 022 077 225 577 015 056 001 006 227 277 168 344 009 011 368 388 020 127 126 026 068 024 038 234 244 169 044 258`
- **Pennsylvania4**: `238 378 233 288 337 788 338 388 025 057 002 007 138 368 133 188 186 334 003 034 028 088 244 178 146 599 004 259 344 066 005 103 228 225 117 224`
- **Indiana4**: `025 057 002 007 255 557 016 156 011 066 115 566 027 257 022 077 012 017 026 067 177 617 124 001 559 119 778 019 688 703 137 139 038 166 003 334`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-20/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-20/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-20/<STATE>/play_card__tool_only*.json` (budgeted cuts)
