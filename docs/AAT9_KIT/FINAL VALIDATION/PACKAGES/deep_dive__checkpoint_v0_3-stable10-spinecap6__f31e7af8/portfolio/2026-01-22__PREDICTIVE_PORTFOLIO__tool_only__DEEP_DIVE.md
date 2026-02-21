# Predictive Portfolio — D=2026-01-22

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-22/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| Virginia4 | 27 | 195 | 12:004 | 004 177 199 334 | 3:004 009 334 | 5(6) | idx[22]:1,2,3,4…(36) |
| Ohio4 | 27 | 207 | 11:009 | 009 066 113 118 | 4:004 009 559 | 5(6) | idx[20]:2,3,4,5…(36) |
| OntarioCanada4 | 27 | 185 | 10:004 | 004 044 144 228 | 4:004 044 144 | 15(6) | idx[20]:2,4,5,8…(36) |
| Connecticut4 | 27 | 190 | 10:088 | 088 099 116 223 | 2:033 088 | 6(6) | idx[22]:1,2,3,4…(36) |
| PuertoRico4 | 27 | 211 | 10:022 | 022 033 088 112 | 3:022 033 168 | 10(6) | idx[20]:2,3,4,5…(36) |
| Pennsylvania4 | 27 | 215 | 10:007 | 007 066 228 255 | 1:007 | 4(6) | idx[20]:3,4,5,6…(36) |
| Indiana4 | 27 | 216 | 10:002 | 002 022 177 226 | 3:002 007 177 | 20(6) | idx[20]:2,3,4,5…(36) |
| Delaware4 | 27 | 221 | 10:009 | 009 088 117 223 | 3:009 223 559 | 5(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | 27 | 193 | 9:066 | 066 112 119 155 | 2:066 119 | 22(8) | idx[20]:2,3,5,6…(36) |
| SouthCarolina4 | 27 | 198 | 9:114 | 114 115 155 233 | 2:114 155 | 2(6) | idx[20]:1,2,3,5…(36) |
| NewYork4 | 27 | 208 | 9:001 | 001 007 011 066 | 1:001 | 29(6) | idx[20]:2,3,5,6…(36) |
| NewJersey4 | 27 | 211 | 9:022 | 022 114 155 339 | 2:022 225 | 7(8) | idx[20]:1,2,3,4…(36) |
| NorthCarolina4 | 27 | 213 | 9:001 | 001 009 044 225 | 3:001 225 228 | 27(6) | idx[20]:2,5,6,8…(36) |
| Florida4 | 27 | 218 | 9:003 | 003 009 011 077 | 1:003 | 11(8) | idx[20]:1,3,4,5…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

### B12 (`analysis_prefix`)
- **Virginia4**: `040 004 400 090 334 343 433 009 900 105 702 705`
- **Ohio4**: `009 090 900 878 004 559 595 955 040 400 788 887`
- **OntarioCanada4**: `004 040 400 044 404 440 144 414 441 455 545 554`
- **Connecticut4**: `088 808 880 038 016 033 303 330 083 308 380 803`
- **PuertoRico4**: `022 202 220 186 681 033 303 330 168 618 816 861`
- **Pennsylvania4**: `007 070 700 183 085 580 003 030 058 850 146 059`
- **Indiana4**: `002 020 200 007 070 700 177 717 771 001 347 037`
- **Delaware4**: `009 090 900 559 595 955 259 223 232 322 255 592`
- **Michigan4**: `066 606 660 119 191 911 155 150 171 297 547 792`
- **SouthCarolina4**: `114 141 411 005 683 155 515 551 670 673 903 010`
- **NewYork4**: `001 010 100 328 377 183 283 832 177 138 238 318`
- **NewJersey4**: `022 202 220 017 001 071 170 077 225 252 522 707`
- **NorthCarolina4**: `001 010 100 228 282 822 225 252 522 322 287 782`
- **Florida4**: `003 030 300 035 087 638 025 052 138 078 780 870`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **Virginia4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-22/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:1,2,3,4…(36)` pack=`045 059 004 009 455 559 025 057 002 007 255 557 127 267 122 177 005 055 003 201 702 013 334 599 033 105 016 133 344 199 224 244 269 449 227 703` (src: `sharepacks/_predictive/2026-01-22/Virginia4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-22/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`045 059 004 009 455 559 023 028 037 078 235 258 238 378 233 288 027 257 022 077 084 088 778 688 244 007 113 178 127 008 224 499 066 599 889 556` (src: `sharepacks/_predictive/2026-01-22/Ohio4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=15(6)` pack=`049 459 044 099 445 599` (src: `sharepacks/_predictive/2026-01-22/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,4,5,8…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 149 469 144 199 349 489 344 399 249 024 348 688 238 088 068 346 001 246 449 228 224 003 840 826` (src: `sharepacks/_predictive/2026-01-22/OntarioCanada4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-22/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:1,2,3,4…(36)` pack=`038 358 033 088 335 588 016 156 011 066 115 566 237 278 223 228 116 166 027 699 800 068 233 688 001 099 005 007 338 244 559 224 114 227 842 802` (src: `sharepacks/_predictive/2026-01-22/Connecticut4/play_card__tool_only__stable10.json`)
- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-22/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`027 257 022 077 225 577 015 056 001 006 155 556 136 168 113 118 038 358 033 088 011 805 133 013 012 014 148 338 112 002 559 599 166 114 023 804` (src: `sharepacks/_predictive/2026-01-22/PuertoRico4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=4(6)` pack=`035 058 003 008 355 558` (src: `sharepacks/_predictive/2026-01-22/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,4,5,6…(36)` pack=`035 058 003 008 355 558 025 057 002 007 255 557 136 168 113 118 348 389 334 339 093 183 059 033 178 066 146 228 126 238 399 077 224 599 103 193` (src: `sharepacks/_predictive/2026-01-22/Pennsylvania4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=20(6)` pack=`127 267 122 177 226 677` (src: `sharepacks/_predictive/2026-01-22/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`025 057 002 007 255 557 027 257 022 077 225 577 127 267 122 177 023 028 037 078 004 224 011 017 244 347 137 001 471 377 599 334 344 003 133 380` (src: `sharepacks/_predictive/2026-01-22/Indiana4/play_card__tool_only__stable10.json`)
- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-22/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`045 059 004 009 455 559 025 057 002 007 255 557 024 029 047 079 146 169 114 119 615 149 117 244 001 599 003 223 034 336 224 346 055 338 399 611` (src: `sharepacks/_predictive/2026-01-22/Delaware4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=22(8)` pack=`124 129 147 179 246 269 467 679` (src: `sharepacks/_predictive/2026-01-22/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`016 156 011 066 115 566 126 167 112 117 266 667 124 129 147 179 247 279 224 229 119 155 244 559 007 449 547 077 599 334 227 366 778 788 157 188` (src: `sharepacks/_predictive/2026-01-22/Michigan4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-22/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,5…(36)` pack=`146 169 114 119 466 669 015 056 001 006 155 556 045 059 004 009 025 057 002 007 920 233 667 005 670 673 683 115 903 136 389 369 244 166 399 603` (src: `sharepacks/_predictive/2026-01-22/SouthCarolina4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=29(6)` pack=`238 378 233 288 337 788` (src: `sharepacks/_predictive/2026-01-22/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`238 378 233 288 337 788 015 056 001 006 155 556 237 278 223 228 127 267 122 177 183 113 038 153 011 234 007 577 338 599 244 357 559 117 339 679` (src: `sharepacks/_predictive/2026-01-22/NewYork4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=7(8)` pack=`012 017 026 067 125 157 256 567` (src: `sharepacks/_predictive/2026-01-22/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`015 056 001 006 155 556 027 257 022 077 225 577 045 059 004 009 012 017 026 067 244 599 339 007 033 133 394 019 035 149 233 137 224 177 005 304` (src: `sharepacks/_predictive/2026-01-22/NewJersey4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=27(6)` pack=`237 278 223 228 377 778` (src: `sharepacks/_predictive/2026-01-22/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,5,6,8…(36)` pack=`237 278 223 228 377 778 027 257 022 077 225 577 015 056 001 006 238 378 233 288 136 399 336 028 677 044 621 009 036 388 224 277 119 011 321 048` (src: `sharepacks/_predictive/2026-01-22/NorthCarolina4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=11(8)` pack=`023 028 037 078 235 258 357 578` (src: `sharepacks/_predictive/2026-01-22/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,3,4,5…(36)` pack=`035 058 003 008 355 558 025 057 002 007 255 557 023 028 037 078 138 368 133 188 137 378 278 038 257 068 009 224 259 689 388 011 055 599 046 117` (src: `sharepacks/_predictive/2026-01-22/Florida4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **Virginia4**: `045 059 004 009 455 559 334 055 016 201 206 002 005 133 105 702 705 540 950 177 199 717 771 919`
- **Ohio4**: `045 059 004 009 455 559 878 087 077 027 499 088 178 084 007 098 028 073 066 113 118 131 181 311`
- **OntarioCanada4**: `049 459 044 099 445 599 004 144 455 446 449 249 844 001 024 029 074 245 254 452 542 228 282 822`
- **Connecticut4**: `016 156 011 066 115 566 088 038 068 858 116 033 166 005 338 383 833 083 308 380 803 830 688 868`
- **PuertoRico4**: `027 257 022 077 225 577 186 033 013 338 001 136 011 805 012 017 062 088 112 121 211 808 880 668`
- **Pennsylvania4**: `035 058 003 008 355 558 007 183 224 059 093 598 178 133 146 530 066 228 255 282 525 552 606 660`
- **Indiana4**: `127 267 122 177 226 677 002 007 001 037 347 017 011 137 471 077 172 271 721 027 072 270 720 012`
- **Delaware4**: `045 059 004 009 455 559 259 255 223 055 034 336 338 614 615 146 029 020 025 075 520 570 088 117`
- **Michigan4**: `124 129 147 179 246 269 467 679 066 119 155 449 499 477 297 547 792 927 227 277 150 171 174 247`
- **SouthCarolina4**: `015 056 001 006 155 556 114 005 007 009 055 670 673 903 920 255 100 683 059 065 510 560 115 151`
- **NewYork4**: `238 378 233 288 337 788 001 377 183 177 113 038 327 827 153 513 013 018 063 007 011 066 070 101`
- **NewJersey4**: `012 017 026 067 125 157 256 567 022 001 077 225 177 007 590 009 394 501 504 062 114 141 155 339`
- **NorthCarolina4**: `237 278 223 228 377 778 001 028 225 006 399 136 828 677 277 388 838 883 621 186 681 320 023 073`
- **Florida4**: `023 028 037 078 235 258 357 578 003 035 388 378 138 188 278 638 025 052 368 038 257 032 009 011`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`)

- **Virginia4**: `045 059 004 009 455 559 025 057 002 007 255 557 127 267 122 177 005 055 003 201 702 013 334 599 033 105 016 133 344 199 224 244 269 449 227 703`
- **Ohio4**: `045 059 004 009 455 559 023 028 037 078 235 258 238 378 233 288 027 257 022 077 084 088 778 688 244 007 113 178 127 008 224 499 066 599 889 556`
- **OntarioCanada4**: `045 059 004 009 455 559 049 459 044 099 445 599 149 469 144 199 349 489 344 399 249 024 348 688 238 088 068 346 001 246 449 228 224 003 840 826`
- **Connecticut4**: `038 358 033 088 335 588 016 156 011 066 115 566 237 278 223 228 116 166 027 699 800 068 233 688 001 099 005 007 338 244 559 224 114 227 842 802`
- **PuertoRico4**: `027 257 022 077 225 577 015 056 001 006 155 556 136 168 113 118 038 358 033 088 011 805 133 013 012 014 148 338 112 002 559 599 166 114 023 804`
- **Pennsylvania4**: `035 058 003 008 355 558 025 057 002 007 255 557 136 168 113 118 348 389 334 339 093 183 059 033 178 066 146 228 126 238 399 077 224 599 103 193`
- **Indiana4**: `025 057 002 007 255 557 027 257 022 077 225 577 127 267 122 177 023 028 037 078 004 224 011 017 244 347 137 001 471 377 599 334 344 003 133 380`
- **Delaware4**: `045 059 004 009 455 559 025 057 002 007 255 557 024 029 047 079 146 169 114 119 615 149 117 244 001 599 003 223 034 336 224 346 055 338 399 611`
- **Michigan4**: `016 156 011 066 115 566 126 167 112 117 266 667 124 129 147 179 247 279 224 229 119 155 244 559 007 449 547 077 599 334 227 366 778 788 157 188`
- **SouthCarolina4**: `146 169 114 119 466 669 015 056 001 006 155 556 045 059 004 009 025 057 002 007 920 233 667 005 670 673 683 115 903 136 389 369 244 166 399 603`
- **NewYork4**: `238 378 233 288 337 788 015 056 001 006 155 556 237 278 223 228 127 267 122 177 183 113 038 153 011 234 007 577 338 599 244 357 559 117 339 679`
- **NewJersey4**: `015 056 001 006 155 556 027 257 022 077 225 577 045 059 004 009 012 017 026 067 244 599 339 007 033 133 394 019 035 149 233 137 224 177 005 304`
- **NorthCarolina4**: `237 278 223 228 377 778 027 257 022 077 225 577 015 056 001 006 238 378 233 288 136 399 336 028 677 044 621 009 036 388 224 277 119 011 321 048`
- **Florida4**: `035 058 003 008 355 558 025 057 002 007 255 557 023 028 037 078 138 368 133 188 137 378 278 038 257 068 009 224 259 689 388 011 055 599 046 117`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-22/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-22/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-22/<STATE>/play_card__tool_only*.json` (budgeted cuts)
