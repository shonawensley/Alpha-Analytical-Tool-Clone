# Predictive Portfolio — D=2026-01-06

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `mixed` | rank_by: `profit_alerts`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-06/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe.json`
- Play Card file: `play_card.json`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---:|---:|---|---|---|
| PuertoRico4 | 6 | 12 | Midday:A05:STR8_3:003(3); Combined:A04:BOX:068(6); Midday:A01:BOX:036(6) | 38 | 213 | 14:022 | 022 033 088 199 | 3:022 068 088 |
| Pennsylvania4 | 5 | 10 | Midday:A05:STR8_3:000(1); Midday:A02:STR8_3:005(3); Midday:A02:STR8_3:009(3) | 37 | 166 | 10:007 | 007 066 228 255 | 3:007 059 455 |
| Virginia4 | 4 | 13 | Combined:A11:BOX:189(6); Combined:A05:STR8_3:009(3); Combined:A01:BOX:089(6) | 36 | 177 | 9:004 | 004 177 199 377 | 3:004 009 189 |
| SouthCarolina4 | 4 | 12 | Midday:A01:BOX:078(6); Midday:A05:STR8_3:007(3); Combined:A12:STR8_4of8:677(4) | 36 | 187 | 9:115 | 115 155 224 233 | 3:007 059 115 |
| NorthCarolina4 | 4 | 10 | Evening:A05:STR8_3:044(3); Evening:A02:STR8_3:044(3); Evening:A02:STR8_3:044(3) | 36 | 181 | 9:001 | 001 009 044 225 | 3:001 044 049 |
| NewJersey4 | 3 | 11 | Combined:A10:STR8_3:556(3); Evening:A05:STR8_3:778(3); Midday:A04:BOX:189(6) | 35 | 156 | 9:022 | 022 114 155 339 | 3:022 189 778 |
| Delaware4 | 3 | 11 | Midday:A05:STR8_3:003(3); Combined:A04:BOX:348(6); Combined:A10:STR8_3:009(3) | 35 | 176 | 12:009 | 009 088 223 228 | 3:004 009 348 |
| NewYork4 | 3 | 10 | Combined:A05:STR8_3:005(3); Evening:A12:STR8_4of8:008(4); Midday:A04:BOX:245(6) | 35 | 161 | 13:001 | 001 007 011 066 | 3:001 005 058 |
| Florida4 | 3 | 10 | Combined:A05:STR8_3:033(3); Combined:A12:STR8_4of8:334(4); Evening:A04:BOX:346(6) | 35 | 162 | 9:003 | 003 009 011 077 | 2:346 348 |
| Ohio4 | 3 | 10 | Midday:A05:STR8_3:229(3); Evening:A12:STR8_4of8:088(4); Combined:A04:BOX:059(6) | 35 | 178 | 12:009 | 009 066 113 118 | 3:009 059 229 |
| Michigan4 | 2 | 7 | Midday:A05:STR8_3:344(3); Evening:A04:BOX:156(6) | 34 | 155 | 10:112 | 112 119 155 199 | 3:112 119 156 |
| Connecticut4 | 2 | 7 | Combined:A05:STR8_3:224(3); Evening:A04:BOX:024(6) | 34 | 181 | 9:088 | 088 099 223 228 | 3:024 088 224 |
| OntarioCanada4 | 2 | 7 | Midday:A05:STR8_3:244(3); Evening:A04:BOX:015(6) | 34 | 182 | 9:004 | 004 044 144 244 | 3:004 015 244 |
| Indiana4 | 2 | 7 | Evening:A05:STR8_3:244(3); Midday:A04:BOX:039(6) | 34 | 194 | 9:002 | 002 022 177 226 | 4:002 066 244 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **PuertoRico4**: `022 202 220 068 086 608 680 806 860 088 808 880`
- **Pennsylvania4**: `059 095 509 590 905 950 007 070 700 455 545 554`
- **Virginia4**: `009 090 900 004 040 400 189 198 819 891 918 981`
- **SouthCarolina4**: `059 095 509 590 905 950 115 151 511 007 070 700`
- **NorthCarolina4**: `044 404 440 001 010 100 049 094 409 490 904 940`
- **NewJersey4**: `778 787 877 022 202 220 189 198 819 891 918 981`
- **Delaware4**: `009 090 900 348 384 438 483 834 843 004 040 400`
- **NewYork4**: `001 010 100 005 050 500 058 085 508 580 805 850`
- **Florida4**: `346 364 436 463 634 643 348 384 438 483 834 843`
- **Ohio4**: `009 090 900 059 095 509 590 905 950 229 292 922`
- **Michigan4**: `156 165 516 561 615 651 112 121 211 119 191 911`
- **Connecticut4**: `224 242 422 088 808 880 024 042 204 240 402 420`
- **OntarioCanada4**: `244 424 442 015 051 105 150 501 510 004 040 400`
- **Indiana4**: `244 424 442 002 020 200 066 606 660 667 676 766`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-06/control_center/profit_alerts.csv` (bet-ready implied sets; may be excluded by profile)
  - `sharepacks/_predictive/2026-01-06/<STATE>/candidate_universe.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-06/<STATE>/play_card.json` (budgeted cuts)
