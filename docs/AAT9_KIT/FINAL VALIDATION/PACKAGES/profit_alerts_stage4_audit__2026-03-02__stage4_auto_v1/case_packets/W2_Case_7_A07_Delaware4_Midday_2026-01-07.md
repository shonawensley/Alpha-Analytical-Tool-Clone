# Profit Alerts Stage-4 Audit Packet — W2 Case 7

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W2 |
| Case number | 7 |
| AlertId | A07 |
| StateKey | Delaware4 |
| Variant | Midday |
| Results date D | 2026-01-07 |
| Status | EXPIRED |
| Suggested | BOX |
| Canonical | 035 |
| Badges | BA/MIRROR |
| RowNum (eval/board) | 45 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-07/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-07/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-07/Delaware4/winners/Delaware4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-07/Delaware4/winners/Delaware4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-07/Delaware4/json/Delaware4_tables.json
- Stable excerpt: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-07/Delaware4/stable/Delaware4/Delaware4_stable_patterns_scores__profit_alerts_excerpt.csv

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | Delaware4 |
| Variant | Midday |
| AlertId | A07 |
| Strength | 4 |
| Suggested | BOX |
| CapLines | 12 |
| DecayDraws | 2 |
| Badges | BA/MIRROR |
| Canonical | 035 |
| ImpliedSet | ["035","053","305","350","503","530"] |
| Winner Midday | 657 |
| Winner Evening | 922 |

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
| start_when | 2026-01-07 Midday |
| expiry_when | 2026-01-08 Midday |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "ba_mirror_latest": 1,
  "col": "2",
  "last_draw": "758",
  "mirror_tail": "03",
  "stable_column": "2",
  "stable_draw": "Draw4",
  "stable_family_id": "4.0",
  "stable_scores_relpath": "Delaware4/stable/Delaware4/Delaware4_stable_patterns_scores.csv",
  "stable_section": "Midday",
  "stable_set": "Set1",
  "stable_why": "boxed|cov2|mirror|hot2|perm2|set_chain2",
  "stub_canonical": "03",
  "stub_column": "2",
  "stub_draw": "Draw1",
  "stub_section": "Midday",
  "stub_set": "Set1",
  "stub_type": "consensus_stub",
  "tail": "03"
}
```

## Stable locator + excerpt row (if applicable)
| Field | Value |
|---|---|
| stable_section | Midday |
| stable_set | Set1 |
| stable_draw | Draw4 |
| stable_column | 2 |
| stable_family_id | 4.0 |
| stable_why | boxed|cov2|mirror|hot2|perm2|set_chain2 |

| Field | Value |
|---|---|
| type | boxed |
| score | 12.0 |
| rows | R2,R6 |
| orders_modal_value | 503 |
| orders_modal_rows | 1 |
| order dominance (computed later) |  |
| why | boxed|cov2|mirror|hot2|perm2|set_chain2 |

## JSON environment snapshot at locator (audit mirror)
| Field | Value |
|---|---|
| json_section | Midday |
| json_set | Set1 |
| json_draw | Draw4 |
| json_col | 2 |
| json_arr_len | 7 |
| json_arr_idx | 5 |
| R2 @col | 503386** |
| R4 @col | 506833** |
| R6 @col | 680533** |
| R8 @col | 083365** |
| R2 last3 | 386 |
| R4 last3 | 833 |
| R6 last3 | 533 |
| R8 last3 | 365 |

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
