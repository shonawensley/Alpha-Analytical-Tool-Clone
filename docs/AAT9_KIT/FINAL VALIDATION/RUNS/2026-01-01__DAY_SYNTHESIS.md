# Day Synthesis — D=2026-01-01 (H=2025-12-31)

Scope
- Results date (D): `2026-01-01`
- History workbook date (H): `2025-12-31` (usually D-1)
- States (14): Connecticut4, Delaware4, Florida4, Indiana4, Michigan4, NewJersey4, NewYork4, NorthCarolina4, Ohio4, OntarioCanada4, Pennsylvania4, PuertoRico4, SouthCarolina4, Virginia4
- Outcomes: Midday + Evening (Combined is a lens only; used for cross-variant structure and tags)

Sources
- Sharepack day root: `sharepacks/2026-01-01/README.md`
- Control Center portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__CONTROL_CENTER.md`
- Run reports (per-state): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__<STATE>.md`
- Results file: `data/results/2026-01-01.txt`

---

## Executive Summary

- Day-level synthesis is intentionally conservative (avoid overfitting).
- Use this doc to classify environment types and log cross-state patterns you notice during review.

## Verdict Distribution (Part A “Environment verdict”, distilled)

- Strong: `Delaware4`, `Indiana4`, `NewYork4`, `NorthCarolina4`, `Ohio4`, `OntarioCanada4`, `Pennsylvania4`, `SouthCarolina4`, `Virginia4`
- Support: `Connecticut4`, `Florida4`, `Michigan4`, `NewJersey4`
- Mixed/Other: `PuertoRico4`

## Pack Translation Snapshot (Part 5 “Pack vs winners”, quick map)

- `Connecticut4`: Midday 228 → BOX `228`; Evening 109 → BOX `019`.
- `Delaware4`: Midday 149 → BOX `149`; Evening 937 → BOX `379`.
- `Florida4`: Midday 195 → BOX `159`; Evening 291 → BOX `129`.
- `Indiana4`: Midday 474 → BOX `447`; Evening 909 → BOX `099`.
- `Michigan4`: Midday 032 → BOX `023`; Evening 204 → BOX `024`.
- `NewJersey4`: Midday 770 → BOX `077`; Evening 504 → BOX `045`.
- `NewYork4`: Midday 117 → BOX `117`; Evening 174 → BOX `147`.
- `NorthCarolina4`: Midday 416 → BOX `146`; Evening 053 → BOX `035`.
- `Ohio4`: Midday 746 → BOX `467`; Evening 416 → BOX `146`.
- `OntarioCanada4`: Midday 528 → BOX `258`; Evening 546 → BOX `456`.
- `Pennsylvania4`: Midday 322 → BOX `223`; Evening 328 → BOX `238`.
- `PuertoRico4`: Midday: Midday: no winner in results file (expected on some days).; Evening: Evening: no winner in results file (expected on some days)..
- `SouthCarolina4`: Midday 910 → BOX `019`; Evening 821 → BOX `128`.
- `Virginia4`: Midday 019 → BOX `019`; Evening 354 → BOX `345`.

## Fix-later / anomalies (day-specific)

- (Add anything that looks repeatable or suspicious, with links to the state run reports.)
