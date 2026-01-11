# Day Synthesis — D=2026-01-06 (H=2026-01-05)

Scope
- Results date (D): `2026-01-06`
- History workbook date (H): `2026-01-05` (usually D-1)
- States (14): Connecticut4, Delaware4, Florida4, Indiana4, Michigan4, NewJersey4, NewYork4, NorthCarolina4, Ohio4, OntarioCanada4, Pennsylvania4, PuertoRico4, SouthCarolina4, Virginia4
- Outcomes: Midday + Evening (Combined is a lens only; used for cross-variant structure and tags)

Sources
- Sharepack day root: `sharepacks/2026-01-06/README.md`
- Control Center portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__CONTROL_CENTER.md`
- Run reports (per-state): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__<STATE>.md`
- Results file: `data/results/2026-01-06.txt`

---

## Executive Summary

- Day-level synthesis is intentionally conservative (avoid overfitting).
- Use this doc to classify environment types and log cross-state patterns you notice during review.

## Verdict Distribution (Part A “Environment verdict”, distilled)

- Strong: `Delaware4`, `NewJersey4`, `NewYork4`, `NorthCarolina4`, `Pennsylvania4`, `Virginia4`
- Support: `Indiana4`, `Michigan4`, `Ohio4`, `OntarioCanada4`, `SouthCarolina4`
- Mixed/Other: `PuertoRico4`
- Weak/Noisy: `Connecticut4`, `Florida4`

## Pack Translation Snapshot (Part 5 “Pack vs winners”, quick map)

- `Connecticut4`: Midday 576 → BOX `567`; Evening 737 → BOX `377`.
- `Delaware4`: Midday 165 → BOX `156`; Evening 758 → BOX `578`.
- `Florida4`: Midday 209 → BOX `029`; Evening: Evening: no winner in results file (expected on some days)..
- `Indiana4`: Midday 043 → BOX `034`; Evening 961 → BOX `169`.
- `Michigan4`: Midday 618 → BOX `168`; Evening 578 → BOX `578`.
- `NewJersey4`: Midday 865 → BOX `568`; Evening 942 → BOX `249`.
- `NewYork4`: Midday 181 → BOX `118`; Evening 342 → BOX `234`.
- `NorthCarolina4`: Midday 552 → BOX `255`; Evening 298 → BOX `289`.
- `Ohio4`: Midday 260 → BOX `026`; Evening 064 → BOX `046`.
- `OntarioCanada4`: Midday 111 → BOX `111`; Evening 433 → BOX `334`.
- `Pennsylvania4`: Midday 684 → BOX `468`; Evening 757 → BOX `577`.
- `PuertoRico4`: Midday: Midday: no winner in results file (expected on some days).; Evening: Evening: no winner in results file (expected on some days)..
- `SouthCarolina4`: Midday 586 → BOX `568`; Evening 412 → BOX `124`.
- `Virginia4`: Midday 820 → BOX `028`; Evening 958 → BOX `589`.

## Fix-later / anomalies (day-specific)

- (Add anything that looks repeatable or suspicious, with links to the state run reports.)
