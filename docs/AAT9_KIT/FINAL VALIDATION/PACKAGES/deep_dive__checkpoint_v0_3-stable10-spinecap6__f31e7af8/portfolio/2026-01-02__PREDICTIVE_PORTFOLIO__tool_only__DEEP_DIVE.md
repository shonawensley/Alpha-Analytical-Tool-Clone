# Predictive Portfolio — D=2026-01-02

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-02/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only*.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| Pennsylvania4 | 27 | 188 | 13:007 | 007 228 255 277 | 2:007 378 | 3(6) | idx[20]:1,3,4,5…(36) |
| Ohio4 | 27 | 191 | 11:009 | 009 066 113 114 | 2:009 057 | 3(6) | idx[20]:1,2,3,4…(36) |
| Delaware4 | 27 | 204 | 11:009 | 009 088 223 228 | 3:004 009 559 | 5(6) | idx[22]:1,2,5,6…(36) |
| NorthCarolina4 | 27 | 210 | 11:001 | 001 009 044 225 | 4:001 009 044 | 11(8) | idx[20]:1,2,4,5…(36) |
| PuertoRico4 | 27 | 273 | 11:022 | 022 033 088 199 | 3:022 224 225 | 10(6) | idx[20]:2,7,10,11…(36) |
| Indiana4 | 27 | 226 | 10:002 | 002 022 177 226 | 3:002 177 667 | 7(8) | idx[20]:2,3,5,6…(36) |
| Connecticut4 | 27 | 229 | 10:088 | 088 099 223 228 | 1:088 | 23(6) | idx[20]:2,3,4,5…(36) |
| NewJersey4 | 27 | 154 | 9:022 | 022 114 155 339 | 2:022 077 | 28(6) | idx[20]:1,2,10,12…(36) |
| Michigan4 | 27 | 170 | 9:112 | 112 119 155 199 | 3:112 155 199 | 23(6) | idx[20]:1,2,4,5…(36) |
| Florida4 | 27 | 190 | 9:003 | 003 008 009 011 | 3:003 008 778 | 8(8) | idx[22]:3,4,5,6…(36) |
| SouthCarolina4 | 27 | 194 | 9:115 | 115 155 224 288 | 3:011 115 224 | 2(6) | idx[20]:2,3,4,5…(36) |
| Virginia4 | 27 | 199 | 9:004 | 004 177 199 377 | 4:004 177 455 | 12(8) | idx[20]:2,3,5,6…(36) |
| OntarioCanada4 | 27 | 211 | 9:004 | 004 044 144 244 | 2:004 244 | 23(6) | idx[20]:2,3,4,5…(36) |
| NewYork4 | 27 | 228 | 9:001 | 001 007 011 066 | 3:001 006 066 | 6(6) | idx[20]:2,3,4,5…(36) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

Play strategy defaults (configurable):
- B12: `analysis_prefix`
- B24: `vtrac_pack_boxed_first_laneonly_presetB`
- B36: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

### B12 (`analysis_prefix`)
- **Pennsylvania4**: `007 070 700 755 759 378 387 738 783 837 873 077`
- **Ohio4**: `090 009 900 570 075 507 705 057 750 025 520 559`
- **Delaware4**: `090 009 900 040 004 400 595 411 559 955 114 119`
- **NorthCarolina4**: `001 010 100 044 404 440 009 344 434 443 090 900`
- **PuertoRico4**: `022 202 220 224 225 252 522 242 422 144 199 919`
- **Indiana4**: `020 002 200 066 626 177 717 771 667 676 766 266`
- **Connecticut4**: `088 808 880 086 228 386 683 540 580 750 368 784`
- **NewJersey4**: `022 202 220 077 242 279 297 792 707 770 292 889`
- **Michigan4**: `112 121 211 155 515 551 565 199 919 991 559 595`
- **Florida4**: `003 030 300 008 080 800 778 787 877 338 388 667`
- **SouthCarolina4**: `115 151 511 138 831 224 242 422 011 101 110 183`
- **Virginia4**: `004 040 400 771 177 717 455 545 554 559 595 955`
- **OntarioCanada4**: `004 040 400 114 244 424 442 167 176 617 671 716`
- **NewYork4**: `001 010 100 066 660 606 948 011 006 060 600 249`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (sometimes multi-index) and which play_card file it came from.

