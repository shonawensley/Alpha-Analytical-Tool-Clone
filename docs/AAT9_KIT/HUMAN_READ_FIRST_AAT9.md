# HUMAN READ FIRST — AAT9 Quick Instructions

Use these steps at the start of a session to set Codex up correctly and avoid path issues.

## 1) Start Codex with AAT9 boot line
- Run: `TOOLS\codex_start_aat9.bat`
- Paste the clipboard line into Codex:
  - “Read briefings\CODEX_READ_FIRST_AAT9.md and follow it exactly. After preflight + quick checks, reply: READY.”

## 2) Run preflight (from repo root)
- `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"`
- Check that imports resolve inside your repo and `data/cleaned/*_draws.csv` files exist.

## 3) Launch the app
- Use: `run_app.bat`
- The app runs at: `src\app.py`

## 4) Where to read more (when needed)
- Curated docs index: `docs/AAT9_KIT/AAT9_KIT_README.md`
- Quickstart Cheat Sheet: `docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md`
- Workflow Standard + Task Template: `docs/AAT9_KIT/AAT9_Workflow_Standard.md`, `docs/AAT9_KIT/AAT9_Task_Template.md`
- Practices: coding standards, agent rules, pitfalls: `docs/AAT9_KIT/Practices/*`

That’s it. These quick steps ensure a clean start every time and guide Codex to the optimal workflow and docs.



________

for human additional:

What I added to support your ideas

- AAT9_Checkpoint_Log.md (running, detailed log)
    - Location: docs/AAT9_KIT/AAT9_Checkpoint_Log.md
    - Purpose: A single, date-tagged checkpoint log with deeper explanations (context, rationale, impact) that complement the one-line Unified Changelog.
    - Template included; I seeded an example for the preflight “tables check” and new startup docs.
    - Template included; I seeded an example for the preflight “tables check” and new startup docs.
-
AAT9_Post_Implementation_Checklist.md (standardized wrap-up)
    - Location: docs/AAT9_KIT/AAT9_Post_Implementation_Checklist.md
    - Purpose: The exact steps to run after a feature/fix (compile/import checks, optional headless boot & preflight, Update Changelog, Update Checkpoint Log, update diagrams/docs, handoff summary).
    - Trigger phrase: “document and process” — a single phrase you can use at the end of any implementation. Agents should interpret this as “run the post-implementation checklist and return links/log tail.”
-
Updated workflow standard with the trigger and checkpoint
    - docs/AAT9_KIT/AAT9_Workflow_Standard.md now references:
    - Checkpoint Log as required for deeper notes
    - Trigger phrase “document and process” for AI to execute the post-implementation checklist

- Preflight enhancement (optional Stable/DR/V‑TRAC)
    - .codex/preflight.ps1 now supports -CheckTables to quickly confirm tables root and optional state directory presence:
    - Example: powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4" -CheckTables

Why this makes building cleaner

- Single path for agents and devs: TOOLS\codex_start_aat9.bat + CODEX_READ_FIRST_AAT9.md ensures every session lands in the AAT9 KIT, runs preflight, and follows the same Plan → Implement → Verify → Document
flow.
- Zero ambiguity on docs: KIT is the living source (Quickstart, Workflow, Practices, Preflight, Diagrams, Changelog, Checkpoint Log), with light banners steering away from outdated entry points.
- Documentation “automation”: The trigger phrase “document and process” is your simple verbal switch. An AI can always use it to:
    - Update the Unified Changelog entry
    - Append a clear, structured note to the Checkpoint Log
    - Update diagrams/docs if structure/wiring changed
    - Run optional preflight/headless boot and attach a short log tail
- Path and data safety: Preflight catches path/import drift in seconds; -CheckTables gives a quick pulse check for tables when needed; BA’s absolute-path loader prevents name collisions.

On your Phase‑2 Aux audit

- Your instinct is right — hold off until you’ve added the next Aux tools. Later, I can produce a read‑only inventory and a precise move map to archive any remaining runnable legacy scripts under modules/
module_d_auxiliary_tools (keeping importable library code intact). That avoids churn while you’re still building Aux.

Next steps (if you want)

- Start your next feature. At the end, say “document and process,” and I’ll run the standardized wrap-up (update Changelog + Checkpoint, preflight/headless if helpful, and post links/logs).
- If you want me to create a tiny “KIT pointer” in a few more legacy AAT9 docs, I can do that safely, but it’s optional now that we have READ_FIRST, banners, and KIT.

You’re in great shape to proceed: the app is stable, the surface is clean, and the workflow is codified so both you and any AI can deliver consistently and safely.

