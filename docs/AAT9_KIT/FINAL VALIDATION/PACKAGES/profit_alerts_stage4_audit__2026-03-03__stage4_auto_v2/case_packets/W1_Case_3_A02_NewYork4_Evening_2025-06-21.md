# Profit Alerts Stage-4 Audit Packet — W1 Case 3

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W1 |
| Case number | 3 |
| AlertId | A02 |
| StateKey | NewYork4 |
| Variant | Evening |
| Results date D | 2025-06-21 |
| Status | EXPIRED |
| Suggested | STR8_3 |
| Canonical | 055 |
| Badges | CONS/DBL/A10/BA |
| RowNum (eval/board) | 14 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-21/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-21/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-21/NewYork4/winners/NewYork4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-21/NewYork4/winners/NewYork4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-21/NewYork4/json/NewYork4_tables.json
- Stable excerpt: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-21/NewYork4/stable/NewYork4/NewYork4_stable_patterns_scores__profit_alerts_excerpt.csv

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | NewYork4 |
| Variant | Evening |
| AlertId | A02 |
| Strength | 5 |
| Suggested | STR8_3 |
| CapLines | 6 |
| DecayDraws | 2 |
| Badges | CONS/DBL/A10/BA |
| Canonical | 055 |
| ImpliedSet | ["055","505","550"] |
| Winner Midday | 802 |
| Winner Evening | 602 |

## Eval row (extracted)
| Field | Value |
|---|---|
| row_type | CANDIDATE |
| strict_hit (D-only) | N |
| hit_within_decay (primary) | N |
| hit_any_within_decay (diagnostic) | N |
| hit_within_7 | N |
| hit_within_14 | N |
| hit_type |  |
| hit_any_type |  |
| start_when | 2025-06-21 Evening |
| expiry_when | 2025-06-22 Evening |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "ba_score": 3,
  "col": "2",
  "due_doubles_rank": 3,
  "perm": 1,
  "rowcov": 4,
  "stable_column": "2",
  "stable_draw": "Draw1",
  "stable_family_id": "1.0",
  "stable_scores_relpath": "NewYork4/stable/NewYork4/NewYork4_stable_patterns_scores.csv",
  "stable_section": "Evening",
  "stable_set": "Set3",
  "stable_why": "straight|cov4|hp_repeat7|vstr2|vstr3|mirror|cons_full|hot1|cons_3v|double_mirror|vtrac_straight|set_chain3",
  "stub_canonical": "55",
  "stub_column": "2",
  "stub_draw": "Draw1",
  "stub_section": "Evening",
  "stub_set": "Set2",
  "stub_type": "consensus_stub",
  "tail": "55"
}
```

## Stable locator + excerpt row (if applicable)
| Field | Value |
|---|---|
| stable_section | Evening |
| stable_set | Set3 |
| stable_draw | Draw1 |
| stable_column | 2 |
| stable_family_id | 1.0 |
| stable_why | straight|cov4|hp_repeat7|vstr2|vstr3|mirror|cons_full|hot1|cons_3v|double_mirror|vtrac_straight|set_chain3 |

| Field | Value |
|---|---|
| type | straight |
| score | 37.0 |
| rows | R2,R4,R6,R8 |
| orders_modal_value | 055 |
| orders_modal_rows | 4 |
| order dominance (computed later) |  |
| why | straight|cov4|hp_repeat7|vstr2|vstr3|mirror|cons_full|hot1|cons_3v|double_mirror|vtrac_straight|set_chain3 |

## JSON environment snapshot at locator (audit mirror)
| Field | Value |
|---|---|
| json_section | Evening |
| json_set | Set3 |
| json_draw | Draw1 |
| json_col | 2 |
| json_arr_len | 7 |
| json_arr_idx | 5 |
| R2 @col | 055* |
| R4 @col | 055* |
| R6 @col | 055* |
| R8 @col | 055* |
| R2 last3 | 055 |
| R4 last3 | 055 |
| R6 last3 | 055 |
| R8 last3 | 055 |

## Contract checks (auto)
| Field | Value |
|---|---|
| expected_row_type | CANDIDATE |
| eval_row_type | CANDIDATE |
| row_type_ok | Y |
| implied_set_required | Y |
| implied_set_parse_error |  |
| implied_set_size | 3 |
| box_canonical_ok | NA |
| box_family_ok | NA |
| a08_base_pointer_ok | NA |
| a11_star_fields_ok | NA |
| stable_locator_present | Y |
| stable_excerpt_row_found | Y |
| json_snapshot_ok | Y |

## Audit questions (yes/no)
1) Does the Stable excerpt row exist at the locator and match Evidence fields?
2) Does the JSON environment at that locator ‘look consistent’ with the alert’s intended meaning?

## Notes / overrides (human / Deep Research)
- HumanVerdict: (PASS/FAIL/AMBIG)  
- HumanNotes:  
- ProposedFix (if FAIL):
