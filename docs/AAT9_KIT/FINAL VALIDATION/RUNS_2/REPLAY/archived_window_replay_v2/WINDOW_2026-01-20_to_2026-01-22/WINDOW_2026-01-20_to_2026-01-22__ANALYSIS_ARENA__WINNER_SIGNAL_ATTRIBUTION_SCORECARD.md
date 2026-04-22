# Winner Signal Attribution Scorecard

Purpose: show which indicators fired toward winners, by exact/box/VTRAC modes, and whether they are sharp enough for future Brain scoring work.

## 1. Totals

- Winner events: `84`
- Winner-aligned attribution rows: `2689`
- Source keys with emitted-value denominators: `50`

## 2. Boolean Alignment Signals

| Signal | Tier | Present | Converted | Gap | VT-only | Read |
|---|---:|---:|---:|---:|---:|---|
| `play_card_any_box` | `A` | `5` (6.0%) | `5` (100.0%) | `0` (0.0%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `sandbox_exact_seed` | `A` | `1` (1.2%) | `1` (100.0%) | `0` (0.0%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `arena_exact_signal` | `A` | `1` (1.2%) | `1` (100.0%) | `0` (0.0%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `play_card_any_exact` | `A` | `13` (15.5%) | `12` (92.3%) | `1` (7.7%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `sandbox_box_seed` | `A` | `3` (3.6%) | `2` (66.7%) | `1` (33.3%) | `0` (0.0%) | Conversion-grade candidate signal in this window. |
| `arena_box_signal` | `A` | `4` (4.8%) | `2` (50.0%) | `2` (50.0%) | `0` (0.0%) | High-priority translator-learning signal; often saw value that old final layer missed. |
| `arena_primary_box` | `A` | `3` (3.6%) | `1` (33.3%) | `2` (66.7%) | `0` (0.0%) | High-priority translator-learning signal; often saw value that old final layer missed. |
| `cu_exact` | `B` | `14` (16.7%) | `13` (92.9%) | `1` (7.1%) | `0` (0.0%) | Strong territory signal; promote to conversion only when paired with sharper exact/box evidence. |
| `cu_box` | `B` | `20` (23.8%) | `18` (90.0%) | `1` (5.0%) | `1` (5.0%) | Strong territory signal; promote to conversion only when paired with sharper exact/box evidence. |
| `arena_primary_vt` | `B` | `24` (28.6%) | `11` (45.8%) | `1` (4.2%) | `11` (45.8%) | Strong territory signal; promote to conversion only when paired with sharper exact/box evidence. |
| `sandbox_vt_seed` | `B` | `30` (35.7%) | `11` (36.7%) | `1` (3.3%) | `14` (46.7%) | Track as supporting evidence; confirm stability in next window. |

## 3. Matched Emitted Source Values

| Source | Pre-draw aligned rows | Exact | Box | VTRAC | Values examined | Alignment rate |
|---|---:|---:|---:|---:|---:|---:|
| `translation_sandbox:diagnostic_straight_seed` | `67` | `2` | `9` | `66` | `1344` | 4.91% |
| `old_candidate_universe:pack:stable_top` | `51` | `0` | `6` | `51` | `2016` | 2.53% |
| `old_play_card:ranked_candidate_canonical` | `51` | `0` | `6` | `51` | `1260` | 4.05% |
| `old_play_card:ranked_candidate_combo` | `51` | `1` | `6` | `51` | `1260` | 4.05% |
| `translation_sandbox:diagnostic_boxed_seed` | `45` | `0` | `6` | `42` | `1344` | 3.12% |
| `old_play_card:budgeted_canonicals_top` | `39` | `0` | `5` | `39` | `1478` | 2.64% |
| `positional:positional_canonical` | `33` | `0` | `4` | `33` | `672` | 4.91% |
| `positional:positional_combo` | `33` | `0` | `4` | `33` | `672` | 4.91% |
| `brain1:secondary_canonicals` | `33` | `0` | `1` | `33` | `1008` | 3.27% |
| `brain1:dominant_canonicals` | `30` | `0` | `3` | `30` | `1008` | 2.98% |
| `translation_sandbox:diagnostic_vt_box_seed` | `30` | `0` | `0` | `30` | `1008` | 2.98% |
| `old_candidate_universe:pack:due_doubles` | `27` | `0` | `0` | `27` | `896` | 3.01% |
| `blackapple:recommended_canonicals` | `25` | `0` | `1` | `25` | `672` | 3.72% |
| `brain1:dominant_vtrac_indices` | `24` | `0` | `0` | `24` | `732` | 3.28% |
| `old_play_card:strategy_card:convergence_box_first:B36` | `23` | `0` | `4` | `23` | `670` | 3.43% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B36` | `23` | `0` | `4` | `23` | `670` | 3.43% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B36` | `23` | `0` | `4` | `23` | `670` | 3.43% |
| `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B36` | `23` | `0` | `4` | `23` | `670` | 3.43% |
| `old_candidate_universe:top_canonicals` | `23` | `0` | `3` | `23` | `1008` | 2.28% |
| `due_doubles:example_canonicals` | `23` | `0` | `2` | `23` | `672` | 3.42% |
| `old_play_card:strategy_card:conversion_box_first:B36` | `22` | `0` | `3` | `22` | `628` | 3.50% |
| `old_candidate_universe:pack:mirror_pair_closure` | `19` | `0` | `3` | `19` | `504` | 3.77% |
| `brain1:context_reinforced_canonicals` | `19` | `0` | `1` | `19` | `408` | 4.66% |
| `old_play_card:strategy_card:analysis_prefix:B36` | `18` | `0` | `1` | `18` | `608` | 2.96% |
| `shadow_policy:primary_cluster_canonicals` | `17` | `0` | `1` | `17` | `504` | 3.37% |
| `survivor:survivor_frontier_canonicals` | `17` | `0` | `1` | `17` | `672` | 2.53% |
| `old_candidate_universe:pack:R-perm-4` | `16` | `0` | `3` | `16` | `336` | 4.76% |
| `old_play_card:strategy_card:convergence_box_first:B24` | `15` | `0` | `3` | `15` | `544` | 2.76% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24` | `15` | `0` | `3` | `15` | `544` | 2.76% |
| `old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B24` | `15` | `0` | `3` | `15` | `544` | 2.76% |
| `old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B24` | `15` | `0` | `3` | `15` | `544` | 2.76% |
| `old_play_card:strategy_card:conversion_box_first:B24` | `15` | `0` | `1` | `15` | `432` | 3.47% |
| `brain1:watchlist_indices` | `15` | `0` | `0` | `15` | `504` | 2.98% |
| `shadow_policy:primary_cluster_context` | `15` | `0` | `0` | `15` | `324` | 4.63% |
| `board_scoreboard:top_vtrac_indices` | `13` | `0` | `0` | `13` | `336` | 3.87% |
| `profit_alerts:top_profit_alerts` | `13` | `0` | `0` | `13` | `262` | 4.96% |
| `old_candidate_universe:pack:aux_vtrac_index_overdue` | `12` | `0` | `2` | `12` | `456` | 2.63% |
| `old_play_card:strategy_card:analysis_prefix:B24` | `12` | `0` | `1` | `12` | `382` | 3.14% |
| `shadow_policy:primary_cluster_survivor_frontier` | `12` | `0` | `1` | `12` | `336` | 3.57% |
| `board_scoreboard:top_canonicals` | `11` | `0` | `1` | `11` | `336` | 3.27% |

## 4. Boolean / Derived Attribution Rows

| Source | Pre-draw aligned rows | Exact | Box | VTRAC | Notes |
|---|---:|---:|---:|---:|---|
| `tracker:blackapple_support` | `84` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:due_double_support` | `84` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:positional_support` | `84` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:profit_alert_support` | `84` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:survivor_support` | `84` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:vtrac_total_decay_resolution` | `82` | `0` | `0` | `82` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:vt_seed_decay_resolution` | `82` | `0` | `0` | `82` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `brain1:vtrac_core_decay_resolution` | `72` | `0` | `0` | `72` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:r_consensus_support` | `68` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `board_scoreboard:top_vtrac_indices_decay_resolution` | `50` | `0` | `0` | `50` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:compound_event_support` | `44` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:box_total_decay_resolution` | `42` | `0` | `42` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `brain1:box_core_decay_resolution` | `36` | `0` | `36` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:boxed_seed_decay_resolution` | `32` | `0` | `32` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:diagnostic_vt_seed` | `30` | `0` | `0` | `30` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:brain1_dominant_vtrac` | `24` | `0` | `0` | `24` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `tracker:compound_event_present` | `22` | `0` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_candidate_universe:candidate_universe_box` | `20` | `0` | `20` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_candidate_universe:candidate_universe_exact` | `14` | `14` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b36_exact` | `13` | `13` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_exact_any` | `13` | `13` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `board_scoreboard:top_canonicals_decay_resolution` | `10` | `0` | `10` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b24_exact` | `8` | `8` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `translation_sandbox:straight_seed_decay_resolution` | `6` | `6` | `0` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b36_box` | `5` | `0` | `5` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_box_any` | `5` | `0` | `5` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:arena_box_rollup` | `4` | `0` | `4` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `control_arm:preserved_decay_resolution` | `4` | `0` | `4` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `old_play_card:play_card_b24_box` | `4` | `0` | `4` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |
| `arena:brain1_dominant_canonicals` | `3` | `0` | `3` | `0` | Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list. |

## 5. Practical Read

- Treat this as winner-alignment attribution, not final predictive lift by itself.
- Stage 2 should add a full false-positive/exposure denominator for the same source keys across non-winning emitted values.
- Exact and box rows are most relevant to future straight/boxed lanes; VTRAC rows are territory and decay-lane evidence unless paired with sharper evidence.
