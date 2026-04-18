# Analysis Arena Predictive Portfolio — D=2026-01-07

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-07/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| NewYork4 | - | 008 001 667 | 008 001 025 | - | 4 | 174 | 3:001 011 066 | 2(6) | idx[20]:1,2,3,4…(36) |
| PuertoRico4 | - | 068 006 003 | 068 003 138 | - | 3 | 243 | 3:022 033 225 | 10(6) | idx[20]:3,4,5,6…(36) |
| NewJersey4 | - | 778 189 088 | 778 189 119 | - | 5 | 186 | 3:022 077 114 | 10(6) | idx[20]:1,2,4,7…(36) |
| SouthCarolina4 | - | 599 224 399 | 224 005 559 | - | 4 | 191 | 3:115 224 566 | 6(6) | idx[20]:1,2,3,4…(36) |
| Ohio4 | - | 559 088 299 | 559 299 889 | - | 4 | 198 | 4:009 088 559 | 4(6) | idx[20]:1,2,3,4…(36) |
| NorthCarolina4 | - | 299 244 229 | 299 244 246 | - | 4 | 201 | 2:001 044 | 31(6) | idx[20]:2,3,4,5…(36) |
| Delaware4 | - | 334 003 044 | 334 118 033 | - | 8 | 220 | 3:004 009 559 | 5(6) | idx[20]:2,4,5,6…(36) |
| OntarioCanada4 | - | 559 244 015 | 244 015 224 | - | 2 | 241 | 3:004 044 224 | 28(6) | idx[20]:2,5,6,9…(36) |
| Florida4 | - | 334 346 336 | 334 346 336 | - | 4 | 163 | 3:003 033 334 | 33(6) | idx[20]:4,5,6,10…(36) |
| Michigan4 | - | 668 011 001 | 011 001 344 | - | 4 | 179 | 2:112 119 | 19(6) | idx[20]:2,5,6,8…(36) |
| Connecticut4 | - | 224 2244 244 | 224 244 448 | - | 4 | 189 | 3:088 223 228 | 30(8) | idx[20]:5,6,12,13…(36) |
| Virginia4 | - | 559 224 009 | 559 009 024 | - | 8 | 200 | 3:004 199 377 | 34(6) | idx[20]:2,3,4,5…(36) |
| Pennsylvania4 | - | 000 001 009 | 000 001 009 | - | 6 | 219 | 3:007 112 557 | 7(8) | idx[20]:1,2,3,4…(36) |
| Indiana4 | - | 244 066 004 | 244 066 004 | - | 5 | 240 | 3:002 066 266 | 12(8) | idx[20]:2,3,5,6…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **NewYork4**: CU packs=`27` union=`174` top_support=`14:001` due=`001 007 011 066`
- **PuertoRico4**: CU packs=`27` union=`243` top_support=`12:022` due=`022 033 199 299`
- **NewJersey4**: CU packs=`27` union=`186` top_support=`11:022` due=`022 114 155 339`
- **SouthCarolina4**: CU packs=`27` union=`191` top_support=`11:115` due=`115 155 224 233`
- **Ohio4**: CU packs=`27` union=`198` top_support=`10:009` due=`009 066 113 118`
- **NorthCarolina4**: CU packs=`27` union=`201` top_support=`10:001` due=`001 009 044 225`
- **Delaware4**: CU packs=`27` union=`220` top_support=`10:009` due=`009 088 223 228`
- **OntarioCanada4**: CU packs=`27` union=`241` top_support=`10:004` due=`004 044 144 228`
- **Florida4**: CU packs=`27` union=`163` top_support=`9:003` due=`003 009 011 077`
- **Michigan4**: CU packs=`27` union=`179` top_support=`9:112` due=`112 119 155 199`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **NewYork4**: B24 `2(6)` (src `sharepacks/_predictive/2026-01-07/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-07/NewYork4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-07/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-01-07/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-07/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,7…(36)` (src `sharepacks/_predictive/2026-01-07/NewJersey4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-07/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-07/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `4(6)` (src `sharepacks/_predictive/2026-01-07/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-07/Ohio4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `31(6)` (src `sharepacks/_predictive/2026-01-07/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-07/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-07/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive/2026-01-07/Delaware4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `28(6)` (src `sharepacks/_predictive/2026-01-07/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,9…(36)` (src `sharepacks/_predictive/2026-01-07/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `33(6)` (src `sharepacks/_predictive/2026-01-07/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,6,10…(36)` (src `sharepacks/_predictive/2026-01-07/Florida4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `19(6)` (src `sharepacks/_predictive/2026-01-07/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,8…(36)` (src `sharepacks/_predictive/2026-01-07/Michigan4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `30(8)` (src `sharepacks/_predictive/2026-01-07/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:5,6,12,13…(36)` (src `sharepacks/_predictive/2026-01-07/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `34(6)` (src `sharepacks/_predictive/2026-01-07/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-07/Virginia4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-07/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-07/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `12(8)` (src `sharepacks/_predictive/2026-01-07/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-01-07/Indiana4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
