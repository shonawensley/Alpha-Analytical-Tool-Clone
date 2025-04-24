@echo off
echo ================================================
echo = Enhanced Lottery Processor with V-TRAC Analyzer =
echo = Includes:                                      =
echo = - Full Data Processing Pipeline                =
echo = - Advanced V-TRAC Analysis                     =
echo = - Combined Table Integration                   =
echo = - Optimized Table Loading                      =
echo ================================================
echo.

cd /d "%~dp0"
call .venv\Scripts\activate.bat
streamlit run scripts/streamlit_app_with_analyzer.py

pause 