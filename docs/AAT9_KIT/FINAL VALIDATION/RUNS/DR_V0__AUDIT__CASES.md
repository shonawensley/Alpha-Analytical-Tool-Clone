# Digit Reduction — v0 Audit (Case Studies)

Purpose: validate (with concrete examples) whether Digit Reduction (DR) is currently being:

- extracted correctly,
- scored/selected correctly,
- and consumed correctly by the prediction layers (Candidate Universe / Play Cards).

This is a **consumption audit** (v0 synthesis). We do not tune analyzers here.

Read first:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__DESIGN_INTENT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__QUANT.md`

---

## How these cases were inspected

For each case, the fastest “truth” surface is the DR winners overlay + stamp/flags/hits files:

- `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/winners/*_winner_overlay.html`
- `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/winners/*_winner_stamp.json`
- `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/winners/*_winner_flags.csv`
- `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/winners/*_winner_hits.csv`

Then cross-check “what DR would have suggested pre-results” via:

- `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/<STATE>_analyzer_v2_top_candidates.csv`

And anchor everything back to the comprehensive per-state run report:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`

---

## Case 1 — NewJersey4 (D=2026-01-09) — Evening winner `028` (canon `028`)

Gold reference:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md` (GOLD-0018)

Evidence pointers:
- DR winners: `sharepacks/2026-01-09/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/winners/`
- DR analyzer_v2: `sharepacks/2026-01-09/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/`
- Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__NewJersey4.md`

What DR “knows” post-results (overlay/stats):
- The winner appears **very frequently** in DR traces for Evening:
  - `exact_any=133/162` (the literal winner is present in many DR boxes)
  - `vtrac_any=159/162` (winner’s VTRAC family is broadly present)

What DR “would have suggested” pre-results (top candidates):
- In `*_analyzer_v2_top_candidates.csv`, the Evening winner **is present**, but only at a **very low local rank**:
  - `winner_present=True`, `winner_best_rank=23` out of `rows_total=28`
  - So it is **not** included by the default `--top-n-dr 3`.

Interpretation:
- This is the “trace vs caller” split:
  - DR contains the winner *inside the reduction trace*,
  - but the analyzer’s top-candidate ranking doesn’t elevate it.
- If we want DR to contribute predictively in v0.2 without tuning analyzers, we should consume it as:
  - envelope/persistence evidence,
  - not as “top‑3 straight caller”.

---

## Case 2 — Florida4 (D=2026-01-07) — Midday winner `434` (canon `344`)

Gold reference:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md` (GOLD-0015)

Evidence pointers:
- DR winners: `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/winners/`
- DR analyzer_v2: `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/`
- Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Florida4.md`

What DR “knows” post-results (overlay/stats):
- Midday winner `434` is present widely in the trace:
  - `exact_any=91/117`, `vtrac_any=104/117`

What DR “would have suggested” pre-results (top candidates):
- The winner is **not present** in the top-candidate list:
  - `winner_present=False` in `*_analyzer_v2_top_candidates.csv` for Midday.

Observed failure mode:
- DR top candidates are dominated by other patterns (e.g., repeated 552/544/522 motifs).
- The winner exists in the reduction trace (so the extractor worked), but it wasn’t promoted to a “best_pattern”.

Interpretation:
- Same conclusion: DR is rich evidence, but the current “best_pattern” caller surface is unreliable as a predictor.

---

## Case 3 — Florida4 (D=2026-01-07) — Evening winner `963` (canon `369`)

Gold reference:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md` (GOLD-0016)

Evidence pointers:
- DR winners: `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/winners/`
- DR analyzer_v2: `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/`
- Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Florida4.md`

What DR “knows” post-results (overlay/stats):
- Evening winner `963` has:
  - `exact_any=0/90` but `vtrac_any=90/90`, `vt_boxed=6`
  - Meaning: DR is “seeing” the winner primarily through VTRAC-family structure rather than literal exact presence.

What DR “would have suggested” pre-results:
- The winner does **not** appear in the Evening top-candidates list.

Interpretation:
- This is a strong example of why DR should be treated as:
  - family/lane structure evidence (support),
  - not as a literal “top 3 straight” caller.

---

## Case 4 — NewYork4 (D=2026-01-05) — Midday winner `080` (canon `008`)

Gold reference:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md` (GOLD-0014)

Evidence pointers:
- DR winners: `sharepacks/2026-01-05/NewYork4/digit_reduction/NewYork4/analyzer_v2/winners/`
- DR analyzer_v2: `sharepacks/2026-01-05/NewYork4/digit_reduction/NewYork4/analyzer_v2/`
- Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__NewYork4.md`

What DR “knows” post-results:
- Midday winner `080` is present in DR trace:
  - `exact_any=41/131`, `vtrac_any=89/131`

What DR “would have suggested” pre-results:
- Winner is not present in `*_analyzer_v2_top_candidates.csv` (Midday).

Observed failure mode:
- Top candidates are dominated by repeated motifs (e.g., 500/552/520), which do not include the winner.

Interpretation:
- Again: the extractor shows the winner is “in the DR world”, but the caller surface does not elevate it.

---

## Case 5 — NewJersey4 (D=2026-01-06) — Evening winner `942` (canon `249`)

Gold reference:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md` (GOLD-0006)

Evidence pointers:
- DR winners: `sharepacks/2026-01-06/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/winners/`
- DR analyzer_v2: `sharepacks/2026-01-06/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/`
- Run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__NewJersey4.md`

What DR “knows” post-results:
- Evening winner `942` has:
  - `exact_any=30/252`, `vtrac_any=252/252`, `drop_vtrac_any=240`
  - Meaning: the winner’s family structure is extremely present in DR traces.

What DR “would have suggested” pre-results:
- Winner is not present in the top-candidates list (Evening).

Interpretation:
- Strong “lane awareness”, no “caller promotion”.

---

## Cross-case conclusion (v0)

Across these cases, the repeated pattern is:

1) **DR traces/overlays frequently contain the winner (exact_any/vtrac_any often high).**
2) **DR “best_pattern” top-candidates often do not include the winner, or include it only at very low local rank.**

This supports a v0.2 posture decision:

- Treat DR as an **environment/trace/envelope lens** (digit pools, persistence, VTRAC-family structure).
- Do **not** treat `analyzer_v2_top_candidates.csv` as a primary “top picks” caller without further redesign.

The explicit v0.2 “Keep/Demote/Remove-as-input” table lives here:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__FEATURE_DECISIONS.md`

