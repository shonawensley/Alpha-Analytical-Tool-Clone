# Predictive Portfolio — D=2026-01-06

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-06/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file: `play_card__tool_only.json`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---:|---:|---|---|---|
| PuertoRico4 | 6 | 12 | Midday:A05:STR8_3:003(3); Combined:A04:BOX:068(6); Midday:A01:BOX:036(6) | 30 | 188 | 14:022 | 022 033 088 199 | 3:022 027 077 |
| NewYork4 | 3 | 10 | Combined:A05:STR8_3:005(3); Evening:A12:STR8_4of8:008(4); Midday:A04:BOX:245(6) | 30 | 141 | 13:001 | 001 007 011 066 | 4:001 005 006 |
| Ohio4 | 3 | 10 | Midday:A05:STR8_3:229(3); Evening:A12:STR8_4of8:088(4); Combined:A04:BOX:059(6) | 30 | 165 | 12:009 | 009 066 113 118 | 3:009 025 559 |
| NewJersey4 | 3 | 11 | Combined:A10:STR8_3:556(3); Evening:A05:STR8_3:778(3); Midday:A04:BOX:189(6) | 30 | 139 | 11:022 | 022 114 155 339 | 4:022 077 788 |
| Delaware4 | 3 | 11 | Midday:A05:STR8_3:003(3); Combined:A04:BOX:348(6); Combined:A10:STR8_3:009(3) | 30 | 166 | 11:009 | 009 088 223 228 | 4:004 009 011 |
| Michigan4 | 2 | 7 | Midday:A05:STR8_3:344(3); Evening:A04:BOX:156(6) | 30 | 143 | 10:112 | 112 119 155 199 | 3:112 119 156 |
| Pennsylvania4 | 5 | 10 | Midday:A05:STR8_3:000(1); Midday:A02:STR8_3:005(3); Midday:A02:STR8_3:009(3) | 30 | 158 | 10:007 | 007 066 228 255 | 3:007 059 557 |
| Florida4 | 3 | 10 | Combined:A05:STR8_3:033(3); Combined:A12:STR8_4of8:334(4); Evening:A04:BOX:346(6) | 30 | 149 | 9:003 | 003 009 011 077 | 3:003 346 366 |
| SouthCarolina4 | 4 | 12 | Midday:A01:BOX:078(6); Midday:A05:STR8_3:007(3); Combined:A12:STR8_4of8:677(4) | 30 | 163 | 9:115 | 115 155 224 233 | 4:005 115 224 |
| NorthCarolina4 | 4 | 10 | Evening:A05:STR8_3:044(3); Evening:A02:STR8_3:044(3); Evening:A02:STR8_3:044(3) | 30 | 168 | 9:001 | 001 009 044 225 | 3:001 044 049 |
| Connecticut4 | 2 | 7 | Combined:A05:STR8_3:224(3); Evening:A04:BOX:024(6) | 30 | 169 | 9:088 | 088 099 223 228 | 4:088 224 277 |
| OntarioCanada4 | 2 | 7 | Midday:A05:STR8_3:244(3); Evening:A04:BOX:015(6) | 30 | 174 | 9:004 | 004 044 144 244 | 3:004 015 244 |
| Virginia4 | 4 | 13 | Combined:A11:BOX:189(6); Combined:A05:STR8_3:009(3); Combined:A01:BOX:089(6) | 30 | 174 | 9:004 | 004 177 199 377 | 3:004 009 489 |
| Indiana4 | 2 | 7 | Evening:A05:STR8_3:244(3); Midday:A04:BOX:039(6) | 30 | 184 | 9:002 | 002 022 177 226 | 4:002 066 244 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **PuertoRico4**: `022 202 220 077 707 770 027 072 207 270 702 720`
- **NewYork4**: `001 010 100 005 050 500 006 060 600 011 101 110`
- **Ohio4**: `009 090 900 559 595 955 025 052 205 250 502 520`
- **NewJersey4**: `022 202 220 788 878 887 077 707 770 889 898 988`
- **Delaware4**: `009 090 900 004 040 400 559 595 955 011 101 110`
- **Michigan4**: `112 121 211 119 191 911 156 165 516 561 615 651`
- **Pennsylvania4**: `007 070 700 557 575 755 059 095 509 590 905 950`
- **Florida4**: `003 030 300 346 364 436 463 634 643 366 636 663`
- **SouthCarolina4**: `115 151 511 224 242 422 005 050 500 566 656 665`
- **NorthCarolina4**: `001 010 100 044 404 440 049 094 409 490 904 940`
- **Connecticut4**: `088 808 880 277 727 772 224 242 422 477 747 774`
- **OntarioCanada4**: `004 040 400 244 424 442 015 051 105 150 501 510`
- **Virginia4**: `004 040 400 489 498 849 894 948 984 009 090 900`
- **Indiana4**: `002 020 200 066 606 660 244 424 442 667 676 766`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-06/control_center/profit_alerts.csv` (bet-ready implied sets; may be excluded by profile)
  - `sharepacks/_predictive/2026-01-06/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-06/<STATE>/play_card__tool_only.json` (budgeted cuts)
