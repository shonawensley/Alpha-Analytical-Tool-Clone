# Profit Compound Events — 2025-12-31

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
| CLAMP_4 | 7 | 25 |
| CLAMP_ANY | 7 | 20 |
| CARRY_PERM | 5 | 70 |
| DBL_BA | 2 | 45 |
| ENGINE_GOV | 1 | 85 |
| IDX_ECHO_CLAMP | 1 | 65 |
| IDX_ECHO_BASE | 1 | 60 |

## Rows (sorted)

| Priority | StateKey | Variant | TopEvent | Tags | A11★ | A12 sizes | MinSet | MinCap | MergedHit |
|---|---|---|---|---|---|---|---|---|---|
| 85 | Connecticut4 | Combined | ENGINE_GOV | ENGINE_GOV | 2 |  | 3 | 12 | N |
| 70 | NewJersey4 | Combined | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 70 | NewYork4 | Midday | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 70 | NorthCarolina4 | Combined | CARRY_PERM | CARRY_PERM |  |  | 3 | 0 | N |
| 70 | Ohio4 | Midday | CARRY_PERM | CARRY_PERM|DBL_BA |  |  | 3 | 0 | N |
| 70 | SouthCarolina4 | Midday | CARRY_PERM | CARRY_PERM|IDX_ECHO_CLAMP|IDX_ECHO_BASE|CLAMP_4|CLAMP_ANY |  | 4 | 3 | 0 | N |
| 45 | OntarioCanada4 | Midday | DBL_BA | DBL_BA |  |  | 3 | 0 | N |
| 25 | Connecticut4 | Evening | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 3 | 3 | N |
| 25 | Michigan4 | Evening | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 3 | 0 | N |
| 25 | PuertoRico4 | Midday | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 3 | 3 | N |
| 25 | Indiana4 | Combined | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 0 | N |
| 25 | NewYork4 | Combined | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 5 | N |
| 25 | Virginia4 | Midday | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 0 | N |

## Regenerate
```bash
python3 scripts/tools/export_profit_compound_events.py --date 2025-12-31
```
