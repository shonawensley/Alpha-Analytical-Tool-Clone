# Predictive Portfolio — D=2026-01-06

Purpose
- Cross-state triage for a predictive day (pre-results).
- Starts from Control Center Profit Alerts (bet-ready) and annotates with Candidate Universe size.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-06/control_center/profit_alerts.csv`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---:|---:|---|---|
| PuertoRico4 | 6 | 12 | Midday:A05:STR8_3:003(3); Combined:A04:BOX:068(6); Midday:A01:BOX:036(6) | 34 | 172 | 022 033 088 199 | 3:022 068 088 |
| Pennsylvania4 | 5 | 10 | Midday:A05:STR8_3:000(1); Midday:A02:STR8_3:005(3); Midday:A02:STR8_3:009(3) | 33 | 133 | 007 066 228 255 | 4:000 007 455 |
| Virginia4 | 4 | 13 | Combined:A11:BOX:189(6); Combined:A05:STR8_3:009(3); Combined:A01:BOX:089(6) | 32 | 148 | 004 177 199 377 | 3:004 009 189 |
| SouthCarolina4 | 4 | 12 | Midday:A01:BOX:078(6); Midday:A05:STR8_3:007(3); Combined:A12:STR8_4of8:677(4) | 32 | 138 | 115 155 224 233 | 4:007 115 224 |
| NorthCarolina4 | 4 | 10 | Evening:A05:STR8_3:044(3); Evening:A02:STR8_3:044(3); Evening:A02:STR8_3:044(3) | 32 | 147 | 001 009 044 225 | 3:001 029 044 |
| NewJersey4 | 3 | 11 | Combined:A10:STR8_3:556(3); Evening:A05:STR8_3:778(3); Midday:A04:BOX:189(6) | 31 | 117 | 022 114 155 339 | 3:022 189 778 |
| Delaware4 | 3 | 11 | Midday:A05:STR8_3:003(3); Combined:A04:BOX:348(6); Combined:A10:STR8_3:009(3) | 31 | 140 | 009 088 223 228 | 4:003 004 009 |
| Florida4 | 3 | 10 | Combined:A05:STR8_3:033(3); Combined:A12:STR8_4of8:334(4); Evening:A04:BOX:346(6) | 31 | 118 | 003 009 011 077 | 3:003 033 346 |
| NewYork4 | 3 | 10 | Combined:A05:STR8_3:005(3); Evening:A12:STR8_4of8:008(4); Midday:A04:BOX:245(6) | 31 | 119 | 001 007 011 066 | 4:001 005 006 |
| Ohio4 | 3 | 10 | Midday:A05:STR8_3:229(3); Evening:A12:STR8_4of8:088(4); Combined:A04:BOX:059(6) | 31 | 139 | 009 066 113 118 | 4:009 088 229 |
| Michigan4 | 2 | 7 | Midday:A05:STR8_3:344(3); Evening:A04:BOX:156(6) | 30 | 114 | 112 119 155 199 | 3:112 119 156 |
| Connecticut4 | 2 | 7 | Combined:A05:STR8_3:224(3); Evening:A04:BOX:024(6) | 30 | 136 | 088 099 223 228 | 3:024 088 224 |
| OntarioCanada4 | 2 | 7 | Midday:A05:STR8_3:244(3); Evening:A04:BOX:015(6) | 30 | 139 | 004 044 144 244 | 3:004 015 244 |
| Indiana4 | 2 | 7 | Evening:A05:STR8_3:244(3); Midday:A04:BOX:039(6) | 30 | 155 | 002 022 177 226 | 4:002 066 244 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **PuertoRico4**: `022 202 220 068 086 608 680 806 860 088 808 880`
- **Pennsylvania4**: `007 070 700 455 545 554 000 557 575 755 590 059`
- **Virginia4**: `009 090 900 004 040 400 189 198 819 891 918 981`
- **SouthCarolina4**: `115 151 511 007 070 700 224 242 422 677 767 776`
- **NorthCarolina4**: `044 404 440 001 010 100 029 092 209 290 902 920`
- **NewJersey4**: `778 787 877 022 202 220 189 198 819 891 918 981`
- **Delaware4**: `009 090 900 004 040 400 003 030 300 559 595 955`
- **Florida4**: `346 364 436 463 634 643 003 030 300 033 303 330`
- **NewYork4**: `001 010 100 005 050 500 008 080 800 006 060 600`
- **Ohio4**: `009 090 900 229 292 922 088 808 880 559 595 955`
- **Michigan4**: `112 121 211 156 165 516 561 615 651 119 191 911`
- **Connecticut4**: `224 242 422 088 808 880 024 042 204 240 402 420`
- **OntarioCanada4**: `244 424 442 015 051 105 150 501 510 004 040 400`
- **Indiana4**: `244 424 442 002 020 200 066 606 660 667 676 766`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical “what to play” remains:
  - `sharepacks/_predictive/2026-01-06/control_center/profit_alerts.csv` (bet-ready implied sets)
  - `sharepacks/_predictive/2026-01-06/<STATE>/candidate_universe.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-06/<STATE>/play_card.json` (budgeted cuts)
