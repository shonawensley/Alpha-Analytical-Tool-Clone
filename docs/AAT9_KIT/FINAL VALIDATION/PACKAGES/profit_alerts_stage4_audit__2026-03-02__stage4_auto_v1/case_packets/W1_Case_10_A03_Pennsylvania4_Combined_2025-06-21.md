# Profit Alerts Stage-4 Audit Packet — W1 Case 10

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W1 |
| Case number | 10 |
| AlertId | A03 |
| StateKey | Pennsylvania4 |
| Variant | Combined |
| Results date D | 2025-06-21 |
| Status | PROMOTER |
| Suggested | OVERLAY |
| Canonical |  |
| Badges | CONS/XVAR |
| RowNum (eval/board) | 26 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-02-22__provloc_v1/sharepacks/2025-06-21/Pennsylvania4/json/Pennsylvania4_tables.json

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | Pennsylvania4 |
| Variant | Combined |
| AlertId | A03 |
| Strength | 3 |
| Suggested | OVERLAY |
| CapLines | 8 |
| DecayDraws | 2 |
| Badges | CONS/XVAR |
| Canonical | - |
| ImpliedSet |  |
| Winner Midday | 667 |
| Winner Evening | 360 |

## Eval row (extracted)
| Field | Value |
|---|---|
| row_type | PROMOTER |
| strict_hit (D-only) | NA |
| hit_within_decay (primary) | NA |
| hit_any_within_decay (diagnostic) | NA |
| hit_within_7 | NA |
| hit_within_14 | NA |
| hit_type |  |
| hit_any_type |  |
| start_when | 2025-06-21 Midday |
| expiry_when | 2025-06-21 Evening |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "col": "1",
  "cons_cross_sections": 2,
  "sections": [
    "Combined",
    "Evening"
  ],
  "stub_locators": [
    {
      "stub_canonical": "03",
      "stub_column": "1",
      "stub_draw": "Draw2",
      "stub_section": "Combined",
      "stub_set": "Set1",
      "stub_type": "consensus_stub"
    },
    {
      "stub_canonical": "03",
      "stub_column": "1",
      "stub_draw": "Draw1",
      "stub_section": "Evening",
      "stub_set": "Set1",
      "stub_type": "consensus_stub"
    }
  ],
  "tail": "03"
}
```

## Stable locator + excerpt row (if applicable)
- No stable locator for this case (expected for some alerts, e.g., promoters / lane-only signals).

## JSON environment snapshot at locator (audit mirror)
- No JSON snapshot extracted (no locator available or json file missing).

## Contract checks (auto)
| Field | Value |
|---|---|
| expected_row_type | PROMOTER |
| eval_row_type | PROMOTER |
| row_type_ok | Y |
| implied_set_required | N |
| implied_set_parse_error |  |
| implied_set_size | 0 |
| stable_locator_present | N |
| stable_excerpt_row_found | NA |
| json_snapshot_ok | NA |

## Audit questions (yes/no)
1) Is this row typed as PROMOTER and not graded like a candidate?
2) Does the Evidence JSON contain enough context to understand what it is promoting?

## Notes / overrides (human / Deep Research)
- HumanVerdict: (PASS/FAIL/AMBIG)  
- HumanNotes:  
- ProposedFix (if FAIL):
