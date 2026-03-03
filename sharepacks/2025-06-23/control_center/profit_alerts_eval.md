# Profit Alerts Evaluation — 2025-06-23

- Generated: `2026-03-03T08:01:09.889395+00:00`
- Inputs:
  - `sharepacks/2025-06-23/control_center/profit_alerts.csv`
  - `data/results/*.txt` (local only)
- Charter: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`

## Integrity summary
- rows_total: `88`
- evidence_parse_errors: `0`
- non_3digit_canonical: `0`
- missing_results_state (state not found on D): `0`
- stable_scores_missing (per-state Stable scores missing/unreadable): `0`
- stable_candidate_missing (canonical not found in Stable scores section): `0`

## Scorecard (variant-faithful lens, by AlertId)
| AlertId | Fired | HIT(decay) | EXPIRED | CENSORED | HIT<=7 | HIT<=14 | mean t_hit |
|---:|---:|---:|---:|---:|---:|---:|---:|
| A01 | 13 | 0 | 13 | 0 | 0 | 0 | - |
| A02 | 10 | 0 | 10 | 0 | 0 | 0 | - |
| A04 | 14 | 0 | 14 | 0 | 0 | 0 | - |
| A05 | 14 | 0 | 14 | 0 | 1 | 1 | - |
| A09 | 1 | 0 | 1 | 0 | 0 | 0 | - |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 | - |
| A11:S2 | 7 | 0 | 7 | 0 | 1 | 1 | - |
| A12 | 5 | 0 | 5 | 0 | 0 | 0 | - |

Promoters fired (not gradeable as winner hits):
- A03: 2
- A08: 19

## Scorecard (any-outcome lens, by AlertId)

For `Midday` / `Evening` variant rows, this counts a hit if the episode resolves on either `Midday` or `Evening` within the same time-span boundary as the variant-faithful window.

| AlertId | Fired | HIT_any(decay) | EXPIRED_any | CENSORED_any | HIT_any<=7 | HIT_any<=14 |
|---:|---:|---:|---:|---:|---:|---:|
| A01 | 13 | 0 | 13 | 0 | 0 | 0 |
| A02 | 10 | 0 | 10 | 0 | 0 | 0 |
| A04 | 14 | 0 | 14 | 0 | 0 | 0 |
| A05 | 14 | 0 | 14 | 0 | 1 | 2 |
| A09 | 1 | 0 | 1 | 0 | 0 | 1 |
| A10 | 3 | 0 | 3 | 0 | 0 | 0 |
| A11:S2 | 7 | 0 | 7 | 0 | 1 | 1 |
| A12 | 5 | 0 | 5 | 0 | 0 | 0 |

## Merged episodes (deduped play-sets)

This view dedupes rows that imply the same concrete play-set (same `StateKey × Variant × implied_set`) so co-firing alerts do not get double-counted.

- merged_rows_total: `55`

| StateKey | Variant | Strength | Alerts | Promoters | DecayMax | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen |
|---|---|---:|---|---|---:|---|---:|---|---|---|---|---|---|
| Connecticut4 | Combined | 5 | A02,A11 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Indiana4 | Combined | 5 | A11 | A03 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Michigan4 | Combined | 5 | A11 | A03,A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Ohio4 | Combined | 5 | A02,A11 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Pennsylvania4 | Combined | 5 | A11 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| PuertoRico4 | Combined | 5 | A01,A04,A11 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| SouthCarolina4 | Combined | 5 | A11 | - | 2 | EXPIRED | - | - | - | Y | Y | N | - |
| Connecticut4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Delaware4 | Midday | 4 | A02,A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Florida4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Florida4 | Evening | 4 | A04 | A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Indiana4 | Evening | 4 | A05 | A03 | 2 | EXPIRED | - | - | - | N | N | N | - |
| Indiana4 | Evening | 4 | A01,A04 | A03 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Indiana4 | Midday | 4 | A01 | A03 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Michigan4 | Combined | 4 | A04 | A03,A08 | 3 | EXPIRED | - | - | - | N | N | N | - |
| Michigan4 | Midday | 4 | A02,A05 | A03,A08 | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewJersey4 | Evening | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| NewYork4 | Combined | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | Y | Y | N | - |
| NorthCarolina4 | Combined | 4 | A10 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| NorthCarolina4 | Midday | 4 | A01,A04 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| NorthCarolina4 | Midday | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Ohio4 | Midday | 4 | A05 | - | 2 | EXPIRED | - | - | - | N | N | N | - |
| Ohio4 | Midday | 4 | A01 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| Ohio4 | Midday | 4 | A01,A04 | - | 3 | EXPIRED | - | - | - | N | N | N | - |
| OntarioCanada4 | Evening | 4 | A05 | A08 | 2 | EXPIRED | - | - | - | N | N | N | - |

Full merged evaluation:
- `sharepacks/2025-06-23/control_center/profit_alerts_eval_merged.csv`

## Top episodes (by Strength, then earliest hit)

| # | StateKey | Variant | AlertId | Strength | Suggested | Decay | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen | Strict |
|---:|---|---|---|---:|---|---:|---|---:|---|---|---|---|---|---|---|
| 77 | Connecticut4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 78 | Indiana4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 79 | Michigan4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 80 | Ohio4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 81 | Pennsylvania4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 82 | PuertoRico4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 83 | SouthCarolina4 | Combined | A11 | 5 | BOX | 2 | EXPIRED | - | - | - | Y | Y | N | - | N |
| 1 | Indiana4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 2 | Indiana4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 3 | NorthCarolina4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 4 | Ohio4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 5 | Ohio4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 6 | OntarioCanada4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 7 | Pennsylvania4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 8 | Pennsylvania4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 9 | PuertoRico4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 10 | PuertoRico4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 11 | PuertoRico4 | Midday | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 12 | SouthCarolina4 | Combined | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 13 | SouthCarolina4 | Evening | A01 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 14 | SouthCarolina4 | Evening | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 15 | Virginia4 | Evening | A02 | 4 | STR8_3 | 2 | EXPIRED | - | - | - | N | N | N | - | N |
| 26 | Florida4 | Evening | A04 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 27 | Michigan4 | Combined | A04 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |
| 28 | Virginia4 | Combined | A04 | 4 | BOX | 3 | EXPIRED | - | - | - | N | N | N | - | N |

Full per-row evaluation:
- `sharepacks/2025-06-23/control_center/profit_alerts_eval.csv`
