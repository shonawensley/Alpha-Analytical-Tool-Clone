# Analysis Arena Day Synthesis — D=2026-03-09 (H=2026-03-08)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-03-09`
- History date `H`: `2026-03-08`
- Predictive sharepacks root: `sharepacks/_predictive_replay/march_2026_15day_replay_v2`
- Predictive day dir: `sharepacks/_predictive_replay/march_2026_15day_replay_v2/2026-03-09`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-03-09.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`168,189,006` vtrac=`18,9,25` hints=`A04:168:PERSIST,BA | Combined:0/5-4/9 | 149,167,014 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,129,259` vtrac=`12,31,2` hints=`A11:006:HOT,CONS | Combined:0/5-3/8 | 012,013,014 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:06|ev:3|2d:3|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,778,889` vtrac=`28,33,27` hints=`A05:224:PERM,HP7 | Combined:0/5-4/9 | 036,045,126 | Prog:27|Hidden | tail:24|ev:2|2d:2|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`011,225,255` vtrac=`3,10,6` hints=`A04:078:PERSIST,BA | Combined:0/5-4/9 | 016,025,027 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`118,778,188` vtrac=`18,27,23` hints=`A05:119:PERM,HP3 | Combined:0/5-1/6 | 012,013,014 | Prog:27|Hidden | -`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,177,007` vtrac=`20,28,12` hints=`A11:006:HOT,CONS | Combined:0/5-1/6 | 013,049,058 | Prog:27|Hidden | tail:06|ev:7|2d:7|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,368,689` vtrac=`5,23,24` hints=`A05:559:PERM,HP4 | Combined:0/5-1/6 | 023,059,149 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`599,003,344` vtrac=`15,4,5` hints=`A04:035:PERSIST,BA | Combined:0/5-4/9 | 049,058,247 | Prog:27|Hidden | tail:03|ev:5|2d:5|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`917` Evening=`091`
- **Delaware4**: Midday=`884` Evening=`062`
- **Florida4**: Midday=`383` Evening=`941`
- **Indiana4**: Midday=`203` Evening=`965`
- **Michigan4**: Midday=`373` Evening=`116`
- **NewJersey4**: Midday=`617` Evening=`302`
- **NewYork4**: Midday=`900` Evening=`298`
- **NorthCarolina4**: Midday=`855` Evening=`000`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
