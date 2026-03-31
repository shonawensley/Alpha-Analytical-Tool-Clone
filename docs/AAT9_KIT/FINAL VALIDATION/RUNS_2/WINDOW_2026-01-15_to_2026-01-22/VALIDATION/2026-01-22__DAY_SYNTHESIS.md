# Analysis Arena Day Synthesis — D=2026-01-22 (H=2026-01-21)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-22`
- History date `H`: `2026-01-21`
- Predictive sharepacks root: `sharepacks/_predictive`
- Predictive day dir: `sharepacks/_predictive/2026-01-22`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-22.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`005,006,255` vtrac=`1,2,4` hints=`A09::VTRAC,REP | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,255,336` vtrac=`5,12,23` hints=`A05:133:PERM,HP6 | Combined:0/5-4/9 | 059,068,158 | Prog:27|Hidden | tail:03|ev:2|2d:2|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`007,259,224` vtrac=`3,10,21` hints=`A11:007:HOT,CONS | Combined:0/5-2/7 | 012,013,014 | Prog:27|Hidden | tail:07|ev:4|2d:4|xvar|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`077,001,003` vtrac=`11,10,21` hints=`A01:014:CONS,3V | Combined:1/6-2/7 | 057,138,237 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:01|ev:8|2d:8|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`224,477,559` vtrac=`28,10,12` hints=`A01:027:CONS,3V | Combined:1/6-2/7 | 013,015,017 | Prog:27|Hidden | tail:07|ev:5|2d:4|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`017,299,009` vtrac=`5,7,31` hints=`A05:299:PERM,HP4 | Combined:3/8-4/9 | 012,013,023 | Prog:27|Hidden | -`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`238,337,133` vtrac=`29,23,13` hints=`A05:337:PERM,HP6 | Combined:0/5-1/6 | 059,068,158 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`113,778,011` vtrac=`18,27,31` hints=`A05:006:PERM,HP2 | Combined:0/5-4/9 | 014,023,059 | Prog:27|Hidden | tail:06|ev:3|2d:3|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`556` Evening=`345`
- **Delaware4**: Midday=`288` Evening=`243`
- **Florida4**: Midday=`093` Evening=`116`
- **Indiana4**: Midday=`286` Evening=`757`
- **Michigan4**: Midday=`428` Evening=`652`
- **NewJersey4**: Midday=`862` Evening=`152`
- **NewYork4**: Midday=`981` Evening=`787`
- **NorthCarolina4**: Midday=`731` Evening=`845`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-22__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-22__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-22__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-22__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-22__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-22__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-22__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-22__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-22__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-22__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-22__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-22__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
