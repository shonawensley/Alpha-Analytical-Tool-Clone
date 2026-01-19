# RUNS Portal (Start Here)

Purpose: give you a single “open these files” map so you can review days, predictive packs, grades, and triage without getting lost.

Key idea: **sharepacks are the frozen evidence**, while **RUNS is the review/scaffolding/grades layer**.

---

## 0) If you feel lost (read these in order)

1) This portal:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`

1.5) Macro roadmap (how the whole workflow fits together):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_ROADMAP.md`

1.6) v0.2 integration log (what changed, why, what remains):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`

2) What the whole system is (SSOT portal):
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`

3) How to review without drowning (the “how to think” map):
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`

4) What exists / what’s filled:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`
- Portal coverage sanity check (legacy/unprofiled docs inventory):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL_COVERAGE_CHECK.md`

5) “Are we broken?” triage:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/POST_RUNS_TRIAGE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`
- v0.3 analyzer edits backlog (“nothing gets missed” inventory):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__ANALYZER_CHANGE_BACKLOG.md`

6) The fast “are we improving?” rollups (cross-day):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup.md`
- Profit Alerts quarantine (ablation profiles; compare without deleting):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup__tool_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup__profit_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__profit_only.md`
  - Tool v0 consumption audits (quant → cases → feature decisions):
  - Digit Reduction:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__QUANT.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__CASES.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__FEATURE_DECISIONS.md`
    - DR envelope harness (reporting-only; digit-pool scoring from `*_digit_reduction_steps.csv` + gateway metrics):
      - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__ENVELOPE_HARNESS__2025-06-21_to_2025-06-23.md` (and `.csv`)
      - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__ENVELOPE_HARNESS__2025-12-30_to_2026-01-04.md` (and `.csv`)
      - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__ENVELOPE_HARNESS__2026-01-05_to_2026-01-09.md` (and `.csv`)
      - Analysis notes: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__ENVELOPE_HARNESS__ANALYSIS.md`
    - Harness-driven DR study queue (bounded “what to read next” list):
      - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__STUDY_QUEUE.md`
    - Design intent (provenance; helps interpret DR outputs):
      - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__DESIGN_INTENT.md`
  - Aux:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__QUANT.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__CASES.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__FEATURE_DECISIONS.md`
    - Aux signals table (CSV; evidence inventory used by the audit):
      - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__SIGNALS__QUANT.csv`
  - Stable:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__QUANT.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__CASES.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__FEATURE_DECISIONS.md`
  - Hot Zones:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__QUANT.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__CASES.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__FEATURE_DECISIONS.md`
    - HOTZ‑003 harness (weight sweep; reporting-only):
      - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP__2025-06-21_to_2025-06-23.md` (and `.csv`)
      - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP__2025-12-30_to_2026-01-04.md` (and `.csv`)
      - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP__2026-01-05_to_2026-01-09.md` (and `.csv`)
      - Follow-up sweep (adds `w_col1_arrival`):
        - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2025-06-21_to_2025-06-23.md` (and `.csv`)
        - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2025-12-30_to_2026-01-04.md` (and `.csv`)
        - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__2026-01-05_to_2026-01-09.md` (and `.csv`)
      - Sweep v3 (adds VTRAC-index gateway metrics):
        - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__2025-06-21_to_2025-06-23.md` (and `.csv`)
        - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__2025-12-30_to_2026-01-04.md` (and `.csv`)
        - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__2026-01-05_to_2026-01-09.md` (and `.csv`)
      - Analysis notes (paired with winners lens + Master Validation):
        - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP2__ANALYSIS.md`
        - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__WEIGHT_SWEEP3__ANALYSIS.md`
      - Optional selection-layer experiment (bounded index-closure helper; research-only):
        - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_INDEX_CLOSURE__EXPERIMENT__2026-01-05_to_2026-01-09.md`
  - VTRAC enhanced:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__QUANT.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__CASES.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__FEATURE_DECISIONS.md`
    - VTRAC Enhanced harness (reporting-only; cross-window gateway metrics):
      - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_ENHANCED_V0__HARNESS__2025-06-21_to_2025-06-23.md` (and `.csv`)
      - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_ENHANCED_V0__HARNESS__2025-12-30_to_2026-01-04.md` (and `.csv`)
      - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_ENHANCED_V0__HARNESS__2026-01-05_to_2026-01-09.md` (and `.csv`)
