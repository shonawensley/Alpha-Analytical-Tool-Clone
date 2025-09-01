# GitHub Desktop: Daily Workflow & Quick Tasks (Clone repo)

Your repo (local folder): C:\dev\Alpha-Analytical-Tool

Remote (origin): https://github.com/shonawensley/Alpha-Analytical-Tool-Clone.git (the Clone repo)

## Daily checkpoint (3 clicks)
- Open GitHub Desktop → review changed files
- Bottom‑left Summary: write a message, e.g., `checkpoint: <what changed>` → Commit to main
- Top bar: Push origin
- Verify: On GitHub.com (Clone repo page), the top line above the file list shows your commit message; click it to see details. Or click “X commits” near `main • 1 branch • …` to view history

## Common tasks
- Fetch latest from GitHub: Top bar Fetch origin → Pull (if offered)
- Undo last local commit (not pushed): Menu Repository → Undo last commit
- Discard a file’s local changes: Right‑click file in Changes → Discard changes
- See/Change the remote URL: Repository → Repository settings → Remote (must end with `…Tool-Clone.git`)
- Rename the repo label in sidebar: Desktop uses your folder name
- To show “Clone” in the sidebar: rename folder in Explorer to `C:\dev\Alpha-Analytical-Tool-Clone`, then in Desktop File → Add local repository… and point to the renamed folder (remove the old entry via Repository → Remove – does not delete files)
- Check the remote without the web: Repository → Open in Command Prompt → `git remote -v` (read‑only)

## “No freezes” settings & habits
- Do Git in GitHub Desktop, not inside editors/terminals that may hide auth popups
- Keep the repo outside OneDrive paths; short paths help (e.g., `C:\dev\…`)
- Keep big generated files out of Git via `.gitignore` (hygiene rules already included)
- If Git asks to sign in again, Desktop will show a browser auth – complete it once, then pushes work
