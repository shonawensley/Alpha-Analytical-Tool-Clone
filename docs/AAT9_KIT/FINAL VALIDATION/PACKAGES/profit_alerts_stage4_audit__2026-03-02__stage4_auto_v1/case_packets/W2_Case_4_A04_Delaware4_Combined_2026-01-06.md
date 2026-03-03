# Profit Alerts Stage-4 Audit Packet — W2 Case 4

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W2 |
| Case number | 4 |
| AlertId | A04 |
| StateKey | Delaware4 |
| Variant | Combined |
| Results date D | 2026-01-06 |
| Status | EXPIRED |
| Suggested | BOX |
| Canonical | 348 |
| Badges | PERSIST/BA |
| RowNum (eval/board) | 19 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-06/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-06/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-06/Delaware4/winners/Delaware4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-06/Delaware4/winners/Delaware4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-06/Delaware4/json/Delaware4_tables.json
- Stable excerpt: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-06/Delaware4/stable/Delaware4/Delaware4_stable_patterns_scores__profit_alerts_excerpt.csv

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | Delaware4 |
| Variant | Combined |
| AlertId | A04 |
| Strength | 4 |
| Suggested | BOX |
| CapLines | 12 |
| DecayDraws | 3 |
| Badges | PERSIST/BA |
| Canonical | 348 |
| ImpliedSet | ["348","384","438","483","834","843"] |
| Winner Midday | 165 |
| Winner Evening | 758 |

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
| start_when | 2026-01-06 Midday |
| expiry_when | 2026-01-07 Midday |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "ba_score": 3,
  "persistence_set_count": 2,
  "rowcov": 2,
  "stable_column": "1",
  "stable_draw": "Draw1",
  "stable_family_id": "33.0",
  "stable_scores_relpath": "Delaware4/stable/Delaware4/Delaware4_stable_patterns_scores.csv",
  "stable_section": "Combined",
  "stable_set": "Set1",
  "stable_why": "straight|cov2|hp_repeat7|vstr2|mirror|hot2|hidden3v|vtrac_straight|set_chain2"
}
```

## Stable locator + excerpt row (if applicable)
| Field | Value |
|---|---|
| stable_section | Combined |
| stable_set | Set1 |
| stable_draw | Draw1 |
| stable_column | 1 |
| stable_family_id | 33.0 |
| stable_why | straight|cov2|hp_repeat7|vstr2|mirror|hot2|hidden3v|vtrac_straight|set_chain2 |

| Field | Value |
|---|---|
| type | straight |
| score | 25.5 |
| rows | R4,R8 |
| orders_modal_value | 834 |
| orders_modal_rows | 2 |
| order dominance (computed later) |  |
| why | straight|cov2|hp_repeat7|vstr2|mirror|hot2|hidden3v|vtrac_straight|set_chain2 |

## JSON environment snapshot at locator (audit mirror)
| Field | Value |
|---|---|
| json_section | Combined |
| json_set | Set1 |
| json_draw | Draw1 |
| json_col | 1 |
| json_arr_len | 7 |
| json_arr_idx | 6 |
| R2 @col | 54138** |
| R4 @col | 58341** |
| R6 @col | 81534** |
| R8 @col | 18345** |
| R2 last3 | 138 |
| R4 last3 | 341 |
| R6 last3 | 534 |
| R8 last3 | 345 |

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
