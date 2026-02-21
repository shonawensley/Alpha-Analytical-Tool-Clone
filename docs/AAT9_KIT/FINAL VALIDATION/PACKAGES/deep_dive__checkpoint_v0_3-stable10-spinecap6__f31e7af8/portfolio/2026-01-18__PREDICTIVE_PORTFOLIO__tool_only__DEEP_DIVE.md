# Predictive Portfolio — D=2026-01-18

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-18/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| Ohio4 | 27 | 192 | 13:009 | 009 066 113 118 | 3:004 009 499 | 5(6) | idx[22]:2,3,4,5…(36) |
| Connecticut4 | 27 | 213 | 13:088 | 088 099 223 228 | 2:088 588 | 13(6) | idx[20]:3,4,5,8…(36) |
| Delaware4 | 27 | 214 | 12:009 | 009 088 117 223 | 3:004 009 559 | 5(6) | idx[20]:1,2,3,4…(36) |
| OntarioCanada4 | 27 | 187 | 11:004 | 004 044 144 228 | 3:004 044 144 | 5(6) | idx[20]:2,5,9,10…(36) |
| Virginia4 | 27 | 187 | 11:004 | 004 177 199 334 | 4:004 099 455 | 5(6) | idx[22]:1,2,3,5…(36) |
| Pennsylvania4 | 27 | 228 | 10:007 | 007 066 228 255 | 1:007 | 12(8) | idx[20]:3,4,5,6…(36) |
| PuertoRico4 | 27 | 245 | 10:022 | 022 033 088 112 | 2:022 033 | 10(6) | idx[20]:2,3,4,5…(36) |
| Michigan4 | 27 | 173 | 9:066 | 066 112 119 155 | 4:011 066 155 | 7(8) | idx[20]:2,3,4,5…(36) |
| SouthCarolina4 | 27 | 186 | 9:114 | 114 115 155 233 | 2:114 466 | 19(6) | idx[20]:1,2,3,5…(36) |
| Florida4 | 27 | 188 | 9:003 | 003 009 011 077 | 2:003 355 | 11(8) | idx[20]:1,3,4,5…(36) |
| NewJersey4 | 27 | 204 | 9:022 | 022 114 155 339 | 3:022 339 348 | 12(8) | idx[20]:2,3,4,5…(36) |
| NewYork4 | 27 | 205 | 9:001 | 001 007 011 066 | 2:001 007 | 27(6) | idx[20]:2,3,5,6…(36) |
| NorthCarolina4 | 27 | 209 | 9:001 | 001 009 044 225 | 3:001 225 277 | 26(2) | idx[23]:1,2,3,4…(35) |
| Indiana4 | 27 | 248 | 9:002 | 002 022 177 226 | 3:002 007 226 | 6(6) | idx[20]:1,2,3,4…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

