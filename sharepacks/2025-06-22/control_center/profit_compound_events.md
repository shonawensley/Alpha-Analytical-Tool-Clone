# Profit Compound Events — 2025-06-22

This is a **shadow-only** triage board derived from Profit Alerts.
It flags “watchlist” compound co-fire environments defined in:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Compound_Events_Watchlist.md`

## Counts
| Field | Value |
|---|---|
| Tagged rows | 16 |
| Unique tags | 8 |

## Tag counts

| Tag | Count | Weight |
|---|---|---|
| ENGINE_GOV | 7 | 85 |
| CARRY_PERM | 6 | 70 |
| CLAMP_4 | 5 | 25 |
| CLAMP_ANY | 5 | 20 |
| STRAIGHT_GATE | 4 | 80 |
| DBL_BA | 3 | 45 |
| CARRY_PERM_GOV | 2 | 75 |
| CARRY_PERM_HARDLOCK | 1 | 95 |

## Rows (sorted)

| Priority | StateKey | Variant | TopEvent | Tags | A11★ | A12 sizes | MinSet | MinCap | MergedHit |
|---|---|---|---|---|---|---|---|---|---|
| 95 | Pennsylvania4 | Combined | CARRY_PERM_HARDLOCK | CARRY_PERM_HARDLOCK|ENGINE_GOV|STRAIGHT_GATE|CARRY_PERM_GOV|CARRY_PERM | 2 |  | 3 | 3 | N |
| 85 | Indiana4 | Combined | ENGINE_GOV | ENGINE_GOV | 2 |  | 3 | 12 | N |
| 85 | Michigan4 | Combined | ENGINE_GOV | ENGINE_GOV | 2 |  | 3 | 8 | Y |
| 85 | NewJersey4 | Combined | ENGINE_GOV | ENGINE_GOV|STRAIGHT_GATE|CARRY_PERM_GOV|CARRY_PERM | 2 |  | 3 | 3 | N |
| 85 | Ohio4 | Combined | ENGINE_GOV | ENGINE_GOV|STRAIGHT_GATE|CLAMP_4|CLAMP_ANY | 2 | 4 | 3 | 5 | N |
| 85 | SouthCarolina4 | Combined | ENGINE_GOV | ENGINE_GOV | 2 |  | 3 | 12 | N |
| 85 | PuertoRico4 | Combined | ENGINE_GOV | ENGINE_GOV | 2 |  | 6 | 12 | N |
| 80 | NewYork4 | Combined | STRAIGHT_GATE | STRAIGHT_GATE|DBL_BA | 2 |  | 3 | 0 | N |
| 70 | Delaware4 | Midday | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 70 | Florida4 | Evening | CARRY_PERM | CARRY_PERM |  |  | 3 | 0 | N |
| 70 | Ohio4 | Midday | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 70 | Virginia4 | Combined | CARRY_PERM | CARRY_PERM|CLAMP_4|CLAMP_ANY |  | 4 | 3 | 0 | N |
| 45 | NewYork4 | Evening | DBL_BA | DBL_BA|CLAMP_4|CLAMP_ANY |  | 4 | 3 | 0 | N |
| 45 | Virginia4 | Evening | DBL_BA | DBL_BA |  |  | 3 | 0 | N |
| 25 | Delaware4 | Evening | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 5 | N |
| 25 | NorthCarolina4 | Evening | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 5 | N |

## Regenerate
```bash
python3 scripts/tools/export_profit_compound_events.py --date 2025-06-22
```
