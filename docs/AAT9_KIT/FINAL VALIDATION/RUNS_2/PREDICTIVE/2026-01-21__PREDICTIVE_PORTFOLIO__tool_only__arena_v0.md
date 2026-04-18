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
- Predictive sharepacks root: `sharepacks/_predictive`
- Control Center profit alerts: `sharepacks/_predictive/2026-01-21/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| OntarioCanada4 | - | 244 044 004 | 044 468 448 | - | 8 | 143 | 4:004 044 144 | 5(6) | idx[20]:1,3,4,5…(36) |
| Delaware4 | - | 255 559 336 | 259 055 003 | - | 4 | 167 | 3:004 009 559 | 5(6) | idx[20]:1,2,3,4…(36) |
| Ohio4 | - | 077 007 078 | 007 078 224 | - | 4 | 179 | 1:009 | 5(6) | idx[20]:2,3,4,5…(36) |
| Virginia4 | - | 133 339 033 | 133 339 033 | - | 7 | 162 | 2:004 009 | 12(8) | idx[20]:1,2,3,4…(36) |
| Connecticut4 | - | 006 255 355 | 355 001 668 | - | 5 | 174 | 1:088 | 11(8) | idx[20]:1,2,3,4…(36) |
| PuertoRico4 | - | 168 668 336 | 168 334 138 | - | 5 | 184 | 2:022 033 | 10(6) | idx[20]:1,2,3,4…(36) |
| Michigan4 | - | 224 477 017 | 224 017 247 | - | 4 | 137 | 2:066 155 | 7(8) | idx[20]:1,2,3,6…(36) |
| Florida4 | - | 259 378 008 | 259 008 388 | - | 3 | 138 | 3:003 008 355 | 29(6) | idx[20]:1,3,4,5…(34) |
| SouthCarolina4 | - | 009 599 005 | 599 005 039 | - | 4 | 149 | 3:114 233 466 | 1(2) | idx[22]:1,2,4,5…(36) |
| NewJersey4 | - | 001 559 004 | 001 004 014 | - | 4 | 158 | 2:001 022 | 2(6) | idx[20]:1,2,3,5…(36) |
| NewYork4 | - | 113 337 115 | 113 337 115 | - | 4 | 164 | 1:001 | 27(6) | idx[20]:2,3,6,7…(36) |
| Pennsylvania4 | - | 559 599 178 | 559 178 334 | - | 2 | 169 | 2:007 138 | 23(6) | idx[20]:1,3,4,5…(36) |
| NorthCarolina4 | - | 778 006 366 | 006 024 119 | - | 8 | 176 | 3:001 006 225 | 27(6) | idx[20]:1,2,3,5…(36) |
| Indiana4 | - | 001 077 244 | 001 147 014 | - | 4 | 178 | 2:002 226 | 6(6) | idx[20]:1,2,3,4…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **OntarioCanada4**: CU packs=`27` union=`143` top_support=`11:004` due=`004 044 144 228`
- **Delaware4**: CU packs=`27` union=`167` top_support=`11:009` due=`009 088 117 223`
- **Ohio4**: CU packs=`27` union=`179` top_support=`11:009` due=`009 066 113 118`
- **Virginia4**: CU packs=`27` union=`162` top_support=`10:004` due=`004 177 199 334`
- **Connecticut4**: CU packs=`27` union=`174` top_support=`10:088` due=`088 099 223 228`
- **PuertoRico4**: CU packs=`27` union=`184` top_support=`10:022` due=`022 033 088 112`
- **Michigan4**: CU packs=`27` union=`137` top_support=`9:066` due=`066 112 119 155`
- **Florida4**: CU packs=`27` union=`138` top_support=`9:003` due=`003 009 011 077`
- **SouthCarolina4**: CU packs=`27` union=`149` top_support=`9:114` due=`114 115 155 233`
- **NewJersey4**: CU packs=`27` union=`158` top_support=`9:022` due=`022 114 155 339`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-21/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-21/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-21/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-21/Delaware4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-21/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-21/Ohio4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `12(8)` (src `sharepacks/_predictive/2026-01-21/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-21/Virginia4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `11(8)` (src `sharepacks/_predictive/2026-01-21/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-21/Connecticut4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-21/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-21/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-21/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,6…(36)` (src `sharepacks/_predictive/2026-01-21/Michigan4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `29(6)` (src `sharepacks/_predictive/2026-01-21/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(34)` (src `sharepacks/_predictive/2026-01-21/Florida4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `1(2)` (src `sharepacks/_predictive/2026-01-21/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-01-21/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `2(6)` (src `sharepacks/_predictive/2026-01-21/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-21/NewJersey4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `27(6)` (src `sharepacks/_predictive/2026-01-21/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,6,7…(36)` (src `sharepacks/_predictive/2026-01-21/NewYork4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `23(6)` (src `sharepacks/_predictive/2026-01-21/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-21/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `27(6)` (src `sharepacks/_predictive/2026-01-21/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-21/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-21/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-21/Indiana4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
