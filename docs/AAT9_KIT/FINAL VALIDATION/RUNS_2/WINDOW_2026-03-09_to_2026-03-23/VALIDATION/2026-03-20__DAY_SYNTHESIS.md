# Analysis Arena Day Synthesis — D=2026-03-20 (H=2026-03-19)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-03-20`
- History date `H`: `2026-03-19`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-03-20`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-03-20.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,113,133` vtrac=`18,28,23` hints=`A05:224:PERM,HP6 | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,099,399` vtrac=`2,15,5` hints=`A05:399:PERM,HP7 | Combined:0/5-3/8 | 019,028,037 | Prog:27|Hidden | tail:93|ev:3|2d:2|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`244,114,246` vtrac=`31,22,28` hints=`A05:244:PERM,HP4 | Combined:0/5-4/9 | 013,014,016 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,455,155` vtrac=`5,12,15` hints=`A05:559:PERM,HP2 | Combined:0/5-4/9 | 012,015,023 | Prog:27|Hidden | tail:55|ev:3|2d:2|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,001,677` vtrac=`5,2,1` hints=`A05:055:PERM,HP4 | Combined:0/5-1/6 | 046,145,469 | Prog:27|Hidden | tail:05|ev:7|2d:7|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,499,334` vtrac=`5,35,15` hints=`A01:049:CONS,3V | Combined:3/8-4/9 | 013,014,015 | Prog:27|Hidden | tail:94|ev:6|2d:6|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`066,035,667` vtrac=`6,17,4` hints=`A11:066:HOT,CONS | Combined:0/5-1/6 | 013,067,139 | Prog:27|Hidden | tail:66|ev:6|2d:6|xvar|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`299,117,088` vtrac=`31,17,15` hints=`A04:348:PERSIST,BA | Combined:0/5-4/9 | 049,058,139 | Prog:27|Hidden | tail:4|ev:8|2d:4|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`936` Evening=`592`
- **Delaware4**: Midday=`799` Evening=`248`
- **Florida4**: Midday=`033` Evening=`397`
- **Indiana4**: Midday=`515` Evening=`884`
- **Michigan4**: Midday=`780` Evening=`032`
- **NewJersey4**: Midday=`337` Evening=`688`
- **NewYork4**: Midday=`401` Evening=`055`
- **NorthCarolina4**: Midday=`532` Evening=`807`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-20__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
