@echo off
echo =====================================
echo = V-TRAC Analyzer (Fixed Version)   =
echo = Uses optimized table loading      =
echo =====================================
echo.

cd /d "%~dp0"
call .venv\Scripts\activate.bat
streamlit run scripts/vtrac_analyzer.py

pause 