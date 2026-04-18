# Analysis Arena Predictive Portfolio — D=2026-01-02

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
- Control Center profit alerts: `sharepacks/_predictive/2026-01-02/control_center/profit_alerts.csv`
- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.json`

## Portfolio Table

| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |
|---|---|---|---|---|---:|---:|---|---|---|
| NewJersey4 | - | 299 599 899 | 599 899 229 | - | 4 | 136 | 1:022 | 10(6) | idx[20]:1,2,8,10…(36) |
| Pennsylvania4 | - | 559 579 599 | 559 579 015 | - | 5 | 155 | 3:007 255 277 | 3(6) | idx[22]:1,3,4,5…(36) |
| Delaware4 | - | 244 449 499 | 449 144 114 | - | 4 | 164 | 3:004 009 114 | 5(6) | idx[22]:1,2,5,6…(36) |
| Ohio4 | - | 055 559 255 | 055 559 224 | - | 7 | 173 | 2:009 559 | 7(8) | idx[20]:1,2,3,4…(36) |
| PuertoRico4 | - | 344 113 224 | 224 002 001 | - | 5 | 223 | 3:022 199 224 | 10(6) | idx[20]:2,3,6,10…(36) |
| Connecticut4 | - | 368 559 388 | 368 388 006 | - | 3 | 171 | 1:088 | 23(6) | idx[20]:2,3,4,5…(36) |
| Indiana4 | - | 244 668 367 | 244 367 677 | - | 4 | 189 | 2:002 066 | 7(8) | idx[20]:1,2,3,4…(36) |
| Michigan4 | - | 006 069 599 | 006 069 599 | - | 7 | 144 | 2:112 155 | 18(6) | idx[20]:2,3,4,5…(36) |
| SouthCarolina4 | - | 118 008 009 | 008 138 368 | - | 3 | 150 | 2:115 224 | 18(6) | idx[20]:1,2,4,5…(36) |
| Florida4 | - | 559 466 366 | 559 466 677 | - | 4 | 158 | 2:003 008 | 8(8) | idx[22]:4,5,6,7…(36) |
| OntarioCanada4 | - | 118 255 188 | 118 255 022 | - | 5 | 164 | 3:004 114 167 | 23(6) | idx[20]:1,2,5,6…(36) |
| Virginia4 | - | 224 177 133 | 224 177 577 | - | 4 | 164 | 3:004 177 455 | 12(8) | idx[20]:1,2,3,5…(36) |
| NorthCarolina4 | - | 224 223 229 | 224 223 229 | - | 5 | 173 | 3:001 009 044 | 12(8) | idx[20]:1,2,3,4…(36) |
| NewYork4 | - | 688 788 778 | 788 248 026 | - | 4 | 174 | 3:001 006 066 | 6(6) | idx[20]:2,3,4,5…(36) |

## Arena-First Board Snapshot


## Control Arm Snapshot

These are still baseline/control-arm surfaces, not the definition of arena truth.

- **NewJersey4**: CU packs=`27` union=`136` top_support=`11:022` due=`022 114 155 339`
- **Pennsylvania4**: CU packs=`27` union=`155` top_support=`11:007` due=`007 228 255 277`
- **Delaware4**: CU packs=`27` union=`164` top_support=`11:009` due=`009 088 223 228`
- **Ohio4**: CU packs=`27` union=`173` top_support=`11:009` due=`009 066 113 114`
- **PuertoRico4**: CU packs=`27` union=`223` top_support=`11:022` due=`022 033 088 199`
- **Connecticut4**: CU packs=`27` union=`171` top_support=`10:088` due=`088 099 223 228`
- **Indiana4**: CU packs=`27` union=`189` top_support=`10:002` due=`002 022 177 226`
- **Michigan4**: CU packs=`27` union=`144` top_support=`9:112` due=`112 119 155 199`
- **SouthCarolina4**: CU packs=`27` union=`150` top_support=`9:115` due=`115 155 224 288`
- **Florida4**: CU packs=`27` union=`158` top_support=`9:003` due=`003 008 009 011`

## Play Card Defaults

- B12 strategy: `analysis_prefix`
- B24 strategy: `vtrac_pack_boxed_first_laneonly_presetB`
- B36 strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22`

