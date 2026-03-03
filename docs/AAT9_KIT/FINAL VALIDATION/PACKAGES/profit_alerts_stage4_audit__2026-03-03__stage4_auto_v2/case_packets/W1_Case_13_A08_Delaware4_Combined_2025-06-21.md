# Profit Alerts Stage-4 Audit Packet — W1 Case 13

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W1 |
| Case number | 13 |
| AlertId | A08 |
| StateKey | Delaware4 |
| Variant | Combined |
| Results date D | 2025-06-21 |
| Status | PROMOTER |
| Suggested | OVERLAY |
| Canonical |  |
| Badges | BA/TEMPO |
| RowNum (eval/board) | 55 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-21/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-21/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-21/Delaware4/winners/Delaware4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-21/Delaware4/winners/Delaware4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-21/Delaware4/json/Delaware4_tables.json

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | Delaware4 |
| Variant | Combined |
| AlertId | A08 |
| Strength | 4 |
| Suggested | OVERLAY |
| CapLines | 0 |
| DecayDraws | 2 |
| Badges | BA/TEMPO |
| Canonical | - |
| ImpliedSet |  |
| Winner Midday | 756 |
| Winner Evening | 989 |

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
  "ba_score": 4,
  "base_candidate_present": 1,
  "base_candidates": [
    {
      "alert_id": "A04",
      "canonical": "368",
      "variant": "Combined"
    }
  ],
  "pairs_remaining": 0,
  "promoter_only": 1,
  "requires_base_box": 1
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
| box_canonical_ok | NA |
| box_family_ok | NA |
| a08_base_pointer_ok | Y |
| a11_star_fields_ok | NA |
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
