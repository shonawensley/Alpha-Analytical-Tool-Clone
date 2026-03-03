# Profit Alerts Stage-4 Audit Packet — W2 Case 10

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W2 |
| Case number | 10 |
| AlertId | A12 |
| StateKey | NewJersey4 |
| Variant | Midday |
| Results date D | 2026-01-08 |
| Status | HIT |
| Suggested | STR8_4of8 |
| Canonical | 089 |
| Badges | PERM/CLAMP |
| RowNum (eval/board) | 66 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-08/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-08/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-08/NewJersey4/winners/NewJersey4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-08/NewJersey4/winners/NewJersey4
- Winner HTML (best guess): docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-08/NewJersey4/winners/NewJersey4/NewJersey4_vtrac14_winner_089_20260110_034428.html
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-08/NewJersey4/json/NewJersey4_tables.json
- Stable excerpt: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-08/NewJersey4/stable/NewJersey4/NewJersey4_stable_patterns_scores__profit_alerts_excerpt.csv

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | NewJersey4 |
| Variant | Midday |
| AlertId | A12 |
| Strength | 3 |
| Suggested | STR8_4of8 |
| CapLines | 5 |
| DecayDraws | 2 |
| Badges | PERM/CLAMP |
| Canonical | 089 |
| ImpliedSet | ["034","039","084","089"] |
| Winner Midday | 089 |
| Winner Evening | 055 |

## Eval row (extracted)
| Field | Value |
|---|---|
| row_type | CANDIDATE |
| strict_hit (D-only) | Y |
| hit_within_decay (primary) | Y |
| hit_any_within_decay (diagnostic) | Y |
| hit_within_7 | Y |
| hit_within_14 | Y |
| hit_type | Straight+Boxed |
| hit_any_type | Straight+Boxed |
| start_when | 2026-01-08 Midday |
| expiry_when | 2026-01-09 Midday |
| hit_when | 2026-01-08 Midday |
| time_to_hit_steps | 0 |

## Evidence JSON (pretty)
```json
{
  "clamp_rule": "STR8_4of8:first_digit",
  "lane_size": 4,
  "order_dominance": 0.75,
  "orders_modal_rows": 3,
  "orders_modal_value": "098",
  "rowcov": 4,
  "stable_column": "1",
  "stable_draw": "Draw1",
  "stable_family_id": "14.0",
  "stable_scores_relpath": "NewJersey4/stable/NewJersey4/NewJersey4_stable_patterns_scores.csv",
  "stable_section": "Midday",
  "stable_set": "Set1",
  "stable_why": "boxed|cov4|hp_repeat4|vstr2|vstr3|hot2|dom_last|perm2|set_chain2|draw_chain4"
}
```

## Stable locator + excerpt row (if applicable)
| Field | Value |
|---|---|
| stable_section | Midday |
| stable_set | Set1 |
| stable_draw | Draw1 |
| stable_column | 1 |
| stable_family_id | 14.0 |
| stable_why | boxed|cov4|hp_repeat4|vstr2|vstr3|hot2|dom_last|perm2|set_chain2|draw_chain4 |

| Field | Value |
|---|---|
| type | boxed |
| score | 32.0 |
| rows | R2,R4,R6,R8 |
| orders_modal_value | 098 |
| orders_modal_rows | 3 |
| order dominance (computed later) |  |
| why | boxed|cov4|hp_repeat4|vstr2|vstr3|hot2|dom_last|perm2|set_chain2|draw_chain4 |

## JSON environment snapshot at locator (audit mirror)
| Field | Value |
|---|---|
| json_section | Midday |
| json_set | Set1 |
| json_draw | Draw1 |
| json_col | 1 |
| json_arr_len | 7 |
| json_arr_idx | 6 |
| R2 @col | 098** |
| R4 @col | 098** |
| R6 @col | 089** |
| R8 @col | 098** |
| R2 last3 | 098 |
| R4 last3 | 098 |
| R6 last3 | 089 |
| R8 last3 | 098 |

## Contract checks (auto)
| Field | Value |
|---|---|
| expected_row_type | CANDIDATE |
| eval_row_type | CANDIDATE |
| row_type_ok | Y |
| implied_set_required | Y |
| implied_set_parse_error |  |
| implied_set_size | 4 |
| stable_locator_present | Y |
| stable_excerpt_row_found | Y |
| json_snapshot_ok | Y |
| A12 orders_modal_value | 098 |
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
