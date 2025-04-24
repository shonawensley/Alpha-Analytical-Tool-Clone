@echo off
echo ================================================
echo = Enhanced V-TRAC Analyzer FINAL               =
echo = Includes:                                     =
echo = - Full Data Processing Pipeline               =
echo = - Original Enhanced Analyzer Processing       =
echo = - Identical V-TRAC Scoring Logic              =
echo = - Improved UI and Reporting                   =
echo ================================================
echo.

cd /d "%~dp0"
call .venv\Scripts\activate.bat

rem Clear port if needed
taskkill /F /IM streamlit.exe /T >nul 2>&1

echo Starting application...

rem Direct command to run Streamlit
streamlit run scripts/enhanced_analyzer_final.py --server.port 8523

pause 