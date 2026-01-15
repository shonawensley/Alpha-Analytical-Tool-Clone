# Stable (String Tables) — v0 Audit (Cases)

Purpose: pick a small number of **high-signal Stable cases** to understand *why* Stable is frequently an index/lane lens but rarely an exact top-caller in v0, and what that implies for v0.2/v0.3.

Scope guardrails:
- No analyzer changes (Stable/DR/VTRAC/HZ).
- Profit Alerts quarantined (use `--profile tool_only` as baseline).

Companion quant:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__QUANT.md`

---

## How to review one case (repeatable checklist)

For each case below:
1) Open the Master Validation run report:
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`
2) Stable evidence (post-results summary; rank fractions + gaps):
   - `sharepacks/<D>/<STATE>/stable/<STATE>/summary.json`
3) Stable scores evidence (predictive snapshot; what `stable_top` ingests):
   - `sharepacks/_predictive/<D>/<STATE>/stable/<STATE>/<STATE>_stable_patterns_scores.csv`
4) Predictive artifacts (so we can compare “before” → “after”):
   - `sharepacks/_predictive/<D>/<STATE>/candidate_universe.json`
   - `sharepacks/_predictive/<D>/<STATE>/play_card.json`
5) Winners quick scan:
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__WINNERS_DIGEST.md`

Key questions:
- Is the winner canonical present in Stable scores at all? If yes, how far down (canonical-rank, not row-rank)?
- Is Stable “right about the index” even when wrong about the canonical?
- Is this an environment issue (winners lens col1/2 silent), or a Stable scoring/consumption issue?

---

## A) Direct hits (Stable top‑3 canonicals)

These are the only cases in the v0 window where the winner canonical lands in Stable’s top‑3 canonicals in at least one section (Combined/Midday/Evening) and therefore `stable_top` hits.

| D | State | Outcome | Winner | Canon | VTRAC idx | Winner min canonical-rank | Best section |
|---|---|---|---:|---:|---:|---:|---|
| 2026-01-05 | NewYork4 | Midday | 080 | 008 | 4 | 1 | Evening |
| 2026-01-08 | NewJersey4 | Midday | 089 | 089 | 14 | 1 | Midday |

---

## B) Near misses (rank 4–10)

These cases are “almost Stable hits”: the winner canonical is ranked 4–10 in at least one section. These are high‑signal for v0.2/v0.3 decisions because they show Stable scoring is *close*.

| D | State | Outcome | Winner | Canon | VTRAC idx | Winner min canonical-rank | Best section |
|---|---|---|---:|---:|---:|---:|---|
| 2026-01-09 | Pennsylvania4 | Midday | 811 | 118 | 18 | 4 | Evening |
| 2026-01-06 | Michigan4 | Midday | 618 | 168 | 18 | 6 | Combined |
| 2026-01-07 | Florida4 | Midday | 434 | 344 | 34 | 7 | Combined |
| 2026-01-09 | Delaware4 | Midday | 843 | 348 | 33 | 8 | Midday |
| 2026-01-07 | Indiana4 | Evening | 290 | 029 | 12 | 10 | Midday |
| 2026-01-08 | NewJersey4 | Evening | 055 | 055 | 1 | 10 | Evening |

---

## C) “Index hit → box miss” queue (top Stable lane cases)

These are cases where Stable’s **top‑3 canonicals** include the correct `vtrac_index` family (lane hit), but not the exact canonical (box miss). This is the class of failure we want to convert via bounded closures.

| D | State | Outcome | Winner | Canon | VTRAC idx | Winner min canonical-rank | Best section |
|---|---|---|---:|---:|---:|---:|---|
| 2026-01-06 | Michigan4 | Midday | 618 | 168 | 18 | 6 | Combined |
| 2026-01-09 | Delaware4 | Midday | 843 | 348 | 33 | 8 | Midday |
| 2026-01-09 | NewJersey4 | Midday | 287 | 278 | 27 | 16 | Evening |
| 2026-01-09 | Pennsylvania4 | Evening | 014 | 014 | 9 | 17 | Evening |
| 2026-01-08 | Florida4 | Midday | 429 | 249 | 31 | 19 | Midday |
| 2026-01-05 | Virginia4 | Midday | 473 | 347 | 30 | 24 | Midday |
| 2026-01-09 | NewJersey4 | Evening | 028 | 028 | 11 | 26 | Evening |
| 2026-01-07 | Florida4 | Evening | 963 | 369 | 24 | 31 | Midday |
| 2026-01-07 | Pennsylvania4 | Midday | 060 | 006 | 2 | 33 | Midday |
| 2026-01-05 | OntarioCanada4 | Evening | 797 | 779 | 28 | 37 | Evening |

Next step: for each row above, compare:
- Stable top canonicals’ indices vs the winner index (lane correctness),
- Candidate Universe pack votes (`CU top support`) and whether any bounded closure pack could have converted this to a box hit,
- winners lens environment (Set1 col1/2 density) to filter out “low-signal lane hits”.

