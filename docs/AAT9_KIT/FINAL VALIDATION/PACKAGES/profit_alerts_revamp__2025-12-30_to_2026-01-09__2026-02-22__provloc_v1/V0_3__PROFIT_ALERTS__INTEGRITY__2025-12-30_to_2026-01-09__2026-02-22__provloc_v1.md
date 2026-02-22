# Profit Alerts Integrity — 2025-12-30 → 2026-01-09

Label: `provloc_v1`

Purpose: summarize evaluation integrity signals (coverage + evidence wiring) before any tuning.

## Coverage

- Dates in range: **11**
- Dates with `profit_alerts_eval.csv`: **11**
- Missing eval dates: **0**

## Totals

- Total rows: **721**
- Candidate rows: **543**
- Promoter rows: **139**

- Evidence OK (all rows): Y=721, N=0 (Y rate: 100.0%)
- Stable contains canonical (candidates): Y=493, N=0, ?=0, -=50 (measured: 493/543, Y rate: 100.0%)
- Candidate canonical invalid (canonical-required alerts only): **0/530** (0.0%)
- Candidate implied_set_size missing: **0/543** (0.0%)
- Candidate implied_set_size mismatches (vs expected for suggested kind): **0/543** (0.0%)

## Per-day quick stats

| date | rows | candidates | promoters | evidence_ok_Y | evidence_ok_N | stable_contains_Y | stable_contains_N |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2025-12-30 | 72 | 53 | 15 | 72 | 0 | 49 | 0 |
| 2025-12-31 | 69 | 53 | 14 | 69 | 0 | 48 | 0 |
| 2026-01-01 | 70 | 54 | 12 | 70 | 0 | 48 | 0 |
| 2026-01-02 | 64 | 46 | 16 | 64 | 0 | 42 | 0 |
| 2026-01-03 | 66 | 51 | 11 | 66 | 0 | 45 | 0 |
| 2026-01-04 | 67 | 52 | 11 | 67 | 0 | 46 | 0 |
| 2026-01-05 | 12 | 7 | 4 | 12 | 0 | 4 | 0 |
| 2026-01-06 | 72 | 55 | 12 | 72 | 0 | 52 | 0 |
| 2026-01-07 | 76 | 58 | 15 | 76 | 0 | 54 | 0 |
| 2026-01-08 | 70 | 53 | 13 | 70 | 0 | 49 | 0 |
| 2026-01-09 | 83 | 61 | 16 | 83 | 0 | 56 | 0 |

## Evidence errors (top)

- None.

## Candidate set-size mismatches (by suggested kind)

- None.

## Stable containment misses (by alert_id)

| alert_id | stable_contains_Y | stable_contains_N | N_rate |
|---|---:|---:|---:|
| A01 | 80 | 0 | 0.0% |
| A02 | 69 | 0 | 0.0% |
| A04 | 142 | 0 | 0.0% |
| A05 | 141 | 0 | 0.0% |
| A07 | 1 | 0 | 0.0% |
| A12 | 60 | 0 | 0.0% |

## Notes

- `evidence_ok=N` means the evaluator could not load the required evidence row(s) to grade the alert row; inspect `evidence_error` for the reason.
- `stable_contains_canonical=N` means the canonical 3-digit did not appear in Stable’s exported scored rows for that state/day/variant; this can be legitimate (signal disagreement) or a wiring issue.
- `implied_set_size` is sanity-checked against suggested kinds:
  - BOX expects full perms (6/3/1 depending on unique digits in canonical).
  - STR8_3 expects min(3, perms) (so triples can legitimately be 1).
  - STR8_8 expects 8, STR8_4of8 expects 4, OVERLAY/SKIP expect 0.
