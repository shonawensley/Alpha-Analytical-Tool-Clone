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

## Current Analysis Arena Path (preferred)

If you are working on the rebuilt Analysis Arena branch, start here:

- Arena branch map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena active system index: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__SYSTEM_INDEX.md`
- Arena metric legend: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__METRIC_LEGEND.md`
- Arena fresh-window reading guide: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__HOW_TO_READ_FRESH_WINDOW_RESULTS.md`
- Arena Stage 8 downstream rebuild readiness guardrail: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE8_DOWNSTREAM_REBUILD_READINESS.md`
- Arena Stage 7C / Stage 8A entry dossier: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER.md`
- Arena Stage 7C / Stage 8A machine appendix: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER__APPENDIX.json`
- Arena Stage 7C / Stage 8A mechanism appendix: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER__MECHANISM_APPENDIX.md`
- Arena Stage 7C / Stage 8A freeze receipt: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER__FREEZE_RECEIPT.md`
- Arena window replay / replication protocol: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_AND_REPLICATION_PROTOCOL.md`
- Arena available window replay inventory: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__AVAILABLE_WINDOW_REPLAY_INVENTORY.md`
- Arena window replay readiness report: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.md`
- Arena window replay comparison design: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`
- Arena window replay comparison report: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.md`
- Arena replay-plan guardrail check: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__REPLAY_PLAN_GUARDRAIL_CHECK.md`
- Arena evidence boundary / next-run map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__EVIDENCE_BOUNDARY_AND_NEXT_RUN_MAP.md`
- Arena gold-day / window inventory: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__GOLD_DAY_WINDOW_INVENTORY.md`
- Arena March replay runbook: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_REPLAY_RUNBOOK.md`
- Arena fresh-runs cadence: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md`
- Arena operating flow / diagram: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Arena macro findings log: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MACRO_FINDINGS_LOG.md`
- Arena tune-up diagnostics: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__TUNEUP_DIAGNOSTICS.md`
- Arena frontier negative-control study: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_STUDY.md`
- Arena fresh-window readiness report: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRESH_WINDOW_READINESS.md`
- Arena decay / carryover companion scorecard: emitted per window via `window-decay-close`
- Arena bonus-ball sidecar truth: `scripts/tools/create_bonus_ball_truth_report.py` + `data/results_bonus/YYYY-MM-DD.txt`
- Arena-era RUNS portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/PORTAL.md`
- Window-close reports now include:
  - performance / opportunity gap
  - deep hit analysis + hit roster
  - pure arena finalist / candidate scorecard
  - translator-learning ledger
  - C1/C2 frontier harness analysis + frontier cases
  - window deep analysis / Codex report
  - optional decay / carryover companion scorecard
- Per-state Master Validation: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Master Validation VTRAC appendix: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__VTRAC_REFERENCE_APPENDIX.md`
- Brain 2 operating template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation companion: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

Legacy note:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/` remains valuable for older v0.2 / v0.3 history and control-arm comparison.
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/` is the current home for arena-era fresh runs.

