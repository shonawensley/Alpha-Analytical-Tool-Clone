@echo off
echo ==================================================
echo Launching Codex CLI in WSL Ubuntu Environment...
echo ==================================================

:: Launch Ubuntu, cd into repo root, and start Codex in VS Code
wsl.exe -d Ubuntu bash -lc ^
"cd ~/code/Alpha-Analytical-Tool-Clone && \
git status -s && git branch -vv && git remote -v && pwd && \
echo ----------------------------------------------- && \
echo Starting Codex CLI Session && \
echo ----------------------------------------------- && \
powershell.exe -NoProfile -File \"$(wslpath -w .)\.codex\preflight.ps1\" -State \"Connecticut4\" && \
code ."

pause
