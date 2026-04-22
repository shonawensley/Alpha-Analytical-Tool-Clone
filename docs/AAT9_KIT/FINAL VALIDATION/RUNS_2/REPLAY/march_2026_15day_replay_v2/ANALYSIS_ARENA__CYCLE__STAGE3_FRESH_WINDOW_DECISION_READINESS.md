# Stage 3 Fresh-Window Decision Readiness

Purpose: lock how Stage-3 evidence should be used before the next fresh window.

## Permission Model

- Approved now: observation, replay, casebook review, decay/watch interpretation, negative-control restraint.
- Blocked now: live scoring changes, live budget changes, automatic candidate promotion.
- Required before scoring rewrite: replay candidates must survive cross-window fixture replay with denominator controls.

## Decision Mix

- `needs_more_windows`: `3451`
- `watch_decay_only`: `581`
- `needs_replay`: `64`
- `negative_control`: `17`

## Highest Priority Replay

- `P3_vtrac_decay_watch_replay` `translation_sandbox:diagnostic_vt_box_seed` windows=`1` support=`39.1%` match=`6.3%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::old_candidate_universe:candidate_universe_union_combo + translation_sandbox:diagnostic_vt_box_seed` windows=`1` support=`35.0%` match=`6.4%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::old_candidate_universe:pack_method:stable_top:canonical + translation_sandbox:diagnostic_vt_box_seed` windows=`1` support=`29.0%` match=`6.3%`
- `P3_vtrac_decay_watch_replay` `vtrac_overlap::brain1:dominant_vtrac_indices + translation_sandbox:diagnostic_vt_box_seed` windows=`1` support=`28.0%` match=`6.5%`
- `P3_vtrac_decay_watch_replay` `brain1:dominant_vtrac_indices` windows=`1` support=`28.0%` match=`6.5%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:candidate_universe_union_combo` windows=`1` support=`26.8%` match=`6.5%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::old_candidate_universe:pack:stable_top + translation_sandbox:diagnostic_vt_box_seed` windows=`1` support=`26.6%` match=`6.2%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack_method:stable_top:canonical` windows=`1` support=`24.4%` match=`6.4%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::translation_sandbox:diagnostic_boxed_seed + translation_sandbox:diagnostic_vt_box_seed` windows=`1` support=`23.9%` match=`6.4%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::brain1:secondary_canonicals + translation_sandbox:diagnostic_vt_box_seed` windows=`1` support=`22.7%` match=`7.0%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack:stable_top` windows=`1` support=`22.7%` match=`6.2%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::old_play_card:strategy:v0_2_default:B36:combos + translation_sandbox:diagnostic_vt_box_seed` windows=`1` support=`21.5%` match=`6.1%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:candidate_universe_union_combo` windows=`1` support=`20.0%` match=`6.5%`
- `P3_vtrac_decay_watch_replay` `brain1:watchlist_indices` windows=`1` support=`20.0%` match=`6.4%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::brain1:dominant_canonicals + translation_sandbox:diagnostic_vt_box_seed` windows=`1` support=`19.8%` match=`6.2%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::brain1:dominant_vtrac_indices + translation_sandbox:diagnostic_boxed_seed` windows=`1` support=`19.1%` match=`6.4%`
- `P3_vtrac_decay_watch_replay` `vtrac_overlap::brain1:watchlist_indices + translation_sandbox:diagnostic_vt_box_seed` windows=`1` support=`18.8%` match=`6.4%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::old_play_card:strategy:v0_2_default:B24:combos + translation_sandbox:diagnostic_vt_box_seed` windows=`1` support=`18.6%` match=`6.6%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:pack_method:stable_top:canonical` windows=`1` support=`18.6%` match=`6.3%`
- `P3_vtrac_decay_watch_replay` `vtrac_box_confirmation::brain1:dominant_canonicals + brain1:dominant_vtrac_indices` windows=`1` support=`18.6%` match=`6.3%`

## Highest Priority Restraints

