# Analysis Arena Predictive Portfolio — D=2026-01-15

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-15/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Delaware4 | - | 059 249 299 | 059 599 013 | - | 4 | 168 | 2:004 009 | 5(6) | idx[20]:1,2,4,5…(36) |
| Virginia4 | - | 449 599 459 | 449 599 459 | - | 9 | 148 | 3:004 499 599 | 5(6) | idx[22]:1,5,6,7…(36) |
| NewYork4 | - | 677 377 337 | 677 377 337 | - | 4 | 139 | 2:001 677 | 6(6) | idx[20]:2,3,5,6…(36) |
| Ohio4 | - | 599 039 559 | 599 039 349 | - | 3 | 162 | 3:009 559 599 | 14(8) | idx[20]:2,5,6,9…(36) |
| OntarioCanada4 | - | 225 039 049 | 039 049 022 | - | 8 | 170 | 3:002 004 009 | 12(8) | idx[20]:1,3,4,5…(36) |
| PuertoRico4 | - | 088 004 034 | 088 034 003 | - | 6 | 171 | 3:022 033 088 | 10(6) | idx[20]:1,2,3,4…(36) |
| Florida4 | - | 177 577 224 | 577 224 257 | - | 2 | 128 | 2:003 077 | 10(6) | idx[18]:2,3,4,5…(32) |
| Michigan4 | - | 114 344 014 | 114 344 014 | - | 6 | 143 | 3:112 155 559 | 9(8) | idx[20]:1,2,4,5…(36) |
| SouthCarolina4 | - | 449 678 004 | 449 004 467 | - | 3 | 153 | 1:115 | 9(8) | idx[20]:2,5,6,8…(36) |
| NewJersey4 | - | 001 136 179 | 001 136 179 | - | 8 | 155 | 3:011 022 136 | 18(6) | idx[20]:1,2,4,6…(36) |
| Pennsylvania4 | - | 244 446 234 | 244 446 239 | - | 5 | 170 | 2:007 244 | 23(6) | idx[20]:1,3,6,11…(36) |
| Connecticut4 | - | 899 599 559 | 899 599 359 | - | 2 | 171 | 3:088 099 899 | 34(6) | idx[20]:5,6,7,11…(36) |
| NorthCarolina4 | - | 224 344 255 | 224 344 225 | - | 5 | 177 | 2:001 225 | 34(6) | idx[20]:1,2,3,4…(36) |
| Indiana4 | - | 599 339 667 | 339 368 038 | - | 4 | 195 | 2:002 336 | 23(6) | idx[20]:1,3,6,7…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Delaware4**: CU packs=`27` union=`168` top_support=`12:009` due=`009 088 117 223`
- **Virginia4**: CU packs=`27` union=`148` top_support=`11:004` due=`004 177 199 445`
- **NewYork4**: CU packs=`27` union=`139` top_support=`10:001` due=`001 007 011 066`
- **Ohio4**: CU packs=`27` union=`162` top_support=`10:009` due=`009 066 113 118`
- **OntarioCanada4**: CU packs=`27` union=`170` top_support=`10:004` due=`004 044 144 228`
- **PuertoRico4**: CU packs=`27` union=`171` top_support=`10:022` due=`022 033 088 112`
- **Florida4**: CU packs=`27` union=`128` top_support=`9:003` due=`003 009 011 077`
- **Michigan4**: CU packs=`27` union=`143` top_support=`9:112` due=`112 119 155 199`
- **SouthCarolina4**: CU packs=`27` union=`153` top_support=`9:115` due=`115 155 224 233`
- **NewJersey4**: CU packs=`27` union=`155` top_support=`9:022` due=`022 114 155 339`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-15/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-01-15/Delaware4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-15/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,5,6,7…(36)` (src `sharepacks/_predictive/2026-01-15/Virginia4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-15/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-01-15/NewYork4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `14(8)` (src `sharepacks/_predictive/2026-01-15/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,9…(36)` (src `sharepacks/_predictive/2026-01-15/Ohio4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `12(8)` (src `sharepacks/_predictive/2026-01-15/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-15/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-15/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-15/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-15/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[18]:2,3,4,5…(32)` (src `sharepacks/_predictive/2026-01-15/Florida4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `9(8)` (src `sharepacks/_predictive/2026-01-15/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-01-15/Michigan4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `9(8)` (src `sharepacks/_predictive/2026-01-15/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,8…(36)` (src `sharepacks/_predictive/2026-01-15/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `18(6)` (src `sharepacks/_predictive/2026-01-15/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,6…(36)` (src `sharepacks/_predictive/2026-01-15/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `23(6)` (src `sharepacks/_predictive/2026-01-15/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,6,11…(36)` (src `sharepacks/_predictive/2026-01-15/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `34(6)` (src `sharepacks/_predictive/2026-01-15/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:5,6,7,11…(36)` (src `sharepacks/_predictive/2026-01-15/Connecticut4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `34(6)` (src `sharepacks/_predictive/2026-01-15/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-15/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `23(6)` (src `sharepacks/_predictive/2026-01-15/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,6,7…(36)` (src `sharepacks/_predictive/2026-01-15/Indiana4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
