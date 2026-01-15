# Digit Reduction — v0 Design Intent (What It Should Be in “Superbrain”)

Purpose: capture the *intended* analytical role of Digit Reduction (DR) so the v0 audit doesn’t devolve into “did it hit?”. This document is the posture reference for the DR v0 audit deliverables:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__QUANT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__CASES.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__FEATURE_DECISIONS.md`

This is a synthesis doc (design intent + contracts), not a tuning spec.

---

## Scope + guardrails (v0 synthesis sprint)

- Use only frozen SSOT evidence:
  - Post-results (“after”): `sharepacks/<D>/<STATE>/...` + `docs/.../RUNS/<D>__<STATE>.md`
  - Predictive (“before”): `sharepacks/_predictive/<D>/<STATE>/...` (must stay winners-free)
- No analyzer edits during v0 synthesis (DR/Stable/VTRAC/Hot Zones).
- Profit Alerts must stay quarantined for conclusions (baseline profile = `tool_only`).

---

## Core concept (universal DR framing)

DR is a “reduce the long strings” method that:

1) Takes the most recent draw digits as a *reduction driver*.
2) Reduces long strings via multiple reduction methods/modes to expose:
   - **3-value residues** (clean, “lingering” triples),
   - **digit pools / envelopes** (e.g., 4+ digit remnants that imply triads),
   - **VTRAC-family equivalents** (via the project’s mirror mapping).

DR is *not* primarily “the final top-3 picks”. Often the true value is:

- how early a triad shows up,
- how persistently it reappears across boxes/sets/variants,
- and whether multiple reductions converge on the same residue (or digit pool).

This is the mental model described in your notes (e.g., `tasks/REDUCTION_THOUGHTS.txt`).

---

## Terminology locks (avoid drift)

- **Mirror scheme (default)**: VTRAC-pair mirror (not sum-to-9):
  - `0↔5, 1↔6, 2↔7, 3↔8, 4↔9`
- **Canonicalization**: treat Pick‑3 literals as 3-digit strings; canonical = sorted digits (boxed equivalence).
- **Disambiguate “VTRAC”**:
  - `vtrac_index`: boxed-family index (1–35 via `get_vtrac_index`)
  - `vstraight lane`: 8-combo STR8_8 lane (VSTRAIGHTS)

---

## “Account for occurrence” vs “as-is” reduction (why both exist)

From `tasks/REDUCTION_THOUGHTS.txt` (design intent):

- **Remove-all-occurrences**:
  - Removes every occurrence of each draw digit (and if a digit isn’t present, removes its VTRAC mirror mate instead).
  - Fast path to a clean 3-value residue.
- **Remove “as-is” / one-at-a-time**:
  - Removes only one occurrence (first occurrence) per elimination step.
  - Preserves repeats/structure and can expose pending residues that would be destroyed by full removal.

This is not “extra jargon”; it’s how DR captures both:

- “clean residue now” and
- “structure under pressure that resolves soon”.

---

## DR outputs (lean contract; what’s evidence vs what’s evaluation-only)

Reference contract: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Analyzer_Lean_Outputs.md`.

Inside each sharepack:

- Brain evidence (pre-results capable):
  - `.../digit_reduction/<STATE>/analyzer_v2/<STATE>_analyzer_v2_per_item.csv`
  - `.../digit_reduction/<STATE>/analyzer_v2/<STATE>_analyzer_v2_top_candidates.csv`
  - `.../digit_reduction/<STATE>/analyzer_v2/<STATE>_analyzer_v2_meta.json`
  - `.../digit_reduction/<STATE>/*digit_reduction*_report*.html` + `*_scores.csv` (human lens)
  - `.../digit_reduction/<STATE>/training/*_digit_reduction_steps.csv` + `*_digit_reduction_logs.json` (method trace)
- Winners/evaluation-only (post-results):
  - `.../digit_reduction/<STATE>/analyzer_v2/winners/*_winner_stamp.json`
  - `.../digit_reduction/<STATE>/analyzer_v2/winners/*_winner_flags.csv`
  - `.../digit_reduction/<STATE>/analyzer_v2/winners/*_winner_hits.csv`

Key rule: evaluation-only files must never be used as predictive inputs.

---

## “Golden indicators” DR is supposed to surface (v0 framing)

These are the DR primitives implied by `tasks/REDUCTION_THOUGHTS.txt` and related notes:

- Early arrival: a 3-value residue appears early in the reduction trace (not just at the end).
- Persistence: the same residue (or digit pool) repeats across multiple boxes/sets/variants.
- Cross-variant agreement: similar residues appear in Midday/Evening/Combined around the same timeframe.
- Digit-pool envelopes: 4+ digit remnants that imply a small triad family (bounded combinations).
- Mirror/VTRAC structure: residues and envelopes that align with the VTRAC-pair mirror mapping.
- “Noise vs structure”: dense, repeated residues are more meaningful than scattered one-offs.

The audit question is: which of these are present in the artifacts today, and how should we consume them in v0.2 *without* touching analyzers yet?

