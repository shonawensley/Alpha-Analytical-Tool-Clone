# Profit Alerts Stage-4 Audit Packet — W2 Case 6

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W2 |
| Case number | 6 |
| AlertId | A06 |
| StateKey | SouthCarolina4 |
| Variant | Combined |
| Results date D | 2026-01-04 |
| Status | EXPIRED |
| Suggested | BOX |
| Canonical | 259 |
| Badges | DR/3V |
| RowNum (eval/board) | 45 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-04/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-04/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-04/SouthCarolina4/winners/SouthCarolina4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-04/SouthCarolina4/winners/SouthCarolina4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-12-30_to_2026-01-09__2026-02-22__provloc_v1/sharepacks/2026-01-04/SouthCarolina4/json/SouthCarolina4_tables.json

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | SouthCarolina4 |
| Variant | Combined |
| AlertId | A06 |
| Strength | 3 |
| Suggested | BOX |
| CapLines | 12 |
| DecayDraws | 2 |
| Badges | DR/3V |
| Canonical | 592 |
| ImpliedSet | ["259","295","529","592","925","952"] |
| Winner Midday | - |
| Winner Evening | 432 |

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
| start_when | 2026-01-04 Midday |
| expiry_when | 2026-01-05 Midday |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "best_rank": 2,
  "dr_survivor_3v": 1,
  "variants": [
    "Combined",
    "Midday"
  ]
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
| implied_set_required | N |
| implied_set_parse_error |  |
| implied_set_size | 6 |
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
