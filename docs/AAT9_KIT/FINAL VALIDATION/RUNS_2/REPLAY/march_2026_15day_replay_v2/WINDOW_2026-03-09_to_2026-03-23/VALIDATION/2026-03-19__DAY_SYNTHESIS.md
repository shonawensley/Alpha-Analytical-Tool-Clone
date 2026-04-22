# Analysis Arena Day Synthesis — D=2026-03-19 (H=2026-03-18)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-03-19`
- History date `H`: `2026-03-18`
- Predictive sharepacks root: `sharepacks/_predictive_replay/march_2026_15day_replay_v2`
- Predictive day dir: `sharepacks/_predictive_replay/march_2026_15day_replay_v2/2026-03-19`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-03-19.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,113,355` vtrac=`18,34,5` hints=`A05:224:PERM,HP4 | Combined:0/5-4/9 | 012,013,015 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`099,001,069` vtrac=`15,9,2` hints=`A04:069:PERSIST,BA | Combined:0/5-3/8 | 127,136,469 | Prog:27|Hidden | tail:93|ev:5|2d:3|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,224,244` vtrac=`22,28,19` hints=`A05:224:PERM,HP3 | Combined:0/5-4/9 | 012,023,024 | Prog:27|Hidden | tail:06|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,599,455` vtrac=`5,15,9` hints=`A05:599:PERM,HP6 | Combined:0/5-4/9 | 015,025,035 | Prog:27|Hidden | tail:4|ev:2|2d:1|trial|moderate`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,001,059` vtrac=`5,2,15` hints=`A11:009:HOT,CONS | Combined:0/5-1/6 | 037,136,235 | Prog:27|Hidden | tail:09|ev:6|2d:6|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`499,559,023` vtrac=`5,35,25` hints=`A01:049:CONS,3V | Combined:3/8-4/9 | 015,025,035 | Prog:27|Hidden | tail:94|ev:6|2d:6|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`036,066,366` vtrac=`8,6,17` hints=`A09::VTRAC,REP | Combined:0/5-1/6 | 013,049,058 | Prog:27|Hidden | tail:66|ev:2|2d:2|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`299,112,117` vtrac=`17,20,31` hints=`A05:008:PERM,HP2 | Combined:0/5-4/9 | 049,238,247 | Prog:27|Hidden | tail:08|ev:5|2d:5|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`699` Evening=`795`
- **Delaware4**: Midday=`286` Evening=`295`
- **Florida4**: Midday=`752` Evening=`801`
- **Indiana4**: Midday=`764` Evening=`790`
- **Michigan4**: Midday=`398` Evening=`851`
- **NewJersey4**: Midday=`822` Evening=`686`
- **NewYork4**: Midday=`303` Evening=`047`
- **NorthCarolina4**: Midday=`611` Evening=`236`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-19__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
