# Profit Alerts Stage-4 Audit Packet — W2 Case 3

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W2 |
| Case number | 3 |
| AlertId | A04 |
| StateKey | SouthCarolina4 |
| Variant | Evening |
| Results date D | 2026-01-03 |
| Status | HIT |
| Suggested | BOX |
| Canonical | 015 |
| Badges | PERSIST |
| RowNum (eval/board) | 27 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2026-01-03/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2026-01-03/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2026-01-03/SouthCarolina4/winners/SouthCarolina4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2026-01-03/SouthCarolina4/winners/SouthCarolina4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2026-01-03/SouthCarolina4/json/SouthCarolina4_tables.json
- Stable excerpt: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2026-01-03/SouthCarolina4/stable/SouthCarolina4/SouthCarolina4_stable_patterns_scores__profit_alerts_excerpt.csv

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | SouthCarolina4 |
| Variant | Evening |
| AlertId | A04 |
| Strength | 3 |
| Suggested | BOX |
| CapLines | 12 |
| DecayDraws | 3 |
| Badges | PERSIST |
| Canonical | 015 |
| ImpliedSet | ["015","051","105","150","501","510"] |
| Winner Midday | 189 |
| Winner Evening | 051 |

## Eval row (extracted)
| Field | Value |
|---|---|
| row_type | CANDIDATE |
| strict_hit (D-only) | Y |
| hit_within_decay (primary) | Y |
| hit_any_within_decay (diagnostic) | Y |
| hit_within_7 | Y |
| hit_within_14 | Y |
| hit_type | Boxed |
| hit_any_type | Boxed |
| start_when | 2026-01-03 Evening |
| expiry_when | 2026-01-05 Evening |
| hit_when | 2026-01-03 Evening |
| time_to_hit_steps | 0 |

## Evidence JSON (pretty)
```json
{
  "ba_score": 1,
  "persistence_set_count": 2,
  "rowcov": 4,
  "stable_column": "1",
  "stable_draw": "Draw1",
  "stable_family_id": "2.0",
  "stable_scores_relpath": "SouthCarolina4/stable/SouthCarolina4/SouthCarolina4_stable_patterns_scores.csv",
  "stable_section": "Evening",
  "stable_set": "Set1",
  "stable_why": "boxed|cov4|hp_repeat2|vstr2|mirror|hot2|dom_last|perm2|hidden3v|set_chain2|draw_chain3"
}
```

## Stable locator + excerpt row (if applicable)
| Field | Value |
|---|---|
| stable_section | Evening |
| stable_set | Set1 |
| stable_draw | Draw1 |
| stable_column | 1 |
| stable_family_id | 2.0 |
| stable_why | boxed|cov4|hp_repeat2|vstr2|mirror|hot2|dom_last|perm2|hidden3v|set_chain2|draw_chain3 |

| Field | Value |
|---|---|
| type | boxed |
| score | 26.5 |
| rows | R2,R4,R6,R8 |
| orders_modal_value | 051 |
| orders_modal_rows | 2 |
| order dominance (computed later) |  |
| why | boxed|cov4|hp_repeat2|vstr2|mirror|hot2|dom_last|perm2|hidden3v|set_chain2|draw_chain3 |

## JSON environment snapshot at locator (audit mirror)
| Field | Value |
|---|---|
| json_section | Evening |
| json_set | Set1 |
| json_draw | Draw1 |
| json_col | 1 |
| json_arr_len | 7 |
| json_arr_idx | 6 |
| R2 @col | 051** |
| R4 @col | 051** |
| R6 @col | 015** |
| R8 @col | 015** |
| R2 last3 | 051 |
| R4 last3 | 051 |
| R6 last3 | 015 |
| R8 last3 | 015 |

## Contract checks (auto)
| Field | Value |
|---|---|
| expected_row_type | CANDIDATE |
| eval_row_type | CANDIDATE |
| row_type_ok | Y |
| implied_set_required | Y |
| implied_set_parse_error |  |
| implied_set_size | 6 |
| box_canonical_ok | Y |
| box_family_ok | Y |
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
