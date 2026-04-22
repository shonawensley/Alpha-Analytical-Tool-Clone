# Winner Signal Attribution Scorecard

Purpose: show which indicators fired toward winners, by exact/box/VTRAC modes, and whether they are sharp enough for future Brain scoring work.

## 1. Totals

- Winner events: `301`
- Winner-aligned attribution rows: `9256`
- Source keys with emitted-value denominators: `50`

## 2. Boolean Alignment Signals

| Signal | Tier | Present | Converted | Gap | VT-only | Read |
|---|---:|---:|---:|---:|---:|---|
| `play_card_any_box` | `A` | `21` (7.0%) | `21` (100.0%) | `0` (0.0%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `sandbox_exact_seed` | `A` | `4` (1.3%) | `4` (100.0%) | `0` (0.0%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `arena_exact_signal` | `A` | `4` (1.3%) | `4` (100.0%) | `0` (0.0%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `play_card_any_exact` | `A` | `39` (13.0%) | `34` (87.2%) | `5` (12.8%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `sandbox_box_seed` | `A` | `19` (6.3%) | `10` (52.6%) | `9` (47.4%) | `0` (0.0%) | High-priority translator-learning signal; often saw value that old final layer missed. |
| `arena_primary_box` | `A` | `15` (5.0%) | `7` (46.7%) | `8` (53.3%) | `0` (0.0%) | High-priority translator-learning signal; often saw value that old final layer missed. |
| `arena_box_signal` | `A` | `22` (7.3%) | `10` (45.5%) | `12` (54.5%) | `0` (0.0%) | High-priority translator-learning signal; often saw value that old final layer missed. |
| `cu_exact` | `B` | `57` (18.9%) | `43` (75.4%) | `8` (14.0%) | `6` (10.5%) | Strong territory signal; promote to conversion only when paired with sharper exact/box evidence. |
| `cu_box` | `B` | `73` (24.3%) | `51` (69.9%) | `10` (13.7%) | `9` (12.3%) | Strong territory signal; promote to conversion only when paired with sharper exact/box evidence. |
| `arena_primary_vt` | `B` | `68` (22.6%) | `29` (42.6%) | `9` (13.2%) | `27` (39.7%) | Strong territory signal; promote to conversion only when paired with sharper exact/box evidence. |
| `sandbox_vt_seed` | `B` | `109` (36.2%) | `39` (35.8%) | `9` (8.3%) | `45` (41.3%) | Track as supporting evidence; confirm stability in next window. |

## 3. Matched Emitted Source Values

| Source | Pre-draw aligned rows | Exact | Box | VTRAC | Values examined | Alignment rate |
|---|---:|---:|---:|---:|---:|---:|
| `old_candidate_universe:pack:stable_top` | `182` | `0` | `24` | `182` | `7224` | 2.52% |
| `translation_sandbox:diagnostic_straight_seed` | `155` | `8` | `19` | `151` | `4816` | 3.14% |
| `old_play_card:budgeted_canonicals_top` | `139` | `0` | `21` | `139` | `5317` | 2.61% |
| `old_play_card:ranked_candidate_canonical` | `135` | `0` | `27` | `135` | `4515` | 2.99% |
| `old_play_card:ranked_candidate_combo` | `135` | `7` | `27` | `135` | `4515` | 2.99% |
| `translation_sandbox:diagnostic_boxed_seed` | `147` | `0` | `38` | `128` | `4816` | 2.66% |
| `translation_sandbox:diagnostic_vt_box_seed` | `109` | `0` | `0` | `109` | `3608` | 3.02% |
| `brain1:secondary_canonicals` | `106` | `0` | `15` | `106` | `3612` | 2.93% |
| `old_candidate_universe:top_canonicals` | `101` | `0` | `17` | `101` | `3612` | 2.80% |
| `brain1:dominant_canonicals` | `93` | `0` | `15` | `93` | `3588` | 2.59% |
| `blackapple:recommended_canonicals` | `88` | `0` | `15` | `88` | `2408` | 3.65% |
| `positional:positional_combo` | `82` | `1` | `7` | `82` | `2408` | 3.41% |
| `positional:positional_canonical` | `81` | `0` | `7` | `81` | `2408` | 3.36% |
| `old_play_card:strategy_card:conversion_box_first:B36` | `73` | `0` | `12` | `73` | `2305` | 3.17% |
| `old_candidate_universe:pack:due_doubles` | `73` | `0` | `10` | `73` | `2956` | 2.47% |
| `old_candidate_universe:pack:aux_vtrac_index_overdue` | `72` | `0` | `12` | `72` | `2272` | 3.17% |
| `old_play_card:strategy_card:convergence_box_first:B36` | `72` | `0` | `12` | `72` | `2402` | 3.00% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` | `72` | `0` | `12` | `72` | `2402` | 3.00% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` | `72` | `0` | `12` | `72` | `2402` | 3.00% |
| `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` | `72` | `0` | `12` | `72` | `2402` | 3.00% |
| `brain1:dominant_vtrac_indices` | `68` | `0` | `0` | `68` | `2537` | 2.68% |
| `survivor:survivor_frontier_canonicals` | `66` | `0` | `6` | `66` | `2408` | 2.74% |
| `old_play_card:strategy_card:convergence_box_first:B24` | `59` | `0` | `12` | `59` | `1943` | 3.04% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` | `59` | `0` | `12` | `59` | `1943` | 3.04% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` | `59` | `0` | `12` | `59` | `1943` | 3.04% |
| `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` | `59` | `0` | `12` | `59` | `1943` | 3.04% |
| `old_play_card:strategy_card:analysis_prefix:B36` | `56` | `0` | `9` | `56` | `2081` | 2.69% |
| `brain1:context_reinforced_canonicals` | `54` | `0` | `7` | `54` | `1819` | 2.97% |
| `shadow_policy:primary_cluster_canonicals` | `52` | `0` | `7` | `52` | `1806` | 2.88% |
| `brain1:watchlist_indices` | `52` | `0` | `0` | `52` | `1804` | 2.88% |
| `old_candidate_universe:pack:mirror_pair_closure` | `47` | `0` | `11` | `47` | `1806` | 2.60% |
| `due_doubles:example_canonicals` | `44` | `0` | `5` | `44` | `2408` | 1.83% |
| `old_candidate_universe:pack:R-perm-4` | `43` | `0` | `7` | `43` | `1204` | 3.57% |
| `old_play_card:strategy_card:conversion_box_first:B24` | `43` | `0` | `6` | `43` | `1561` | 2.75% |
| `board_scoreboard:top_canonicals` | `41` | `0` | `4` | `41` | `1204` | 3.41% |
| `shadow_policy:primary_cluster_context` | `37` | `0` | `4` | `37` | `1192` | 3.10% |
| `board_scoreboard:top_vtrac_indices` | `36` | `0` | `0` | `36` | `1204` | 2.99% |
| `profit_alerts:implied_canonicals` | `35` | `0` | `5` | `35` | `1364` | 2.57% |
| `old_play_card:strategy_card:convergence_box_first:B12` | `31` | `0` | `7` | `31` | `1005` | 3.08% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12` | `31` | `0` | `7` | `31` | `979` | 3.17% |

## 4. Boolean / Derived Attribution Rows

| Source | Pre-draw aligned rows | Exact | Box | VTRAC | Notes |
|---|---:|---:|---:|---:|---|
| `tracker:blackapple_support` | `301` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:due_double_support` | `301` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:positional_support` | `301` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:profit_alert_support` | `301` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:survivor_support` | `301` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:vtrac_total_decay_resolution` | `295` | `0` | `0` | `295` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:vt_seed_decay_resolution` | `295` | `0` | `0` | `295` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `brain1:vtrac_core_decay_resolution` | `271` | `0` | `0` | `271` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:r_consensus_support` | `227` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `board_scoreboard:top_vtrac_indices_decay_resolution` | `204` | `0` | `0` | `204` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:compound_event_support` | `185` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:box_total_decay_resolution` | `164` | `0` | `164` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:boxed_seed_decay_resolution` | `138` | `0` | `138` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `brain1:box_core_decay_resolution` | `126` | `0` | `126` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:diagnostic_vt_seed` | `109` | `0` | `0` | `109` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:compound_event_present` | `98` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_candidate_universe:candidate_universe_box` | `73` | `0` | `73` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:brain1_dominant_vtrac` | `68` | `0` | `0` | `68` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_candidate_universe:candidate_universe_exact` | `57` | `57` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:straight_seed_decay_resolution` | `54` | `54` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `board_scoreboard:top_canonicals_decay_resolution` | `50` | `0` | `50` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b36_exact` | `39` | `39` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_exact_any` | `39` | `39` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b24_exact` | `23` | `23` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:arena_box_rollup` | `22` | `0` | `22` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_box_any` | `21` | `0` | `21` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b36_box` | `20` | `0` | `20` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:brain1_dominant_canonicals` | `15` | `0` | `15` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b24_box` | `15` | `0` | `15` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b12_exact` | `15` | `15` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |

## 5. Practical Read

- Treat this as winner-alignment attribution, not final predictive lift by itself.
- Stage 2 should add a full false-positive/exposure denominator for the same source keys across non-winning emitted values.
- Exact and box rows are most relevant to future straight/boxed lanes; VTRAC rows are territory and decay-lane evidence unless paired with sharper evidence.
