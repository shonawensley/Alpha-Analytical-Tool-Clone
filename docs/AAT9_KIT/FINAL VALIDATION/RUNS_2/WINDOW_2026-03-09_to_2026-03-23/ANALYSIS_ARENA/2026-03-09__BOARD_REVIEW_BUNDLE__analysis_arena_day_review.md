# Board Review Bundle — analysis_arena_day_review

Purpose: one-step Brain 2 board review bundle linking the runtime overlay and compact scoreboard.

**RANK INTEGRITY STATUS: `INVALID_STATIC_ORDER`.** Analytical rank and rank-derived top-state decisions are unavailable; structural evidence remains reviewable.

**DISPLAY ORDER:** `INPUT_ROSTER_NON_ANALYTICAL`; navigation only, with no analytical meaning.

## Artifacts

- overlay_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.json`
- overlay_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.md`
- scoreboard_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__BOARD_SCOREBOARD__analysis_arena_day_review.md`
- scoreboard_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__BOARD_SCOREBOARD__analysis_arena_day_review.csv`
- scoreboard_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__BOARD_SCOREBOARD__analysis_arena_day_review.json`
- shadow_decision_policy_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__SHADOW_DECISION_POLICY__analysis_arena_day_review.md`
- shadow_decision_policy_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/ANALYSIS_ARENA/2026-03-09__SHADOW_DECISION_POLICY__analysis_arena_day_review.json`

## Workflow

- brain1_runtime_entrypoint: `scripts/tools/build_aggregated_analysis_arena.py`
- brain2_runtime_entrypoint: `scripts/tools/create_board_review_bundle.py`
- board_overlay_builder: `scripts/tools/build_board_spillover_overlay.py`
- board_scoreboard_consumer: `scripts/tools/create_board_scoreboard.py`
- shadow_decision_policy_builder: `scripts/tools/build_shadow_decision_policy.py`
- next_step: `Use this bundle as the canonical board-level review receipt before any later combination-forming or UI display work.`

## Board Verdict

- rank_evaluation: `NOT_EVALUABLE`
- rank_unavailable_reason: `INVALID_STATIC_ORDER`
- top_primary_target: `-`
- secondary_target: `-`
- best_clean_host: `-`
- best_relationship_source: `-`
- highest_context_support_state: `NorthCarolina4`
- tight_core_states: `-`
- small_shoulder_states: `Connecticut4, Delaware4, Florida4, Indiana4, Michigan4, NewJersey4, NewYork4, NorthCarolina4, Ohio4, OntarioCanada4, Pennsylvania4, PuertoRico4, SouthCarolina4, Virginia4`
- watch_only_states: `-`

## Shadow Decision Policy

- top_play_state: `-`
- top_watch_state: `-`
- play_states: `-`
- watch_states: `-`
- skip_states: `-`
- unresolved_states: `Connecticut4, Delaware4, Florida4, Indiana4, Michigan4, NewJersey4, NewYork4, NorthCarolina4, Ohio4, OntarioCanada4, Pennsylvania4, PuertoRico4, SouthCarolina4, Virginia4`

## Board Evidence Rows

| Input Order | Legacy Rank | Analytical Rank | State | Legacy Priority | Role | Targeting |
|---:|---:|---:|---|---:|---|---|
| 1 | 1 | - | Connecticut4 | 128 | shared_host | small_shoulder |
| 2 | 2 | - | Delaware4 | 118 | shared_host | small_shoulder |
| 3 | 3 | - | Florida4 | 108 | shared_host | small_shoulder |
| 4 | 4 | - | Indiana4 | 98 | shared_host | small_shoulder |
| 5 | 5 | - | Michigan4 | 88 | shared_host | small_shoulder |

## Duplicate Pairs

- `Ohio4 ↔ OntarioCanada4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ SouthCarolina4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Pennsylvania4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ SouthCarolina4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `PuertoRico4 ↔ Virginia4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`

## Shadow Decision Receipts

| Input Order | Legacy Rank | Analytical Rank | State | Posture | Mode | Cap | Route |
|---:|---:|---:|---|---|---|---|---|
| 1 | 1 | - | Connecticut4 | UNRESOLVED | boxed | unavailable | none |
| 2 | 2 | - | Delaware4 | UNRESOLVED | boxed | unavailable | none |
| 3 | 3 | - | Florida4 | UNRESOLVED | boxed | unavailable | none |
| 4 | 4 | - | Indiana4 | UNRESOLVED | boxed | unavailable | none |
| 5 | 5 | - | Michigan4 | UNRESOLVED | boxed | unavailable | none |
