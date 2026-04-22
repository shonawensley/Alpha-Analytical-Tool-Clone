# Analysis Arena Predictive Portfolio — D=2026-01-21

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
- Control Center profit alerts: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| OntarioCanada4 | - | 244 044 004 | 044 468 448 | - | 8 | 185 | 4:004 044 144 | 5(6) | idx[20]:2,3,5,9…(36) |
| Connecticut4 | - | 006 255 355 | 355 001 668 | - | 5 | 200 | 2:088 588 | 2(6) | idx[20]:1,2,3,4…(36) |
| Ohio4 | - | 077 007 078 | 007 078 224 | - | 4 | 201 | 4:004 009 499 | 5(6) | idx[20]:2,3,4,5…(36) |
| Virginia4 | - | 133 339 033 | 133 339 033 | - | 7 | 205 | 4:003 004 009 | 14(8) | idx[20]:2,3,4,5…(36) |
| Delaware4 | - | 255 559 336 | 259 055 003 | - | 4 | 224 | 3:009 223 559 | 5(6) | idx[20]:1,2,3,4…(36) |
| PuertoRico4 | - | 168 668 336 | 168 334 138 | - | 5 | 234 | 2:022 033 | 10(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | - | 224 477 017 | 224 017 247 | - | 4 | 180 | 2:066 155 | 28(6) | idx[20]:2,3,5,6…(36) |
| Florida4 | - | 259 378 008 | 259 008 388 | - | 3 | 186 | 2:003 355 | 29(6) | idx[20]:1,3,4,5…(36) |
| SouthCarolina4 | - | 009 599 005 | 599 005 039 | - | 4 | 199 | 2:114 233 | 8(8) | idx[20]:1,2,3,4…(36) |
| NewYork4 | - | 113 337 115 | 113 337 115 | - | 4 | 202 | 1:001 | 27(6) | idx[20]:2,3,6,8…(36) |
| NewJersey4 | - | 001 559 004 | 001 004 014 | - | 4 | 204 | 3:001 022 077 | 2(6) | idx[20]:1,2,3,5…(36) |
| Pennsylvania4 | - | 559 599 178 | 559 178 334 | - | 2 | 210 | 3:007 033 168 | 23(6) | idx[20]:1,3,4,6…(36) |
| NorthCarolina4 | - | 778 006 366 | 006 024 119 | - | 8 | 225 | 3:001 225 228 | 27(6) | idx[20]:2,5,7,8…(36) |
| Indiana4 | - | 001 077 244 | 001 147 014 | - | 4 | 240 | 2:002 007 | 6(6) | idx[20]:2,3,4,5…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **OntarioCanada4**: CU packs=`27` union=`185` top_support=`11:004` due=`004 044 144 228`
- **Connecticut4**: CU packs=`27` union=`200` top_support=`11:088` due=`088 099 223 228`
- **Ohio4**: CU packs=`27` union=`201` top_support=`11:009` due=`009 066 113 118`
- **Virginia4**: CU packs=`27` union=`205` top_support=`10:004` due=`004 177 199 334`
- **Delaware4**: CU packs=`27` union=`224` top_support=`10:009` due=`009 088 117 223`
- **PuertoRico4**: CU packs=`27` union=`234` top_support=`10:022` due=`022 033 088 112`
- **Michigan4**: CU packs=`27` union=`180` top_support=`9:066` due=`066 112 119 155`
- **Florida4**: CU packs=`27` union=`186` top_support=`9:003` due=`003 009 011 077`
- **SouthCarolina4**: CU packs=`27` union=`199` top_support=`9:114` due=`114 115 155 233`
- **NewYork4**: CU packs=`27` union=`202` top_support=`9:001` due=`001 007 011 066`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,9…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `2(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Ohio4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `14(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Virginia4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Delaware4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `28(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Michigan4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `29(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Florida4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `8(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `27(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,6,8…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/NewYork4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `2(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `23(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `27(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,7,8…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `6(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21/Indiana4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
