# Analysis Arena Day Synthesis — D=2026-01-15 (H=2026-01-14)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-15`
- History date `H`: `2026-01-14`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive day dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-15`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-15.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`899,599,559` vtrac=`34,14,15` hints=`A05:899:PERM,HP5 | Combined:0/5-4/9 | 013,015,019 | Prog:27|Hidden | tail:09|ev:1|2d:1|trial|moderate`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`059,249,299` vtrac=`5,31,15` hints=`A04:059:PERSIST,BA | Combined:2/7-3/8 | 049,059,149 | Prog:27|Hidden | tail:04|ev:2|2d:1|trial|moderate`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`177,577,224` vtrac=`10,20,27` hints=`A05:224:PERM,HP6 | Combined:3/8-4/9 | 015,025,027 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`599,339,667` vtrac=`15,23,33` hints=`A05:339:PERM,HP7 | Combined:1/6-2/7 | 015,123,168 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`114,344,014` vtrac=`9,2,19` hints=`A09::VTRAC,REP | Combined:1/6-2/7 | 015,016,126 | Prog:27|Hidden | -`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,136,179` vtrac=`18,2,35` hints=`A11:001:HOT,CONS | Combined:3/8-4/9 | 038,128,389 | Prog:27|Hidden | tail:01|ev:5|2d:5|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`677,377,337` vtrac=`23,20,29` hints=`A05:009:PERM,HP4 | Combined:0/5-1/6 | 023,167,239 | Prog:27|Hidden | tail:09|ev:1|2d:1|trial|moderate`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`224,344,255` vtrac=`5,28,3` hints=`A04:245:PERSIST,BA | Combined:0/5-4/9 | 146,479,029 | Prog:27|Hidden | tail:00|ev:4|2d:4|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`495` Evening=`617`
- **Delaware4**: Midday=`288` Evening=`309`
- **Florida4**: Midday=`404` Evening=`647`
- **Indiana4**: Midday=`311` Evening=`094`
- **Michigan4**: Midday=`386` Evening=`664`
- **NewJersey4**: Midday=`419` Evening=`466`
- **NewYork4**: Midday=`901` Evening=`684`
- **NorthCarolina4**: Midday=`045` Evening=`912`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/VALIDATION/2026-01-15__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
