# Analysis Arena Day Synthesis — D=2026-01-20 (H=2026-01-19)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-20`
- History date `H`: `2026-01-19`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-01-20`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-20.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`006,005,255` vtrac=`3,2,1` hints=`A05:355:PERM,HP3 | Combined:0/5-4/9 | 038,056,029 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`559,259,007` vtrac=`5,12,15` hints=`A04:259:PERSIST,BA | Combined:0/5-4/9 | 059,257,023 | Prog:27|Hidden | tail:03|ev:2|2d:2|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`378,255,259` vtrac=`29,3,27` hints=`A05:778:PERM,HP4 | Combined:0/5-4/9 | 017,027,037 | Prog:27|Hidden | tail:07|ev:3|2d:3|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`077,224,007` vtrac=`10,28,23` hints=`A11:007:HOT,CONS | Combined:1/6-2/7 | 012,023,024 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:07|ev:6|2d:6|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,778,007` vtrac=`28,10,27` hints=`A05:224:PERM,HP7 | Combined:1/6-2/7 | 016,017,026 | Prog:27|Hidden | tail:07|ev:5|2d:5|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,559,004` vtrac=`5,9,2` hints=`A11:001:HOT,CONS | Combined:3/8-4/9 | 047,056,128 | Prog:27|Hidden | tail:04|ev:9|2d:9|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`378,377,113` vtrac=`29,18,27` hints=`A09::VTRAC,REP | Combined:0/5-1/6 | 014,023,149 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,244,368` vtrac=`27,31,10` hints=`A05:244:PERM,HP6 | Combined:0/5-4/9 | 014,068,149 | Prog:27|Hidden | tail:04|ev:6|2d:6|xvar|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`587` Evening=`961`
- **Delaware4**: Midday=`099` Evening=`106`
- **Florida4**: Midday=`743` Evening=`406`
- **Indiana4**: Midday=`965` Evening=`208`
- **Michigan4**: Midday=`616` Evening=`881`
- **NewJersey4**: Midday=`866` Evening=`689`
- **NewYork4**: Midday=`479` Evening=`406`
- **NorthCarolina4**: Midday=`254` Evening=`084`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-20__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-20__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-20__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-20__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-20__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-20__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-20__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-20__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-20__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-20__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-20__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-20__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
