# Profit Alerts Evaluation — 2025-06-21

- Generated: `2026-02-22T05:02:54.584667+00:00`
- Inputs:
  - `sharepacks/2025-06-21/control_center/profit_alerts.csv`
  - `data/results/*.txt` (local only)
- Charter: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`

## Integrity summary
- rows_total: `84`
- evidence_parse_errors: `0`
- non_3digit_canonical: `0`
- missing_results_state (state not found on D): `0`
- stable_scores_missing (per-state Stable scores missing/unreadable): `0`
- stable_candidate_missing (canonical not found in Stable scores section): `0`

## Scorecard (variant-faithful lens, by AlertId)
| AlertId | Fired | HIT(decay) | EXPIRED | CENSORED | HIT<=7 | HIT<=14 | mean t_hit |
|---:|---:|---:|---:|---:|---:|---:|---:|
| A01 | 13 | 0 | 13 | 0 | 0 | 1 | - |
| A02 | 12 | 2 | 10 | 0 | 2 | 2 | 1.00 |
| A04 | 14 | 0 | 14 | 0 | 0 | 1 | - |
| A05 | 14 | 1 | 13 | 0 | 1 | 1 | 1.00 |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 | - |
| A11:S2 | 4 | 0 | 4 | 0 | 0 | 0 | - |
| A12 | 5 | 0 | 5 | 0 | 0 | 0 | - |

Promoters fired (not gradeable as winner hits):
- A03: 1
- A08: 18

## Scorecard (any-outcome lens, by AlertId)

For `Midday` / `Evening` variant rows, this counts a hit if the episode resolves on either `Midday` or `Evening` within the same time-span boundary as the variant-faithful window.

| AlertId | Fired | HIT_any(decay) | EXPIRED_any | CENSORED_any | HIT_any<=7 | HIT_any<=14 |
|---:|---:|---:|---:|---:|---:|---:|
| A01 | 13 | 0 | 13 | 0 | 0 | 1 |
| A02 | 12 | 2 | 10 | 0 | 2 | 2 |
| A04 | 14 | 0 | 14 | 0 | 0 | 2 |
| A05 | 14 | 1 | 13 | 0 | 1 | 1 |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 |
| A11:S2 | 4 | 0 | 4 | 0 | 0 | 0 |
| A12 | 5 | 0 | 5 | 0 | 0 | 0 |

## Merged episodes (deduped play-sets)

This view dedupes rows that imply the same concrete play-set (same `StateKey × Variant × implied_set`) so co-firing alerts do not get double-counted.

- merged_rows_total: `52`

| StateKey | Variant | Strength | Alerts | Promoters | DecayMax | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen |
|---|---|---:|---|---|---:|---|---:|---|---|---|---|---|---|
| NewJersey4 | Evening | 4 | A05 | - | 2 | HIT | 1 | 2025-06-22 Evening | Straight | Y | Y | Y | 2025-06-22 Evening |
| Florida4 | Midday | 3 | A02 | A08 | 2 | HIT | 1 | 2025-06-22 Midday | Straight | Y | Y | Y | 2025-06-22 Midday |
| Indiana4 | Combined | 5 | A01,A11 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Combined | 5 | A11 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Evening | 5 | A02 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| OntarioCanada4 | Combined | 5 | A01,A11 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Pennsylvania4 | Combined | 5 | A01,A04,A11 | A03,A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Connecticut4 | Combined | 4 | A10 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Connecticut4 | Combined | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Delaware4 | Combined | 4 | A04 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Delaware4 | Midday | 4 | A02,A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Florida4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Indiana4 | Combined | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Indiana4 | Midday | 4 | A02 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Michigan4 | Evening | 4 | A01,A04 | A08 | 3 | EXPIRED | - | - | - | N | Y | N | - |
| Michigan4 | Midday | 4 | A02,A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Combined | 4 | A01 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Combined | 4 | A02,A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Evening | 4 | A04 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Midday | 4 | A02 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| NorthCarolina4 | Combined | 4 | A04 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| NorthCarolina4 | Midday | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Ohio4 | Midday | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Ohio4 | Midday | 4 | A01 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| OntarioCanada4 | Evening | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |

Full merged evaluation:
- `sharepacks/2025-06-21/control_center/profit_alerts_eval_merged.csv`

## Top episodes (by Strength, then earliest hit)

| # | StateKey | Variant | AlertId | Strength | Suggested | Decay | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen | Strict |
|---:|---|---|---|---:|---|---:|---|---:|---|---|---|---|---|---|---|
| 46 | NewJersey4 | Evening | A05 | 4 | STR8_3 | 2 | HIT | 1 | 2025-06-22 Evening | Straight+Boxed | Y | Y | Y | 2025-06-22 Evening | N |
| 19 | Florida4 | Midday | A02 | 3 | STR8_3 | 2 | HIT | 1 | 2025-06-22 Midday | Straight+Boxed | Y | Y | Y | 2025-06-22 Midday | N |
| 20 | Florida4 | Midday | A02 | 3 | STR8_3 | 2 | HIT | 1 | 2025-06-22 Midday | Straight+Boxed | Y | Y | Y | 2025-06-22 Midday | N |
| 14 | NewYork4 | Evening | A02 | 5 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 76 | Indiana4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 77 | NewYork4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 78 | OntarioCanada4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 79 | Pennsylvania4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 1 | Indiana4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 2 | Michigan4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | Y | N | - | N |
| 3 | NewYork4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 4 | Ohio4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 5 | OntarioCanada4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 6 | Pennsylvania4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 7 | Pennsylvania4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 8 | Pennsylvania4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 9 | Pennsylvania4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 10 | Pennsylvania4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 11 | PuertoRico4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 12 | PuertoRico4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 13 | SouthCarolina4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 15 | Delaware4 | Midday | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 16 | Indiana4 | Midday | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 17 | NewYork4 | Combined | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 18 | NewYork4 | Midday | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |

Full per-row evaluation:
- `sharepacks/2025-06-21/control_center/profit_alerts_eval.csv`
