# GitHub Desktop: Daily Workflow & Quick Tasks (WSL repo)

WSL repo root (canonical): `/home/ser/code/Alpha-Analytical-Tool-Clone`

Remote (origin): https://github.com/shonawensley/Alpha-Analytical-Tool-Clone.git (the Clone repo)

## Daily checkpoint (3 clicks)
- Open GitHub Desktop → review changed files
- Bottom‑left Summary: write a message, e.g., `checkpoint: <what changed>` → Commit to main
- Top bar: Push origin
- Verify: On GitHub.com (Clone repo page), the top line above the file list shows your commit message; click it to see details. Or click “X commits” near `main • 1 branch • …` to view history

GitHub Desktop repo path (Windows view of the same WSL tree):
- `\\wsl$\Ubuntu\home\ser\code\Alpha-Analytical-Tool-Clone`

## Common tasks
- Fetch latest from GitHub: Top bar Fetch origin → Pull (if offered)
- Undo last local commit (not pushed): Menu Repository → Undo last commit
- Discard a file’s local changes: Right‑click file in Changes → Discard changes
- See/Change the remote URL: Repository → Repository settings → Remote (must end with `…Tool-Clone.git`)
- Rename the repo label in sidebar: Desktop uses your folder name
- Check the remote without the web: Repository → Open in Command Prompt → `git remote -v` (read‑only)

## “No freezes” settings & habits
- GitHub Desktop can freeze on very large commits (many CSV/JSON/HTML diffs), especially `sharepacks/`.
- Prefer **WSL CLI commits** for large artifact batches; use Desktop mainly to **push** (or push via CLI).
- Repo guardrails:
  - `.gitattributes` forces LF for text and treats large `sharepacks/**` artifacts as binary to reduce Desktop diff load.
  - `.gitignore` excludes live outputs (`data/outputs/**`, `reports/**`) so only frozen sharepacks are versioned.
- If Git asks to sign in again, Desktop will show a browser auth – complete it once, then pushes work

## Recommended checkpoint patterns (beginner-friendly)

1) Code/docs checkpoint (small, easy review)
- Commit: changes under `src/`, `modules/`, `scripts/`, `docs/`, `briefings/`
- Avoid: `sharepacks/` (too large for frequent “tiny” commits)

2) Sharepack day checkpoint (big artifacts)
- Commit one day at a time: `sharepacks/<D>/`
- If Desktop hangs, do the commit in WSL:
  ```bash
  D=2025-06-22
  git status -s
  git add "sharepacks/$D" scripts/tools "docs/AAT9_KIT/FINAL VALIDATION/final docs" briefings
  git restore --staged data/original/Pick3StatsC4.xlsm 2>/dev/null || true
  git commit -m "checkpoint: sharepacks $D"
  ```
  Then push from Desktop (or `git push` from WSL).
