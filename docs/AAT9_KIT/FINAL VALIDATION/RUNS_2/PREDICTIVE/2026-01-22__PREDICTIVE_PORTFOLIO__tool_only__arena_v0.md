# Analysis Arena Predictive Portfolio — D=2026-01-22

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-22/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Delaware4 | - | 559 255 336 | 255 259 133 | - | 3 | 162 | 3:004 009 559 | 5(6) | idx[20]:1,2,3,4…(36) |
| Ohio4 | - | 007 078 008 | 008 057 224 | - | 3 | 171 | 2:009 559 | 5(6) | idx[20]:3,4,5,6…(36) |
| OntarioCanada4 | - | 044 244 445 | 044 255 | - | 7 | 143 | 3:004 044 144 | 15(6) | idx[20]:1,3,4,5…(36) |
| Virginia4 | - | 559 026 016 | 026 339 033 | - | 8 | 155 | 2:004 009 | 3(6) | idx[20]:1,2,3,4…(36) |
| PuertoRico4 | - | 366 011 334 | 334 168 015 | - | 5 | 162 | 3:022 033 168 | 10(6) | idx[20]:1,2,3,4…(36) |
| Connecticut4 | - | 005 006 255 | 058 003 038 | - | 4 | 169 | 2:088 116 | 6(6) | idx[20]:1,2,3,4…(36) |
| Pennsylvania4 | - | 559 599 399 | 559 399 007 | - | 5 | 171 | 2:007 138 | 23(6) | idx[20]:3,4,5,6…(36) |
| Indiana4 | - | 077 001 003 | 003 347 014 | - | 6 | 177 | 3:001 002 007 | 10(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | - | 224 477 559 | 077 017 457 | - | 3 | 139 | 1:066 | 19(6) | idx[20]:2,3,5,6…(36) |
| Florida4 | - | 007 259 224 | 007 178 138 | - | 4 | 143 | 2:003 355 | 11(8) | idx[20]:1,3,4,5…(36) |
| NewJersey4 | - | 017 299 009 | 017 299 137 | - | 3 | 143 | 2:001 022 | 2(6) | idx[20]:1,2,3,4…(36) |
| SouthCarolina4 | - | 009 599 005 | 599 005 039 | - | 3 | 156 | 2:114 233 | 5(6) | idx[20]:1,2,3,5…(36) |
| NewYork4 | - | 238 337 133 | 238 337 115 | - | 4 | 167 | 2:001 238 | 29(6) | idx[20]:2,3,6,7…(36) |
| NorthCarolina4 | - | 113 778 011 | 113 006 119 | - | 4 | 179 | 2:001 006 | 27(6) | idx[20]:1,2,5,6…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Delaware4**: CU packs=`27` union=`162` top_support=`11:009` due=`009 088 117 223`
- **Ohio4**: CU packs=`27` union=`171` top_support=`11:009` due=`009 066 113 118`
- **OntarioCanada4**: CU packs=`27` union=`143` top_support=`10:004` due=`004 044 144 228`
- **Virginia4**: CU packs=`27` union=`155` top_support=`10:004` due=`004 177 199 334`
- **PuertoRico4**: CU packs=`27` union=`162` top_support=`10:022` due=`022 033 088 112`
- **Connecticut4**: CU packs=`27` union=`169` top_support=`10:088` due=`088 099 116 223`
- **Pennsylvania4**: CU packs=`27` union=`171` top_support=`10:007` due=`007 066 228 255`
- **Indiana4**: CU packs=`27` union=`177` top_support=`10:002` due=`002 022 177 226`
- **Michigan4**: CU packs=`27` union=`139` top_support=`9:066` due=`066 112 119 155`
- **Florida4**: CU packs=`27` union=`143` top_support=`9:003` due=`003 009 011 077`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-22/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-22/Delaware4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-22/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-01-22/Ohio4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `15(6)` (src `sharepacks/_predictive/2026-01-22/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-22/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `3(6)` (src `sharepacks/_predictive/2026-01-22/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-22/Virginia4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-22/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-22/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-22/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-22/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `23(6)` (src `sharepacks/_predictive/2026-01-22/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-01-22/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-22/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-22/Indiana4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `19(6)` (src `sharepacks/_predictive/2026-01-22/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-01-22/Michigan4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `11(8)` (src `sharepacks/_predictive/2026-01-22/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-22/Florida4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `2(6)` (src `sharepacks/_predictive/2026-01-22/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-22/NewJersey4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-22/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-22/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `29(6)` (src `sharepacks/_predictive/2026-01-22/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,6,7…(36)` (src `sharepacks/_predictive/2026-01-22/NewYork4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `27(6)` (src `sharepacks/_predictive/2026-01-22/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,6…(36)` (src `sharepacks/_predictive/2026-01-22/NorthCarolina4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