- **NewJersey4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-02/NewJersey4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,8,10…(36)` (src `sharepacks/_predictive/2026-01-02/NewJersey4/play_card__tool_only__arena_v0.json`)
- **Pennsylvania4**: B24 `3(6)` (src `sharepacks/_predictive/2026-01-02/Pennsylvania4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-02/Pennsylvania4/play_card__tool_only__arena_v0.json`)
- **Delaware4**: B24 `5(6)` (src `sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:1,2,5,6…(36)` (src `sharepacks/_predictive/2026-01-02/Delaware4/play_card__tool_only__arena_v0.json`)
- **Ohio4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-02/Ohio4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-02/Ohio4/play_card__tool_only__arena_v0.json`)
- **PuertoRico4**: B24 `10(6)` (src `sharepacks/_predictive/2026-01-02/PuertoRico4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,6,10…(36)` (src `sharepacks/_predictive/2026-01-02/PuertoRico4/play_card__tool_only__arena_v0.json`)
- **Connecticut4**: B24 `23(6)` (src `sharepacks/_predictive/2026-01-02/Connecticut4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-02/Connecticut4/play_card__tool_only__arena_v0.json`)
- **Indiana4**: B24 `7(8)` (src `sharepacks/_predictive/2026-01-02/Indiana4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-02/Indiana4/play_card__tool_only__arena_v0.json`)
- **Michigan4**: B24 `18(6)` (src `sharepacks/_predictive/2026-01-02/Michigan4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-02/Michigan4/play_card__tool_only__arena_v0.json`)
- **SouthCarolina4**: B24 `18(6)` (src `sharepacks/_predictive/2026-01-02/SouthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,4,5…(36)` (src `sharepacks/_predictive/2026-01-02/SouthCarolina4/play_card__tool_only__arena_v0.json`)
- **Florida4**: B24 `8(8)` (src `sharepacks/_predictive/2026-01-02/Florida4/play_card__tool_only__arena_v0.json`) | B36 `idx[22]:4,5,6,7…(36)` (src `sharepacks/_predictive/2026-01-02/Florida4/play_card__tool_only__arena_v0.json`)
- **OntarioCanada4**: B24 `23(6)` (src `sharepacks/_predictive/2026-01-02/OntarioCanada4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,5,6…(36)` (src `sharepacks/_predictive/2026-01-02/OntarioCanada4/play_card__tool_only__arena_v0.json`)
- **Virginia4**: B24 `12(8)` (src `sharepacks/_predictive/2026-01-02/Virginia4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,5…(36)` (src `sharepacks/_predictive/2026-01-02/Virginia4/play_card__tool_only__arena_v0.json`)
- **NorthCarolina4**: B24 `12(8)` (src `sharepacks/_predictive/2026-01-02/NorthCarolina4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:1,2,3,4…(36)` (src `sharepacks/_predictive/2026-01-02/NorthCarolina4/play_card__tool_only__arena_v0.json`)
- **NewYork4**: B24 `6(6)` (src `sharepacks/_predictive/2026-01-02/NewYork4/play_card__tool_only__arena_v0.json`) | B36 `idx[20]:2,3,4,5…(36)` (src `sharepacks/_predictive/2026-01-02/NewYork4/play_card__tool_only__arena_v0.json`)

## Analyst Notes

- Which states are strongest from the arena-first lens?: `...`
- Which states are strongest only from the control-arm lens?: `...`
- Any state where tracker hints materially outran the control arm?: `...`
- Any state where arena rank feels too high or too low?: `...`
