# Analysis Arena Predictive Portfolio — D=2026-03-19

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
- Control Center profit alerts: `sharepacks/_predictive/2026-03-19/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Delaware4 | - | 099 001 069 | 099 069 019 | - | 4 | 181 | 3:009 099 559 | 34(6) | idx[20]:2,3,5,6…(36) |
| Pennsylvania4 | - | 477 067 244 | 477 033 034 | - | 4 | 187 | 3:007 077 477 | 3(6) | idx[20]:2,3,4,5…(36) |
| Ohio4 | - | 559 006 099 | 006 099 004 | - | 7 | 204 | 3:004 009 559 | 9(8) | idx[20]:2,4,5,6…(36) |
| PuertoRico4 | - | 244 006 144 | 244 006 029 | - | 4 | 233 | 3:001 003 006 | 7(8) | idx[20]:2,3,4,5…(36) |
| Virginia4 | - | 225 255 268 | 225 268 055 | - | 2 | 177 | 3:004 055 255 | 3(6) | idx[22]:1,2,3,4…(36) |
| Michigan4 | - | 559 001 059 | 001 059 009 | - | 7 | 184 | 3:011 055 066 | 5(6) | idx[20]:1,2,3,4…(36) |
| NewYork4 | - | 036 066 366 | 036 366 667 | - | 6 | 185 | 3:007 033 066 | 14(8) | idx[20]:1,2,3,4…(36) |
| NewJersey4 | - | 499 559 023 | 499 013 558 | - | 5 | 199 | 3:022 049 244 | 35(2) | idx[22]:1,2,3,4…(36) |
| Florida4 | - | 006 224 244 | 006 224 246 | - | 4 | 205 | 3:003 009 118 | 7(8) | idx[20]:1,2,3,4…(36) |
| SouthCarolina4 | - | 344 455 559 | 455 003 348 | - | 6 | 209 | 1:114 | 31(6) | idx[20]:2,3,4,5…(36) |
| Connecticut4 | - | 224 113 355 | 224 355 399 | - | 5 | 213 | 3:099 136 366 | 18(6) | idx[20]:2,4,5,6…(36) |
| OntarioCanada4 | - | 368 334 223 | 368 334 348 | - | 3 | 219 | 1:004 | 33(6) | idx[20]:1,4,5,8…(36) |
| Indiana4 | - | 559 599 455 | 559 599 455 | - | 4 | 232 | 1:177 | 28(6) | idx[20]:2,5,6,9…(36) |
| NorthCarolina4 | - | 299 112 117 | 299 008 122 | - | 4 | 241 | 4:009 112 225 | 18(6) | idx[20]:1,2,4,5…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Delaware4**: CU packs=`27` union=`181` top_support=`11:009` due=`009 033 088 117`
- **Pennsylvania4**: CU packs=`27` union=`187` top_support=`11:007` due=`007 009 066 228`
- **Ohio4**: CU packs=`27` union=`204` top_support=`11:009` due=`009 066 113 118`
- **PuertoRico4**: CU packs=`27` union=`233` top_support=`10:001` due=`001 003 011 033`
- **Virginia4**: CU packs=`27` union=`177` top_support=`9:004` due=`004 115 177 199`
- **Michigan4**: CU packs=`27` union=`184` top_support=`9:066` due=`066 077 119 144`
- **NewYork4**: CU packs=`27` union=`185` top_support=`9:007` due=`007 011 066 488`
- **NewJersey4**: CU packs=`27` union=`199` top_support=`9:022` due=`022 155 335 339`
- **Florida4**: CU packs=`27` union=`205` top_support=`9:003` due=`003 009 011 118`
- **SouthCarolina4**: CU packs=`27` union=`209` top_support=`9:114` due=`114 115 155 233`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Delaware4**: B24 `34(6)` (src `sharepacks/_predictive/2026-03-19/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-19/Delaware4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `3(6)` (src `sharepacks/_predictive/2026-03-19/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-19/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `9(8)` (src `sharepacks/_predictive/2026-03-19/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-19/Ohio4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `7(8)` (src `sharepacks/_predictive/2026-03-19/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-19/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `3(6)` (src `sharepacks/_predictive/2026-03-19/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-19/Virginia4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-19/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-19/Michigan4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `14(8)` (src `sharepacks/_predictive/2026-03-19/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-19/NewYork4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `35(2)` (src `sharepacks/_predictive/2026-03-19/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-19/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `7(8)` (src `sharepacks/_predictive/2026-03-19/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-19/Florida4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `31(6)` (src `sharepacks/_predictive/2026-03-19/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-19/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `18(6)` (src `sharepacks/_predictive/2026-03-19/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-19/Connecticut4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `33(6)` (src `sharepacks/_predictive/2026-03-19/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,4,5,8…(36)` (src `sharepacks/_predictive/2026-03-19/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `28(6)` (src `sharepacks/_predictive/2026-03-19/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,9…(36)` (src `sharepacks/_predictive/2026-03-19/Indiana4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `18(6)` (src `sharepacks/_predictive/2026-03-19/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-03-19/NorthCarolina4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
