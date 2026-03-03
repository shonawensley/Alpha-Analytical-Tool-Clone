# Profit Alerts Stage-4 Audit Packet — W2 Case 2

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W2 |
| Case number | 2 |
| AlertId | A02 |
| StateKey | OntarioCanada4 |
| Variant | Midday |
| Results date D | 2026-01-02 |
| Status | EXPIRED |
| Suggested | STR8_3 |
| Canonical | 022 |
| Badges | CONS/DBL/A10 |
| RowNum (eval/board) | 5 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-02/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-02/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-02/OntarioCanada4/winners/OntarioCanada4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-02/OntarioCanada4/json/OntarioCanada4_tables.json
- Stable excerpt: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-02/OntarioCanada4/stable/OntarioCanada4/OntarioCanada4_stable_patterns_scores__profit_alerts_excerpt.csv

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | OntarioCanada4 |
| Variant | Midday |
| AlertId | A02 |
| Strength | 4 |
| Suggested | STR8_3 |
| CapLines | 6 |
| DecayDraws | 2 |
| Badges | CONS/DBL/A10 |
| Canonical | 022 |
| ImpliedSet | ["022","202","220"] |
| Winner Midday | 053 |
| Winner Evening | 816 |

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
| start_when | 2026-01-02 Midday |
| expiry_when | 2026-01-03 Midday |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "ba_score": 0,
  "col": "1",
  "due_doubles_rank": 2,
  "perm": 1,
  "rowcov": 4,
  "stable_column": "1",
  "stable_draw": "Draw1",
  "stable_family_id": "10.0",
  "stable_scores_relpath": "OntarioCanada4/stable/OntarioCanada4/OntarioCanada4_stable_patterns_scores.csv",
  "stable_section": "Midday",
  "stable_set": "Set3",
  "stable_why": "straight|cov4|hp_repeat2|vstr2|vstr3|cons_full|hot1|dom_last|cons_3v|hidden3v|double_mirror|vtrac_straight|set_chain3",
  "stub_canonical": "22",
  "stub_column": "1",
  "stub_draw": "Draw1",
  "stub_section": "Midday",
  "stub_set": "Set2",
  "stub_type": "consensus_stub",
  "tail": "22"
}
```

## Stable locator + excerpt row (if applicable)
| Field | Value |
|---|---|
| stable_section | Midday |
| stable_set | Set3 |
| stable_draw | Draw1 |
| stable_column | 1 |
| stable_family_id | 10.0 |
| stable_why | straight|cov4|hp_repeat2|vstr2|vstr3|cons_full|hot1|dom_last|cons_3v|hidden3v|double_mirror|vtrac_straight|set_chain3 |

| Field | Value |
|---|---|
| type | straight |
| score | 37.0 |
| rows | R2,R4,R6,R8 |
| orders_modal_value | 022 |
| orders_modal_rows | 4 |
| order dominance (computed later) |  |
| why | straight|cov4|hp_repeat2|vstr2|vstr3|cons_full|hot1|dom_last|cons_3v|hidden3v|double_mirror|vtrac_straight|set_chain3 |

## JSON environment snapshot at locator (audit mirror)
| Field | Value |
|---|---|
| json_section | Midday |
| json_set | Set3 |
| json_draw | Draw1 |
| json_col | 1 |
| json_arr_len | 7 |
| json_arr_idx | 6 |
| R2 @col | 022* |
| R4 @col | 022* |
| R6 @col | 022* |
| R8 @col | 022* |
| R2 last3 | 022 |
| R4 last3 | 022 |
| R6 last3 | 022 |
| R8 last3 | 022 |

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
