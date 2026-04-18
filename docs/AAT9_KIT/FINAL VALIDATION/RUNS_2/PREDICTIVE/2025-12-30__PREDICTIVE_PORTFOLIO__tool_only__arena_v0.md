# Analysis Arena Predictive Portfolio — D=2025-12-30

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
- Control Center profit alerts: `sharepacks/_predictive/2025-12-30/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Ohio4 | - | 677 057 599 | 057 077 699 | - | 3 | 167 | 2:009 077 | 5(6) | idx[20]:2,3,4,5…(36) |
| Delaware4 | - | 344 113 244 | 344 113 017 | - | 4 | 173 | 2:004 009 | 5(6) | idx[20]:1,2,4,5…(36) |
| Florida4 | - | 778 177 677 | 778 677 133 | - | 3 | 137 | 3:003 008 388 | 11(8) | idx[20]:4,5,6,10…(36) |
| PuertoRico4 | - | 344 134 244 | 344 244 299 | - | 6 | 204 | 3:022 199 224 | 10(6) | idx[20]:5,10,11,12…(36) |
| Pennsylvania4 | - | 339 113 138 | 339 113 138 | - | 3 | 147 | 2:007 138 | 23(6) | idx[20]:1,3,6,8…(36) |
| Michigan4 | - | 599 244 136 | 244 136 355 | - | 4 | 150 | 3:112 155 355 | 4(6) | idx[20]:2,3,4,5…(36) |
| NewJersey4 | - | 224 118 299 | 224 012 229 | - | 6 | 153 | 1:022 | 11(8) | idx[20]:1,2,5,6…(36) |
| Virginia4 | - | 399 133 177 | 399 133 113 | - | 4 | 158 | 3:004 133 177 | 17(6) | idx[20]:1,5,6,8…(36) |
| SouthCarolina4 | - | 189 599 009 | 189 017 011 | - | 4 | 163 | 2:115 224 | 24(8) | idx[20]:1,2,5,6…(36) |
| OntarioCanada4 | - | 188 225 114 | 188 022 255 | - | 4 | 165 | 3:004 022 244 | 20(6) | idx[20]:1,3,5,6…(36) |
| NewYork4 | - | 016 778 677 | 016 778 001 | - | 2 | 168 | 2:001 066 | 6(6) | idx[20]:2,3,6,9…(36) |
| Indiana4 | - | 066 116 068 | 066 068 677 | - | 4 | 170 | 3:002 066 226 | 7(8) | idx[19]:1,2,3,4…(33) |
| NorthCarolina4 | - | 224 003 005 | 224 003 004 | - | 3 | 178 | 3:001 044 244 | 12(8) | idx[20]:1,2,3,4…(36) |
| Connecticut4 | - | 559 011 000 | 011 117 009 | - | 5 | 185 | 2:009 088 | 8(8) | idx[20]:1,2,3,4…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Ohio4**: CU packs=`27` union=`167` top_support=`11:009` due=`009 066 113 114`
- **Delaware4**: CU packs=`27` union=`173` top_support=`11:009` due=`009 088 223 228`
- **Florida4**: CU packs=`27` union=`137` top_support=`10:003` due=`003 008 009 011`
- **PuertoRico4**: CU packs=`27` union=`204` top_support=`10:022` due=`022 033 088 199`
- **Pennsylvania4**: CU packs=`27` union=`147` top_support=`9:007` due=`007 228 255 277`
- **Michigan4**: CU packs=`27` union=`150` top_support=`9:112` due=`112 119 155 199`
- **NewJersey4**: CU packs=`27` union=`153` top_support=`9:022` due=`022 155 336 339`
- **Virginia4**: CU packs=`27` union=`158` top_support=`9:004` due=`004 115 177 199`
- **SouthCarolina4**: CU packs=`27` union=`163` top_support=`9:115` due=`115 155 224 288`
- **OntarioCanada4**: CU packs=`27` union=`165` top_support=`9:004` due=`004 044 144 244`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Ohio4**: B24 `5(6)` (src `sharepacks/_predictive/2025-12-30/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2025-12-30/Ohio4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2025-12-30/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2025-12-30/Delaware4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `11(8)` (src `sharepacks/_predictive/2025-12-30/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,6,10…(36)` (src `sharepacks/_predictive/2025-12-30/Florida4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2025-12-30/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:5,10,11,12…(36)` (src `sharepacks/_predictive/2025-12-30/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `23(6)` (src `sharepacks/_predictive/2025-12-30/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,6,8…(36)` (src `sharepacks/_predictive/2025-12-30/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `4(6)` (src `sharepacks/_predictive/2025-12-30/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2025-12-30/Michigan4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `11(8)` (src `sharepacks/_predictive/2025-12-30/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,6…(36)` (src `sharepacks/_predictive/2025-12-30/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `17(6)` (src `sharepacks/_predictive/2025-12-30/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,5,6,8…(36)` (src `sharepacks/_predictive/2025-12-30/Virginia4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `24(8)` (src `sharepacks/_predictive/2025-12-30/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,6…(36)` (src `sharepacks/_predictive/2025-12-30/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `20(6)` (src `sharepacks/_predictive/2025-12-30/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,5,6…(36)` (src `sharepacks/_predictive/2025-12-30/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive/2025-12-30/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,6,9…(36)` (src `sharepacks/_predictive/2025-12-30/NewYork4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `7(8)` (src `sharepacks/_predictive/2025-12-30/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[19]:1,2,3,4…(33)` (src `sharepacks/_predictive/2025-12-30/Indiana4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `12(8)` (src `sharepacks/_predictive/2025-12-30/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2025-12-30/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `8(8)` (src `sharepacks/_predictive/2025-12-30/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2025-12-30/Connecticut4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
