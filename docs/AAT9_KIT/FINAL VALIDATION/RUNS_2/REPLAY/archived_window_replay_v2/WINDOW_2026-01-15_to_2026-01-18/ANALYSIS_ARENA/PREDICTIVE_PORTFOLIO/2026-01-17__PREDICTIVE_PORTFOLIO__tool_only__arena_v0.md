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
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Control Center profit alerts: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Delaware4 | - | 167 259 007 | 167 249 047 | - | 3 | 219 | 4:004 009 117 | 5(6) | idx[20]:1,2,3,4…(36) |
| Ohio4 | - | 009 599 049 | 599 349 013 | - | 2 | 193 | 3:004 009 499 | 5(6) | idx[20]:2,3,4,5…(36) |
| Virginia4 | - | 449 339 033 | 339 029 001 | - | 6 | 177 | 3:004 455 599 | 5(6) | idx[20]:1,2,3,5…(36) |
| Indiana4 | - | 368 077 559 | 368 077 366 | - | 5 | 254 | 3:002 066 566 | 3(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | - | 011 559 117 | 011 115 125 | - | 3 | 171 | 4:112 117 119 | 7(8) | idx[20]:1,2,3,4…(36) |
| Connecticut4 | - | 559 599 899 | 559 589 089 | - | 4 | 186 | 3:088 389 588 | 14(8) | idx[20]:3,4,5,10…(36) |
| OntarioCanada4 | - | 244 346 044 | 346 022 255 | - | 4 | 201 | 2:004 044 | 15(6) | idx[20]:2,5,9,10…(36) |
| Pennsylvania4 | - | 244 668 344 | 244 668 024 | - | 7 | 220 | 2:007 118 | 23(6) | idx[20]:2,3,4,5…(36) |
| PuertoRico4 | - | 334 014 018 | 334 014 024 | - | 3 | 241 | 2:022 033 | 10(6) | idx[20]:2,4,5,6…(36) |
| Florida4 | - | 255 225 559 | 255 577 557 | - | 2 | 163 | 2:003 355 | 10(6) | idx[20]:1,3,4,5…(36) |
| NewYork4 | - | 377 339 368 | 377 339 368 | - | 5 | 188 | 4:001 007 377 | 18(6) | idx[20]:2,3,5,6…(36) |
| SouthCarolina4 | - | 677 005 006 | 677 005 067 | - | 3 | 188 | 3:114 224 466 | 19(6) | idx[20]:1,2,5,6…(36) |
| NorthCarolina4 | - | 224 244 225 | 224 244 477 | - | 5 | 215 | 3:001 225 277 | 26(2) | idx[22]:1,2,3,4…(36) |
| NewJersey4 | - | 001 019 499 | 001 019 499 | - | 5 | 219 | 2:022 348 | 9(8) | idx[20]:1,2,3,4…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Delaware4**: CU packs=`27` union=`219` top_support=`13:009` due=`009 088 117 223`
- **Ohio4**: CU packs=`27` union=`193` top_support=`12:009` due=`009 066 113 118`
- **Virginia4**: CU packs=`27` union=`177` top_support=`11:004` due=`004 177 199 334`
- **Indiana4**: CU packs=`27` union=`254` top_support=`11:002` due=`002 022 177 226`
- **Michigan4**: CU packs=`27` union=`171` top_support=`10:112` due=`112 119 155 199`
- **Connecticut4**: CU packs=`27` union=`186` top_support=`10:088` due=`088 099 223 228`
- **OntarioCanada4**: CU packs=`27` union=`201` top_support=`10:004` due=`004 044 144 228`
- **Pennsylvania4**: CU packs=`27` union=`220` top_support=`10:007` due=`007 066 228 255`
- **PuertoRico4**: CU packs=`27` union=`241` top_support=`10:022` due=`022 033 088 112`
- **Florida4**: CU packs=`27` union=`163` top_support=`9:003` due=`003 009 011 077`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Delaware4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Ohio4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Virginia4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `3(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Indiana4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `7(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Michigan4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `14(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,10…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Connecticut4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `15(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,9,10…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `23(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `10(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/Florida4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `18(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/NewYork4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `19(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `26(2)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `9(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-17/NewJersey4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
