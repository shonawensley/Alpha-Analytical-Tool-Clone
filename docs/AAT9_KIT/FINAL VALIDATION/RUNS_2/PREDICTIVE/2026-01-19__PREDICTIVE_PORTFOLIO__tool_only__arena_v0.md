# Analysis Arena Predictive Portfolio — D=2026-01-19

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-19/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Ohio4 | - | 004 009 077 | 004 009 003 | - | 5 | 173 | 2:004 009 | 5(6) | idx[20]:3,4,5,6…(36) |
| SouthCarolina4 | - | 005 099 399 | 005 399 677 | - | 5 | 138 | 2:114 466 | 19(6) | idx[20]:1,2,4,5…(36) |
| Connecticut4 | - | 599 058 559 | 058 025 355 | - | 5 | 176 | 1:088 | 11(8) | idx[20]:1,2,4,5…(36) |
| Delaware4 | - | 559 259 007 | 559 259 467 | - | 4 | 176 | 3:004 009 559 | 5(6) | idx[20]:1,2,3,5…(36) |
| OntarioCanada4 | - | 244 044 236 | 244 246 368 | - | 3 | 152 | 2:004 044 | 5(6) | idx[20]:1,2,3,5…(36) |
| PuertoRico4 | - | 334 014 148 | 334 014 148 | - | 5 | 191 | 2:022 225 | 10(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | - | 224 011 017 | 011 017 115 | - | 3 | 122 | 3:011 066 155 | 2(6) | idx[20]:1,2,3,4…(36) |
| NewYork4 | - | 377 337 177 | 377 337 177 | - | 4 | 136 | 2:001 007 | 6(6) | idx[20]:2,3,5,6…(36) |
| Florida4 | - | 388 255 378 | 378 358 889 | - | 2 | 140 | 2:003 355 | 11(8) | idx[18]:1,2,3,4…(34) |
| Virginia4 | - | 339 133 002 | 339 133 016 | - | 6 | 152 | 2:004 455 | 3(6) | idx[20]:1,2,3,4…(36) |
| NewJersey4 | - | 004 014 019 | 004 014 019 | - | 9 | 156 | 2:001 022 | 5(6) | idx[20]:1,2,3,5…(36) |
| Pennsylvania4 | - | 344 004 224 | 344 004 034 | - | 6 | 170 | 1:007 | 34(6) | idx[20]:3,4,5,6…(36) |
| NorthCarolina4 | - | 778 244 225 | 244 225 238 | - | 4 | 172 | 2:001 225 | 27(6) | idx[22]:1,2,5,6…(36) |
| Indiana4 | - | 077 007 038 | 007 038 017 | - | 4 | 198 | 3:002 007 226 | 3(6) | idx[20]:1,2,3,5…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Ohio4**: CU packs=`27` union=`173` top_support=`12:009` due=`009 066 113 118`
- **SouthCarolina4**: CU packs=`27` union=`138` top_support=`11:114` due=`114 115 155 233`
- **Connecticut4**: CU packs=`27` union=`176` top_support=`11:088` due=`088 099 223 228`
- **Delaware4**: CU packs=`27` union=`176` top_support=`11:009` due=`009 088 117 223`
- **OntarioCanada4**: CU packs=`27` union=`152` top_support=`10:004` due=`004 044 144 228`
- **PuertoRico4**: CU packs=`27` union=`191` top_support=`10:022` due=`022 033 088 112`
- **Michigan4**: CU packs=`27` union=`122` top_support=`9:066` due=`066 112 119 155`
- **NewYork4**: CU packs=`27` union=`136` top_support=`9:001` due=`001 007 011 066`
- **Florida4**: CU packs=`27` union=`140` top_support=`9:003` due=`003 009 011 077`
- **Virginia4**: CU packs=`27` union=`152` top_support=`9:004` due=`004 177 199 334`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Ohio4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-19/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-01-19/Ohio4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `19(6)` (src `sharepacks/_predictive/2026-01-19/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-01-19/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `11(8)` (src `sharepacks/_predictive/2026-01-19/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-01-19/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-19/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-19/Delaware4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-19/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-19/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-19/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-19/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `2(6)` (src `sharepacks/_predictive/2026-01-19/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-19/Michigan4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-19/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-01-19/NewYork4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `11(8)` (src `sharepacks/_predictive/2026-01-19/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[18]:1,2,3,4…(34)` (src `sharepacks/_predictive/2026-01-19/Florida4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `3(6)` (src `sharepacks/_predictive/2026-01-19/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-19/Virginia4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-19/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-19/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `34(6)` (src `sharepacks/_predictive/2026-01-19/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-01-19/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `27(6)` (src `sharepacks/_predictive/2026-01-19/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,5,6…(36)` (src `sharepacks/_predictive/2026-01-19/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `3(6)` (src `sharepacks/_predictive/2026-01-19/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-19/Indiana4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
