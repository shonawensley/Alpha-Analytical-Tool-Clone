# Profit Compound Events — 2025-06-21

This is a **shadow-only** triage board derived from Profit Alerts.
It flags “watchlist” compound co-fire environments defined in:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Compound_Events_Watchlist.md`

## Counts
| Field | Value |
|---|---|
| Tagged rows | 14 |
| Unique tags | 8 |

## Tag counts

| Tag | Count | Weight |
|---|---|---|
| CLAMP_4 | 5 | 25 |
| CLAMP_ANY | 5 | 20 |
| ENGINE_GOV | 4 | 85 |
| DBL_BA | 4 | 45 |
| STRAIGHT_GATE | 3 | 80 |
| CARRY_PERM | 3 | 70 |
| CARRY_PERM_HARDLOCK | 1 | 95 |
| CARRY_PERM_GOV | 1 | 75 |

## Rows (sorted)

| Priority | StateKey | Variant | TopEvent | Tags | A11★ | A12 sizes | MinSet | MinCap | MergedHit |
|---|---|---|---|---|---|---|---|---|---|
| 95 | Pennsylvania4 | Combined | CARRY_PERM_HARDLOCK | CARRY_PERM_HARDLOCK|ENGINE_GOV|STRAIGHT_GATE|CARRY_PERM_GOV|CARRY_PERM | 2 |  | 3 | 3 | N |
| 85 | Indiana4 | Combined | ENGINE_GOV | ENGINE_GOV|STRAIGHT_GATE | 2 |  | 3 | 3 | N |
| 85 | NewYork4 | Combined | ENGINE_GOV | ENGINE_GOV|STRAIGHT_GATE|DBL_BA | 2 |  | 3 | 0 | N |
| 85 | OntarioCanada4 | Combined | ENGINE_GOV | ENGINE_GOV | 2 |  | 3 | 6 | N |
| 70 | OntarioCanada4 | Evening | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 70 | Virginia4 | Midday | CARRY_PERM | CARRY_PERM |  |  | 3 | 0 | N |
| 45 | Delaware4 | Midday | DBL_BA | DBL_BA |  |  | 3 | 0 | N |
| 45 | NewYork4 | Evening | DBL_BA | DBL_BA |  |  | 3 | 0 | N |
| 45 | Virginia4 | Evening | DBL_BA | DBL_BA |  |  | 3 | 0 | N |
| 25 | Florida4 | Midday | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 3 | 5 | Y |
| 25 | Indiana4 | Midday | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 3 | 5 | N |
| 25 | NewYork4 | Midday | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 3 | 5 | N |
| 25 | Connecticut4 | Midday | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 0 | N |
| 25 | Virginia4 | Combined | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 0 | N |

## Regenerate
```bash
python3 scripts/tools/export_profit_compound_events.py --date 2025-06-21
```
