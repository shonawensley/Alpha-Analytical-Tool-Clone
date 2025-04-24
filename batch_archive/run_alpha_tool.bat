@echo off
echo ======================================
echo Alpha Analytical Tool
echo ======================================
echo.

REM Change to script directory
cd /d "%~dp0"

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Install/upgrade required packages
pip install -q streamlit pandas numpy matplotlib seaborn plotly

REM Run the integrated app
streamlit run scripts/streamlit_app.py

if %ERRORLEVEL% NEQ 0 (
  echo Error running Alpha Analytical Tool!
  echo.
  echo Please check that all dependencies are installed and data files are in place.
  echo.
)

echo.
echo Press any key to close this window...
pause > nul 