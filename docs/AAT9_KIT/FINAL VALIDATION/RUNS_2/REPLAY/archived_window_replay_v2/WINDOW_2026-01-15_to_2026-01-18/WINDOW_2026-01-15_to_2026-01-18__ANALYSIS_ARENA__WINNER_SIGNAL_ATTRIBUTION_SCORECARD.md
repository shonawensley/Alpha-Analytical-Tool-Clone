# Winner Signal Attribution Scorecard

Purpose: show which indicators fired toward winners, by exact/box/VTRAC modes, and whether they are sharp enough for future Brain scoring work.

## 1. Totals

- Winner events: `109`
- Winner-aligned attribution rows: `3433`
- Source keys with emitted-value denominators: `50`

## 2. Boolean Alignment Signals

| Signal | Tier | Present | Converted | Gap | VT-only | Read |
|---|---:|---:|---:|---:|---:|---|
| `play_card_any_box` | `A` | `11` (10.1%) | `11` (100.0%) | `0` (0.0%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `sandbox_exact_seed` | `A` | `3` (2.8%) | `3` (100.0%) | `0` (0.0%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `arena_exact_signal` | `A` | `3` (2.8%) | `3` (100.0%) | `0` (0.0%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `play_card_any_exact` | `A` | `16` (14.7%) | `15` (93.8%) | `1` (6.2%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `sandbox_box_seed` | `A` | `10` (9.2%) | `8` (80.0%) | `2` (20.0%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `arena_box_signal` | `A` | `12` (11.0%) | `8` (66.7%) | `4` (33.3%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `arena_primary_box` | `A` | `9` (8.3%) | `5` (55.6%) | `4` (44.4%) | `0` (0.0%) | High-priority translator-learning signal; often saw value that old final layer missed. |
| `cu_exact` | `B` | `26` (23.9%) | `23` (88.5%) | `3` (11.5%) | `0` (0.0%) | Strong territory signal; promote to conversion only when paired with sharper exact/box evidence. |
| `cu_box` | `B` | `33` (30.3%) | `25` (75.8%) | `3` (9.1%) | `5` (15.2%) | Strong territory signal; promote to conversion only when paired with sharper exact/box evidence. |
| `arena_primary_vt` | `B` | `33` (30.3%) | `18` (54.5%) | `3` (9.1%) | `12` (36.4%) | Strong territory signal; promote to conversion only when paired with sharper exact/box evidence. |
| `sandbox_vt_seed` | `B` | `46` (42.2%) | `20` (43.5%) | `3` (6.5%) | `18` (39.1%) | Strong territory signal; promote to conversion only when paired with sharper exact/box evidence. |

## 3. Matched Emitted Source Values

| Source | Pre-draw aligned rows | Exact | Box | VTRAC | Values examined | Alignment rate |
|---|---:|---:|---:|---:|---:|---:|
| `old_candidate_universe:pack:stable_top` | `91` | `0` | `13` | `91` | `2616` | 3.48% |
| `translation_sandbox:diagnostic_straight_seed` | `56` | `6` | `15` | `53` | `1744` | 3.04% |
| `old_play_card:budgeted_canonicals_top` | `52` | `0` | `11` | `52` | `1920` | 2.71% |
| `translation_sandbox:diagnostic_boxed_seed` | `61` | `0` | `20` | `51` | `1744` | 2.92% |
| `brain1:dominant_canonicals` | `51` | `0` | `9` | `51` | `1304` | 3.91% |
| `translation_sandbox:diagnostic_vt_box_seed` | `46` | `0` | `0` | `46` | `1308` | 3.52% |
| `brain1:secondary_canonicals` | `43` | `0` | `8` | `43` | `1308` | 3.29% |
| `positional:positional_canonical` | `39` | `0` | `5` | `39` | `872` | 4.47% |
| `positional:positional_combo` | `39` | `0` | `5` | `39` | `872` | 4.47% |
| `old_play_card:ranked_candidate_canonical` | `36` | `0` | `17` | `36` | `1635` | 2.20% |
| `old_play_card:ranked_candidate_combo` | `36` | `3` | `17` | `36` | `1635` | 2.20% |
| `blackapple:recommended_canonicals` | `35` | `0` | `5` | `35` | `872` | 4.01% |
| `old_candidate_universe:top_canonicals` | `33` | `0` | `5` | `33` | `1308` | 2.52% |
| `brain1:dominant_vtrac_indices` | `33` | `0` | `0` | `33` | `942` | 3.50% |
| `old_candidate_universe:pack:due_doubles` | `31` | `0` | `0` | `31` | `1164` | 2.66% |
| `old_candidate_universe:pack:aux_vtrac_index_overdue` | `30` | `0` | `5` | `30` | `640` | 4.69% |
| `brain1:context_reinforced_canonicals` | `24` | `0` | `3` | `24` | `629` | 3.82% |
| `old_play_card:strategy_card:convergence_box_first:B36` | `23` | `0` | `9` | `23` | `872` | 2.64% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` | `23` | `0` | `9` | `23` | `872` | 2.64% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` | `23` | `0` | `9` | `23` | `872` | 2.64% |
| `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` | `23` | `0` | `9` | `23` | `872` | 2.64% |
| `shadow_policy:primary_cluster_canonicals` | `23` | `0` | `5` | `23` | `654` | 3.52% |
| `brain1:watchlist_indices` | `23` | `0` | `0` | `23` | `654` | 3.52% |
| `old_candidate_universe:pack:R-perm-4` | `22` | `0` | `6` | `22` | `436` | 5.05% |
| `old_candidate_universe:pack:mirror_pair_closure` | `21` | `0` | `10` | `21` | `654` | 3.21% |
| `survivor:survivor_frontier_canonicals` | `19` | `0` | `3` | `19` | `872` | 2.18% |
| `due_doubles:example_canonicals` | `19` | `0` | `1` | `19` | `872` | 2.18% |
| `board_scoreboard:top_vtrac_indices` | `18` | `0` | `0` | `18` | `436` | 4.13% |
| `old_play_card:strategy_card:conversion_box_first:B36` | `17` | `0` | `7` | `17` | `826` | 2.06% |
| `shadow_policy:primary_cluster_context` | `17` | `0` | `3` | `17` | `422` | 4.03% |
| `old_play_card:strategy_card:analysis_prefix:B36` | `17` | `0` | `2` | `17` | `736` | 2.31% |
| `board_scoreboard:top_canonicals` | `15` | `0` | `3` | `15` | `436` | 3.44% |
| `old_play_card:strategy_card:convergence_box_first:B24` | `13` | `0` | `4` | `13` | `703` | 1.85% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` | `13` | `0` | `4` | `13` | `703` | 1.85% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` | `13` | `0` | `4` | `13` | `703` | 1.85% |
| `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` | `13` | `0` | `4` | `13` | `703` | 1.85% |
| `profit_alerts:implied_canonicals` | `13` | `0` | `3` | `13` | `486` | 2.67% |
| `profit_alerts:top_profit_alerts` | `13` | `0` | `2` | `13` | `338` | 3.85% |
| `old_play_card:strategy_card:conversion_box_first:B24` | `12` | `0` | `3` | `12` | `562` | 2.14% |
| `shadow_policy:primary_cluster_survivor_frontier` | `10` | `0` | `2` | `10` | `436` | 2.29% |

## 4. Boolean / Derived Attribution Rows

| Source | Pre-draw aligned rows | Exact | Box | VTRAC | Notes |
|---|---:|---:|---:|---:|---|
| `tracker:blackapple_support` | `109` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:due_double_support` | `109` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:positional_support` | `109` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:profit_alert_support` | `109` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:survivor_support` | `109` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:vtrac_total_decay_resolution` | `107` | `0` | `0` | `107` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:vt_seed_decay_resolution` | `107` | `0` | `0` | `107` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `brain1:vtrac_core_decay_resolution` | `97` | `0` | `0` | `97` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:r_consensus_support` | `78` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:compound_event_support` | `70` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `board_scoreboard:top_vtrac_indices_decay_resolution` | `67` | `0` | `0` | `67` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:box_total_decay_resolution` | `56` | `0` | `56` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `brain1:box_core_decay_resolution` | `50` | `0` | `50` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:diagnostic_vt_seed` | `46` | `0` | `0` | `46` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:boxed_seed_decay_resolution` | `44` | `0` | `44` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:compound_event_present` | `40` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_candidate_universe:candidate_universe_box` | `33` | `0` | `33` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:brain1_dominant_vtrac` | `33` | `0` | `0` | `33` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_candidate_universe:candidate_universe_exact` | `26` | `26` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `board_scoreboard:top_canonicals_decay_resolution` | `18` | `0` | `18` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_exact_any` | `16` | `16` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:straight_seed_decay_resolution` | `16` | `16` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b36_exact` | `15` | `15` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:arena_box_rollup` | `12` | `0` | `12` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_box_any` | `11` | `0` | `11` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b24_exact` | `11` | `11` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b36_box` | `10` | `0` | `10` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:brain1_dominant_canonicals` | `9` | `0` | `9` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b24_box` | `8` | `0` | `8` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `control_arm:preserved_decay_resolution` | `6` | `0` | `6` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |

## 5. Practical Read

- Treat this as winner-alignment attribution, not final predictive lift by itself.
- Stage 2 should add a full false-positive/exposure denominator for the same source keys across non-winning emitted values.
- Exact and box rows are most relevant to future straight/boxed lanes; VTRAC rows are territory and decay-lane evidence unless paired with sharper evidence.
