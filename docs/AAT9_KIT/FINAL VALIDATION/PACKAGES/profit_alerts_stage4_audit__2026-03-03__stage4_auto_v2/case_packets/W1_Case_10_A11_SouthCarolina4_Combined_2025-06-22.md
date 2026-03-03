# Profit Alerts Stage-4 Audit Packet — W1 Case 10

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W1 |
| Case number | 10 |
| AlertId | A11 |
| StateKey | SouthCarolina4 |
| Variant | Combined |
| Results date D | 2025-06-22 |
| Status | EXPIRED |
| Suggested | BOX |
| Canonical | 005 |
| Badges | HOT/CONS |
| RowNum (eval/board) | 80 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-22/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-22/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-22/SouthCarolina4/winners/SouthCarolina4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-22/SouthCarolina4/winners/SouthCarolina4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-22/SouthCarolina4/json/SouthCarolina4_tables.json
- Stable excerpt: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-22/SouthCarolina4/stable/SouthCarolina4/SouthCarolina4_stable_patterns_scores__profit_alerts_excerpt.csv

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | SouthCarolina4 |
| Variant | Combined |
| AlertId | A11 |
| Strength | 5 |
| Suggested | BOX |
| CapLines | 12 |
| DecayDraws | 2 |
| Badges | HOT/CONS |
| Canonical | 005 |
| ImpliedSet | ["005","050","500"] |
| Winner Midday | - |
| Winner Evening | 675 |

## Eval row (extracted)
| Field | Value |
|---|---|
| row_type | GOVERNOR |
| strict_hit (D-only) | N |
| hit_within_decay (primary) | N |
| hit_any_within_decay (diagnostic) | N |
| hit_within_7 | Y |
| hit_within_14 | Y |
| hit_type |  |
| hit_any_type |  |
| start_when | 2025-06-22 Midday |
| expiry_when | 2025-06-23 Midday |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "a11_star_score": 34.95,
  "canon_source": "stable_attach",
  "col": "1",
  "evidence_tags": "col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight",
  "stable_column": "1",
  "stable_draw": "Draw1",
  "stable_family_id": "1.0",
  "stable_scores_relpath": "SouthCarolina4/stable/SouthCarolina4/SouthCarolina4_stable_patterns_scores.csv",
  "stable_section": "Combined",
  "stable_set": "Set1",
  "stable_why": "straight|cov4|vstr2|vstr3|mirror|cons_full|hot2|dom_last|cons_3v|double_mirror|vtrac_straight",
  "star_level": 2,
  "stub_canonical": "05",
  "stub_column": "1",
  "stub_draw": "Draw1",
  "stub_section": "Combined",
  "stub_set": "Set1",
  "stub_type": "consensus_stub",
  "triad": "478"
}
```

## Stable locator + excerpt row (if applicable)
| Field | Value |
|---|---|
| stable_section | Combined |
| stable_set | Set1 |
| stable_draw | Draw1 |
| stable_column | 1 |
| stable_family_id | 1.0 |
| stable_why | straight|cov4|vstr2|vstr3|mirror|cons_full|hot2|dom_last|cons_3v|double_mirror|vtrac_straight |

| Field | Value |
|---|---|
| type | straight |
| score | 34.5 |
| rows | R2,R4,R6,R8 |
| orders_modal_value | 005 |
| orders_modal_rows | 4 |
| order dominance (computed later) |  |
| why | straight|cov4|vstr2|vstr3|mirror|cons_full|hot2|dom_last|cons_3v|double_mirror|vtrac_straight |

## JSON environment snapshot at locator (audit mirror)
| Field | Value |
|---|---|
| json_section | Combined |
| json_set | Set1 |
| json_draw | Draw1 |
| json_col | 1 |
| json_arr_len | 7 |
| json_arr_idx | 6 |
| R2 @col | 005** |
| R4 @col | 005** |
| R6 @col | 005** |
| R8 @col | 005** |
| R2 last3 | 005 |
| R4 last3 | 005 |
| R6 last3 | 005 |
| R8 last3 | 005 |

## Contract checks (auto)
| Field | Value |
|---|---|
| expected_row_type | GOVERNOR |
| eval_row_type | GOVERNOR |
| row_type_ok | Y |
| implied_set_required | Y |
| implied_set_parse_error |  |
| implied_set_size | 3 |
| box_canonical_ok | Y |
| box_family_ok | Y |
| a08_base_pointer_ok | NA |
| a11_star_fields_ok | Y |
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
