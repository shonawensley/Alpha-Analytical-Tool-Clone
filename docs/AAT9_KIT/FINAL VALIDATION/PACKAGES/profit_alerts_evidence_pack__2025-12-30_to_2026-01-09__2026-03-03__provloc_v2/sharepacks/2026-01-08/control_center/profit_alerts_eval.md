# Profit Alerts Evaluation — 2026-01-08

- Generated: `2026-03-03T07:02:53.817871+00:00`
- Inputs:
  - `sharepacks/2026-01-08/control_center/profit_alerts.csv`
  - `data/results/*.txt` (local only)
- Charter: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`

## Integrity summary
- rows_total: `70`
- evidence_parse_errors: `0`
- non_3digit_canonical: `0`
- missing_results_state (state not found on D): `0`
- stable_scores_missing (per-state Stable scores missing/unreadable): `0`
- stable_candidate_missing (canonical not found in Stable scores section): `0`

## Scorecard (variant-faithful lens, by AlertId)
| AlertId | Fired | HIT(decay) | EXPIRED | CENSORED | HIT<=7 | HIT<=14 | mean t_hit |
|---:|---:|---:|---:|---:|---:|---:|---:|
| A01 | 8 | 0 | 8 | 0 | 0 | 0 | - |
| A02 | 7 | 0 | 7 | 0 | 0 | 0 | - |
| A04 | 14 | 1 | 13 | 0 | 1 | 1 | 0.00 |
| A05 | 13 | 0 | 13 | 0 | 0 | 0 | - |
| A09 | 1 | 0 | 1 | 0 | 0 | 0 | - |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 | - |
| A11:S2 | 4 | 0 | 4 | 0 | 0 | 0 | - |
| A12 | 7 | 1 | 6 | 0 | 1 | 1 | 0.00 |

Promoters fired (not gradeable as winner hits):
- A08: 13

## Scorecard (any-outcome lens, by AlertId)

For `Midday` / `Evening` variant rows, this counts a hit if the episode resolves on either `Midday` or `Evening` within the same time-span boundary as the variant-faithful window.

| AlertId | Fired | HIT_any(decay) | EXPIRED_any | CENSORED_any | HIT_any<=7 | HIT_any<=14 |
|---:|---:|---:|---:|---:|---:|---:|
| A01 | 8 | 0 | 8 | 0 | 0 | 0 |
| A02 | 7 | 0 | 7 | 0 | 0 | 0 |
| A04 | 14 | 1 | 13 | 0 | 1 | 1 |
| A05 | 13 | 0 | 13 | 0 | 1 | 1 |
| A09 | 1 | 0 | 1 | 0 | 0 | 1 |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 |
| A11:S2 | 4 | 0 | 4 | 0 | 0 | 0 |
| A12 | 7 | 1 | 6 | 0 | 1 | 1 |

## Merged episodes (deduped play-sets)

This view dedupes rows that imply the same concrete play-set (same `StateKey × Variant × implied_set`) so co-firing alerts do not get double-counted.

- merged_rows_total: `49`

| StateKey | Variant | Strength | Alerts | Promoters | DecayMax | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen |
|---|---|---:|---|---|---:|---|---:|---|---|---|---|---|---|
| NewJersey4 | Midday | 3 | A12 | - | 2 | HIT | 0 | 2026-01-08 Midday | Straight | Y | Y | Y | 2026-01-08 Midday |
| NewJersey4 | Midday | 3 | A04 | - | 3 | HIT | 0 | 2026-01-08 Midday | Boxed | Y | Y | Y | 2026-01-08 Midday |
| Michigan4 | Combined | 5 | A02,A11 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewJersey4 | Combined | 5 | A11 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Combined | 5 | A05,A11 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Virginia4 | Combined | 5 | A11 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Connecticut4 | Combined | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Delaware4 | Midday | 4 | A09 | A08 | 1 | EXPIRED | - | - | - | N | N | N | - |
| Delaware4 | Midday | 4 | A02,A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Florida4 | Combined | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Indiana4 | Evening | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Michigan4 | Midday | 4 | A02,A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewJersey4 | Combined | 4 | A01 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| NewJersey4 | Combined | 4 | A10 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| NewJersey4 | Evening | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Combined | 4 | A01 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Evening | 4 | A02 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| NorthCarolina4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Ohio4 | Combined | 4 | A04 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Ohio4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| OntarioCanada4 | Midday | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Pennsylvania4 | Midday | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Pennsylvania4 | Midday | 4 | A01,A04 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| SouthCarolina4 | Evening | 4 | A01 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| SouthCarolina4 | Midday | 4 | A01 | - | 3 | EXPIRED | - | - | - | N | ? | N | - |

Full merged evaluation:
- `sharepacks/2026-01-08/control_center/profit_alerts_eval_merged.csv`

## Top episodes (by Strength, then earliest hit)

| # | StateKey | Variant | AlertId | Strength | Suggested | Decay | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen | Strict |
|---:|---|---|---|---:|---|---:|---|---:|---|---|---|---|---|---|---|
| 22 | NewJersey4 | Midday | A04 | 3 | BOX | 3 | HIT | 0 | 2026-01-08 Midday | Boxed | Y | Y | Y | 2026-01-08 Midday | Y |
| 66 | NewJersey4 | Midday | A12 | 3 | STR8_4of8 | 2 | HIT | 0 | 2026-01-08 Midday | Straight+Boxed | Y | Y | Y | 2026-01-08 Midday | Y |
| 60 | Michigan4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 61 | NewJersey4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 62 | NewYork4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 63 | Virginia4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 1 | NewJersey4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 2 | NewYork4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 3 | Pennsylvania4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 4 | SouthCarolina4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 5 | SouthCarolina4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | ? | N | - | N |
| 6 | Virginia4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 7 | Virginia4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 8 | Virginia4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 9 | NewYork4 | Evening | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 16 | Ohio4 | Combined | A04 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 30 | Connecticut4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 31 | Delaware4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 32 | Florida4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 33 | Indiana4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 34 | Michigan4 | Midday | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 35 | NewJersey4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 36 | NewYork4 | Combined | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 37 | NorthCarolina4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 38 | Ohio4 | Evening | A05 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |

Full per-row evaluation:
- `sharepacks/2026-01-08/control_center/profit_alerts_eval.csv`
