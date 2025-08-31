# Codex Boot Contract – AAT9

## Repo & working dir
- Always work at: C:\dev\Alpha-Analytical-Tool  (repo root)
- Before any work, run and show:
  - git status -s
  - git remote -v
  - git branch -vv

## Session config
- /config model_reasoning_effort=high
- /config yolo=false   # ask before running edits/commands

## Guardrails (scope)
- Allowed edits unless I say otherwise:
  - modules/module_d_auxiliary_tools/**
  - scripts/**
  - src/app.py  (Aux page only)
  - briefings/**
- Do **not** modify `core_legacy/**` or unrelated modules.

## Legacy import wiring (Aux only)
- Ensure legacy code is importable with a single call:
  ```python
  from modules.module_d_auxiliary_tools.refactored.bootstrap_imports import init as wire_legacy
  wire_legacy()

4) (Optional) reuse your Claude workflow docs without pasting

If you want Codex to follow those practices, add this one paragraph to the top of briefings\codex_boot.md (under the H1):

Follow the spirit of docs/CLAUDE_CODE/CLAUDE.md (7 rules: think → plan → review → implement small → audit → learn → wrap-up).
Do not auto-load those large prompts; just mirror the workflow: write a plan, wait for “Approved,” implement in small diffs, add a brief learning recap in the commit message when helpful.


This gives you the benefits of your Claude workflow without loading huge texts into Codex’s context.