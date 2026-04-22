# Analysis Arena Predictive Portfolio — D=2026-01-04

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
- Control Center profit alerts: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| PuertoRico4 | - | 344 224 268 | 026 003 226 | - | 4 | 227 | 4:022 033 088 | 10(6) | idx[20]:3,4,7,8…(36) |
| Pennsylvania4 | - | 559 599 5599 | 559 059 055 | - | 4 | 200 | 2:007 255 | 3(6) | idx[22]:1,2,3,5…(36) |
| Florida4 | - | 344 334 033 | 344 334 033 | - | 5 | 178 | 3:003 008 033 | 14(8) | idx[20]:4,5,6,7…(36) |
| Delaware4 | - | 449 559 004 | 004 058 055 | - | 5 | 186 | 3:004 009 559 | 5(6) | idx[22]:1,2,4,5…(36) |
| OntarioCanada4 | - | 007 047 118 | 007 047 118 | - | 6 | 214 | 3:004 167 244 | 5(6) | idx[20]:3,5,6,8…(36) |
| Ohio4 | - | 559 599 259 | 559 599 259 | - | 4 | 153 | 1:009 | 3(6) | idx[20]:1,2,3,4…(36) |
| NewYork4 | - | 038 005 025 | 038 005 025 | - | 4 | 236 | 3:001 006 066 | 6(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | - | 168 668 156 | 168 156 013 | - | 5 | 154 | 1:112 | 18(6) | idx[20]:2,4,5,6…(36) |
| NewJersey4 | - | 599 299 229 | 778 899 245 | - | 2 | 187 | 3:022 077 889 | 27(6) | idx[20]:2,5,10,11…(36) |
| NorthCarolina4 | - | 229 299 044 | 299 044 224 | - | 4 | 192 | 4:001 009 044 | 12(8) | idx[20]:1,2,3,4…(36) |
| Virginia4 | - | 224 229 559 | 224 377 279 | - | 3 | 209 | 4:004 177 377 | 27(6) | idx[20]:2,3,5,6…(36) |
| SouthCarolina4 | - | 002 559 007 | 002 007 677 | - | 8 | 220 | 3:115 224 233 | 21(8) | idx[20]:2,3,4,5…(36) |
| Indiana4 | - | 244 668 138 | 244 368 066 | - | 2 | 223 | 2:002 177 | 18(6) | idx[20]:2,3,5,6…(36) |
| Connecticut4 | - | 224 456 024 | 024 668 004 | - | 2 | 241 | 1:088 | 9(8) | idx[20]:1,2,5,9…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **PuertoRico4**: CU packs=`27` union=`227` top_support=`13:022` due=`022 033 088 199`
- **Pennsylvania4**: CU packs=`27` union=`200` top_support=`12:007` due=`007 066 228 255`
- **Florida4**: CU packs=`27` union=`178` top_support=`11:003` due=`003 008 009 011`
- **Delaware4**: CU packs=`27` union=`186` top_support=`11:009` due=`009 088 223 228`
- **OntarioCanada4**: CU packs=`27` union=`214` top_support=`11:004` due=`004 044 144 244`
- **Ohio4**: CU packs=`27` union=`153` top_support=`10:009` due=`009 066 113 118`
- **NewYork4**: CU packs=`27` union=`236` top_support=`10:001` due=`001 007 011 066`
- **Michigan4**: CU packs=`27` union=`154` top_support=`9:112` due=`112 119 155 199`
- **NewJersey4**: CU packs=`27` union=`187` top_support=`9:022` due=`022 114 155 339`
- **NorthCarolina4**: CU packs=`27` union=`192` top_support=`9:001` due=`001 009 044 225`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,7,8…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `3(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `14(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,6,7…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Florida4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Delaware4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,5,6,8…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `3(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Ohio4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/NewYork4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `18(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Michigan4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `27(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,10,11…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/NewJersey4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `12(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `27(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Virginia4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `21(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `18(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Indiana4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `9(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,9…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-04/Connecticut4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
