# Due Doubles — Parity Audit (2026-01-05 → 2026-01-09)

- Generated: `2026-01-23T06:27:15.488832+00:00`
- Predictive root (preferred): `sharepacks/_predictive`
- Post-results root (fallback): `sharepacks`
- Output CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DUE_DOUBLES__PARITY_AUDIT__2026-01-05_to_2026-01-09.csv`

## 1) Parity summary

- Rows audited: **210**
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

- Midday outcomes: **69**
- Evening outcomes: **69**
- Midday double+triple events: **19** (rate=0.2754)
- Evening double+triple events: **24** (rate=0.3478)
- Midday mirror-double events: **17** (rate=0.2464)
- Evening mirror-double events: **14** (rate=0.2029)
- Midday doubleish (double/triple/mirror) events: **36** (rate=0.5217)
- Evening doubleish (double/triple/mirror) events: **38** (rate=0.5507)

### 2.2 'Winner in due-doubles family' (strict membership)

- Midday any-type in-family: **2** / 69 (rate=0.0290)
- Evening any-type in-family: **7** / 69 (rate=0.1014)

- Midday double-only in-family: **2** / 19 (rate=0.1053)
- Evening double-only in-family: **7** / 24 (rate=0.2917)

### 2.3 VTRAC-lane credit (includes mirror-double conversions)

- Midday any-type VTRAC-in-family: **9** / 69 (rate=0.1304)
- Evening any-type VTRAC-in-family: **19** / 69 (rate=0.2754)

- Midday mirror-double VTRAC-in-family: **4** / 17 (rate=0.2353)
- Evening mirror-double VTRAC-in-family: **5** / 14 (rate=0.3571)

- Midday doubleish VTRAC-in-family: **9** / 36 (rate=0.2500)
- Evening doubleish VTRAC-in-family: **19** / 38 (rate=0.5000)

### 2.4 'Most due' evaluation (DS ranking → next-day double events)

- TopK used: **5** states per day/period (ranked by `Draws Since Double`).
- Midday topK double events: **4** / 25 (rate=0.1600)
- Evening topK double events: **9** / 25 (rate=0.3600)
- Midday topK doubleish events: **10** / 25 (rate=0.4000)
- Evening topK doubleish events: **15** / 25 (rate=0.6000)

Interpretation:
- DS is a 'state due for any double' indicator; family membership is a stricter 'which double' indicator.
- Family membership should be interpreted mainly on double/triple winners (conditional rate above).
- If you treat mirror-double outcomes as 'due-doubles conversions', use the doubleish and VTRAC-lane sections.
