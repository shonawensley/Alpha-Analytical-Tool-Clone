# Profit Compound Events — 2026-01-04

This is a **shadow-only** triage board derived from Profit Alerts.
It flags “watchlist” compound co-fire environments defined in:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Compound_Events_Watchlist.md`

## Counts
| Field | Value |
|---|---|
| Tagged rows | 8 |
| Unique tags | 8 |

## Tag counts

| Tag | Count | Weight |
|---|---|---|
| CLAMP_4 | 4 | 25 |
| CLAMP_ANY | 4 | 20 |
| ENGINE_GOV | 3 | 85 |
| CARRY_PERM | 2 | 70 |
| STRAIGHT_GATE | 1 | 80 |
| CARRY_PERM_GOV | 1 | 75 |
| IDX_ECHO_BASE | 1 | 60 |
| XVAR_IDX_ECHO | 1 | 55 |

## Rows (sorted)

| Priority | StateKey | Variant | TopEvent | Tags | A11★ | A12 sizes | MinSet | MinCap | MergedHit |
|---|---|---|---|---|---|---|---|---|---|
| 85 | Delaware4 | Combined | ENGINE_GOV | ENGINE_GOV|IDX_ECHO_BASE|XVAR_IDX_ECHO | 2 |  | 3 | 8 | N |
| 85 | Michigan4 | Combined | ENGINE_GOV | ENGINE_GOV|STRAIGHT_GATE|CARRY_PERM_GOV|CARRY_PERM | 2 |  | 3 | 0 | N |
| 85 | OntarioCanada4 | Combined | ENGINE_GOV | ENGINE_GOV | 2 |  | 3 | 3 | N |
| 70 | Ohio4 | Combined | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 25 | Pennsylvania4 | Combined | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 3 | 3 | N |
| 25 | SouthCarolina4 | Midday | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 3 | 0 | N |
| 25 | Connecticut4 | Combined | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 5 | N |
| 25 | Michigan4 | Midday | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 5 | N |

## Regenerate
```bash
python3 scripts/tools/export_profit_compound_events.py --date 2026-01-04
```
