# Profit Alerts Stage-4 Audit Packet — W1 Case 5

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W1 |
| Case number | 5 |
| AlertId | A05 |
| StateKey | NewJersey4 |
| Variant | Evening |
| Results date D | 2025-06-21 |
| Status | HIT |
| Suggested | STR8_3 |
| Canonical | 788 |
| Badges | PERM/HP7 |
| RowNum (eval/board) | 46 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/NewJersey4/winners/NewJersey4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/NewJersey4/winners/NewJersey4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/NewJersey4/json/NewJersey4_tables.json
- Stable excerpt: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/NewJersey4/stable/NewJersey4/NewJersey4_stable_patterns_scores__profit_alerts_excerpt.csv

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | NewJersey4 |
| Variant | Evening |
| AlertId | A05 |
| Strength | 4 |
| Suggested | STR8_3 |
| CapLines | 3 |
| DecayDraws | 2 |
| Badges | PERM/HP7 |
| Canonical | 788 |
| ImpliedSet | ["788","878","887"] |
| Winner Midday | 182 |
| Winner Evening | 554 |

## Eval row (extracted)
| Field | Value |
|---|---|
| row_type | CANDIDATE |
| strict_hit (D-only) | N |
| hit_within_decay (primary) | Y |
| hit_any_within_decay (diagnostic) | Y |
| hit_within_7 | Y |
| hit_within_14 | Y |
| hit_type | Straight+Boxed |
| hit_any_type | Straight+Boxed |
| start_when | 2025-06-21 Evening |
| expiry_when | 2025-06-22 Evening |
| hit_when | 2025-06-22 Evening |
| time_to_hit_steps | 1 |

## Evidence JSON (pretty)
```json
{
  "horiz_span": 7,
  "lane_size": 3,
  "orders_modal_rows": 3,
  "orders_modal_value": "887",
  "stable_column": "1",
  "stable_draw": "Draw1",
  "stable_family_id": "29",
  "stable_scores_relpath": "NewJersey4/stable/NewJersey4/NewJersey4_stable_patterns_scores.csv",
  "stable_section": "Evening",
  "stable_set": "Set1",
  "stable_why": "straight|cov3|hp_repeat7|vstr2|vstr3|hot2|double_mirror|vtrac_straight|set_chain3|draw_chain5"
}
```

## Stable locator + excerpt row (if applicable)
| Field | Value |
|---|---|
| stable_section | Evening |
| stable_set | Set1 |
| stable_draw | Draw1 |
| stable_column | 1 |
| stable_family_id | 29 |
| stable_why | straight|cov3|hp_repeat7|vstr2|vstr3|hot2|double_mirror|vtrac_straight|set_chain3|draw_chain5 |

| Field | Value |
|---|---|
| type | straight |
| score | 37.0 |
| rows | R2,R4,R6 |
| orders_modal_value | 887 |
| orders_modal_rows | 3 |
| order dominance (computed later) |  |
| why | straight|cov3|hp_repeat7|vstr2|vstr3|hot2|double_mirror|vtrac_straight|set_chain3|draw_chain5 |

## JSON environment snapshot at locator (audit mirror)
| Field | Value |
|---|---|
| json_section | Evening |
| json_set | Set1 |
| json_draw | Draw1 |
| json_col | 1 |
| json_arr_len | 7 |
| json_arr_idx | 6 |
| R2 @col | 0887** |
| R4 @col | 0887** |
| R6 @col | 8870** |
| R8 @col | 7088** |
| R2 last3 | 887 |
| R4 last3 | 887 |
| R6 last3 | 870 |
| R8 last3 | 088 |

## Contract checks (auto)
| Field | Value |
|---|---|
| expected_row_type | CANDIDATE |
| eval_row_type | CANDIDATE |
| row_type_ok | Y |
| implied_set_required | Y |
| implied_set_parse_error |  |
| implied_set_size | 3 |
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
