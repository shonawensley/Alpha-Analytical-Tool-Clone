# Codex Boot Contract â€” Universal, Desktop-first

**Working dir**: `C:\dev\Alpha-Analytical-Tool`

**Session config (aim high)**  
/config model_reasoning_effort=high  
/config yolo=false    # ask before edits/commands

**Quick checks (print only)**
- git status -s
- git branch -vv
- git remote -v    # must show origin â†’ https://github.com/shonawensley/Alpha-Analytical-Tool-Clone.git

**Operating rules**
1. Think â†’ write a short checkbox plan; wait for **Approved**.
2. Implement in small diffs; show the /diff before any commit step.
3. **Do not** change Git remotes or push.
4. **Do not** run Linux tools on Windows; use PowerShell-native when needed.
5. When a change is ready, show the diff and STOP. The operator will commit/push via GitHub Desktop.

**Guardrails (edits allowed)**
- briefings/**
- docs/**
- scripts/**
- tests/**
- src/**           # allowed for task-specific code changes once the task file says so

**Must not edit**
- core_legacy/**
- git remotes or repo config

**Special one-off exception**
- If a briefings/* document (e.g., hygiene) explicitly asks to edit a root file (like `.gitignore`),
  you may propose the patch, show /diff, and STOP for operator commit via Desktop.
