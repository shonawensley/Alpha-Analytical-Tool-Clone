# Analysis Arena Stage 6F Priority Bucket Casebook

## Guardrail

This casebook is evidence review only. It does not create live scoring, candidate-generation, translator, hard-veto, support-promotion, or budget permission.

## Target Summary

| target_id | source_stage | candidate | rows | positive | fp | yield | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S6F-TARGET-001 | Stage6D | S6D-RESCUE-003 | 502 | 492 | 58.3% | 40.898 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-002 | Stage6D | S6D-RESCUE-004 | 256 | 246 | 50.5% | 47.582 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-003 | Stage6D | S6D-RESCUE-005 | 251 | 242 | 50.7% | 47.544 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-004 | Stage6D | S6D-RESCUE-009 | 104 | 101 | 54.0% | 44.690 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-005 | Stage6D | S6D-RESCUE-011 | 79 | 76 | 52.1% | 46.061 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-006 | Stage6D | S6D-RESCUE-012 | 74 | 74 | 50.7% | 49.333 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-007 | Stage6D | S6D-RESCUE-013 | 37 | 36 | 27.5% | 70.588 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-008 | Stage6D | S6D-RESCUE-017 | 15 | 13 | 54.5% | 39.394 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-009 | Stage6D | S6D-RESCUE-001 | 502 | 492 | 58.3% | 40.898 | strong_research_casebook_high_yield_but_not_live_permission |
| S6F-TARGET-010 | Stage6D | S6D-RESCUE-002 | 497 | 488 | 58.4% | 40.837 | strong_research_casebook_high_yield_but_not_live_permission |
| S6F-TARGET-011 | Stage6D | S6D-RESCUE-006 | 222 | 222 | 64.0% | 36.039 | strong_research_casebook_high_yield_but_not_live_permission |
| S6F-TARGET-012 | Stage6D | S6D-RESCUE-007 | 222 | 222 | 64.0% | 36.039 | strong_research_casebook_high_yield_but_not_live_permission |
| S6F-TARGET-013 | Stage6E | S6E-SUPPORT-001 | 401 | 391 | 55.2% | 43.638 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-014 | Stage6E | S6E-SUPPORT-002 | 220 | 220 | 50.2% | 49.774 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-015 | Stage6E | S6E-SUPPORT-003 | 200 | 200 | 50.7% | 49.261 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-016 | Stage6E | S6E-SUPPORT-004 | 203 | 193 | 44.8% | 52.446 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-017 | Stage6E | S6E-SUPPORT-005 | 198 | 189 | 45.0% | 52.500 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-018 | Stage6E | S6E-SUPPORT-006 | 80 | 80 | 54.5% | 45.455 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-019 | Stage6E | S6E-SUPPORT-007 | 80 | 77 | 48.7% | 49.359 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-020 | Stage6E | S6E-SUPPORT-008 | 60 | 57 | 46.9% | 50.442 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-021 | Stage6E | S6E-SUPPORT-009 | 36 | 36 | 25.0% | 75.000 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-022 | Stage6E | S6E-SUPPORT-010 | 788 | 752 | 51.0% | 46.737 | strong_research_casebook_high_yield_but_not_live_permission |
| S6F-TARGET-023 | Stage6E | S6E-SUPPORT-011 | 387 | 361 | 45.7% | 50.631 | strong_research_casebook_high_yield_but_not_live_permission |
| S6F-TARGET-024 | Stage6E | S6E-SUPPORT-012 | 90 | 73 | 33.3% | 54.074 | strong_research_casebook_high_yield_but_not_live_permission |

## Example Rows

