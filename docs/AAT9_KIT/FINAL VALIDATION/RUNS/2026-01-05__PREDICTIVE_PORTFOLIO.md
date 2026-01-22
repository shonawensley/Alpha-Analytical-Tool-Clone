# Predictive Portfolio — D=2026-01-05

Purpose
- Cross-state triage for a predictive day (pre-results).
- Profile: `mixed` | rank_by: `profit_alerts`
- Annotates state snapshots with Candidate Universe size + Due Doubles + Play Card closures.

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center Profit Alerts: `sharepacks/_predictive/2026-01-05/control_center/profit_alerts.csv`
- Candidate Universe file: `candidate_universe.json`
- Play Card file(s): `play_card*.json`

## Portfolio table (ranked)

| State | Alerts | Strength(top) | Top alerts (variant:id:mode:canon(cost)) | CU packs | CU union | CU top support | Due doubles (canonicals) | PlayCard B12 boxed (analysis_prefix) | B24 VTRAC pack (idx/size) | B36 VTRAC pack (idx/size) |
|---|---:|---:|---|---:|---:|---|---|---|---|---|
| NewJersey4 | 5 | 13 | Combined:A11:BOX:028(6); Combined:A05:STR8_3:008(3); Combined:A01:BOX:028(6) | 37 | 172 | 9:022 | 022 114 155 339 | 2:008 022 | - | - |
| SouthCarolina4 | 5 | 12 | Combined:A11:BOX:259(6); Midday:A05:STR8_3:007(3); Combined:A10:STR8_3:115(3) | 37 | 185 | 10:115 | 115 155 224 233 | 2:057 115 | - | - |
| Virginia4 | 4 | 13 | Combined:A11:BOX:089(6); Combined:A05:STR8_3:008(3); Combined:A01:BOX:089(6) | 36 | 174 | 11:004 | 004 177 199 377 | 2:004 008 | - | - |
| PuertoRico4 | 4 | 12 | Midday:A05:STR8_3:003(3); Midday:A01:BOX:036(6); Midday:A01:BOX:036(6) | 36 | 210 | 13:022 | 022 033 088 199 | 3:003 022 026 | - | - |
| NorthCarolina4 | 4 | 10 | Evening:A05:STR8_3:044(3); Evening:A02:STR8_3:044(3); Evening:A02:STR8_3:044(3) | 36 | 191 | 9:001 | 001 009 044 225 | 2:001 044 | - | - |
| Pennsylvania4 | 3 | 11 | Combined:A05:STR8_3:055(3); Combined:A09:STR8_8:034(8); Midday:A04:BOX:059(6) | 35 | 159 | 11:007 | 007 066 228 255 | 2:007 059 | - | - |
| NewYork4 | 3 | 11 | Midday:A05:STR8_3:066(3); Midday:A09:STR8_8:234(8); Midday:A04:BOX:056(6) | 35 | 166 | 11:001 | 001 007 011 066 | 2:001 066 | - | - |
| OntarioCanada4 | 3 | 11 | Combined:A10:STR8_3:255(3); Midday:A05:STR8_3:244(3); Evening:A04:BOX:459(6) | 35 | 170 | 11:004 | 004 044 144 244 | 2:004 244 | - | - |
| Connecticut4 | 3 | 11 | Evening:A05:STR8_8:024(8); Evening:A09:STR8_8:113(8); Evening:A04:BOX:024(6) | 35 | 214 | 9:088 | 088 099 223 228 | 2:024 088 | - | - |
| Michigan4 | 3 | 10 | Combined:A05:STR8_3:011(3); Combined:A10:STR8_3:566(3); Combined:A04:BOX:168(6) | 35 | 138 | 9:112 168 | 112 119 155 199 | 2:112 168 | - | - |
| Florida4 | 3 | 10 | Combined:A05:STR8_3:033(3); Combined:A12:STR8_4of8:334(4); Evening:A04:BOX:467(6) | 35 | 164 | 9:003 | 003 008 009 011 | 2:003 033 | - | - |
| Ohio4 | 3 | 10 | Midday:A05:STR8_3:599(3); Combined:A12:STR8_4of8:088(4); Combined:A04:BOX:259(6) | 35 | 165 | 11:009 | 009 066 113 118 | 2:009 599 | - | - |
| Indiana4 | 3 | 10 | Evening:A05:STR8_3:244(3); Midday:A12:STR8_4of8:066(4); Midday:A04:BOX:368(6) | 35 | 181 | 9:002 | 002 022 177 226 | 2:002 244 | - | - |
| Delaware4 | 2 | 7 | Evening:A05:STR8_3:449(3); Combined:A04:BOX:058(6) | 34 | 179 | 11:009 | 009 088 223 228 | 3:004 009 449 | - | - |

## Play cards (defaults)

These are the budgeted “what to play now” cuts derived from Candidate Universe (pre-results).

v0.2 posture (budget-split):
- B12 uses `analysis_prefix` (conservative / diagnostic-first).
- B24/B36 use `vtrac_pack_boxed_first` (conversion-friendly; boxed-member VTRAC pack + filler).

### B12 (analysis_prefix)
- **NewJersey4**: `839 022 202 220 889 008 080 800 982 884 028 829`
- **SouthCarolina4**: `115 151 511 224 627 672 057 075 507 570 705 750`
- **Virginia4**: `040 004 400 561 377 008 080 800 559 593 455 545`
- **PuertoRico4**: `220 022 202 206 003 026 062 602 030 300 260 620`
- **NorthCarolina4**: `044 404 440 001 010 100 294 249 492 942 522 429`
- **Pennsylvania4**: `590 059 095 070 509 905 950 007 700 015 055 505`
- **NewYork4**: `001 010 100 066 660 606 506 520 805 250 056 065`
- **OntarioCanada4**: `244 040 424 442 004 400 594 459 495 954 194 549`
- **Connecticut4**: `088 808 880 724 024 042 204 240 402 420 113 118`
- **Michigan4**: `168 186 681 618 861 816 160 112 121 211 011 016`
- **Florida4**: `384 003 030 300 033 303 330 334 434 443 008 080`
- **Ohio4**: `090 009 900 599 088 059 559 959 995 038 592 033`
- **Indiana4**: `066 244 002 020 200 016 061 386 683 836 424 442`
- **Delaware4**: `090 009 900 040 449 494 944 004 400 594 058 085`

### B24/B36 VTRAC pack picks

Shows the inserted boxed-member VTRAC pack (usually 8 combos; fewer for doubles/triples) and which play_card file it came from.


## Notes

- This is not a hit-rate claim; it is a *triage surface* to decide where to spend attention/budget.
- For any state, the canonical evidence remains the frozen predictive sharepack artifacts:
  - `sharepacks/_predictive/2026-01-05/control_center/profit_alerts.csv` (bet-ready implied sets; included only for mixed/profit_only)
  - `sharepacks/_predictive/2026-01-05/<STATE>/candidate_universe.json` (gradeable playset)
  - `sharepacks/_predictive/2026-01-05/<STATE>/play_card*.json` (budgeted cuts)
