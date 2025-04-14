@echo off
echo V-TRAC Enhanced Lottery Data Processor
echo ======================================
echo This is a TEST VERSION that includes the V-TRAC Analyzer
echo Your original working process is NOT affected

cd /d "%~dp0"
call .venv\Scripts\activate.bat
streamlit run scripts/streamlit_app_with_analyzer.py

echo.
echo App closed. Press any key to exit...
pause > nul 