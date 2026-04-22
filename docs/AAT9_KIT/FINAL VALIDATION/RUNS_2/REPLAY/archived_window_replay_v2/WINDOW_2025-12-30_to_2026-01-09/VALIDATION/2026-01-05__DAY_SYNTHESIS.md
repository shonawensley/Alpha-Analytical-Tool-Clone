# Analysis Arena Day Synthesis — D=2026-01-05 (H=2026-01-04)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-05`
- History date `H`: `2026-01-04`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive day dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-05`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-05.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,447,024` vtrac=`28,31,12` hints=`A05:024:PERM,HP2 | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | tail:24|ev:3|2d:3|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`449,244,004` vtrac=`5,31,35` hints=`A05:449:PERM,HP7 | Combined:2/7-3/8 | 012,013,014 | Prog:27|Hidden | tail:04|ev:7|2d:7|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`344,033,334` vtrac=`33,15,34` hints=`A05:033:PERM,HP7 | Combined:0/5-3/8 | 014,023,149 | Prog:27|Hidden | tail:33|ev:4|2d:4|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,668,066` vtrac=`31,18,23` hints=`A05:244:PERM,HP6 | Combined:1/6-2/7 | 012,013,014 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`168,118,668` vtrac=`18,6,23` hints=`A05:011:PERM,HP3 | Combined:1/6-2/7 | 013,049,058 | Prog:27|Hidden | -`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,008,599` vtrac=`4,27,15` hints=`A11:008:HOT,CONS | Combined:3/8-4/9 | 015,016,025 | Prog:27|Hidden | tail:08|ev:3|2d:3|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`025,008,005` vtrac=`3,6,7` hints=`A09::VTRAC,REP | Combined:0/5-1/6 | 015,016,025 | Prog:27|Hidden | tail:08|ev:2|2d:2|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`229,224,299` vtrac=`28,15,31` hints=`A05:044:PERM,HP7 | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | tail:44|ev:4|2d:4|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`071` Evening=`660`
- **Delaware4**: Midday=`978` Evening=`267`
- **Florida4**: Midday=`080` Evening=`994`
- **Indiana4**: Midday=`187` Evening=`629`
- **Michigan4**: Midday=`260` Evening=`772`
- **NewJersey4**: Midday=`604` Evening=`694`
- **NewYork4**: Midday=`080` Evening=`735`
- **NorthCarolina4**: Midday=`553` Evening=`895`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-05__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
