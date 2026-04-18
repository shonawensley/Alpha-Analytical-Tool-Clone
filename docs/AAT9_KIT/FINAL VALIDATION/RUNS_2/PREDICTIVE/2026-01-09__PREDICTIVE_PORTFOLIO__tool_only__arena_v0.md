# Analysis Arena Predictive Portfolio — D=2026-01-09

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| PuertoRico4 | - | 068 008 006 | 068 008 006 | - | 5 | 207 | 3:022 033 088 | 10(6) | idx[20]:2,3,4,5…(36) |
| NewYork4 | - | 005 001 255 | 005 001 025 | - | 10 | 182 | 4:001 006 007 | 2(6) | idx[20]:1,2,3,4…(36) |
| Florida4 | - | 255 559 224 | 224 557 034 | - | 4 | 189 | 2:003 077 | 4(6) | idx[20]:3,4,5,6…(36) |
| OntarioCanada4 | - | 015 006 224 | 015 006 224 | - | 6 | 205 | 3:004 009 224 | 5(6) | idx[20]:1,2,3,5…(36) |
| Delaware4 | - | 344 033 445 | 344 033 144 | - | 6 | 212 | 4:009 044 344 | 5(6) | idx[20]:2,4,5,6…(36) |
| Virginia4 | - | 024 559 599 | 024 346 134 | - | 6 | 214 | 2:004 136 | 34(6) | idx[20]:3,4,5,9…(36) |
| Connecticut4 | - | 224 448 2244 | 224 448 244 | - | 5 | 173 | 2:088 228 | 30(8) | idx[20]:4,5,6,7…(36) |
| Michigan4 | - | 334 019 059 | 334 019 144 | - | 3 | 179 | 2:112 119 | 9(8) | idx[20]:2,5,6,8…(36) |
| SouthCarolina4 | - | 599 559 244 | 559 244 059 | - | 3 | 189 | 2:115 499 | 15(6) | idx[20]:1,2,3,4…(36) |
| Ohio4 | - | 599 559 299 | 299 399 788 | - | 5 | 200 | 2:009 559 | 4(6) | idx[20]:1,3,4,5…(36) |
| NorthCarolina4 | - | 299 066 446 | 299 066 446 | - | 2 | 206 | 4:001 009 044 | 25(6) | idx[20]:2,3,4,5…(36) |
| Pennsylvania4 | - | 445 019 009 | 445 019 009 | - | 4 | 211 | 2:007 112 | 9(8) | idx[20]:1,2,3,5…(36) |
| NewJersey4 | - | 778 137 014 | 778 003 078 | - | 4 | 230 | 2:022 077 | 7(8) | idx[22]:1,2,3,4…(36) |
| Indiana4 | - | 244 669 004 | 669 004 066 | - | 2 | 281 | 4:002 066 177 | 9(8) | idx[20]:3,5,6,7…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **PuertoRico4**: CU packs=`27` union=`207` top_support=`15:022` due=`022 033 088 199`
- **NewYork4**: CU packs=`27` union=`182` top_support=`13:001` due=`001 007 011 066`
- **Florida4**: CU packs=`27` union=`189` top_support=`11:003` due=`003 009 011 077`
- **OntarioCanada4**: CU packs=`27` union=`205` top_support=`11:004` due=`004 044 144 228`
- **Delaware4**: CU packs=`27` union=`212` top_support=`10:009` due=`009 088 117 223`
- **Virginia4**: CU packs=`27` union=`214` top_support=`10:004` due=`004 177 199 377`
- **Connecticut4**: CU packs=`27` union=`173` top_support=`9:088` due=`088 099 223 228`
- **Michigan4**: CU packs=`27` union=`179` top_support=`9:112` due=`112 119 155 199`
- **SouthCarolina4**: CU packs=`27` union=`189` top_support=`9:115` due=`115 155 224 233`
- **Ohio4**: CU packs=`27` union=`200` top_support=`9:009` due=`009 066 113 118`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-09/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-09/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `2(6)` (src `sharepacks/_predictive/2026-01-09/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-09/NewYork4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `4(6)` (src `sharepacks/_predictive/2026-01-09/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,6…(36)` (src `sharepacks/_predictive/2026-01-09/Florida4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-09/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-09/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-09/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,4,5,6…(36)` (src `sharepacks/_predictive/2026-01-09/Delaware4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `34(6)` (src `sharepacks/_predictive/2026-01-09/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,4,5,9…(36)` (src `sharepacks/_predictive/2026-01-09/Virginia4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `30(8)` (src `sharepacks/_predictive/2026-01-09/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:4,5,6,7…(36)` (src `sharepacks/_predictive/2026-01-09/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `9(8)` (src `sharepacks/_predictive/2026-01-09/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,5,6,8…(36)` (src `sharepacks/_predictive/2026-01-09/Michigan4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `15(6)` (src `sharepacks/_predictive/2026-01-09/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-09/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `4(6)` (src `sharepacks/_predictive/2026-01-09/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-09/Ohio4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `25(6)` (src `sharepacks/_predictive/2026-01-09/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-09/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `9(8)` (src `sharepacks/_predictive/2026-01-09/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-09/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **NewJersey4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-09/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-09/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `9(8)` (src `sharepacks/_predictive/2026-01-09/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:3,5,6,7…(36)` (src `sharepacks/_predictive/2026-01-09/Indiana4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
