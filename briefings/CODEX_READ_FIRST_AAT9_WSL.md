# CODEX READ FIRST — AAT9 (WSL/Ubuntu Optimized)

Follow this sequence exactly each session. Goal: reliable setup, path‑safe execution, and consistent documentation.

---

## 0) Operating assumptions (WSL/Ubuntu)

- You are running inside **Ubuntu on WSL2** (Linux prompt like `ser@…:~$`).  
- Project root (CWD) is **`/home/ser/code/Alpha-Analytical-Tool-Clone`**.  
  - Never work under `/mnt/c/...` (slow I/O and path pitfalls).
- Windows paths are accessible via `wslpath` when needed (e.g., PowerShell scripts).

---

## 1) Session setup

- Model preset: **`gpt-5-codex` (High)**. Use Medium only for routine edits.
- Reasoning: high‑effort; _yolo=false_ (ask before destructive changes).
- Force CWD:
  ```bash
  cd ~/code/Alpha-Analytical-Tool-Clone
git status -s && git branch -vv && git remote -v && pwd
2) Read these (KIT first)

Read in this order and internalize rules/paths:

docs/AAT9_KIT/AAT9_KIT_README.md (index)

docs/AAT9_KIT/AAT9_Workflow_Standard.md (workflow)

docs/AAT9_KIT/Practices/AAT9_Coding_Standards.md (path‑safe coding)

docs/AAT9_KIT/Practices/AAT9_Agent_Operating_Rules.md (guardrails)

docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md (daily flow)

docs/AAT9_KIT/AAT9_Preflight_Reference.md (expected outputs)

docs/AAT9_KIT/AAT9_Diagrams_Guide.md (Mermaid updates)

docs/AAT9_KIT/AAT9_Unified_Changelog.md (how to log)

AGENTS.md and .codex/AGENTS.universal.md (project & universal rules)

Rule alignment for WSL:

Treat the repo root as /home/ser/code/Alpha-Analytical-Tool-Clone.

When invoking Windows‑only scripts (e.g., .ps1, .bat), use powershell.exe -NoProfile -File "<windows path>" and create the path with wslpath -w . when needed.
3) Preflight (run now)

Run the PowerShell preflight from Linux using powershell.exe:

powershell.exe -NoProfile -File "$(wslpath -w .)\.codex\preflight.ps1" -State "Connecticut4"


Fix exactly one failing root cause at a time (cwd/import/data), then re‑run.

Preflight must finish clean before coding.

If you prefer a shorthand and the user defined a preflight function, you may call:
preflight Connecticut4
3.5) Dev Health (optional)

Only toggle Dev Health in the Streamlit UI when explicitly requested.
Skip it during boot if it stalls or if this session doesn’t need UI checks.

App launch (Linux path): run the Streamlit entry directly:

# headless smoke (optional)
STREAMLIT_BROWSER=none python3 -m py_compile $(git ls-files '*.py') || true
streamlit run src/app.py


Windows .bat launchers are for Windows shells. When inside Ubuntu/WSL, prefer the direct streamlit run shown above.

4) Plan → Implement → Verify → Document

Plan: state the files you will edit and why; keep diffs minimal.

Implement: follow utils.path_handler for outputs; keep tools’ data contracts:

Aux/Blackapple: only data/cleaned/*_draws.csv (newest‑first strings).

V‑TRAC / Stable / Digit Reduction: combined string tables via utils.path_handler.

Verify:

python3 -m py_compile $(git ls-files '*.py') || true
# optional headless boot, timeboxed to 120s:
# STREAMLIT_BROWSER=none streamlit run src/app.py & sleep 120; pkill -f streamlit


Capture logs to .codex/first_boot.log when relevant.

Document:

Always append to docs/AAT9_KIT/AAT9_Unified_Changelog.md.

Update any affected KIT docs or diagrams.
5) Done checklist

App starts from streamlit run src/app.py without path/import errors.

All changes logged in AAT9_Unified_Changelog.md.

If structure/wiring changed, update architecture/app‑flow docs.
Guardrails & approvals (WSL‑aware)

Never write outside the repo.

Never edit Git remotes/config.

Ask before:

Changing analyzers, pipelines, or app wiring.

Launching long‑running jobs beyond the smoke checks.

Allowed without asking:

Docs under docs/**, .codex/**

python3 -m py_compile on touched files

Running the preflight command above

Path & tool hygiene (WSL)

Ensure Linux‑side tools are used: python3, pip3, node, npm, git.

Print versions (no mutation): python3 --version && pip3 --version && node -v && npm -v

Avoid /mnt/c/... paths for work (slow semantics).

Convert paths when calling Windows scripts:

powershell.exe -File "$(wslpath -w .)\path\to\script.ps1"
Finish signal

When preflight is clean and the Plan is printed, reply: READY (WSL), then proceed with the agreed scope.


### One‑line boot to use in Codex
Replace your previous line with this WSL‑specific one:



Read briefings/CODEX_READ_FIRST_AAT9_WSL.md and follow it exactly. Select model preset gpt‑5‑codex (High), run the WSL preflight command, then reply: READY (WSL).

> If you keep the old filename in your routine, you can also **rename** the file above to `briefings/CODEX_READ_FIRST_AAT9.md` so your old one‑liner still works. Just don’t maintain multiple competing “read‑first” docs—pick one.

---

## About your “health helpers”

- Keep **preflight** in this doc; it’s fast and deterministic.  
- Treat **Dev Health** as optional (turn it on only when you’re validating UI bindings). That avoids Codex getting stuck “hunting” for optional checks.

---

## FAQ (practical, based on your notes)

- **Do I lose anything by staying with GitHub Desktop control?**  
  No. You get the same history and remote; you simply point Desktop to the WSL path (`\\wsl$\Ubuntu\home\ser\code\Alpha-Analytical-Tool-Clone`). Codex won’t push unless you instruct it.

- **What if I want a Windows shortcut to open Codex in WSL?**  
  Create `TOOLS\codex_run.bat`:
  ```bat
  @echo off
  wsl.exe -d Ubuntu bash -lc "cd ~/code/Alpha-Analytical-Tool-Clone && codex"
