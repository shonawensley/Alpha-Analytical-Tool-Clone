# Analysis Arena Predictive Portfolio — D=2026-03-13

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
- Control Center profit alerts: `sharepacks/_predictive/2026-03-13/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Virginia4 | - | 559 599 259 | 559 259 059 | - | 3 | 173 | 2:004 455 | 5(6) | idx[24]:1,2,3,4…(36) |
| Delaware4 | - | 499 559 005 | 005 249 129 | - | 4 | 172 | 3:009 117 559 | 5(6) | idx[20]:1,3,5,6…(36) |
| PuertoRico4 | - | 677 559 449 | 677 559 449 | - | 5 | 199 | 3:001 006 011 | 2(6) | idx[20]:1,2,3,4…(36) |
| Indiana4 | - | 599 788 005 | 005 889 689 | - | 4 | 212 | 3:177 255 288 | 20(6) | idx[20]:1,2,3,4…(36) |
| NorthCarolina4 | - | 009 388 366 | 388 366 368 | - | 3 | 216 | 2:009 344 | 5(6) | idx[20]:3,4,5,10…(36) |
| Ohio4 | - | 033 338 003 | 033 338 003 | - | 12 | 185 | 3:004 009 559 | 14(8) | idx[20]:2,4,5,6…(36) |
| OntarioCanada4 | - | 449 388 049 | 449 388 049 | - | 4 | 175 | 2:004 238 | 15(6) | idx[20]:1,4,5,9…(36) |
| Michigan4 | - | 688 455 559 | 008 045 058 | - | 2 | 187 | 3:004 008 066 | 4(6) | idx[20]:1,2,4,5…(36) |
| NewJersey4 | - | 244 004 167 | 244 004 167 | - | 12 | 189 | 2:022 244 | 12(8) | idx[20]:2,5,6,8…(36) |
| Florida4 | - | 224 499 226 | 499 022 024 | - | 2 | 194 | 2:003 244 | 12(8) | idx[20]:2,3,4,5…(36) |
| NewYork4 | - | 224 039 006 | 224 039 006 | - | 5 | 196 | 4:007 066 366 | 4(6) | idx[20]:2,3,4,5…(36) |
| Pennsylvania4 | - | 559 224 003 | 003 013 005 | - | 8 | 210 | 2:002 007 | 11(8) | idx[20]:1,2,3,4…(36) |
| Connecticut4 | - | 368 668 336 | 368 668 066 | - | 3 | 214 | 2:099 599 | 34(6) | idx[20]:2,3,5,6…(36) |
| SouthCarolina4 | - | 559 029 009 | 029 077 027 | - | 3 | 219 | 3:027 114 177 | 22(8) | idx[20]:2,3,5,6…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Virginia4**: CU packs=`27` union=`173` top_support=`12:004` due=`004 115 177 199`
- **Delaware4**: CU packs=`27` union=`172` top_support=`11:009` due=`009 033 088 117`
- **PuertoRico4**: CU packs=`27` union=`199` top_support=`11:001` due=`001 003 011 033`
- **Indiana4**: CU packs=`27` union=`212` top_support=`11:177` due=`177 226 288 337`
- **NorthCarolina4**: CU packs=`27` union=`216` top_support=`11:009` due=`009 225 299 344`
- **Ohio4**: CU packs=`27` union=`185` top_support=`10:009` due=`009 066 113 118`
- **OntarioCanada4**: CU packs=`27` union=`175` top_support=`9:004` due=`004 044 055 228`
- **Michigan4**: CU packs=`27` union=`187` top_support=`9:066` due=`066 077 119 144`
- **NewJersey4**: CU packs=`27` union=`189` top_support=`9:022` due=`022 155 335 339`
- **Florida4**: CU packs=`27` union=`194` top_support=`9:003` due=`003 009 011 118`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-13/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[24]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-13/Virginia4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-13/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-13/Delaware4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `2(6)` (src `sharepacks/_predictive/2026-03-13/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-13/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `20(6)` (src `sharepacks/_predictive/2026-03-13/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-13/Indiana4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-13/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,10…(36)` (src `sharepacks/_predictive/2026-03-13/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `14(8)` (src `sharepacks/_predictive/2026-03-13/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-13/Ohio4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `15(6)` (src `sharepacks/_predictive/2026-03-13/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,4,5,9…(36)` (src `sharepacks/_predictive/2026-03-13/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `4(6)` (src `sharepacks/_predictive/2026-03-13/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-03-13/Michigan4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `12(8)` (src `sharepacks/_predictive/2026-03-13/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,8…(36)` (src `sharepacks/_predictive/2026-03-13/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `12(8)` (src `sharepacks/_predictive/2026-03-13/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-13/Florida4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `4(6)` (src `sharepacks/_predictive/2026-03-13/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-13/NewYork4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `11(8)` (src `sharepacks/_predictive/2026-03-13/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-13/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `34(6)` (src `sharepacks/_predictive/2026-03-13/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-13/Connecticut4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `22(8)` (src `sharepacks/_predictive/2026-03-13/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-13/SouthCarolina4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
