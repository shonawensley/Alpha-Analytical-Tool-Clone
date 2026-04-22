# Analysis Arena Predictive Portfolio — D=2026-01-08

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
- Control Center profit alerts: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| NewYork4 | - | 005 008 256 | 005 001 245 | - | 6 | 172 | 2:001 011 | 2(6) | idx[22]:1,2,3,4…(36) |
| PuertoRico4 | - | 068 006 244 | 068 028 008 | - | 1 | 253 | 3:022 033 225 | 10(6) | idx[20]:2,3,4,5…(36) |
| NewJersey4 | - | 778 189 089 | 778 189 089 | - | 4 | 183 | 3:022 077 088 | 10(6) | idx[20]:1,2,3,4…(36) |
| SouthCarolina4 | - | 599 244 005 | 244 005 559 | - | 2 | 186 | 2:115 224 | 6(6) | idx[20]:1,2,3,5…(36) |
| Delaware4 | - | 033 334 003 | 033 034 118 | - | 7 | 212 | 3:009 011 559 | 5(6) | idx[20]:2,4,5,6…(36) |
| OntarioCanada4 | - | 224 015 006 | 224 015 006 | - | 3 | 230 | 4:004 044 224 | 12(8) | idx[20]:1,2,3,4…(36) |
| Florida4 | - | 334 346 3345 | 334 346 335 | - | 4 | 157 | 2:003 334 | 33(6) | idx[20]:4,5,6,9…(36) |
| Connecticut4 | - | 224 229 2244 | 224 448 248 | - | 3 | 175 | 2:088 228 | 34(6) | idx[20]:5,7,10,13…(36) |
| NorthCarolina4 | - | 299 244 559 | 299 244 446 | - | 3 | 193 | 3:001 009 044 | 31(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | - | 344 019 144 | 344 019 144 | - | 5 | 198 | 3:112 117 119 | 9(8) | idx[20]:2,3,5,6…(36) |
| Ohio4 | - | 889 559 599 | 889 299 788 | - | 4 | 201 | 4:009 088 559 | 4(6) | idx[20]:1,3,4,5…(36) |
| Pennsylvania4 | - | 599 009 445 | 009 445 001 | - | 6 | 217 | 2:007 557 | 5(6) | idx[20]:2,3,5,6…(36) |
| Virginia4 | - | 559 024 244 | 559 024 134 | - | 8 | 231 | 2:004 136 | 9(8) | idx[20]:3,5,6,8…(36) |
| Indiana4 | - | 244 066 669 | 066 669 344 | - | 3 | 246 | 3:002 066 266 | 12(8) | idx[20]:1,3,5,6…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **NewYork4**: CU packs=`27` union=`172` top_support=`13:001` due=`001 007 011 066`
- **PuertoRico4**: CU packs=`27` union=`253` top_support=`13:022` due=`022 033 199 299`
- **NewJersey4**: CU packs=`27` union=`183` top_support=`11:022` due=`022 114 155 339`
- **SouthCarolina4**: CU packs=`27` union=`186` top_support=`11:115` due=`115 155 224 233`
- **Delaware4**: CU packs=`27` union=`212` top_support=`10:009` due=`009 088 223 228`
- **OntarioCanada4**: CU packs=`27` union=`230` top_support=`10:004` due=`004 044 144 228`
- **Florida4**: CU packs=`27` union=`157` top_support=`9:003` due=`003 009 011 077`
- **Connecticut4**: CU packs=`27` union=`175` top_support=`9:088` due=`088 099 223 228`
- **NorthCarolina4**: CU packs=`27` union=`193` top_support=`9:001` due=`001 009 044 225`
- **Michigan4**: CU packs=`27` union=`198` top_support=`9:112` due=`112 119 155 199`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **NewYork4**: B24 `2(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/NewYork4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `10(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/NewJersey4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `6(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Delaware4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `12(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `33(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,6,9…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Florida4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `34(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:5,7,10,13…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Connecticut4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `31(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `9(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Michigan4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `4(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Ohio4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `9(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,5,6,8…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Virginia4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `12(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08/Indiana4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
