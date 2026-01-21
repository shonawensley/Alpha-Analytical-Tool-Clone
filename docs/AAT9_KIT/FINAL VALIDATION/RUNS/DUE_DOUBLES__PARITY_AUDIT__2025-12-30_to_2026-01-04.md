# Due Doubles — Parity Audit (2025-12-30 → 2026-01-04)

- Generated: `2026-01-21T08:58:50.373047+00:00`
- Predictive root (preferred): `sharepacks/_predictive`
- Post-results root (fallback): `sharepacks`
- Output CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DUE_DOUBLES__PARITY_AUDIT__2025-12-30_to_2026-01-04.csv`

## 1) Parity summary

- Rows audited: **252**
- DS mismatches: **0**
- Family invalid tokens: **0**
- Family unknown combos: **0**
- Family non-double combos: **0**
- Family severity mismatches: **0**
- Family unknown labels: **0**

Per-day notes (only non-OK rows shown):

## 2) Interpretable evaluation metrics (RUNS-only; results labels)

These are meant to prevent misreading low raw counts as a data bug.

### 2.1 Base rates

- Midday outcomes: **81**
- Evening outcomes: **82**
- Midday double+triple events: **22** (rate=0.2716)
- Evening double+triple events: **20** (rate=0.2439)

### 2.2 'Winner in due-doubles family' (strict membership)

- Midday any-type in-family: **4** / 81 (rate=0.0494)
- Evening any-type in-family: **3** / 82 (rate=0.0366)

- Midday double-only in-family: **4** / 22 (rate=0.1818)
- Evening double-only in-family: **3** / 20 (rate=0.1500)

### 2.3 'Most due' evaluation (DS ranking → next-day double events)

- TopK used: **5** states per day/period (ranked by `Draws Since Double`).
- Midday topK double events: **7** / 30 (rate=0.2333)
- Evening topK double events: **6** / 30 (rate=0.2000)

Interpretation:
- DS is a 'state due for any double' indicator; family membership is a stricter 'which double' indicator.
- Family membership should be interpreted mainly on double/triple winners (conditional rate above).
