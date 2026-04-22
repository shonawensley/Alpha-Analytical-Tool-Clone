# Analysis Arena Day Synthesis — D=2026-01-21 (H=2026-01-20)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-21`
- History date `H`: `2026-01-20`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive day dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-21`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-21.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`006,255,355` vtrac=`2,3,15` hints=`A05:001:PERM,HP4 | Combined:0/5-4/9 | 015,016,025 | Prog:27|Hidden | tail:06|ev:2|2d:2|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`255,559,336` vtrac=`5,3,23` hints=`A04:259:PERSIST,BA | Combined:0/5-4/9 | 059,257,023 | Prog:27|Hidden | tail:03|ev:2|2d:2|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`259,378,008` vtrac=`29,11,3` hints=`A05:008:PERM,HP3 | Combined:0/5-4/9 | 012,013,014 | Prog:27|Hidden | tail:08|ev:3|2d:3|trial|strong`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-support` canonicals=`001,077,244` vtrac=`10,11,31` hints=`A01:014:CONS,3V | Combined:1/6-2/7 | 014,024,034 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | tail:01|ev:6|2d:6|trial|strong`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,477,017` vtrac=`28,10,3` hints=`A01:017:CONS,3V | Combined:1/6-2/7 | 013,017,023 | Prog:27|Hidden | tail:07|ev:4|2d:4|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`001,559,004` vtrac=`5,9,2` hints=`A05:004:PERM,HP3 | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | tail:04|ev:4|2d:4|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`113,337,115` vtrac=`18,29,23` hints=`A05:337:PERM,HP6 | Combined:0/5-1/6 | 014,023,059 | LR:2|Prog:27|Hidden|multi_literal_mixed_family | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,006,366` vtrac=`27,10,2` hints=`A11:006:HOT,CONS | Combined:0/5-4/9 | 014,059,068 | Prog:27|Hidden | tail:06|ev:7|2d:7|xvar|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`786` Evening=`141`
- **Delaware4**: Midday=`029` Evening=`432`
- **Florida4**: Midday=`350` Evening=`284`
- **Indiana4**: Midday=`458` Evening=`612`
- **Michigan4**: Midday=`220` Evening=`221`
- **NewJersey4**: Midday=`185` Evening=`786`
- **NewYork4**: Midday=`616` Evening=`233`
- **NorthCarolina4**: Midday=`767` Evening=`577`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/VALIDATION/2026-01-21__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
