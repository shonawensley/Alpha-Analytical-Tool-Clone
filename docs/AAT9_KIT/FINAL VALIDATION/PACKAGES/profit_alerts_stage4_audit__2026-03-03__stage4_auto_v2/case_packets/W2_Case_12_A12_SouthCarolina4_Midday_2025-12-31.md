# Profit Alerts Stage-4 Audit Packet — W2 Case 12

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W2 |
| Case number | 12 |
| AlertId | A12 |
| StateKey | SouthCarolina4 |
| Variant | Midday |
| Results date D | 2025-12-31 |
| Status | EXPIRED |
| Suggested | STR8_4of8 |
| Canonical | 006 |
| Badges | PERM/CLAMP |
| RowNum (eval/board) | 68 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-31/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-31/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-31/SouthCarolina4/winners/SouthCarolina4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-31/SouthCarolina4/winners/SouthCarolina4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-31/SouthCarolina4/json/SouthCarolina4_tables.json
- Stable excerpt: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-31/SouthCarolina4/stable/SouthCarolina4/SouthCarolina4_stable_patterns_scores__profit_alerts_excerpt.csv

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | SouthCarolina4 |
| Variant | Midday |
| AlertId | A12 |
| Strength | 3 |
| Suggested | STR8_4of8 |
| CapLines | 5 |
| DecayDraws | 2 |
| Badges | PERM/CLAMP |
| Canonical | 006 |
| ImpliedSet | ["001","006","051","056"] |
| Winner Midday | 653 |
| Winner Evening | 044 |

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
| start_when | 2025-12-31 Midday |
| expiry_when | 2026-01-01 Midday |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "clamp_rule": "STR8_4of8:first_digit",
  "lane_size": 4,
  "order_dominance": 0.75,
  "orders_modal_rows": 3,
  "orders_modal_value": "006",
  "rowcov": 4,
  "stable_column": "1",
  "stable_draw": "Draw1",
  "stable_family_id": "2",
  "stable_scores_relpath": "SouthCarolina4/stable/SouthCarolina4/SouthCarolina4_stable_patterns_scores.csv",
  "stable_section": "Midday",
  "stable_set": "Set1",
  "stable_why": "boxed|cov4|hp_repeat2|vstr2|vstr3|hot2|dom_last|perm2|hidden3v|double_mirror|set_chain2|draw_chain7"
}
```

## Stable locator + excerpt row (if applicable)
| Field | Value |
|---|---|
| stable_section | Midday |
| stable_set | Set1 |
| stable_draw | Draw1 |
| stable_column | 1 |
| stable_family_id | 2 |
| stable_why | boxed|cov4|hp_repeat2|vstr2|vstr3|hot2|dom_last|perm2|hidden3v|double_mirror|set_chain2|draw_chain7 |

| Field | Value |
|---|---|
| type | boxed |
| score | 35.5 |
| rows | R2,R4,R6,R8 |
| orders_modal_value | 006 |
| orders_modal_rows | 3 |
| order dominance (computed later) |  |
| why | boxed|cov4|hp_repeat2|vstr2|vstr3|hot2|dom_last|perm2|hidden3v|double_mirror|set_chain2|draw_chain7 |

## JSON environment snapshot at locator (audit mirror)
| Field | Value |
|---|---|
| json_section | Midday |
| json_set | Set1 |
| json_draw | Draw1 |
| json_col | 1 |
| json_arr_len | 7 |
| json_arr_idx | 6 |
| R2 @col | 006** |
| R4 @col | 006** |
| R6 @col | 060** |
| R8 @col | 006** |
| R2 last3 | 006 |
| R4 last3 | 006 |
| R6 last3 | 060 |
| R8 last3 | 006 |

## Contract checks (auto)
| Field | Value |
|---|---|
| expected_row_type | CANDIDATE |
| eval_row_type | CANDIDATE |
| row_type_ok | Y |
| implied_set_required | Y |
| implied_set_parse_error |  |
| implied_set_size | 4 |
| box_canonical_ok | NA |
| box_family_ok | NA |
| a08_base_pointer_ok | NA |
| a11_star_fields_ok | NA |
| stable_locator_present | Y |
| stable_excerpt_row_found | Y |
| json_snapshot_ok | Y |
| A12 orders_modal_value | 006 |
| A12 orders_modal_rows (evidence) | 3 |
| A12 order_dominance (evidence) | 0.75 |
| A12 modal_rows (computed) | 3 |
| A12 dominance (computed) | 0.75 |
| A12 dominance ok | Y |

## Audit questions (yes/no)
1) Do JSON row-ends at the locator show the same modal order in 3 of 4 rows?
2) Do Stable excerpt + Evidence JSON agree on modal order + dominance fields?
3) Is `ImpliedSet` consistent with clamp_rule + modal order (no guessing by evaluator)?

## Notes / overrides (human / Deep Research)
- HumanVerdict: (PASS/FAIL/AMBIG)  
- HumanNotes:  
- ProposedFix (if FAIL):
