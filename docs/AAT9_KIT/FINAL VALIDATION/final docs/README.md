# Final Validation — “Final Docs” Portal (SSOT)

This folder is the **one place to start** for the Final Validation workflow.

## How To Use These Docs (so nothing feels “mystery”)
There are 3 “classes” of docs in this workflow:

1) **Operational (read/run)**
- These tell you **what commands to run**, what dates mean, and where artifacts live.
- You generally **do not “fill these out”**; you only edit them when the workflow changes.

2) **Per-run analysis (fill)**
- These are the **state/date** run reports you fill with answers (Parts 1–5).
- These are the artifacts you share with a second analyst without pasting raw outputs.

3) **Global memory (append)**
- These capture “don’t forget” guardrails + “fix later” ideas so you don’t lose them across context resets.

**Control Center (Brain 2) relationship**
- Brain 1 (state template runs) produces evidence + hypotheses.
- Any “this seems profitable / trackable across states” ideas should be logged to the **workflow changelog** now, then later promoted into Control Center trackers when you resume Brain 2 work.

## Core docs (keep in sync)
- Master template (questions only): `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`
- Analysis navigator (how to review without getting lost): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`
- Pattern progression primer (concept training; survives context resets): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Pattern_Progression_Primer.md`
- Workflow changelog (“fix later” capture): `docs/AAT9_KIT/FINAL VALIDATION/final docs/WORKFLOW_CHANGELOG.md`
- Final validation checklist (guardrails + design notes): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Checklist.md`
- Control Center / Brain 2 reference (keep for later): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md`
- Control Center daily template (Brain-2, per day): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Control_Center_Daily_Template.md`

## v0.2 / v0.3 posture SSOT (avoid drift)
- RUNS portal (what to open next): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- v0.2 defaults/posture (what to run): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
- v0.2 integration log (why it changed): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`

Optional (brainstorm / historical templates; not SSOT):
- `docs/AAT9_KIT/FINAL VALIDATION/FINAL_VALIDATION_TEMPC.md`

## Run reports (filled answers live here)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`
  - Resume/handoff rule (context resets): see `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Evaluate_Only_Quickstart.md` → “Context reset / handoff rule”.
  - Progress tracker (which reports are filled): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`
  - Per-day Control Center run report (Brain-2): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CONTROL_CENTER.md`
  - Curated “research packs” (for external review / ChatGPT Pro): `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/README.md`

Generate a run report scaffold:
```bash
python3 scripts/tools/create_master_validation_run_report.py --date YYYY-MM-DD --state OntarioCanada4
```

Generate a predictive run report scaffold (pre-results, no winners):
```bash
python3 scripts/tools/create_predictive_run_report.py --date YYYY-MM-DD --state OntarioCanada4 --sharepacks-root sharepacks/_predictive
```

Generate a predictive portfolio triage report (cross-state):
```bash
python3 scripts/tools/create_predictive_portfolio_report.py --date YYYY-MM-DD --sharepacks-root sharepacks/_predictive
```
(Optional) Include Profit Alerts (mixed profile):
```bash
python3 scripts/tools/create_predictive_portfolio_report.py --date YYYY-MM-DD --sharepacks-root sharepacks/_predictive --profile mixed
```

Generate a Candidate Universe (gradeable predictions) inside a predictive sharepack:
```bash
python3 scripts/tools/create_candidate_universe.py --date YYYY-MM-DD --sharepacks-root sharepacks/_predictive
```
(Optional) Profile variants (additive, measured; does not delete anything):
```bash
python3 scripts/tools/create_candidate_universe.py --date YYYY-MM-DD --sharepacks-root sharepacks/_predictive --profile mixed
python3 scripts/tools/create_candidate_universe.py --date YYYY-MM-DD --sharepacks-root sharepacks/_predictive --profile profit_only
```

