@echo off
:: ======================================================
:: AAT9 - WSL + VS Code + GitHub Desktop Startup Script
:: ======================================================

:: Kill any stray VS Code processes
echo Closing any open VS Code windows...
taskkill /F /IM Code.exe 2>nul

:: Shut down WSL cleanly
echo Resetting WSL instance...
wsl --shutdown

:: Launch Ubuntu, open the repo in WSL, start Codex CLI and VS Code
echo Starting Ubuntu and opening repo in VS Code (WSL)...
wsl.exe -d Ubuntu bash -lc ^
"cd ~/code/Alpha-Analytical-Tool-Clone && \
 git status -s && git remote -v && pwd && \
 code -r . && \
 codex"

:: Optional: Start GitHub Desktop (if installed)
echo Launching GitHub Desktop...
start "" "%LOCALAPPDATA%\GitHubDesktop\GitHubDesktop.exe"

echo ------------------------------------------------------
echo AAT9 environment launched successfully!
echo ------------------------------------------------------
pause
