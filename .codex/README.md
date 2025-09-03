Codex helper utilities for this repo

always_root.ps1

- Ensures the current PowerShell session is rooted at the project path before any ad‑hoc commands.
- Usage:
  - Right‑click “Run with PowerShell”, or:  .\.codex\always_root.ps1
  - Then run any python/streamlit/git commands; they will execute from the repo root.

first_boot.log

- Headless app boot logs are written here for quick diagnostics.

