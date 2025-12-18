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
- Workflow changelog (“fix later” capture): `docs/AAT9_KIT/FINAL VALIDATION/final docs/WORKFLOW_CHANGELOG.md`
- Final validation checklist (guardrails + design notes): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Checklist.md`
- Control Center / Brain 2 reference (keep for later): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md`

Optional (brainstorm / historical templates; not SSOT):
- `docs/AAT9_KIT/FINAL VALIDATION/FINAL_VALIDATION_TEMPC.md`

## Run reports (filled answers live here)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`

Generate a run report scaffold:
```bash
python3 scripts/tools/create_master_validation_run_report.py --date YYYY-MM-DD --state OntarioCanada4
```

Per-run workflow (high level):
1) Generate/verify sharepack artifacts (see help + preflight).
2) Generate the run report scaffold (command above).
3) Fill the run report Parts 1–5 (using embedded `summary.md` evidence blocks).
4) Log “fix later” items to `WORKFLOW_CHANGELOG.md` so they aren’t lost.

## Operational guides
- Entry (contracts + semantics): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`
- Preflight / drift guards: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Preflight.md`
- Workflow architecture map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`

## Key references
- Lean outputs index: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Analyzer_Lean_Outputs.md`
- VTRAC permutations + VSTRAIGHTS reference: `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`
