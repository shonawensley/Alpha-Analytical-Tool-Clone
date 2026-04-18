# Analysis Arena Predictive Portfolio — D=2026-01-16

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-16/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Delaware4 | - | 009 249 059 | 059 013 | - | 4 | 163 | 1:009 | 5(6) | idx[20]:1,2,3,5…(36) |
| Connecticut4 | - | 899 599 389 | 899 089 889 | - | 4 | 149 | 2:088 389 | 13(6) | idx[22]:5,6,7,13…(36) |
| OntarioCanada4 | - | 003 039 049 | 003 039 049 | - | 7 | 162 | 2:004 009 | 5(6) | idx[20]:1,3,4,5…(36) |
| Ohio4 | - | 599 009 049 | 677 349 499 | - | 3 | 169 | 3:009 349 559 | 5(6) | idx[24]:3,4,5,6…(36) |
| Virginia4 | - | 449 599 033 | 339 459 059 | - | 7 | 122 | 3:004 455 499 | 5(6) | idx[22]:1,5,6,8…(36) |
| PuertoRico4 | - | 244 334 224 | 334 024 014 | - | 4 | 169 | 3:022 033 088 | 10(6) | idx[20]:1,2,3,4…(36) |
| Florida4 | - | 225 577 255 | 577 255 178 | - | 2 | 132 | 3:003 077 377 | 10(6) | idx[19]:3,4,5,6…(35) |
| Michigan4 | - | 344 245 559 | 245 114 011 | - | 3 | 147 | 4:112 117 155 | 2(6) | idx[20]:2,3,4,5…(36) |
| SouthCarolina4 | - | 677 678 014 | 677 678 014 | - | 4 | 148 | 2:115 566 | 9(8) | idx[20]:1,2,5,6…(36) |
| NewJersey4 | - | 001 008 019 | 019 018 088 | - | 5 | 152 | 1:022 | 7(8) | idx[20]:1,2,4,7…(36) |
| NewYork4 | - | 337 377 334 | 337 377 336 | - | 5 | 152 | 2:001 377 | 8(8) | idx[20]:2,3,5,6…(36) |
| Pennsylvania4 | - | 244 344 044 | 344 044 689 | - | 5 | 171 | 3:007 044 244 | 10(6) | idx[20]:1,2,3,4…(36) |
| NorthCarolina4 | - | 224 344 255 | 224 344 244 | - | 6 | 172 | 1:001 | 34(6) | idx[20]:1,2,3,4…(36) |
| Indiana4 | - | 368 599 366 | 368 366 339 | - | 4 | 194 | 3:002 336 368 | 23(6) | idx[20]:1,2,3,5…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Delaware4**: CU packs=`27` union=`163` top_support=`13:009` due=`009 088 117 223`
- **Connecticut4**: CU packs=`27` union=`149` top_support=`12:088` due=`088 099 223 228`
- **OntarioCanada4**: CU packs=`27` union=`162` top_support=`12:004` due=`004 044 144 228`
- **Ohio4**: CU packs=`27` union=`169` top_support=`12:009` due=`009 066 113 118`
- **Virginia4**: CU packs=`27` union=`122` top_support=`11:004` due=`004 177 199 445`
- **PuertoRico4**: CU packs=`27` union=`169` top_support=`10:022` due=`022 033 088 112`
- **Florida4**: CU packs=`27` union=`132` top_support=`9:003` due=`003 009 011 077`
- **Michigan4**: CU packs=`27` union=`147` top_support=`9:112` due=`112 119 155 199`
- **SouthCarolina4**: CU packs=`27` union=`148` top_support=`9:115` due=`115 155 224 233`
- **NewJersey4**: CU packs=`27` union=`152` top_support=`9:022` due=`022 114 155 339`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-16/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-16/Delaware4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `13(6)` (src `sharepacks/_predictive/2026-01-16/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:5,6,7,13…(36)` (src `sharepacks/_predictive/2026-01-16/Connecticut4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-16/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-16/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-16/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[24]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-01-16/Ohio4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-16/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,5,6,8…(36)` (src `sharepacks/_predictive/2026-01-16/Virginia4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-16/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-16/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-16/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[19]:3,4,5,6…(35)` (src `sharepacks/_predictive/2026-01-16/Florida4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `2(6)` (src `sharepacks/_predictive/2026-01-16/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-16/Michigan4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `9(8)` (src `sharepacks/_predictive/2026-01-16/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,6…(36)` (src `sharepacks/_predictive/2026-01-16/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-16/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,7…(36)` (src `sharepacks/_predictive/2026-01-16/NewJersey4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `8(8)` (src `sharepacks/_predictive/2026-01-16/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-01-16/NewYork4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-16/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-16/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `34(6)` (src `sharepacks/_predictive/2026-01-16/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-16/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `23(6)` (src `sharepacks/_predictive/2026-01-16/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-16/Indiana4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
