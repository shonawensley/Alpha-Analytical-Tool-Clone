# Analysis Arena Predictive Portfolio — D=2026-03-17

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
- Control Center profit alerts: `sharepacks/_predictive/2026-03-17/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Ohio4 | - | 069 559 224 | 069 224 599 | - | 6 | 189 | 3:004 009 066 | 9(8) | idx[20]:2,3,4,5…(36) |
| Indiana4 | - | 599 559 224 | 559 569 015 | - | 4 | 238 | 2:177 288 | 20(6) | idx[20]:6,9,11,12…(36) |
| Virginia4 | - | 255 559 289 | 255 559 289 | - | 4 | 179 | 3:004 055 455 | 5(6) | idx[22]:1,2,3,4…(36) |
| NewYork4 | - | 007 6678 668 | 007 035 234 | - | 7 | 197 | 2:007 035 | 14(8) | idx[20]:2,3,4,5…(36) |
| Pennsylvania4 | - | 077 559 033 | 077 067 334 | - | 7 | 211 | 2:007 077 | 10(6) | idx[20]:2,3,4,5…(36) |
| NorthCarolina4 | - | 138 366 036 | 138 036 338 | - | 4 | 235 | 2:009 344 | 18(6) | idx[20]:1,5,6,8…(36) |
| Delaware4 | - | 599 099 019 | 599 099 019 | - | 5 | 188 | 3:009 499 559 | 25(6) | idx[20]:2,5,6,7…(36) |
| NewJersey4 | - | 038 118 499 | 038 499 013 | - | 4 | 193 | 1:022 | 19(6) | idx[22]:2,3,5,6…(36) |
| SouthCarolina4 | - | 344 455 559 | 344 036 477 | - | 4 | 194 | 2:114 445 | 31(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | - | 044 667 677 | 044 667 055 | - | 6 | 197 | 2:066 088 | 5(6) | idx[20]:1,2,4,5…(36) |
| OntarioCanada4 | - | 223 168 138 | 223 138 113 | - | 4 | 197 | 2:004 168 | 9(8) | idx[20]:1,2,5,9…(36) |
| Florida4 | - | 668 006 255 | 668 466 266 | - | 4 | 206 | 2:003 118 | 6(6) | idx[20]:1,2,3,4…(36) |
| Connecticut4 | - | 344 559 139 | 139 399 136 | - | 5 | 217 | 3:099 399 599 | 34(6) | idx[20]:2,4,5,6…(36) |
| PuertoRico4 | - | 244 677 047 | 677 047 024 | - | 3 | 217 | 1:001 | 10(6) | idx[20]:2,3,4,5…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Ohio4**: CU packs=`27` union=`189` top_support=`12:009` due=`009 066 113 118`
- **Indiana4**: CU packs=`27` union=`238` top_support=`12:177` due=`177 226 288 337`
- **Virginia4**: CU packs=`27` union=`179` top_support=`11:004` due=`004 115 177 199`
- **NewYork4**: CU packs=`27` union=`197` top_support=`10:007` due=`007 011 066 488`
- **Pennsylvania4**: CU packs=`27` union=`211` top_support=`10:007` due=`007 009 066 228`
- **NorthCarolina4**: CU packs=`27` union=`235` top_support=`10:009` due=`009 225 299 344`
- **Delaware4**: CU packs=`27` union=`188` top_support=`9:009` due=`009 033 088 117`
- **NewJersey4**: CU packs=`27` union=`193` top_support=`9:022` due=`022 155 335 339`
- **SouthCarolina4**: CU packs=`27` union=`194` top_support=`9:114` due=`114 115 155 233`
- **Michigan4**: CU packs=`27` union=`197` top_support=`9:066` due=`066 077 119 144`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Ohio4**: B24 `9(8)` (src `sharepacks/_predictive/2026-03-17/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-17/Ohio4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `20(6)` (src `sharepacks/_predictive/2026-03-17/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:6,9,11,12…(36)` (src `sharepacks/_predictive/2026-03-17/Indiana4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-17/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-17/Virginia4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `14(8)` (src `sharepacks/_predictive/2026-03-17/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-17/NewYork4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `10(6)` (src `sharepacks/_predictive/2026-03-17/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-17/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `18(6)` (src `sharepacks/_predictive/2026-03-17/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,5,6,8…(36)` (src `sharepacks/_predictive/2026-03-17/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `25(6)` (src `sharepacks/_predictive/2026-03-17/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,7…(36)` (src `sharepacks/_predictive/2026-03-17/Delaware4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `19(6)` (src `sharepacks/_predictive/2026-03-17/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-17/NewJersey4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `31(6)` (src `sharepacks/_predictive/2026-03-17/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-17/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-17/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-03-17/Michigan4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `9(8)` (src `sharepacks/_predictive/2026-03-17/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,9…(36)` (src `sharepacks/_predictive/2026-03-17/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `6(6)` (src `sharepacks/_predictive/2026-03-17/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-17/Florida4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `34(6)` (src `sharepacks/_predictive/2026-03-17/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-17/Connecticut4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-03-17/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-17/PuertoRico4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
