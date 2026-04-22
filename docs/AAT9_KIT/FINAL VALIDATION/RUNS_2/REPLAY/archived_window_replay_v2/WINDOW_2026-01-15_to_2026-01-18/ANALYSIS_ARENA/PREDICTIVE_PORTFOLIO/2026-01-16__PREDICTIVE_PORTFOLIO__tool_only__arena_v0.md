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
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Control Center profit alerts: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Delaware4 | - | 009 249 059 | 059 013 | - | 4 | 192 | 3:009 117 559 | 5(6) | idx[20]:1,2,3,5…(36) |
| Ohio4 | - | 599 009 049 | 677 349 499 | - | 3 | 205 | 3:004 009 559 | 5(6) | idx[22]:2,3,4,5…(36) |
| Virginia4 | - | 449 599 033 | 339 459 059 | - | 7 | 172 | 3:004 455 499 | 5(6) | idx[22]:1,3,5,6…(36) |
| OntarioCanada4 | - | 003 039 049 | 003 039 049 | - | 7 | 210 | 3:004 009 044 | 13(6) | idx[20]:2,3,4,5…(36) |
| NewYork4 | - | 337 377 334 | 337 377 336 | - | 5 | 199 | 3:001 011 377 | 8(8) | idx[20]:2,3,5,6…(36) |
| Pennsylvania4 | - | 244 344 044 | 344 044 689 | - | 5 | 214 | 3:007 044 344 | 23(6) | idx[20]:2,3,4,5…(36) |
| PuertoRico4 | - | 244 334 224 | 334 024 014 | - | 4 | 225 | 3:022 033 088 | 10(6) | idx[20]:1,2,3,4…(36) |
| Florida4 | - | 225 577 255 | 577 255 178 | - | 2 | 172 | 3:003 077 355 | 10(6) | idx[20]:3,4,5,6…(36) |
| Connecticut4 | - | 899 599 389 | 899 089 889 | - | 4 | 176 | 2:088 388 | 29(6) | idx[22]:5,6,11,13…(36) |
| SouthCarolina4 | - | 677 678 014 | 677 678 014 | - | 4 | 191 | 3:115 224 566 | 9(8) | idx[20]:1,2,5,6…(36) |
| Michigan4 | - | 344 245 559 | 245 114 011 | - | 3 | 200 | 4:112 117 155 | 2(6) | idx[20]:1,2,3,4…(36) |
| NorthCarolina4 | - | 224 344 255 | 224 344 244 | - | 6 | 221 | 2:001 225 | 26(2) | idx[22]:1,2,3,4…(36) |
| NewJersey4 | - | 001 008 019 | 019 018 088 | - | 5 | 228 | 1:022 | 7(8) | idx[20]:1,2,6,7…(36) |
| Indiana4 | - | 368 599 366 | 368 366 339 | - | 4 | 235 | 2:002 368 | 23(6) | idx[20]:2,3,5,6…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Delaware4**: CU packs=`27` union=`192` top_support=`13:009` due=`009 088 117 223`
- **Ohio4**: CU packs=`27` union=`205` top_support=`12:009` due=`009 066 113 118`
- **Virginia4**: CU packs=`27` union=`172` top_support=`11:004` due=`004 177 199 445`
- **OntarioCanada4**: CU packs=`27` union=`210` top_support=`11:004` due=`004 044 144 228`
- **NewYork4**: CU packs=`27` union=`199` top_support=`10:001` due=`001 007 011 066`
- **Pennsylvania4**: CU packs=`27` union=`214` top_support=`10:007` due=`007 066 228 255`
- **PuertoRico4**: CU packs=`27` union=`225` top_support=`10:022` due=`022 033 088 112`
- **Florida4**: CU packs=`27` union=`172` top_support=`9:003` due=`003 009 011 077`
- **Connecticut4**: CU packs=`27` union=`176` top_support=`9:088` due=`088 099 223 228`
- **SouthCarolina4**: CU packs=`27` union=`191` top_support=`9:115` due=`115 155 224 233`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Delaware4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Ohio4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Virginia4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `13(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `8(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/NewYork4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `23(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `10(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Florida4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `29(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:5,6,11,13…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Connecticut4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `9(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `2(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Michigan4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `26(2)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `7(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,6,7…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `23(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-16/Indiana4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
