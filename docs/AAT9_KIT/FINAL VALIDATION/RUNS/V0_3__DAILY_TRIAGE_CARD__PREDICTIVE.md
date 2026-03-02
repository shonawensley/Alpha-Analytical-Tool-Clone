# V0_3 Daily Triage Card (Predictive Day Review)

Purpose: a **single, plain-English checklist** to evaluate “where we are” on any predictive day without drowning in artifacts.

This card assumes the current reality we’ve validated in the evidence ledger:
- The **tools often see the winner neighborhood (lane)**.
- The pain is usually **conversion under a fixed budget** (B12/B24/B36), not “tools are dead”.

---

## 1) The 3 files you open first (minimum viable review)

Pick a predictive day `D` (YYYY-MM-DD), then open:

1) Predictive portfolio (baseline, tool_only):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PREDICTIVE_PORTFOLIO__tool_only.md`

2) Predictive portfolio (dc1 conversion, tool_only; optional but recommended):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PREDICTIVE_PORTFOLIO__tool_only__dc1__B36__closure_v2.md`

3) Posted results (same date as the portfolio):
- `data/results/<D>.txt`

If you only do these 3, you can already answer:
- “What did we play?” (B12/B24/B36)
- “Did it hit?” (straight / boxed / lane)
- “If it missed, what kind of miss?”

---

## 2) What the portfolio *rank* means (plain English)

The portfolio’s top-to-bottom state order is **not** a promise of conversion (hit rate).

It is a **triage surface**: it tends to put states higher when the day looks more “structured” for that state, e.g.:
- **boundedness**: Candidate Universe (`CU union`) is smaller / tighter (less sprawl),
- **convergence**: there’s a clearer “top support” (a canonical shows up a lot across packs),
- **alignment**: the Due Doubles / VTRAC-pack lanes are more coherent with the CU surface.

Translation: **rank tells you where evidence is denser**, not where strict hits are guaranteed.

---

## 3) The fastest post-results questions (what you actually care about)

For each state/outcome you check, answer in this order:

1) **Straight?** Did the exact winner appear in B36?
2) **Boxed(any perm)?** If not, did any permutation appear? (winner canonical present)
3) **Lane?** If not boxed, did we at least hit the winner’s VTRAC index (“winner lane”)?
4) **Digits?** If lane-hit but not boxed, did we at least capture all 3 digits somewhere? (digit-assembly miss)

Why this order:
- **Straight** is the hardest “end goal”.
- **Boxed(any perm)** tells you if we assembled the canonical.
- **Lane hit** tells you if we were “in the right neighborhood”.
- **Digit cover** tells you if the miss is mostly “perm assembly” vs “we never saw it”.

---

## 4) Where to see those answers instantly (no eyeballing)

Use the “Portfolio vs Results” reports (they compute straight/box/lane/digit-cover + near-miss signals):

- Windowed (broad-first; best starting point):
  - Baseline: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only.md`
  - Baseline: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only.md`
  - dc1: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.md`
  - dc1: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.md`
  - Optional (posture buckets; tight vs noisy; baseline vs dc1): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__ENV_VERDICT_SCOREBOARD__B36__tool_only__baseline_vs_dc1.md`
  - Optional (label gaps; explains `UNLABELED`): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__ENV_VERDICT_LABEL_GAPS__B36__tool_only.md`

- Single-day (when you want “just one day”):
  - Example baseline: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__PORTFOLIO_VS_RESULTS__tool_only.md`
  - Example dc1: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__PORTFOLIO_VS_RESULTS__tool_only__dc1__B36__closure_v2.md`

---

## 5) Quick diagnosis map (what a miss usually means)

Use this as a “what to fix” compass:

- **Lane hit is high, but boxed(any perm) is low** → we’re losing to **within-lane conversion** (need deeper/cheaper closure inside the correct lane).
- **DigitCoverAll is high, but boxed(any perm) is low** → classic **digit-assembly miss** (we saw the digits; didn’t spend lines on the right permutations).
- **CU contains the winner lane, but B36 misses the lane** → **retention / lane allocation** problem (we knew the neighborhood but didn’t fund it).
- **Doubles/triples day** → treat it as a different regime; conversion should exploit doubles/mirror structure (cheaper closure).

If you want the “why this is true (with receipts)”, open:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MASTER_EVIDENCE_EXTRACTION__WINS.md`

---

## 6) Optional: generate a one-day scoreboard yourself (if a day is missing)

If you don’t see a per-day `__PORTFOLIO_VS_RESULTS__` report for a day you care about, generate it:

This writes:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>_to_<D>__PORTFOLIO_VS_RESULTS__tool_only.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>_to_<D>__PORTFOLIO_VS_RESULTS__tool_only.csv`

```bash
python3 scripts/tools/create_portfolio_vs_results_report.py \
  --start-date 2026-01-04 \
  --end-date 2026-01-04 \
  --profile tool_only \
  --prefer-experiment-tags stable10,,vtracpack_v1
```

For dc1 (uses the `play_card__tool_only__dc1.json` when present):

```bash
python3 scripts/tools/create_portfolio_vs_results_report.py \
  --start-date 2026-01-04 \
  --end-date 2026-01-04 \
  --profile tool_only \
  --prefer-experiment-tags dc1,,stable10
```

If the output already exists, the script will refuse to overwrite unless you add `--force`.

---

## 7) Available predictive days (current sharepacks)

Predictive sharepacks currently exist under `sharepacks/_predictive/` for:
- `2026-01-01` → `2026-01-09`
- `2026-01-15` → `2026-01-18`
- `2026-01-20` → `2026-01-22`

---

## 8) Regime tags + posture anchors (so you don’t overreact)

If you feel yourself getting pulled into “talking circles”, use the regime tags section in the SSOT:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MASTER_EVIDENCE_EXTRACTION__WINS.md` (see “Phase 3 output — Regime tags + stability map”)

Two anchors to calibrate your intuition:
- **Press / playable anchor:** `C019` (PA, 2026‑01‑09 Evening 014) — a clean strict hit example.
- **Skip / tiny hedge anchor:** `C030` (NC, 2026‑01‑08) — weak/noisy + 0 lane hit on both outcomes.
