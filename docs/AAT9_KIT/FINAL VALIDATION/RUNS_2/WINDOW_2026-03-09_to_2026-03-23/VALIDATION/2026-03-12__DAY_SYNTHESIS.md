# Analysis Arena Day Synthesis — D=2026-03-12 (H=2026-03-11)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-03-12`
- History date `H`: `2026-03-11`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-03-12`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-03-12.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`368,168,006` vtrac=`23,18,24` hints=`A01:068:CONS,3V | Combined:0/5-4/9 | 014,023,059 | Prog:27|Hidden | tail:06|ev:4|2d:4|xvar|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`499,599,047` vtrac=`35,22,12` hints=`A05:499:PERM,HP4 | Combined:0/5-3/8 | 048,147,246 | Prog:27|Hidden | tail:99|ev:4|2d:4|xvar|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,077,499` vtrac=`28,10,12` hints=`A05:499:PERM,HP6 | Combined:0/5-4/9 | 249,267,015 | Prog:27|Hidden | tail:99|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`788,015,688` vtrac=`29,17,27` hints=`A05:788:PERM,HP6 | Combined:0/5-4/9 | 038,058,138 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`455,688,488` vtrac=`5,33,23` hints=`A05:488:PERM,HP6 | Combined:0/5-1/6 | 012,013,014 | Prog:27|Hidden | tail:88|ev:1|2d:1|trial|moderate`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`177,244,006` vtrac=`12,31,20` hints=`A01:068:CONS,3V | Combined:0/5-1/6 | 049,247,058 | Prog:27|Hidden | tail:06|ev:5|2d:5|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`224,368,559` vtrac=`23,5,18` hints=`A05:224:PERM,HP4 | Combined:0/5-1/6 | 689,014,023 | Prog:27|Hidden | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`009,344,388` vtrac=`5,24,34` hints=`A04:349:PERSIST,BA | Combined:0/5-4/9 | 238,013,049 | Prog:27|Hidden | tail:3|ev:2|2d:1|trial|moderate`

## 2) Results Truth Map

- **Connecticut4**: Midday=`120` Evening=`802`
- **Delaware4**: Midday=`184` Evening=`763`
- **Florida4**: Midday=`708` Evening=`739`
- **Indiana4**: Midday=`021` Evening=`636`
- **Michigan4**: Midday=`212` Evening=`215`
- **NewJersey4**: Midday=`165` Evening=`725`
- **NewYork4**: Midday=`354` Evening=`865`
- **NorthCarolina4**: Midday=`314` Evening=`996`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-12__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
