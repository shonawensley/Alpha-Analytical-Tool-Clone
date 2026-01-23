# Due Doubles — Parity Audit (2025-06-21 → 2025-06-23)

- Generated: `2026-01-23T06:27:13.229141+00:00`
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
- Midday mirror-double events: **7** (rate=0.1750)
- Evening mirror-double events: **12** (rate=0.2927)
- Midday doubleish (double/triple/mirror) events: **16** (rate=0.4000)
- Evening doubleish (double/triple/mirror) events: **25** (rate=0.6098)

### 2.2 'Winner in due-doubles family' (strict membership)

- Midday any-type in-family: **2** / 40 (rate=0.0500)
- Evening any-type in-family: **3** / 41 (rate=0.0732)

- Midday double-only in-family: **2** / 9 (rate=0.2222)
- Evening double-only in-family: **3** / 13 (rate=0.2308)

### 2.3 VTRAC-lane credit (includes mirror-double conversions)

- Midday any-type VTRAC-in-family: **7** / 40 (rate=0.1750)
- Evening any-type VTRAC-in-family: **7** / 41 (rate=0.1707)

- Midday mirror-double VTRAC-in-family: **3** / 7 (rate=0.4286)
- Evening mirror-double VTRAC-in-family: **4** / 12 (rate=0.3333)

- Midday doubleish VTRAC-in-family: **7** / 16 (rate=0.4375)
- Evening doubleish VTRAC-in-family: **7** / 25 (rate=0.2800)

### 2.4 'Most due' evaluation (DS ranking → next-day double events)

- TopK used: **5** states per day/period (ranked by `Draws Since Double`).
- Midday topK double events: **3** / 15 (rate=0.2000)
- Evening topK double events: **3** / 15 (rate=0.2000)
- Midday topK doubleish events: **4** / 15 (rate=0.2667)
- Evening topK doubleish events: **5** / 15 (rate=0.3333)

Interpretation:
- DS is a 'state due for any double' indicator; family membership is a stricter 'which double' indicator.
- Family membership should be interpreted mainly on double/triple winners (conditional rate above).
- If you treat mirror-double outcomes as 'due-doubles conversions', use the doubleish and VTRAC-lane sections.
