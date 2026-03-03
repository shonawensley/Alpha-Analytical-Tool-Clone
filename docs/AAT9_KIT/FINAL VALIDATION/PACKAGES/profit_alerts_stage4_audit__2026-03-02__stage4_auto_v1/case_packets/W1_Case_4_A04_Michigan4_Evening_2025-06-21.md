# Profit Alerts Stage-4 Audit Packet — W1 Case 4

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W1 |
| Case number | 4 |
| AlertId | A04 |
| StateKey | Michigan4 |
| Variant | Evening |
| Results date D | 2025-06-21 |
| Status | EXPIRED |
| Suggested | BOX |
| Canonical | 057 |
| Badges | PERSIST |
| RowNum (eval/board) | 34 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/Michigan4/winners/Michigan4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/Michigan4/winners/Michigan4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/Michigan4/json/Michigan4_tables.json
- Stable excerpt: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/Michigan4/stable/Michigan4/Michigan4_stable_patterns_scores__profit_alerts_excerpt.csv

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | Michigan4 |
| Variant | Evening |
| AlertId | A04 |
| Strength | 3 |
| Suggested | BOX |
| CapLines | 12 |
| DecayDraws | 3 |
| Badges | PERSIST |
| Canonical | 057 |
| ImpliedSet | ["057","075","507","570","705","750"] |
| Winner Midday | 432 |
| Winner Evening | 280 |

## Eval row (extracted)
| Field | Value |
|---|---|
| row_type | CANDIDATE |
| strict_hit (D-only) | N |
| hit_within_decay (primary) | N |
| hit_any_within_decay (diagnostic) | N |
| hit_within_7 | N |
| hit_within_14 | Y |
| hit_type |  |
| hit_any_type |  |
| start_when | 2025-06-21 Evening |
| expiry_when | 2025-06-23 Evening |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "ba_score": 1,
  "persistence_set_count": 3,
  "rowcov": 4,
  "stable_column": "1",
  "stable_draw": "Draw1",
  "stable_family_id": "3.0",
  "stable_scores_relpath": "Michigan4/stable/Michigan4/Michigan4_stable_patterns_scores.csv",
  "stable_section": "Evening",
  "stable_set": "Set3",
  "stable_why": "boxed|cov4|hp_repeat2|vstr2|mirror|hot1|dom_last|perm2|hidden3v|set_chain3"
}
```

## Stable locator + excerpt row (if applicable)
| Field | Value |
|---|---|
| stable_section | Evening |
| stable_set | Set3 |
| stable_draw | Draw1 |
| stable_column | 1 |
| stable_family_id | 3.0 |
| stable_why | boxed|cov4|hp_repeat2|vstr2|mirror|hot1|dom_last|perm2|hidden3v|set_chain3 |

| Field | Value |
|---|---|
| type | boxed |
| score | 24.5 |
| rows | R2,R4,R6,R8 |
| orders_modal_value | 057 |
| orders_modal_rows | 2 |
| order dominance (computed later) |  |
| why | boxed|cov4|hp_repeat2|vstr2|mirror|hot1|dom_last|perm2|hidden3v|set_chain3 |

## JSON environment snapshot at locator (audit mirror)
| Field | Value |
|---|---|
| json_section | Evening |
| json_set | Set3 |
| json_draw | Draw1 |
| json_col | 1 |
| json_arr_len | 7 |
| json_arr_idx | 6 |
| R2 @col | 057* |
| R4 @col | 057* |
| R6 @col | 075* |
| R8 @col | 075* |
| R2 last3 | 057 |
| R4 last3 | 057 |
| R6 last3 | 075 |
| R8 last3 | 075 |

## Contract checks (auto)
| Field | Value |
|---|---|
| expected_row_type | CANDIDATE |
| eval_row_type | CANDIDATE |
| row_type_ok | Y |
| implied_set_required | N |
| implied_set_parse_error |  |
| implied_set_size | 6 |
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
