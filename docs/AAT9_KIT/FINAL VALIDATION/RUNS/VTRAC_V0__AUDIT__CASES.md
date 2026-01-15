# VTRAC Enhanced — v0 Audit (Cases)

Purpose: pick a small number of **high-signal VTRAC cases** to understand:
- why VTRAC’s top‑N straights often miss as a direct caller, and
- how often VTRAC is “right about the index” (lane hit) even when it misses the canonical/straight.

Scope guardrails:
- No analyzer changes (Stable/DR/VTRAC/HZ).
- Profit Alerts quarantined (use `--profile tool_only` as baseline).

Companion quant:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__QUANT.md`

---

## How to review one case (repeatable checklist)

For each case below:
1) Open the Master Validation run report:
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`
2) VTRAC post-results summary (winner index placement):
   - `sharepacks/<D>/<STATE>/vtrac/<STATE>/summary.json`
3) Predictive enhanced bundle (what `vtrac_enhanced_top` ingests):
   - `sharepacks/_predictive/<D>/<STATE>/vtrac/<STATE>/<STATE>_vtrac_enhanced_*.json`
4) Predictive artifacts (so we can compare “before” → “after”):
   - `sharepacks/_predictive/<D>/<STATE>/candidate_universe__tool_only.json`
   - `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only.json`
5) Winners quick scan:
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__WINNERS_DIGEST.md`

Key questions:
- Did the winner’s **index** place high even when the winner’s literal straight didn’t?
- Is this an “index-hit → box-miss” case (convertible via bounded closure), or just noise?
- Would BOX-equivalent canonicalization of the top straights have converted this?

---

## A) Direct hits (VTRAC top‑8 straights)

These are the only cases in the v0 window where the literal winner appears in VTRAC’s top‑8 ranked straights (straight hit).

| D | State | Outcome | Winner | Canon | Winner straight rank |
|---|---|---|---:|---:|---:|
| 2026-01-07 | Florida4 | Evening | 963 | 369 | 4 |

---

## B) Near misses (winner in top‑20 straights, not top‑8)

| D | State | Outcome | Winner | Canon | Winner straight rank |
|---|---|---|---:|---:|---:|
| 2026-01-06 | NewJersey4 | Midday | 865 | 568 | 18 |

---

## C) Canonical-only hits (BOX-equivalent would have hit)

In these cases, VTRAC surfaced a straight that shares the winner’s canonical, but not the literal permutation.

| D | State | Outcome | Winner | Canon | VTRAC top‑8 straight(s) |
|---|---|---|---:|---:|---|
| 2026-01-08 | Delaware4 | Evening | 031 | 013 | 013 |

---

## D) Index-hit → box-miss queue (top‑12 straights)

These are “lane correctness” cases: the winner’s VTRAC index is present among the indices implied by VTRAC’s top‑12 straights, but the winner canonical is not.

Start with these (first 10 from the v0 window):

| D | State | Outcome | Winner | Canon | VTRAC idx |
|---|---|---|---:|---:|---:|
| 2026-01-05 | OntarioCanada4 | Evening | 797 | 779 | 28 |
| 2026-01-05 | Pennsylvania4 | Evening | 600 | 006 | 2 |
| 2026-01-05 | SouthCarolina4 | Evening | 712 | 127 | 20 |
| 2026-01-06 | SouthCarolina4 | Evening | 412 | 124 | 22 |
| 2026-01-06 | Virginia4 | Evening | 958 | 589 | 14 |
| 2026-01-07 | Florida4 | Midday | 434 | 344 | 34 |
| 2026-01-07 | Indiana4 | Evening | 290 | 029 | 12 |
| 2026-01-07 | Ohio4 | Evening | 204 | 024 | 12 |
| 2026-01-07 | Pennsylvania4 | Evening | 263 | 236 | 21 |
| 2026-01-08 | Delaware4 | Evening | 031 | 013 | 8 |

Next step: for each row, compare:
- winner index placement (`summary.json`) vs the pack’s implied index set (lane correctness),
- cross-pack convergence votes in Candidate Universe,
- whether a bounded closure rule (v0.2/v0.3) would have converted this into a box hit.

