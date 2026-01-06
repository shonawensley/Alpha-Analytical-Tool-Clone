# Profit Alerts Evaluation — 2026-01-01

- Generated: `2026-01-05T12:31:54.002148+00:00`
- Inputs:
  - `sharepacks/2026-01-01/control_center/profit_alerts.csv`
  - `data/results/*.txt` (local only)
- Charter: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`

## Integrity summary
- rows_total: `70`
- evidence_parse_errors: `0`
- non_3digit_canonical: `0`
- missing_results_state (state not found on D): `7`
- stable_scores_missing (per-state Stable scores missing/unreadable): `0`
- stable_candidate_missing (canonical not found in Stable scores section): `0`

## Scorecard (variant-faithful lens, by AlertId)
| AlertId | Fired | HIT(decay) | EXPIRED | CENSORED | HIT<=7 | HIT<=14 | mean t_hit |
|---:|---:|---:|---:|---:|---:|---:|---:|
| A01 | 6 | 0 | 5 | 1 | 0 | 0 | - |
| A02 | 8 | 0 | 8 | 0 | 0 | 0 | - |
| A04 | 14 | 0 | 14 | 0 | 1 | 1 | - |
| A05 | 14 | 0 | 14 | 0 | 0 | 0 | - |
| A06 | 1 | 0 | 1 | 0 | 0 | 0 | - |
| A09 | 2 | 0 | 2 | 0 | 0 | 0 | - |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 | - |
| A11:S2 | 4 | 0 | 4 | 0 | 0 | 0 | - |
| A12 | 6 | 0 | 6 | 0 | 1 | 1 | - |

Promoters fired (not gradeable as winner hits):
- A03: 1
- A08: 11

## Scorecard (any-outcome lens, by AlertId)

For `Midday` / `Evening` variant rows, this counts a hit if the episode resolves on either `Midday` or `Evening` within the same time-span boundary as the variant-faithful window.

| AlertId | Fired | HIT_any(decay) | EXPIRED_any | CENSORED_any | HIT_any<=7 | HIT_any<=14 |
|---:|---:|---:|---:|---:|---:|---:|
| A01 | 6 | 0 | 5 | 1 | 0 | 0 |
| A02 | 8 | 0 | 8 | 0 | 0 | 0 |
| A04 | 14 | 0 | 14 | 0 | 1 | 1 |
| A05 | 14 | 0 | 14 | 0 | 0 | 0 |
| A06 | 1 | 0 | 1 | 0 | 0 | 0 |
| A09 | 2 | 0 | 2 | 0 | 0 | 0 |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 |
| A11:S2 | 4 | 0 | 4 | 0 | 0 | 0 |
| A12 | 6 | 0 | 6 | 0 | 1 | 1 |

## Merged episodes (deduped play-sets)

This view dedupes rows that imply the same concrete play-set (same `StateKey × Variant × implied_set`) so co-firing alerts do not get double-counted.

- merged_rows_total: `49`

| StateKey | Variant | Strength | Alerts | Promoters | DecayMax | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen |
|---|---|---:|---|---|---:|---|---:|---|---|---|---|---|---|
| Connecticut4 | Combined | 5 | A11 | A08 | 2 | EXPIRED | - | - | - | N | ? | N | - |
| Michigan4 | Combined | 5 | A01,A04,A11 | A03,A08 | 3 | EXPIRED | - | - | - | N | ? | N | - |
| NewYork4 | Midday | 5 | A01 | A08 | 3 | EXPIRED | - | - | - | ? | ? | N | - |
| Ohio4 | Combined | 5 | A11 | A08 | 2 | EXPIRED | - | - | - | N | ? | N | - |
| PuertoRico4 | Combined | 5 | A11 | - | 2 | EXPIRED | - | - | - | ? | ? | N | - |
| Connecticut4 | Combined | 4 | A02 | A08 | 2 | EXPIRED | - | - | - | N | ? | N | - |
| Connecticut4 | Evening | 4 | A02,A05 | - | 2 | EXPIRED | - | - | - | ? | ? | N | - |
| Connecticut4 | Midday | 4 | A01 | A08 | 3 | EXPIRED | - | - | - | ? | ? | N | - |
| Delaware4 | Combined | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | ? | N | - |
| Florida4 | Evening | 4 | A02,A05 | A08 | 2 | EXPIRED | - | - | - | ? | ? | N | - |
| Indiana4 | Combined | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | ? | N | - |
| Michigan4 | Evening | 4 | A05 | A03 | 2 | EXPIRED | - | - | - | ? | ? | N | - |
| Michigan4 | Midday | 4 | A01 | A03,A08 | 3 | EXPIRED | - | - | - | ? | ? | N | - |
| NewJersey4 | Combined | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | ? | N | - |
| NewYork4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | ? | ? | N | - |
| NorthCarolina4 | Midday | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | ? | ? | N | - |
| Ohio4 | Combined | 4 | A02,A05 | A08 | 2 | EXPIRED | - | - | - | N | ? | N | - |
| OntarioCanada4 | Midday | 4 | A02,A05 | A08 | 2 | EXPIRED | - | - | - | ? | ? | N | - |
| Pennsylvania4 | Midday | 4 | A05 | - | 2 | EXPIRED | - | - | - | ? | ? | N | - |
| PuertoRico4 | Combined | 4 | A02 | - | 2 | EXPIRED | - | - | - | ? | ? | N | - |
| PuertoRico4 | Combined | 4 | A10 | - | 3 | EXPIRED | - | - | - | ? | ? | N | - |
| PuertoRico4 | Evening | 4 | A05 | - | 2 | EXPIRED | - | - | - | ? | ? | N | - |
| PuertoRico4 | Evening | 4 | A09 | - | 1 | EXPIRED | - | - | - | ? | ? | N | - |
| SouthCarolina4 | Midday | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | ? | ? | N | - |
| Virginia4 | Combined | 4 | A09 | A08 | 1 | EXPIRED | - | - | - | N | ? | N | - |

Full merged evaluation:
- `sharepacks/2026-01-01/control_center/profit_alerts_eval_merged.csv`

## Top episodes (by Strength, then earliest hit)

| # | StateKey | Variant | AlertId | Strength | Suggested | Decay | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen | Strict |
|---:|---|---|---|---:|---|---:|---|---:|---|---|---|---|---|---|---|
| 1 | NewYork4 | Midday | A01 | 5 | BOX | 3 | EXPIRED | - | - | - | ? | ? | N | - | N |
| 61 | Connecticut4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | ? | N | - | N |
| 62 | Michigan4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | ? | N | - | N |
| 63 | Ohio4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | ? | N | - | N |
| 64 | PuertoRico4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | ? | ? | N | - | ? |
| 2 | Connecticut4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | ? | ? | N | - | N |
| 3 | Connecticut4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | ? | ? | N | - | N |
| 4 | Michigan4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | ? | N | - | N |
| 5 | Michigan4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | ? | ? | N | - | N |
| 7 | Connecticut4 | Combined | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | ? | N | - | N |
| 8 | Connecticut4 | Evening | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | ? | ? | N | - | N |
| 9 | OntarioCanada4 | Midday | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | ? | ? | N | - | N |
| 10 | OntarioCanada4 | Midday | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | ? | ? | N | - | N |
| 11 | PuertoRico4 | Combined | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | ? | ? | N | - | ? |
| 30 | Connecticut4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | ? | ? | N | - | N |
| 31 | Delaware4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | ? | N | - | N |
| 32 | Florida4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | ? | ? | N | - | N |
| 33 | Indiana4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | ? | N | - | N |
| 34 | Michigan4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | ? | ? | N | - | N |
| 35 | NewJersey4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | ? | N | - | N |
| 36 | NewYork4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | ? | ? | N | - | N |
| 37 | NorthCarolina4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | ? | ? | N | - | N |
| 38 | Ohio4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | ? | N | - | N |
| 39 | OntarioCanada4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | ? | ? | N | - | N |
| 40 | Pennsylvania4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | ? | ? | N | - | N |

Full per-row evaluation:
- `sharepacks/2026-01-01/control_center/profit_alerts_eval.csv`
