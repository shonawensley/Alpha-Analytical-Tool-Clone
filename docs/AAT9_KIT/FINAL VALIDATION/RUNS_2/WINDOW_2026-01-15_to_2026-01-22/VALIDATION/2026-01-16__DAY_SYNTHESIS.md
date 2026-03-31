# Analysis Arena Day Synthesis — D=2026-01-16 (H=2026-01-15)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-16`
- History date `H`: `2026-01-15`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-01-16`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-16.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`899,599,389` vtrac=`34,15,33` hints=`A05:899:PERM,HP5 | Combined:0/5-4/9 | 035,038,058 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`009,249,059` vtrac=`5,31,15` hints=`A05:599:PERM,HP5 | Combined:2/7-3/8 | 012,013,014 | Prog:27|Hidden | -`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`225,577,255` vtrac=`10,27,20` hints=`A05:223:PERM,HP4 | Combined:3/8-4/9 | 012,015,018 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`368,599,366` vtrac=`23,18,15` hints=`A04:368:PERSIST,BA | Combined:1/6-2/7 | 015,024,123 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`344,245,559` vtrac=`12,6,34` hints=`A05:011:PERM,HP3 | Combined:1/6-2/7 | 012,013,014 | Prog:27|Hidden | tail:01|ev:2|2d:2|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,008,019` vtrac=`18,9,4` hints=`A05:788:PERM,HP3 | Combined:3/8-4/9 | 578,038,128 | Prog:27|Hidden | tail:01|ev:2|2d:2|xvar|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`337,377,334` vtrac=`29,23,33` hints=`A09::VTRAC,REP | Combined:0/5-1/6 | 023,167,239 | Prog:27|Hidden | tail:09|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,344,255` vtrac=`28,34,27` hints=`A05:224:PERM,HP4 | Combined:0/5-4/9 | 038,047,137 | Prog:27|Hidden | tail:00|ev:3|2d:3|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`319` Evening=`431`
- **Delaware4**: Midday=`902` Evening=`107`
- **Florida4**: Midday=`273` Evening=`100`
- **Indiana4**: Midday=`954` Evening=`836`
- **Michigan4**: Midday=`946` Evening=`633`
- **NewJersey4**: Midday=`877` Evening=`180`
- **NewYork4**: Midday=`539` Evening=`496`
- **NorthCarolina4**: Midday=`169` Evening=`083`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-16__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-16__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-16__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-16__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-16__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-16__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-16__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-16__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-16__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-16__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-16__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-16__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
