# CODEX READ THIS — AAT9 (WSL / Ubuntu Canonical)

**This document supersedes any Windows‑first startup docs.**  
All development happens in **WSL**. The only Windows touchpoint is **GitHub Desktop** pushing from the WSL path.

---

## 0) Canonical paths & repo sanity

- **Repo root (CWD, canonical):** `/home/ser/code/Alpha-Analytical-Tool-Clone`
- **GitHub Desktop path (Windows view of the same tree):** `\\wsl$\Ubuntu\home\ser\code\Alpha-Analytical-Tool-Clone`
- **Remote (origin):** `https://github.com/shonawensley/Alpha-Analytical-Tool-Clone.git`

**Print‑only sanity (no writes):**
```bash
cd ~/code/Alpha-Analytical-Tool-Clone
git status -s && git branch -vv && git remote -v && pwd
```
1) Reading order (AAT9 KIT first)

docs/AAT9_KIT/AAT9_KIT_README.md

docs/AAT9_KIT/AAT9_Workflow_Standard.md

docs/AAT9_KIT/Practices/AAT9_Coding_Standards.md

docs/AAT9_KIT/Practices/AAT9_Agent_Operating_Rules.md

docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md

docs/AAT9_KIT/AAT9_Preflight_Reference.md

docs/AAT9_KIT/AAT9_Diagrams_Guide.md

docs/AAT9_KIT/AAT9_Unified_Changelog.md
- Lean bundles + analyzer outputs: docs/AAT9_KIT/AAT9_Analyzer_Lean_Outputs.md and USER_GUIDE_AAT9/DigitReduction_UserGuide.txt

AGENTS.md, .codex/AGENTS.universal.md

Data contracts recap (enforced in code & docs):

