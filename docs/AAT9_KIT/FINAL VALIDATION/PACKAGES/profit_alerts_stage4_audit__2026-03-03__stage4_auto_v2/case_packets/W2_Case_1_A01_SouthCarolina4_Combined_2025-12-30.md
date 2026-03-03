# Profit Alerts Stage-4 Audit Packet — W2 Case 1

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W2 |
| Case number | 1 |
| AlertId | A01 |
| StateKey | SouthCarolina4 |
| Variant | Combined |
| Results date D | 2025-12-30 |
| Status | EXPIRED |
| Suggested | BOX |
| Canonical | 019 |
| Badges | CONS/3V/BA |
| RowNum (eval/board) | 4 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-30/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-30/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-30/SouthCarolina4/winners/SouthCarolina4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-30/SouthCarolina4/winners/SouthCarolina4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-30/SouthCarolina4/json/SouthCarolina4_tables.json
- Stable excerpt: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-03-03__provloc_v2/sharepacks/2025-12-30/SouthCarolina4/stable/SouthCarolina4/SouthCarolina4_stable_patterns_scores__profit_alerts_excerpt.csv

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | SouthCarolina4 |
| Variant | Combined |
| AlertId | A01 |
| Strength | 4 |
| Suggested | BOX |
| CapLines | 12 |
| DecayDraws | 3 |
| Badges | CONS/3V/BA |
| Canonical | 019 |
| ImpliedSet | ["019","091","109","190","901","910"] |
| Winner Midday | 754 |
| Winner Evening | 976 |

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
| start_when | 2025-12-30 Midday |
| expiry_when | 2025-12-31 Midday |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "ba_score": 2,
  "col": "1",
  "perm": 2,
  "rowcov": 4,
  "stable_column": "1",
  "stable_draw": "Draw1",
  "stable_family_id": "9.0",
  "stable_scores_relpath": "SouthCarolina4/stable/SouthCarolina4/SouthCarolina4_stable_patterns_scores.csv",
  "stable_section": "Combined",
  "stable_set": "Set2",
  "stable_why": "boxed|cov4|hp_repeat2|vstr2|hot1|dom_last|perm2|hidden3v|set_chain3",
  "stub_canonical": "09",
  "stub_column": "1",
  "stub_draw": "Draw1",
  "stub_section": "Combined",
  "stub_set": "Set3",
  "stub_type": "consensus_stub",
  "tail": "09"
}
```

## Stable locator + excerpt row (if applicable)
| Field | Value |
|---|---|
| stable_section | Combined |
| stable_set | Set2 |
| stable_draw | Draw1 |
| stable_column | 1 |
| stable_family_id | 9.0 |
| stable_why | boxed|cov4|hp_repeat2|vstr2|hot1|dom_last|perm2|hidden3v|set_chain3 |

| Field | Value |
|---|---|
| type | boxed |
| score | 23.5 |
| rows | R2,R4,R6,R8 |
| orders_modal_value | 091 |
| orders_modal_rows | 2 |
| order dominance (computed later) |  |
| why | boxed|cov4|hp_repeat2|vstr2|hot1|dom_last|perm2|hidden3v|set_chain3 |

## JSON environment snapshot at locator (audit mirror)
| Field | Value |
|---|---|
| json_section | Combined |
| json_set | Set2 |
| json_draw | Draw1 |
| json_col | 1 |
| json_arr_len | 7 |
| json_arr_idx | 6 |
| R2 @col | 091* |
| R4 @col | 091* |
| R6 @col | 019* |
| R8 @col | 019* |
| R2 last3 | 091 |
| R4 last3 | 091 |
| R6 last3 | 019 |
| R8 last3 | 019 |

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
