# Analysis Arena Predictive Portfolio — D=2026-01-05

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-05/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| PuertoRico4 | - | 344 224 268 | 026 003 226 | - | 4 | 227 | 4:022 033 088 | 10(6) | idx[20]:3,4,7,8…(36) |
| Pennsylvania4 | - | 559 059 599 | 559 059 007 | - | 3 | 193 | 2:007 557 | 3(6) | idx[20]:1,2,3,5…(36) |
| Ohio4 | - | 088 599 008 | 088 599 008 | - | 6 | 170 | 1:009 | 3(6) | idx[20]:1,3,4,5…(36) |
| NewYork4 | - | 025 008 005 | 025 008 005 | - | 5 | 175 | 1:001 | 6(6) | idx[20]:1,2,3,4…(36) |
| Delaware4 | - | 449 244 004 | 449 055 058 | - | 3 | 188 | 4:004 009 088 | 5(6) | idx[20]:1,2,4,5…(36) |
| Michigan4 | - | 168 118 668 | 168 668 011 | - | 4 | 150 | 2:112 119 | 18(6) | idx[20]:2,3,5,6…(36) |
| Florida4 | - | 344 033 334 | 344 033 334 | - | 4 | 171 | 3:003 008 344 | 34(6) | idx[20]:4,5,6,9…(36) |
| NewJersey4 | - | 778 008 599 | 778 008 289 | - | 7 | 193 | 4:022 077 088 | 11(8) | idx[20]:2,3,4,8…(36) |
| NorthCarolina4 | - | 229 224 299 | 224 299 044 | - | 4 | 196 | 3:001 044 225 | 31(6) | idx[20]:1,2,3,4…(36) |
| Indiana4 | - | 244 668 0668 | 244 668 066 | - | 3 | 223 | 2:002 177 | 18(6) | idx[20]:2,3,5,6…(36) |
| OntarioCanada4 | - | 477 177 459 | 477 459 244 | - | 4 | 224 | 3:004 244 249 | 9(8) | idx[20]:2,5,6,7…(36) |
| SouthCarolina4 | - | 677 007 599 | 677 007 259 | - | 6 | 224 | 2:115 224 | 20(6) | idx[20]:1,2,3,4…(36) |
| Connecticut4 | - | 224 447 2244 | 447 024 044 | - | 3 | 225 | 2:088 778 | 12(8) | idx[20]:1,5,9,11…(36) |
| Virginia4 | - | 224 559 377 | 377 008 599 | - | 6 | 225 | 4:004 377 455 | 14(8) | idx[20]:1,2,4,5…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **PuertoRico4**: CU packs=`27` union=`227` top_support=`13:022` due=`022 033 088 199`
- **Pennsylvania4**: CU packs=`27` union=`193` top_support=`12:007` due=`007 066 228 255`
- **Ohio4**: CU packs=`27` union=`170` top_support=`11:009` due=`009 066 113 118`
- **NewYork4**: CU packs=`27` union=`175` top_support=`11:001` due=`001 007 011 066`
- **Delaware4**: CU packs=`27` union=`188` top_support=`11:009` due=`009 088 223 228`
- **Michigan4**: CU packs=`27` union=`150` top_support=`9:112` due=`112 119 155 199`
- **Florida4**: CU packs=`27` union=`171` top_support=`9:003` due=`003 008 009 011`
- **NewJersey4**: CU packs=`27` union=`193` top_support=`9:022` due=`022 114 155 339`
- **NorthCarolina4**: CU packs=`27` union=`196` top_support=`9:001` due=`001 009 044 225`
- **Indiana4**: CU packs=`27` union=`223` top_support=`9:002` due=`002 022 177 226`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-05/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,7,8…(36)` (src `sharepacks/_predictive/2026-01-05/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `3(6)` (src `sharepacks/_predictive/2026-01-05/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-05/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `3(6)` (src `sharepacks/_predictive/2026-01-05/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-05/Ohio4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-05/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-05/NewYork4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-05/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-01-05/Delaware4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `18(6)` (src `sharepacks/_predictive/2026-01-05/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-01-05/Michigan4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `34(6)` (src `sharepacks/_predictive/2026-01-05/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,6,9…(36)` (src `sharepacks/_predictive/2026-01-05/Florida4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `11(8)` (src `sharepacks/_predictive/2026-01-05/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,8…(36)` (src `sharepacks/_predictive/2026-01-05/NewJersey4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `31(6)` (src `sharepacks/_predictive/2026-01-05/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-05/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `18(6)` (src `sharepacks/_predictive/2026-01-05/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-01-05/Indiana4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `9(8)` (src `sharepacks/_predictive/2026-01-05/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,7…(36)` (src `sharepacks/_predictive/2026-01-05/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `20(6)` (src `sharepacks/_predictive/2026-01-05/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-05/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `12(8)` (src `sharepacks/_predictive/2026-01-05/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,5,9,11…(36)` (src `sharepacks/_predictive/2026-01-05/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `14(8)` (src `sharepacks/_predictive/2026-01-05/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-01-05/Virginia4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
