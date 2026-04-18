# Analysis Arena Day Synthesis — D=2026-01-09 (H=2026-01-08)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-09`
- History date `H`: `2026-01-08`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-01-09`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-09.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,448,229` vtrac=`28,34,31` hints=`A09::VTRAC,REP | Combined:0/5-4/9 | 012,014,018 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`344,033,445` vtrac=`15,34,13` hints=`A05:033:PERM,HP6 | Combined:2/7-3/8 | 034,124,349 | Prog:27|Hidden | tail:33|ev:7|2d:7|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`255,559,224` vtrac=`3,5,33` hints=`A05:224:PERM,HP4 | Combined:3/8-4/9 | 068,158,167 | Prog:27|Hidden | tail:55|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`244,669,004` vtrac=`5,9,19` hints=`A05:004:PERM,HP2 | Combined:1/6-2/7 | 017,027,037 | Prog:27|Hidden | tail:04|ev:2|2d:2|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`334,019,059` vtrac=`15,5,33` hints=`A05:334:PERM,HP3 | Combined:1/6-2/7 | 012,013,014 | Prog:27|Hidden | tail:44|ev:2|2d:1|trial|moderate`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,137,014` vtrac=`4,27,12` hints=`A05:003:PERM,HP2 | Combined:3/8-4/9 | 015,016,025 | Prog:27|Hidden | tail:03|ev:3|2d:3|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`005,001,255` vtrac=`3,5,1` hints=`A11:005:HOT,CONS | Combined:0/5-1/6 | 015,016,025 | Prog:27|Hidden | tail:05|ev:7|2d:7|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`299,066,446` vtrac=`15,31,25` hints=`A05:066:PERM,HP6 | Combined:0/5-4/9 | 036,126,369 | Prog:27|Hidden | -`

## 2) Results Truth Map

- **Connecticut4**: Midday=`234` Evening=`513`
- **Delaware4**: Midday=`843` Evening=`681`
- **Florida4**: Midday=`860` Evening=`093`
- **Indiana4**: Midday=`219` Evening=`377`
- **Michigan4**: Midday=`842` Evening=`273`
- **NewJersey4**: Midday=`287` Evening=`028`
- **NewYork4**: Midday=`989` Evening=`835`
- **NorthCarolina4**: Midday=`177` Evening=`960`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-09__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-09__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-09__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-09__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-09__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-09__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-09__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-09__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-09__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-09__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-09__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-09__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
