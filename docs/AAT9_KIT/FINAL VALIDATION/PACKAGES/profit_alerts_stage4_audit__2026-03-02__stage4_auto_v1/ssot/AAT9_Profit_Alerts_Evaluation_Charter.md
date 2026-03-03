# AAT9 Profit Alerts (A01–A12) — Evaluation Charter (Master Validation)

Purpose: define the **non‑negotiable evaluation rules** for the A01–A12 Profit Alerts so we can measure them consistently across days/states and avoid “Combined / variant” confusion during context resets.

Scope:
- This charter is **evaluation-only** (Brain‑2). It does **not** define wagering logic.
- It applies to the **sharepack-aligned** export:
  - `sharepacks/<D>/control_center/profit_alerts.csv`
  - `sharepacks/<D>/control_center/profit_alerts.md`

Definitions:
- **H** = history workbook date (tables/draws “world snapshot” date, D‑1)
- **D** = results date (winners date; sharepack day folder name)

---

## 1) Outcomes vs lenses (the most important rule)

- **Real outcomes (gradeable):** `State × {Midday, Evening}`
  - These are the only things that can “hit” (a real winning draw).
- **Combined is not a third draw.**
  - **Combined** is an **analytic lens** that reads the state using blended history (Midday+Evening) to generate structure signals.
  - Combined alerts must still be graded only against real outcomes (Midday/Evening).

If you remember only one sentence:
> Combined is an analyzer view, not an outcome stream.

---

## 2) Draw-step rules (how decay windows are counted)

Profit Alerts include `DecayDraws`. To evaluate “hit within range”, we must define what a “draw-step” is.

**Draw-step = one real outcome event (a Midday or Evening result) for the state.**

Variant-specific step sequences (starting at date **D**):

- **Variant = Midday**
  - Steps are Midday outcomes only: `D Midday`, `D+1 Midday`, `D+2 Midday`, …
- **Variant = Evening**
  - Steps are Evening outcomes only: `D Evening`, `D+1 Evening`, `D+2 Evening`, …
- **Variant = Combined**
  - Steps are the real outcome sequence: `D Midday`, `D Evening`, `D+1 Midday`, `D+1 Evening`, …
  - This reflects “two chances per day” where both outcomes exist.

**Window semantics (inclusive):**
- A window of `N` draw-steps means **N opportunities starting on D**.
  - Example (Combined, `DecayDraws=3`): evaluate `D Midday`, `D Evening`, `D+1 Midday`.

---

## 2b) Cross-variant (“any-outcome”) diagnostic lens

In addition to the **variant-faithful** evaluation, Master Validation also reports a second lens to capture “bounce” behavior (e.g., a Midday signal resolving on Evening).

Rules:
- This lens is **diagnostic**; it does **not** change the primary episode `status` for the row.
- The window is defined by the same **time-span boundary** as the variant-faithful window:
  - For `Midday`/`Evening` rows, that boundary is the `Nth` variant-faithful step’s `(date, period)` (skipping missing periods per the Charter).
- Within that time-span, we scan **any real outcomes** (`Midday` + `Evening`) to detect hits.
- For `Combined` rows, “any-outcome” is equivalent to the primary evaluation (Combined already steps through real outcomes).

---

## 3) Missing results periods (skip + censored)

Reality: some results files have missing periods (blank Midday or Evening, or a state missing entirely).

Rules:
- If a period is missing for a state/day, it is **skipped** (it does not consume a draw-step).
- If the repo does not contain enough future `data/results/<date>.txt` files to fully evaluate a window, mark the episode **CENSORED** (unknown yet), not failed.

---

## 4) Hit modes (what counts as a “hit”)

Profit Alerts can imply different hit modes depending on the alert row evidence.

Minimum hit modes (v0):

- **Boxed hit**: `canonical(winner_literal) == canonical(candidate)`
- **Straight hit** (when provided): `winner_literal == orders_modal_value`
- **VTRAC-index hit** (when provided): `vtrac_index(winner_literal) == current_index`
- **Set hit** (when provided): `winner_literal ∈ implied_set`  
  - Used when the alert implies a concrete small set (e.g., `STR8_8`, `STR8_4of8`, `STR8_3`, or explicit BOX perms).
  - The per-alert “what is a hit” rules live in: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Grading_Matrix.md`

Notes:
- Winners and candidates must be treated as **3-digit strings** (preserve leading zeros).
- A single episode may have multiple matching modes; evaluators should record the **first hit** and its hit_type(s).

---

## 5) Scorecards (what we report)

Evaluation output must report two tiers:

1) **Strict (diagnostic):** did it hit on results date `D` only?
2) **Windowed (primary):** did it hit within the episode’s own `DecayDraws` draw-steps?

Additionally, for windowed evaluation we report both:
- **Variant-faithful** (primary): Midday-only, Evening-only, Combined sequence
- **Any-outcome** (diagnostic): for Midday/Evening rows, allow resolution on either outcome within the same time-span boundary

Additionally, report fixed secondary horizons (default):
- `7` draw-steps
- `14` draw-steps

These secondary horizons are diagnostics to learn timing patterns without pretending they’re “fast” signals.

Episode status (for the primary DecayDraws window):
- **HIT**: first hit occurs within DecayDraws
- **EXPIRED**: no hit and we have enough results to fully evaluate the window
- **CENSORED**: no hit yet, but we don’t have enough future results files to fully evaluate

---

## 6) Canonical evaluator command (local only; no web)

For a given sharepack day `D`:
```bash
python3 scripts/tools/evaluate_profit_alerts.py --date <D>
```

Outputs:
- `sharepacks/<D>/control_center/profit_alerts_eval.md`
- `sharepacks/<D>/control_center/profit_alerts_eval.csv`