- **Pennsylvania4**: B24 `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-02/Pennsylvania4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,3,4,5…(36)` pack=`025 057 002 007 255 557 247 279 224 229 477 779 045 059 004 009 237 278 223 228 759 138 077 038 378 599 339 338 593 277 055 717 899 499 168 855` (src: `sharepacks/_predictive/2026-01-02/Pennsylvania4/play_card__tool_only__stable10.json`)
- **Ohio4**: B24 `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-02/Ohio4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,3,4…(36)` pack=`025 057 002 007 255 557 045 059 004 009 455 559 027 257 022 077 247 279 224 229 058 056 018 259 677 055 099 368 114 066 113 388 244 116 906 449` (src: `sharepacks/_predictive/2026-01-02/Ohio4/play_card__tool_only__stable10.json`)
- **Delaware4**: B24 `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:1,2,5,6…(36)` pack=`045 059 004 009 455 559 146 169 114 119 466 669 449 499 149 469 144 199 171 223 459 294 001 274 124 271 017 014 245 368 088 344 871 011 334 005` (src: `sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__stable10.json`)
- **NorthCarolina4**: B24 `idx(size)=11(8)` pack=`023 028 037 078 235 258 357 578` (src: `sharepacks/_predictive/2026-01-02/NorthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,4,5…(36)` pack=`049 459 044 099 445 599 027 257 022 077 225 577 045 059 004 009 015 056 001 006 344 242 244 144 032 003 932 005 232 033 240 233 339 227 338 093` (src: `sharepacks/_predictive/2026-01-02/NorthCarolina4/play_card__tool_only__stable10.json`)
- **PuertoRico4**: B24 `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-02/PuertoRico4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,7,10,11…(36)` pack=`027 257 022 077 225 577 149 469 144 199 446 699 247 279 224 229 023 028 037 078 136 223 236 233 134 226 344 244 033 624 445 026 234 334 001 116` (src: `sharepacks/_predictive/2026-01-02/PuertoRico4/play_card__tool_only__stable10.json`)
- **Indiana4**: B24 `idx(size)=7(8)` pack=`012 017 026 067 125 157 256 567` (src: `sharepacks/_predictive/2026-01-02/Indiana4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`025 057 002 007 255 557 012 017 026 067 125 157 126 167 112 117 016 156 011 066 368 177 056 224 164 366 367 022 069 079 447 144 116 559 359 377` (src: `sharepacks/_predictive/2026-01-02/Indiana4/play_card__tool_only__stable10.json`)
- **Connecticut4**: B24 `idx(size)=23(6)` pack=`138 368 133 188 336 688` (src: `sharepacks/_predictive/2026-01-02/Connecticut4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`038 358 033 088 335 588 237 278 223 228 377 778 045 059 004 009 138 368 133 188 086 580 784 039 144 224 027 388 750 099 006 456 346 116 117 710` (src: `sharepacks/_predictive/2026-01-02/Connecticut4/play_card__tool_only__stable10.json`)
- **NewJersey4**: B24 `idx(size)=28(6)` pack=`247 279 224 229 477 779` (src: `sharepacks/_predictive/2026-01-02/NewJersey4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,10,12…(36)` pack=`247 279 224 229 477 779 027 257 022 077 225 577 348 389 334 339 249 479 244 299 238 282 127 138 182 155 114 227 989 118 599 199 388 449 709 005` (src: `sharepacks/_predictive/2026-01-02/NewJersey4/play_card__tool_only__stable10.json`)
- **Michigan4**: B24 `idx(size)=23(6)` pack=`138 368 133 188 336 688` (src: `sharepacks/_predictive/2026-01-02/Michigan4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:1,2,4,5…(36)` pack=`015 056 001 006 155 556 138 368 133 188 336 688 016 156 011 066 146 169 114 119 112 168 355 335 199 069 559 224 599 244 055 166 449 338 128 124` (src: `sharepacks/_predictive/2026-01-02/Michigan4/play_card__tool_only__stable10.json`)
- **Florida4**: B24 `idx(size)=8(8)` pack=`013 018 036 068 135 158 356 568` (src: `sharepacks/_predictive/2026-01-02/Florida4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[22]:3,4,5,6…(36)` pack=`146 169 114 119 466 669 013 018 036 068 135 158 338 388 035 058 003 008 368 667 011 767 027 778 224 596 009 366 567 057 088 599 699 244 227 449` (src: `sharepacks/_predictive/2026-01-02/Florida4/play_card__tool_only__stable10.json`)
- **SouthCarolina4**: B24 `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-02/SouthCarolina4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`015 056 001 006 155 556 138 368 133 188 336 688 013 018 036 068 016 156 011 066 118 238 182 338 224 126 389 009 007 017 078 008 599 335 232 489` (src: `sharepacks/_predictive/2026-01-02/SouthCarolina4/play_card__tool_only__stable10.json`)
- **Virginia4**: B24 `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-02/Virginia4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,5,6…(36)` pack=`045 059 004 009 455 559 127 267 122 177 226 677 024 029 047 079 247 279 224 229 349 167 057 561 015 377 244 791 169 227 339 133 113 199 337 345` (src: `sharepacks/_predictive/2026-01-02/Virginia4/play_card__tool_only__stable10.json`)
- **OntarioCanada4**: B24 `idx(size)=23(6)` pack=`138 368 133 188 336 688` (src: `sharepacks/_predictive/2026-01-02/OntarioCanada4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`045 059 004 009 455 559 136 168 113 118 366 668 138 368 133 188 146 169 114 119 884 167 484 014 001 115 244 225 255 017 226 678 044 144 558 237` (src: `sharepacks/_predictive/2026-01-02/OntarioCanada4/play_card__tool_only__stable10.json`)
- **NewYork4**: B24 `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-02/NewYork4/play_card__tool_only__stable10.json`) | B36 `idx(size)=idx[20]:2,3,4,5…(36)` pack=`016 156 011 066 115 566 015 056 001 006 155 556 049 459 044 099 136 168 113 118 948 559 249 026 224 144 058 334 266 678 248 007 949 688 677 388` (src: `sharepacks/_predictive/2026-01-02/NewYork4/play_card__tool_only__stable10.json`)

### B24 (`vtrac_pack_boxed_first_laneonly_presetB`)

- **Pennsylvania4**: `025 057 002 007 255 557 759 590 138 559 277 338 388 055 378 387 738 783 837 873 077 707 770 717`
- **Ohio4**: `025 057 002 007 255 557 090 559 055 224 225 056 058 050 027 072 207 257 270 275 527 572 702 720`
- **Delaware4**: `045 059 004 009 455 559 494 499 411 119 414 171 124 294 459 495 594 954 054 450 545 554 271 274`
- **NorthCarolina4**: `023 028 037 078 235 258 357 578 001 044 009 344 242 003 006 244 424 442 040 232 292 223 202 932`
- **PuertoRico4**: `027 257 022 077 225 577 224 144 199 136 226 236 334 134 469 496 624 649 694 946 964 223 232 322`
- **Indiana4**: `012 017 026 067 125 157 256 567 020 066 626 177 116 368 667 224 242 422 688 868 886 266 606 660`
- **Connecticut4**: `138 368 133 188 336 688 088 086 228 116 388 784 006 338 540 580 750 031 036 099 223 232 282 322`
- **NewJersey4**: `247 279 224 229 477 779 077 022 989 299 227 277 889 182 282 799 249 294 492 942 938 983 742 114`
- **Michigan4**: `138 368 133 188 336 688 155 112 565 559 199 168 006 335 355 169 196 691 961 183 386 683 813 831`
- **Florida4**: `013 018 036 068 135 158 356 568 338 388 003 008 368 778 667 669 766 767 596 659 965 688 377 031`
- **SouthCarolina4**: `015 056 001 006 155 556 138 115 081 158 224 011 118 338 388 838 883 183 238 283 318 328 381 382`
- **Virginia4**: `024 029 047 079 245 259 457 579 771 004 227 455 349 399 559 791 277 272 722 561 167 617 716 597`
- **OntarioCanada4**: `138 368 133 188 336 688 004 114 244 167 115 181 884 225 161 484 164 183 186 386 681 683 831 836`
- **NewYork4**: `016 156 011 066 115 566 001 948 006 688 949 168 668 249 026 116 788 160 610 940 248 561 007 070`

### B36 (`v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`)

- **Pennsylvania4**: `025 057 002 007 255 557 247 279 224 229 477 779 045 059 004 009 237 278 223 228 759 138 077 038 378 599 339 338 593 277 055 717 899 499 168 855`
- **Ohio4**: `025 057 002 007 255 557 045 059 004 009 455 559 027 257 022 077 247 279 224 229 058 056 018 259 677 055 099 368 114 066 113 388 244 116 906 449`
- **Delaware4**: `045 059 004 009 455 559 146 169 114 119 466 669 449 499 149 469 144 199 171 223 459 294 001 274 124 271 017 014 245 368 088 344 871 011 334 005`
- **NorthCarolina4**: `049 459 044 099 445 599 027 257 022 077 225 577 045 059 004 009 015 056 001 006 344 242 244 144 032 003 932 005 232 033 240 233 339 227 338 093`
- **PuertoRico4**: `027 257 022 077 225 577 149 469 144 199 446 699 247 279 224 229 023 028 037 078 136 223 236 233 134 226 344 244 033 624 445 026 234 334 001 116`
- **Indiana4**: `025 057 002 007 255 557 012 017 026 067 125 157 126 167 112 117 016 156 011 066 368 177 056 224 164 366 367 022 069 079 447 144 116 559 359 377`
- **Connecticut4**: `038 358 033 088 335 588 237 278 223 228 377 778 045 059 004 009 138 368 133 188 086 580 784 039 144 224 027 388 750 099 006 456 346 116 117 710`
- **NewJersey4**: `247 279 224 229 477 779 027 257 022 077 225 577 348 389 334 339 249 479 244 299 238 282 127 138 182 155 114 227 989 118 599 199 388 449 709 005`
- **Michigan4**: `015 056 001 006 155 556 138 368 133 188 336 688 016 156 011 066 146 169 114 119 112 168 355 335 199 069 559 224 599 244 055 166 449 338 128 124`
- **Florida4**: `146 169 114 119 466 669 013 018 036 068 135 158 338 388 035 058 003 008 368 667 011 767 027 778 224 596 009 366 567 057 088 599 699 244 227 449`
- **SouthCarolina4**: `015 056 001 006 155 556 138 368 133 188 336 688 013 018 036 068 016 156 011 066 118 238 182 338 224 126 389 009 007 017 078 008 599 335 232 489`
- **Virginia4**: `045 059 004 009 455 559 127 267 122 177 226 677 024 029 047 079 247 279 224 229 349 167 057 561 015 377 244 791 169 227 339 133 113 199 337 345`
- **OntarioCanada4**: `045 059 004 009 455 559 136 168 113 118 366 668 138 368 133 188 146 169 114 119 884 167 484 014 001 115 244 225 255 017 226 678 044 144 558 237`
- **NewYork4**: `016 156 011 066 115 566 015 056 001 006 155 556 049 459 044 099 136 168 113 118 948 559 249 026 224 144 058 334 266 678 248 007 949 688 677 388`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-02/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-02/<STATE>/candidate_universe__tool_only*.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-02/<STATE>/play_card__tool_only*.json` (budgeted cuts)