| target_id | rank | window | date | state | positive | matched_values | sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S6F-TARGET-001 | 1 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_candidate_universe:top_canonicals |
| S6F-TARGET-001 | 2 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:boxed_canonicals |
| S6F-TARGET-001 | 3 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:combos |
| S6F-TARGET-001 | 4 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B24:boxed_canonicals |
| S6F-TARGET-001 | 5 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals |
| S6F-TARGET-001 | 6 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B12:combos |
| S6F-TARGET-001 | 7 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-001 | 8 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals |
| S6F-TARGET-002 | 1 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_candidate_universe:top_canonicals |
| S6F-TARGET-002 | 2 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:boxed_canonicals |
| S6F-TARGET-002 | 3 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:combos |
| S6F-TARGET-002 | 4 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B24:boxed_canonicals |
| S6F-TARGET-002 | 5 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals |
| S6F-TARGET-002 | 6 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B12:combos |
| S6F-TARGET-002 | 7 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-002 | 8 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals |
| S6F-TARGET-003 | 1 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_candidate_universe:top_canonicals |
| S6F-TARGET-003 | 2 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:boxed_canonicals |
| S6F-TARGET-003 | 3 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:combos |
| S6F-TARGET-003 | 4 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B24:boxed_canonicals |
| S6F-TARGET-003 | 5 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals |
| S6F-TARGET-003 | 6 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B12:combos |
| S6F-TARGET-003 | 7 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-003 | 8 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals |
| S6F-TARGET-004 | 1 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals |
| S6F-TARGET-004 | 2 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals |
| S6F-TARGET-004 | 3 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B36:boxed_canonicals |
| S6F-TARGET-004 | 4 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B36:combos |
| S6F-TARGET-004 | 5 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:analysis_prefix:B36 |
| S6F-TARGET-004 | 6 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first:B36 |
| S6F-TARGET-004 | 7 | WINDOW_2026-01-15_to_2026-01-18 | 2026-01-16 | Indiana4 | 1 | 368 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals |
| S6F-TARGET-004 | 8 | WINDOW_2026-01-15_to_2026-01-18 | 2026-01-16 | Indiana4 | 1 | 368 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:analysis_prefix:B36 |
| S6F-TARGET-005 | 1 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B24:boxed_canonicals |
| S6F-TARGET-005 | 2 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-005 | 3 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B24:boxed_canonicals |
| S6F-TARGET-005 | 4 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B24:combos |
| S6F-TARGET-005 | 5 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:analysis_prefix:B24 |
| S6F-TARGET-005 | 6 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:convergence_box_first:B24 |
| S6F-TARGET-005 | 7 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first:B24 |
| S6F-TARGET-005 | 8 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B24 |
| S6F-TARGET-006 | 1 | WINDOW_2025-12-30_to_2026-01-09 | 2026-01-08 | Indiana4 | 1 | 224 | old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:convergence_box_first:B12 |
| S6F-TARGET-006 | 2 | WINDOW_2025-12-30_to_2026-01-09 | 2026-01-08 | Indiana4 | 1 | 224 | old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12 |
| S6F-TARGET-006 | 3 | WINDOW_2025-12-30_to_2026-01-09 | 2026-01-08 | Indiana4 | 1 | 224 | old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12 |
| S6F-TARGET-006 | 4 | WINDOW_2025-12-30_to_2026-01-09 | 2026-01-08 | Indiana4 | 1 | 224 | old_candidate_universe:pack:aux_vtrac_index_overdue + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12 |
| S6F-TARGET-006 | 5 | WINDOW_2025-12-30_to_2026-01-09 | 2026-01-08 | Indiana4 | 1 | 224 | old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_play_card:strategy_card:convergence_box_first:B12 |
| S6F-TARGET-006 | 6 | WINDOW_2025-12-30_to_2026-01-09 | 2026-01-08 | Indiana4 | 1 | 224 | old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetA:B12 |
| S6F-TARGET-006 | 7 | WINDOW_2025-12-30_to_2026-01-09 | 2026-01-08 | Indiana4 | 1 | 224 | old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_play_card:strategy_card:conversion_box_first_conditional_lenient_presetB:B12 |
| S6F-TARGET-006 | 8 | WINDOW_2025-12-30_to_2026-01-09 | 2026-01-08 | Indiana4 | 1 | 224 | old_candidate_universe:pack_method:aux_vtrac_index_overdue:canonical + old_play_card:strategy_card:conversion_box_first_conditional_strict_presetA:B12 |
| S6F-TARGET-007 | 1 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:boxed_canonicals |
| S6F-TARGET-007 | 2 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:combos |
| S6F-TARGET-007 | 3 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B12:combos |
| S6F-TARGET-007 | 4 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B12:boxed_canonicals |
| S6F-TARGET-007 | 5 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:play_box_first:B12:combos |
| S6F-TARGET-007 | 6 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:v0_2_default:B12:boxed_canonicals |
| S6F-TARGET-007 | 7 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:v0_2_default:B12:combos |
| S6F-TARGET-007 | 8 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy_card:analysis_prefix:B12 |
| S6F-TARGET-008 | 1 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack:stable_top + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical |
| S6F-TARGET-008 | 2 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:stable_top:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical |
| S6F-TARGET-008 | 3 | WINDOW_2026-01-15_to_2026-01-18 | 2026-01-16 | Indiana4 | 1 | 368 | old_candidate_universe:pack:stable_top + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical |
| S6F-TARGET-008 | 4 | WINDOW_2026-01-15_to_2026-01-18 | 2026-01-16 | Indiana4 | 1 | 368 | old_candidate_universe:pack_method:stable_top:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical |
| S6F-TARGET-008 | 5 | WINDOW_2026-01-15_to_2026-01-18 | 2026-01-16 | NewJersey4 | 1 | 018 | old_candidate_universe:pack:stable_top + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical |
| S6F-TARGET-008 | 6 | WINDOW_2026-01-15_to_2026-01-18 | 2026-01-16 | NewJersey4 | 1 | 018 | old_candidate_universe:pack_method:stable_top:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical |
| S6F-TARGET-008 | 7 | WINDOW_2026-01-15_to_2026-01-18 | 2026-01-16 | OntarioCanada4 | 1 | 039 | old_candidate_universe:pack:stable_top + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical |
| S6F-TARGET-008 | 8 | WINDOW_2026-01-15_to_2026-01-18 | 2026-01-16 | OntarioCanada4 | 1 | 039 | old_candidate_universe:pack_method:stable_top:canonical + old_candidate_universe:pack_method:vtrac_enhanced_top:canonical |
| S6F-TARGET-009 | 1 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_candidate_universe:top_canonicals |
| S6F-TARGET-009 | 2 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:boxed_canonicals |
| S6F-TARGET-009 | 3 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:combos |
| S6F-TARGET-009 | 4 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B24:boxed_canonicals |
| S6F-TARGET-009 | 5 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals |
| S6F-TARGET-009 | 6 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B12:combos |
| S6F-TARGET-009 | 7 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-009 | 8 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals |
| S6F-TARGET-010 | 1 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_candidate_universe:top_canonicals |
| S6F-TARGET-010 | 2 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:boxed_canonicals |
| S6F-TARGET-010 | 3 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B12:combos |
| S6F-TARGET-010 | 4 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B24:boxed_canonicals |
| S6F-TARGET-010 | 5 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:analysis_prefix:B36:boxed_canonicals |
| S6F-TARGET-010 | 6 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B12:combos |
| S6F-TARGET-010 | 7 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B24:boxed_canonicals |
| S6F-TARGET-010 | 8 | WINDOW_2025-12-30_to_2026-01-09 | 2025-12-30 | Connecticut4 | 1 | 059 | old_candidate_universe:pack_method:vtrac_enhanced_top:canonical + old_play_card:strategy:conversion_box_first:B36:boxed_canonicals |

## Files

- casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6F_PRIORITY_BUCKET_CASEBOOK.csv`
- example_ledger_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6F_BUCKET_EXAMPLE_LEDGER.csv`
