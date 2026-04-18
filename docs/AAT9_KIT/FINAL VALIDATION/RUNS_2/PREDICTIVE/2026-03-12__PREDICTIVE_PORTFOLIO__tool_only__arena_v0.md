# Analysis Arena Predictive Portfolio — D=2026-03-12

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
- Control Center profit alerts: `sharepacks/_predictive/2026-03-12/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Indiana4 | - | 788 015 688 | 788 015 688 | - | 3 | 206 | 3:177 288 677 | 20(6) | idx[20]:2,3,4,5…(36) |
| Virginia4 | - | 599 559 099 | 099 005 358 | - | 3 | 169 | 3:004 055 455 | 5(6) | idx[22]:1,2,3,4…(36) |
| SouthCarolina4 | - | 029 667 069 | 029 667 678 | - | 5 | 197 | 2:114 466 | 19(6) | idx[20]:1,2,5,6…(36) |
| PuertoRico4 | - | 559 449 667 | 449 667 077 | - | 5 | 202 | 1:001 | 2(6) | idx[20]:1,2,3,4…(36) |
| NorthCarolina4 | - | 009 344 388 | 346 339 445 | - | 5 | 233 | 3:009 344 366 | 5(6) | idx[20]:3,4,5,10…(36) |
| Ohio4 | - | 033 338 013 | 033 338 013 | - | 9 | 189 | 2:009 113 | 8(8) | idx[20]:2,3,4,5…(36) |
| Pennsylvania4 | - | 559 233 224 | 005 008 238 | - | 3 | 198 | 3:002 007 238 | 11(8) | idx[20]:1,3,4,5…(36) |
| OntarioCanada4 | - | 449 244 388 | 449 388 238 | - | 6 | 168 | 2:004 044 | 31(6) | idx[20]:1,4,5,9…(36) |
| Michigan4 | - | 455 688 488 | 488 058 014 | - | 3 | 174 | 3:008 011 066 | 19(6) | idx[20]:2,4,5,6…(36) |
| Delaware4 | - | 499 599 047 | 499 344 129 | - | 3 | 183 | 3:009 117 559 | 17(6) | idx[20]:1,5,6,8…(36) |
| NewYork4 | - | 224 368 559 | 224 368 366 | - | 2 | 187 | 3:007 368 388 | 4(6) | idx[20]:2,3,4,5…(36) |
| Connecticut4 | - | 368 168 006 | 368 168 006 | - | 5 | 206 | 1:099 | 24(8) | idx[20]:2,5,6,8…(36) |
| Florida4 | - | 224 077 499 | 077 499 022 | - | 3 | 206 | 3:003 011 244 | 10(6) | idx[20]:2,3,4,5…(36) |
| NewJersey4 | - | 177 244 006 | 244 006 024 | - | 7 | 227 | 3:022 244 445 | 12(8) | idx[20]:2,3,5,6…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Indiana4**: CU packs=`27` union=`206` top_support=`12:177` due=`177 226 288 337`
- **Virginia4**: CU packs=`27` union=`169` top_support=`11:004` due=`004 115 177 199`
- **SouthCarolina4**: CU packs=`27` union=`197` top_support=`11:114` due=`114 115 155 233`
- **PuertoRico4**: CU packs=`27` union=`202` top_support=`11:001` due=`001 011 033 088`
- **NorthCarolina4**: CU packs=`27` union=`233` top_support=`11:009` due=`009 225 299 344`
- **Ohio4**: CU packs=`27` union=`189` top_support=`10:009` due=`009 066 113 118`
- **Pennsylvania4**: CU packs=`27` union=`198` top_support=`10:007` due=`007 009 066 228`
- **OntarioCanada4**: CU packs=`27` union=`168` top_support=`9:004` due=`004 044 055 228`
- **Michigan4**: CU packs=`27` union=`174` top_support=`9:066` due=`066 077 119 144`
- **Delaware4**: CU packs=`27` union=`183` top_support=`9:009` due=`009 033 088 117`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Indiana4**: B24 `20(6)` (src `sharepacks/_predictive/2026-03-12/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-12/Indiana4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-12/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-12/Virginia4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `19(6)` (src `sharepacks/_predictive/2026-03-12/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,6…(36)` (src `sharepacks/_predictive/2026-03-12/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `2(6)` (src `sharepacks/_predictive/2026-03-12/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-12/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-12/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,10…(36)` (src `sharepacks/_predictive/2026-03-12/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `8(8)` (src `sharepacks/_predictive/2026-03-12/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-12/Ohio4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `11(8)` (src `sharepacks/_predictive/2026-03-12/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-12/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `31(6)` (src `sharepacks/_predictive/2026-03-12/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,4,5,9…(36)` (src `sharepacks/_predictive/2026-03-12/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `19(6)` (src `sharepacks/_predictive/2026-03-12/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-12/Michigan4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `17(6)` (src `sharepacks/_predictive/2026-03-12/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,5,6,8…(36)` (src `sharepacks/_predictive/2026-03-12/Delaware4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `4(6)` (src `sharepacks/_predictive/2026-03-12/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-12/NewYork4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `24(8)` (src `sharepacks/_predictive/2026-03-12/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,8…(36)` (src `sharepacks/_predictive/2026-03-12/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `10(6)` (src `sharepacks/_predictive/2026-03-12/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-12/Florida4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `12(8)` (src `sharepacks/_predictive/2026-03-12/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-12/NewJersey4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
