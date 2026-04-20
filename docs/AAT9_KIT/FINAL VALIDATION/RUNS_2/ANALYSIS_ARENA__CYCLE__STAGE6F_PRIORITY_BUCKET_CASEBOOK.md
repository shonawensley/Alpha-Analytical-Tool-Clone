# Analysis Arena Stage 6F Priority Bucket Casebook

## Guardrail

This casebook is evidence review only. It does not create live scoring, candidate-generation, translator, hard-veto, support-promotion, or budget permission.

## Target Summary

| target_id | source_stage | candidate | rows | positive | fp | yield | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S6F-TARGET-001 | Stage6D | S6D-RESCUE-012 | 142 | 50 | 47.8% | 18.382 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-002 | Stage6D | S6D-RESCUE-015 | 110 | 39 | 47.6% | 18.571 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-003 | Stage6D | S6D-RESCUE-016 | 110 | 39 | 47.6% | 18.571 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-004 | Stage6D | S6D-RESCUE-001 | 1488 | 502 | 62.8% | 12.550 | research_casebook_review_only |
| S6F-TARGET-005 | Stage6D | S6D-RESCUE-002 | 1488 | 502 | 62.8% | 12.550 | research_casebook_review_only |
| S6F-TARGET-006 | Stage6D | S6D-RESCUE-003 | 1464 | 494 | 63.1% | 12.456 | research_casebook_review_only |
| S6F-TARGET-007 | Stage6D | S6D-RESCUE-004 | 902 | 294 | 62.2% | 12.312 | research_casebook_review_only |
| S6F-TARGET-008 | Stage6D | S6D-RESCUE-005 | 878 | 286 | 62.7% | 12.150 | research_casebook_review_only |
| S6F-TARGET-009 | Stage6D | S6D-RESCUE-006 | 586 | 208 | 63.6% | 12.903 | research_casebook_review_only |
| S6F-TARGET-010 | Stage6D | S6D-RESCUE-007 | 586 | 208 | 63.6% | 12.903 | research_casebook_review_only |
| S6F-TARGET-011 | Stage6D | S6D-RESCUE-008 | 217 | 79 | 64.2% | 13.036 | research_casebook_review_only |
| S6F-TARGET-012 | Stage6D | S6D-RESCUE-009 | 216 | 76 | 69.7% | 10.674 | research_casebook_review_only |
| S6F-TARGET-013 | Stage6E | S6E-SUPPORT-001 | 408 | 98 | 35.8% | 15.409 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-014 | Stage6E | S6E-SUPPORT-002 | 342 | 81 | 34.7% | 15.458 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-015 | Stage6E | S6E-SUPPORT-003 | 131 | 29 | 39.4% | 13.426 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-016 | Stage6E | S6E-SUPPORT-004 | 1740 | 434 | 46.3% | 13.395 | research_casebook_review_only |
| S6F-TARGET-017 | Stage6E | S6E-SUPPORT-005 | 128 | 20 | 36.6% | 9.901 | research_casebook_review_only |

## Example Rows

