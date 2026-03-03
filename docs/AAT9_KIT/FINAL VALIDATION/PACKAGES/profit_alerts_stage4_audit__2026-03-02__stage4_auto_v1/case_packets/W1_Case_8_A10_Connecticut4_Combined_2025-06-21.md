# Profit Alerts Stage-4 Audit Packet — W1 Case 8

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W1 |
| Case number | 8 |
| AlertId | A10 |
| StateKey | Connecticut4 |
| Variant | Combined |
| Results date D | 2025-06-21 |
| Status | EXPIRED |
| Suggested | STR8_3 |
| Canonical | 225 |
| Badges | DBL/RANK1 |
| RowNum (eval/board) | 73 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/Connecticut4/winners/Connecticut4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/Connecticut4/json/Connecticut4_tables.json

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | Connecticut4 |
| Variant | Combined |
| AlertId | A10 |
| Strength | 4 |
| Suggested | STR8_3 |
| CapLines | 3 |
| DecayDraws | 3 |
| Badges | DBL/RANK1 |
| Canonical | 225 |
| ImpliedSet | ["225","252","522"] |
| Winner Midday | 950 |
| Winner Evening | 155 |

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
| start_when | 2025-06-21 Midday |
| expiry_when | 2025-06-22 Midday |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "due_doubles_canonical": "225",
  "due_doubles_family": "0/5-2/7",
  "due_doubles_gap": 1000,
  "due_doubles_rank": 1,
  "due_doubles_unseen": true
}
```

## Stable locator + excerpt row (if applicable)
- No stable locator for this case (expected for some alerts, e.g., promoters / lane-only signals).

## JSON environment snapshot at locator (audit mirror)
- No JSON snapshot extracted (no locator available or json file missing).

## Contract checks (auto)
| Field | Value |
|---|---|
| expected_row_type | CANDIDATE |
| eval_row_type | CANDIDATE |
| row_type_ok | Y |
| implied_set_required | Y |
| implied_set_parse_error |  |
| implied_set_size | 3 |
| stable_locator_present | N |
| stable_excerpt_row_found | NA |
| json_snapshot_ok | NA |

## Audit questions (yes/no)
1) Does the Stable excerpt row exist at the locator and match Evidence fields?
2) Does the JSON environment at that locator ‘look consistent’ with the alert’s intended meaning?

## Notes / overrides (human / Deep Research)
- HumanVerdict: (PASS/FAIL/AMBIG)  
- HumanNotes:  
- ProposedFix (if FAIL):
