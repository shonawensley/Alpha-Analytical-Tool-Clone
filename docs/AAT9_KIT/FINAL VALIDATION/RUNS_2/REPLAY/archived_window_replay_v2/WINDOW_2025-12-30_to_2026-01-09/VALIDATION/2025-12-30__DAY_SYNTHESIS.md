# Analysis Arena Day Synthesis — D=2025-12-30 (H=2025-12-29)

Purpose
- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.
- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

## 0) Provenance
- Results date `D`: `2025-12-30`
- History date `H`: `2025-12-29`
- Predictive sharepacks root: `sharepacks/_predictive_replay/archived_window_replay_v2`
- Predictive day dir: `sharepacks/_predictive_replay/archived_window_replay_v2/2025-12-30`
- Validation dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Results file: `data/results/2025-12-30.txt`

## 1) Board Carry-Through Snapshot

- **Connecticut4**: `#1` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`559,011,000` vtrac=`5,2,6` hints=`A05:011:PERM,HP7 | Combined:0/5-4/9 | 167,059,068 | Prog:27|Hidden | tail:3|ev:14|2d:8|trial|strong`
- **Delaware4**: `#2` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`344,113,244` vtrac=`31,22,34` hints=`A05:113:PERM,HP7 | Combined:2/7-3/8 | 015,016,045 | Prog:27|Hidden | -`
- **Florida4**: `#3` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`778,177,677` vtrac=`20,10,23` hints=`A05:077:PERM,HP5 | Combined:0/5-3/8 | 014,068,149 | Prog:27|Hidden | tail:77|ev:1|2d:1|trial|moderate`
- **Indiana4**: `#4` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`066,116,068` vtrac=`6,16,18` hints=`A04:256:PERSIST,BA | Combined:1/6-2/7 | 127,028,037 | Prog:27|Hidden | -`
- **Michigan4**: `#5` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`599,244,136` vtrac=`18,15,3` hints=`A05:244:PERM,HP3 | Combined:1/6-2/7 | 014,024,034 | Prog:27|Hidden | tail:02|ev:2|2d:2|trial|strong`
- **NewJersey4**: `#6` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`224,118,299` vtrac=`28,18,31` hints=`A11:224:HOT,CONS | Combined:3/8-4/9 | 012,014,017 | Prog:27|Hidden | tail:44|ev:11|2d:9|trial|strong`
- **NewYork4**: `#7` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-strong` canonicals=`016,778,677` vtrac=`6,17,28` hints=`A05:778:PERM,HP6 | Combined:0/5-1/6 | 016,017,026 | Prog:27|Hidden | -`
- **NorthCarolina4**: `#8` role=`shared_host` bucket=`small_shoulder` tracker=`tracker-rich` canonicals=`224,003,005` vtrac=`1,28,5` hints=`A05:003:PERM,HP5 | Combined:0/5-4/9 | 059,149,257 | Prog:27|Hidden | tail:03|ev:4|2d:4|trial|strong`

## 2) Results Truth Map

- **Connecticut4**: Midday=`095` Evening=`467`
- **Delaware4**: Midday=`706` Evening=`563`
- **Florida4**: Midday=`377` Evening=`870`
- **Indiana4**: Midday=`585` Evening=`512`
- **Michigan4**: Midday=`250` Evening=`214`
- **NewJersey4**: Midday=`421` Evening=`356`
- **NewYork4**: Midday=`051` Evening=`132`
- **NorthCarolina4**: Midday=`455` Evening=`879`

## 3) Validation Artifact Lock

- Per-state validation reports generated: `14`
- Brain 2 Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__BRAIN2_MASTER_VALIDATION.md`
- Control Center daily report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__CONTROL_CENTER.md`
- State reports (sample): `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Connecticut4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Delaware4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Florida4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Indiana4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Michigan4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__NewJersey4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__NewYork4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__NorthCarolina4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__Ohio4.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/VALIDATION/2025-12-30__OntarioCanada4.md`

## 4) Synthesis Prompts

- Which states were true hosts vs echoes today?: `...`
- Did the board scoreboard describe the day well as a board?: `...`
- What shared complex / carryover pattern most defined the day?: `...`
- Which tracker families most shaped the day across states?: `...`
- What should be handed into the Brain 2 Master Validation report?: `...`
