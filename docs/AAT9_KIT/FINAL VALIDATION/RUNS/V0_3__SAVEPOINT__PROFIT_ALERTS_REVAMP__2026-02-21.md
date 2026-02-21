# V0.3 Savepoint — Profit Alerts Revamp (Quarantined)

Timestamp (UTC): `2026-02-21T08:16:37Z`

Repo:
- Branch: `checkpoint/v0_3-stable10-spinecap6`
- Git HEAD: `f31e7af81677d57bc12da29c10f8c3f6111b2f68`

Purpose:
- Run a **quarantined** “truth layer” pass for Profit Alerts (A01–A12):
  - ensure evaluation artifacts exist,
  - produce rollups/scoreboards with explicit lenses,
  - produce a curated manual-audit casebook,
  - and only then apply minimal fixes if evidence demands it.

Hard invariants:
- No analyzer edits (Stable/DR/Hot Zones/VTRAC remain frozen).
- Profit Alerts remain quarantined (do not change `tool_only` posture).
- No overwrite footguns: all outputs are uniquely named per window.
- Date rosters are built from existing sharepack folders (missing days are skipped).

Reference SSOT (do not drift):
- Evaluation semantics: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`
- Per-alert grading: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Grading_Matrix.md`
- Exporter: `scripts/tools/export_control_center_sharepack.py`
- Evaluator: `scripts/tools/evaluate_profit_alerts.py`

Target windows (initial):
- “Known-good mini corpus”: `2025-06-21..2025-06-23`
- “Reported-bad window”: `2025-12-30..2026-01-09`

Primary scripts (expected to run):
- Ensure eval artifacts exist:
  - `python3 scripts/tools/evaluate_profit_alerts.py --date <D>`
- Corpus rollups:
  - `python3 scripts/tools/rollup_profit_alerts_corpus.py --start <A> --end <B>`
- Casebook/package generation (new, quarantined helper; see Packages output below).

Outputs (expected):
- Window rollups (rows + merged + summary):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__PROFIT_ALERTS_ROLLUP_ROWS.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__PROFIT_ALERTS_ROLLUP_MERGED.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__PROFIT_ALERTS_ROLLUP.md`
- Integrity summaries (new, windowed):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PROFIT_ALERTS__INTEGRITY__<A>_to_<B>__2026-02-21.md`
- Manual audit casebooks (new, windowed packages):
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_revamp__<A>_to_<B>__2026-02-21/CASEBOOK.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_revamp__<A>_to_<B>__2026-02-21/MANIFEST.md`
- End summary (new, decision-ready):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PROFIT_ALERTS__REVAMP_STAGE2_REPORT__2026-02-21.md`

