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
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Control Center profit alerts: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Delaware4 | - | 059 249 299 | 059 599 013 | - | 4 | 203 | 3:004 009 559 | 5(6) | idx[20]:2,3,4,5…(36) |
| Virginia4 | - | 449 599 459 | 449 599 459 | - | 9 | 183 | 3:004 445 499 | 5(6) | idx[22]:1,5,6,7…(36) |
| OntarioCanada4 | - | 225 039 049 | 039 049 022 | - | 8 | 209 | 2:004 009 | 12(8) | idx[20]:3,4,5,8…(36) |
| Ohio4 | - | 599 039 559 | 599 039 349 | - | 3 | 198 | 2:009 559 | 14(8) | idx[20]:3,4,5,6…(36) |
| NewYork4 | - | 677 377 337 | 677 377 337 | - | 4 | 200 | 3:001 011 377 | 8(8) | idx[20]:2,3,6,7…(36) |
| Pennsylvania4 | - | 244 446 234 | 244 446 239 | - | 5 | 208 | 3:007 244 344 | 23(6) | idx[20]:1,3,4,6…(36) |
| PuertoRico4 | - | 088 004 034 | 088 034 003 | - | 6 | 217 | 2:022 033 | 10(6) | idx[20]:1,2,3,4…(36) |
| Florida4 | - | 177 577 224 | 577 224 257 | - | 2 | 179 | 2:003 077 | 10(6) | idx[20]:2,3,4,5…(36) |
| Connecticut4 | - | 899 599 559 | 899 599 359 | - | 2 | 184 | 2:088 389 | 34(6) | idx[20]:3,5,6,7…(36) |
| Michigan4 | - | 114 344 014 | 114 344 014 | - | 6 | 191 | 2:112 155 | 2(6) | idx[20]:1,2,3,4…(36) |
| SouthCarolina4 | - | 449 678 004 | 449 004 467 | - | 3 | 198 | 3:115 224 334 | 9(8) | idx[20]:2,5,6,7…(36) |
| NewJersey4 | - | 001 136 179 | 001 136 179 | - | 8 | 202 | 1:022 | 22(8) | idx[20]:1,2,3,4…(36) |
| NorthCarolina4 | - | 224 344 255 | 224 344 225 | - | 5 | 226 | 2:001 225 | 12(8) | idx[20]:1,2,3,4…(36) |
| Indiana4 | - | 599 339 667 | 339 368 038 | - | 4 | 229 | 1:002 | 23(6) | idx[20]:1,3,5,6…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Delaware4**: CU packs=`27` union=`203` top_support=`12:009` due=`009 088 117 223`
- **Virginia4**: CU packs=`27` union=`183` top_support=`11:004` due=`004 177 199 445`
- **OntarioCanada4**: CU packs=`27` union=`209` top_support=`11:004` due=`004 044 144 228`
- **Ohio4**: CU packs=`27` union=`198` top_support=`10:009` due=`009 066 113 118`
- **NewYork4**: CU packs=`27` union=`200` top_support=`10:001` due=`001 007 011 066`
- **Pennsylvania4**: CU packs=`27` union=`208` top_support=`10:007` due=`007 066 228 255`
- **PuertoRico4**: CU packs=`27` union=`217` top_support=`10:022` due=`022 033 088 112`
- **Florida4**: CU packs=`27` union=`179` top_support=`9:003` due=`003 009 011 077`
- **Connecticut4**: CU packs=`27` union=`184` top_support=`9:088` due=`088 099 223 228`
- **Michigan4**: CU packs=`27` union=`191` top_support=`9:112` due=`112 119 155 199`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Delaware4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,5,6,7…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Virginia4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `12(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,8…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `14(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Ohio4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `8(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,6,7…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/NewYork4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `23(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `10(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Florida4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `34(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,5,6,7…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `2(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Michigan4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `9(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,7…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `22(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/NewJersey4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `12(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `23(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15/Indiana4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
