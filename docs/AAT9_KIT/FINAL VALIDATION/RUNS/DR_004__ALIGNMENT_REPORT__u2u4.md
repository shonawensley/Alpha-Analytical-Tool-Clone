# DR-004 — 10-Case Alignment Report

Purpose: validate (case-first) whether DR-004 signals surface the winner as:

- a top digit pool (envelope),
- a top canonical,
- and/or a top VTRAC index gateway.

## Config

- recent_draws: `2`
- unique_digits: `2` → `4`
- top_pools: `12`
- top_canonicals: `25`
- top_indices: `12`
- predictive root (preferred): `sharepacks/_predictive`
- evidence root (winners/overlays): `sharepacks`

## Summary (winner presence in DR-004 signals)

| # | Date | State | Outcome | Winner | Type | Canon | VTRAC idx | pool_contains | canonical_top | index_top |
|---:|---|---|---|---:|---|---:|---:|---|---|---|
| 1 | 2026-01-09 | OntarioCanada4 | Evening | 104 | unique | 014 | 9 | YES (#3) | YES (#12) | YES (#6) |
| 2 | 2026-01-08 | Florida4 | Midday | 429 | unique | 249 | 31 | — | — | — |
| 3 | 2026-01-07 | Michigan4 | Evening | 616 | double | 166 | 16 | YES (#1) | YES (#6) | YES (#3) |
| 4 | 2026-01-02 | NorthCarolina4 | Midday | 033 | double | 033 | 13 | YES (#1) | YES (#14) | YES (#12) |
| 5 | 2025-12-31 | Delaware4 | Evening | 337 | double | 337 | 29 | YES (#3) | YES (#25) | — |
| 6 | 2025-06-21 | Pennsylvania4 | Midday | 667 | double | 667 | 17 | YES (#4) | — | YES (#6) |
| 7 | 2026-01-07 | Delaware4 | Evening | 922 | double | 229 | 28 | — | — | — |
| 8 | 2025-06-23 | Indiana4 | Midday | 110 | double | 011 | 6 | YES (#9) | — | — |
| 9 | 2025-12-31 | Virginia4 | Midday | 686 | double | 668 | 18 | — | — | YES (#2) |
| 10 | 2025-06-21 | OntarioCanada4 | Midday | 678 | unique | 678 | 21 | — | YES (#16) | YES (#10) |

## Case Details

### 1) 2026-01-09 OntarioCanada4 Evening — winner 104

- Evidence dir: `sharepacks/2026-01-09/OntarioCanada4`
- Signals input dir: `sharepacks/_predictive/2026-01-09/OntarioCanada4`
- Winners HTML: `sharepacks/2026-01-09/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac9_winner_104_20260110_035057.html`
- DR overlay: `sharepacks/2026-01-09/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/winners/20260110_Evening_winner_overlay.html`
- Winner canonical/index: `014` / `9` (type=unique; pool=`014`)
- pool_contains: YES (#3); canonical_top: YES (#12); index_top: YES (#6)
- Top pools (first 6): `015, 05, 0145, 0157, 15, 0156`
- Top canonicals (first 6): `015, 057, 005, 055, 157, 115`
### 2) 2026-01-08 Florida4 Midday — winner 429

- Evidence dir: `sharepacks/2026-01-08/Florida4`
- Signals input dir: `sharepacks/_predictive/2026-01-08/Florida4`
- Winners HTML: `sharepacks/2026-01-08/Florida4/winners/Florida4/Florida4_vtrac31_winner_429_20260110_034419.html`
- DR overlay: `sharepacks/2026-01-08/Florida4/digit_reduction/Florida4/analyzer_v2/winners/20260110_Midday_winner_overlay.html`
- Winner canonical/index: `249` / `31` (type=unique; pool=`249`)
- pool_contains: —; canonical_top: —; index_top: —
- Top pools (first 6): `34, 349, 38, 3456, 3469, 348`
- Top canonicals (first 6): `349, 348, 334, 344, 346, 134`
### 3) 2026-01-07 Michigan4 Evening — winner 616

- Evidence dir: `sharepacks/2026-01-07/Michigan4`
- Signals input dir: `sharepacks/_predictive/2026-01-07/Michigan4`
- Winners HTML: `sharepacks/2026-01-07/Michigan4/winners/Michigan4/Michigan4_vtrac16_winner_616_20260110_033422.html`
- DR overlay: `sharepacks/2026-01-07/Michigan4/digit_reduction/Michigan4/analyzer_v2/winners/20260110_Evening_winner_overlay.html`
- Winner canonical/index: `166` / `16` (type=double; pool=`16`)
- pool_contains: YES (#1); canonical_top: YES (#6); index_top: YES (#3)
- Top pools (first 6): `169, 1356, 16, 09, 0169, 016`
- Top canonicals (first 6): `169, 156, 016, 136, 116, 166`
### 4) 2026-01-02 NorthCarolina4 Midday — winner 033

- Evidence dir: `sharepacks/2026-01-02/NorthCarolina4`
- Signals input dir: `sharepacks/2026-01-02/NorthCarolina4`
- Winners HTML: `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac13_winner_033_20260105_070916.html`
- DR overlay: `sharepacks/2026-01-02/NorthCarolina4/digit_reduction/NorthCarolina4/analyzer_v2/winners/20260102_Midday_winner_overlay.html`
- Winner canonical/index: `033` / `13` (type=double; pool=`03`)
- pool_contains: YES (#1); canonical_top: YES (#14); index_top: YES (#12)
- Top pools (first 6): `0239, 023, 29, 028, 289, 05`
- Top canonicals (first 6): `023, 029, 239, 039, 229, 299`
### 5) 2025-12-31 Delaware4 Evening — winner 337

- Evidence dir: `sharepacks/2025-12-31/Delaware4`
- Signals input dir: `sharepacks/2025-12-31/Delaware4`
- Winners HTML: `sharepacks/2025-12-31/Delaware4/winners/Delaware4/Delaware4_vtrac29_winner_337_20260105_052144.html`
- DR overlay: `sharepacks/2025-12-31/Delaware4/digit_reduction/Delaware4/analyzer_v2/winners/20260105_Evening_winner_overlay.html`
- Winner canonical/index: `337` / `29` (type=double; pool=`37`)
- pool_contains: YES (#3); canonical_top: YES (#25); index_top: —
- Top pools (first 6): `479, 49, 137, 1479, 1347, 17`
- Top canonicals (first 6): `479, 137, 147, 449, 499, 149`
### 6) 2025-06-21 Pennsylvania4 Midday — winner 667

- Evidence dir: `sharepacks/2025-06-21/Pennsylvania4`
- Signals input dir: `sharepacks/2025-06-21/Pennsylvania4`
- Winners HTML: `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251201_233404.html`
- DR overlay: `sharepacks/2025-06-21/Pennsylvania4/digit_reduction/Pennsylvania4/analyzer_v2/winners/20251219_Midday_winner_overlay.html`
- Winner canonical/index: `667` / `17` (type=double; pool=`67`)
- pool_contains: YES (#4); canonical_top: —; index_top: YES (#6)
- Top pools (first 6): `27, 028, 28, 267, 0278, 278`
- Top canonicals (first 6): `028, 278, 267, 127, 227, 277`
### 7) 2026-01-07 Delaware4 Evening — winner 922

- Evidence dir: `sharepacks/2026-01-07/Delaware4`
- Signals input dir: `sharepacks/_predictive/2026-01-07/Delaware4`
- Winners HTML: `sharepacks/2026-01-07/Delaware4/winners/Delaware4/Delaware4_vtrac28_winner_922_20260110_033414.html`
- DR overlay: `sharepacks/2026-01-07/Delaware4/digit_reduction/Delaware4/analyzer_v2/winners/20260110_Evening_winner_overlay.html`
- Winner canonical/index: `229` / `28` (type=double; pool=`29`)
- pool_contains: —; canonical_top: —; index_top: —
- Top pools (first 6): `14, 49, 149, 0134, 04, 014`
- Top canonicals (first 6): `149, 014, 114, 144, 034, 449`
### 8) 2025-06-23 Indiana4 Midday — winner 110

- Evidence dir: `sharepacks/2025-06-23/Indiana4`
- Signals input dir: `sharepacks/2025-06-23/Indiana4`
- Winners HTML: `sharepacks/2025-06-23/Indiana4/winners/Indiana4/Indiana4_vtrac6_winner_110_20251223_052048.html`
- DR overlay: `sharepacks/2025-06-23/Indiana4/digit_reduction/Indiana4/analyzer_v2/winners/20251223_Midday_winner_overlay.html`
- Winner canonical/index: `011` / `6` (type=double; pool=`01`)
- pool_contains: YES (#9); canonical_top: —; index_top: —
- Top pools (first 6): `358, 38, 458, 08, 58, 3458`
- Top canonicals (first 6): `358, 458, 148, 338, 388, 558`
### 9) 2025-12-31 Virginia4 Midday — winner 686

- Evidence dir: `sharepacks/2025-12-31/Virginia4`
- Signals input dir: `sharepacks/2025-12-31/Virginia4`
- Winners HTML: `sharepacks/2025-12-31/Virginia4/winners/Virginia4/Virginia4_vtrac18_winner_686_20260105_052215.html`
- DR overlay: `sharepacks/2025-12-31/Virginia4/digit_reduction/Virginia4/analyzer_v2/winners/20260105_Midday_winner_overlay.html`
- Winner canonical/index: `668` / `18` (type=double; pool=`68`)
- pool_contains: —; canonical_top: —; index_top: YES (#2)
- Top pools (first 6): `1367, 167, 136, 16, 1356, 67`
- Top canonicals (first 6): `136, 167, 156, 116, 166, 146`
### 10) 2025-06-21 OntarioCanada4 Midday — winner 678

- Evidence dir: `sharepacks/2025-06-21/OntarioCanada4`
- Signals input dir: `sharepacks/2025-06-21/OntarioCanada4`
- Winners HTML: `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac21_winner_678_20251201_233402.html`
- DR overlay: `sharepacks/2025-06-21/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/winners/20251219_Midday_winner_overlay.html`
- Winner canonical/index: `678` / `21` (type=unique; pool=`678`)
- pool_contains: —; canonical_top: YES (#16); index_top: YES (#10)
- Top pools (first 6): `267, 59, 067, 459, 3459, 2567`
- Top canonicals (first 6): `267, 459, 067, 667, 677, 038`
