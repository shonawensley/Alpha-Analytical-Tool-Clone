# Predictive Portfolio — D=2026-01-09

Purpose
- Cross-state triage for a predictive day (pre-results).
- Starts from Control Center Profit Alerts (bet-ready) and annotates with Candidate Universe size.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---:|---:|---|---|
| NewYork4 | 8 | 13 | Combined:A11:BOX:045(6); Combined:A05:STR8_3:005(3); Combined:A01:BOX:045(6) | 36 | 140 | 001 007 011 066 | 3:001 005 045 |
| Delaware4 | 5 | 10 | Midday:A05:STR8_3:033(3); Midday:A02:STR8_3:033(3); Midday:A02:STR8_3:033(3) | 33 | 157 | 009 088 117 223 | 4:009 033 344 |
| Virginia4 | 4 | 12 | Evening:A01:BOX:024(6); Evening:A01:BOX:024(6); Evening:A05:STR8_8:024(8) | 32 | 157 | 004 177 199 377 | 3:004 346 455 |
| Connecticut4 | 4 | 11 | Combined:A05:STR8_3:224(3); Midday:A09:STR8_8:011(8); Midday:A12:STR8_4of8:448(4) | 32 | 129 | 088 099 223 228 | 4:088 224 244 |
| PuertoRico4 | 4 | 11 | Midday:A05:STR8_3:006(3); Midday:A01:BOX:068(6); Combined:A12:STR8_4of8:088(4) | 32 | 155 | 022 033 088 199 | 3:022 068 088 |
| OntarioCanada4 | 4 | 10 | Midday:A05:STR8_3:224(3); Combined:A12:STR8_4of8:006(4); Combined:A06:BOX:015(6) | 32 | 151 | 004 044 144 228 | 3:004 015 224 |
| Florida4 | 3 | 11 | Combined:A10:STR8_3:077(3); Evening:A05:STR8_3:224(3); Evening:A04:BOX:034(6) | 31 | 111 | 003 009 011 077 | 4:003 077 224 |
| Pennsylvania4 | 3 | 11 | Midday:A05:STR8_3:009(3); Midday:A04:BOX:019(6); Combined:A10:STR8_3:066(3) | 31 | 153 | 007 066 228 255 | 3:007 019 066 |
| NewJersey4 | 3 | 10 | Combined:A05:STR8_3:003(3); Evening:A12:STR8_4of8:078(4); Evening:A04:BOX:078(6) | 31 | 134 | 022 114 155 339 | 3:003 022 078 |
| Ohio4 | 3 | 10 | Combined:A05:STR8_3:399(3); Combined:A10:STR8_3:066(3); Combined:A04:BOX:039(6) | 31 | 136 | 009 066 113 118 | 4:009 066 399 |
| SouthCarolina4 | 2 | 7 | Midday:A05:STR8_3:244(3); Combined:A04:BOX:059(6) | 30 | 117 | 115 155 224 233 | 3:059 115 599 |
| Michigan4 | 2 | 7 | Combined:A05:STR8_3:334(3); Evening:A04:BOX:019(6) | 30 | 120 | 112 119 155 199 | 3:019 112 334 |
| NorthCarolina4 | 2 | 7 | Combined:A05:STR8_3:066(3); Combined:A04:BOX:039(6) | 30 | 151 | 001 009 044 225 | 4:001 044 066 |
| Indiana4 | 2 | 7 | Combined:A05:STR8_3:004(3); Midday:A04:BOX:069(6) | 30 | 191 | 002 022 177 226 | 3:002 004 069 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **NewYork4**: `001 010 100 005 050 500 045 054 405 450 504 540`
- **Delaware4**: `009 090 900 344 434 443 033 303 330 445 454 544`
- **Virginia4**: `004 040 400 346 364 436 463 634 643 455 545 554`
- **Connecticut4**: `448 484 844 088 808 880 224 242 422 244 424 442`
- **PuertoRico4**: `022 202 220 088 808 880 068 086 608 680 806 860`
- **OntarioCanada4**: `224 242 422 004 040 400 015 051 105 150 501 510`
- **Florida4**: `003 030 300 077 707 770 224 242 422 577 757 775`
- **Pennsylvania4**: `019 091 109 190 901 910 007 070 700 066 606 660`
- **NewJersey4**: `022 202 220 003 030 300 078 087 708 780 807 870`
- **Ohio4**: `009 090 900 066 606 660 559 595 955 399 939 993`
- **SouthCarolina4**: `115 151 511 599 959 995 059 095 509 590 905 950`
- **Michigan4**: `112 121 211 019 091 109 190 901 910 334 343 433`
- **NorthCarolina4**: `001 010 100 446 464 644 044 404 440 066 606 660`
- **Indiana4**: `002 020 200 069 096 609 690 906 960 004 040 400`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical “what to play” remains:
  - `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv` (bet-ready implied sets)
  - `sharepacks/_predictive/2026-01-09/<STATE>/candidate_universe.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-09/<STATE>/play_card.json` (budgeted cuts)
