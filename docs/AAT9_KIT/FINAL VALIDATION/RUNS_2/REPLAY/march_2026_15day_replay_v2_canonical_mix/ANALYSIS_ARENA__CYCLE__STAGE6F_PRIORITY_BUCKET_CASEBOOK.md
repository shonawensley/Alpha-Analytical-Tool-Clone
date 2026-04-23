# Analysis Arena Stage 6F Priority Bucket Casebook

## Guardrail

This casebook is evidence review only. It does not create live scoring, candidate-generation, translator, hard-veto, support-promotion, or budget permission.

## Target Summary

| target_id | source_stage | candidate | rows | positive | fp | yield | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S6F-TARGET-001 | Stage6D | S6D-RESCUE-002 | 1220 | 477 | 49.1% | 19.908 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-002 | Stage6D | S6D-RESCUE-008 | 272 | 91 | 38.5% | 20.588 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-003 | Stage6D | S6D-RESCUE-009 | 266 | 89 | 38.6% | 20.554 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-004 | Stage6D | S6D-RESCUE-010 | 196 | 88 | 46.6% | 23.978 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-005 | Stage6D | S6D-RESCUE-011 | 158 | 78 | 47.3% | 26.000 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-006 | Stage6D | S6D-RESCUE-012 | 158 | 78 | 47.3% | 26.000 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-007 | Stage6D | S6D-RESCUE-013 | 79 | 39 | 47.3% | 26.000 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-008 | Stage6D | S6D-RESCUE-014 | 79 | 39 | 47.3% | 26.000 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-009 | Stage6D | S6D-RESCUE-015 | 116 | 38 | 43.4% | 18.537 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-010 | Stage6D | S6D-RESCUE-016 | 106 | 38 | 44.2% | 20.000 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-011 | Stage6D | S6D-RESCUE-017 | 84 | 30 | 39.6% | 21.583 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-012 | Stage6D | S6D-RESCUE-018 | 38 | 13 | 11.6% | 30.233 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-013 | Stage6E | S6E-SUPPORT-001 | 1581 | 639 | 46.9% | 21.450 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-014 | Stage6E | S6E-SUPPORT-002 | 1171 | 473 | 48.8% | 20.700 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-015 | Stage6E | S6E-SUPPORT-003 | 764 | 304 | 51.9% | 19.119 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-016 | Stage6E | S6E-SUPPORT-004 | 1395 | 551 | 47.0% | 20.935 | strong_research_casebook_high_yield_but_not_live_permission |

## Example Rows

