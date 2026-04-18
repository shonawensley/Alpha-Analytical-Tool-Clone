# Analysis Arena Predictive Portfolio — D=2026-01-01

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-01/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| NewJersey4 | - | 299 778 118 | 299 778 899 | - | 2 | 142 | 1:022 | 10(6) | idx[20]:1,2,10,12…(36) |
| Delaware4 | - | 244 014 144 | 244 014 144 | - | 2 | 159 | 3:004 009 114 | 5(6) | idx[22]:1,2,5,6…(36) |
| Ohio4 | - | 055 559 068 | 055 559 068 | - | 6 | 161 | 2:009 559 | 6(6) | idx[20]:1,2,3,4…(36) |
| PuertoRico4 | - | 344 113 224 | 224 002 001 | - | 5 | 223 | 3:022 199 224 | 10(6) | idx[20]:2,3,6,10…(36) |
| Connecticut4 | - | 011 388 368 | 011 368 008 | - | 8 | 178 | 2:008 088 | 4(6) | idx[20]:2,3,4,6…(36) |
| SouthCarolina4 | - | 118 011 138 | 118 138 068 | - | 4 | 139 | 3:011 115 155 | 2(6) | idx[20]:1,2,4,5…(36) |
| Florida4 | - | 599 138 559 | 138 077 133 | - | 4 | 145 | 4:003 008 077 | 11(8) | idx[24]:4,5,6,7…(36) |
| Michigan4 | - | 006 133 599 | 006 133 069 | - | 8 | 153 | 2:112 155 | 2(6) | idx[20]:2,3,4,5…(36) |
| Virginia4 | - | 224 177 133 | 224 137 113 | - | 4 | 167 | 3:004 177 334 | 20(6) | idx[20]:1,2,3,4…(36) |
| OntarioCanada4 | - | 114 022 255 | 114 022 255 | - | 6 | 170 | 2:004 114 | 19(6) | idx[20]:1,2,4,5…(36) |
| Pennsylvania4 | - | 559 359 339 | 559 359 339 | - | 3 | 170 | 3:007 138 277 | 23(6) | idx[20]:1,3,4,5…(36) |
| NorthCarolina4 | - | 224 003 223 | 224 223 229 | - | 4 | 175 | 2:001 044 | 12(8) | idx[20]:1,2,3,4…(36) |
| Indiana4 | - | 677 244 668 | 677 368 056 | - | 3 | 180 | 3:002 177 667 | 7(8) | idx[19]:1,2,3,4…(35) |
| NewYork4 | - | 778 677 6677 | 778 677 678 | - | 4 | 183 | 3:001 006 677 | 6(6) | idx[20]:2,3,5,6…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **NewJersey4**: CU packs=`27` union=`142` top_support=`12:022` due=`022 114 155 339`
- **Delaware4**: CU packs=`27` union=`159` top_support=`11:009` due=`009 088 223 228`
- **Ohio4**: CU packs=`27` union=`161` top_support=`11:009` due=`009 066 113 114`
- **PuertoRico4**: CU packs=`27` union=`223` top_support=`11:022` due=`022 033 088 199`
- **Connecticut4**: CU packs=`27` union=`178` top_support=`10:088` due=`088 099 223 228`
- **SouthCarolina4**: CU packs=`27` union=`139` top_support=`9:115` due=`115 155 224 288`
- **Florida4**: CU packs=`27` union=`145` top_support=`9:003` due=`003 008 009 011`
- **Michigan4**: CU packs=`27` union=`153` top_support=`9:112` due=`112 119 155 199`
- **Virginia4**: CU packs=`27` union=`167` top_support=`9:004` due=`004 177 199 377`
- **OntarioCanada4**: CU packs=`27` union=`170` top_support=`9:004` due=`004 044 144 244`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **NewJersey4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-01/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,10,12…(36)` (src `sharepacks/_predictive/2026-01-01/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-01/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,5,6…(36)` (src `sharepacks/_predictive/2026-01-01/Delaware4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-01/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-01/Ohio4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-01/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,6,10…(36)` (src `sharepacks/_predictive/2026-01-01/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `4(6)` (src `sharepacks/_predictive/2026-01-01/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,6…(36)` (src `sharepacks/_predictive/2026-01-01/Connecticut4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `2(6)` (src `sharepacks/_predictive/2026-01-01/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-01-01/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `11(8)` (src `sharepacks/_predictive/2026-01-01/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[24]:4,5,6,7…(36)` (src `sharepacks/_predictive/2026-01-01/Florida4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `2(6)` (src `sharepacks/_predictive/2026-01-01/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-01/Michigan4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `20(6)` (src `sharepacks/_predictive/2026-01-01/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-01/Virginia4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `19(6)` (src `sharepacks/_predictive/2026-01-01/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-01-01/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `23(6)` (src `sharepacks/_predictive/2026-01-01/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-01/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `12(8)` (src `sharepacks/_predictive/2026-01-01/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-01/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-01/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[19]:1,2,3,4…(35)` (src `sharepacks/_predictive/2026-01-01/Indiana4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-01/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-01-01/NewYork4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
