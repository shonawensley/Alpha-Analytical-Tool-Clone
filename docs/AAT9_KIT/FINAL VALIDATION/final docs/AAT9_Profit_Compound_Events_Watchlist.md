# AAT9 Profit Compound Events — Watchlist (SSOT)

Purpose: define the **shadow-only** “compound co-fire watchlist” surface so we can quickly spot states/variants where **multiple Profit Alerts co-fire in historically meaningful ways**.

Scope / non-goals:
- This is **triage only** (Brain‑2). It does **not** auto-bet and does **not** feed Candidate Universe / Play Cards.
- It is derived from the frozen Profit Alerts board for a results day **D**:
  - `sharepacks/<D>/control_center/profit_alerts.csv`
- It optionally annotates rows using the merged evaluation artifact when present:
  - `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`

Outputs:
- `sharepacks/<D>/control_center/profit_compound_events.csv`
- `sharepacks/<D>/control_center/profit_compound_events.md`

Regenerate:
```bash
python3 scripts/tools/export_profit_compound_events.py --date <D>
```

---

## What a “compound event” row means

Each row is an **environment bucket**: `(StateKey, Variant)` for day **D**.

It collects:
- which **candidate** alert ids fired (A01/A02/A04/A05/A06/A07/A09/A10/A11/A12)
- which **promoter** alert ids fired (A03/A08)
- A11 star severity (if present)
- A12 clamp sizes (if present)
- the **lowest implied-set size** and **lowest cap_lines** among the contributing candidate rows (to keep it “profit-first”)

Important: it does **not** try to merge play-sets. It is a “where should I look first?” board.

---

## Watchlist tags (SSOT meanings)

Tags are simple “co-fire patterns” intended to surface the most actionable environments quickly.

- `ENGINE_GOV`: A01 + A11 co-fire (consensus engine + hot-zone governor).
- `STRAIGHT_GATE`: A11 co-fires with a straight candidate (A05 or A12) → straight-style environment with governor support.
- `STRAIGHT_GATE_STAR3PLUS`: `STRAIGHT_GATE` and A11 star_level ≥ 3.
- `CLAMP_ANY`: Any A12 clamp present (low-entropy lane subset exported).
- `CLAMP_4` / `CLAMP_2` / `CLAMP_1`: Clamp present and the exported clamp size is exactly 4 / 2 / 1.
- `CARRY_PERM`: A04 + A05 co-fire (carry + horizontal drift).
- `CARRY_PERM_GOV`: `CARRY_PERM` + A11 co-fire.
- `CARRY_PERM_HARDLOCK`: `CARRY_PERM` + A03 promoter co-fire (cross-variant consensus boost).
- `IDX_ECHO_BASE`: A09 co-fires with any base candidate (lane echo + base play present).
- `IDX_ECHO_CLAMP`: `IDX_ECHO_BASE` + clamp present (A12).
- `XVAR_IDX_ECHO`: A03 promoter co-fires with A09 (cross-variant + lane echo).
- `DBL_BA`: A02 co-fires with A08 (doubles bias + remaining pairs promoter).
- `DBL_MIRROR`: A02 co-fires with A07 (doubles bias + mirror echo).
- `DBL_BA_MIRROR`: A02 co-fires with both A07 and A08.

---

## How to use it (practical)

1) Open the board for day **D**:
   - `sharepacks/<D>/control_center/profit_compound_events.md`
2) Pick the top 1–3 rows by priority and open the underlying Profit Alerts board:
   - `sharepacks/<D>/control_center/profit_alerts.md`
3) If you’re doing evaluation, use the merged episodes:
   - `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`

---

## Contract notes (do not drift)

- Tags are a **derived view** and must not change the underlying A01–A12 semantics.
- If the tagger changes, validate with:
  - `python3 scripts/tools/validate_profit_alerts_contract.py --start <D1> --end <D2>`
