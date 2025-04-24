@echo off
echo ================================================
echo = Clustering App 3 (Based on Enhanced Analyzer) =
echo = Includes:                                     =
echo = - Full Data Processing Pipeline               =
echo = - Advanced V-TRAC Analysis                    =
echo = - Expanded HTML Report View                   =
echo = - File Upload Capability                      =
echo ================================================
echo.

cd /d "%~dp0"
call .venv\Scripts\activate.bat

rem Clear port if needed
taskkill /F /IM streamlit.exe /T >nul 2>&1

echo Starting application...

rem Direct command to run Streamlit
streamlit run scripts/clustering_app_3.py --server.port 8522

pause 