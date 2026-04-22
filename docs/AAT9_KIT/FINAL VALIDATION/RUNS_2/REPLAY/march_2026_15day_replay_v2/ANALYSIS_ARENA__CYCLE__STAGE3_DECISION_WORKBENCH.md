# Analysis Arena Stage 3 Decision Workbench

Purpose: convert Stage-2/Stage-2B evidence into disciplined promotion, replay, restraint, and readiness decisions.

## Executive Read

- Stage 3 is a decision surface, not a live scoring surface.
- Cross-window repeatability is now the main filter separating replay candidates from one-window noise.
- VTRAC/territory strength remains valuable, but it is explicitly watch/decay unless paired with bounded boxed/exact proof.
- Negative controls are promoted as restraint assets so future ranking/budget work learns what not to spend on.

## Corpus

- Cross-window windows: `1`
- Focus casebook window: `WINDOW_2026-03-09_to_2026-03-23`
- Registry rows: `4113`
- Replay rows: `104`
- Negative-control rows: `3235`
- Evidence-family rows: `15`
- Decay rows: `10`
- Casebook rows: `67`

## Decision Role Mix

- `needs_more_windows`: `3451`
- `watch_decay_only`: `581`
- `needs_replay`: `64`
- `negative_control`: `17`

## Replay Queue Mix

- `P4_diagnostic_replay`: `64`
- `P3_vtrac_decay_watch_replay`: `40`

## Top Boxed Translator Candidates

- None.

## Top Support Gates

- None.

## Top Watch/Decay Surfaces

- `translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`1` support=`39.1%`
- `vtrac_box_confirmation::old_candidate_universe:candidate_universe_union_combo + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`1` support=`35.0%`
- `vtrac_box_confirmation::old_candidate_universe:pack_method:stable_top:canonical + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`1` support=`29.0%`
- `vtrac_overlap::brain1:dominant_vtrac_indices + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`1` support=`28.0%`
- `brain1:dominant_vtrac_indices` lane=`vtrac` windows=`1` support=`28.0%`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:candidate_universe_union_combo` lane=`vtrac` windows=`1` support=`26.8%`
- `vtrac_box_confirmation::old_candidate_universe:pack:stable_top + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`1` support=`26.6%`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack_method:stable_top:canonical` lane=`vtrac` windows=`1` support=`24.4%`
- `vtrac_box_confirmation::translation_sandbox:diagnostic_boxed_seed + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`1` support=`23.9%`
- `vtrac_box_confirmation::brain1:secondary_canonicals + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`1` support=`22.7%`
- `vtrac_box_confirmation::brain1:dominant_vtrac_indices + old_candidate_universe:pack:stable_top` lane=`vtrac` windows=`1` support=`22.7%`
- `vtrac_box_confirmation::old_play_card:strategy:v0_2_default:B36:combos + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`1` support=`21.5%`
- `vtrac_box_confirmation::brain1:watchlist_indices + old_candidate_universe:candidate_universe_union_combo` lane=`vtrac` windows=`1` support=`20.0%`
- `brain1:watchlist_indices` lane=`vtrac` windows=`1` support=`20.0%`
- `vtrac_box_confirmation::brain1:dominant_canonicals + translation_sandbox:diagnostic_vt_box_seed` lane=`vtrac` windows=`1` support=`19.8%`

## Top Negative Controls

- `old_candidate_universe:pack:PackB_mirror3rd` false_proxy=`95.9%` role=`negative_control`
- `old_play_card:strategy:v0_2_default:B24:boxed_canonicals` false_proxy=`95.8%` role=`negative_control`
- `due_doubles:example_canonicals` false_proxy=`95.7%` role=`negative_control`
- `old_play_card:strategy:v0_2_default:B36:boxed_canonicals` false_proxy=`95.5%` role=`negative_control`
- `old_candidate_universe:pack_method:PackA_vt8:canonical` false_proxy=`95.3%` role=`negative_control`
- `old_candidate_universe:pack_method:PackB_mirror3rd:canonical` false_proxy=`95.2%` role=`negative_control`
- `old_candidate_universe:pack:due_doubles` false_proxy=`95.1%` role=`negative_control`
- `old_candidate_universe:pack_method:due_doubles:canonical` false_proxy=`95.1%` role=`negative_control`
- `old_candidate_universe:pack:mirror_pair_closure` false_proxy=`94.8%` role=`negative_control`
- `old_candidate_universe:pack_method:mirror_pair_closure:canonical` false_proxy=`94.8%` role=`negative_control`
- `old_candidate_universe:pack_method:consensus_double_9:canonical` false_proxy=`94.8%` role=`negative_control`
- `old_play_card:strategy:v0_2_default:B36:combos` false_proxy=`94.7%` role=`negative_control`
- `old_candidate_universe:candidate_universe_union_combo` false_proxy=`94.6%` role=`negative_control`
- `old_play_card:strategy_card:analysis_prefix:B36` false_proxy=`94.5%` role=`negative_control`
- `old_play_card:strategy:analysis_prefix:B36:boxed_canonicals` false_proxy=`94.4%` role=`negative_control`

## Evidence Utilization Read

- `arena` -> `translator_teaching_surface`; used `97`, underused `23`, wrong-lane `66`, decay `103`.
- `translation_sandbox` -> `translator_teaching_surface`; used `97`, underused `23`, wrong-lane `66`, decay `103`.
- `brain1` -> `translator_teaching_surface`; used `95`, underused `23`, wrong-lane `66`, decay `101`.
- `frontier` -> `hypothesis_probe_surface`; used `97`, underused `23`, wrong-lane `66`, decay `103`.
- `tracker` -> `hypothesis_probe_surface`; used `97`, underused `23`, wrong-lane `66`, decay `103`.
- `board_scoreboard` -> `hypothesis_probe_surface`; used `82`, underused `21`, wrong-lane `50`, decay `78`.
- `old_candidate_universe` -> `diagnostic_surface`; used `97`, underused `20`, wrong-lane `55`, decay `38`.
- `shadow_policy` -> `diagnostic_surface`; used `47`, underused `19`, wrong-lane `31`, decay `5`.
- `old_play_card` -> `diagnostic_surface`; used `75`, underused `13`, wrong-lane `11`, decay `16`.
- `survivor` -> `diagnostic_surface`; used `28`, underused `12`, wrong-lane `15`, decay `13`.
- `profit_alerts` -> `diagnostic_surface`; used `15`, underused `10`, wrong-lane `21`, decay `0`.
- `positional` -> `diagnostic_surface`; used `39`, underused `9`, wrong-lane `8`, decay `20`.

## Generated Files

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_DECISION_WORKBENCH.json`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_PROMOTION_REGISTRY.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_REPLAY_QUEUE.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_NEGATIVE_CONTROL_MAP.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_EVIDENCE_UTILIZATION_MATRIX.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_DECAY_STRATIFICATION.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE3_FRESH_WINDOW_DECISION_READINESS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__STAGE3_CASEBOOK.md`

## Guardrail

- This workbench grants replay and interpretation permission only. It does not grant live scoring, candidate-formation, or budget permission.
