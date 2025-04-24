@echo off
echo ======================================
echo V-TRAC Pattern Analysis Tool
echo ======================================
echo.

REM Change to script directory
cd /d "%~dp0"

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Install/upgrade required packages
pip install -q streamlit pandas numpy matplotlib

REM Run the analyzer
streamlit run scripts/vtrac_analyzer.py

if %ERRORLEVEL% NEQ 0 (
  echo Error running V-TRAC Analyzer!
  echo.
  echo Please check that all data files are in place and try again.
  echo.
)

echo.
echo Press any key to close this window...
pause > nul 