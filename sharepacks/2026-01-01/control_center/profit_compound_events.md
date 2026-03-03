# Profit Compound Events — 2026-01-01

This is a **shadow-only** triage board derived from Profit Alerts.
It flags “watchlist” compound co-fire environments defined in:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Compound_Events_Watchlist.md`

## Counts
| Field | Value |
|---|---|
| Tagged rows | 10 |
| Unique tags | 7 |

## Tag counts

| Tag | Count | Weight |
|---|---|---|
| CLAMP_4 | 6 | 25 |
| CLAMP_ANY | 6 | 20 |
| CARRY_PERM | 3 | 70 |
| STRAIGHT_GATE | 2 | 80 |
| ENGINE_GOV | 1 | 85 |
| IDX_ECHO_CLAMP | 1 | 65 |
| IDX_ECHO_BASE | 1 | 60 |

## Rows (sorted)

| Priority | StateKey | Variant | TopEvent | Tags | A11★ | A12 sizes | MinSet | MinCap | MergedHit |
|---|---|---|---|---|---|---|---|---|---|
| 85 | Michigan4 | Combined | ENGINE_GOV | ENGINE_GOV | 2 |  | 3 | 8 | N |
| 80 | Connecticut4 | Combined | STRAIGHT_GATE | STRAIGHT_GATE|CLAMP_4|CLAMP_ANY | 2 | 4 | 3 | 3 | N |
| 80 | Ohio4 | Combined | STRAIGHT_GATE | STRAIGHT_GATE | 2 |  | 3 | 3 | N |
| 70 | NorthCarolina4 | Midday | CARRY_PERM | CARRY_PERM |  |  | 3 | 3 | N |
| 70 | Pennsylvania4 | Midday | CARRY_PERM | CARRY_PERM|CLAMP_4|CLAMP_ANY |  | 4 | 3 | 3 | N |
| 70 | SouthCarolina4 | Midday | CARRY_PERM | CARRY_PERM|CLAMP_4|CLAMP_ANY |  | 4 | 3 | 0 | N |
| 65 | PuertoRico4 | Evening | IDX_ECHO_CLAMP | IDX_ECHO_CLAMP|IDX_ECHO_BASE |  |  | 3 | 3 | N |
| 25 | Indiana4 | Combined | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 3 | 3 | N |
| 25 | Florida4 | Combined | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 0 | N |
| 25 | Michigan4 | Midday | CLAMP_4 | CLAMP_4|CLAMP_ANY |  | 4 | 4 | 0 | N |

## Regenerate
```bash
python3 scripts/tools/export_profit_compound_events.py --date 2026-01-01
```
