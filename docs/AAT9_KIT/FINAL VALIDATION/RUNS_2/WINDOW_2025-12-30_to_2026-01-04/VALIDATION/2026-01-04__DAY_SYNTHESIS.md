# Analysis Arena Day Synthesis — D=2026-01-04 (H=2026-01-03)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-04`
- History date `H`: `2026-01-03`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-01-04`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-04.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`224,456,024` vtrac=`28,9,31` hints=`A05:004:PERM,HP2 | Combined:0/5-4/9 | 012,014,023 | Prog:27|Hidden | tail:06|ev:4|2d:4|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`449,559,004` vtrac=`5,35,15` hints=`A09::VTRAC,REP | Combined:2/7-3/8 | 015,018,025 | Prog:27|Hidden | tail:04|ev:10|2d:9|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`344,334,033` vtrac=`33,23,15` hints=`A04:346:PERSIST,BA | Combined:0/5-3/8 | 149,014,023 | Prog:27|Hidden | tail:33|ev:2|2d:2|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,668,138` vtrac=`18,23,31` hints=`A05:244:PERM,HP7 | Combined:1/6-2/7 | 016,018,026 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`168,668,156` vtrac=`18,6,19` hints=`A05:446:PERM,HP4 | Combined:1/6-2/7 | 013,049,058 | Prog:27|Hidden | -`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`599,299,229` vtrac=`31,15,12` hints=`A05:778:PERM,HP6 | Combined:3/8-4/9 | 017,018,027 | Prog:27|Hidden | -`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`038,005,025` vtrac=`3,13,33` hints=`A05:889:PERM,HP6 | Combined:0/5-1/6 | 012,013,014 | Prog:27|Hidden | tail:88|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`229,299,044` vtrac=`28,15,31` hints=`A05:044:PERM,HP7 | Combined:0/5-4/9 | 012,016,019 | Prog:27|Hidden | tail:44|ev:4|2d:4|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`569` Evening=`311`
- **Delaware4**: Midday=`057` Evening=`269`
- **Florida4**: Midday=`171` Evening=`871`
- **Indiana4**: Midday=`813` Evening=`517`
- **Michigan4**: Midday=`539` Evening=`324`
- **NewJersey4**: Midday=`275` Evening=`261`
- **NewYork4**: Midday=`793` Evening=`489`
- **NorthCarolina4**: Midday=`187` Evening=`887`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2026-01-04__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
