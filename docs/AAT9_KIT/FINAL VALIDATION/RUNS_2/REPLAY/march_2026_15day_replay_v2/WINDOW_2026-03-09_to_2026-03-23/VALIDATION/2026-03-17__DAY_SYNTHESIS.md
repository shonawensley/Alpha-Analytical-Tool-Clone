# Analysis Arena Day Synthesis — D=2026-03-17 (H=2026-03-16)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-03-17`
- History date `H`: `2026-03-16`
- Predictive sharepacks root: `sharepacks/_predictive_replay/march_2026_15day_replay_v2`
- Predictive day dir: `sharepacks/_predictive_replay/march_2026_15day_replay_v2/2026-03-17`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-03-17.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`344,559,139` vtrac=`34,24,5` hints=`A05:399:PERM,HP5 | Combined:0/5-4/9 | 014,023,149 | Prog:27|Hidden | tail:99|ev:2|2d:2|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,099,019` vtrac=`15,5,9` hints=`A05:099:PERM,HP5 | Combined:0/5-3/8 | 019,046,136 | Prog:27|Hidden | tail:99|ev:3|2d:3|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`668,006,255` vtrac=`18,19,25` hints=`A05:113:PERM,HP5 | Combined:0/5-4/9 | 016,026,036 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,559,224` vtrac=`15,28,5` hints=`A05:559:PERM,HP3 | Combined:0/5-4/9 | 015,016,025 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`044,667,677` vtrac=`20,15,5` hints=`A05:055:PERM,HP5 | Combined:0/5-1/6 | 019,028,046 | Prog:27|Hidden | tail:44|ev:4|2d:4|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`038,118,499` vtrac=`13,25,19` hints=`A05:499:PERM,HP6 | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | tail:99|ev:4|2d:4|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`007,668,035` vtrac=`18,7,4` hints=`A11:006:HOT,CONS | Combined:0/5-1/6 | 049,067,148 | Prog:27|Hidden | tail:03|ev:7|2d:7|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`138,366,036` vtrac=`23,18,29` hints=`A04:378:PERSIST,BA | Combined:0/5-4/9 | 247,013,049 | Prog:27|Hidden | -`

## 2) Results Truth Map

- **Connecticut4**: Midday=`991` Evening=`077`
- **Delaware4**: Midday=`471` Evening=`589`
- **Florida4**: Midday=`036` Evening=`815`
- **Indiana4**: Midday=`832` Evening=`108`
- **Michigan4**: Midday=`269` Evening=`867`
- **NewJersey4**: Midday=`876` Evening=`021`
- **NewYork4**: Midday=`829` Evening=`744`
- **NorthCarolina4**: Midday=`465` Evening=`383`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-17__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
