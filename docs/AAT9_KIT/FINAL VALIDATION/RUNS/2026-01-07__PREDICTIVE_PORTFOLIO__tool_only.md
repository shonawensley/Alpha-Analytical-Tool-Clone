# Predictive Portfolio — D=2026-01-07

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-07/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file: `play_card__tool_only.json`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed |
|---|---:|---:|---|---:|---:|---|---|---|
| NewYork4 | 3 | 10 | Combined:A05:STR8_3:001(3); Evening:A12:STR8_4of8:008(4); Midday:A04:BOX:245(6) | 30 | 136 | 14:001 | 001 007 011 066 | 3:001 006 056 |
| PuertoRico4 | 3 | 11 | Midday:A05:STR8_3:003(3); Evening:A04:BOX:068(6); Midday:A12:STR8_4of8:066(4) | 30 | 190 | 14:022 | 022 033 199 299 | 3:022 027 077 |
| NewJersey4 | 3 | 11 | Combined:A10:STR8_3:556(3); Evening:A05:STR8_3:778(3); Midday:A04:BOX:189(6) | 30 | 146 | 11:022 | 022 114 155 339 | 4:022 077 088 |
| Delaware4 | 6 | 12 | Combined:A05:STR8_3:334(3); Midday:A01:BOX:038(6); Midday:A07:BOX:035(6) | 30 | 169 | 11:009 | 009 088 223 228 | 4:004 009 011 |
| Michigan4 | 3 | 10 | Midday:A05:STR8_3:344(3); Combined:A12:STR8_4of8:001(4); Evening:A04:BOX:016(6) | 30 | 151 | 10:112 | 112 119 155 199 | 4:112 114 119 |
| Pennsylvania4 | 5 | 10 | Midday:A05:STR8_3:000(1); Midday:A02:STR8_3:001(3); Midday:A02:STR8_3:009(3) | 30 | 168 | 10:007 | 007 066 228 255 | 3:002 007 015 |
| OntarioCanada4 | 2 | 7 | Midday:A05:STR8_3:244(3); Evening:A04:BOX:015(6) | 30 | 179 | 10:004 | 004 044 144 228 | 3:004 224 247 |
| Florida4 | 3 | 10 | Evening:A05:STR8_3:033(3); Evening:A12:STR8_4of8:334(4); Midday:A04:BOX:346(6) | 30 | 151 | 9:003 | 003 009 011 077 | 3:003 334 346 |
| Connecticut4 | 4 | 11 | Combined:A05:STR8_3:224(3); Midday:A09:STR8_8:012(8); Midday:A12:STR8_4of8:448(4) | 30 | 152 | 9:088 | 088 099 223 228 | 4:088 224 244 |
| Ohio4 | 2 | 7 | Evening:A05:STR8_3:559(3); Combined:A04:BOX:089(6) | 30 | 163 | 9:009 | 009 066 113 118 | 4:009 088 559 |
| SouthCarolina4 | 3 | 11 | Midday:A05:STR8_3:224(3); Midday:A01:BOX:079(6); Combined:A04:BOX:369(6) | 30 | 166 | 9:115 | 115 155 224 233 | 4:115 224 566 |
| NorthCarolina4 | 3 | 10 | Evening:A05:STR8_3:244(3); Combined:A12:STR8_4of8:066(4); Evening:A04:BOX:246(6) | 30 | 172 | 9:001 | 001 009 044 225 | 4:001 006 044 |
| Virginia4 | 6 | 13 | Combined:A11:BOX:134(6); Combined:A05:STR8_3:009(3); Combined:A01:BOX:019(6) | 30 | 172 | 9:004 | 004 177 199 377 | 3:004 009 349 |
| Indiana4 | 4 | 10 | Evening:A05:STR8_3:244(3); Combined:A10:STR8_3:002(3); Combined:A12:STR8_4of8:004(4) | 30 | 192 | 9:002 | 002 022 177 226 | 3:002 066 267 |

## Play cards (B12, play_box_first)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

- **NewYork4**: `001 010 100 006 060 600 056 065 506 560 605 650`
- **PuertoRico4**: `022 202 220 077 707 770 027 072 207 270 702 720`
- **NewJersey4**: `022 202 220 077 707 770 088 808 880 788 878 887`
- **Delaware4**: `009 090 900 004 040 400 011 101 110 559 595 955`
- **Michigan4**: `112 121 211 119 191 911 155 515 551 114 141 411`
- **Pennsylvania4**: `007 070 700 002 020 200 015 051 105 150 501 510`
- **OntarioCanada4**: `004 040 400 224 242 422 247 274 427 472 724 742`
- **Florida4**: `003 030 300 334 343 433 346 364 436 463 634 643`
- **Connecticut4**: `088 808 880 244 424 442 448 484 844 224 242 422`
- **Ohio4**: `009 090 900 559 595 955 889 898 988 088 808 880`
- **SouthCarolina4**: `115 151 511 224 242 422 599 959 995 566 656 665`
- **NorthCarolina4**: `001 010 100 044 404 440 006 060 600 244 424 442`
- **Virginia4**: `004 040 400 349 394 439 493 934 943 009 090 900`
- **Indiana4**: `002 020 200 267 276 627 672 726 762 066 606 660`

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-07/control_center/profit_alerts.csv` (bet-ready implied sets; may be excluded by profile)
  - `sharepacks/_predictive/2026-01-07/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-07/<STATE>/play_card__tool_only.json` (budgeted cuts)
