# Analysis Arena Day Synthesis — D=2026-03-13 (H=2026-03-12)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-03-13`
- History date `H`: `2026-03-12`
- Predictive sharepacks root: `sharepacks/_predictive_replay/march_2026_15day_replay_v2`
- Predictive day dir: `sharepacks/_predictive_replay/march_2026_15day_replay_v2/2026-03-13`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-03-13.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`368,668,336` vtrac=`23,18,24` hints=`A05:066:PERM,HP6 | Combined:0/5-4/9 | 014,149,248 | Prog:27|Hidden | tail:06|ev:3|2d:3|xvar|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`499,559,005` vtrac=`12,5,35` hints=`A05:005:PERM,HP2 | Combined:0/5-3/8 | 012,039,048 | Prog:27|Hidden | tail:07|ev:7|2d:6|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`224,499,226` vtrac=`28,20,10` hints=`A05:499:PERM,HP6 | Combined:0/5-4/9 | 012,015,023 | Prog:27|Hidden | tail:99|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,788,005` vtrac=`29,15,33` hints=`A05:005:PERM,HP2 | Combined:0/5-4/9 | 018,019,028 | Prog:27|Hidden | tail:05|ev:2|2d:2|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`688,455,559` vtrac=`5,23,4` hints=`A05:008:PERM,HP5 | Combined:0/5-1/6 | 019,028,037 | Prog:27|Hidden | tail:88|ev:1|2d:1|trial|moderate`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`244,004,167` vtrac=`31,17,5` hints=`A11:004:HOT,CONS | Combined:3/8-4/9 | 049,247,058 | Prog:27|Hidden | tail:44|ev:10|2d:10|xvar|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,039,006` vtrac=`5,18,28` hints=`A11:006:HOT,CONS | Combined:0/5-1/6 | 059,149,239 | Prog:27|Hidden | tail:93|ev:7|2d:7|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`009,388,366` vtrac=`23,5,24` hints=`A05:003:PERM,HP6 | Combined:0/5-4/9 | 058,148,238 | Prog:27|Hidden | tail:3|ev:4|2d:1|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`404` Evening=`377`
- **Delaware4**: Midday=`266` Evening=`876`
- **Florida4**: Midday=`450` Evening=`334`
- **Indiana4**: Midday=`240` Evening=`831`
- **Michigan4**: Midday=`319` Evening=`968`
- **NewJersey4**: Midday=`864` Evening=`056`
- **NewYork4**: Midday=`340` Evening=`986`
- **NorthCarolina4**: Midday=`950` Evening=`046`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-13__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
