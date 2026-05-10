# Analysis Arena Predictive Portfolio — D=2026-03-21

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
- Control Center profit alerts: `sharepacks/_predictive/2026-03-21/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Delaware4 | - | 001 599 016 | 001 599 016 | - | 5 | 192 | 4:009 099 399 | 2(6) | idx[20]:1,2,3,4…(36) |
| OntarioCanada4 | - | 368 559 055 | 368 559 355 | - | 3 | 217 | 2:004 244 | 5(6) | idx[20]:1,3,4,5…(36) |
| Pennsylvania4 | - | 446 447 478 | 447 014 088 | - | 4 | 219 | 2:007 477 | 28(6) | idx[20]:1,3,5,6…(36) |
| NewJersey4 | - | 455 559 499 | 455 003 005 | - | 3 | 156 | 2:022 449 | 5(6) | idx[22]:1,2,3,4…(36) |
| NewYork4 | - | 066 667 013 | 066 667 013 | - | 11 | 174 | 3:007 066 338 | 8(8) | idx[20]:3,4,5,6…(36) |
| Virginia4 | - | 225 022 255 | 022 268 256 | - | 5 | 193 | 4:004 022 225 | 10(6) | idx[20]:1,3,4,5…(36) |
| SouthCarolina4 | - | 559 455 155 | 455 155 003 | - | 6 | 199 | 4:114 155 455 | 4(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | - | 567 001 599 | 567 445 556 | - | 7 | 205 | 3:011 066 455 | 2(6) | idx[20]:1,2,3,4…(36) |
| Connecticut4 | - | 113 224 355 | 113 355 123 | - | 6 | 210 | 2:099 116 | 18(6) | idx[20]:3,4,6,7…(36) |
| Florida4 | - | 244 246 114 | 246 066 224 | - | 4 | 211 | 3:003 118 224 | 22(8) | idx[20]:2,3,4,5…(36) |
| Ohio4 | - | 699 002 018 | 002 018 024 | - | 6 | 214 | 3:004 009 118 | 8(8) | idx[20]:3,5,6,8…(36) |
| Indiana4 | - | 559 455 002 | 559 455 002 | - | 6 | 223 | 3:122 177 337 | 7(8) | idx[20]:1,2,3,5…(36) |
| PuertoRico4 | - | 224 244 388 | 224 368 013 | - | 2 | 230 | 4:001 003 006 | 11(8) | idx[20]:1,2,3,4…(36) |
| NorthCarolina4 | - | 499 117 889 | 499 889 348 | - | 9 | 244 | 3:009 225 299 | 31(6) | idx[20]:5,9,10,13…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Delaware4**: CU packs=`27` union=`192` top_support=`11:009` due=`009 033 088 117`
- **OntarioCanada4**: CU packs=`27` union=`217` top_support=`11:004` due=`004 044 228 244`
- **Pennsylvania4**: CU packs=`27` union=`219` top_support=`10:007` due=`007 009 066 228`
- **NewJersey4**: CU packs=`27` union=`156` top_support=`9:022` due=`022 155 335 339`
- **NewYork4**: CU packs=`27` union=`174` top_support=`9:007` due=`007 011 066 488`
- **Virginia4**: CU packs=`27` union=`193` top_support=`9:004` due=`004 005 115 199`
- **SouthCarolina4**: CU packs=`27` union=`199` top_support=`9:114` due=`114 115 155 233`
- **Michigan4**: CU packs=`27` union=`205` top_support=`9:066` due=`066 077 119 144`
- **Connecticut4**: CU packs=`27` union=`210` top_support=`9:099` due=`099 116 228 668`
- **Florida4**: CU packs=`27` union=`211` top_support=`9:003` due=`003 009 011 118`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Delaware4**: B24 `2(6)` (src `sharepacks/_predictive/2026-03-21/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-21/Delaware4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-21/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-21/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `28(6)` (src `sharepacks/_predictive/2026-03-21/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-21/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-21/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-21/NewJersey4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `8(8)` (src `sharepacks/_predictive/2026-03-21/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-21/NewYork4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `10(6)` (src `sharepacks/_predictive/2026-03-21/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-21/Virginia4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `4(6)` (src `sharepacks/_predictive/2026-03-21/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-21/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `2(6)` (src `sharepacks/_predictive/2026-03-21/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-21/Michigan4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `18(6)` (src `sharepacks/_predictive/2026-03-21/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,6,7…(36)` (src `sharepacks/_predictive/2026-03-21/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `22(8)` (src `sharepacks/_predictive/2026-03-21/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-21/Florida4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `8(8)` (src `sharepacks/_predictive/2026-03-21/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,5,6,8…(36)` (src `sharepacks/_predictive/2026-03-21/Ohio4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `7(8)` (src `sharepacks/_predictive/2026-03-21/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-03-21/Indiana4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `11(8)` (src `sharepacks/_predictive/2026-03-21/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-21/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `31(6)` (src `sharepacks/_predictive/2026-03-21/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:5,9,10,13…(36)` (src `sharepacks/_predictive/2026-03-21/NorthCarolina4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
