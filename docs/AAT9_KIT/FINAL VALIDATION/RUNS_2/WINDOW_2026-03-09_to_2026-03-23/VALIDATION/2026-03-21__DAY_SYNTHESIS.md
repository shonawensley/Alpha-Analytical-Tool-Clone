# Analysis Arena Day Synthesis — D=2026-03-21 (H=2026-03-20)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-03-21`
- History date `H`: `2026-03-20`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-03-21`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-03-21.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`113,224,355` vtrac=`18,28,4` hints=`A09::VTRAC,REP | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,599,016` vtrac=`2,15,6` hints=`A05:599:PERM,HP6 | Combined:0/5-3/8 | 019,028,037 | Prog:27|Hidden | tail:3|ev:1|light`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,246,114` vtrac=`31,22,19` hints=`A05:224:PERM,HP3 | Combined:0/5-4/9 | 014,016,024 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,455,002` vtrac=`5,3,28` hints=`A11:022:HOT,CONS | Combined:0/5-4/9 | 012,023,024 | Prog:27|Hidden | tail:02|ev:7|2d:6|xvar|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`567,001,599` vtrac=`5,2,15` hints=`A11:445:HOT,CONS | Combined:0/5-1/6 | 046,136,145 | Prog:27|Hidden | tail:03|ev:5|2d:5|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`455,559,499` vtrac=`5,4,1` hints=`A05:003:PERM,HP5 | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | tail:03|ev:4|2d:4|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`066,667,013` vtrac=`6,17,18` hints=`A11:066:HOT,CONS | Combined:0/5-1/6 | 058,238,049 | Prog:27|Hidden | tail:66|ev:6|2d:6|xvar|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`499,117,889` vtrac=`35,33,17` hints=`A11:499:HOT,CONS | Combined:0/5-4/9 | 049,139,148 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:94|ev:14|2d:9|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`954` Evening=`394`
- **Delaware4**: Midday=`547` Evening=`888`
- **Florida4**: Midday=`466` Evening=`465`
- **Indiana4**: Midday=`912` Evening=`230`
- **Michigan4**: Midday=`276` Evening=`699`
- **NewJersey4**: Midday=`992` Evening=`950`
- **NewYork4**: Midday=`271` Evening=`899`
- **NorthCarolina4**: Midday=`550` Evening=`537`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-21__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
