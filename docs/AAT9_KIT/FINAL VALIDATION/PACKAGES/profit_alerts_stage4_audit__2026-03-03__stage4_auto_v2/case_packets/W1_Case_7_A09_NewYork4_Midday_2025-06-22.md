# Profit Alerts Stage-4 Audit Packet — W1 Case 7

## Case metadata
| Field | Value |
|---|---|
| Evidence pack key | W1 |
| Case number | 7 |
| AlertId | A09 |
| StateKey | NewYork4 |
| Variant | Midday |
| Results date D | 2025-06-22 |
| Status | EXPIRED |
| Suggested | STR8_8 |
| Canonical |  |
| Badges | VTRAC/REP |
| RowNum (eval/board) | 68 |
| AutoVerdict | PASS |
| FailReasons |  |

## Files to open (portable)
- Board CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-22/control_center/profit_alerts.csv
- Eval CSV: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-22/control_center/profit_alerts_eval.csv
- Winners digest: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-22/NewYork4/winners/NewYork4/digest.md
- Winners dir: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-22/NewYork4/winners/NewYork4
- JSON tables: docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_evidence_pack__2025-06-21_to_2025-06-23__2026-03-03__provloc_v2/sharepacks/2025-06-22/NewYork4/json/NewYork4_tables.json

## Board row (extracted)
| Field | Value |
|---|---|
| StateKey | NewYork4 |
| Variant | Midday |
| AlertId | A09 |
| Strength | 4 |
| Suggested | STR8_8 |
| CapLines | 8 |
| DecayDraws | 1 |
| Badges | VTRAC/REP |
| Canonical | - |
| ImpliedSet | ["023","028","073","078","523","528","573","578"] |
| Winner Midday | 202 |
| Winner Evening | 968 |

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
| start_when | 2025-06-22 Midday |
| expiry_when | 2025-06-22 Midday |
| hit_when |  |
| time_to_hit_steps |  |

## Evidence JSON (pretty)
```json
{
  "current_index": 11,
  "current_streak": 2,
  "lane_size": 8,
  "vcode": "v134",
  "vtrac_index": 11
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
| implied_set_size | 8 |
| box_canonical_ok | NA |
| box_family_ok | NA |
| a08_base_pointer_ok | NA |
| a11_star_fields_ok | NA |
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
