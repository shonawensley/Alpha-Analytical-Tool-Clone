# Analysis Arena Predictive Portfolio — D=2026-03-15

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
- Control Center profit alerts: `sharepacks/_predictive/2026-03-15/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| OntarioCanada4 | - | 449 388 368 | 449 388 138 | - | 3 | 174 | 2:004 238 | 5(6) | idx[20]:1,3,5,8…(36) |
| Virginia4 | - | 559 259 599 | 559 259 889 | - | 3 | 198 | 2:004 455 | 5(6) | idx[20]:1,2,3,4…(36) |
| Ohio4 | - | 069 099 599 | 069 099 599 | - | 4 | 170 | 3:004 009 066 | 9(8) | idx[20]:2,4,5,6…(36) |
| Delaware4 | - | 559 049 599 | 559 049 007 | - | 9 | 196 | 2:009 559 | 14(8) | idx[20]:1,5,6,7…(36) |
| Indiana4 | - | 599 224 669 | 599 005 559 | - | 7 | 205 | 3:177 299 699 | 20(6) | idx[20]:1,2,5,6…(36) |
| NorthCarolina4 | - | 388 138 368 | 388 138 368 | - | 3 | 228 | 2:009 344 | 18(6) | idx[20]:3,4,5,8…(36) |
| Michigan4 | - | 455 044 008 | 008 448 048 | - | 3 | 192 | 3:011 066 077 | 9(8) | idx[20]:1,2,3,4…(36) |
| SouthCarolina4 | - | 244 559 077 | 077 036 027 | - | 2 | 200 | 2:114 249 | 10(6) | idx[20]:1,2,3,4…(36) |
| NewJersey4 | - | 244 099 004 | 244 099 024 | - | 6 | 201 | 2:022 244 | 12(8) | idx[20]:2,3,5,6…(36) |
| PuertoRico4 | - | 677 445 047 | 677 445 047 | - | 4 | 201 | 2:001 006 | 12(8) | idx[20]:1,2,3,4…(36) |
| Florida4 | - | 699 224 668 | 699 668 469 | - | 4 | 208 | 2:003 118 | 7(8) | idx[20]:2,3,4,5…(36) |
| NewYork4 | - | 668 039 012 | 039 012 001 | - | 5 | 216 | 4:002 007 011 | 18(6) | idx[20]:2,3,4,5…(36) |
| Pennsylvania4 | - | 366 559 244 | 244 346 338 | - | 2 | 218 | 1:007 | 11(8) | idx[22]:2,3,5,6…(36) |
| Connecticut4 | - | 559 689 346 | 559 689 044 | - | 5 | 226 | 2:099 599 | 24(8) | idx[20]:2,5,6,7…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **OntarioCanada4**: CU packs=`27` union=`174` top_support=`12:004` due=`004 044 055 228`
- **Virginia4**: CU packs=`27` union=`198` top_support=`11:004` due=`004 115 177 199`
- **Ohio4**: CU packs=`27` union=`170` top_support=`10:009` due=`009 066 113 118`
- **Delaware4**: CU packs=`27` union=`196` top_support=`10:009` due=`009 033 088 117`
- **Indiana4**: CU packs=`27` union=`205` top_support=`10:177` due=`177 226 288 337`
- **NorthCarolina4**: CU packs=`27` union=`228` top_support=`10:009` due=`009 225 299 344`
- **Michigan4**: CU packs=`27` union=`192` top_support=`9:066` due=`066 077 119 144`
- **SouthCarolina4**: CU packs=`27` union=`200` top_support=`9:114` due=`114 115 155 233`
- **NewJersey4**: CU packs=`27` union=`201` top_support=`9:022` due=`022 155 335 339`
- **PuertoRico4**: CU packs=`27` union=`201` top_support=`9:001` due=`001 003 011 033`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-15/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,5,8…(36)` (src `sharepacks/_predictive/2026-03-15/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-15/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-15/Virginia4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `9(8)` (src `sharepacks/_predictive/2026-03-15/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-15/Ohio4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `14(8)` (src `sharepacks/_predictive/2026-03-15/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,5,6,7…(36)` (src `sharepacks/_predictive/2026-03-15/Delaware4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `20(6)` (src `sharepacks/_predictive/2026-03-15/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,6…(36)` (src `sharepacks/_predictive/2026-03-15/Indiana4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `18(6)` (src `sharepacks/_predictive/2026-03-15/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,8…(36)` (src `sharepacks/_predictive/2026-03-15/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `9(8)` (src `sharepacks/_predictive/2026-03-15/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-15/Michigan4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `10(6)` (src `sharepacks/_predictive/2026-03-15/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-15/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `12(8)` (src `sharepacks/_predictive/2026-03-15/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-15/NewJersey4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `12(8)` (src `sharepacks/_predictive/2026-03-15/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-15/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `7(8)` (src `sharepacks/_predictive/2026-03-15/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-15/Florida4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `18(6)` (src `sharepacks/_predictive/2026-03-15/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-15/NewYork4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `11(8)` (src `sharepacks/_predictive/2026-03-15/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-15/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `24(8)` (src `sharepacks/_predictive/2026-03-15/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,7…(36)` (src `sharepacks/_predictive/2026-03-15/Connecticut4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
