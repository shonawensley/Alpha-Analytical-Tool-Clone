# Analysis Arena Predictive Portfolio — D=2026-01-04

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-04/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| PuertoRico4 | - | 344 224 268 | 026 003 226 | - | 4 | 185 | 2:022 033 | 10(6) | idx[20]:3,4,7,10…(36) |
| Michigan4 | - | 168 668 156 | 168 156 013 | - | 5 | 136 | 2:016 112 | 17(6) | idx[20]:2,5,6,8…(36) |
| Pennsylvania4 | - | 559 599 5599 | 559 059 055 | - | 4 | 148 | 1:007 | 3(6) | idx[21]:1,2,3,5…(35) |
| Delaware4 | - | 449 559 004 | 004 058 055 | - | 5 | 156 | 4:004 009 088 | 5(6) | idx[24]:1,2,4,5…(36) |
| OntarioCanada4 | - | 007 047 118 | 007 047 118 | - | 6 | 158 | 2:004 244 | 5(6) | idx[20]:1,3,5,6…(36) |
| Florida4 | - | 344 334 033 | 344 334 033 | - | 5 | 138 | 4:003 008 033 | 14(8) | idx[20]:4,5,6,7…(36) |
| Ohio4 | - | 559 599 259 | 559 599 259 | - | 4 | 139 | 2:009 559 | 10(6) | idx[20]:1,2,3,4…(36) |
| NewYork4 | - | 038 005 025 | 038 005 025 | - | 4 | 180 | 3:001 006 066 | 6(6) | idx[18]:1,2,3,4…(34) |
| NewJersey4 | - | 599 299 229 | 778 899 245 | - | 2 | 145 | 1:022 | 28(6) | idx[20]:1,2,5,10…(36) |
| SouthCarolina4 | - | 002 559 007 | 002 007 677 | - | 8 | 153 | 3:115 224 233 | 21(8) | idx[20]:1,2,3,4…(36) |
| Virginia4 | - | 224 229 559 | 224 377 279 | - | 3 | 164 | 4:004 377 455 | 27(6) | idx[20]:1,2,3,5…(36) |
| NorthCarolina4 | - | 229 299 044 | 299 044 224 | - | 4 | 170 | 2:001 044 | 12(8) | idx[20]:1,2,3,4…(36) |
| Indiana4 | - | 244 668 138 | 244 368 066 | - | 2 | 177 | 2:002 066 | 7(8) | idx[19]:1,2,3,5…(35) |
| Connecticut4 | - | 224 456 024 | 024 668 004 | - | 2 | 186 | 2:088 223 | 9(8) | idx[20]:2,5,6,9…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **PuertoRico4**: CU packs=`27` union=`185` top_support=`12:022` due=`022 033 088 199`
- **Michigan4**: CU packs=`27` union=`136` top_support=`11:112` due=`112 119 155 199`
- **Pennsylvania4**: CU packs=`27` union=`148` top_support=`11:007` due=`007 066 228 255`
- **Delaware4**: CU packs=`27` union=`156` top_support=`11:009` due=`009 088 223 228`
- **OntarioCanada4**: CU packs=`27` union=`158` top_support=`11:004` due=`004 044 144 244`
- **Florida4**: CU packs=`27` union=`138` top_support=`10:003` due=`003 008 009 011`
- **Ohio4**: CU packs=`27` union=`139` top_support=`10:009` due=`009 066 113 118`
- **NewYork4**: CU packs=`27` union=`180` top_support=`10:001` due=`001 007 011 066`
- **NewJersey4**: CU packs=`27` union=`145` top_support=`9:022` due=`022 114 155 339`
- **SouthCarolina4**: CU packs=`27` union=`153` top_support=`9:115` due=`115 155 224 233`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-04/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,7,10…(36)` (src `sharepacks/_predictive/2026-01-04/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `17(6)` (src `sharepacks/_predictive/2026-01-04/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,8…(36)` (src `sharepacks/_predictive/2026-01-04/Michigan4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `3(6)` (src `sharepacks/_predictive/2026-01-04/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[21]:1,2,3,5…(35)` (src `sharepacks/_predictive/2026-01-04/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-04/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[24]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-01-04/Delaware4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-04/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,5,6…(36)` (src `sharepacks/_predictive/2026-01-04/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `14(8)` (src `sharepacks/_predictive/2026-01-04/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,6,7…(36)` (src `sharepacks/_predictive/2026-01-04/Florida4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-04/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-04/Ohio4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-04/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[18]:1,2,3,4…(34)` (src `sharepacks/_predictive/2026-01-04/NewYork4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `28(6)` (src `sharepacks/_predictive/2026-01-04/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,10…(36)` (src `sharepacks/_predictive/2026-01-04/NewJersey4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `21(8)` (src `sharepacks/_predictive/2026-01-04/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-04/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `27(6)` (src `sharepacks/_predictive/2026-01-04/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-04/Virginia4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `12(8)` (src `sharepacks/_predictive/2026-01-04/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-04/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-04/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[19]:1,2,3,5…(35)` (src `sharepacks/_predictive/2026-01-04/Indiana4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `9(8)` (src `sharepacks/_predictive/2026-01-04/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,9…(36)` (src `sharepacks/_predictive/2026-01-04/Connecticut4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