| target_id | rank | window | date | state | positive | matched_values | sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S6F-TARGET-001 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:conversion_box_first:B12:boxed_canonicals |
| S6F-TARGET-001 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:play_box_first:B12:boxed_canonicals |
| S6F-TARGET-001 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:play_box_first:B12:combos |
| S6F-TARGET-001 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:convergence_box_first:B12 |
| S6F-TARGET-001 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first:B12 |
| S6F-TARGET-001 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12 |
| S6F-TARGET-001 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12 |
| S6F-TARGET-001 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12 |
| S6F-TARGET-002 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-002 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-002 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:combos + positional:positional_canonical |
| S6F-TARGET-002 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:convergence_box_first:B12 + positional:positional_canonical |
| S6F-TARGET-002 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first:B12 + positional:positional_canonical |
| S6F-TARGET-002 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12 + positional:positional_canonical |
| S6F-TARGET-002 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12 + positional:positional_canonical |
| S6F-TARGET-002 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12 + positional:positional_canonical |
| S6F-TARGET-003 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-003 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-003 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:combos + positional:positional_combo |
| S6F-TARGET-003 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:convergence_box_first:B12 + positional:positional_combo |
| S6F-TARGET-003 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first:B12 + positional:positional_combo |
| S6F-TARGET-003 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12 + positional:positional_combo |
| S6F-TARGET-003 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12 + positional:positional_combo |
| S6F-TARGET-003 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12 + positional:positional_combo |
| S6F-TARGET-004 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-14 | Florida4 | 1 | 027 | blackapple:recommended_canonicals + old_candidate_universe:pack:mirror_pair_closure |
| S6F-TARGET-004 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-14 | Florida4 | 1 | 027 | blackapple:recommended_canonicals + old_candidate_universe:pack_method:mirror_pair_closure:canonical |
| S6F-TARGET-004 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:conversion_box_first:B12:boxed_canonicals |
| S6F-TARGET-004 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-004 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:play_box_first:B12:boxed_canonicals |
| S6F-TARGET-004 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:play_box_first:B12:combos |
| S6F-TARGET-004 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:convergence_box_first:B12 |
| S6F-TARGET-004 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first:B12 |
| S6F-TARGET-005 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-14 | Florida4 | 1 | 027 | blackapple:recommended_canonicals + old_candidate_universe:pack:mirror_pair_closure |
| S6F-TARGET-005 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-14 | Florida4 | 1 | 027 | blackapple:recommended_canonicals + old_candidate_universe:pack_method:mirror_pair_closure:canonical |
| S6F-TARGET-005 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:conversion_box_first:B12:boxed_canonicals |
| S6F-TARGET-005 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-005 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:play_box_first:B12:boxed_canonicals |
| S6F-TARGET-005 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:play_box_first:B12:combos |
| S6F-TARGET-005 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:convergence_box_first:B12 |
| S6F-TARGET-005 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first:B12 |
| S6F-TARGET-006 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:conversion_box_first:B12:boxed_canonicals |
| S6F-TARGET-006 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-006 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:play_box_first:B12:boxed_canonicals |
| S6F-TARGET-006 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:play_box_first:B12:combos |
| S6F-TARGET-006 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:convergence_box_first:B12 |
| S6F-TARGET-006 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first:B12 |
| S6F-TARGET-006 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first:B24 |
| S6F-TARGET-006 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12 |
| S6F-TARGET-007 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-14 | Florida4 | 1 | 027 | blackapple:recommended_canonicals + old_candidate_universe:pack:mirror_pair_closure |
| S6F-TARGET-007 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-14 | Florida4 | 1 | 027 | blackapple:recommended_canonicals + old_candidate_universe:pack_method:mirror_pair_closure:canonical |
| S6F-TARGET-007 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-007 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-007 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B24:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-007 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B24:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-007 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-007 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-008 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-008 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-008 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B24:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-008 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B24:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-008 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-008 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-008 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:combos + positional:positional_canonical |
| S6F-TARGET-008 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:combos + positional:positional_combo |
| S6F-TARGET-009 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:conversion_box_first:B12:boxed_canonicals |
| S6F-TARGET-009 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-009 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:play_box_first:B12:boxed_canonicals |
| S6F-TARGET-009 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:play_box_first:B12:combos |
| S6F-TARGET-009 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:convergence_box_first:B12 |
| S6F-TARGET-009 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first:B12 |
| S6F-TARGET-009 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first:B24 |
| S6F-TARGET-009 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12 |
| S6F-TARGET-010 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:conversion_box_first:B12:boxed_canonicals |
| S6F-TARGET-010 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-010 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:play_box_first:B12:boxed_canonicals |
| S6F-TARGET-010 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy:play_box_first:B12:combos |
| S6F-TARGET-010 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:convergence_box_first:B12 |
| S6F-TARGET-010 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first:B12 |
| S6F-TARGET-010 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first:B24 |
| S6F-TARGET-010 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_candidate_universe:pack_method:aux_positional:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12 |

## Files

- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_PRIORITY_BUCKET_CASEBOOK.csv`
- example_ledger_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_BUCKET_EXAMPLE_LEDGER.csv`
