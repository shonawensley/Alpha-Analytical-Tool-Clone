# Analysis Arena Day Synthesis — D=2026-01-01 (H=2025-12-31)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-01`
- History date `H`: `2025-12-31`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-01-01`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-01.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`011,388,368` vtrac=`4,23,32` hints=`A11:008:HOT,CONS | Combined:0/5-4/9 | 038,058,138 | Prog:27|Hidden | tail:11|ev:16|2d:13|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`244,014,144` vtrac=`35,31,25` hints=`A05:244:PERM,HP6 | Combined:2/7-3/8 | 012,013,014 | Prog:27|Hidden | tail:9|ev:10|2d:4|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,138,559` vtrac=`23,15,10` hints=`A05:077:PERM,HP5 | Combined:0/5-3/8 | 059,068,149 | Prog:27|Hidden | tail:77|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`677,244,668` vtrac=`20,18,23` hints=`A05:677:PERM,HP6 | Combined:1/6-2/7 | 037,127,379 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,133,599` vtrac=`2,23,3` hints=`A11:006:HOT,CONS | Combined:1/6-2/7 | 016,049,056 | Prog:27|Hidden | tail:06|ev:6|2d:6|xvar|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`299,778,118` vtrac=`31,30,18` hints=`A05:778:PERM,HP7 | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | tail:4|ev:2|trial|moderate`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`778,677,678` vtrac=`30,27,31` hints=`A05:778:PERM,HP6 | Combined:0/5-1/6 | 027,038,057 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`224,003,223` vtrac=`28,4,1` hints=`A05:224:PERM,HP5 | Combined:0/5-4/9 | 012,013,023 | Prog:27|Hidden | tail:03|ev:9|2d:7|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`228` Evening=`109`
- **Delaware4**: Midday=`149` Evening=`937`
- **Florida4**: Midday=`195` Evening=`291`
- **Indiana4**: Midday=`474` Evening=`909`
- **Michigan4**: Midday=`032` Evening=`204`
- **NewJersey4**: Midday=`770` Evening=`504`
- **NewYork4**: Midday=`117` Evening=`174`
- **NorthCarolina4**: Midday=`416` Evening=`053`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-01__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
