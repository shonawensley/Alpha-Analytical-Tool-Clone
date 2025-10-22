@echo off
echo Syncing repo and launching...
wsl.exe -d Ubuntu bash -lc "cd ~/code/Alpha-Analytical-Tool-Clone && git fetch origin && git pull --ff-only && powershell.exe -NoProfile -File \"$(wslpath -w .)\\run_app.bat\""
pause
