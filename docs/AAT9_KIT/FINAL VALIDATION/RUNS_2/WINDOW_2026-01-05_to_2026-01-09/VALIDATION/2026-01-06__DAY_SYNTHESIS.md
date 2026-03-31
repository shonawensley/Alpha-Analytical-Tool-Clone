# Analysis Arena Day Synthesis — D=2026-01-06 (H=2026-01-05)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-06`
- History date `H`: `2026-01-05`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-01-06`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-06.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`224,244,468` vtrac=`28,31,30` hints=`A05:224:PERM,HP7 | Combined:0/5-4/9 | 012,014,023 | Prog:27|Hidden | tail:24|ev:3|2d:3|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`334,003,118` vtrac=`5,15,33` hints=`A04:348:PERSIST,BA | Combined:2/7-3/8 | 016,169,349 | Prog:27|Hidden | tail:03|ev:5|2d:5|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`334,033,346` vtrac=`24,33,13` hints=`A05:033:PERM,HP7 | Combined:3/8-4/9 | 059,257,023 | Prog:27|Hidden | tail:33|ev:3|2d:3|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`244,366,066` vtrac=`31,18,6` hints=`A05:244:PERM,HP6 | Combined:1/6-2/7 | 012,013,014 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`118,144,668` vtrac=`18,6,25` hints=`A05:344:PERM,HP2 | Combined:1/6-2/7 | 058,238,013 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | -`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,088,788` vtrac=`27,13,24` hints=`A05:778:PERM,HP7 | Combined:3/8-4/9 | 038,058,138 | Prog:27|Hidden | tail:08|ev:3|2d:3|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`008,005,025` vtrac=`6,3,4` hints=`A05:005:PERM,HP7 | Combined:0/5-1/6 | 016,025,124 | Prog:27|Hidden | tail:11|ev:6|2d:6|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,229,299` vtrac=`28,31,15` hints=`A05:044:PERM,HP7 | Combined:0/5-4/9 | 018,027,036 | Prog:27|Hidden | tail:44|ev:2|2d:2|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`576` Evening=`737`
- **Delaware4**: Midday=`165` Evening=`758`
- **Florida4**: Midday=`209` Evening=`160`
- **Indiana4**: Midday=`043` Evening=`961`
- **Michigan4**: Midday=`618` Evening=`578`
- **NewJersey4**: Midday=`865` Evening=`942`
- **NewYork4**: Midday=`181` Evening=`342`
- **NorthCarolina4**: Midday=`552` Evening=`298`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-06__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-06__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-06__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-06__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-06__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-06__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-06__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-06__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-06__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-06__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-06__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/VALIDATION/2026-01-06__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
