# Codex Boot Contract — AAT9 (Universal, Desktop-first)

**Working dir**: `C:\dev\Alpha-Analytical-Tool\`

**Session config**
/config model_reasoning_effort=high
/config yolo=false

**Quick checks (print outputs)**
- git status -s
- git branch -vv
- git remote -v   # must show origin → https://github.com/shonawensley/Alpha-Analytical-Tool-Clone.git

**Operating rules**
1. Think → write a short checkbox plan; wait for **Approved**.
2. Small diffs only; security sanity before commit.
3. Do **not** change Git remotes or push.
4. Do **not** run Linux tools on Windows; use PowerShell-native when needed.
5. When a change is ready, show the diff and STOP. I will commit/push via GitHub Desktop.

**Guardrails (edits allowed)**
- modules/module_d_auxiliary_tools/**
- scripts/**
- tests/**
- briefings/**

Must not edit:
- core_legacy/**
- git remotes or repo config