| target_id | rank | window | date | state | positive | matched_values | sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S6F-TARGET-001 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | board_scoreboard:top_canonicals + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical |
| S6F-TARGET-001 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:combos |
| S6F-TARGET-001 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals |
| S6F-TARGET-001 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B12:combos |
| S6F-TARGET-001 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-001 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals |
| S6F-TARGET-001 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B12:boxed_canonicals |
| S6F-TARGET-001 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B12:combos |
| S6F-TARGET-002 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | board_scoreboard:top_canonicals + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical |
| S6F-TARGET-002 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:combos |
| S6F-TARGET-002 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals |
| S6F-TARGET-002 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B12:combos |
| S6F-TARGET-002 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-002 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals |
| S6F-TARGET-002 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B12:boxed_canonicals |
| S6F-TARGET-002 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B12:combos |
| S6F-TARGET-003 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:combos |
| S6F-TARGET-003 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals |
| S6F-TARGET-003 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B12:combos |
| S6F-TARGET-003 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-003 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals |
| S6F-TARGET-003 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B12:boxed_canonicals |
| S6F-TARGET-003 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B12:combos |
| S6F-TARGET-003 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B24:boxed_canonicals |
| S6F-TARGET-004 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | board_scoreboard:top_canonicals + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical |
| S6F-TARGET-004 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | OntarioCanada4 | 1 | 014 | board_scoreboard:top_canonicals + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical |
| S6F-TARGET-004 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-004 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-004 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-004 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-004 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:combos + positional:positional_canonical |
| S6F-TARGET-004 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:combos + positional:positional_combo |
| S6F-TARGET-005 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-005 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-005 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-005 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-005 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:combos + positional:positional_canonical |
| S6F-TARGET-005 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:combos + positional:positional_combo |
| S6F-TARGET-005 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:convergence_box_first:B12 + positional:positional_canonical |
| S6F-TARGET-005 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:convergence_box_first:B12 + positional:positional_combo |
| S6F-TARGET-006 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-006 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-006 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-006 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-006 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:combos + positional:positional_canonical |
| S6F-TARGET-006 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:combos + positional:positional_combo |
| S6F-TARGET-006 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:convergence_box_first:B12 + positional:positional_canonical |
| S6F-TARGET-006 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:convergence_box_first:B12 + positional:positional_combo |
| S6F-TARGET-007 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-007 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_canonical |
| S6F-TARGET-007 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:combos + positional:positional_canonical |
| S6F-TARGET-007 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:convergence_box_first:B12 + positional:positional_canonical |
| S6F-TARGET-007 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first:B12 + positional:positional_canonical |
| S6F-TARGET-007 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12 + positional:positional_canonical |
| S6F-TARGET-007 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12 + positional:positional_canonical |
| S6F-TARGET-007 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12 + positional:positional_canonical |
| S6F-TARGET-008 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:conversion_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-008 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:boxed_canonicals + positional:positional_combo |
| S6F-TARGET-008 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy:play_box_first:B12:combos + positional:positional_combo |
| S6F-TARGET-008 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:convergence_box_first:B12 + positional:positional_combo |
| S6F-TARGET-008 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first:B12 + positional:positional_combo |
| S6F-TARGET-008 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12 + positional:positional_combo |
| S6F-TARGET-008 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12 + positional:positional_combo |
| S6F-TARGET-008 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-16 | SouthCarolina4 | 1 | 077 | old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12 + positional:positional_combo |
| S6F-TARGET-009 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals |
| S6F-TARGET-009 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals |
| S6F-TARGET-009 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:analysis_prefix:B36 |
| S6F-TARGET-009 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-10 | SouthCarolina4 | 1 | 069 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first:B36 |
| S6F-TARGET-009 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-22 | NewYork4 | 1 | 168 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals |
| S6F-TARGET-009 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-22 | NewYork4 | 1 | 168 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:combos |
| S6F-TARGET-009 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-22 | NewYork4 | 1 | 168 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals |
| S6F-TARGET-009 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-22 | NewYork4 | 1 | 168 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:combos |
| S6F-TARGET-010 | 1 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-11 | Florida4 | 1 | 149 | old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B12:combos |
| S6F-TARGET-010 | 2 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-11 | Florida4 | 1 | 149 | old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:conversion_box_first:B12:combos |
| S6F-TARGET-010 | 3 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-11 | Florida4 | 1 | 149 | old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:v0_2_default:B12:combos |
| S6F-TARGET-010 | 4 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-11 | Florida4 | 1 | 149 | old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:analysis_prefix:B12:combos |
| S6F-TARGET-010 | 5 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-11 | Florida4 | 1 | 149 | old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:conversion_box_first:B12:combos |
| S6F-TARGET-010 | 6 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-11 | Florida4 | 1 | 149 | old_candidate_universe:pack_method:mirror_pair_closure:canonical + old_play_card:strategy:v0_2_default:B12:combos |
| S6F-TARGET-010 | 7 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-23 | NorthCarolina4 | 1 | 479 | old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:analysis_prefix:B12:combos |
| S6F-TARGET-010 | 8 | WINDOW_2026-03-09_to_2026-03-23 | 2026-03-23 | NorthCarolina4 | 1 | 479 | old_candidate_universe:pack:mirror_pair_closure + old_play_card:strategy:v0_2_default:B12:combos |

## Files

- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6F_PRIORITY_BUCKET_CASEBOOK.csv`
- example_ledger_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6F_BUCKET_EXAMPLE_LEDGER.csv`
