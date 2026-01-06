# GOLD_RUNS_2 Triage (2025‑12‑30 → 2026‑01‑04)

Purpose: convert the post‑run “Gold Runs 2” analysis into a **non‑panic, SSOT‑aligned** action list so we can separate:

- **Fix‑Now (pipeline correctness)**: does the system grade/label the right thing and read the right data?
- **New analytics lenses (reporting/instrumentation)**: adds measurability without changing analyzers.
- **Fix‑Later (tuning/strategy)**: do not implement until we have a larger corpus and a clear contract.

Primary input (summarized here so it’s not required reading):
- `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/GOLD_RUNS_2_REPORT.txt`

SSOT guardrail:
- Pipeline integrity ≠ tool outcome. “Weak/noisy” days are expected; they are a measurement, not a defect.
- Do **not** change analyzers (Stable/DR/VTRAC/Hot Zones) based only on this 6‑day window.

## Current pipeline status (Fix‑Now)

No new Fix‑Now blockers are introduced by GOLD_RUNS_2. Pipeline/semantics fixes remain centralized here:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/POST_RUNS_TRIAGE.md`
- Corpus audit (must stay FAIL=0): `reports/audit/sharepacks_audit_gold_days.md`

## Triage table (recommendations → status)

| GOLD_RUNS_2 recommendation | Status | What to do now (SSOT‑safe) | What to do later (Fix‑Later) |
|---|---|---|---|
| Environment taxonomy (Classes A–F) | New analytics lens | Quantify using numeric tool evidence (not prose). Add corpus metrics and a “class labels” report. | Move to Control Center gating once validated across a larger corpus. |
| Confidence‑tiered betting / “skip is valuable” | Fix‑Later | Capture as *unitless* economics fields in reports (set_size, window_steps, cost_units). | Encode gating/caps only after we validate the taxonomy against more days. |
| “Synergy scoring” / cross‑tool convergence boosting | Fix‑Later + analytics lens | Measure convergence first (counts of independent confirmations) in a corpus metrics file. | Later: implement scoring weights in aggregator/superbrain. |
| “Combined/cross‑variant bounce matters” | New analytics lens | Add explicit cross‑variant metrics: where a winner’s strongest evidence came from (Midday vs Evening vs Combined sections). | Later: tune any “cross‑variant boost” rules based on measured lift. |
| Stable is “best early gauge” but may undervalue some patterns | Fix‑Later | Record measurable Stable signals (exact hits, family rank fraction, section source). | Consider Stable scoring/tail logic adjustments only after more days confirm. |
| Hot Zones contains winners but not always top‑ranked | New analytics lens | Export Hot Zones rank fractions to make the “net vs needle” behavior explicit. | Later: experiment with top‑N trims only with sufficient sample. |
| Digit Reduction is valuable for structure, top‑caller rare | New analytics lens | Export DR stamp counts (vtrac_any / drops) and top candidate flags separately. | Later: adjust DR top‑N/filters only if metrics show consistent lift. |
| Negative controls (dominant‑lane miss) need explicit flags | New analytics lens | Add “dominant signal but miss” detectors at reporting layer (no tuning yet). | Later: incorporate into Control Center warnings / gating logic. |
| Profit Alerts: expand tracking (hit rate, time‑to‑hit, ROI) | New analytics lens | Aggregate episode evaluation across the 6 days (HIT(decay), HIT<=7, HIT<=14, censoring). | Tune gates/decays only after corpus expansion. |
| “Documentation/training/cheat sheets” | New analytics lens | Add an “analysis navigator” style pointer doc for how to read the corpus outputs. | Later: distill into operator cheat sheets once stable. |

## Next SSOT deliverables (what we should build)

These are reporting/instrumentation only (no analyzer changes):

1) `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_tool_metrics.csv`
   - Machine‑readable numeric metrics extracted from `sharepacks/<D>/<STATE>/*/summary.json` + `sharepacks/<D>/control_center/*`.
2) `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CROSS_VARIANT_REPORT.md`
   - Explicit “where did the strongest evidence come from?” (Midday vs Evening vs Combined sections).
3) `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__MIRROR_DOUBLE_FREQUENCY.md`
   - Corpus‑level frequency of literal doubles vs “VTRAC‑space mirror doubles” (duplicates in reduced signature).

These outputs keep the workflow broad but measurable, so future “superbrain” work can be evidence‑driven.
