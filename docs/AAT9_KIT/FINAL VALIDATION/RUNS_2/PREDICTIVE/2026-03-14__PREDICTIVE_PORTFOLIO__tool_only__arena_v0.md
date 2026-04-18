# Analysis Arena Predictive Portfolio — D=2026-03-14

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
- Control Center profit alerts: `sharepacks/_predictive/2026-03-14/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| OntarioCanada4 | - | 449 368 388 | 449 388 014 | - | 4 | 163 | 1:004 | 5(6) | idx[20]:1,4,5,9…(36) |
| Ohio4 | - | 049 069 338 | 049 069 338 | - | 8 | 179 | 3:004 009 066 | 14(8) | idx[20]:2,4,5,6…(36) |
| Virginia4 | - | 559 259 299 | 559 029 889 | - | 5 | 184 | 2:004 455 | 5(6) | idx[24]:1,2,3,4…(36) |
| PuertoRico4 | - | 677 449 445 | 677 057 056 | - | 7 | 193 | 1:001 | 2(6) | idx[20]:1,2,3,4…(36) |
| Delaware4 | - | 559 049 007 | 049 007 059 | - | 11 | 187 | 2:009 559 | 5(6) | idx[20]:1,3,5,6…(36) |
| Indiana4 | - | 599 788 005 | 005 559 566 | - | 7 | 215 | 1:177 | 20(6) | idx[22]:1,2,3,4…(36) |
| NorthCarolina4 | - | 388 368 009 | 388 368 003 | - | 4 | 225 | 2:009 344 | 18(6) | idx[20]:4,5,8,10…(36) |
| Michigan4 | - | 008 688 455 | 008 448 058 | - | 4 | 174 | 2:058 066 | 4(6) | idx[20]:1,2,3,4…(36) |
| NewJersey4 | - | 004 244 224 | 004 244 024 | - | 7 | 191 | 3:022 167 244 | 19(6) | idx[20]:2,5,6,10…(36) |
| Florida4 | - | 224 226 499 | 226 499 022 | - | 3 | 195 | 2:003 008 | 20(6) | idx[20]:2,3,4,5…(36) |
| NewYork4 | - | 668 006 039 | 006 039 033 | - | 7 | 203 | 1:007 | 12(8) | idx[20]:2,3,4,5…(36) |
| SouthCarolina4 | - | 244 077 003 | 077 027 013 | - | 3 | 203 | 2:027 114 | 10(6) | idx[20]:1,2,3,4…(36) |
| Pennsylvania4 | - | 559 013 224 | 013 005 008 | - | 6 | 216 | 2:002 007 | 8(8) | idx[20]:2,3,4,5…(36) |
| Connecticut4 | - | 559 368 689 | 559 368 689 | - | 2 | 221 | 2:099 599 | 24(8) | idx[20]:2,3,5,6…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **OntarioCanada4**: CU packs=`27` union=`163` top_support=`12:004` due=`004 044 055 228`
- **Ohio4**: CU packs=`27` union=`179` top_support=`12:009` due=`009 066 113 118`
- **Virginia4**: CU packs=`27` union=`184` top_support=`12:004` due=`004 115 177 199`
- **PuertoRico4**: CU packs=`27` union=`193` top_support=`12:001` due=`001 003 011 033`
- **Delaware4**: CU packs=`27` union=`187` top_support=`11:009` due=`009 033 088 117`
- **Indiana4**: CU packs=`27` union=`215` top_support=`11:177` due=`177 226 288 337`
- **NorthCarolina4**: CU packs=`27` union=`225` top_support=`10:009` due=`009 225 299 344`
- **Michigan4**: CU packs=`27` union=`174` top_support=`9:066` due=`066 077 119 144`
- **NewJersey4**: CU packs=`27` union=`191` top_support=`9:022` due=`022 155 335 339`
- **Florida4**: CU packs=`27` union=`195` top_support=`9:003` due=`003 009 011 118`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-14/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,4,5,9…(36)` (src `sharepacks/_predictive/2026-03-14/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `14(8)` (src `sharepacks/_predictive/2026-03-14/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-14/Ohio4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-14/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[24]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-14/Virginia4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `2(6)` (src `sharepacks/_predictive/2026-03-14/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-14/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-14/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-14/Delaware4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `20(6)` (src `sharepacks/_predictive/2026-03-14/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-14/Indiana4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `18(6)` (src `sharepacks/_predictive/2026-03-14/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,8,10…(36)` (src `sharepacks/_predictive/2026-03-14/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `4(6)` (src `sharepacks/_predictive/2026-03-14/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-14/Michigan4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `19(6)` (src `sharepacks/_predictive/2026-03-14/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,10…(36)` (src `sharepacks/_predictive/2026-03-14/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `20(6)` (src `sharepacks/_predictive/2026-03-14/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-14/Florida4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `12(8)` (src `sharepacks/_predictive/2026-03-14/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-14/NewYork4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `10(6)` (src `sharepacks/_predictive/2026-03-14/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-14/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `8(8)` (src `sharepacks/_predictive/2026-03-14/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-03-14/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `24(8)` (src `sharepacks/_predictive/2026-03-14/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-14/Connecticut4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
