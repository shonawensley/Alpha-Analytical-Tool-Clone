# Codex Boot Contract — Universal (WSL-first)

Status:
- This file is legacy; prefer `briefings/CODEX_READ_FIRST_AAT9_WSL_2.md` as the session entrypoint.

**Working dir (canonical)**: `/home/ser/code/Alpha-Analytical-Tool-Clone`

**Session config (aim high)**  
/config model_reasoning_effort=high  
/config yolo=false    # ask before edits/commands

**Quick checks (print only)**
- git status -s
- git branch -vv
- git remote -v    # must show origin → https://github.com/shonawensley/Alpha-Analytical-Tool-Clone.git

**Operating rules**
1. Think → write a short checkbox plan; wait for **Approved**.
2. Implement in small diffs; show the /diff before any commit step.
3. **Do not** change Git remotes.
4. Prefer running tools in WSL (avoid `/mnt/c/...` working copies).
5. Git operations:
   - OK: local `git status`, `git diff`, staging, and local commits when requested.
   - Push only when explicitly approved (and never change origin/remote settings).

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
  you may propose the patch, show /diff, and proceed with a local commit only if the operator approves.
Read briefings\codex_boot.md and follow it exactly. After config + quick checks, reply: READY.