- `old_candidate_universe:pack:PackB_mirror3rd` role=`negative_control` windows=`1` false_proxy=`95.9%`
- `old_play_card:strategy:v0_2_default:B24:boxed_canonicals` role=`negative_control` windows=`1` false_proxy=`95.8%`
- `due_doubles:example_canonicals` role=`negative_control` windows=`1` false_proxy=`95.7%`
- `old_play_card:strategy:v0_2_default:B36:boxed_canonicals` role=`negative_control` windows=`1` false_proxy=`95.5%`
- `old_candidate_universe:pack_method:PackA_vt8:canonical` role=`negative_control` windows=`1` false_proxy=`95.3%`
- `old_candidate_universe:pack_method:PackB_mirror3rd:canonical` role=`negative_control` windows=`1` false_proxy=`95.2%`
- `old_candidate_universe:pack:due_doubles` role=`negative_control` windows=`1` false_proxy=`95.1%`
- `old_candidate_universe:pack_method:due_doubles:canonical` role=`negative_control` windows=`1` false_proxy=`95.1%`
- `old_candidate_universe:pack:mirror_pair_closure` role=`negative_control` windows=`1` false_proxy=`94.8%`
- `old_candidate_universe:pack_method:mirror_pair_closure:canonical` role=`negative_control` windows=`1` false_proxy=`94.8%`
- `old_candidate_universe:pack_method:consensus_double_9:canonical` role=`negative_control` windows=`1` false_proxy=`94.8%`
- `old_play_card:strategy:v0_2_default:B36:combos` role=`negative_control` windows=`1` false_proxy=`94.7%`
- `old_candidate_universe:candidate_universe_union_combo` role=`negative_control` windows=`1` false_proxy=`94.6%`
- `old_play_card:strategy_card:analysis_prefix:B36` role=`negative_control` windows=`1` false_proxy=`94.5%`
- `old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` role=`negative_control` windows=`1` false_proxy=`94.4%`

## Evidence Families To Watch

- `arena` role=`translator_teaching_surface` used=`97` underused=`23` wrong_lane=`66`
- `translation_sandbox` role=`translator_teaching_surface` used=`97` underused=`23` wrong_lane=`66`
- `brain1` role=`translator_teaching_surface` used=`95` underused=`23` wrong_lane=`66`
- `frontier` role=`hypothesis_probe_surface` used=`97` underused=`23` wrong_lane=`66`
- `tracker` role=`hypothesis_probe_surface` used=`97` underused=`23` wrong_lane=`66`
- `board_scoreboard` role=`hypothesis_probe_surface` used=`82` underused=`21` wrong_lane=`50`
- `old_candidate_universe` role=`diagnostic_surface` used=`97` underused=`20` wrong_lane=`55`
- `shadow_policy` role=`diagnostic_surface` used=`47` underused=`19` wrong_lane=`31`
- `old_play_card` role=`diagnostic_surface` used=`75` underused=`13` wrong_lane=`11`
- `survivor` role=`diagnostic_surface` used=`28` underused=`12` wrong_lane=`15`
- `profit_alerts` role=`diagnostic_surface` used=`15` underused=`10` wrong_lane=`21`
- `positional` role=`diagnostic_surface` used=`39` underused=`9` wrong_lane=`8`

## Decay Guardrail

- `arena_box_total` lane=`boxed` horizon=`60.5%` incremental=`44.3%` role=`boxed_carryforward_teacher`
- `sandbox_box_seed` lane=`boxed` horizon=`53.3%` incremental=`40.5%` role=`boxed_carryforward_teacher`
- `brain1_box_core` lane=`boxed` horizon=`46.7%` incremental=`33.3%` role=`boxed_carryforward_teacher`
- `board_top_box_core` lane=`boxed` horizon=`11.0%` incremental=`6.7%` role=`boxed_carryforward_teacher`
- `board_top_vt_core` lane=`vtrac` horizon=`79.5%` incremental=`55.2%` role=`territory_decay_watch`
- `brain1_vt_core` lane=`vtrac` horizon=`97.6%` incremental=`48.6%` role=`territory_decay_watch`
- `arena_vt_total` lane=`vtrac` horizon=`100.0%` incremental=`33.8%` role=`territory_decay_watch`
- `sandbox_vt_seed` lane=`vtrac` horizon=`100.0%` incremental=`33.8%` role=`territory_decay_watch`
- `sandbox_exact_seed` lane=`straight` horizon=`14.3%` incremental=`10.0%` role=`straight_precision_probe`
- `preserved_not_budgeted` lane=`context` horizon=`4.5%` incremental=`3.9%` role=`carryforward_context`

## Files

- Decision workbench: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_DECISION_WORKBENCH.md`
- Promotion registry: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_PROMOTION_REGISTRY.csv`
- Replay queue: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_REPLAY_QUEUE.csv`
- Negative-control map: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_NEGATIVE_CONTROL_MAP.csv`
- Evidence-utilization matrix: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_EVIDENCE_UTILIZATION_MATRIX.csv`
- Decay stratification: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_DECAY_STRATIFICATION.csv`