### B12 (`analysis_prefix`)
- **Ohio4**: `009 090 900 004 499 949 994 040 400 094 940 941`
- **Connecticut4**: `088 808 880 858 588 885 828 898 868 238 283 832`
- **Delaware4**: `090 009 900 595 559 955 040 045 540 590 004 400`
- **OntarioCanada4**: `004 040 400 044 144 414 441 404 440 014 813 816`
- **Virginia4**: `040 004 400 455 545 554 599 959 995 099 909 990`
- **Pennsylvania4**: `007 070 700 163 141 894 934 943 948 984 024 349`
- **PuertoRico4**: `022 202 220 033 303 330 808 168 186 618 681 816`
- **Michigan4**: `066 606 660 155 110 515 551 011 101 255 525 552`
- **SouthCarolina4**: `114 141 411 466 646 664 670 677 667 663 167 067`
- **Florida4**: `003 030 300 355 755 752 535 553 258 057 075 507`
- **NewJersey4**: `022 202 220 339 393 933 348 384 438 483 834 843`
- **NewYork4**: `001 010 100 377 177 237 732 007 070 700 273 327`
- **NorthCarolina4**: `001 010 100 727 277 772 225 252 522 237 077 477`
- **Indiana4**: `002 020 200 660 007 070 700 005 177 226 262 622`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **Ohio4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-18/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:2,3,4,5…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 249 479 244 299 449 499 077 097 334 941 113 224 138 358 489 003 039 066 007 006 108 126 677 109` (src: `sharepacks/_predictive/2026-01-18/Ohio4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=13(6)` pack=`038 358 033 088 335 588` (src: `sharepacks/_predictive/2026-01-18/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,4,5,8…(36)` pack=`038 358 033 088 335 588 238 378 233 288 337 788 049 459 044 099 034 039 048 089 898 699 899 244 868 023 223 689 245 008 068 842 559 224 687 255` (src: `sharepacks/_predictive/2026-01-18/Connecticut4/play_card__tool_only__stable10.json`)
- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-18/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`045 059 004 009 455 559 024 029 047 079 245 259 025 057 002 007 027 257 022 077 744 006 224 034 223 117 599 035 088 177 336 446 344 449 734 005` (src: `sharepacks/_predictive/2026-01-18/Delaware4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-18/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,5,9,10…(36)` pack=`045 059 004 009 455 559 023 028 037 078 235 258 049 459 044 099 138 368 133 188 233 816 348 263 364 014 144 228 126 146 033 449 244 001 344 225` (src: `sharepacks/_predictive/2026-01-18/OntarioCanada4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-18/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:1,2,3,5…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 449 499 127 267 122 177 749 199 225 224 113 339 029 002 016 033 338 001 119 336 005 458 399 116` (src: `sharepacks/_predictive/2026-01-18/Virginia4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-18/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:3,4,5,6…(36)` pack=`025 057 002 007 255 557 024 029 047 079 245 259 349 489 344 399 138 368 133 188 163 141 689 244 334 034 149 066 234 117 004 599 068 014 003 027` (src: `sharepacks/_predictive/2026-01-18/Pennsylvania4/play_card__tool_only__stable10.json`)
- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-18/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`027 257 022 077 225 577 045 059 004 009 455 559 023 028 037 078 038 358 033 088 168 011 018 418 805 233 001 404 014 336 338 244 112 224 144 002` (src: `sharepacks/_predictive/2026-01-18/PuertoRico4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=7(8)` pack=`012 017 026 067 125 157 256 567` (src: `sharepacks/_predictive/2026-01-18/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`016 156 011 066 115 566 015 056 001 006 155 556 012 017 026 067 126 167 112 117 255 225 113 850 119 592 224 244 177 227 599 559 778 344 158 449` (src: `sharepacks/_predictive/2026-01-18/Michigan4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=19(6)` pack=`146 169 114 119 466 669` (src: `sharepacks/_predictive/2026-01-18/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,5…(36)` pack=`146 169 114 119 466 669 126 167 112 117 266 667 016 156 011 066 127 267 122 177 233 663 064 670 339 368 155 099 007 009 344 244 499 005 077 166` (src: `sharepacks/_predictive/2026-01-18/SouthCarolina4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=11(8)` pack=`023 028 037 078 235 258 357 578` (src: `sharepacks/_predictive/2026-01-18/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,3,4,5…(36)` pack=`023 028 037 078 235 258 035 058 003 008 355 558 027 257 022 077 025 057 002 007 728 738 187 009 368 349 388 011 055 599 224 244 889 227 358 046` (src: `sharepacks/_predictive/2026-01-18/Florida4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-18/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`024 029 047 079 245 259 348 389 334 339 488 889 038 358 033 088 238 378 233 288 022 559 019 155 002 008 344 114 224 449 599 244 708 101 701 018` (src: `sharepacks/_predictive/2026-01-18/NewJersey4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=27(6)` pack=`237 278 223 228 377 778` (src: `sharepacks/_predictive/2026-01-18/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`237 278 223 228 377 778 127 267 122 177 226 677 013 018 036 068 015 056 001 006 366 011 373 167 249 386 007 225 224 079 338 227 559 599 339 367` (src: `sharepacks/_predictive/2026-01-18/NewYork4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=26(2)` pack=`227 277` (src: `sharepacks/_predictive/2026-01-18/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[23]:1,2,3,4…(35)` pack=`027 257 022 077 225 577 227 277 237 278 223 228 247 279 224 229 001 024 344 126 721 387 334 044 009 156 244 003 258 255 144 005 338 751 169` (src: `sharepacks/_predictive/2026-01-18/NorthCarolina4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-18/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`016 156 011 066 115 566 025 057 002 007 255 557 014 019 046 069 127 267 122 177 663 119 608 368 559 056 117 022 035 139 005 166 078 359 088 647` (src: `sharepacks/_predictive/2026-01-18/Indiana4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **Ohio4**: `045 059 004 009 455 559 499 094 097 007 077 449 006 941 794 042 047 079 790 970 066 113 118 131`
- **Connecticut4**: `038 358 033 088 335 588 868 089 699 828 898 238 459 023 028 078 099 223 228 232 282 322 822 909`
- **Delaware4**: `045 059 004 009 455 559 577 740 744 597 007 259 006 750 035 088 117 171 223 232 322 711 808 880`
- **OntarioCanada4**: `045 059 004 009 455 559 044 014 244 144 449 263 364 001 813 816 820 023 028 073 228 282 822 090`
- **Virginia4**: `045 059 004 009 455 559 499 449 599 016 099 002 339 459 749 267 049 094 490 940 540 950 177 199`
- **Pennsylvania4**: `024 029 047 079 245 259 457 579 007 388 034 004 344 133 055 688 868 886 163 141 894 934 943 948`
- **PuertoRico4**: `027 257 022 077 225 577 808 244 033 338 168 404 014 018 418 841 336 405 805 400 078 023 028 073`
- **Michigan4**: `012 017 026 067 125 157 256 567 155 110 066 117 255 100 592 599 170 227 277 150 850 105 501 015`
- **SouthCarolina4**: `146 169 114 119 466 669 677 670 667 064 499 005 663 088 099 167 014 019 046 460 640 115 151 155`
- **Florida4**: `023 028 037 078 235 258 357 578 355 003 755 752 388 738 255 057 075 507 570 705 750 557 575 757`
- **NewJersey4**: `024 029 047 079 245 259 457 579 022 339 449 019 348 101 738 038 083 803 378 708 074 092 290 920`
- **NewYork4**: `237 278 223 228 377 778 001 177 007 227 277 366 668 373 136 163 316 361 386 613 631 683 783 249`
- **NorthCarolina4**: `227 277 001 237 024 074 244 225 077 477 387 247 344 434 443 721 725 728 287 782 278 029 047 470`
- **Indiana4**: `016 156 011 066 115 566 002 005 166 007 177 226 019 159 677 767 776 901 910 915 951 608 663 068`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`)

- **Ohio4**: `045 059 004 009 455 559 049 459 044 099 445 599 249 479 244 299 449 499 077 097 334 941 113 224 138 358 489 003 039 066 007 006 108 126 677 109`
- **Connecticut4**: `038 358 033 088 335 588 238 378 233 288 337 788 049 459 044 099 034 039 048 089 898 699 899 244 868 023 223 689 245 008 068 842 559 224 687 255`
- **Delaware4**: `045 059 004 009 455 559 024 029 047 079 245 259 025 057 002 007 027 257 022 077 744 006 224 034 223 117 599 035 088 177 336 446 344 449 734 005`
- **OntarioCanada4**: `045 059 004 009 455 559 023 028 037 078 235 258 049 459 044 099 138 368 133 188 233 816 348 263 364 014 144 228 126 146 033 449 244 001 344 225`
- **Virginia4**: `045 059 004 009 455 559 049 459 044 099 445 599 449 499 127 267 122 177 749 199 225 224 113 339 029 002 016 033 338 001 119 336 005 458 399 116`
- **Pennsylvania4**: `025 057 002 007 255 557 024 029 047 079 245 259 349 489 344 399 138 368 133 188 163 141 689 244 334 034 149 066 234 117 004 599 068 014 003 027`
- **PuertoRico4**: `027 257 022 077 225 577 045 059 004 009 455 559 023 028 037 078 038 358 033 088 168 011 018 418 805 233 001 404 014 336 338 244 112 224 144 002`
- **Michigan4**: `016 156 011 066 115 566 015 056 001 006 155 556 012 017 026 067 126 167 112 117 255 225 113 850 119 592 224 244 177 227 599 559 778 344 158 449`
- **SouthCarolina4**: `146 169 114 119 466 669 126 167 112 117 266 667 016 156 011 066 127 267 122 177 233 663 064 670 339 368 155 099 007 009 344 244 499 005 077 166`
- **Florida4**: `023 028 037 078 235 258 035 058 003 008 355 558 027 257 022 077 025 057 002 007 728 738 187 009 368 349 388 011 055 599 224 244 889 227 358 046`
- **NewJersey4**: `024 029 047 079 245 259 348 389 334 339 488 889 038 358 033 088 238 378 233 288 022 559 019 155 002 008 344 114 224 449 599 244 708 101 701 018`
- **NewYork4**: `237 278 223 228 377 778 127 267 122 177 226 677 013 018 036 068 015 056 001 006 366 011 373 167 249 386 007 225 224 079 338 227 559 599 339 367`
- **NorthCarolina4**: `027 257 022 077 225 577 227 277 237 278 223 228 247 279 224 229 001 024 344 126 721 387 334 044 009 156 244 003 258 255 144 005 338 751 169 727`
- **Indiana4**: `016 156 011 066 115 566 025 057 002 007 255 557 014 019 046 069 127 267 122 177 663 119 608 368 559 056 117 022 035 139 005 166 078 359 088 647`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-18/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-18/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-18/<STATE>/play_card__tool_only*.json` (budgeted cuts)
