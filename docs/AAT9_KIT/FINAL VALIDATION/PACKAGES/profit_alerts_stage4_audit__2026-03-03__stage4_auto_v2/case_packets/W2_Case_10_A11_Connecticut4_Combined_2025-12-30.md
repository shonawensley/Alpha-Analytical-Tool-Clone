# Profit Alerts Stage-4 Audit Packet — W2 Case 10

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W2 |
| Case number | 10 |
| AlertId | A11 |
| StateKey | Connecticut4 |
| Variant | Combined |
| Results date D | 2025-12-30 |
| Status | EXPIRED |
| Suggested | BOX |
| Canonical | 005 |
| Badges | HOT/CONS |
| RowNum (eval/board) | 64 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-30/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-30/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-30/Connecticut4/winners/Connecticut4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-30/Connecticut4/winners/Connecticut4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-30/Connecticut4/json/Connecticut4_tables.json
- Stable excerpt: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-30/Connecticut4/stable/Connecticut4/Connecticut4_stable_patterns_scores__profit_alerts_excerpt.csv

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | Connecticut4 |
| Variant | Combined |
| AlertId | A11 |
| Strength | 5 |
| Suggested | BOX |
| CapLines | 12 |
| DecayDraws | 2 |
| Badges | HOT/CONS |
| Canonical | 005 |
| ImpliedSet | ["005","050","500"] |
| Winner Midday | 095 |
| Winner Evening | 467 |

## Eval row (extracted)
| Field | Value |
|---|---|
| row_type | GOVERNOR |
| strict_hit (D-only) | N |
| hit_within_decay (primary) | N |
| hit_any_within_decay (diagnostic) | N |
| hit_within_7 | N |
| hit_within_14 | N |
| hit_type |  |
| hit_any_type |  |
| start_when | 2025-12-30 Midday |
| expiry_when | 2025-12-30 Evening |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "a11_star_score": 35.95,
  "canon_source": "stable_attach",
  "col": "1",
  "evidence_tags": "col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight",
  "stable_column": "1",
  "stable_draw": "Draw1",
  "stable_family_id": "1.0",
  "stable_scores_relpath": "Connecticut4/stable/Connecticut4/Connecticut4_stable_patterns_scores.csv",
  "stable_section": "Combined",
  "stable_set": "Set3",
  "stable_why": "straight|cov4|hp_repeat4|vstr2|vstr3|mirror|cons_full|hot1|dom_last|cons_3v|double_mirror|vtrac_straight|set_chain3",
  "star_level": 2,
  "stub_canonical": "06",
  "stub_column": "1",
  "stub_draw": "Draw1",
  "stub_section": "Combined",
  "stub_set": "Set1",
  "stub_type": "consensus_stub",
  "triad": "112"
}
```

## Stable locator + excerpt row (if applicable)
| Field | Value |
|---|---|
| stable_section | Combined |
| stable_set | Set3 |
| stable_draw | Draw1 |
| stable_column | 1 |
| stable_family_id | 1.0 |
| stable_why | straight|cov4|hp_repeat4|vstr2|vstr3|mirror|cons_full|hot1|dom_last|cons_3v|double_mirror|vtrac_straight|set_chain3 |

| Field | Value |
|---|---|
| type | straight |
| score | 39.5 |
| rows | R2,R4,R6,R8 |
| orders_modal_value | 005 |
| orders_modal_rows | 4 |
| order dominance (computed later) |  |
| why | straight|cov4|hp_repeat4|vstr2|vstr3|mirror|cons_full|hot1|dom_last|cons_3v|double_mirror|vtrac_straight|set_chain3 |

## JSON environment snapshot at locator (audit mirror)
| Field | Value |
|---|---|
| json_section | Combined |
| json_set | Set3 |
| json_draw | Draw1 |
| json_col | 1 |
| json_arr_len | 7 |
| json_arr_idx | 6 |
| R2 @col | 005* |
| R4 @col | 005* |
| R6 @col | 005* |
| R8 @col | 005* |
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
