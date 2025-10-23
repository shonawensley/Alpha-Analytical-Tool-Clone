@echo off
echo ================================================
echo Syncing latest repo and launching Streamlit app
echo ================================================
wsl.exe -d Ubuntu bash -lc "cd ~/code/Alpha-Analytical-Tool-Clone && git fetch origin && git pull --ff-only && ./run_app.sh"
pause
