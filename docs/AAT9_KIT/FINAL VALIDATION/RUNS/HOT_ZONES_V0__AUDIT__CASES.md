# Hot Zones — v0 Audit (Cases)

Purpose: pick a small number of **high-signal Hot Zones cases** to understand:
- why Hot Zones rarely hits as a strict straight caller in v0, and
- whether Hot Zones is better treated as a canonical/BOX contributor or an index/lane lens.

Scope guardrails:
- No analyzer changes (Stable/DR/VTRAC/HZ).
- Profit Alerts quarantined (use `--profile tool_only` as baseline).

Companion quant:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__QUANT.md`

---

## How to review one case (repeatable checklist)

For each case below:
1) Open the Master Validation run report:
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`
2) Hot Zones post-results summary (winner placement + notes):
   - `sharepacks/<D>/<STATE>/hot_zones/<STATE>/summary.json`
3) Predictive triads (what `hot_zones_top` ingests):
   - `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<D>_hot_zones_winner_map.json`
4) Predictive artifacts (so we can compare “before” → “after”):
   - `sharepacks/_predictive/<D>/<STATE>/candidate_universe__tool_only.json`
   - `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only.json`
5) Winners quick scan:
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__WINNERS_DIGEST.md`

Key questions:
- Did Hot Zones place the literal winner anywhere near the top of `top_lanes` (rank fraction)?
- Is the winner absent only because we’re consuming **top20 triads** (not full lanes)?
- Would BOX-equivalent canonicalization have converted this into a hit?
- Is Hot Zones “right about the index” even when wrong about the straight?

---

## A) Direct hits (Hot Zones top‑8 straights)

These are the only cases in the v0 window where the literal winner appears in Hot Zones’ top‑8 triads (straight hit).

| D | State | Outcome | Winner | Canon | Winner triad rank |
|---|---|---|---:|---:|---:|
| 2026-01-09 | Pennsylvania4 | Evening | 014 | 014 | 6 |

---

## B) Near misses (winner in top‑20 triads, not top‑8)

These show sensitivity to `top_n` without changing the underlying tool output.

| D | State | Outcome | Winner | Canon | Winner triad rank |
|---|---|---|---:|---:|---:|
| 2026-01-08 | NewJersey4 | Midday | 089 | 089 | 12 |

---

## C) Canonical-only hits (BOX-equivalent would have hit)

In these cases, Hot Zones surfaced a triad that shares the winner’s canonical, but not the literal permutation.

This is evidence that Hot Zones is often “right about the box” even when it misses as a straight caller.

| D | State | Outcome | Winner | Canon | Hot Zones triad(s) in top‑8 |
|---|---|---|---:|---:|---|
| 2026-01-07 | Pennsylvania4 | Midday | 060 | 006 | 006 |
| 2026-01-08 | Ohio4 | Evening | 580 | 058 | 058 |
| 2026-01-09 | Michigan4 | Midday | 842 | 248 | 248 |

---

## D) Index-hit → box-miss queue (top‑12 triads)

These are the “Hot Zones lane correctness” cases: the winner’s VTRAC index is present among the indices implied by Hot Zones’ top‑12 triads, but the winner canonical is not.

This is exactly the class of failure we want to convert via bounded closures (selection-layer rules), not by changing the analyzer.

Start with these (first 10 from the v0 window):

| D | State | Outcome | Winner | Canon | VTRAC idx |
|---|---|---|---:|---:|---:|
| 2026-01-05 | Indiana4 | Evening | 629 | 269 | 22 |
| 2026-01-05 | NorthCarolina4 | Midday | 553 | 355 | 4 |
| 2026-01-05 | OntarioCanada4 | Evening | 797 | 779 | 28 |
| 2026-01-05 | Pennsylvania4 | Evening | 600 | 006 | 2 |
| 2026-01-05 | SouthCarolina4 | Evening | 712 | 127 | 20 |
| 2026-01-05 | Virginia4 | Midday | 473 | 347 | 30 |
| 2026-01-06 | Connecticut4 | Midday | 576 | 567 | 7 |
| 2026-01-06 | Connecticut4 | Evening | 737 | 377 | 27 |
| 2026-01-06 | Michigan4 | Evening | 578 | 578 | 11 |
| 2026-01-06 | NorthCarolina4 | Evening | 298 | 289 | 30 |

Next step: for each row, compare:
- Hot Zones triads’ implied indices vs winner index (lane correctness),
- Candidate Universe pack votes (`CU top support`) and whether any bounded closure pack could have converted this to a box hit,
- winners lens environment (col1/2 density) to filter out low-signal environments.

