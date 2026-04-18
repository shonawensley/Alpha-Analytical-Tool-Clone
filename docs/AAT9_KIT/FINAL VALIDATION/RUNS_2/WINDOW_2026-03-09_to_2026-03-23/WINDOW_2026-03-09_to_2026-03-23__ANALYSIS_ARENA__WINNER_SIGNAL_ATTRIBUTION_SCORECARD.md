# Winner Signal Attribution Scorecard

Purpose: show which indicators fired toward winners, by exact/box/VTRAC modes, and whether they are sharp enough for future Brain scoring work.

## 1. Totals

- Winner events: `414`
- Winner-aligned attribution rows: `13559`
- Source keys with emitted-value denominators: `50`

## 2. Boolean Alignment Signals

| Signal | Tier | Present | Converted | Gap | VT-only | Read |
|---|---:|---:|---:|---:|---:|---|
| `play_card_any_box` | `A` | `29` (7.0%) | `29` (100.0%) | `0` (0.0%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `play_card_any_exact` | `A` | `54` (13.0%) | `51` (94.4%) | `3` (5.6%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `sandbox_exact_seed` | `A` | `9` (2.2%) | `7` (77.8%) | `2` (22.2%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `arena_exact_signal` | `A` | `9` (2.2%) | `7` (77.8%) | `2` (22.2%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `sandbox_box_seed` | `A` | `27` (6.5%) | `12` (44.4%) | `15` (55.6%) | `0` (0.0%) | High-priority translator-learning signal; often saw value that old final layer missed. |
| `arena_box_signal` | `A` | `35` (8.5%) | `14` (40.0%) | `21` (60.0%) | `0` (0.0%) | High-priority translator-learning signal; often saw value that old final layer missed. |
| `arena_primary_box` | `A` | `25` (6.0%) | `9` (36.0%) | `16` (64.0%) | `0` (0.0%) | High-priority translator-learning signal; often saw value that old final layer missed. |
| `cu_exact` | `B` | `80` (19.3%) | `62` (77.5%) | `12` (15.0%) | `5` (6.2%) | Strong territory signal; promote to conversion only when paired with sharper exact/box evidence. |
| `cu_box` | `B` | `97` (23.4%) | `74` (76.3%) | `14` (14.4%) | `8` (8.2%) | Strong territory signal; promote to conversion only when paired with sharper exact/box evidence. |
| `arena_primary_vt` | `B` | `116` (28.0%) | `49` (42.2%) | `16` (13.8%) | `43` (37.1%) | Strong territory signal; promote to conversion only when paired with sharper exact/box evidence. |
| `sandbox_vt_seed` | `B` | `162` (39.1%) | `59` (36.4%) | `19` (11.7%) | `64` (39.5%) | Track as supporting evidence; confirm stability in next window. |

## 3. Matched Emitted Source Values

| Source | Pre-draw aligned rows | Exact | Box | VTRAC | Values examined | Alignment rate |
|---|---:|---:|---:|---:|---:|---:|
| `old_candidate_universe:pack:stable_top` | `285` | `0` | `38` | `285` | `9936` | 2.87% |
| `translation_sandbox:diagnostic_straight_seed` | `255` | `18` | `30` | `246` | `6624` | 3.71% |
| `translation_sandbox:diagnostic_boxed_seed` | `243` | `0` | `54` | `216` | `6624` | 3.26% |
| `old_play_card:ranked_candidate_canonical` | `209` | `0` | `23` | `209` | `6210` | 3.37% |
| `old_play_card:ranked_candidate_combo` | `209` | `7` | `23` | `209` | `6210` | 3.37% |
| `old_play_card:budgeted_canonicals_top` | `208` | `0` | `29` | `208` | `7329` | 2.84% |
| `brain1:secondary_canonicals` | `191` | `0` | `22` | `191` | `4968` | 3.84% |
| `brain1:dominant_canonicals` | `172` | `0` | `25` | `172` | `4958` | 3.47% |
| `translation_sandbox:diagnostic_vt_box_seed` | `162` | `0` | `0` | `162` | `4966` | 3.26% |
| `old_candidate_universe:top_canonicals` | `150` | `0` | `18` | `150` | `4968` | 3.02% |
| `blackapple:recommended_canonicals` | `133` | `0` | `17` | `133` | `3312` | 4.02% |
| `positional:positional_combo` | `116` | `6` | `18` | `116` | `3312` | 3.50% |
| `brain1:dominant_vtrac_indices` | `116` | `0` | `0` | `116` | `3473` | 3.34% |
| `positional:positional_canonical` | `114` | `0` | `18` | `114` | `3312` | 3.44% |
| `old_candidate_universe:pack:due_doubles` | `109` | `0` | `3` | `109` | `4592` | 2.37% |
| `old_play_card:strategy_card:convergence_box_first:B36` | `104` | `0` | `18` | `104` | `3306` | 3.15% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` | `104` | `0` | `18` | `104` | `3306` | 3.15% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` | `104` | `0` | `18` | `104` | `3306` | 3.15% |
| `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` | `104` | `0` | `18` | `104` | `3306` | 3.15% |
| `survivor:survivor_frontier_canonicals` | `104` | `0` | `17` | `104` | `3312` | 3.14% |
| `old_play_card:strategy_card:conversion_box_first:B36` | `100` | `0` | `15` | `100` | `3098` | 3.23% |
| `shadow_policy:primary_cluster_canonicals` | `92` | `0` | `13` | `92` | `2484` | 3.70% |
| `old_play_card:strategy_card:convergence_box_first:B24` | `87` | `0` | `15` | `87` | `2648` | 3.29% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` | `87` | `0` | `15` | `87` | `2648` | 3.29% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` | `87` | `0` | `15` | `87` | `2648` | 3.29% |
| `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` | `87` | `0` | `15` | `87` | `2648` | 3.29% |
| `profit_alerts:implied_canonicals` | `85` | `0` | `8` | `85` | `2127` | 4.00% |
| `brain1:context_reinforced_canonicals` | `83` | `0` | `11` | `83` | `2370` | 3.50% |
| `brain1:watchlist_indices` | `83` | `0` | `0` | `83` | `2482` | 3.34% |
| `old_play_card:strategy_card:analysis_prefix:B36` | `80` | `0` | `11` | `80` | `2875` | 2.78% |
| `due_doubles:example_canonicals` | `72` | `0` | `7` | `72` | `3312` | 2.17% |
| `old_play_card:strategy_card:conversion_box_first:B24` | `69` | `0` | `12` | `69` | `2066` | 3.34% |
| `old_candidate_universe:pack:mirror_pair_closure` | `65` | `0` | `16` | `65` | `2484` | 2.62% |
| `old_candidate_universe:pack:R-perm-4` | `63` | `0` | `11` | `63` | `1656` | 3.80% |
| `shadow_policy:primary_cluster_survivor_frontier` | `62` | `0` | `7` | `62` | `1656` | 3.74% |
| `old_play_card:strategy_card:analysis_prefix:B24` | `61` | `0` | `8` | `61` | `1828` | 3.34% |
| `shadow_policy:primary_cluster_context` | `60` | `0` | `9` | `60` | `1618` | 3.71% |
| `board_scoreboard:top_canonicals` | `57` | `0` | `9` | `57` | `1656` | 3.44% |
| `old_candidate_universe:pack:aux_vtrac_index_overdue` | `54` | `0` | `9` | `54` | `1704` | 3.17% |
| `board_scoreboard:top_vtrac_indices` | `54` | `0` | `0` | `54` | `1656` | 3.26% |

## 4. Boolean / Derived Attribution Rows

| Source | Pre-draw aligned rows | Exact | Box | VTRAC | Notes |
|---|---:|---:|---:|---:|---|
| `arena:vtrac_total_decay_resolution` | `414` | `0` | `0` | `414` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:blackapple_support` | `414` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:due_double_support` | `414` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:positional_support` | `414` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:profit_alert_support` | `414` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:survivor_support` | `414` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:vt_seed_decay_resolution` | `414` | `0` | `0` | `414` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `brain1:vtrac_core_decay_resolution` | `404` | `0` | `0` | `404` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:r_consensus_support` | `352` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `board_scoreboard:top_vtrac_indices_decay_resolution` | `328` | `0` | `0` | `328` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:compound_event_support` | `268` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:box_total_decay_resolution` | `248` | `0` | `248` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:boxed_seed_decay_resolution` | `218` | `0` | `218` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `brain1:box_core_decay_resolution` | `190` | `0` | `190` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:diagnostic_vt_seed` | `162` | `0` | `0` | `162` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:compound_event_present` | `148` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:brain1_dominant_vtrac` | `116` | `0` | `0` | `116` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_candidate_universe:candidate_universe_box` | `97` | `0` | `97` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_candidate_universe:candidate_universe_exact` | `80` | `80` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:straight_seed_decay_resolution` | `57` | `57` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b36_exact` | `54` | `54` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_exact_any` | `54` | `54` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `board_scoreboard:top_canonicals_decay_resolution` | `45` | `0` | `45` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:arena_box_rollup` | `35` | `0` | `35` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b24_exact` | `34` | `34` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b36_box` | `29` | `0` | `29` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_box_any` | `29` | `0` | `29` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:brain1_dominant_canonicals` | `25` | `0` | `25` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b24_box` | `21` | `0` | `21` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b12_exact` | `16` | `16` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |

## 5. Practical Read

- Treat this as winner-alignment attribution, not final predictive lift by itself.
- Stage 2 should add a full false-positive/exposure denominator for the same source keys across non-winning emitted values.
- Exact and box rows are most relevant to future straight/boxed lanes; VTRAC rows are territory and decay-lane evidence unless paired with sharper evidence.
