# Analysis Arena Day Synthesis — D=2026-01-19 (H=2026-01-18)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-19`
- History date `H`: `2026-01-18`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-01-19`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-19.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,058,559` vtrac=`4,3,15` hints=`A05:224:PERM,HP3 | Combined:0/5-4/9 | 029,038,047 | Prog:27|Hidden | tail:06|ev:2|2d:2|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,259,007` vtrac=`5,12,7` hints=`A05:559:PERM,HP3 | Combined:2/7-3/8 | 059,158,257 | Prog:27|Hidden | tail:07|ev:1|2d:1|trial|moderate`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`388,255,378` vtrac=`32,3,29` hints=`A05:889:PERM,HP6 | Combined:0/5-4/9 | 013,017,018 | Prog:27|Hidden | tail:07|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`077,007,038` vtrac=`10,6,23` hints=`A11:007:HOT,CONS | Combined:1/6-2/7 | 012,013,014 | LR:4|Prog:27|Hidden|multi_literal_mixed_family | tail:07|ev:6|2d:6|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,011,017` vtrac=`28,10,6` hints=`A05:011:PERM,HP3 | Combined:1/6-2/7 | 012,014,017 | Prog:27|Hidden | tail:11|ev:4|2d:4|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`004,014,019` vtrac=`5,9,2` hints=`A11:000:HOT,CONS | Combined:3/8-4/9 | 569,047,056 | Prog:27|Hidden | tail:04|ev:13|2d:13|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`377,337,177` vtrac=`27,18,10` hints=`A05:339:PERM,HP4 | Combined:0/5-1/6 | 149,167,257 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:07|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,244,225` vtrac=`27,31,29` hints=`A05:244:PERM,HP7 | Combined:0/5-4/9 | 167,059,068 | Prog:27|Hidden | tail:04|ev:5|2d:5|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`437` Evening=`429`
- **Delaware4**: Midday=`778` Evening=`146`
- **Florida4**: Midday=`863` Evening=`359`
- **Indiana4**: Midday=`865` Evening=`109`
- **Michigan4**: Midday=`818` Evening=`402`
- **NewJersey4**: Midday=`833` Evening=`440`
- **NewYork4**: Midday=`769` Evening=`440`
- **NorthCarolina4**: Midday=`535` Evening=`845`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-19__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-19__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-19__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-19__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-19__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-19__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-19__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-19__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-19__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-19__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-19__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-19__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
