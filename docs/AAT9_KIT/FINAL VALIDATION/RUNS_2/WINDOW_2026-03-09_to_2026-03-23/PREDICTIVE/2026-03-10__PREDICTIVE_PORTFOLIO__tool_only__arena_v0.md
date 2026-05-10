# Analysis Arena Predictive Portfolio — D=2026-03-10

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
- Control Center profit alerts: `sharepacks/_predictive/2026-03-10/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| NorthCarolina4 | - | 344 003 188 | 344 003 034 | - | 4 | 229 | 4:004 009 344 | 5(6) | idx[20]:3,4,5,6…(36) |
| Pennsylvania4 | - | 559 008 024 | 559 008 024 | - | 4 | 150 | 2:007 255 | 3(6) | idx[20]:1,3,4,5…(36) |
| OntarioCanada4 | - | 189 077 449 | 077 049 014 | - | 4 | 171 | 3:004 009 138 | 5(6) | idx[20]:1,3,5,9…(36) |
| PuertoRico4 | - | 559 117 359 | 359 557 449 | - | 4 | 193 | 3:001 033 177 | 2(6) | idx[20]:2,3,5,6…(36) |
| Virginia4 | - | 599 039 559 | 039 059 005 | - | 6 | 194 | 2:004 009 | 5(6) | idx[20]:1,2,4,5…(36) |
| Indiana4 | - | 255 027 113 | 255 027 088 | - | 4 | 203 | 2:177 677 | 10(6) | idx[20]:1,2,3,4…(36) |
| NewJersey4 | - | 009 459 117 | 009 459 007 | - | 7 | 226 | 3:007 009 022 | 10(6) | idx[20]:2,3,5,6…(36) |
| Ohio4 | - | 003 599 069 | 003 599 069 | - | 7 | 206 | 3:009 113 559 | 9(8) | idx[20]:1,2,3,4…(36) |
| SouthCarolina4 | - | 667 069 669 | 667 069 778 | - | 3 | 184 | 1:114 | 6(6) | idx[20]:2,3,5,6…(36) |
| Michigan4 | - | 224 778 118 | 224 118 114 | - | 4 | 187 | 2:066 119 | 19(6) | idx[20]:2,3,4,5…(36) |
| Connecticut4 | - | 168 006 368 | 168 368 668 | - | 5 | 203 | 2:099 599 | 24(8) | idx[20]:2,4,6,8…(36) |
| NewYork4 | - | 559 368 224 | 559 368 136 | - | 2 | 209 | 2:007 368 | 23(6) | idx[20]:2,3,4,5…(36) |
| Delaware4 | - | 599 117 129 | 117 129 006 | - | 3 | 221 | 3:009 117 559 | 9(8) | idx[20]:2,5,9,12…(36) |
| Florida4 | - | 224 778 066 | 778 077 004 | - | 5 | 226 | 3:003 011 118 | 9(8) | idx[20]:4,5,6,7…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **NorthCarolina4**: CU packs=`27` union=`229` top_support=`12:009` due=`009 225 344 445`
- **Pennsylvania4**: CU packs=`27` union=`150` top_support=`11:007` due=`007 066 228 255`
- **OntarioCanada4**: CU packs=`27` union=`171` top_support=`11:004` due=`004 044 055 228`
- **PuertoRico4**: CU packs=`27` union=`193` top_support=`11:001` due=`001 011 033 088`
- **Virginia4**: CU packs=`27` union=`194` top_support=`11:004` due=`004 115 177 199`
- **Indiana4**: CU packs=`27` union=`203` top_support=`11:177` due=`177 226 288 337`
- **NewJersey4**: CU packs=`27` union=`226` top_support=`11:022` due=`022 155 335 339`
- **Ohio4**: CU packs=`27` union=`206` top_support=`10:009` due=`009 066 113 118`
- **SouthCarolina4**: CU packs=`27` union=`184` top_support=`9:114` due=`114 115 155 233`
- **Michigan4**: CU packs=`27` union=`187` top_support=`9:066` due=`066 077 119 144`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **NorthCarolina4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-10/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-10/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `3(6)` (src `sharepacks/_predictive/2026-03-10/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-10/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-10/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,5,9…(36)` (src `sharepacks/_predictive/2026-03-10/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `2(6)` (src `sharepacks/_predictive/2026-03-10/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-10/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-10/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-03-10/Virginia4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `10(6)` (src `sharepacks/_predictive/2026-03-10/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-10/Indiana4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `10(6)` (src `sharepacks/_predictive/2026-03-10/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-10/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `9(8)` (src `sharepacks/_predictive/2026-03-10/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-10/Ohio4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `6(6)` (src `sharepacks/_predictive/2026-03-10/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-10/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `19(6)` (src `sharepacks/_predictive/2026-03-10/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-10/Michigan4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `24(8)` (src `sharepacks/_predictive/2026-03-10/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,6,8…(36)` (src `sharepacks/_predictive/2026-03-10/Connecticut4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `23(6)` (src `sharepacks/_predictive/2026-03-10/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-10/NewYork4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `9(8)` (src `sharepacks/_predictive/2026-03-10/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,9,12…(36)` (src `sharepacks/_predictive/2026-03-10/Delaware4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `9(8)` (src `sharepacks/_predictive/2026-03-10/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,6,7…(36)` (src `sharepacks/_predictive/2026-03-10/Florida4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
