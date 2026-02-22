# Profit Alerts Evaluation — 2026-01-07

- Generated: `2026-02-22T05:03:09.844702+00:00`
- Inputs:
  - `sharepacks/2026-01-07/control_center/profit_alerts.csv`
  - `data/results/*.txt` (local only)
- Charter: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`

## Integrity summary
- rows_total: `76`
- evidence_parse_errors: `0`
- non_3digit_canonical: `0`
- missing_results_state (state not found on D): `0`
- stable_scores_missing (per-state Stable scores missing/unreadable): `0`
- stable_candidate_missing (canonical not found in Stable scores section): `0`

## Scorecard (variant-faithful lens, by AlertId)
| AlertId | Fired | HIT(decay) | EXPIRED | CENSORED | HIT<=7 | HIT<=14 | mean t_hit |
|---:|---:|---:|---:|---:|---:|---:|---:|
| A01 | 9 | 0 | 9 | 0 | 1 | 1 | - |
| A02 | 7 | 0 | 7 | 0 | 0 | 0 | - |
| A04 | 14 | 0 | 14 | 0 | 1 | 1 | - |
| A05 | 14 | 0 | 14 | 0 | 0 | 0 | - |
| A07 | 1 | 0 | 1 | 0 | 0 | 0 | - |
| A09 | 1 | 0 | 1 | 0 | 0 | 0 | - |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 | - |
| A11:S2 | 3 | 0 | 3 | 0 | 0 | 0 | - |
| A12 | 9 | 0 | 9 | 0 | 0 | 0 | - |

Promoters fired (not gradeable as winner hits):
- A08: 15

## Scorecard (any-outcome lens, by AlertId)

For `Midday` / `Evening` variant rows, this counts a hit if the episode resolves on either `Midday` or `Evening` within the same time-span boundary as the variant-faithful window.

| AlertId | Fired | HIT_any(decay) | EXPIRED_any | CENSORED_any | HIT_any<=7 | HIT_any<=14 |
|---:|---:|---:|---:|---:|---:|---:|
| A01 | 9 | 0 | 9 | 0 | 1 | 1 |
| A02 | 7 | 0 | 7 | 0 | 0 | 1 |
| A04 | 14 | 0 | 14 | 0 | 1 | 1 |
| A05 | 14 | 0 | 14 | 0 | 0 | 1 |
| A07 | 1 | 0 | 1 | 0 | 1 | 1 |
| A09 | 1 | 0 | 1 | 0 | 1 | 1 |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 |
| A11:S2 | 3 | 0 | 3 | 0 | 0 | 0 |
| A12 | 9 | 0 | 9 | 0 | 0 | 0 |

## Merged episodes (deduped play-sets)

This view dedupes rows that imply the same concrete play-set (same `StateKey × Variant × implied_set`) so co-firing alerts do not get double-counted.

- merged_rows_total: `58`

| StateKey | Variant | Strength | Alerts | Promoters | DecayMax | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen |
|---|---|---:|---|---|---:|---|---:|---|---|---|---|---|---|
| NewYork4 | Combined | 5 | A11 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| OntarioCanada4 | Combined | 5 | A11 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Virginia4 | Combined | 5 | A11 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Connecticut4 | Combined | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Connecticut4 | Evening | 4 | A01,A04 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| Connecticut4 | Midday | 4 | A09 | - | 1 | EXPIRED | - | - | - | N | N | N | - |
| Delaware4 | Combined | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Delaware4 | Midday | 4 | A02 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Delaware4 | Midday | 4 | A07 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Florida4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Indiana4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Michigan4 | Midday | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewJersey4 | Combined | 4 | A10 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| NewJersey4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Combined | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Evening | 4 | A01 | A08 | 3 | EXPIRED | - | - | - | Y | Y | N | - |
| NorthCarolina4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Ohio4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| OntarioCanada4 | Midday | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Pennsylvania4 | Midday | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| PuertoRico4 | Evening | 4 | A04 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| PuertoRico4 | Midday | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| PuertoRico4 | Midday | 4 | A01 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| SouthCarolina4 | Evening | 4 | A01 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| SouthCarolina4 | Midday | 4 | A01 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |

Full merged evaluation:
- `sharepacks/2026-01-07/control_center/profit_alerts_eval_merged.csv`

## Top episodes (by Strength, then earliest hit)

| # | StateKey | Variant | AlertId | Strength | Suggested | Decay | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen | Strict |
|---:|---|---|---|---:|---|---:|---|---:|---|---|---|---|---|---|---|
| 65 | NewYork4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 66 | OntarioCanada4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 67 | Virginia4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 1 | Connecticut4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 2 | Connecticut4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 3 | NewYork4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | Y | Y | N | - | N |
| 4 | PuertoRico4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 5 | SouthCarolina4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 6 | SouthCarolina4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 7 | Virginia4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 8 | Virginia4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 9 | Virginia4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 10 | Delaware4 | Midday | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 17 | PuertoRico4 | Evening | A04 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 31 | Connecticut4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 32 | Delaware4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 33 | Florida4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 34 | Indiana4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 35 | Michigan4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 36 | NewJersey4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 37 | NewYork4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 38 | NorthCarolina4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 39 | Ohio4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 40 | OntarioCanada4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 41 | Pennsylvania4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |

Full per-row evaluation:
- `sharepacks/2026-01-07/control_center/profit_alerts_eval.csv`
