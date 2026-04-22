# Analysis Arena Predictive Portfolio — D=2026-01-06

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
- Control Center profit alerts: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Ohio4 | - | 088 008 559 | 088 008 559 | - | 4 | 172 | 3:002 009 559 | 3(6) | idx[20]:1,2,3,4…(36) |
| PuertoRico4 | - | 068 003 006 | 068 003 268 | - | 6 | 235 | 3:022 033 225 | 10(6) | idx[20]:3,4,5,6…(36) |
| SouthCarolina4 | - | 007 599 667 | 007 005 669 | - | 5 | 193 | 3:115 224 566 | 6(6) | idx[20]:1,2,5,6…(36) |
| NewYork4 | - | 008 005 025 | 008 005 025 | - | 4 | 196 | 3:001 011 066 | 6(6) | idx[20]:1,2,3,4…(36) |
| Delaware4 | - | 334 003 118 | 003 118 158 | - | 5 | 202 | 4:004 009 088 | 5(6) | idx[20]:2,4,5,6…(36) |
| Florida4 | - | 334 033 346 | 334 033 346 | - | 4 | 170 | 2:003 136 | 24(8) | idx[20]:3,4,5,6…(36) |
| Pennsylvania4 | - | 059 559 455 | 059 559 455 | - | 5 | 203 | 3:007 059 557 | 3(6) | idx[20]:1,2,3,5…(36) |
| Michigan4 | - | 118 144 668 | 118 144 156 | - | 4 | 159 | 2:112 119 | 18(6) | idx[20]:2,5,6,7…(36) |
| NewJersey4 | - | 778 088 788 | 778 788 889 | - | 4 | 174 | 3:022 077 114 | 27(6) | idx[20]:2,4,5,10…(36) |
| NorthCarolina4 | - | 224 229 299 | 224 229 299 | - | 5 | 189 | 3:001 044 244 | 12(8) | idx[20]:1,2,3,5…(36) |
| Connecticut4 | - | 224 244 2244 | 224 478 044 | - | 2 | 196 | 2:088 228 | 30(8) | idx[20]:5,6,7,10…(36) |
| Virginia4 | - | 224 559 189 | 189 009 377 | - | 5 | 215 | 2:004 377 | 14(8) | idx[20]:3,4,5,7…(36) |
| OntarioCanada4 | - | 014 015 177 | 014 015 244 | - | 3 | 226 | 3:004 044 244 | 9(8) | idx[20]:2,5,6,7…(36) |
| Indiana4 | - | 244 366 066 | 244 066 014 | - | 2 | 232 | 2:002 177 | 6(6) | idx[20]:2,3,4,5…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Ohio4**: CU packs=`27` union=`172` top_support=`12:009` due=`009 066 113 118`
- **PuertoRico4**: CU packs=`27` union=`235` top_support=`12:022` due=`022 033 088 199`
- **SouthCarolina4**: CU packs=`27` union=`193` top_support=`11:115` due=`115 155 224 233`
- **NewYork4**: CU packs=`27` union=`196` top_support=`11:001` due=`001 007 011 066`
- **Delaware4**: CU packs=`27` union=`202` top_support=`11:009` due=`009 088 223 228`
- **Florida4**: CU packs=`27` union=`170` top_support=`10:003` due=`003 009 011 077`
- **Pennsylvania4**: CU packs=`27` union=`203` top_support=`10:007` due=`007 066 228 255`
- **Michigan4**: CU packs=`27` union=`159` top_support=`9:112` due=`112 119 155 199`
- **NewJersey4**: CU packs=`27` union=`174` top_support=`9:022` due=`022 114 155 339`
- **NorthCarolina4**: CU packs=`27` union=`189` top_support=`9:001` due=`001 009 044 225`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Ohio4**: B24 `3(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Ohio4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `6(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/NewYork4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Delaware4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `24(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Florida4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `3(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `18(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,7…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Michigan4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `27(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,10…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/NewJersey4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `12(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `30(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:5,6,7,10…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `14(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,7…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Virginia4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `9(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,7…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `6(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-06/Indiana4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
