# RUNS Portal (Start Here)

Purpose: give you a single “open these files” map so you can review days, predictive packs, grades, and triage without getting lost.

Key idea: **sharepacks are the frozen evidence**, while **RUNS is the review/scaffolding/grades layer**.

---

## 0) If you feel lost (read these in order)

1) This portal:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`

2) What the whole system is (SSOT portal):
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`

3) How to review without drowning (the “how to think” map):
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`

4) What exists / what’s filled:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`

5) “Are we broken?” triage:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/POST_RUNS_TRIAGE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`

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
  - Aux:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__QUANT.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__CASES.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__FEATURE_DECISIONS.md`
  - Stable:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__QUANT.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__CASES.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__FEATURE_DECISIONS.md`
  - Hot Zones:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__QUANT.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__CASES.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__FEATURE_DECISIONS.md`
  - VTRAC enhanced:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__QUANT.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__CASES.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__FEATURE_DECISIONS.md`
- Doubles / mirror-doubles research (reverse-engineering lens):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__INVENTORY.md`
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
