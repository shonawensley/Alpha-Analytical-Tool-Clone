# Due Doubles — Parity Audit (2025-06-21 → 2025-06-23)

- Generated: `2026-01-21T08:58:51.240886+00:00`
- Predictive root (preferred): `sharepacks/_predictive`
- Post-results root (fallback): `sharepacks`
- Output CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DUE_DOUBLES__PARITY_AUDIT__2025-06-21_to_2025-06-23.csv`

## 1) Parity summary

- Rows audited: **126**
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

- Midday outcomes: **40**
- Evening outcomes: **41**
- Midday double+triple events: **9** (rate=0.2250)
- Evening double+triple events: **13** (rate=0.3171)

### 2.2 'Winner in due-doubles family' (strict membership)

- Midday any-type in-family: **2** / 40 (rate=0.0500)
- Evening any-type in-family: **3** / 41 (rate=0.0732)

- Midday double-only in-family: **2** / 9 (rate=0.2222)
- Evening double-only in-family: **3** / 13 (rate=0.2308)

### 2.3 'Most due' evaluation (DS ranking → next-day double events)

- TopK used: **5** states per day/period (ranked by `Draws Since Double`).
- Midday topK double events: **3** / 15 (rate=0.2000)
- Evening topK double events: **3** / 15 (rate=0.2000)

Interpretation:
- DS is a 'state due for any double' indicator; family membership is a stricter 'which double' indicator.
- Family membership should be interpreted mainly on double/triple winners (conditional rate above).
