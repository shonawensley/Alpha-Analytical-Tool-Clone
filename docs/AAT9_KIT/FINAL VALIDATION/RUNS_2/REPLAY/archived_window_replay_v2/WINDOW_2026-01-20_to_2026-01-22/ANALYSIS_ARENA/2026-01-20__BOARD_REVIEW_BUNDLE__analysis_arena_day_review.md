# Board Review Bundle — analysis_arena_day_review

Purpose: one-step Brain 2 board review bundle linking the runtime overlay and compact scoreboard.

## Artifacts

- overlay_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/ANALYSIS_ARENA/2026-01-20__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.json`
- overlay_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/ANALYSIS_ARENA/2026-01-20__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.md`
- scoreboard_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/ANALYSIS_ARENA/2026-01-20__BOARD_SCOREBOARD__analysis_arena_day_review.md`
- scoreboard_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/ANALYSIS_ARENA/2026-01-20__BOARD_SCOREBOARD__analysis_arena_day_review.csv`
- scoreboard_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/ANALYSIS_ARENA/2026-01-20__BOARD_SCOREBOARD__analysis_arena_day_review.json`
- shadow_decision_policy_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/ANALYSIS_ARENA/2026-01-20__SHADOW_DECISION_POLICY__analysis_arena_day_review.md`
- shadow_decision_policy_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/ANALYSIS_ARENA/2026-01-20__SHADOW_DECISION_POLICY__analysis_arena_day_review.json`

## Workflow

- brain1_runtime_entrypoint: `scripts/tools/build_aggregated_analysis_arena.py`
- brain2_runtime_entrypoint: `scripts/tools/create_board_review_bundle.py`
- board_overlay_builder: `scripts/tools/build_board_spillover_overlay.py`
- board_scoreboard_consumer: `scripts/tools/create_board_scoreboard.py`
- shadow_decision_policy_builder: `scripts/tools/build_shadow_decision_policy.py`
- next_step: `Use this bundle as the canonical board-level review receipt before any later combination-forming or UI display work.`

## Board Verdict

- top_primary_target: `Connecticut4`
- secondary_target: `Delaware4`
- best_clean_host: `Connecticut4`
- best_relationship_source: `-`
- highest_context_support_state: `Connecticut4`
- tight_core_states: `-`
- small_shoulder_states: `Connecticut4, Delaware4, Florida4`
- watch_only_states: `-`

## Shadow Decision Policy

- top_play_state: `-`
- top_watch_state: `Connecticut4`
- play_states: `-`
- watch_states: `Connecticut4, Delaware4, Florida4, Indiana4, Michigan4, NewJersey4, NewYork4, NorthCarolina4, Ohio4, OntarioCanada4, Pennsylvania4, PuertoRico4, SouthCarolina4, Virginia4`
- skip_states: `-`

## Top Scoreboard Rows

| Rank | State | Priority | Role | Targeting |
|---:|---|---:|---|---|
| 1 | Connecticut4 | 128 | shared_host | small_shoulder |
| 2 | Delaware4 | 118 | shared_host | small_shoulder |
| 3 | Florida4 | 108 | shared_host | small_shoulder |
| 4 | Indiana4 | 98 | shared_host | small_shoulder |
| 5 | Michigan4 | 88 | shared_host | small_shoulder |

## Duplicate Pairs

- `PuertoRico4 ↔ Virginia4` score=`40` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Michigan4` score=`38` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Virginia4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ NewYork4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ PuertoRico4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`

## Top Shadow Decisions

| Rank | State | Posture | Mode | Cap | Route |
|---:|---|---|---|---|---|
| 1 | Connecticut4 | WATCH | boxed | low | none |
| 2 | Delaware4 | WATCH | boxed | low | none |
| 3 | Florida4 | WATCH | boxed | low | none |
| 4 | Indiana4 | WATCH | boxed | low | none |
| 5 | Michigan4 | WATCH | boxed | low | none |
