# Final Validation — Curated Research Packs

Purpose: pointer-only bundles that define a precise review scope (for external reviewers / ChatGPT Pro) without copying or moving sharepacks/run reports.

Each pack includes:
- a `README.md` (start-here pointers),
- a `MANIFEST.md` (exact file scope),
- and a `CHATGPT_PRO_DEEP_RESEARCH_PROMPT.md` (copy/paste prompt).

## Optional: build a physical “upload pack”

If you need a **single folder/zip** you can upload (instead of pointer-only manifests), use:

```bash
python3 scripts/tools/export_chatgpt_research_pack.py --start-date <D0> --end-date <D1> --mode curated --include-predictive --include-control-center --zip
```

This writes a bounded export under `sharepacks/_scratch/` (and includes `README.md` + `MANIFEST.csv` inside the export).

Useful flags (common)
- Experiment-tagged predictive artifacts (e.g. stable10): add `--experiment-tag stable10`
- Include an OOS guardrail window in the same export: add `--extra-window YYYY-MM-DD:YYYY-MM-DD` (repeatable)
- Include a pointer-only pack prompt/manifest inside the export: add `--include-path "docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/<pack_name>"`

## Available packs

- v0.2 closeout (selection + grading alignment; VTRAC pack strategy + windowed grading):
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/v0_2_closeout_play_card_windowed_vtracpack/README.md`

- v0.3 fresh days run pack (how to run + what to review; receipt-based cadence):
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/v0_3_fresh_days_run_pack/README.md`

- Play Cards + budgets + combo packs (selection/grading design review):
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/play_cards_budget_system_review/README.md`

- Profit Alerts postmortem (v0.2 quarantine; wiring/semantics audit scope):
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_postmortem_v0_2/README.md`

- Crossroads re-entry (glass-box; one gold day; B36-only):
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/README.md`

- 2025‑06‑21 → 2025‑06‑23 (3-day starter corpus):
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/gold_days_2025-06-21_to_2025-06-23/README.md`

- 2025‑12‑30 → 2026‑01‑04 (6-day expansion corpus):
  - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/gold_days_2025-12-30_to_2026-01-04/README.md`
