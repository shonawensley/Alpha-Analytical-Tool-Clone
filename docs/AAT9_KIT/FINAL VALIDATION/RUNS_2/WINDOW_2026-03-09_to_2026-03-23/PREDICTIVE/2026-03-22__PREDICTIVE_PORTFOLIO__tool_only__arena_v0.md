# Analysis Arena Predictive Portfolio — D=2026-03-22

Purpose
- Cross-state pre-results triage for the Analysis Arena branch.
- Brain 1 / Brain 2 posture is surfaced first; Candidate Universe / Play Card remain the downstream control arm.
- Profile: `tool_only` | experiment tag: `arena_v0` | rank_by: `tool_first`

SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Arena cadence quickstart: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md`
- Aggregated arena contract: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md`
- Translation sandbox companion: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

Evidence roots
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center profit alerts: `sharepacks/_predictive/2026-03-22/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Delaware4 | - | 001 599 00116 | 001 038 039 | - | 4 | 187 | 3:001 009 559 | 2(6) | idx[20]:1,2,3,4…(36) |
| OntarioCanada4 | - | 559 055 599 | 579 399 355 | - | 2 | 206 | 2:004 244 | 5(6) | idx[20]:1,2,3,4…(36) |
| NewJersey4 | - | 445 344 455 | 445 455 005 | - | 5 | 144 | 2:022 449 | 5(6) | idx[22]:1,2,3,4…(36) |
| NewYork4 | - | 066 668 667 | 066 668 667 | - | 10 | 175 | 1:007 | 6(6) | idx[20]:3,4,5,6…(36) |
| Connecticut4 | - | 113 224 003 | 113 355 123 | - | 6 | 197 | 2:099 116 | 18(6) | idx[20]:3,4,5,6…(36) |
| Michigan4 | - | 445 344 244 | 445 455 009 | - | 4 | 198 | 3:011 066 144 | 3(6) | idx[20]:1,2,3,4…(36) |
| Virginia4 | - | 225 559 003 | 003 255 259 | - | 4 | 201 | 3:004 022 225 | 3(6) | idx[20]:1,3,5,6…(36) |
| Pennsylvania4 | - | 448 449 468 | 448 449 468 | - | 6 | 202 | 3:007 088 488 | 12(8) | idx[20]:3,4,5,7…(36) |
| Indiana4 | - | 559 002 259 | 559 259 025 | - | 5 | 207 | 3:177 249 337 | 3(6) | idx[20]:1,2,3,5…(36) |
| SouthCarolina4 | - | 559 155 455 | 155 055 577 | - | 3 | 215 | 4:114 155 455 | 5(6) | idx[20]:2,3,4,5…(36) |
| Ohio4 | - | 002 168 669 | 002 168 224 | - | 6 | 220 | 3:009 118 559 | 8(8) | idx[20]:2,3,5,6…(36) |
| PuertoRico4 | - | 338 224 244 | 338 007 368 | - | 3 | 220 | 4:001 006 033 | 2(6) | idx[20]:1,2,3,4…(36) |
| Florida4 | - | 118 024 224 | 024 224 026 | - | 2 | 231 | 3:003 118 224 | 7(8) | idx[20]:2,3,4,5…(36) |
| NorthCarolina4 | - | 499 599 088 | 499 088 299 | - | 10 | 240 | 3:009 249 299 | 31(6) | idx[20]:1,5,10,13…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Delaware4**: CU packs=`27` union=`187` top_support=`11:009` due=`009 033 088 117`
- **OntarioCanada4**: CU packs=`27` union=`206` top_support=`11:004` due=`004 044 228 244`
- **NewJersey4**: CU packs=`27` union=`144` top_support=`9:022` due=`022 155 335 339`
- **NewYork4**: CU packs=`27` union=`175` top_support=`9:007` due=`007 011 066 115`
- **Connecticut4**: CU packs=`27` union=`197` top_support=`9:099` due=`099 116 228 668`
- **Michigan4**: CU packs=`27` union=`198` top_support=`9:066` due=`066 077 119 144`
- **Virginia4**: CU packs=`27` union=`201` top_support=`9:004` due=`004 005 115 199`
- **Pennsylvania4**: CU packs=`27` union=`202` top_support=`9:007` due=`007 009 088 228`
- **Indiana4**: CU packs=`27` union=`207` top_support=`9:177` due=`177 226 288 337`
- **SouthCarolina4**: CU packs=`27` union=`215` top_support=`9:114` due=`114 115 155 233`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Delaware4**: B24 `2(6)` (src `sharepacks/_predictive/2026-03-22/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-22/Delaware4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-22/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-22/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-22/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-22/NewJersey4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive/2026-03-22/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-22/NewYork4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `18(6)` (src `sharepacks/_predictive/2026-03-22/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-22/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `3(6)` (src `sharepacks/_predictive/2026-03-22/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-22/Michigan4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `3(6)` (src `sharepacks/_predictive/2026-03-22/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-22/Virginia4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `12(8)` (src `sharepacks/_predictive/2026-03-22/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,7…(36)` (src `sharepacks/_predictive/2026-03-22/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `3(6)` (src `sharepacks/_predictive/2026-03-22/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-03-22/Indiana4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-22/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-22/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `8(8)` (src `sharepacks/_predictive/2026-03-22/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-22/Ohio4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `2(6)` (src `sharepacks/_predictive/2026-03-22/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-22/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `7(8)` (src `sharepacks/_predictive/2026-03-22/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-22/Florida4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `31(6)` (src `sharepacks/_predictive/2026-03-22/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,5,10,13…(36)` (src `sharepacks/_predictive/2026-03-22/NorthCarolina4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
