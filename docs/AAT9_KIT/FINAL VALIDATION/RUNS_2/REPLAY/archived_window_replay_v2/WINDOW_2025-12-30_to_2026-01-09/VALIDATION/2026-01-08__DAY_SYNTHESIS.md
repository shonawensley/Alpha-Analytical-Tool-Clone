# Analysis Arena Day Synthesis — D=2026-01-08 (H=2026-01-07)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2026-01-08`
- History date `H`: `2026-01-07`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive day dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2026-01-08`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2026-01-08.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,229,448` vtrac=`28,34,30` hints=`A05:224:PERM,HP7 | Combined:0/5-4/9 | 012,018,019 | Prog:27|Hidden | -`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`033,334,003` vtrac=`13,15,33` hints=`A09::VTRAC,REP | Combined:2/7-3/8 | 016,025,034 | Prog:27|Hidden | tail:33|ev:13|2d:12|xvar|trial|strong`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`334,346,335` vtrac=`33,24,13` hints=`A05:334:PERM,HP4 | Combined:3/8-4/9 | 023,068,158 | Prog:27|Hidden | -`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`244,066,669` vtrac=`5,31,6` hints=`A05:344:PERM,HP4 | Combined:1/6-2/7 | 015,017,025 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`344,019,144` vtrac=`5,34,15` hints=`A05:344:PERM,HP4 | Combined:1/6-2/7 | 015,016,025 | Prog:27|Hidden | tail:44|ev:1|2d:1|trial|moderate`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,189,089` vtrac=`27,4,3` hints=`A05:778:PERM,HP5 | Combined:3/8-4/9 | 012,013,014 | Prog:27|Hidden | tail:03|ev:1|2d:1|trial|moderate`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`005,008,256` vtrac=`3,7,6` hints=`A11:005:HOT,CONS | Combined:0/5-1/6 | 012,013,014 | Prog:27|Hidden | tail:05|ev:3|2d:3|trial|strong`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`299,244,559` vtrac=`31,5,25` hints=`A05:244:PERM,HP6 | Combined:0/5-4/9 | 027,036,126 | Prog:27|Hidden | -`

## 2) Results Truth Map

- **Connecticut4**: Midday=`106` Evening=`331`
- **Delaware4**: Midday=`820` Evening=`031`
- **Florida4**: Midday=`429` Evening=`596`
- **Indiana4**: Midday=`325` Evening=`242`
- **Michigan4**: Midday=`824` Evening=`567`
- **NewJersey4**: Midday=`089` Evening=`055`
- **NewYork4**: Midday=`199` Evening=`732`
- **NorthCarolina4**: Midday=`132` Evening=`571`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2026-01-08__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
