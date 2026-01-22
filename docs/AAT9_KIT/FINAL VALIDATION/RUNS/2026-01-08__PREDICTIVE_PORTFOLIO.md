# Predictive Portfolio — D=2026-01-08

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `mixed` | rank_by: `profit_alerts`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe.json`
- Play Card file(s): `play_card*.json`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---:|---:|---|---|---|---|---|
| NewYork4 | 6 | 13 | Combined:A11:BOX:459(6); Combined:A05:STR8_3:005(3); Combined:A01:BOX:057(6) | 38 | 164 | 16:001 | 001 007 011 066 | 2:001 057 | - | - |
| Virginia4 | 5 | 12 | Evening:A01:BOX:024(6); Evening:A01:BOX:024(6); Evening:A05:STR8_8:024(8) | 37 | 179 | 9:004 | 004 177 199 377 | 2:004 024 | - | - |
| Delaware4 | 5 | 11 | Midday:A05:STR8_3:033(3); Midday:A09:STR8_8:011(8); Midday:A02:STR8_3:033(3) | 37 | 204 | 10:009 | 009 088 223 228 | 2:009 033 | - | - |
| Pennsylvania4 | 5 | 10 | Midday:A05:STR8_3:009(3); Midday:A02:STR8_3:001(3); Midday:A02:STR8_3:009(3) | 37 | 188 | 10:007 | 007 066 228 255 | 2:007 009 | - | - |
| NewJersey4 | 4 | 11 | Combined:A10:STR8_3:556(3); Evening:A05:STR8_3:778(3); Midday:A12:STR8_4of8:089(4) | 36 | 177 | 11:022 | 022 114 155 339 | 2:022 778 | - | - |
| Florida4 | 3 | 10 | Combined:A05:STR8_3:334(3); Combined:A12:STR8_4of8:334(4); Midday:A04:BOX:346(6) | 35 | 156 | 9:003 | 003 009 011 077 | 2:003 334 | - | - |
| Michigan4 | 3 | 10 | Midday:A05:STR8_3:344(3); Combined:A12:STR8_4of8:004(4); Evening:A04:BOX:019(6) | 35 | 168 | 10:112 | 112 119 155 199 | 2:112 344 | - | - |
| OntarioCanada4 | 3 | 10 | Midday:A05:STR8_3:224(3); Combined:A12:STR8_4of8:006(4); Evening:A04:BOX:015(6) | 35 | 182 | 9:004 | 004 044 144 228 | 2:004 224 | - | - |
| Indiana4 | 3 | 10 | Evening:A05:STR8_3:344(3); Combined:A10:STR8_3:002(3); Midday:A04:BOX:069(6) | 35 | 216 | 10:002 | 002 022 177 226 | 2:002 344 | - | - |
| Ohio4 | 2 | 8 | Evening:A05:STR8_3:889(3); Combined:A04:BOX:359(6) | 34 | 179 | 9:009 | 009 066 113 118 | 2:009 889 | - | - |
| Connecticut4 | 2 | 7 | Combined:A05:STR8_3:224(3); Evening:A04:BOX:248(6) | 34 | 162 | 9:088 | 088 099 223 228 | 2:088 224 | - | - |
| SouthCarolina4 | 2 | 7 | Midday:A05:STR8_3:244(3); Combined:A04:BOX:369(6) | 34 | 172 | 9:115 | 115 155 224 233 | 2:115 244 | - | - |
| NorthCarolina4 | 2 | 7 | Evening:A05:STR8_3:244(3); Evening:A04:BOX:016(6) | 34 | 175 | 9:001 | 001 009 044 225 | 2:001 244 | - | - |
| PuertoRico4 | 1 | 3 | Evening:A04:BOX:068(6) | 33 | 205 | 16:022 | 022 033 199 299 | 2:022 068 | - | - |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

v0.2 posture (budget-split):
- B12 uses `analysis_prefix` (conservative / diagnostic-first).
- B24/B36 use `vtrac_pack_boxed_first` (conversion-friendly; boxed-member VTRAC pack + filler).

### B12 (analysis_prefix)
- **NewYork4**: `001 010 100 507 500 005 057 075 570 705 750 006`
- **Virginia4**: `004 040 400 024 559 042 240 420 554 029 204 402`
- **Delaware4**: `011 009 090 900 033 034 016 061 303 330 043 340`
- **Pennsylvania4**: `070 007 700 599 009 090 900 019 091 109 190 544`
- **NewJersey4**: `022 220 202 089 778 787 877 138 183 098 809 890`
- **Florida4**: `343 334 384 433 003 030 300 436 346 364 634 335`
- **Michigan4**: `112 121 211 054 344 434 443 004 019 091 109 190`
- **OntarioCanada4**: `224 242 422 004 040 400 501 015 440 270 274 924`
- **Indiana4**: `002 020 200 344 434 443 609 906 237 267 273 276`
- **Ohio4**: `889 898 988 009 090 900 559 459 489 495 498 549`
- **Connecticut4**: `224 088 808 880 824 448 248 242 422 284 424 484`
- **SouthCarolina4**: `115 151 511 244 424 442 059 599 936 963 224 242`
- **NorthCarolina4**: `244 424 442 001 010 100 924 940 049 094 249 294`
- **PuertoRico4**: `220 022 202 068 086 680 608 806 860 077 207 027`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (usually 8 combos; fewer for doubles/triples) and which play_card file it came from.


## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-08/<STATE>/candidate_universe.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-08/<STATE>/play_card*.json` (budgeted cuts)
