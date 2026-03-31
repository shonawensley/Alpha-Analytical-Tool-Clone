# Analysis Arena Day Synthesis — D=2026-01-07 (H=2026-01-06)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-07`
- History date `H`: `2026-01-06`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-01-07`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-07.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,244,229` vtrac=`28,31,30` hints=`A09::VTRAC,REP | Combined:0/5-4/9 | 012,014,018 | Prog:27|Hidden | tail:24|ev:2|2d:2|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`334,003,044` vtrac=`33,15,4` hints=`A01:038:CONS,3V | Combined:2/7-3/8 | 016,025,034 | Prog:27|Hidden | tail:03|ev:6|2d:6|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`334,346,336` vtrac=`33,24,23` hints=`A05:033:PERM,HP4 | Combined:3/8-4/9 | 059,257,023 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,066,004` vtrac=`31,6,18` hints=`A05:244:PERM,HP5 | Combined:1/6-2/7 | 015,016,025 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`668,011,001` vtrac=`6,18,15` hints=`A05:344:PERM,HP3 | Combined:1/6-2/7 | 049,139,589 | Prog:27|Hidden | tail:44|ev:1|2d:1|trial|moderate`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,189,088` vtrac=`24,27,13` hints=`A05:778:PERM,HP7 | Combined:3/8-4/9 | 027,035,038 | Prog:27|Hidden | -`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`008,001,667` vtrac=`6,4,2` hints=`A05:001:PERM,HP5 | Combined:0/5-1/6 | 016,169,268 | Prog:27|Hidden | tail:08|ev:3|2d:3|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`299,244,229` vtrac=`31,28,25` hints=`A05:244:PERM,HP7 | Combined:0/5-4/9 | 018,027,036 | Prog:27|Hidden | -`

## 2) Results Truth Map

- **Connecticut4**: Midday=`156` Evening=`553`
- **Delaware4**: Midday=`657` Evening=`922`
- **Florida4**: Midday=`434` Evening=`963`
- **Indiana4**: Midday=`823` Evening=`290`
- **Michigan4**: Midday=`692` Evening=`616`
- **NewJersey4**: Midday=`361` Evening=`847`
- **NewYork4**: Midday=`916` Evening=`286`
- **NorthCarolina4**: Midday=`184` Evening=`202`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-07__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-07__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-07__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-07__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-07__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-07__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-07__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-07__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-07__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-07__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-07__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-07__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
