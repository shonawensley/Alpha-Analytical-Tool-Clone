# Brain 2 Rank Source Registry

- Analytical rank status: `INVALID_STATIC_ORDER`
- Replacement ranker introduced: `False`

| Source | Timing | Scope | Validity | Displayed | Influential | Phase 2 treatment |
|---|---|---|---|---|---|---|
| `brain2_legacy_board_priority` | PRE_MIDDAY_OR_POST_MIDDAY_PRE_EVENING_BY_INVOCATION | cross_state_board | INVALID_STATIC_ORDER | True | True | preserve relationship/spent evidence; quarantine rank and score as diagnostic-only |
| `predictive_portfolio_arena_first` | PRE_RESULT | cross_state_portfolio | INHERITS_INVALID_STATIC_ORDER | True | True | superseded for analytical rank evaluation |
| `predictive_portfolio_tool_first` | PRE_RESULT | cross_state_control_arm | UNVALIDATED_HEURISTIC | True | True | retain as named legacy control-arm heuristic; do not promote to Brain 2 analytical rank |
| `predictive_portfolio_profit_alerts` | PRE_RESULT | cross_state_control_arm | UNVALIDATED_HEURISTIC | True | True | retain as named diagnostic heuristic; do not promote to Brain 2 analytical rank |
| `portfolio_vs_results_tool_first` | PRE_RESULT_RANK_POST_RESULT_EVALUATION | cross_state_evaluation | UNVALIDATED_HEURISTIC_EVALUATION | True | False | retain as historical control-arm evaluation only |
| `superbrain_experimental_rankers` | PRE_RESULT_RANK_POST_RESULT_HARNESS | cross_state_experiment | EXPERIMENTAL_UNVALIDATED | True | False | retain as experiment; not a current Brain 2 rank source |
| `post_midday_competition_priority` | POST_MIDDAY_PRE_EVENING | period_specific_board | DECISION_TIME_SPECIFIC_LEGACY_PRIORITY | True | True | keep distinct from pre-Midday rank; quarantine strongest-state claims |
| `tool_local_candidate_ranks` | PRE_RESULT | within_state_candidate_or_lane | OUT_OF_SCOPE_NOT_A_STATE_RANK | True | True | preserve unchanged; never reinterpret as cross-state analytical rank |
| `due_doubles_state_order` | PRE_RESULT | mechanism_specific_state_context | VALID_MECHANISM_CONTEXT_NOT_GLOBAL_STATE_RANK | True | True | preserve as mechanism-specific context only |
| `post_result_deep_review_priority` | POST_RESULT | review_only | VALID_REVIEW_PRIORITY_NOT_PREDICTIVE_RANK | True | False | preserve but label truth-aware; never use for predictive Capture@K |
