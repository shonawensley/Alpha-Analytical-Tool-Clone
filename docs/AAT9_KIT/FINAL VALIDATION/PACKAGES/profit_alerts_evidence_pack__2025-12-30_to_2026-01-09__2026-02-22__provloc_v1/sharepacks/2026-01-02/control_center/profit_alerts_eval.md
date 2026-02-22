# Profit Alerts Evaluation — 2026-01-02

- Generated: `2026-02-22T05:18:36.281830+00:00`
- Inputs:
  - `sharepacks/2026-01-02/control_center/profit_alerts.csv`
  - `data/results/*.txt` (local only)
- Charter: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`

## Integrity summary
- rows_total: `64`
- evidence_parse_errors: `0`
- non_3digit_canonical: `0`
- missing_results_state (state not found on D): `0`
- stable_scores_missing (per-state Stable scores missing/unreadable): `0`
- stable_candidate_missing (canonical not found in Stable scores section): `0`

## Scorecard (variant-faithful lens, by AlertId)
| AlertId | Fired | HIT(decay) | EXPIRED | CENSORED | HIT<=7 | HIT<=14 | mean t_hit |
|---:|---:|---:|---:|---:|---:|---:|---:|
| A01 | 4 | 0 | 4 | 0 | 0 | 0 | - |
| A02 | 4 | 0 | 4 | 0 | 2 | 2 | - |
| A04 | 14 | 0 | 14 | 0 | 0 | 0 | - |
| A05 | 14 | 0 | 14 | 0 | 1 | 1 | - |
| A09 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 | - |
| A11:S2 | 2 | 0 | 2 | 0 | 0 | 0 | - |
| A12 | 6 | 0 | 6 | 0 | 0 | 0 | - |

Promoters fired (not gradeable as winner hits):
- A03: 1
- A08: 15

## Scorecard (any-outcome lens, by AlertId)

For `Midday` / `Evening` variant rows, this counts a hit if the episode resolves on either `Midday` or `Evening` within the same time-span boundary as the variant-faithful window.

| AlertId | Fired | HIT_any(decay) | EXPIRED_any | CENSORED_any | HIT_any<=7 | HIT_any<=14 |
|---:|---:|---:|---:|---:|---:|---:|
| A01 | 4 | 0 | 4 | 0 | 0 | 0 |
| A02 | 4 | 0 | 4 | 0 | 2 | 2 |
| A04 | 14 | 0 | 14 | 0 | 0 | 0 |
| A05 | 14 | 0 | 14 | 0 | 1 | 1 |
| A09 | 1 | 0 | 1 | 0 | 0 | 1 |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 |
| A11:S2 | 2 | 0 | 2 | 0 | 0 | 0 |
| A12 | 6 | 0 | 6 | 0 | 0 | 0 |

## Merged episodes (deduped play-sets)

This view dedupes rows that imply the same concrete play-set (same `StateKey × Variant × implied_set`) so co-firing alerts do not get double-counted.

- merged_rows_total: `40`

| StateKey | Variant | Strength | Alerts | Promoters | DecayMax | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen |
|---|---|---:|---|---|---:|---|---:|---|---|---|---|---|---|
| Michigan4 | Combined | 5 | A01,A04,A11 | A03 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Connecticut4 | Midday | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Delaware4 | Midday | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Delaware4 | Midday | 4 | A01 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Florida4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Indiana4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Michigan4 | Combined | 4 | A05 | A03 | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewJersey4 | Combined | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| NorthCarolina4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Ohio4 | Combined | 4 | A02,A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| OntarioCanada4 | Midday | 4 | A02,A05 | - | 2 | EXPIRED | - | - | - | Y | Y | N | - |
| Pennsylvania4 | Combined | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| PuertoRico4 | Combined | 4 | A10 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| PuertoRico4 | Evening | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| PuertoRico4 | Evening | 4 | A01 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| PuertoRico4 | Evening | 4 | A09 | - | 1 | EXPIRED | - | - | - | N | N | N | - |
| SouthCarolina4 | Combined | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Virginia4 | Combined | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Connecticut4 | Evening | 3 | A12 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Connecticut4 | Midday | 3 | A04 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| Delaware4 | Combined | 3 | A04 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Florida4 | Combined | 3 | A12 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Florida4 | Evening | 3 | A04 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Indiana4 | Combined | 3 | A04 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |

Full merged evaluation:
- `sharepacks/2026-01-02/control_center/profit_alerts_eval_merged.csv`

## Top episodes (by Strength, then earliest hit)

| # | StateKey | Variant | AlertId | Strength | Suggested | Decay | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen | Strict |
|---:|---|---|---|---:|---|---:|---|---:|---|---|---|---|---|---|---|
| 57 | Michigan4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 58 | Ohio4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 1 | Delaware4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 2 | Michigan4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 3 | Michigan4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 4 | PuertoRico4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 5 | OntarioCanada4 | Midday | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | Y | Y | N | - | N |
| 6 | OntarioCanada4 | Midday | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | Y | Y | N | - | N |
| 24 | Connecticut4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 25 | Delaware4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 26 | Florida4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 27 | Indiana4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 28 | Michigan4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 29 | NewJersey4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 30 | NewYork4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 31 | NorthCarolina4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 32 | Ohio4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 33 | OntarioCanada4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | Y | Y | N | - | N |
| 34 | Pennsylvania4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 35 | PuertoRico4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 36 | SouthCarolina4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 37 | Virginia4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 53 | PuertoRico4 | Evening | A09 | 4 | STR8_8 | 1 | EXPIRED | - | - | - | N | Y | N | - | N |
| 54 | PuertoRico4 | Combined | A10 | 4 | STR8_3 | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 7 | Ohio4 | Combined | A02 | 3 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |

Full per-row evaluation:
- `sharepacks/2026-01-02/control_center/profit_alerts_eval.csv`
