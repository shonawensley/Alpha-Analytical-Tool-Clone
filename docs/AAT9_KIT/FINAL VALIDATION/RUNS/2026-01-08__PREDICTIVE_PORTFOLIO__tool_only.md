# Predictive Portfolio — D=2026-01-08

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file: `play_card__tool_only.json`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---:|---:|---|---|---|
| PuertoRico4 | 1 | 3 | Evening:A04:BOX:068(6) | 30 | 182 | 16:022 | 022 033 199 299 | 3:022 027 077 |
| NewYork4 | 6 | 13 | Combined:A11:BOX:459(6); Combined:A05:STR8_3:005(3); Combined:A01:BOX:057(6) | 30 | 140 | 14:001 | 001 007 011 066 | 4:001 005 006 |
| Florida4 | 3 | 10 | Combined:A05:STR8_3:334(3); Combined:A12:STR8_4of8:334(4); Midday:A04:BOX:346(6) | 30 | 130 | 11:003 | 003 009 011 077 | 4:003 033 334 |
| NewJersey4 | 4 | 11 | Combined:A10:STR8_3:556(3); Evening:A05:STR8_3:778(3); Midday:A12:STR8_4of8:089(4) | 30 | 160 | 11:022 | 022 114 155 339 | 3:022 077 168 |
| Delaware4 | 5 | 11 | Midday:A05:STR8_3:033(3); Midday:A09:STR8_8:011(8); Midday:A02:STR8_3:033(3) | 30 | 167 | 11:009 | 009 088 223 228 | 4:004 009 011 |
| Michigan4 | 3 | 10 | Midday:A05:STR8_3:344(3); Combined:A12:STR8_4of8:004(4); Evening:A04:BOX:019(6) | 30 | 154 | 10:112 | 112 119 155 199 | 4:112 114 119 |
| Pennsylvania4 | 5 | 10 | Midday:A05:STR8_3:009(3); Midday:A02:STR8_3:001(3); Midday:A02:STR8_3:009(3) | 30 | 169 | 10:007 | 007 066 228 255 | 4:002 007 112 |
| Connecticut4 | 2 | 7 | Combined:A05:STR8_3:224(3); Evening:A04:BOX:248(6) | 30 | 149 | 9:088 | 088 099 223 228 | 4:088 224 244 |
| SouthCarolina4 | 2 | 7 | Midday:A05:STR8_3:244(3); Combined:A04:BOX:369(6) | 30 | 157 | 9:115 | 115 155 224 233 | 4:115 224 566 |
| Ohio4 | 2 | 8 | Evening:A05:STR8_3:889(3); Combined:A04:BOX:359(6) | 30 | 161 | 9:009 | 009 066 113 118 | 4:009 299 559 |
| NorthCarolina4 | 2 | 7 | Evening:A05:STR8_3:244(3); Evening:A04:BOX:016(6) | 30 | 171 | 9:001 | 001 009 044 225 | 4:001 006 044 |
| Virginia4 | 5 | 12 | Evening:A01:BOX:024(6); Evening:A01:BOX:024(6); Evening:A05:STR8_8:024(8) | 30 | 177 | 9:004 | 004 177 199 377 | 3:004 224 349 |
| OntarioCanada4 | 3 | 10 | Midday:A05:STR8_3:224(3); Combined:A12:STR8_4of8:006(4); Evening:A04:BOX:015(6) | 30 | 181 | 9:004 | 004 044 144 228 | 4:004 022 044 |
| Indiana4 | 3 | 10 | Evening:A05:STR8_3:344(3); Combined:A10:STR8_3:002(3); Midday:A04:BOX:069(6) | 30 | 194 | 9:002 | 002 022 177 226 | 4:002 066 244 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **PuertoRico4**: `022 202 220 077 707 770 027 072 207 270 702 720`
- **NewYork4**: `001 010 100 005 050 500 006 060 600 011 101 110`
- **Florida4**: `003 030 300 335 353 533 033 303 330 334 343 433`
- **NewJersey4**: `022 202 220 077 707 770 168 186 618 681 816 861`
- **Delaware4**: `009 090 900 011 101 110 004 040 400 559 595 955`
- **Michigan4**: `112 121 211 119 191 911 155 515 551 114 141 411`
- **Pennsylvania4**: `007 070 700 112 121 211 002 020 200 255 525 552`
- **Connecticut4**: `088 808 880 448 484 844 244 424 442 224 242 422`
- **SouthCarolina4**: `115 151 511 599 959 995 224 242 422 566 656 665`
- **Ohio4**: `009 090 900 559 595 955 889 898 988 299 929 992`
- **NorthCarolina4**: `001 010 100 244 424 442 044 404 440 006 060 600`
- **Virginia4**: `004 040 400 349 394 439 493 934 943 224 242 422`
- **OntarioCanada4**: `004 040 400 224 242 422 044 404 440 022 202 220`
- **Indiana4**: `002 020 200 066 606 660 667 676 766 244 424 442`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv` (bet-ready implied sets; may be excluded by profile)
  - `sharepacks/_predictive/2026-01-08/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-08/<STATE>/play_card__tool_only.json` (budgeted cuts)
