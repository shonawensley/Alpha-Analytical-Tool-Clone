# Predictive Portfolio — D=2026-01-05

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-05/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| PuertoRico4 | 27 | 227 | 13:022 | 022 033 088 199 | 4:022 033 088 | 10(6) | idx[16]:7,8,10,11…(36) |
| Pennsylvania4 | 27 | 193 | 12:007 | 007 066 228 255 | 2:007 557 | 3(6) | idx[16]:1,2,3,5…(36) |
| Ohio4 | 27 | 170 | 11:009 | 009 066 113 118 | 1:009 | 3(6) | idx[16]:1,3,4,5…(36) |
| NewYork4 | 27 | 175 | 11:001 | 001 007 011 066 | 1:001 | 6(6) | idx[16]:1,2,3,4…(36) |
| Delaware4 | 27 | 188 | 11:009 | 009 088 223 228 | 4:004 009 088 | 5(6) | idx[16]:1,4,5,6…(36) |
| Michigan4 | 27 | 150 | 9:112 | 112 119 155 199 | 2:112 119 | 18(6) | idx[16]:2,3,5,6…(36) |
| Florida4 | 27 | 171 | 9:003 | 003 008 009 011 | 3:003 008 344 | 34(6) | idx[16]:4,5,6,9…(36) |
| NewJersey4 | 27 | 193 | 9:022 | 022 114 155 339 | 4:022 077 088 | 11(8) | idx[16]:2,10,11,12…(36) |
| NorthCarolina4 | 27 | 196 | 9:001 | 001 009 044 225 | 3:001 044 225 | 31(6) | idx[16]:1,2,4,5…(36) |
| Indiana4 | 27 | 223 | 9:002 | 002 022 177 226 | 2:002 177 | 18(6) | idx[16]:3,5,6,7…(36) |
| OntarioCanada4 | 27 | 224 | 9:004 | 004 044 144 244 | 3:004 244 249 | 9(8) | idx[16]:1,5,7,9…(36) |
| SouthCarolina4 | 27 | 224 | 9:115 | 115 155 224 233 | 2:115 224 | 20(6) | idx[16]:2,4,5,6…(36) |
| Connecticut4 | 27 | 225 | 9:088 | 088 099 223 228 | 2:088 778 | 12(8) | idx[16]:9,10,12,13…(36) |
| Virginia4 | 27 | 225 | 9:004 | 004 177 199 377 | 4:004 377 455 | 14(8) | idx[16]:1,2,4,5…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`

### B12 (`analysis_prefix`)
- **PuertoRico4**: `022 202 220 225 252 522 033 088 303 330 808 880`
- **Pennsylvania4**: `007 070 700 059 095 590 557 057 575 755 015 075`
- **Ohio4**: `090 009 900 059 058 850 050 508 805 020 559 595`
- **NewYork4**: `001 010 100 066 011 110 660 800 250 520 007 070`
- **Delaware4**: `090 009 900 040 595 004 400 559 955 088 808 880`
- **Michigan4**: `112 121 211 168 119 191 911 186 681 160 165 161`
- **Florida4**: `003 030 300 434 008 080 800 344 443 084 033 454`
- **NewJersey4**: `022 202 220 889 077 707 770 088 808 880 898 988`
- **NorthCarolina4**: `001 010 100 044 404 440 522 244 225 252 294 542`
- **Indiana4**: `002 020 200 686 066 626 668 177 717 771 386 683`
- **OntarioCanada4**: `004 040 400 244 424 442 249 294 429 492 924 942`
- **SouthCarolina4**: `115 151 511 267 762 224 242 422 295 276 627 672`
- **Connecticut4**: `088 808 880 727 778 787 877 724 747 707 744 024`
- **Virginia4**: `004 040 400 377 737 773 455 545 554 559 595 955`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-05/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:7,8,10,11…(36)` pack=`027 257 022 077 225 577 237 278 223 228 377 778 023 028 037 078 235 258 012 017 026 067 125 157 226 113 268 199 033 336 134 599 216 224 244 036` (src: `sharepacks/_predictive/2026-01-05/PuertoRico4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-05/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,3,5…(36)` pack=`025 057 002 007 255 557 045 059 004 009 455 559 016 156 011 066 115 566 015 056 001 006 155 556 099 169 005 579 359 019 717 244 228 227 338 399` (src: `sharepacks/_predictive/2026-01-05/Pennsylvania4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-05/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,3,4,5…(36)` pack=`045 059 004 009 455 559 025 057 002 007 255 557 035 058 003 008 355 558 038 358 033 088 335 588 592 050 599 066 225 113 116 224 068 449 688 199` (src: `sharepacks/_predictive/2026-01-05/Ohio4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-05/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,3,4…(36)` pack=`015 056 001 006 155 556 016 156 011 066 115 566 025 057 002 007 255 557 035 058 003 008 355 558 668 038 500 067 233 667 801 449 224 004 488 227` (src: `sharepacks/_predictive/2026-01-05/NewYork4/play_card__tool_only__stable10.json`)
- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-05/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,4,5,6…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 016 156 011 066 115 566 146 169 114 119 466 669 811 144 359 449 088 334 058 224 338 055 984 223` (src: `sharepacks/_predictive/2026-01-05/Delaware4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=18(6)` pack=`136 168 113 118 366 668` (src: `sharepacks/_predictive/2026-01-05/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,3,5,6…(36)` pack=`136 168 113 118 366 668 146 169 114 119 466 669 016 156 011 066 115 566 126 167 112 117 266 667 161 138 155 199 244 148 449 338 599 227 007 559` (src: `sharepacks/_predictive/2026-01-05/Michigan4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=34(6)` pack=`349 489 344 399 448 899` (src: `sharepacks/_predictive/2026-01-05/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:4,5,6,9…(36)` pack=`349 489 344 399 448 899 049 459 044 099 445 599 034 039 048 089 345 359 038 358 033 088 335 588 348 009 003 388 014 734 336 011 244 346 227 224` (src: `sharepacks/_predictive/2026-01-05/Florida4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=11(8)` pack=`023 028 037 078 235 258 357 578` (src: `sharepacks/_predictive/2026-01-05/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,10,11,12…(36)` pack=`027 257 022 077 225 577 348 389 334 339 488 889 247 279 224 229 477 779 023 028 037 078 235 258 982 778 989 299 188 882 079 088 127 189 227 155` (src: `sharepacks/_predictive/2026-01-05/NewJersey4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=31(6)` pack=`249 479 244 299 447 799` (src: `sharepacks/_predictive/2026-01-05/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,4,5…(36)` pack=`249 479 244 299 447 799 049 459 044 099 445 599 024 029 047 079 245 259 027 257 022 077 225 577 242 144 009 001 019 500 003 227 226 344 192 449` (src: `sharepacks/_predictive/2026-01-05/NorthCarolina4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=18(6)` pack=`136 168 113 118 366 668` (src: `sharepacks/_predictive/2026-01-05/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:3,5,6,7…(36)` pack=`136 168 113 118 366 668 126 167 112 117 266 667 016 156 011 066 115 566 012 017 026 067 125 157 386 177 002 244 224 059 069 246 146 116 022 038` (src: `sharepacks/_predictive/2026-01-05/Indiana4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-05/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,5,7,9…(36)` pack=`014 019 046 069 145 159 045 059 004 009 455 559 247 279 224 229 477 779 146 169 114 119 466 669 244 194 171 174 044 267 017 047 161 005 118 077` (src: `sharepacks/_predictive/2026-01-05/OntarioCanada4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=20(6)` pack=`127 267 122 177 226 677` (src: `sharepacks/_predictive/2026-01-05/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,4,5,6…(36)` pack=`247 279 224 229 477 779 024 029 047 079 245 259 238 378 233 288 337 788 015 056 001 006 155 556 115 267 599 244 275 120 595 003 227 696 296 019` (src: `sharepacks/_predictive/2026-01-05/SouthCarolina4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-05/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:9,10,12,13…(36)` pack=`024 029 047 079 245 259 038 358 033 088 335 588 247 279 224 229 477 779 237 278 223 228 377 778 048 386 727 744 099 248 707 388 644 684 456 668` (src: `sharepacks/_predictive/2026-01-05/Connecticut4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=14(8)` pack=`034 039 048 089 345 359 458 589` (src: `sharepacks/_predictive/2026-01-05/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,4,5…(36)` pack=`045 059 004 009 455 559 034 039 048 089 345 359 237 278 223 228 377 778 049 459 044 099 445 599 224 177 008 349 001 055 891 248 561 136 597 334` (src: `sharepacks/_predictive/2026-01-05/Virginia4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **PuertoRico4**: `027 257 022 077 225 577 206 232 237 073 033 088 226 268 278 286 287 327 723 728 782 827 872 223`
- **Pennsylvania4**: `025 057 002 007 255 557 059 015 005 055 156 717 099 359 579 597 795 975 056 052 066 228 282 525`
- **Ohio4**: `025 057 002 007 255 557 090 059 058 050 592 559 080 088 225 252 522 085 580 005 500 055 259 295`
- **NewYork4**: `016 156 011 066 115 566 001 800 250 067 006 007 668 038 500 005 168 186 681 861 118 181 811 025`
- **Delaware4**: `045 059 004 009 455 559 594 088 449 499 224 338 055 388 011 101 110 811 058 085 508 805 114 118`
- **Michigan4**: `136 168 113 118 366 668 119 112 160 165 161 117 661 138 386 831 613 631 163 155 199 515 551 919`
- **Florida4**: `349 489 344 399 448 899 084 003 034 008 388 033 454 594 038 083 348 380 384 483 830 843 734 039`
- **NewJersey4**: `023 028 037 078 235 258 357 578 022 889 982 077 989 088 229 299 778 087 289 298 780 870 892 882`
- **NorthCarolina4**: `249 479 244 299 447 799 029 044 522 001 542 242 144 446 699 969 996 202 245 254 452 524 500 941`
- **Indiana4**: `136 168 113 118 366 668 386 002 066 626 026 076 177 244 224 242 422 688 868 886 188 247 274 427`
- **OntarioCanada4**: `014 019 046 069 145 159 456 569 004 244 774 017 249 114 267 047 074 140 410 470 740 161 164 194`
- **SouthCarolina4**: `127 267 122 177 226 677 115 295 224 599 595 696 795 238 003 015 259 592 952 227 277 275 297 120`
- **Connecticut4**: `024 029 047 079 245 259 457 579 088 727 707 388 778 744 386 684 836 277 368 668 772 042 048 084`
- **Virginia4**: `034 039 048 089 345 359 458 589 377 004 455 559 599 891 055 349 394 493 943 561 597 543 084 093`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`)

- **PuertoRico4**: `027 257 022 077 225 577 237 278 223 228 377 778 023 028 037 078 235 258 012 017 026 067 125 157 226 113 268 199 033 336 134 599 216 224 244 036`
- **Pennsylvania4**: `025 057 002 007 255 557 045 059 004 009 455 559 016 156 011 066 115 566 015 056 001 006 155 556 099 169 005 579 359 019 717 244 228 227 338 399`
- **Ohio4**: `045 059 004 009 455 559 025 057 002 007 255 557 035 058 003 008 355 558 038 358 033 088 335 588 592 050 599 066 225 113 116 224 068 449 688 199`
- **NewYork4**: `015 056 001 006 155 556 016 156 011 066 115 566 025 057 002 007 255 557 035 058 003 008 355 558 668 038 500 067 233 667 801 449 224 004 488 227`
- **Delaware4**: `045 059 004 009 455 559 049 459 044 099 445 599 016 156 011 066 115 566 146 169 114 119 466 669 811 144 359 449 088 334 058 224 338 055 984 223`
- **Michigan4**: `136 168 113 118 366 668 146 169 114 119 466 669 016 156 011 066 115 566 126 167 112 117 266 667 161 138 155 199 244 148 449 338 599 227 007 559`
- **Florida4**: `349 489 344 399 448 899 049 459 044 099 445 599 034 039 048 089 345 359 038 358 033 088 335 588 348 009 003 388 014 734 336 011 244 346 227 224`
- **NewJersey4**: `027 257 022 077 225 577 348 389 334 339 488 889 247 279 224 229 477 779 023 028 037 078 235 258 982 778 989 299 188 882 079 088 127 189 227 155`
- **NorthCarolina4**: `249 479 244 299 447 799 049 459 044 099 445 599 024 029 047 079 245 259 027 257 022 077 225 577 242 144 009 001 019 500 003 227 226 344 192 449`
- **Indiana4**: `136 168 113 118 366 668 126 167 112 117 266 667 016 156 011 066 115 566 012 017 026 067 125 157 386 177 002 244 224 059 069 246 146 116 022 038`
- **OntarioCanada4**: `014 019 046 069 145 159 045 059 004 009 455 559 247 279 224 229 477 779 146 169 114 119 466 669 244 194 171 174 044 267 017 047 161 005 118 077`
- **SouthCarolina4**: `247 279 224 229 477 779 024 029 047 079 245 259 238 378 233 288 337 788 015 056 001 006 155 556 115 267 599 244 275 120 595 003 227 696 296 019`
- **Connecticut4**: `024 029 047 079 245 259 038 358 033 088 335 588 247 279 224 229 477 779 237 278 223 228 377 778 048 386 727 744 099 248 707 388 644 684 456 668`
- **Virginia4**: `045 059 004 009 455 559 034 039 048 089 345 359 237 278 223 228 377 778 049 459 044 099 445 599 224 177 008 349 001 055 891 248 561 136 597 334`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-05/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-05/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-05/<STATE>/play_card__tool_only*.json` (budgeted cuts)
