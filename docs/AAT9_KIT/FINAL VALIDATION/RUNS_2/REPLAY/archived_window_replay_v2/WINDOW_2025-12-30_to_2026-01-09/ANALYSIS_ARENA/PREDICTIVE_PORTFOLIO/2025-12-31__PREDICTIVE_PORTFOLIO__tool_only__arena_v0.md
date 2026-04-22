# Analysis Arena Predictive Portfolio — D=2025-12-31

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
- Control Center profit alerts: `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| NorthCarolina4 | - | 003 224 034 | 003 224 034 | - | 4 | 219 | 4:001 004 006 | 5(6) | idx[20]:1,2,3,4…(36) |
| OntarioCanada4 | - | 188 022 114 | 188 022 255 | - | 7 | 188 | 3:004 144 244 | 5(6) | idx[20]:2,4,5,6…(36) |
| Ohio4 | - | 599 009 559 | 009 559 057 | - | 4 | 205 | 3:009 077 559 | 7(8) | idx[20]:1,2,3,4…(36) |
| NewJersey4 | - | 299 224 118 | 224 128 289 | - | 3 | 189 | 2:022 389 | 28(6) | idx[20]:2,5,6,10…(36) |
| Florida4 | - | 677 116 077 | 677 077 013 | - | 4 | 208 | 4:003 008 011 | 4(6) | idx[22]:3,4,5,6…(36) |
| Delaware4 | - | 244 144 499 | 244 144 014 | - | 2 | 234 | 2:009 114 | 5(6) | idx[20]:2,3,5,6…(36) |
| PuertoRico4 | - | 344 244 113 | 344 224 246 | - | 4 | 266 | 3:022 199 224 | 10(6) | idx[20]:5,10,11,13…(36) |
| SouthCarolina4 | - | 189 066 138 | 006 018 688 | - | 6 | 180 | 2:011 115 | 2(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | - | 136 244 599 | 136 335 036 | - | 5 | 184 | 2:112 155 | 21(8) | idx[20]:2,3,4,5…(36) |
| Pennsylvania4 | - | 339 138 559 | 339 138 559 | - | 3 | 188 | 1:007 | 23(6) | idx[20]:1,3,5,6…(36) |
| Virginia4 | - | 177 224 133 | 224 133 113 | - | 4 | 189 | 4:004 177 339 | 23(6) | idx[20]:1,5,6,13…(36) |
| Indiana4 | - | 677 244 668 | 677 244 066 | - | 4 | 201 | 2:002 368 | 16(2) | idx[22]:1,2,3,4…(36) |
| Connecticut4 | - | 011 559 003 | 011 368 678 | - | 5 | 214 | 4:001 003 008 | 8(8) | idx[20]:1,2,3,4…(36) |
| NewYork4 | - | 778 677 116 | 677 016 668 | - | 3 | 214 | 2:001 066 | 6(6) | idx[20]:2,3,6,7…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **NorthCarolina4**: CU packs=`27` union=`219` top_support=`13:001` due=`001 009 044 225`
- **OntarioCanada4**: CU packs=`27` union=`188` top_support=`11:004` due=`004 044 144 244`
- **Ohio4**: CU packs=`27` union=`205` top_support=`11:009` due=`009 066 113 114`
- **NewJersey4**: CU packs=`27` union=`189` top_support=`10:022` due=`022 155 336 339`
- **Florida4**: CU packs=`27` union=`208` top_support=`10:003` due=`003 008 009 011`
- **Delaware4**: CU packs=`27` union=`234` top_support=`10:009` due=`009 088 223 228`
- **PuertoRico4**: CU packs=`27` union=`266` top_support=`10:022` due=`022 033 088 199`
- **SouthCarolina4**: CU packs=`27` union=`180` top_support=`9:115` due=`115 155 224 288`
- **Michigan4**: CU packs=`27` union=`184` top_support=`9:112` due=`112 119 155 199`
- **Pennsylvania4**: CU packs=`27` union=`188` top_support=`9:007` due=`007 228 255 277`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **NorthCarolina4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `7(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Ohio4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `28(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,10…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `4(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:3,4,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Florida4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Delaware4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:5,10,11,13…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `2(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `21(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Michigan4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `23(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,5,6…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `23(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,5,6,13…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Virginia4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `16(2)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Indiana4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `8(8)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/Connecticut4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,6,7…(36)` (src `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-31/NewYork4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
