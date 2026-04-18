# Analysis Arena Predictive Portfolio — D=2026-03-18

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
- Control Center profit alerts: `sharepacks/_predictive/2026-03-18/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Ohio4 | - | 559 069 006 | 069 006 099 | - | 7 | 193 | 3:004 009 559 | 9(8) | idx[20]:2,3,4,5…(36) |
| Delaware4 | - | 099 399 599 | 399 039 389 | - | 3 | 182 | 3:009 099 559 | 14(8) | idx[20]:1,2,5,6…(36) |
| Michigan4 | - | 001 559 044 | 001 055 267 | - | 4 | 193 | 3:011 066 088 | 6(6) | idx[20]:1,2,3,4…(36) |
| NewYork4 | - | 035 667 036 | 035 667 366 | - | 4 | 192 | 2:007 066 | 8(8) | idx[20]:2,3,4,5…(36) |
| Pennsylvania4 | - | 077 067 034 | 077 067 034 | - | 5 | 205 | 2:007 077 | 3(6) | idx[20]:3,4,5,6…(36) |
| Indiana4 | - | 559 599 224 | 559 599 569 | - | 3 | 231 | 3:177 299 599 | 12(8) | idx[20]:2,5,6,9…(36) |
| SouthCarolina4 | - | 344 455 003 | 344 455 003 | - | 4 | 186 | 2:114 445 | 34(6) | idx[20]:2,4,5,6…(36) |
| Virginia4 | - | 559 255 225 | 235 055 025 | - | 2 | 187 | 4:004 055 255 | 3(6) | idx[20]:1,3,4,5…(36) |
| NewJersey4 | - | 499 118 038 | 499 038 013 | - | 5 | 204 | 2:022 149 | 35(2) | idx[24]:1,2,3,5…(36) |
| OntarioCanada4 | - | 223 138 148 | 138 148 113 | - | 2 | 212 | 1:004 | 8(8) | idx[20]:1,5,8,10…(36) |
| Connecticut4 | - | 344 559 244 | 344 244 399 | - | 5 | 213 | 3:099 136 399 | 24(8) | idx[20]:2,4,5,6…(36) |
| NorthCarolina4 | - | 112 117 177 | 122 299 388 | - | 4 | 217 | 2:009 299 | 29(6) | idx[22]:5,6,8,10…(36) |
| Florida4 | - | 006 224 114 | 006 224 025 | - | 4 | 218 | 2:003 118 | 7(8) | idx[20]:1,2,3,4…(36) |
| PuertoRico4 | - | 244 006 144 | 244 006 024 | - | 4 | 226 | 3:001 003 006 | 28(6) | idx[20]:2,3,4,5…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Ohio4**: CU packs=`27` union=`193` top_support=`12:009` due=`009 066 113 118`
- **Delaware4**: CU packs=`27` union=`182` top_support=`11:009` due=`009 033 088 117`
- **Michigan4**: CU packs=`27` union=`193` top_support=`11:066` due=`066 077 119 144`
- **NewYork4**: CU packs=`27` union=`192` top_support=`10:007` due=`007 011 066 488`
- **Pennsylvania4**: CU packs=`27` union=`205` top_support=`10:007` due=`007 009 066 228`
- **Indiana4**: CU packs=`27` union=`231` top_support=`10:177` due=`177 226 288 337`
- **SouthCarolina4**: CU packs=`27` union=`186` top_support=`9:114` due=`114 115 155 233`
- **Virginia4**: CU packs=`27` union=`187` top_support=`9:004` due=`004 115 177 199`
- **NewJersey4**: CU packs=`27` union=`204` top_support=`9:022` due=`022 155 335 339`
- **OntarioCanada4**: CU packs=`27` union=`212` top_support=`9:004` due=`004 044 055 228`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Ohio4**: B24 `9(8)` (src `sharepacks/_predictive/2026-03-18/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-18/Ohio4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `14(8)` (src `sharepacks/_predictive/2026-03-18/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,6…(36)` (src `sharepacks/_predictive/2026-03-18/Delaware4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `6(6)` (src `sharepacks/_predictive/2026-03-18/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-18/Michigan4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `8(8)` (src `sharepacks/_predictive/2026-03-18/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-18/NewYork4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `3(6)` (src `sharepacks/_predictive/2026-03-18/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-18/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `12(8)` (src `sharepacks/_predictive/2026-03-18/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,9…(36)` (src `sharepacks/_predictive/2026-03-18/Indiana4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `34(6)` (src `sharepacks/_predictive/2026-03-18/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-18/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `3(6)` (src `sharepacks/_predictive/2026-03-18/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-18/Virginia4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `35(2)` (src `sharepacks/_predictive/2026-03-18/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[24]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-03-18/NewJersey4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `8(8)` (src `sharepacks/_predictive/2026-03-18/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,5,8,10…(36)` (src `sharepacks/_predictive/2026-03-18/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `24(8)` (src `sharepacks/_predictive/2026-03-18/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-18/Connecticut4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `29(6)` (src `sharepacks/_predictive/2026-03-18/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:5,6,8,10…(36)` (src `sharepacks/_predictive/2026-03-18/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `7(8)` (src `sharepacks/_predictive/2026-03-18/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-18/Florida4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `28(6)` (src `sharepacks/_predictive/2026-03-18/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-18/PuertoRico4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
