# Day Synthesis — D=2025-06-21 (H=2025-06-20)

Scope
- Results date (D): `2025-06-21`
- History workbook date (H): `2025-06-20` (D-1)
- States (14): Connecticut4, Delaware4, Florida4, Indiana4, Michigan4, NewJersey4, NewYork4, NorthCarolina4, Ohio4, OntarioCanada4, Pennsylvania4, PuertoRico4, SouthCarolina4, Virginia4
- Outcomes: Midday + Evening (Combined is a lens only; used for cross-variant structure and tags)

Sources
- Sharepack day root: `sharepacks/2025-06-21/README.md`
- Run reports (per-state): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__<STATE>.md`
- Results file: `data/results/2025-06-21.txt`

---

## Executive Summary

- This day includes both strong “positive control” environments (clean convergence) and clear negative controls (high heat but off-winner). That is great for early superbrain learning because it forces you to separate “tool ran” vs “tool actually isolated”.
- Strong/clean examples worth revisiting later as calibration anchors: `Ohio4` (strong, especially Evening), `Delaware4` (strong Evening), `Connecticut4` Midday.
- Clear negative-control examples (heavy dominant lanes but not winner-aligned): `Virginia4`, `NewYork4` Midday, and `Florida4` (winners are covered post-hoc, but the environment is broadly noisy/off-board relative to the strongest clusters).

---

## Verdict Distribution (Part A “Environment verdict”, distilled)

- Strong: `Delaware4`, `Ohio4`
- Support (but often draw-split): `Connecticut4`, `Michigan4`, `Indiana4` (Midday stronger), `OntarioCanada4` (high persistence pressure but winners manifest via perm lanes, not clean literals)
- Mixed / cross-variant / weak-to-moderate: `NewJersey4`, `Pennsylvania4`, `NorthCarolina4`, `PuertoRico4`, `SouthCarolina4`
- Weak/noisy: `Florida4`, `NewYork4`, `Virginia4`

---

## Drivers (day-level pattern)

Common “win narratives” that repeat across states on this day:
- Cross-tool convergence on a VTRAC family/canonical anchor can be very clean (ex: `Connecticut4` Midday; `Ohio4` Evening).
- Cross-variant visibility matters: several winners show meaningful tags in a different variant than the draw they hit (log this for later scoring design; do not assume “Midday signals only hit Midday”).
- There are real “dominant-lane miss” days: multiple states show a loud dominant cluster that is not the winner. Treat these as negative controls when later tuning gates (avoid overfitting).

---

## Pack Translation Snapshot (Part 5 “Pack vs winners”, quick map)

Note: post-hoc translation answers “would a small canonical box have hit?”, not “was it identifiable pre-results?”

- `Connecticut4`: Midday 950 (canon 059) box `059`; Evening 155 box `155` (low-confidence environment for Evening).
- `Delaware4`: Midday 756 box `567`; Evening 989 box `899`.
- `Florida4`: Midday 927 (canon 279) covered via boxed `279`; Evening 120 (canon 012) covered via boxed `012` (environment is noisy/off-board).
- `Indiana4`: Midday 565 box `556`; Evening 135 was skipped as low-confidence.
- `Michigan4`: Midday 432 box `234`; Evening 280 (canon 028) box `028` (leading zero handling matters).
- `NewJersey4`: Midday 182 box `128`; Evening 554 box `455`.
- `NewYork4`: Midday 802 (canon 028) not covered (skip); Evening 602 (canon 026) captured via VT-boxed family hedge (idx7).
- `NorthCarolina4`: Midday 427 box `247`; Evening 397 box `379` (evidence weak).
- `Ohio4`: Midday 069 box `069`; Evening 868 box `688`.
- `OntarioCanada4`: Midday 678 box `678`; Evening 517 box `157` (perm-lane vs literal issue is central here).
- `Pennsylvania4`: Midday 667 box `667`; Evening 360 (canon 036) box `036` (evidence weak).
- `PuertoRico4`: Midday 910 box `019`; Evening 551 box `155` (hedge hits despite weak evidence).
- `SouthCarolina4`: Midday 069 box `069`; Evening 847 (canon 478) box `478` (evidence weak).
- `Virginia4`: skipped (dominant clusters were not winner-aligned).

---

## Fix-later / anomalies (high signal, day-specific)

- `PuertoRico4`: DR Combined overlay winner stamp mismatch noted in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__PuertoRico4.md`.
- `Virginia4`: DR Midday overlay emptiness noted in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Virginia4.md`.

