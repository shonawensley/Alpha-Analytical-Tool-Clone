# Profit Alerts Evaluation — 2025-12-31

- Generated: `2026-03-03T08:01:12.948483+00:00`
- Inputs:
  - `sharepacks/2025-12-31/control_center/profit_alerts.csv`
  - `data/results/*.txt` (local only)
- Charter: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`

## Integrity summary
- rows_total: `69`
- evidence_parse_errors: `0`
- non_3digit_canonical: `0`
- missing_results_state (state not found on D): `0`
- stable_scores_missing (per-state Stable scores missing/unreadable): `0`
- stable_candidate_missing (canonical not found in Stable scores section): `0`

## Scorecard (variant-faithful lens, by AlertId)
| AlertId | Fired | HIT(decay) | EXPIRED | CENSORED | HIT<=7 | HIT<=14 | mean t_hit |
|---:|---:|---:|---:|---:|---:|---:|---:|
| A01 | 5 | 0 | 5 | 0 | 0 | 1 | - |
| A02 | 8 | 0 | 8 | 0 | 0 | 2 | - |
| A04 | 14 | 0 | 14 | 0 | 0 | 2 | - |
| A05 | 14 | 0 | 14 | 0 | 0 | 1 | - |
| A09 | 2 | 0 | 2 | 0 | 0 | 0 | - |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 | - |
| A11:S2 | 2 | 0 | 2 | 0 | 0 | 0 | - |
| A12 | 7 | 0 | 7 | 0 | 0 | 0 | - |

Promoters fired (not gradeable as winner hits):
- A08: 14

## Scorecard (any-outcome lens, by AlertId)

For `Midday` / `Evening` variant rows, this counts a hit if the episode resolves on either `Midday` or `Evening` within the same time-span boundary as the variant-faithful window.

| AlertId | Fired | HIT_any(decay) | EXPIRED_any | CENSORED_any | HIT_any<=7 | HIT_any<=14 |
|---:|---:|---:|---:|---:|---:|---:|
| A01 | 5 | 0 | 5 | 0 | 0 | 1 |
| A02 | 8 | 0 | 8 | 0 | 0 | 2 |
| A04 | 14 | 0 | 14 | 0 | 1 | 3 |
| A05 | 14 | 0 | 14 | 0 | 0 | 1 |
| A09 | 2 | 0 | 2 | 0 | 1 | 2 |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 |
| A11:S2 | 2 | 0 | 2 | 0 | 0 | 0 |
| A12 | 7 | 0 | 7 | 0 | 1 | 1 |

## Merged episodes (deduped play-sets)

This view dedupes rows that imply the same concrete play-set (same `StateKey × Variant × implied_set`) so co-firing alerts do not get double-counted.

- merged_rows_total: `48`

| StateKey | Variant | Strength | Alerts | Promoters | DecayMax | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen |
|---|---|---:|---|---|---:|---|---:|---|---|---|---|---|---|
| Connecticut4 | Combined | 5 | A11 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Connecticut4 | Midday | 5 | A01 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| PuertoRico4 | Combined | 5 | A02,A11 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Connecticut4 | Combined | 4 | A01 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Connecticut4 | Evening | 4 | A02,A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Delaware4 | Combined | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Florida4 | Evening | 4 | A09 | A08 | 1 | EXPIRED | - | - | - | N | N | N | - |
| Florida4 | Evening | 4 | A02,A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Indiana4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Michigan4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Michigan4 | Midday | 4 | A01 | - | 3 | EXPIRED | - | - | - | N | Y | N | - |
| NewJersey4 | Combined | 4 | A02,A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Midday | 4 | A01 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Midday | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| NorthCarolina4 | Combined | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Ohio4 | Evening | 4 | A01 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Ohio4 | Midday | 4 | A04 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Ohio4 | Midday | 4 | A02,A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| OntarioCanada4 | Midday | 4 | A02,A05 | A08 | 2 | EXPIRED | - | - | - | N | Y | N | - |
| Pennsylvania4 | Midday | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| PuertoRico4 | Combined | 4 | A10 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| PuertoRico4 | Midday | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| SouthCarolina4 | Midday | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| SouthCarolina4 | Midday | 4 | A09 | A08 | 1 | EXPIRED | - | - | - | N | N | N | - |
| Virginia4 | Combined | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |

Full merged evaluation:
- `sharepacks/2025-12-31/control_center/profit_alerts_eval_merged.csv`

## Top episodes (by Strength, then earliest hit)

| # | StateKey | Variant | AlertId | Strength | Suggested | Decay | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen | Strict |
|---:|---|---|---|---:|---|---:|---|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | Midday | A01 | 5 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 61 | Connecticut4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 62 | PuertoRico4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 2 | Connecticut4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 3 | Michigan4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | Y | N | - | N |
| 4 | NewYork4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 5 | Ohio4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 6 | Ohio4 | Midday | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 7 | PuertoRico4 | Combined | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 14 | Ohio4 | Midday | A04 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 28 | Connecticut4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 29 | Delaware4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 30 | Florida4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 31 | Indiana4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 32 | Michigan4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 33 | NewJersey4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 34 | NewYork4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 35 | NorthCarolina4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 36 | Ohio4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 37 | OntarioCanada4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | Y | N | - | N |
| 38 | Pennsylvania4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 39 | PuertoRico4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 40 | SouthCarolina4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 41 | Virginia4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 56 | Florida4 | Evening | A09 | 4 | STR8_8 | 1 | EXPIRED | - | - | - | N | N | N | - | N |

Full per-row evaluation:
- `sharepacks/2025-12-31/control_center/profit_alerts_eval.csv`
