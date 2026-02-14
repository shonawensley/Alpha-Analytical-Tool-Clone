# Predictive Portfolio — D=2026-01-09

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| PuertoRico4 | 27 | 207 | 15:022 | 022 033 088 199 | 3:022 033 088 | 10(6) | idx[16]:2,3,4,5…(36) |
| NewYork4 | 27 | 182 | 13:001 | 001 007 011 066 | 4:001 006 007 | 2(6) | idx[16]:1,2,3,4…(36) |
| Florida4 | 27 | 189 | 11:003 | 003 009 011 077 | 2:003 077 | 4(6) | idx[16]:3,4,5,6…(36) |
| OntarioCanada4 | 27 | 205 | 11:004 | 004 044 144 228 | 3:004 009 224 | 5(6) | idx[16]:1,5,8,10…(36) |
| Delaware4 | 27 | 212 | 10:009 | 009 088 117 223 | 4:009 044 344 | 5(6) | idx[16]:4,5,6,8…(36) |
| Virginia4 | 27 | 214 | 10:004 | 004 177 199 377 | 2:004 136 | 34(6) | idx[16]:5,9,12,14…(36) |
| Connecticut4 | 27 | 173 | 9:088 | 088 099 223 228 | 2:088 228 | 30(8) | idx[16]:5,13,15,16…(36) |
| Michigan4 | 27 | 179 | 9:112 | 112 119 155 199 | 2:112 119 | 9(8) | idx[16]:2,5,6,8…(36) |
| SouthCarolina4 | 27 | 189 | 9:115 | 115 155 224 233 | 2:115 499 | 15(6) | idx[16]:1,2,5,6…(36) |
| Ohio4 | 27 | 200 | 9:009 | 009 066 113 118 | 2:009 559 | 4(6) | idx[16]:1,4,5,6…(36) |
| NorthCarolina4 | 27 | 206 | 9:001 | 001 009 044 225 | 4:001 009 044 | 25(6) | idx[16]:2,3,5,6…(36) |
| Pennsylvania4 | 27 | 211 | 9:007 | 007 066 228 255 | 2:007 112 | 9(8) | idx[16]:1,2,3,5…(36) |
| NewJersey4 | 27 | 230 | 9:022 | 022 114 155 339 | 2:022 077 | 7(8) | idx[20]:1,2,4,6…(36) |
| Indiana4 | 27 | 281 | 9:002 | 002 022 177 226 | 4:002 066 177 | 9(8) | idx[16]:3,6,7,9…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`

### B12 (`analysis_prefix`)
- **PuertoRico4**: `220 022 202 205 088 808 880 033 303 330 077 207`
- **NewYork4**: `010 001 100 060 006 600 007 011 070 101 110 700`
- **Florida4**: `030 003 300 077 707 770 752 757 717 755 045 080`
- **OntarioCanada4**: `040 004 400 224 090 009 900 095 590 242 422 270`
- **Delaware4**: `009 090 900 404 434 559 595 955 044 344 440 443`
- **Virginia4**: `004 040 400 361 349 136 341 163 316 613 631 113`
- **Connecticut4**: `088 808 880 244 844 298 228 282 822 099 223 232`
- **Michigan4**: `112 121 211 059 590 019 119 191 911 155 117 171`
- **SouthCarolina4**: `115 151 511 599 499 949 994 459 495 594 954 224`
- **Ohio4**: `009 090 900 938 983 088 058 559 595 955 389 398`
- **NorthCarolina4**: `001 010 100 644 044 404 440 446 464 009 090 900`
- **Pennsylvania4**: `007 070 700 445 019 112 121 211 416 059 095 590`
- **NewJersey4**: `022 202 220 127 077 707 770 126 110 112 037 703`
- **Indiana4**: `002 020 200 177 717 771 668 686 866 066 606 660`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-09/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,3,4,5…(36)` pack=`027 257 022 077 225 577 023 028 037 078 235 258 237 278 223 228 377 778 035 058 003 008 355 558 205 188 199 224 088 068 244 388 006 245 011 004` (src: `sharepacks/_predictive/2026-01-09/PuertoRico4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-09/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,3,4…(36)` pack=`015 056 001 006 155 556 025 057 002 007 255 557 016 156 011 066 115 566 136 168 113 118 366 668 508 005 256 504 038 449 227 667 224 245 599 244` (src: `sharepacks/_predictive/2026-01-09/NewYork4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=4(6)` pack=`035 058 003 008 355 558` (src: `sharepacks/_predictive/2026-01-09/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:3,4,5,6…(36)` pack=`035 058 003 008 355 558 027 257 022 077 225 577 045 059 004 009 455 559 025 057 002 007 255 557 224 037 717 364 727 011 244 223 543 536 334 347` (src: `sharepacks/_predictive/2026-01-09/Florida4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-09/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,5,8,10…(36)` pack=`045 059 004 009 455 559 247 279 224 229 477 779 027 257 022 077 225 577 049 459 044 099 445 599 634 228 055 244 116 349 367 068 334 499 234 264` (src: `sharepacks/_predictive/2026-01-09/OntarioCanada4/play_card__tool_only__stable10.json`)
- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-09/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:4,5,6,8…(36)` pack=`045 059 004 009 455 559 049 459 044 099 445 599 034 039 048 089 345 359 038 358 033 088 335 588 434 414 011 893 494 224 338 013 003 313 118 117` (src: `sharepacks/_predictive/2026-01-09/Delaware4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=34(6)` pack=`349 489 344 399 448 899` (src: `sharepacks/_predictive/2026-01-09/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:5,9,12,14…(36)` pack=`045 059 004 009 455 559 349 489 344 399 448 899 136 168 113 118 366 668 034 039 048 089 345 359 169 049 341 199 569 449 177 377 133 224 334 024` (src: `sharepacks/_predictive/2026-01-09/Virginia4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=30(8)` pack=`234 239 248 289 347 379 478 789` (src: `sharepacks/_predictive/2026-01-09/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:5,13,15,16…(36)` pack=`349 489 344 399 448 899 234 239 248 289 347 379 249 479 244 299 447 799 348 389 334 339 488 889 099 088 242 228 233 388 668 494 116 144 227 559` (src: `sharepacks/_predictive/2026-01-09/Connecticut4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-09/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,5,6,8…(36)` pack=`014 019 046 069 145 159 015 056 001 006 155 556 146 169 114 119 466 669 126 167 112 117 266 667 059 199 940 668 101 338 093 018 277 449 244 334` (src: `sharepacks/_predictive/2026-01-09/Michigan4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=15(6)` pack=`049 459 044 099 445 599` (src: `sharepacks/_predictive/2026-01-09/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,5,6…(36)` pack=`049 459 044 099 445 599 149 469 144 199 446 699 016 156 011 066 115 566 349 489 344 399 448 899 195 059 499 233 155 224 336 005 845 865 024 338` (src: `sharepacks/_predictive/2026-01-09/SouthCarolina4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=4(6)` pack=`035 058 003 008 355 558` (src: `sharepacks/_predictive/2026-01-09/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,4,5,6…(36)` pack=`045 059 004 009 455 559 035 058 003 008 355 558 038 358 033 088 335 588 348 389 334 339 488 889 593 849 929 878 113 599 066 116 022 224 449 055` (src: `sharepacks/_predictive/2026-01-09/Ohio4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=25(6)` pack=`149 469 144 199 446 699` (src: `sharepacks/_predictive/2026-01-09/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:2,3,5,6…(36)` pack=`049 459 044 099 445 599 149 469 144 199 446 699 146 169 114 119 466 669 014 019 046 069 145 159 009 244 001 007 225 899 667 366 166 227 224 066` (src: `sharepacks/_predictive/2026-01-09/NorthCarolina4/play_card__tool_only__stable10.json`)
- **Pennsylvania4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-09/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:1,2,3,5…(36)` pack=`025 057 002 007 255 557 015 056 001 006 155 556 014 019 046 069 145 159 016 156 011 066 115 566 445 228 059 416 012 112 899 005 413 224 113 227` (src: `sharepacks/_predictive/2026-01-09/Pennsylvania4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=7(8)` pack=`012 017 026 067 125 157 256 567` (src: `sharepacks/_predictive/2026-01-09/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,4,6…(36)` pack=`027 257 022 077 225 577 012 017 026 067 125 157 005 055 126 167 112 117 266 667 127 168 339 114 037 778 014 137 147 089 244 110 227 155 224 003` (src: `sharepacks/_predictive/2026-01-09/NewJersey4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=9(8)` pack=`014 019 046 069 145 159 456 569` (src: `sharepacks/_predictive/2026-01-09/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[16]:3,6,7,9…(36)` pack=`136 168 113 118 366 668 127 267 122 177 226 677 025 057 002 007 255 557 126 167 112 117 266 667 669 021 022 069 224 788 736 488 066 344 688 730` (src: `sharepacks/_predictive/2026-01-09/Indiana4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **PuertoRico4**: `027 257 022 077 225 577 205 280 088 033 800 068 388 188 278 287 782 872 199 919 991 224 242 422`
- **NewYork4**: `015 056 001 006 155 556 007 011 005 668 504 256 000 118 507 508 057 075 510 066 606 660 559 595`
- **Florida4**: `035 058 003 008 355 558 077 727 717 755 364 536 543 037 752 757 045 057 075 570 750 347 357 085`
- **OntarioCanada4**: `045 059 004 009 455 559 224 055 116 367 634 334 349 489 499 949 994 270 274 279 049 094 490 940`
- **Delaware4**: `045 059 004 009 455 559 404 434 084 414 494 338 445 313 893 938 983 011 118 504 054 450 540 156`
- **Virginia4**: `349 489 344 399 448 899 004 361 341 034 039 113 364 059 539 169 049 084 093 390 930 177 199 377`
- **Connecticut4**: `234 239 248 289 347 379 478 789 244 844 088 294 894 242 228 099 223 232 322 909 990 388 838 883`
- **Michigan4**: `014 019 046 069 145 159 456 569 112 059 119 155 117 338 093 277 051 101 141 041 940 064 199 515`
- **SouthCarolina4**: `049 459 044 099 445 599 499 115 195 665 224 059 595 005 336 694 894 645 695 140 145 159 591 951`
- **Ohio4**: `035 058 003 008 355 558 009 938 088 889 559 878 929 593 849 538 835 598 985 053 066 113 118 131`
- **NorthCarolina4**: `149 469 144 199 446 699 001 940 690 044 009 646 244 899 166 299 649 194 496 344 434 443 049 094`
- **Pennsylvania4**: `014 019 046 069 145 159 456 569 007 445 112 005 416 059 015 012 017 062 125 152 251 521 066 228`
- **NewJersey4**: `012 017 026 067 125 157 256 567 022 127 077 005 037 014 089 055 126 110 112 172 271 721 120 062`
- **Indiana4**: `014 019 046 069 145 159 456 569 002 177 668 066 636 766 186 224 488 788 596 659 688 868 886 021`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`)

- **PuertoRico4**: `027 257 022 077 225 577 023 028 037 078 235 258 237 278 223 228 377 778 035 058 003 008 355 558 205 188 199 224 088 068 244 388 006 245 011 004`
- **NewYork4**: `015 056 001 006 155 556 025 057 002 007 255 557 016 156 011 066 115 566 136 168 113 118 366 668 508 005 256 504 038 449 227 667 224 245 599 244`
- **Florida4**: `035 058 003 008 355 558 027 257 022 077 225 577 045 059 004 009 455 559 025 057 002 007 255 557 224 037 717 364 727 011 244 223 543 536 334 347`
- **OntarioCanada4**: `045 059 004 009 455 559 247 279 224 229 477 779 027 257 022 077 225 577 049 459 044 099 445 599 634 228 055 244 116 349 367 068 334 499 234 264`
- **Delaware4**: `045 059 004 009 455 559 049 459 044 099 445 599 034 039 048 089 345 359 038 358 033 088 335 588 434 414 011 893 494 224 338 013 003 313 118 117`
- **Virginia4**: `045 059 004 009 455 559 349 489 344 399 448 899 136 168 113 118 366 668 034 039 048 089 345 359 169 049 341 199 569 449 177 377 133 224 334 024`
- **Connecticut4**: `349 489 344 399 448 899 234 239 248 289 347 379 249 479 244 299 447 799 348 389 334 339 488 889 099 088 242 228 233 388 668 494 116 144 227 559`
- **Michigan4**: `014 019 046 069 145 159 015 056 001 006 155 556 146 169 114 119 466 669 126 167 112 117 266 667 059 199 940 668 101 338 093 018 277 449 244 334`
- **SouthCarolina4**: `049 459 044 099 445 599 149 469 144 199 446 699 016 156 011 066 115 566 349 489 344 399 448 899 195 059 499 233 155 224 336 005 845 865 024 338`
- **Ohio4**: `045 059 004 009 455 559 035 058 003 008 355 558 038 358 033 088 335 588 348 389 334 339 488 889 593 849 929 878 113 599 066 116 022 224 449 055`
- **NorthCarolina4**: `049 459 044 099 445 599 149 469 144 199 446 699 146 169 114 119 466 669 014 019 046 069 145 159 009 244 001 007 225 899 667 366 166 227 224 066`
- **Pennsylvania4**: `025 057 002 007 255 557 015 056 001 006 155 556 014 019 046 069 145 159 016 156 011 066 115 566 445 228 059 416 012 112 899 005 413 224 113 227`
- **NewJersey4**: `027 257 022 077 225 577 012 017 026 067 125 157 005 055 126 167 112 117 266 667 127 168 339 114 037 778 014 137 147 089 244 110 227 155 224 003`
- **Indiana4**: `136 168 113 118 366 668 127 267 122 177 226 677 025 057 002 007 255 557 126 167 112 117 266 667 669 021 022 069 224 788 736 488 066 344 688 730`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-09/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-09/<STATE>/play_card__tool_only*.json` (budgeted cuts)
