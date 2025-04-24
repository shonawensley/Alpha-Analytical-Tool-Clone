@echo off
title Clustering App 3 - Advanced Lottery Analysis
echo ================================================
echo = Clustering App 3 (Based on Enhanced Analyzer) =
echo = Includes:                                     =
echo = - Full Data Processing Pipeline               =
echo = - Advanced V-TRAC Analysis                    =
echo = - Expanded HTML Report View                   =
echo = - File Upload Capability                      =
echo ================================================
echo.

:: Change to the script's directory
cd /d "%~dp0"

:: Activate virtual environment
call .venv\Scripts\activate.bat

:: Clear port if needed
taskkill /F /IM streamlit.exe /T >nul 2>&1

echo Starting application...

:: Run the Streamlit app
streamlit run scripts/clustering_app_3.py --server.port 8522

:: In case of error, keep the window open
pause 