# Analysis Arena Day Synthesis — D=2026-01-03 (H=2026-01-02)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-03`
- History date `H`: `2026-01-02`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive day dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-03`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-03.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`048,478,368` vtrac=`14,31,23` hints=`A05:006:PERM,HP2 | Combined:0/5-4/9 | 014,024,034 | Prog:27|Hidden | tail:01|ev:5|2d:5|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`449,004,599` vtrac=`5,35,31` hints=`A11:004:HOT,CONS | Combined:2/7-3/8 | 015,018,025 | Prog:27|Hidden | tail:04|ev:15|2d:14|xvar|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`138,599,559` vtrac=`23,15,5` hints=`A05:559:PERM,HP3 | Combined:0/5-3/8 | 014,023,059 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,368,668` vtrac=`23,18,31` hints=`A09::VTRAC,REP | Combined:1/6-2/7 | 019,028,046 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,668,016` vtrac=`18,2,6` hints=`A11:006:HOT,CONS | Combined:1/6-2/7 | 012,013,014 | Prog:27|Hidden | tail:06|ev:3|2d:3|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`299,599,899` vtrac=`31,15,30` hints=`A09::VTRAC,REP | Combined:3/8-4/9 | 012,019,023 | Prog:27|Hidden | -`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`788,889,038` vtrac=`7,29,3` hints=`A05:889:PERM,HP7 | Combined:0/5-1/6 | 012,013,014 | Prog:27|Hidden | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`229,224,299` vtrac=`28,5,31` hints=`A05:044:PERM,HP6 | Combined:0/5-4/9 | 025,027,049 | Prog:27|Hidden | tail:04|ev:5|2d:5|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`533` Evening=`181`
- **Delaware4**: Midday=`422` Evening=`797`
- **Florida4**: Midday=`708` Evening=`611`
- **Indiana4**: Midday=`527` Evening=`199`
- **Michigan4**: Midday=`826` Evening=`479`
- **NewJersey4**: Midday=`293` Evening=`963`
- **NewYork4**: Midday=`243` Evening=`679`
- **NorthCarolina4**: Midday=`374` Evening=`178`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-03__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
