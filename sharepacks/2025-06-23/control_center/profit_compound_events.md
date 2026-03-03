# Profit Compound Events — 2025-06-23

This is a **shadow-only** triage board derived from Profit Alerts.
It flags “watchlist” compound co-fire environments defined in:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Compound_Events_Watchlist.md`

## Counts
| Field | Value |
|---|---|
| Tagged rows | 16 |
| Unique tags | 6 |

## Tag counts

| Tag | Count | Weight |
|---|---|---|
| CARRY_PERM | 7 | 70 |
| CLAMP_4 | 5 | 25 |
| CLAMP_ANY | 5 | 20 |
| ENGINE_GOV | 3 | 85 |
| DBL_BA | 3 | 45 |
| STRAIGHT_GATE | 1 | 80 |

## Rows (sorted)

| Priority | StateKey | Variant | TopEvent | Tags | A11★ | A12 sizes | MinSet | MinCap | MergedHit |
|---|---|---|---|---|---|---|---|---|---|
| 85 | Pennsylvania4 | Combined | ENGINE_GOV | ENGINE_GOV | 2 |  | 3 | 0 | N |
| 85 | SouthCarolina4 | Combined | ENGINE_GOV | ENGINE_GOV | 2 |  | 3 | 3 | N |
| 85 | PuertoRico4 | Combined | ENGINE_GOV | ENGINE_GOV | 2 |  | 6 | 12 | N |
| 80 | Ohio4 | Combined | STRAIGHT_GATE | STRAIGHT_GATE|CLAMP_4|CLAMP_ANY | 2 | 4 | 3 | 5 | N |
| 70 | Connecticut4 | Evening | CARRY_PERM | CARRY_PERM|CLAMP_4|CLAMP_ANY |  | 4 | 3 | 0 | N |
| 70 | Delaware4 | Midday | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 70 | Florida4 | Evening | CARRY_PERM | CARRY_PERM |  |  | 3 | 0 | N |
| 70 | NorthCarolina4 | Midday | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 70 | Ohio4 | Midday | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 70 | Pennsylvania4 | Evening | CARRY_PERM | CARRY_PERM |  |  | 3 | 0 | N |
| 70 | Indiana4 | Evening | CARRY_PERM | CARRY_PERM |  |  | 6 | 8 | N |
| 45 | Connecticut4 | Combined | DBL_BA | DBL_BA | 2 |  | 3 | 0 | N |
| 45 | Pennsylvania4 | Midday | DBL_BA | DBL_BA |  |  | 3 | 0 | N |
| 45 | Virginia4 | Evening | DBL_BA | DBL_BA|CLAMP_4|CLAMP_ANY |  | 4 | 3 | 0 | N |
| 25 | NorthCarolina4 | Combined | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 3 | 3 | N |
| 25 | Delaware4 | Evening | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 0 | N |

## Regenerate
```bash
python3 scripts/tools/export_profit_compound_events.py --date 2025-06-23
```
