@echo off
echo ================================================
echo = Enhanced V-TRAC Analyzer FINAL               =
echo = Includes:                                     =
echo = - Advanced V-TRAC Analysis                    =
echo = - Combined Table Integration                  =
echo = - Optimized Table Loading                     =
echo ================================================
echo.

cd /d "%~dp0"
call .venv\Scripts\activate.bat

rem Clear port if needed
taskkill /F /IM streamlit.exe /T >nul 2>&1

echo Starting application...

rem Direct command to run Streamlit - Using the WORKING script
streamlit run scripts/streamlit_app_with_analyzer.py --server.port 8523

pause 