Generate budgeted Play Cards (e.g., 12/24/36 combos) from Candidate Universe:
```bash
python3 scripts/tools/create_play_card.py --date YYYY-MM-DD --sharepacks-root sharepacks/_predictive --budgets 12,24,36
```
(Add `--write-md` to also write `play_card.md`.)
Play Cards include multiple strategies for controlled experiments: `play_box_first`, `analysis_prefix`, `convergence_box_first`, `conversion_box_first`.
(Optional) Generate Play Cards for a profile:
```bash
python3 scripts/tools/create_play_card.py --date YYYY-MM-DD --sharepacks-root sharepacks/_predictive --profile mixed --budgets 12,24,36
```

Grade Candidate Universe once results exist (writes only to RUNS):
```bash
python3 scripts/tools/grade_candidate_universe.py --date YYYY-MM-DD --sharepacks-root sharepacks/_predictive
```
(Optional) Grade a profile:
```bash
python3 scripts/tools/grade_candidate_universe.py --date YYYY-MM-DD --sharepacks-root sharepacks/_predictive --profile mixed
```

Grade Play Cards once results exist (writes only to RUNS):
```bash
python3 scripts/tools/grade_play_card.py --date YYYY-MM-DD --sharepacks-root sharepacks/_predictive
```
(Optional) Grade a profile:
```bash
python3 scripts/tools/grade_play_card.py --date YYYY-MM-DD --sharepacks-root sharepacks/_predictive --profile mixed
```

Roll up grades across all available days (RUNS):
```bash
python3 scripts/tools/rollup_candidate_universe_corpus.py
python3 scripts/tools/rollup_play_card_corpus.py
```
(Optional) Roll up a profile variant:
```bash
python3 scripts/tools/rollup_candidate_universe_corpus.py --profile mixed
python3 scripts/tools/rollup_play_card_corpus.py --profile mixed
```

Generate a Control Center daily run report scaffold:
```bash
python3 scripts/tools/create_control_center_daily_run_report.py --date YYYY-MM-DD
```

Per-run workflow (high level):
1) Generate/verify sharepack artifacts (see help + preflight).
   - Interpretation note: a tool can “miss” the winner even when the pipeline is correct; treat that as evaluation signal, not corruption. (See: `AAT9_Final_Validation_Help.md` → “Pipeline vs tool outcome”.)
   - Optional (recommended for full-day freeze): export Control Center (Brain‑2) into `sharepacks/<D>/control_center/`:
     - `python3 scripts/tools/export_control_center_sharepack.py --date <D>`
   - Optional (recommended when future results files exist): evaluate Profit Alerts windowed episodes:
     - `python3 scripts/tools/evaluate_profit_alerts.py --date <D>`
   - Optional (recommended for Brain-2 day summary): scaffold the Control Center daily run report:
     - `python3 scripts/tools/create_control_center_daily_run_report.py --date <D>`
2) Generate the run report scaffold (command above).
3) Fill the run report Parts 1–5 (using embedded `summary.md` evidence blocks).
   - Optional: generate a paste-friendly winners JSON digest for Part A: `python3 scripts/tools/winners_json_digest.py --winners-dir sharepacks/<D>/<STATE>/winners/<STATE>`
4) Log “fix later” items to `WORKFLOW_CHANGELOG.md` so they aren’t lost.

## Operational guides
- Entry (contracts + semantics): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`
- Build + freeze (from scratch): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Build_Full_Day_Quickstart.md`
- Predictive day (no results yet): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Predictive_Day_Quickstart.md`
- Candidate Universe (pre-results, gradeable predictions): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Candidate_Universe_Contract.md`
- Evaluate-only (sharepacks already built): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Evaluate_Only_Quickstart.md`
- Preflight / drift guards: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Preflight.md`
- Workflow architecture map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`

## Key references
- Lean outputs index: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Analyzer_Lean_Outputs.md`
- Aux coverage + legend: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Aux_Coverage_And_Legend.md`
- Research ledger (primitives taxonomy): `docs/AAT9_KIT/FINAL VALIDATION/final docs/SUPERBRAIN_PRIMITIVES.md`
- Profit alerts (A01–A12) integration notes: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_A01_A12_Integration_Notes.md`
- Profit alerts evaluation charter (variants/decay semantics): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`
- Profit alerts grading matrix (per‑AID “what is a hit”): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Grading_Matrix.md`
- VTRAC permutations + VSTRAIGHTS reference: `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`
