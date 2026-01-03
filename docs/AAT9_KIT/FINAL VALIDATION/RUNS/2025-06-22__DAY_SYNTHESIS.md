# Day Synthesis — D=2025-06-22 (H=2025-06-21)

Scope
- Results date (D): `2025-06-22`
- History workbook date (H): `2025-06-21` (D-1)
- States (14): Connecticut4, Delaware4, Florida4, Indiana4, Michigan4, NewJersey4, NewYork4, NorthCarolina4, Ohio4, OntarioCanada4, Pennsylvania4, PuertoRico4, SouthCarolina4, Virginia4
- Outcomes: Midday + Evening (Combined is a lens only; used for cross-variant structure and tags)

Sources
- Sharepack day root: `sharepacks/2025-06-22/README.md`
- Run reports (per-state): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__<STATE>.md`
- Results file: `data/results/2025-06-22.txt`

---

## Executive Summary

- This is a heavier “negative-control” day than 2025-06-21 or 2025-06-23: many states are split/low-confidence and multiple reports explicitly recommend pass/tiny hedges rather than confident packs.
- Two non-negotiable grading constraints on this date:
  - `PuertoRico4`: no results present in `data/results/2025-06-22.txt` (environment-only; do not grade hits/misses).
  - `SouthCarolina4`: one-winner day (results file is missing one period), so any post-hoc grading must treat the missing period as N/A (not a miss).

---

## Verdict Distribution (Part A “Environment verdict”, distilled)

- Split (mixed confidence by draw): `NewJersey4`, `NorthCarolina4`, `Ohio4`, `Virginia4`
- Pass / tiny hedge posture called out explicitly: `OntarioCanada4`, `SouthCarolina4`
- Weak/noisy / low-confidence: `Connecticut4`, `Delaware4`, `NewYork4`, `Michigan4` (and several other states where dominant lanes did not isolate winners)
- Supportive-but-noisy: `Florida4` (good example of “it can cover post-hoc, but the dominant board narrative is not a clean caller”)

---

## Drivers (day-level pattern)

Day-level themes that repeat across states:
- “Dominant lane miss” is common: Stable/DR/Hot Zones can converge strongly on a compact universe that is not the winner. Treat these states as negative controls when later tuning gates (do not overfit to the loudest lane).
- Stable exact-hit can rescue a day even when other tools narrate a different dominant universe (ex: `Indiana4`).
- VT-straight / VT-boxed hedges are often the only defensible “cheap family coverage” posture when the environment is noisy and the winner is off-board.

---

## Pack Translation Snapshot (Part 5 “Pack vs winners”, quick map)

Note: post-hoc translation answers “would a small hedge have hit?”, not “was it identifiable pre-results?”

- `Connecticut4`: VT-straight hedges on winner indices (idx21/idx13) would cover both winners; dominant-lane boxes would not.
- `Delaware4`: dominant-lane approach would miss; VT-straight hedges keyed off winner indices (idx31/idx20) would capture but evidence was only moderate.
- `Florida4`: Midday boxed `033` covers 330; Evening VT-boxed idx31 covers 924 (good example of “family hedge works even when the board is noisy”).
- `Indiana4`: Stable-led small-box approach (canon 147 + canon 027) would hit both; dominant DR/Hot Zones lanes would likely miss.
- `Michigan4`: Evening box `007` would hit 700; Midday treated as low-confidence despite Stable exact.
- `NewJersey4`: Evening box `788` would hit 887; Midday treated as low-confidence.
- `NewYork4`: Midday treated as miss (no credible isolation); Evening tiny box `689` would hit 968.
- `NorthCarolina4`: Midday box `567` would hit 765; Evening box `135` would hit 153.
- `Ohio4`: Midday treated as miss; Evening box `199` would hit 199.
- `OntarioCanada4`: dominant board pack would miss; post-hoc minimal “winner capture” would be boxed `189` and `166`, but evidence was weak.
- `Pennsylvania4`: Midday box `389` would hit 398; Evening has no strong isolation (tiny `057` box would hit post-hoc but low confidence).
- `PuertoRico4`: N/A (no winners in results file for this D).
- `SouthCarolina4`: N/A for missing period; the recorded winner is off-board and not isolated (expected miss under convergence-only posture).
- `Virginia4`: Midday no recommended pack; Evening box `389` would hit 938.

---

## Fix-later / anomalies (high signal, day-specific)

- Missing-results handling:
  - `PuertoRico4`: missing results; consider auto-marking as “N/A: results missing” in future syntheses.
  - `SouthCarolina4`: one-winner day; missing period should be treated as N/A.
- Tool output hygiene (logged in state reports):
  - `Pennsylvania4`: DR Combined winner mapping anomaly.
  - `OntarioCanada4`: DR Evening overlay missing flags/hits for the winner.
  - `Ohio4`: winners generator produced a `nan**` lane string (winners-lens hygiene).

