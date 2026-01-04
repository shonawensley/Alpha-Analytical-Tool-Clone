# ChatGPT Pro — Deep Research Prompt (Gold Days 2025‑06‑21..2025‑06‑23)

Use this prompt when attaching the repo for a deep research session.

## Mission

Analyze the “gold days” corpus (D=2025‑06‑21, 2025‑06‑22, 2025‑06‑23) and produce **actionable, evidence‑linked insights** about:
- environment classes (what the winners lens looked like),
- tool performance (Stable / DR / VTRAC / Hot Zones outcomes),
- Aux compounding,
- Control Center (Brain‑2) boards + Profit Alerts episode behavior,
- and candidate‑set/coverage implications.

Important: do not suggest changing analyzers yet unless there is a clear contract violation. Separate “pipeline correctness” from “tool outcomes”.

## What to read first (strict order)

1) Workflow + semantics (SSOT):
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`
- (Optional concept context) `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Pattern_Progression_Primer.md`

2) Corpus entry points (analysis artifacts):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CORPUS_SYNTHESIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`

3) Per-day portals (Brain‑2 then Brain‑1):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__CONTROL_CENTER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__DAY_SYNTHESIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__CONTROL_CENTER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__DAY_SYNTHESIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__CONTROL_CENTER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__DAY_SYNTHESIS.md`

4) Per-state run reports (the template answers):
- Read all `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__*.md` (excluding `__DAY_SYNTHESIS` if you already read it)
- Read all `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__*.md`
- Read all `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__*.md`

Only if you need to audit raw evidence: drill into `sharepacks/<D>/...` (immutable snapshot).

## Deliverables (write these as separate sections)

1) **Top 10 cross-day insights**
- Each insight must include: which days/states it appears, which tool(s) support it, and what artifact(s) prove it.

2) **Environment taxonomy**
- Propose 4–8 “day classes” or “state-day classes” (e.g., “high convergence”, “dominant-lane miss”, “hot zones noisy”, etc.).
- For each class: what you’d look for in the winners lens and which tools tend to confirm/contradict.

3) **Tool performance summary (not tuning)**
- For Stable/DR/VTRAC/Hot Zones:
  - What patterns of misses/hits appear across the 3 days?
  - Any recurring “tool outcome” categories worth tracking (not “bugs”)?

4) **Control Center / Profit Alerts evaluation**
- Summarize:
  - HIT(decay) vs HIT<=7 vs HIT<=14 (variant-faithful and any-outcome) across the 3 days.
  - Merged play‑set behavior (do not interpret raw row counts as “bets”).
- Identify which AlertIds appear most frequently and which correlate with any hits within <=14 (if any).

5) **Candidate set + coverage implications**
- Based on the run reports’ pack decisions (Parts 4/5), identify 3–5 recurring “coverage patterns” that seem most plausible.
- Keep this as “evaluation framing”, not wagering advice.

6) **Fix‑Now vs Fix‑Later**
- Fix‑Now = pipeline correctness / artifact contract issues only (missing artifacts, misalignment, drift).
- Fix‑Later = tuning ideas / hypotheses / new evaluation lenses.

## Constraints (must follow)

- Treat `sharepacks/<D>/` as immutable evidence.
- Do not recommend changing combined-table extraction/readers or analyzer logic based only on 3 days.
- Prefer evidence already embedded in run reports; use raw sharepacks only as audit proof.
