# Predictive Portfolio — D=2026-01-07

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `tool_only` | rank_by: `tool_first`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts (excluded by profile): `sharepacks/_predictive/2026-01-07/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe__tool_only.json`
- Play Card file(s): `play_card__tool_only*.json`

## Portfolio table (ranked)

| State | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---|---|---|---|
| PuertoRico4 | 30 | 199 | 14:022 | 022 033 199 299 | 1:022 | 10(6) | 10(6) |
| OntarioCanada4 | 30 | 173 | 12:004 | 004 044 144 228 | 3:004 044 224 | 5(6) | 5(6) |
| NewYork4 | 30 | 149 | 11:001 | 001 007 011 066 | 3:001 011 066 | 2(6) | 2(6) |
| Delaware4 | 30 | 170 | 11:009 | 009 088 223 228 | 3:004 009 011 | 5(6) | 5(6) |
| Michigan4 | 30 | 153 | 10:112 | 112 119 155 199 | 2:112 119 | 19(6) | 19(6) |
| Pennsylvania4 | 30 | 189 | 10:007 | 007 066 228 255 | 3:002 007 255 | 3(6) | 3(6) |
| Florida4 | 30 | 152 | 9:003 | 003 009 011 077 | 3:003 033 233 | 33(6) | 33(6) |
| NewJersey4 | 30 | 159 | 9:022 | 022 114 155 339 | 4:022 077 088 | 10(6) | 10(6) |
| Connecticut4 | 30 | 164 | 9:088 | 088 099 223 228 | 3:088 244 448 | 31(6) | 31(6) |
| Ohio4 | 30 | 173 | 9:009 | 009 066 113 118 | 4:009 088 559 | 5(6) | 5(6) |
| NorthCarolina4 | 30 | 183 | 9:001 | 001 009 044 225 | 2:001 044 | 31(6) | 31(6) |
| Virginia4 | 30 | 184 | 9:004 | 004 177 199 377 | 2:004 009 | 12(8) | 12(8) |
| SouthCarolina4 | 30 | 187 | 9:115 | 115 155 224 233 | 3:115 224 599 | 6(6) | 6(6) |
| Indiana4 | 30 | 202 | 9:002 | 002 022 177 226 | 2:002 066 | 20(6) | 20(6) |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

v0.2 posture (budget-split):
- B12 uses `analysis_prefix` (conservative / diagnostic-first).
- B24/B36 use `vtrac_pack_boxed_first` (conversion-friendly; boxed-member VTRAC pack + filler).

### B12 (analysis_prefix)
- **PuertoRico4**: `022 220 202 077 027 072 522 770 270 720 216 806`
- **OntarioCanada4**: `040 004 400 224 044 404 440 095 590 242 422 270`
- **NewYork4**: `001 010 100 011 066 110 660 008 506 508 101 606`
- **Delaware4**: `090 009 900 040 004 400 011 595 101 110 511 811`
- **Michigan4**: `112 121 211 191 119 911 155 141 101 156 479 186`
- **Pennsylvania4**: `070 007 700 020 015 016 035 255 525 552 002 200`
- **Florida4**: `003 030 300 436 033 233 303 323 330 332 337 433`
- **NewJersey4**: `022 202 220 077 707 770 088 808 880 788 878 887`
- **Connecticut4**: `088 808 880 424 844 228 244 442 448 484 894 024`
- **Ohio4**: `009 090 900 889 559 595 955 088 808 880 898 988`
- **NorthCarolina4**: `001 010 100 600 244 044 404 440 940 900 964 006`
- **Virginia4**: `004 040 400 349 009 090 900 361 099 042 198 394`
- **SouthCarolina4**: `115 151 511 224 242 422 665 599 959 995 155 233`
- **Indiana4**: `002 020 200 762 066 606 660 766 636 027 072 267`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (usually 8 combos; fewer for doubles/triples) and which play_card file it came from.

- **PuertoRico4**: `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-07/PuertoRico4/play_card__tool_only__vtracpack_v1.json`)
- **OntarioCanada4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-07/OntarioCanada4/play_card__tool_only__vtracpack_v1.json`)
- **NewYork4**: `idx(size)=2(6)` pack=`015 056 001 006 155 556` (src: `sharepacks/_predictive/2026-01-07/NewYork4/play_card__tool_only__vtracpack_v1.json`)
- **Delaware4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-07/Delaware4/play_card__tool_only__vtracpack_v1.json`)
- **Michigan4**: `idx(size)=19(6)` pack=`146 169 114 119 466 669` (src: `sharepacks/_predictive/2026-01-07/Michigan4/play_card__tool_only__vtracpack_v1.json`)
- **Pennsylvania4**: `idx(size)=3(6)` pack=`025 057 002 007 255 557` (src: `sharepacks/_predictive/2026-01-07/Pennsylvania4/play_card__tool_only__vtracpack_v1.json`)
- **Florida4**: `idx(size)=33(6)` pack=`348 389 334 339 488 889` (src: `sharepacks/_predictive/2026-01-07/Florida4/play_card__tool_only__vtracpack_v1.json`)
- **NewJersey4**: `idx(size)=10(6)` pack=`027 257 022 077 225 577` (src: `sharepacks/_predictive/2026-01-07/NewJersey4/play_card__tool_only__vtracpack_v1.json`)
- **Connecticut4**: `idx(size)=31(6)` pack=`249 479 244 299 447 799` (src: `sharepacks/_predictive/2026-01-07/Connecticut4/play_card__tool_only__vtracpack_v1.json`)
- **Ohio4**: `idx(size)=5(6)` pack=`045 059 004 009 455 559` (src: `sharepacks/_predictive/2026-01-07/Ohio4/play_card__tool_only__vtracpack_v1.json`)
- **NorthCarolina4**: `idx(size)=31(6)` pack=`249 479 244 299 447 799` (src: `sharepacks/_predictive/2026-01-07/NorthCarolina4/play_card__tool_only__vtracpack_v1.json`)
- **Virginia4**: `idx(size)=12(8)` pack=`024 029 047 079 245 259 457 579` (src: `sharepacks/_predictive/2026-01-07/Virginia4/play_card__tool_only__vtracpack_v1.json`)
- **SouthCarolina4**: `idx(size)=6(6)` pack=`016 156 011 066 115 566` (src: `sharepacks/_predictive/2026-01-07/SouthCarolina4/play_card__tool_only__vtracpack_v1.json`)
- **Indiana4**: `idx(size)=20(6)` pack=`127 267 122 177 226 677` (src: `sharepacks/_predictive/2026-01-07/Indiana4/play_card__tool_only__vtracpack_v1.json`)

## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-07/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-07/<STATE>/candidate_universe__tool_only.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-07/<STATE>/play_card__tool_only*.json` (budgeted cuts)
