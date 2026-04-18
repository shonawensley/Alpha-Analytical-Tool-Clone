# Analysis Arena Predictive Portfolio — D=2026-01-17

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-17/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Delaware4 | - | 167 259 007 | 167 249 047 | - | 3 | 162 | 2:004 009 | 5(6) | idx[20]:1,2,3,4…(36) |
| Ohio4 | - | 009 599 049 | 599 349 013 | - | 2 | 173 | 1:009 | 5(6) | idx[20]:3,4,5,6…(36) |
| Connecticut4 | - | 559 599 899 | 559 589 089 | - | 4 | 164 | 1:088 | 14(8) | idx[20]:4,5,6,11…(36) |
| Michigan4 | - | 011 559 117 | 011 115 125 | - | 3 | 141 | 3:112 117 155 | 7(8) | idx[20]:2,3,4,5…(36) |
| PuertoRico4 | - | 334 014 018 | 334 014 024 | - | 3 | 189 | 3:003 022 033 | 10(6) | idx[20]:2,3,4,5…(36) |
| Florida4 | - | 255 225 559 | 255 577 557 | - | 2 | 132 | 2:003 355 | 10(6) | idx[17]:1,3,4,5…(33) |
| Virginia4 | - | 449 339 033 | 339 029 001 | - | 6 | 143 | 2:004 455 | 12(8) | idx[20]:1,2,5,9…(36) |
| NewYork4 | - | 377 339 368 | 377 339 368 | - | 5 | 145 | 3:001 007 677 | 6(6) | idx[20]:2,3,5,6…(36) |
| SouthCarolina4 | - | 677 005 006 | 677 005 067 | - | 3 | 148 | 2:114 466 | 9(8) | idx[20]:1,2,5,6…(36) |
| NewJersey4 | - | 001 019 499 | 001 019 499 | - | 5 | 156 | 2:022 348 | 7(8) | idx[20]:1,2,3,4…(36) |
| OntarioCanada4 | - | 244 346 044 | 346 022 255 | - | 4 | 157 | 1:004 | 15(6) | idx[20]:1,4,5,10…(36) |
| NorthCarolina4 | - | 224 244 225 | 224 244 477 | - | 5 | 167 | 2:001 477 | 28(6) | idx[19]:1,2,4,5…(35) |
| Pennsylvania4 | - | 244 668 344 | 244 668 024 | - | 7 | 179 | 1:007 | 18(6) | idx[20]:1,2,3,4…(36) |
| Indiana4 | - | 368 077 559 | 368 077 366 | - | 5 | 204 | 3:002 177 226 | 7(8) | idx[20]:1,2,3,4…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Delaware4**: CU packs=`27` union=`162` top_support=`13:009` due=`009 088 117 223`
- **Ohio4**: CU packs=`27` union=`173` top_support=`12:009` due=`009 066 113 118`
- **Connecticut4**: CU packs=`27` union=`164` top_support=`11:088` due=`088 099 223 228`
- **Michigan4**: CU packs=`27` union=`141` top_support=`10:112` due=`112 119 155 199`
- **PuertoRico4**: CU packs=`27` union=`189` top_support=`10:022` due=`022 033 088 112`
- **Florida4**: CU packs=`27` union=`132` top_support=`9:003` due=`003 009 011 077`
- **Virginia4**: CU packs=`27` union=`143` top_support=`9:004` due=`004 177 199 334`
- **NewYork4**: CU packs=`27` union=`145` top_support=`9:001` due=`001 007 011 066`
- **SouthCarolina4**: CU packs=`27` union=`148` top_support=`9:114` due=`114 115 155 224`
- **NewJersey4**: CU packs=`27` union=`156` top_support=`9:022` due=`022 114 155 339`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-17/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-17/Delaware4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-17/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-01-17/Ohio4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `14(8)` (src `sharepacks/_predictive/2026-01-17/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,6,11…(36)` (src `sharepacks/_predictive/2026-01-17/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-17/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-17/Michigan4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-17/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-17/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-17/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[17]:1,3,4,5…(33)` (src `sharepacks/_predictive/2026-01-17/Florida4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `12(8)` (src `sharepacks/_predictive/2026-01-17/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,9…(36)` (src `sharepacks/_predictive/2026-01-17/Virginia4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-17/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-01-17/NewYork4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `9(8)` (src `sharepacks/_predictive/2026-01-17/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,6…(36)` (src `sharepacks/_predictive/2026-01-17/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-17/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-17/NewJersey4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `15(6)` (src `sharepacks/_predictive/2026-01-17/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,4,5,10…(36)` (src `sharepacks/_predictive/2026-01-17/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `28(6)` (src `sharepacks/_predictive/2026-01-17/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[19]:1,2,4,5…(35)` (src `sharepacks/_predictive/2026-01-17/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `18(6)` (src `sharepacks/_predictive/2026-01-17/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-17/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-17/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-17/Indiana4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
