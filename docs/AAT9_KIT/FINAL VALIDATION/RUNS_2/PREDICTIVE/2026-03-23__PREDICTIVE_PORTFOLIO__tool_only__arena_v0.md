# Analysis Arena Predictive Portfolio — D=2026-03-23

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
- Control Center profit alerts: `sharepacks/_predictive/2026-03-23/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| OntarioCanada4 | - | 559 368 055 | 559 368 077 | - | 3 | 195 | 1:004 | 5(6) | idx[20]:1,2,3,4…(36) |
| Delaware4 | - | 011 001 038 | 001 038 066 | - | 5 | 188 | 3:009 035 559 | 2(6) | idx[20]:1,2,3,4…(36) |
| NewYork4 | - | 066 667 006 | 066 667 006 | - | 10 | 176 | 2:007 066 | 8(8) | idx[20]:2,3,4,5…(36) |
| NewJersey4 | - | 244 344 001 | 344 001 014 | - | 3 | 177 | 3:022 339 459 | 2(6) | idx[20]:1,2,3,4…(36) |
| Connecticut4 | - | 113 025 117 | 113 025 117 | - | 4 | 193 | 4:099 112 116 | 17(6) | idx[20]:1,3,4,5…(36) |
| Michigan4 | - | 344 445 055 | 055 013 | - | 6 | 197 | 4:011 066 144 | 9(8) | idx[20]:2,3,4,5…(36) |
| Pennsylvania4 | - | 448 449 446 | 448 449 446 | - | 6 | 198 | 2:007 088 | 12(8) | idx[20]:3,5,8,12…(36) |
| Florida4 | - | 224 066 114 | 224 124 012 | - | 2 | 202 | 3:003 011 118 | 7(8) | idx[20]:2,3,4,5…(36) |
| Ohio4 | - | 224 667 128 | 224 667 128 | - | 6 | 210 | 3:009 118 559 | 7(8) | idx[20]:2,3,5,6…(36) |
| Virginia4 | - | 225 559 133 | 559 133 003 | - | 7 | 210 | 3:004 005 599 | 3(6) | idx[20]:1,3,4,5…(36) |
| PuertoRico4 | - | 338 224 244 | 338 007 368 | - | 3 | 220 | 4:001 006 033 | 2(6) | idx[20]:1,2,3,4…(36) |
| SouthCarolina4 | - | 559 255 055 | 055 558 568 | - | 3 | 220 | 3:114 155 559 | 5(6) | idx[20]:2,3,4,5…(36) |
| Indiana4 | - | 559 259 004 | 559 259 002 | - | 3 | 238 | 4:033 177 337 | 7(8) | idx[20]:2,3,4,5…(36) |
| NorthCarolina4 | - | 499 889 599 | 499 116 489 | - | 7 | 251 | 3:009 299 499 | 31(6) | idx[20]:5,10,15,16…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **OntarioCanada4**: CU packs=`27` union=`195` top_support=`11:004` due=`004 044 228 244`
- **Delaware4**: CU packs=`27` union=`188` top_support=`10:009` due=`009 033 088 117`
- **NewYork4**: CU packs=`27` union=`176` top_support=`9:007` due=`007 011 066 115`
- **NewJersey4**: CU packs=`27` union=`177` top_support=`9:022` due=`022 155 335 339`
- **Connecticut4**: CU packs=`27` union=`193` top_support=`9:099` due=`099 116 228 668`
- **Michigan4**: CU packs=`27` union=`197` top_support=`9:066` due=`066 077 119 144`
- **Pennsylvania4**: CU packs=`27` union=`198` top_support=`9:007` due=`007 009 088 228`
- **Florida4**: CU packs=`27` union=`202` top_support=`9:003` due=`003 009 011 118`
- **Ohio4**: CU packs=`27` union=`210` top_support=`9:009` due=`009 066 113 118`
- **Virginia4**: CU packs=`27` union=`210` top_support=`9:004` due=`004 005 115 199`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-23/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-23/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `2(6)` (src `sharepacks/_predictive/2026-03-23/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-23/Delaware4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `8(8)` (src `sharepacks/_predictive/2026-03-23/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-23/NewYork4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `2(6)` (src `sharepacks/_predictive/2026-03-23/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-23/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `17(6)` (src `sharepacks/_predictive/2026-03-23/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-23/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `9(8)` (src `sharepacks/_predictive/2026-03-23/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-23/Michigan4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `12(8)` (src `sharepacks/_predictive/2026-03-23/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,5,8,12…(36)` (src `sharepacks/_predictive/2026-03-23/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `7(8)` (src `sharepacks/_predictive/2026-03-23/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-23/Florida4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `7(8)` (src `sharepacks/_predictive/2026-03-23/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-23/Ohio4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `3(6)` (src `sharepacks/_predictive/2026-03-23/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-23/Virginia4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `2(6)` (src `sharepacks/_predictive/2026-03-23/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-23/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-23/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-23/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `7(8)` (src `sharepacks/_predictive/2026-03-23/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-23/Indiana4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `31(6)` (src `sharepacks/_predictive/2026-03-23/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:5,10,15,16…(36)` (src `sharepacks/_predictive/2026-03-23/NorthCarolina4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
