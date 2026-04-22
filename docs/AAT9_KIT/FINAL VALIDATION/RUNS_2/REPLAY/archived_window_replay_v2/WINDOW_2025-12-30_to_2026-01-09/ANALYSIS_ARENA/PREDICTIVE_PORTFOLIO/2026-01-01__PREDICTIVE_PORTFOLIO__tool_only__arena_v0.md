# Analysis Arena Predictive Portfolio — D=2026-01-01

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
- Control Center profit alerts: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Ohio4 | - | 055 559 068 | 055 559 068 | - | 6 | 183 | 1:009 | 3(6) | idx[20]:1,2,3,5…(36) |
| NorthCarolina4 | - | 224 003 223 | 224 223 229 | - | 4 | 212 | 4:001 009 044 | 11(8) | idx[20]:1,2,3,4…(36) |
| PuertoRico4 | - | 344 113 224 | 224 002 001 | - | 5 | 273 | 3:022 224 225 | 10(6) | idx[20]:2,7,10,11…(36) |
| NewJersey4 | - | 299 778 118 | 299 778 899 | - | 2 | 165 | 2:022 225 | 28(6) | idx[20]:1,2,10,15…(36) |
| Connecticut4 | - | 011 388 368 | 011 368 008 | - | 8 | 211 | 4:001 003 008 | 4(6) | idx[20]:2,3,4,5…(36) |
| Delaware4 | - | 244 014 144 | 244 014 144 | - | 2 | 217 | 1:009 | 9(8) | idx[20]:1,2,5,6…(36) |
| SouthCarolina4 | - | 118 011 138 | 118 138 068 | - | 4 | 173 | 3:011 115 224 | 2(6) | idx[20]:1,2,3,4…(36) |
| Virginia4 | - | 224 177 133 | 224 137 113 | - | 4 | 190 | 3:004 177 339 | 22(8) | idx[20]:2,3,4,5…(36) |
| Florida4 | - | 599 138 559 | 138 077 133 | - | 4 | 199 | 4:003 008 011 | 11(8) | idx[24]:3,4,5,6…(36) |
| Michigan4 | - | 006 133 599 | 006 133 069 | - | 8 | 203 | 3:112 155 559 | 18(6) | idx[20]:1,2,3,4…(36) |
| OntarioCanada4 | - | 114 022 255 | 114 022 255 | - | 6 | 208 | 2:004 244 | 19(6) | idx[20]:5,6,7,9…(36) |
| Indiana4 | - | 677 244 668 | 677 368 056 | - | 3 | 221 | 3:002 007 177 | 7(8) | idx[20]:2,3,4,6…(36) |
| NewYork4 | - | 778 677 6677 | 778 677 678 | - | 4 | 221 | 3:001 006 066 | 6(6) | idx[20]:2,3,5,6…(36) |
| Pennsylvania4 | - | 559 359 339 | 559 359 339 | - | 3 | 226 | 2:007 138 | 23(6) | idx[20]:3,4,5,11…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Ohio4**: CU packs=`27` union=`183` top_support=`12:009` due=`009 066 113 114`
- **NorthCarolina4**: CU packs=`27` union=`212` top_support=`11:001` due=`001 009 044 225`
- **PuertoRico4**: CU packs=`27` union=`273` top_support=`11:022` due=`022 033 088 199`
- **NewJersey4**: CU packs=`27` union=`165` top_support=`10:022` due=`022 114 155 339`
- **Connecticut4**: CU packs=`27` union=`211` top_support=`10:088` due=`088 099 223 228`
- **Delaware4**: CU packs=`27` union=`217` top_support=`10:009` due=`009 088 223 228`
- **SouthCarolina4**: CU packs=`27` union=`173` top_support=`9:115` due=`115 155 224 288`
- **Virginia4**: CU packs=`27` union=`190` top_support=`9:004` due=`004 177 199 377`
- **Florida4**: CU packs=`27` union=`199` top_support=`9:003` due=`003 008 009 011`
- **Michigan4**: CU packs=`27` union=`203` top_support=`9:112` due=`112 119 155 199`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Ohio4**: B24 `3(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Ohio4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `11(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,7,10,11…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `28(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,10,15…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `4(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `9(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Delaware4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `2(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `22(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Virginia4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `11(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[24]:3,4,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Florida4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `18(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Michigan4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `19(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:5,6,7,9…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `7(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Indiana4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/NewYork4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `23(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,11…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-01/Pennsylvania4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
