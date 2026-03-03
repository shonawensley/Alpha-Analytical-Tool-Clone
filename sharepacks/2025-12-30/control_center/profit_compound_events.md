# Profit Compound Events — 2025-12-30

This is a **shadow-only** triage board derived from Profit Alerts.
It flags “watchlist” compound co-fire environments defined in:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Compound_Events_Watchlist.md`

## Counts
| Field | Value |
|---|---|
| Tagged rows | 13 |
| Unique tags | 7 |

## Tag counts

| Tag | Count | Weight |
|---|---|---|
| CLAMP_4 | 5 | 25 |
| CLAMP_ANY | 5 | 20 |
| CARRY_PERM | 4 | 70 |
| STRAIGHT_GATE | 3 | 80 |
| DBL_BA | 3 | 45 |
| ENGINE_GOV | 2 | 85 |
| CARRY_PERM_GOV | 1 | 75 |

## Rows (sorted)

| Priority | StateKey | Variant | TopEvent | Tags | A11★ | A12 sizes | MinSet | MinCap | MergedHit |
|---|---|---|---|---|---|---|---|---|---|
| 85 | Connecticut4 | Combined | ENGINE_GOV | ENGINE_GOV | 2 |  | 3 | 0 | N |
| 85 | SouthCarolina4 | Combined | ENGINE_GOV | ENGINE_GOV|STRAIGHT_GATE|CARRY_PERM_GOV|CARRY_PERM | 2 |  | 3 | 3 | N |
| 80 | NewJersey4 | Combined | STRAIGHT_GATE | STRAIGHT_GATE | 2 |  | 3 | 3 | N |
| 80 | NorthCarolina4 | Combined | STRAIGHT_GATE | STRAIGHT_GATE | 2 |  | 3 | 3 | N |
| 70 | Connecticut4 | Evening | CARRY_PERM | CARRY_PERM|DBL_BA|CLAMP_4|CLAMP_ANY |  | 4 | 3 | 0 | N |
| 70 | Indiana4 | Combined | CARRY_PERM | CARRY_PERM |  |  | 3 | 0 | N |
| 70 | Virginia4 | Evening | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 45 | OntarioCanada4 | Midday | DBL_BA | DBL_BA |  |  | 3 | 0 | N |
| 45 | PuertoRico4 | Evening | DBL_BA | DBL_BA |  |  | 3 | 0 | N |
| 25 | Delaware4 | Evening | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 3 | 0 | N |
| 25 | PuertoRico4 | Midday | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 3 | 3 | N |
| 25 | Pennsylvania4 | Evening | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 5 | N |
| 25 | Virginia4 | Midday | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 0 | N |

## Regenerate
```bash
python3 scripts/tools/export_profit_compound_events.py --date 2025-12-30
```
