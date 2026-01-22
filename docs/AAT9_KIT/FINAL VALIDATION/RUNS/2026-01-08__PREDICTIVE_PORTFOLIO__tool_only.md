# Predictive Portfolio — D=2026-01-08

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| PuertoRico4 | 30 | 191 | 15:022 | 022 033 199 299 | 1:022 | 10(6) | 10(6) |
| NewYork4 | 30 | 153 | 13:001 | 001 007 011 066 | 3:001 011 066 | 2(6) | 2(6) |
| NewJersey4 | 30 | 164 | 11:022 | 022 114 155 339 | 1:022 | 10(6) | 10(6) |
| Delaware4 | 30 | 182 | 11:009 | 009 088 223 228 | 3:004 009 011 | 5(6) | 5(6) |
| Michigan4 | 30 | 159 | 10:112 | 112 119 155 199 | 3:112 119 155 | 22(8) | 22(8) |
| Pennsylvania4 | 30 | 177 | 10:007 | 007 066 228 255 | 4:002 007 112 | 3(6) | 3(6) |
| Florida4 | 30 | 143 | 9:003 | 003 009 011 077 | 3:003 033 338 | 13(6) | 13(6) |
| Connecticut4 | 30 | 156 | 9:088 | 088 099 223 228 | 3:088 244 448 | 34(6) | 34(6) |
| SouthCarolina4 | 30 | 168 | 9:115 | 115 155 224 233 | 3:115 224 599 | 6(6) | 6(6) |
| Ohio4 | 30 | 173 | 9:009 | 009 066 113 118 | 3:009 559 889 | 33(6) | 33(6) |
| NorthCarolina4 | 30 | 180 | 9:001 | 001 009 044 225 | 3:001 006 044 | 25(6) | 25(6) |
| OntarioCanada4 | 30 | 189 | 9:004 | 004 044 144 228 | 3:004 044 224 | 5(6) | 5(6) |
| Virginia4 | 30 | 194 | 9:004 | 004 177 199 377 | 1:004 | 5(6) | 5(6) |
| Indiana4 | 30 | 205 | 9:002 | 002 022 177 226 | 2:002 066 | 20(6) | 20(6) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

v0.2 posture (budget-split):
- B12 uses `analysis_prefix` (conservative / diagnostic-first).
- B24/B36 use `vtrac_pack_boxed_first` (conversion-friendly; boxed-member VTRAC pack + filler).

### B12 (analysis_prefix)
- **PuertoRico4**: `220 022 202 077 207 027 072 280 522 770 270 720`
- **NewYork4**: `010 001 100 060 005 011 101 110 066 606 660 006`
- **NewJersey4**: `022 220 202 077 186 089 138 183 126 522 770 114`
- **Delaware4**: `090 009 900 011 040 004 400 595 101 110 811 559`
- **Michigan4**: `112 121 211 119 191 911 155 051 141 199 515 551`
- **Pennsylvania4**: `070 007 700 112 121 211 020 255 525 552 002 200`
- **Florida4**: `003 030 300 338 383 833 335 033 303 330 316 343`
- **Connecticut4**: `088 808 880 424 484 448 894 984 244 442 844 494`
- **SouthCarolina4**: `115 151 511 224 242 422 665 599 959 995 059 155`
- **Ohio4**: `009 090 900 889 559 595 955 898 988 893 929 938`
- **NorthCarolina4**: `001 010 100 244 044 404 440 940 964 006 060 600`
- **OntarioCanada4**: `004 040 400 224 044 404 440 242 422 270 274 279`
- **Virginia4**: `004 040 400 349 361 341 042 146 169 394 439 493`
- **Indiana4**: `002 020 200 066 606 660 766 054 247 274 427 472`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (usually 8 combos; fewer for doubles/triples) and which play_card file it came from.

- **PuertoRico4**: `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-08/PuertoRico4/play_card__tool_only__vtracpack_v1.json`)
- **NewYork4**: `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-08/NewYork4/play_card__tool_only__vtracpack_v1.json`)
- **NewJersey4**: `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-08/NewJersey4/play_card__tool_only__vtracpack_v1.json`)
- **Delaware4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-08/Delaware4/play_card__tool_only__vtracpack_v1.json`)
- **Michigan4**: `idx(size)=22(8)` pack=`124 129 147 179 246 269 467 679` (src: `sharepacks/_predictive/2026-01-08/Michigan4/play_card__tool_only__vtracpack_v1.json`)
- **Pennsylvania4**: `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-08/Pennsylvania4/play_card__tool_only__vtracpack_v1.json`)
- **Florida4**: `idx(size)=13(6)` pack=`038 358 033 088 335 588` (src: `sharepacks/_predictive/2026-01-08/Florida4/play_card__tool_only__vtracpack_v1.json`)
- **Connecticut4**: `idx(size)=34(6)` pack=`349 489 344 399 448 899` (src: `sharepacks/_predictive/2026-01-08/Connecticut4/play_card__tool_only__vtracpack_v1.json`)
- **SouthCarolina4**: `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-08/SouthCarolina4/play_card__tool_only__vtracpack_v1.json`)
- **Ohio4**: `idx(size)=33(6)` pack=`348 389 334 339 488 889` (src: `sharepacks/_predictive/2026-01-08/Ohio4/play_card__tool_only__vtracpack_v1.json`)
- **NorthCarolina4**: `idx(size)=25(6)` pack=`149 469 144 199 446 699` (src: `sharepacks/_predictive/2026-01-08/NorthCarolina4/play_card__tool_only__vtracpack_v1.json`)
- **OntarioCanada4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-08/OntarioCanada4/play_card__tool_only__vtracpack_v1.json`)
- **Virginia4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-08/Virginia4/play_card__tool_only__vtracpack_v1.json`)
- **Indiana4**: `idx(size)=20(6)` pack=`127 267 122 177 226 677` (src: `sharepacks/_predictive/2026-01-08/Indiana4/play_card__tool_only__vtracpack_v1.json`)

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-08/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-08/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-08/<STATE>/play_card__tool_only*.json` (budgeted cuts)
