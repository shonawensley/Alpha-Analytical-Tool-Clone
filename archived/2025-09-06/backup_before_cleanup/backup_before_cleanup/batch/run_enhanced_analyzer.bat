@echo off
echo Starting Enhanced V-TRAC Analyzer...
echo.

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Run the streamlit app
streamlit run scripts\core\enhanced_analyzer_final.py

REM Deactivate virtual environment
call deactivate 