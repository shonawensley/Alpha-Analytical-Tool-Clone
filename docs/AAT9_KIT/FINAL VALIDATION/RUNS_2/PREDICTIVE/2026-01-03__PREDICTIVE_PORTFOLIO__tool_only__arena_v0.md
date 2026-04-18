# Analysis Arena Predictive Portfolio — D=2026-01-03

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-03/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| PuertoRico4 | - | 344 225 226 | 226 003 002 | - | 4 | 198 | 2:022 225 | 10(6) | idx[20]:3,4,10,11…(36) |
| NewJersey4 | - | 299 599 899 | 599 899 229 | - | 3 | 134 | 1:022 | 10(6) | idx[20]:1,2,10,12…(36) |
| Pennsylvania4 | - | 559 599 5599 | 559 579 019 | - | 4 | 146 | 2:007 277 | 3(6) | idx[22]:1,2,3,5…(36) |
| Delaware4 | - | 449 004 599 | 449 004 014 | - | 9 | 149 | 3:004 009 559 | 5(6) | idx[19]:1,2,5,6…(33) |
| Ohio4 | - | 559 255 055 | 559 055 688 | - | 2 | 143 | 2:009 559 | 2(6) | idx[20]:1,2,3,4…(36) |
| Indiana4 | - | 244 368 668 | 244 168 066 | - | 5 | 164 | 3:002 066 177 | 7(8) | idx[17]:1,2,3,6…(33) |
| Michigan4 | - | 006 668 016 | 006 016 168 | - | 6 | 133 | 1:112 | 18(6) | idx[20]:2,4,6,8…(36) |
| Florida4 | - | 138 599 559 | 559 346 336 | - | 4 | 153 | 2:003 008 | 11(8) | idx[20]:4,5,6,10…(36) |
| SouthCarolina4 | - | 559 002 008 | 002 008 007 | - | 5 | 159 | 2:115 224 | 7(8) | idx[20]:2,3,4,5…(36) |
| Virginia4 | - | 224 229 334 | 224 179 | - | 3 | 163 | 3:004 177 455 | 12(8) | idx[22]:1,2,3,5…(36) |
| NorthCarolina4 | - | 229 224 299 | 224 299 044 | - | 3 | 170 | 2:001 044 | 5(6) | idx[19]:1,2,3,4…(35) |
| OntarioCanada4 | - | 267 255 1188 | 255 118 167 | - | 4 | 170 | 3:004 114 244 | 18(6) | idx[20]:2,3,5,6…(36) |
| Connecticut4 | - | 048 478 368 | 048 478 249 | - | 4 | 185 | 1:088 | 12(8) | idx[20]:1,2,4,6…(36) |
| NewYork4 | - | 788 889 038 | 889 038 066 | - | 3 | 190 | 2:001 066 | 6(6) | idx[20]:2,3,4,5…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **PuertoRico4**: CU packs=`27` union=`198` top_support=`12:022` due=`022 033 088 199`
- **NewJersey4**: CU packs=`27` union=`134` top_support=`11:022` due=`022 114 155 339`
- **Pennsylvania4**: CU packs=`27` union=`146` top_support=`11:007` due=`007 228 255 277`
- **Delaware4**: CU packs=`27` union=`149` top_support=`11:009` due=`009 088 223 228`
- **Ohio4**: CU packs=`27` union=`143` top_support=`10:009` due=`009 066 113 114`
- **Indiana4**: CU packs=`27` union=`164` top_support=`10:002` due=`002 022 177 226`
- **Michigan4**: CU packs=`27` union=`133` top_support=`9:112` due=`112 119 155 199`
- **Florida4**: CU packs=`27` union=`153` top_support=`9:003` due=`003 008 009 011`
- **SouthCarolina4**: CU packs=`27` union=`159` top_support=`9:115` due=`115 155 224 233`
- **Virginia4**: CU packs=`27` union=`163` top_support=`9:004` due=`004 177 199 377`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-03/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,10,11…(36)` (src `sharepacks/_predictive/2026-01-03/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-03/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,10,12…(36)` (src `sharepacks/_predictive/2026-01-03/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `3(6)` (src `sharepacks/_predictive/2026-01-03/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-03/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-03/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[19]:1,2,5,6…(33)` (src `sharepacks/_predictive/2026-01-03/Delaware4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `2(6)` (src `sharepacks/_predictive/2026-01-03/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-03/Ohio4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-03/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[17]:1,2,3,6…(33)` (src `sharepacks/_predictive/2026-01-03/Indiana4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `18(6)` (src `sharepacks/_predictive/2026-01-03/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,6,8…(36)` (src `sharepacks/_predictive/2026-01-03/Michigan4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `11(8)` (src `sharepacks/_predictive/2026-01-03/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,6,10…(36)` (src `sharepacks/_predictive/2026-01-03/Florida4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-03/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-03/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `12(8)` (src `sharepacks/_predictive/2026-01-03/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-03/Virginia4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-03/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[19]:1,2,3,4…(35)` (src `sharepacks/_predictive/2026-01-03/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `18(6)` (src `sharepacks/_predictive/2026-01-03/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-01-03/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `12(8)` (src `sharepacks/_predictive/2026-01-03/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,6…(36)` (src `sharepacks/_predictive/2026-01-03/Connecticut4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-03/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-03/NewYork4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