## Core docs (keep in sync)
- Arena per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Arena Brain 2 operating template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Arena Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Analysis navigator (how to review without getting lost): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`
- Pattern progression primer (concept training; survives context resets): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Pattern_Progression_Primer.md`
- Workflow changelog ("fix later" capture): `docs/AAT9_KIT/FINAL VALIDATION/final docs/WORKFLOW_CHANGELOG.md`
- Arena macro findings log (cross-window evidence memory): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MACRO_FINDINGS_LOG.md`
- Arena metric legend (layer ownership + allowed conclusions): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__METRIC_LEGEND.md`
- Arena fresh-window reading guide (fixed interpretation order): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__HOW_TO_READ_FRESH_WINDOW_RESULTS.md`
- Arena Stage 8 downstream rebuild readiness guardrail (candidate object / boxed-straight / budget sandbox timing): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE8_DOWNSTREAM_REBUILD_READINESS.md`
- Arena Stage 7C / Stage 8A entry dossier (pre-Stage-8 evidence boundary, permissions, blockers, fixtures, and fresh-window charter): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER.md`
- Arena Stage 7C / Stage 8A machine appendix (machine-usable contract for the dossier): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER__APPENDIX.json`
- Arena Stage 7C / Stage 8A mechanism appendix (bounded non-authorizing mechanism backlog): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER__MECHANISM_APPENDIX.md`
- Arena Stage 7C / Stage 8A freeze receipt (explicit signoff and next-action lock): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__STAGE7C_STAGE8A_ENTRY_DOSSIER__FREEZE_RECEIPT.md`
- Arena window replay / replication protocol (same-window replay vs archived replication vs true fresh confirmation): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_AND_REPLICATION_PROTOCOL.md`
- Arena available window replay inventory (read-only list of candidate rerun windows and caveats): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__AVAILABLE_WINDOW_REPLAY_INVENTORY.md`
- Arena window replay readiness report (machine-generated readiness matrix, source coverage, and baseline hashes): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.md`
- Arena window replay comparison design (baseline-vs-rerun comparison categories and Stage 6B-through-Stage 7B targets): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`
- Arena window replay comparison report (baseline-vs-candidate artifact ledger; currently candidate-pending): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.md`
- Arena replay-plan guardrail check (machine check for canonical same-window replacement-cycle shape): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__REPLAY_PLAN_GUARDRAIL_CHECK.md`
- Arena evidence boundary / next-run map (fresh vs archived vs same-window replay decision rules): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__EVIDENCE_BOUNDARY_AND_NEXT_RUN_MAP.md`
- Arena gold-day / window inventory (canonical Pick3StatsC4, results, decay-tail, and bonus-tail date reference): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__GOLD_DAY_WINDOW_INVENTORY.md`
- Arena March replay runbook (safe same-window replay procedure; no runtime effect): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_REPLAY_RUNBOOK.md`
- Arena cross-window rollup (system-level comparison memory): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__CROSS_WINDOW_ROLLUP.md`
- Arena tune-up diagnostics (ranking / tracker / doubles research package): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__TUNEUP_DIAGNOSTICS.md`
- Arena frontier negative-control study (promotion gate for frontier traits): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_STUDY.md`
- Arena fresh-window readiness report (preflight before new gold-day windows): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__FRESH_WINDOW_READINESS.md`
- Arena VTRAC appendix (optional advanced review companion): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__VTRAC_REFERENCE_APPENDIX.md`
- Arena decay / carryover companion scorecard (per-window delayed-resolution accounting): generated under each completed window root
- Arena bonus-ball sidecar truth (optional Fireball / Wild Ball / Superball research lane): generated under `reports/stable/bonus_ball_by_date/<D>/`
- Final validation checklist (guardrails + design notes): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Checklist.md`
- Control Center / Brain 2 reference (keep for later): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md`
- Control Center daily template (Brain-2, per day): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Control_Center_Daily_Template.md`

## Legacy / Control-Arm SSOT (avoid drift)
- RUNS portal (what to open next): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- v0.2 defaults/posture (what to run): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
- v0.2 integration log (why it changed): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`

Optional (brainstorm / historical templates; not SSOT):
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`
- `docs/AAT9_KIT/FINAL VALIDATION/FINAL_VALIDATION_TEMPC.md`

## Run reports (filled answers live here)
- Current arena-era runs home:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/`
  - Arena runtime receipts default to: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA/`
  - Arena portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/PORTAL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`
  - Resume/handoff rule (context resets): see `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Evaluate_Only_Quickstart.md` → “Context reset / handoff rule”.
  - Progress tracker (which reports are filled): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`
  - Curated “research packs” (for external review / ChatGPT Pro): `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/README.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/PREDICTIVE/`
  - Current arena-era predictive state reports + cross-state portfolio reports.
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/VALIDATION/`
  - Current arena-era daily validation shells such as Control Center, day synthesis, and window-scoped validation artifacts.

