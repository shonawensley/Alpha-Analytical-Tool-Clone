# Profit Compound Events — 2026-01-02

This is a **shadow-only** triage board derived from Profit Alerts.
It flags “watchlist” compound co-fire environments defined in:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Compound_Events_Watchlist.md`

## Counts
| Field | Value |
|---|---|
| Tagged rows | 12 |
| Unique tags | 10 |

## Tag counts

| Tag | Count | Weight |
|---|---|---|
| CLAMP_4 | 6 | 25 |
| CLAMP_ANY | 6 | 20 |
| CARRY_PERM | 5 | 70 |
| STRAIGHT_GATE | 2 | 80 |
| CARRY_PERM_HARDLOCK | 1 | 95 |
| ENGINE_GOV | 1 | 85 |
| CARRY_PERM_GOV | 1 | 75 |
| IDX_ECHO_CLAMP | 1 | 65 |
| IDX_ECHO_BASE | 1 | 60 |
| DBL_BA | 1 | 45 |

## Rows (sorted)

| Priority | StateKey | Variant | TopEvent | Tags | A11★ | A12 sizes | MinSet | MinCap | MergedHit |
|---|---|---|---|---|---|---|---|---|---|
| 95 | Michigan4 | Combined | CARRY_PERM_HARDLOCK | CARRY_PERM_HARDLOCK|ENGINE_GOV|STRAIGHT_GATE|CARRY_PERM_GOV|CARRY_PERM|CLAMP_4|CLAMP_ANY | 2 | 4 | 3 | 3 | N |
| 80 | Ohio4 | Combined | STRAIGHT_GATE | STRAIGHT_GATE|DBL_BA | 2 |  | 3 | 0 | N |
| 70 | Connecticut4 | Midday | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 70 | Florida4 | Evening | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 70 | OntarioCanada4 | Midday | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 70 | SouthCarolina4 | Combined | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 65 | PuertoRico4 | Evening | IDX_ECHO_CLAMP | IDX_ECHO_CLAMP|IDX_ECHO_BASE |  |  | 3 | 3 | N |
| 25 | Pennsylvania4 | Combined | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 3 | 0 | N |
| 25 | Connecticut4 | Evening | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 5 | N |
| 25 | Florida4 | Combined | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 0 | N |
| 25 | Indiana4 | Combined | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 0 | N |
| 25 | SouthCarolina4 | Midday | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 5 | N |

## Regenerate
```bash
python3 scripts/tools/export_profit_compound_events.py --date 2026-01-02
```