Aux / Blackapple → data/cleaned/*_draws.csv (draws‑only).

V‑TRAC / Stable / Digit Reduction → combined tables via utils.path_handler
(e.g., data/outputs/tables/<STATE>/ or tables/<STATE>/).

“Combined” is baseline; “Midday/Evening” are additive variants surfaced alongside.

Master Validation (frozen day snapshot):
- Brain‑1 per-state sharepacks: `sharepacks/<D>/<STATE>/...`
- Predictive (no results) sharepacks: `sharepacks/_predictive/<D>/...` via `python3 scripts/tools/run_predictive_day.py --history-date <H>`
- v0.3 cadence wrapper (preferred; logs a RUNS receipt): `python3 scripts/tools/run_v0_3_cycle.py pre --history-date <H> --sharepacks-root sharepacks/_predictive --profile tool_only --stable10 --force`
- Candidate Universe (gradeable pre-results playset): `python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive`
  - Contract: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Candidate_Universe_Contract.md`
  - Grading (writes only to RUNS): `python3 scripts/tools/grade_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive`
- v0.2 “don’t get lost” SSOTs (start here after any context reset):
  - RUNS Portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
  - v0.2 defaults/posture: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
  - v0.2 integration log: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`
  - v0.2 coverage ledger (generated): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__COVERAGE_LEDGER.md`
  - Predictive workflow addendum: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Predictive_Workflow_V0_2_Addendum.md`
  - Master Validation template addendum: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Template_V0_2.md`
- Brain‑2 Control Center export (drift-proof): `python3 scripts/tools/export_control_center_sharepack.py --date <D>` → `sharepacks/<D>/control_center/`
  - Includes Profit Alerts board (A01–A12): `sharepacks/<D>/control_center/profit_alerts.*`
- Profit Alerts windowed evaluation (episodes): `python3 scripts/tools/evaluate_profit_alerts.py --date <D>` → `sharepacks/<D>/control_center/profit_alerts_eval.*`
  - Contract: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`
  - Per‑AID grading matrix: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Grading_Matrix.md`
- Control Center daily run report (Brain-2, per day): `python3 scripts/tools/create_control_center_daily_run_report.py --date <D>` → `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CONTROL_CENTER.md`
- Analysis navigator (how to review a day without drifting): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`
- Pattern progression primer (concept lens; survives context resets): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Pattern_Progression_Primer.md`
- Curated “research packs” (for external review / ChatGPT Pro): `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/README.md`
- Deep Research / external reviewers (important):
  - Most `sharepacks/<D>/` and `sharepacks/_predictive/<D>/` folders are gitignored (large, local snapshots).
  - Most `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<date>__*.{md,csv}` and `<date0>_to_<date1>__*.{md,csv}` outputs are also gitignored (regenerable).
  - Therefore: “repo access” alone usually cannot open a pointer-only pack; use a bounded upload export:
    - `python3 scripts/tools/export_chatgpt_research_pack.py ... --zip` (see `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/README.md`).
- Run report progress index (avoid “where are we?” drift): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`
- Brain‑2 policy harness (Top‑N triage; tracks `hit_any` + `box_hit`): `python3 scripts/tools/superbrain_config_harness.py --start-date <A> --end-date <B> ...`
- Optional sharepacks corpus audit (confidence/drift guard across multiple days): `python3 scripts/tools/audit_sharepacks_corpus.py --dates 2025-06-21 2025-06-22 2025-06-23`
- If you add new `data/history/Pick3StatsC4_*.xlsm` files: do a 60‑second sanity check that the workbook is truly “H” (not misdated) by extracting 1 state’s newest draw and comparing to `data/results/<H>.txt` before building `sharepacks/<D=H+1>/`.
- **HARD STOP (workbook swaps): avoid stale tables/winners**
  - Never assume `data/original/Pick3StatsC4.xlsm`, `data/outputs/**`, or any cached “winners” directory still matches the new workbook.
  - For full-day builds (results exist): regenerate the world snapshot via `PYTHONPATH=.:src python3 scripts/tools/run_history_and_results.py --history-date <H> --regen-aux-draws` (this rebuilds tables + JSON + date-scoped winners lens).
  - For predictive builds (no results yet): use `python3 scripts/tools/run_v0_3_cycle.py pre --history-date <H> ...` (activates workbook + regenerates tables/JSON + freezes `sharepacks/_predictive/<D>/...`). Recommended posture: `--stable10`.
  - Winners lens must be date-scoped: prefer `reports/stable/winners_by_date/<D>/...` and `sharepacks/<D>/<STATE>/winners/...` (do not rely on any legacy `data/outputs/winners/` cache).
  - Validate one state after any workbook swap: `python3 scripts/tools/validate_tables_aux_alignment.py --date <D> --state <STATE> --strict` and stop if it fails.
- Optional (Part A helper): winners JSON digest (paste-friendly): `python3 scripts/tools/winners_json_digest.py --winners-dir sharepacks/<D>/<STATE>/winners/<STATE>`
- Quickstarts (zero-context):
  - Build + freeze a new day: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Build_Full_Day_Quickstart.md`
  - Evaluate-only (sharepacks already built): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Evaluate_Only_Quickstart.md`
  - “Pipeline vs tool outcome” sanity + dtype/leading-zero pitfalls: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`

2) WSL alignment & PowerShell bridging

Always treat the repo root as: /home/ser/code/Alpha-Analytical-Tool-Clone

To call a Windows PowerShell script from WSL (only when necessary):

```bash
powershell.exe -NoProfile -File "$(wslpath -w .)\path\to\script.ps1"
```


If pushing from Windows, use GitHub Desktop on:

```bash
\\wsl$\Ubuntu\home\ser\code\Alpha-Analytical-Tool-Clone
```

3) Preflight (run when requested)

From WSL:

```bash
powershell.exe -NoProfile -File "$(wslpath -w .)\.codex\preflight.ps1" -State "Connecticut4"
```


Fix a single root cause at a time (cwd/import/data), then re‑run.
When preflight is clean and the Plan is printed, reply READY (WSL).

4) Plan → Implement → Verify → Document (the loop)

Plan (short, explicit): files to touch and why; keep diffs minimal.

Implement: follow utils.path_handler; respect the data‑contract rules.

Verify: compile + optional smoke boot

```bash
python3 -m py_compile $(git ls-files '*.py') || true
# optional: 120s headless boot
# STREAMLIT_BROWSER=none streamlit run src/app.py & sleep 120; pkill -f streamlit
```


Document: always append to

docs/AAT9_KIT/AAT9_Unified_Changelog.md (one line, concise)

and any affected KIT docs.

**Shareable V-TRAC artifacts**
```bash
# Regenerate summaries, compact scores, and optional ZIP bundle
python TOOLS/run_vtrac_share_bundle.py
```
- Publishes `summary.md`, `summary.csv`, `vtrac_compact_report.{csv,json}`, and (optionally) `vtrac_validation_full_payload.zip` under `data/outputs/analysis/vtrac_validation/`.
- The scorer honours `configs/vtrac_score_config.json` (weights, column priors, state priors). Tweak that file or pass `--config` directly if you need a tuning sandbox.
- Manual invocation (for ad-hoc folders):
  ```bash
  python TOOLS/vtrac_score_and_export.py data/outputs/analysis/vtrac_validation \
      --config configs/vtrac_score_config.json \
      --out-dir data/outputs/analysis/vtrac_validation --verbose
  ```
- Commit locally; push via GitHub Desktop; share the `https://raw.githubusercontent.com/...` links (text files only) with reviewers.

5) Git workflow (Desktop only)

Edit in WSL; commit/push in GitHub Desktop (same WSL path).

GitHub Desktop reliability note (important):
- Desktop can hang on very large commits (lots of CSV/JSON/HTML) because it tries to diff/render everything.
- For **sharepacks** and other large artifact batches, prefer **CLI commit** (WSL) and then use Desktop only to **push** (or push via CLI).
- Repo guard: `.gitattributes` forces LF for text and treats `sharepacks/**/*.csv|json|html` as binary to reduce Desktop diff load.

Local checkpoint (only if asked; no editor popup):

```bash
git add -A
git commit -m "checkpoint: WSL startup doc finalized"
# prefer pushing in GitHub Desktop
```

Safer checkpoint pattern (recommended):
- Commit “code/docs” separately from “sharepacks day” so review/reverts stay clean.
- Avoid committing the staged working workbook unless you explicitly intend to:
  - `data/original/Pick3StatsC4.xlsm` is an active staging file and is usually not part of a checkpoint.

Example (sharepacks day only; no push):
```bash
D=2025-06-22
git status -s
git add "sharepacks/$D" "docs/AAT9_KIT/FINAL VALIDATION/final docs" scripts/tools
git restore --staged data/original/Pick3StatsC4.xlsm 2>/dev/null || true
git commit -m "checkpoint: sharepacks $D + validation workflow fixes"
```

Clutter/retention policy (recommended):
- Treat `sharepacks/<D>/` as the **frozen day** snapshot; do not “commit-all” large runs. Stage only the day(s) you intend to checkpoint.
- If you need to re-run/experiment without polluting Git history, use `sharepacks/_legacy/` (gitignored) until you’re happy.
- When derived summaries/evals are refreshed (e.g., `summary.md` blocks or `control_center/profit_alerts_eval.*`), commit them in a dedicated “refresh summaries/evals” commit so changes stay auditable.


Never edit Git remotes/config. Never write outside the repo.

6) Guardrails (for Codex)

Allowed without asking:

Read/list anywhere inside the repo

Edit under docs/**, .codex/** (docs, logs, images)

python3 -m py_compile, the preflight command above

Ask first:

Edits under src/**, modules/**, utils/**, alpha_analytical/**

Any Streamlit run beyond the optional 120s smoke boot

Any Git operation beyond read‑only status printouts

Never:

Change origin or any remotes

Write outside the repository tree

7) Troubleshooting quickies

VS Code shows old changes but Desktop is clean? VS Code Git noise—Desktop is the source of truth.
Push/commit feels “stuck”? Clear stale flows/locks then return to Desktop:

```bash
[ -f .git/index.lock ] && rm -f .git/index.lock
git rebase --abort 2>/dev/null || true
git merge  --abort 2>/dev/null || true
git am     --abort 2>/dev/null || true
git cherry-pick --abort 2>/dev/null || true
git status -sb
```

8) Finish signal

When the Plan is printed and Preflight is clean, reply:

READY (WSL)