Generate an arena-native per-state Master Validation report scaffold:
```bash
python3 scripts/tools/create_master_validation_run_report.py --date YYYY-MM-DD --state OntarioCanada4
```
Default standalone output:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/<D>__<STATE>.md`
- Window runs should usually pass an explicit `--out` under the window `VALIDATION/` folder.

Generate an arena-native predictive run report (pre-results, no winners):
```bash
python3 scripts/tools/create_predictive_run_report.py --date YYYY-MM-DD --state OntarioCanada4 --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0
```
Default output:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/PREDICTIVE/<D>__<STATE>__PREDICTIVE__tool_only__arena_v0.md`

Run the renamed arena-era predictive cadence (recommended current pre-results wrapper):
```bash
python3 scripts/tools/run_analysis_arena_cycle.py pre --history-date YYYY-MM-DD --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --top-n-stable 10 --write-audit-evidence --play-card-write-md --force
```
This now emits:
- Brain 1 -> Brain 2 -> shadow DPL receipts
- translation sandbox seeds
- Candidate Universe / Play Card control-arm outputs
- Runtime receipts under `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA/`

Generate a predictive portfolio triage report (cross-state):
```bash
python3 scripts/tools/create_predictive_portfolio_report.py --date YYYY-MM-DD --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0
```
(Optional) Include Profit Alerts in a mixed-profile view:
```bash
python3 scripts/tools/create_predictive_portfolio_report.py --date YYYY-MM-DD --sharepacks-root sharepacks/_predictive --profile mixed --experiment-tag arena_v0
```
Default output:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/PREDICTIVE/<D>__PREDICTIVE_PORTFOLIO__<PROFILE>__arena_v0.md`

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

Generate an arena-native Control Center daily run report:
```bash
python3 scripts/tools/create_control_center_daily_run_report.py --date YYYY-MM-DD --predictive-sharepacks-root sharepacks/_predictive --truth-sharepacks-root sharepacks --profile tool_only --experiment-tag arena_v0
```
Default output:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/VALIDATION/<D>__CONTROL_CENTER.md`

Per-run workflow (high level):
1) Generate/verify sharepack artifacts (see help + preflight).
   - Interpretation note: a tool can “miss” the winner even when the pipeline is correct; treat that as evaluation signal, not corruption. (See: `AAT9_Final_Validation_Help.md` → “Pipeline vs tool outcome”.)
   - Optional (recommended for full-day freeze): export Control Center (Brain‑2) into `sharepacks/<D>/control_center/`:
     - `python3 scripts/tools/export_control_center_sharepack.py --date <D>`
   - Optional (recommended when future results files exist): evaluate Profit Alerts windowed episodes:
     - `python3 scripts/tools/evaluate_profit_alerts.py --date <D>`
   - Optional (recommended for Brain-2 day summary): scaffold the Control Center daily run report:
     - `python3 scripts/tools/create_control_center_daily_run_report.py --date <D>`
2) Generate the arena-native run report scaffold (command above).
3) Fill the run report Parts A–I using:
   - winners truth
   - raw string/context tool artifacts
   - aggregated analysis arena
   - translation sandbox
   - control-arm artifacts
   Optional per-tool `summary.md` files remain helper surfaces, but they are no longer the primary contract for the per-state report shell.
   - Optional: generate a paste-friendly winners JSON digest for Part A: `python3 scripts/tools/winners_json_digest.py --winners-dir sharepacks/<D>/<STATE>/winners/<STATE>`
4) Log “fix later” items to `WORKFLOW_CHANGELOG.md` so they aren’t lost.

## Operational guides
- Entry (contracts + semantics): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`
- Build + freeze (from scratch): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Build_Full_Day_Quickstart.md`
- Predictive day (no results yet): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Predictive_Day_Quickstart.md`
- Analysis Arena fresh-runs cadence: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md`
- Analysis Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
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
- Translation sandbox companion: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation companion: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- VTRAC permutations + VSTRAIGHTS reference: `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`
