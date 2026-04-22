# Analysis Arena Day Synthesis — D=2026-03-16 (H=2026-03-15)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-03-16`
- History date `H`: `2026-03-15`
- Predictive sharepacks root: `sharepacks/_predictive_replay/march_2026_15day_replay_v2`
- Predictive day dir: `sharepacks/_predictive_replay/march_2026_15day_replay_v2/2026-03-16`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-03-16.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,344,044` vtrac=`5,24,18` hints=`A05:559:PERM,HP6 | Combined:0/5-4/9 | 014,023,059 | Prog:27|Hidden | tail:01|ev:1|2d:1|trial|moderate`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,559,059` vtrac=`15,5,34` hints=`A09::VTRAC,REP | Combined:0/5-3/8 | 469,019,127 | Prog:27|Hidden | tail:3|ev:6|2d:3|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`668,006,669` vtrac=`18,19,3` hints=`A05:669:PERM,HP5 | Combined:0/5-4/9 | 038,056,128 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,224,559` vtrac=`15,28,31` hints=`A05:224:PERM,HP3 | Combined:0/5-4/9 | 027,279,378 | Prog:27|Hidden | tail:05|ev:3|2d:3|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`044,067,677` vtrac=`15,5,20` hints=`A09::VTRAC,REP | Combined:0/5-1/6 | 019,028,127 | Prog:27|Hidden | tail:44|ev:3|2d:3|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,099,179` vtrac=`31,2,15` hints=`A05:099:PERM,HP4 | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | tail:99|ev:5|2d:5|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`668,003,559` vtrac=`18,15,21` hints=`A01:035:CONS,3V | Combined:0/5-1/6 | 067,256,346 | Prog:27|Hidden | tail:03|ev:8|2d:8|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`138,378,366` vtrac=`23,29,18` hints=`A05:003:PERM,HP7 | Combined:0/5-4/9 | 013,058,139 | Prog:27|Hidden | tail:03|ev:2|2d:1|trial|moderate`

## 2) Results Truth Map

- **Connecticut4**: Midday=`766` Evening=`700`
- **Delaware4**: Midday=`722` Evening=`545`
- **Florida4**: Midday=`390` Evening=`884`
- **Indiana4**: Midday=`279` Evening=`276`
- **Michigan4**: Midday=`818` Evening=`454`
- **NewJersey4**: Midday=`476` Evening=`206`
- **NewYork4**: Midday=`159` Evening=`797`
- **NorthCarolina4**: Midday=`356` Evening=`005`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-16__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
