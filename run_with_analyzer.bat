@echo off
echo ================================
echo = Alpha Analytical Tool (v1.0) =
echo ================================
echo.

cd /d "%~dp0"
call .venv\Scripts\activate.bat
streamlit run scripts/streamlit_app_with_analyzer.py

echo.
echo App closed. Press any key to exit...
pause > nul 