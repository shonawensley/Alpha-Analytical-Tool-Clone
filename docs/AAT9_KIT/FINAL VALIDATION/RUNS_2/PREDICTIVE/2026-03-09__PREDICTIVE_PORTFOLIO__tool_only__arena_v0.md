# Analysis Arena Predictive Portfolio — D=2026-03-09

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
- Control Center profit alerts: `sharepacks/_predictive/2026-03-09/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Pennsylvania4 | - | 559 008 024 | 559 008 024 | - | 7 | 171 | 3:002 007 255 | 3(6) | idx[20]:1,3,4,5…(36) |
| OntarioCanada4 | - | 559 899 599 | 559 049 355 | - | 2 | 171 | 2:004 499 | 5(6) | idx[22]:1,3,4,5…(36) |
| Virginia4 | - | 039 599 358 | 039 358 138 | - | 6 | 195 | 1:004 | 5(6) | idx[20]:1,2,4,5…(36) |
| PuertoRico4 | - | 177 359 339 | 177 359 339 | - | 4 | 202 | 3:001 011 033 | 2(6) | idx[20]:2,3,5,6…(36) |
| NewJersey4 | - | 006 177 007 | 006 007 009 | - | 5 | 215 | 4:007 009 022 | 10(6) | idx[20]:2,3,5,6…(36) |
| NorthCarolina4 | - | 599 003 344 | 003 035 445 | - | 4 | 233 | 4:004 009 344 | 23(6) | idx[20]:2,3,4,5…(36) |
| Ohio4 | - | 599 559 003 | 599 559 003 | - | 10 | 190 | 2:009 559 | 5(6) | idx[20]:1,2,3,4…(36) |
| SouthCarolina4 | - | 667 006 069 | 667 069 077 | - | 3 | 187 | 2:114 155 | 6(6) | idx[20]:1,2,3,5…(36) |
| Connecticut4 | - | 168 189 006 | 168 668 099 | - | 3 | 191 | 2:099 116 | 18(6) | idx[22]:2,3,6,7…(36) |
| Michigan4 | - | 118 778 188 | 118 378 114 | - | 2 | 192 | 1:066 | 19(6) | idx[20]:2,6,8,10…(36) |
| NewYork4 | - | 559 368 689 | 559 368 689 | - | 4 | 196 | 2:007 368 | 8(8) | idx[20]:3,4,5,6…(36) |
| Florida4 | - | 224 778 889 | 224 189 014 | - | 3 | 197 | 3:003 011 388 | 33(6) | idx[22]:4,5,6,8…(36) |
| Indiana4 | - | 011 225 255 | 011 225 559 | - | 4 | 202 | 3:122 177 225 | 7(8) | idx[20]:1,3,4,5…(36) |
| Delaware4 | - | 006 129 259 | 006 129 119 | - | 4 | 220 | 3:009 117 559 | 14(8) | idx[20]:2,5,9,12…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Pennsylvania4**: CU packs=`27` union=`171` top_support=`12:007` due=`007 066 228 255`
- **OntarioCanada4**: CU packs=`27` union=`171` top_support=`11:004` due=`004 044 055 228`
- **Virginia4**: CU packs=`27` union=`195` top_support=`11:004` due=`004 115 177 199`
- **PuertoRico4**: CU packs=`27` union=`202` top_support=`11:001` due=`001 011 033 088`
- **NewJersey4**: CU packs=`27` union=`215` top_support=`11:022` due=`022 155 335 339`
- **NorthCarolina4**: CU packs=`27` union=`233` top_support=`11:009` due=`009 225 344 445`
- **Ohio4**: CU packs=`27` union=`190` top_support=`10:009` due=`009 066 113 118`
- **SouthCarolina4**: CU packs=`27` union=`187` top_support=`9:114` due=`114 115 155 233`
- **Connecticut4**: CU packs=`27` union=`191` top_support=`9:099` due=`099 116 228 399`
- **Michigan4**: CU packs=`27` union=`192` top_support=`9:066` due=`066 077 119 144`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Pennsylvania4**: B24 `3(6)` (src `sharepacks/_predictive/2026-03-09/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-09/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-09/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-09/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-09/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-03-09/Virginia4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `2(6)` (src `sharepacks/_predictive/2026-03-09/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-09/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `10(6)` (src `sharepacks/_predictive/2026-03-09/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-09/NewJersey4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `23(6)` (src `sharepacks/_predictive/2026-03-09/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-09/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-09/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-09/Ohio4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `6(6)` (src `sharepacks/_predictive/2026-03-09/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-03-09/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `18(6)` (src `sharepacks/_predictive/2026-03-09/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:2,3,6,7…(36)` (src `sharepacks/_predictive/2026-03-09/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `19(6)` (src `sharepacks/_predictive/2026-03-09/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,6,8,10…(36)` (src `sharepacks/_predictive/2026-03-09/Michigan4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `8(8)` (src `sharepacks/_predictive/2026-03-09/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-09/NewYork4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `33(6)` (src `sharepacks/_predictive/2026-03-09/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:4,5,6,8…(36)` (src `sharepacks/_predictive/2026-03-09/Florida4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `7(8)` (src `sharepacks/_predictive/2026-03-09/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-09/Indiana4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `14(8)` (src `sharepacks/_predictive/2026-03-09/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,9,12…(36)` (src `sharepacks/_predictive/2026-03-09/Delaware4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
