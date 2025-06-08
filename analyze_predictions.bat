@echo off
echo ================================
echo V-TRAC Prediction Analysis Tool
echo ================================
echo.

cd /d "%~dp0"

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Running prediction analysis...
python scripts\analyze_predictions_vs_winners.py

echo.
echo Analysis complete! Check the output files.
pause 