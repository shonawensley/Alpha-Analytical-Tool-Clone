# Analysis Arena Predictive Portfolio — D=2026-01-20

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-20/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| OntarioCanada4 | - | 244 044 236 | 244 446 268 | - | 6 | 147 | 1:004 | 5(6) | idx[20]:1,2,4,5…(36) |
| Delaware4 | - | 559 259 007 | 259 003 055 | - | 4 | 159 | 3:004 009 559 | 5(6) | idx[21]:1,2,4,5…(35) |
| Ohio4 | - | 077 008 009 | 049 045 244 | - | 5 | 176 | 2:004 009 | 5(6) | idx[20]:3,4,5,6…(36) |
| Virginia4 | - | 339 133 013 | 339 133 013 | - | 8 | 154 | 3:003 004 009 | 14(8) | idx[20]:1,2,3,4…(36) |
| Connecticut4 | - | 006 005 255 | 355 568 668 | - | 6 | 175 | 2:088 228 | 7(8) | idx[20]:1,2,3,4…(36) |
| PuertoRico4 | - | 334 336 013 | 334 013 138 | - | 5 | 190 | 2:022 033 | 10(6) | idx[20]:2,3,4,5…(36) |
| Florida4 | - | 378 255 259 | 378 778 278 | - | 2 | 128 | 4:003 008 077 | 29(6) | idx[15]:3,4,5,6…(31) |
| Michigan4 | - | 224 778 007 | 224 027 017 | - | 3 | 135 | 2:066 155 | 7(8) | idx[20]:1,2,3,6…(36) |
| SouthCarolina4 | - | 005 009 599 | 005 339 067 | - | 4 | 149 | 3:114 233 466 | 1(2) | idx[22]:1,2,5,6…(36) |
| NewJersey4 | - | 001 559 004 | 001 004 348 | - | 6 | 156 | 2:001 022 | 2(6) | idx[20]:1,2,3,5…(36) |
| NewYork4 | - | 378 377 113 | 378 377 337 | - | 4 | 156 | 2:001 378 | 27(6) | idx[20]:2,3,6,7…(36) |
| Pennsylvania4 | - | 344 003 034 | 344 034 000 | - | 6 | 170 | 1:007 | 23(6) | idx[20]:3,4,5,6…(36) |
| Indiana4 | - | 077 224 007 | 007 017 037 | - | 6 | 171 | 2:002 007 | 6(6) | idx[20]:1,2,3,4…(36) |
| NorthCarolina4 | - | 778 244 368 | 244 257 024 | - | 3 | 180 | 2:001 225 | 27(6) | idx[22]:1,2,3,4…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **OntarioCanada4**: CU packs=`27` union=`147` top_support=`11:004` due=`004 044 144 228`
- **Delaware4**: CU packs=`27` union=`159` top_support=`11:009` due=`009 088 117 223`
- **Ohio4**: CU packs=`27` union=`176` top_support=`11:009` due=`009 066 113 118`
- **Virginia4**: CU packs=`27` union=`154` top_support=`10:004` due=`004 177 199 334`
- **Connecticut4**: CU packs=`27` union=`175` top_support=`10:088` due=`088 099 223 228`
- **PuertoRico4**: CU packs=`27` union=`190` top_support=`10:022` due=`022 033 088 112`
- **Florida4**: CU packs=`27` union=`128` top_support=`9:003` due=`003 009 011 077`
- **Michigan4**: CU packs=`27` union=`135` top_support=`9:066` due=`066 112 119 155`
- **SouthCarolina4**: CU packs=`27` union=`149` top_support=`9:114` due=`114 115 155 233`
- **NewJersey4**: CU packs=`27` union=`156` top_support=`9:022` due=`022 114 155 339`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-20/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-01-20/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-20/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[21]:1,2,4,5…(35)` (src `sharepacks/_predictive/2026-01-20/Delaware4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-20/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-01-20/Ohio4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `14(8)` (src `sharepacks/_predictive/2026-01-20/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-20/Virginia4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-20/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-20/Connecticut4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-20/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-20/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `29(6)` (src `sharepacks/_predictive/2026-01-20/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[15]:3,4,5,6…(31)` (src `sharepacks/_predictive/2026-01-20/Florida4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-20/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,6…(36)` (src `sharepacks/_predictive/2026-01-20/Michigan4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `1(2)` (src `sharepacks/_predictive/2026-01-20/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,5,6…(36)` (src `sharepacks/_predictive/2026-01-20/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `2(6)` (src `sharepacks/_predictive/2026-01-20/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-20/NewJersey4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `27(6)` (src `sharepacks/_predictive/2026-01-20/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,6,7…(36)` (src `sharepacks/_predictive/2026-01-20/NewYork4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `23(6)` (src `sharepacks/_predictive/2026-01-20/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-01-20/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-20/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-20/Indiana4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `27(6)` (src `sharepacks/_predictive/2026-01-20/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-20/NorthCarolina4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
