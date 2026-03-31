# Analysis Arena Day Synthesis — D=2026-01-18 (H=2026-01-17)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-18`
- History date `H`: `2026-01-17`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-01-18`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-18.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`088,559,599` vtrac=`13,29,15` hints=`A05:088:PERM,HP4 | Combined:0/5-4/9 | 029,038,047 | Prog:27|Hidden | tail:08|ev:1|2d:1|trial|moderate`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`259,007,559` vtrac=`12,5,15` hints=`A05:249:PERM,HP5 | Combined:2/7-3/8 | 014,059,149 | Prog:27|Hidden | tail:06|ev:3|2d:3|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`225,255,559` vtrac=`10,3,11` hints=`A09::VTRAC,REP | Combined:0/5-4/9 | 018,019,028 | Prog:27|Hidden | tail:07|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`077,368,559` vtrac=`18,9,6` hints=`A05:005:PERM,HP2 | Combined:1/6-2/7 | 015,123,168 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:07|ev:3|2d:3|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,177,011` vtrac=`20,17,10` hints=`A05:011:PERM,HP3 | Combined:1/6-2/7 | 025,027,038 | Prog:27|Hidden | tail:01|ev:4|2d:4|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`019,009,004` vtrac=`5,9,35` hints=`A11:009:HOT,CONS | Combined:3/8-4/9 | 569,578,029 | Prog:27|Hidden | tail:04|ev:11|2d:11|xvar|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`377,339,368` vtrac=`27,23,10` hints=`A05:339:PERM,HP4 | Combined:0/5-1/6 | 014,149,158 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:07|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,778,225` vtrac=`27,31,10` hints=`A05:244:PERM,HP7 | Combined:0/5-4/9 | 167,257,059 | Prog:27|Hidden | tail:24|ev:3|2d:3|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`238` Evening=`781`
- **Delaware4**: Midday=`490` Evening=`403`
- **Florida4**: Midday=`911` Evening=`462`
- **Indiana4**: Midday=`864` Evening=`573`
- **Michigan4**: Midday=`303` Evening=`519`
- **NewJersey4**: Midday=`238` Evening=`955`
- **NewYork4**: Midday=`682` Evening=`094`
- **NorthCarolina4**: Midday=`094` Evening=`772`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-18__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
