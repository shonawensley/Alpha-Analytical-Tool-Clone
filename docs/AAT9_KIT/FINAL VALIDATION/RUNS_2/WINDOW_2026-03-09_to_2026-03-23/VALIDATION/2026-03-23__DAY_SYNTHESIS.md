# Analysis Arena Day Synthesis — D=2026-03-23 (H=2026-03-22)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-03-23`
- History date `H`: `2026-03-22`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-03-23`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-03-23.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`113,025,117` vtrac=`18,17,3` hints=`A05:113:PERM,HP7 | Combined:0/5-4/9 | 015,016,027 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`011,001,038` vtrac=`2,6,13` hints=`A05:001:PERM,HP6 | Combined:0/5-3/8 | 019,037,127 | Prog:27|Hidden | -`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`224,066,114` vtrac=`19,31,28` hints=`A05:224:PERM,HP4 | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | tail:02|ev:2|2d:2|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,259,004` vtrac=`5,12,3` hints=`A05:005:PERM,HP2 | Combined:0/5-4/9 | 027,057,127 | Prog:27|Hidden | tail:04|ev:7|2d:7|xvar|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`344,445,055` vtrac=`15,25,1` hints=`A05:055:PERM,HP2 | Combined:0/5-1/6 | 127,136,019 | Prog:27|Hidden | tail:55|ev:7|2d:7|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,344,001` vtrac=`5,1,2` hints=`A05:344:PERM,HP5 | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | -`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`066,667,006` vtrac=`6,18,23` hints=`A11:006:HOT,CONS | Combined:0/5-1/6 | 049,238,247 | Prog:27|Hidden | tail:66|ev:10|2d:10|xvar|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`499,889,599` vtrac=`35,15,33` hints=`A11:499:HOT,CONS | Combined:0/5-4/9 | 013,049,067 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:44|ev:6|2d:6|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`000` Evening=`917`
- **Delaware4**: Midday=`355` Evening=`059`
- **Florida4**: Midday=`196` Evening=`232`
- **Indiana4**: Midday=`990` Evening=`420`
- **Michigan4**: Midday=`126` Evening=`455`
- **NewJersey4**: Midday=`589` Evening=`380`
- **NewYork4**: Midday=`939` Evening=`409`
- **NorthCarolina4**: Midday=`794` Evening=`615`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-23__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
