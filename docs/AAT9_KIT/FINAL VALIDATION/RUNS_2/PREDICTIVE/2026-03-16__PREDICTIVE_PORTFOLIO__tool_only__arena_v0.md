# Analysis Arena Predictive Portfolio — D=2026-03-16

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
- Control Center profit alerts: `sharepacks/_predictive/2026-03-16/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| Ohio4 | - | 069 099 338 | 069 099 338 | - | 7 | 157 | 3:004 009 066 | 5(6) | idx[20]:2,4,5,6…(36) |
| Indiana4 | - | 599 224 559 | 599 224 559 | - | 4 | 207 | 2:177 288 | 20(6) | idx[20]:1,5,6,10…(36) |
| Virginia4 | - | 559 255 259 | 559 259 889 | - | 3 | 182 | 2:004 455 | 5(6) | idx[20]:1,2,3,4…(36) |
| OntarioCanada4 | - | 014 138 168 | 014 138 223 | - | 2 | 187 | 3:004 168 228 | 27(6) | idx[20]:1,5,8,9…(36) |
| Pennsylvania4 | - | 244 599 033 | 033 259 008 | - | 5 | 212 | 2:007 088 | 32(2) | idx[22]:1,2,3,5…(36) |
| NewYork4 | - | 668 003 559 | 003 039 001 | - | 5 | 220 | 3:007 033 035 | 21(8) | idx[20]:3,4,5,6…(36) |
| NorthCarolina4 | - | 138 378 366 | 138 378 366 | - | 4 | 220 | 2:009 344 | 18(6) | idx[20]:4,5,6,8…(36) |
| NewJersey4 | - | 244 099 179 | 099 013 024 | - | 3 | 201 | 3:022 169 244 | 12(8) | idx[20]:2,3,5,6…(36) |
| PuertoRico4 | - | 677 445 047 | 677 445 047 | - | 4 | 201 | 2:001 006 | 12(8) | idx[20]:1,2,3,4…(36) |
| Michigan4 | - | 044 067 677 | 044 067 458 | - | 6 | 203 | 3:066 077 688 | 13(6) | idx[20]:4,5,6,7…(36) |
| SouthCarolina4 | - | 077 455 477 | 077 036 | - | 2 | 207 | 3:114 177 477 | 10(6) | idx[20]:1,2,3,4…(36) |
| Delaware4 | - | 599 559 059 | 059 399 019 | - | 6 | 208 | 2:009 559 | 14(8) | idx[20]:2,5,6,7…(36) |
| Connecticut4 | - | 559 344 044 | 559 044 569 | - | 4 | 209 | 3:099 399 599 | 24(8) | idx[20]:2,5,9,14…(36) |
| Florida4 | - | 668 006 669 | 668 669 168 | - | 4 | 211 | 2:003 118 | 7(8) | idx[20]:1,2,3,4…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **Ohio4**: CU packs=`27` union=`157` top_support=`13:009` due=`009 066 113 118`
- **Indiana4**: CU packs=`27` union=`207` top_support=`12:177` due=`177 226 288 337`
- **Virginia4**: CU packs=`27` union=`182` top_support=`11:004` due=`004 115 177 199`
- **OntarioCanada4**: CU packs=`27` union=`187` top_support=`10:004` due=`004 044 055 228`
- **Pennsylvania4**: CU packs=`27` union=`212` top_support=`10:007` due=`007 009 066 228`
- **NewYork4**: CU packs=`27` union=`220` top_support=`10:007` due=`007 011 066 488`
- **NorthCarolina4**: CU packs=`27` union=`220` top_support=`10:009` due=`009 225 299 344`
- **NewJersey4**: CU packs=`27` union=`201` top_support=`9:022` due=`022 155 335 339`
- **PuertoRico4**: CU packs=`27` union=`201` top_support=`9:001` due=`001 003 011 033`
- **Michigan4**: CU packs=`27` union=`203` top_support=`9:066` due=`066 077 119 144`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **Ohio4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-16/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-16/Ohio4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `20(6)` (src `sharepacks/_predictive/2026-03-16/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,5,6,10…(36)` (src `sharepacks/_predictive/2026-03-16/Indiana4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `5(6)` (src `sharepacks/_predictive/2026-03-16/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-16/Virginia4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `27(6)` (src `sharepacks/_predictive/2026-03-16/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,5,8,9…(36)` (src `sharepacks/_predictive/2026-03-16/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `32(2)` (src `sharepacks/_predictive/2026-03-16/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-03-16/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `21(8)` (src `sharepacks/_predictive/2026-03-16/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-03-16/NewYork4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `18(6)` (src `sharepacks/_predictive/2026-03-16/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,6,8…(36)` (src `sharepacks/_predictive/2026-03-16/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `12(8)` (src `sharepacks/_predictive/2026-03-16/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,5,6…(36)` (src `sharepacks/_predictive/2026-03-16/NewJersey4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `12(8)` (src `sharepacks/_predictive/2026-03-16/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-16/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `13(6)` (src `sharepacks/_predictive/2026-03-16/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,6,7…(36)` (src `sharepacks/_predictive/2026-03-16/Michigan4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `10(6)` (src `sharepacks/_predictive/2026-03-16/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-16/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `14(8)` (src `sharepacks/_predictive/2026-03-16/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,7…(36)` (src `sharepacks/_predictive/2026-03-16/Delaware4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `24(8)` (src `sharepacks/_predictive/2026-03-16/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,9,14…(36)` (src `sharepacks/_predictive/2026-03-16/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `7(8)` (src `sharepacks/_predictive/2026-03-16/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-03-16/Florida4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
