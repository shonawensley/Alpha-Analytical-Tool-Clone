# Profit Alerts Stage-4 Audit Packet — W1 Case 6

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W1 |
| Case number | 6 |
| AlertId | A05 |
| StateKey | NewYork4 |
| Variant | Combined |
| Results date D | 2025-06-23 |
| Status | EXPIRED |
| Suggested | STR8_3 |
| Canonical | 449 |
| Badges | PERM/HP7 |
| RowNum (eval/board) | 46 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-23/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-23/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-23/NewYork4/winners/NewYork4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-23/NewYork4/winners/NewYork4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-23/NewYork4/json/NewYork4_tables.json
- Stable excerpt: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-23/NewYork4/stable/NewYork4/NewYork4_stable_patterns_scores__profit_alerts_excerpt.csv

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | NewYork4 |
| Variant | Combined |
| AlertId | A05 |
| Strength | 4 |
| Suggested | STR8_3 |
| CapLines | 3 |
| DecayDraws | 2 |
| Badges | PERM/HP7 |
| Canonical | 449 |
| ImpliedSet | ["449","494","944"] |
| Winner Midday | 638 |
| Winner Evening | 767 |

## Eval row (extracted)
| Field | Value |
|---|---|
| row_type | CANDIDATE |
| strict_hit (D-only) | N |
| hit_within_decay (primary) | N |
| hit_any_within_decay (diagnostic) | N |
| hit_within_7 | Y |
| hit_within_14 | Y |
| hit_type |  |
| hit_any_type |  |
| start_when | 2025-06-23 Midday |
| expiry_when | 2025-06-23 Evening |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "horiz_span": 7,
  "lane_size": 3,
  "orders_modal_rows": 4,
  "orders_modal_value": "944",
  "stable_column": "1",
  "stable_draw": "Draw1",
  "stable_family_id": "35",
  "stable_scores_relpath": "NewYork4/stable/NewYork4/NewYork4_stable_patterns_scores.csv",
  "stable_section": "Combined",
  "stable_set": "Set1",
  "stable_why": "straight|cov4|hp_repeat7|vstr2|vstr3|mirror|cons_full|hot2|cons_3v|double_mirror|vtrac_straight|set_chain3|draw_chain7"
}
```

## Stable locator + excerpt row (if applicable)
| Field | Value |
|---|---|
| stable_section | Combined |
| stable_set | Set1 |
| stable_draw | Draw1 |
| stable_column | 1 |
| stable_family_id | 35 |
| stable_why | straight|cov4|hp_repeat7|vstr2|vstr3|mirror|cons_full|hot2|cons_3v|double_mirror|vtrac_straight|set_chain3|draw_chain7 |

| Field | Value |
|---|---|
| type | straight |
| score | 46.0 |
| rows | R2,R4,R6,R8 |
| orders_modal_value | 944 |
| orders_modal_rows | 4 |
| order dominance (computed later) |  |
| why | straight|cov4|hp_repeat7|vstr2|vstr3|mirror|cons_full|hot2|cons_3v|double_mirror|vtrac_straight|set_chain3|draw_chain7 |

## JSON environment snapshot at locator (audit mirror)
| Field | Value |
|---|---|
| json_section | Combined |
| json_set | Set1 |
| json_draw | Draw1 |
| json_col | 1 |
| json_arr_len | 7 |
| json_arr_idx | 6 |
| R2 @col | 94417** |
| R4 @col | 94471** |
| R6 @col | 17944** |
| R8 @col | 71944** |
| R2 last3 | 417 |
| R4 last3 | 471 |
| R6 last3 | 944 |
| R8 last3 | 944 |

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