- CSV companions (general rule of thumb):
  - If a `.md` exists for a rollup/harness/audit, there is usually a `.csv` with the same basename next to it (for sorting/pivoting).
  - Examples: `*_V0__AUDIT__QUANT.csv`, `candidate_universe_rollup.csv`, `play_card_rollup.csv`.
- Corpus exports (power user; large tables):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_tool_metrics.csv`
- Doubles / mirror-doubles research (reverse-engineering lens):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__INVENTORY.md`
    - (CSV companion): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__INVENTORY.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md` (includes winners-lens Set1 col1/2 ladder metrics + samples)
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md` (top “index hit → box miss” cases to study first)
- Aux boxed VTRAC badge matrix (Windows parity signal; reporting-only export):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_VTRAC_BADGE_MATRIX__AUDIT.md`
  - v0 window exports (per-day): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__AUX_VTRAC_BADGE_MATRIX.md` (and `.csv`) for `D=2026-01-05` → `2026-01-09`
    - Regenerate: `python3 scripts/tools/create_aux_vtrac_badge_matrix_report.py --date <D> --sharepacks-root sharepacks --force`
7) v0 “stop running, extract gold” (synthesis sprint):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__SYNTHESIS_SPRINT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
- v0.2 defaults (resume runs without drift):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
- Legacy window analysis (keep for provenance; most conclusions are folded into the v0 audits/ledgers):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/GOLD_RUNS_2_TRIAGE.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/GOLD_RUNS_2_REPORT.txt`

---

## 1) Naming + “before → after” mapping (do not mix these up)

Definitions:
- **H** = history workbook date (inputs / “what we knew”)
- **D** = results date (sharepack folder name / outcomes day)

Folders:
- **Predictive “BEFORE” snapshot (no results):** `sharepacks/_predictive/<D>/...`
- **Post-results “AFTER” snapshot:** `sharepacks/<D>/...`

RUNS files are keyed by the same `<D>` date.

---

## 2) The 3 “most important” day-level RUNS docs (AFTER)

For any results date `D`, start here:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__WINNERS_DIGEST.md` (quick winners scan)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CONTROL_CENTER.md` (Brain‑2 boards + Profit Alerts eval)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__DAY_SYNTHESIS.md` (cross-state synthesis pointers)

Then drill into a specific state:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md` (full Master Validation report)

---

## 3) The 3 “most important” predictive docs (BEFORE)

For any predictive date `D`, start here:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PREDICTIVE_PORTFOLIO__tool_only.md` (cross-state triage; fastest competition surface; tool-first default)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CANDIDATE_UNIVERSE_GRADE__tool_only.md` (once results exist; grading is in RUNS only)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PLAY_CARD_GRADE__tool_only.md` (once results exist; budgeted selection grading)

Then drill into a state:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>__PREDICTIVE__tool_only.md` (pack inventory + evidence pointers; tool-first default)
- Predictive evidence (canonical “what to play now” boards):
  - Tool-first (recommended; Profit Alerts excluded):
    - `sharepacks/_predictive/<D>/<STATE>/candidate_universe__tool_only.json`
    - `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only.json`
  - Profit Alerts are still exported in the predictive sharepack’s Control Center (for measurement/ablation), but are not used by default:
    - `sharepacks/_predictive/<D>/control_center/profit_alerts.csv` (use only if you intentionally run `--profile mixed` / `profit_only`)

---

## 4) Cross-day “range packs” (where patterns start to show)

Range packs are the fastest way to find study cases without opening dozens of state reports:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__CORPUS_DASHBOARD.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__CONVERGENCE_CASES.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__PROFIT_ALERTS_ROLLUP.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__CONTROL_CENTER_ROLLUP.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__CODEX_DEEP_ANALYSIS.md`
Optional (when present for a window):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__CORPUS_SYNTHESIS.md` (narrative summary of the window)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__DR_LENS_REPORT.md` (digit reduction lens / patterns)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__CROSS_VARIANT_REPORT.md` (M/E/C interactions)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__MIRROR_DOUBLE_FREQUENCY.md` (doubles/mirror frequency surface)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__RESULTS_HORIZON.md` (when generated)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__AUDIT_SUMMARY.md` (when generated)

---

## 5) What “Codex analysis” is (and isn’t)

Codex analysis docs are a **parallel reviewer** that:
- summarizes the cross-day rollups,
- points to the highest-signal state/day examples,
- proposes Fix‑Later hypotheses,
- does **not** imply tool/analyzer tuning is warranted from small samples.

Existing Codex analyses:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CODEX_DEEP_ANALYSIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CODEX_DEEP_ANALYSIS.md`
