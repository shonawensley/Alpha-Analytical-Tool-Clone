# Analysis Arena Predictive Portfolio — D=2026-01-18

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-18/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Connecticut4 | - | 088 559 599 | 088 688 025 | - | 3 | 171 | 1:088 | 13(6) | idx[20]:4,5,11,12…(36) |
| Ohio4 | - | 009 004 049 | 009 004 049 | - | 4 | 173 | 2:004 009 | 5(6) | idx[20]:3,4,5,6…(36) |
| Florida4 | - | 225 255 559 | 599 378 578 | - | 3 | 118 | 2:003 355 | 4(6) | idx[16]:1,2,3,4…(32) |
| Virginia4 | - | 339 016 449 | 339 016 125 | - | 6 | 140 | 2:004 455 | 5(6) | idx[22]:1,2,3,5…(36) |
| Delaware4 | - | 259 007 559 | 259 249 579 | - | 3 | 170 | 3:004 009 559 | 5(6) | idx[20]:1,2,3,4…(36) |
| OntarioCanada4 | - | 244 236 344 | 244 236 014 | - | 3 | 145 | 2:004 044 | 5(6) | idx[20]:5,7,8,12…(36) |
| PuertoRico4 | - | 334 014 148 | 334 014 148 | - | 5 | 191 | 2:022 225 | 10(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | - | 224 177 011 | 011 259 001 | - | 5 | 119 | 3:011 066 155 | 2(6) | idx[22]:1,2,3,4…(36) |
| NewYork4 | - | 377 339 368 | 377 339 368 | - | 5 | 141 | 2:001 007 | 6(6) | idx[20]:2,3,6,7…(36) |
| SouthCarolina4 | - | 005 677 007 | 005 677 067 | - | 4 | 146 | 2:114 466 | 19(6) | idx[20]:1,2,3,4…(36) |
| NewJersey4 | - | 019 009 004 | 019 009 499 | - | 8 | 153 | 2:022 348 | 7(8) | idx[20]:1,2,3,4…(36) |
| NorthCarolina4 | - | 244 778 225 | 244 257 278 | - | 3 | 159 | 2:001 225 | 26(2) | idx[19]:1,2,5,6…(33) |
| Pennsylvania4 | - | 344 004 244 | 344 004 024 | - | 8 | 179 | 1:007 | 34(6) | idx[20]:1,3,4,5…(36) |
| Indiana4 | - | 077 368 559 | 005 139 068 | - | 3 | 202 | 3:002 007 226 | 9(8) | idx[20]:1,2,3,4…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Connecticut4**: CU packs=`27` union=`171` top_support=`12:088` due=`088 099 223 228`
- **Ohio4**: CU packs=`27` union=`173` top_support=`12:009` due=`009 066 113 118`
- **Florida4**: CU packs=`27` union=`118` top_support=`11:003` due=`003 009 011 077`
- **Virginia4**: CU packs=`27` union=`140` top_support=`11:004` due=`004 177 199 334`
- **Delaware4**: CU packs=`27` union=`170` top_support=`11:009` due=`009 088 117 223`
- **OntarioCanada4**: CU packs=`27` union=`145` top_support=`10:004` due=`004 044 144 228`
- **PuertoRico4**: CU packs=`27` union=`191` top_support=`10:022` due=`022 033 088 112`
- **Michigan4**: CU packs=`27` union=`119` top_support=`9:066` due=`066 112 119 155`
- **NewYork4**: CU packs=`27` union=`141` top_support=`9:001` due=`001 007 011 066`
- **SouthCarolina4**: CU packs=`27` union=`146` top_support=`9:114` due=`114 115 155 233`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Connecticut4**: B24 `13(6)` (src `sharepacks/_predictive/2026-01-18/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,11,12…(36)` (src `sharepacks/_predictive/2026-01-18/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-18/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-01-18/Ohio4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `4(6)` (src `sharepacks/_predictive/2026-01-18/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[16]:1,2,3,4…(32)` (src `sharepacks/_predictive/2026-01-18/Florida4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-18/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-18/Virginia4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-18/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-18/Delaware4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-18/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:5,7,8,12…(36)` (src `sharepacks/_predictive/2026-01-18/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-18/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-18/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `2(6)` (src `sharepacks/_predictive/2026-01-18/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-18/Michigan4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-18/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,6,7…(36)` (src `sharepacks/_predictive/2026-01-18/NewYork4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `19(6)` (src `sharepacks/_predictive/2026-01-18/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-18/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-18/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-18/NewJersey4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `26(2)` (src `sharepacks/_predictive/2026-01-18/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[19]:1,2,5,6…(33)` (src `sharepacks/_predictive/2026-01-18/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `34(6)` (src `sharepacks/_predictive/2026-01-18/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-18/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `9(8)` (src `sharepacks/_predictive/2026-01-18/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-18/Indiana4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
