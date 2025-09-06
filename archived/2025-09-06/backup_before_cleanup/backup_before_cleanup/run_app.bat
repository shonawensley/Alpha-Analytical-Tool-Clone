@echo off
cd /d "%~dp0"
call .venv\Scripts\activate.bat
streamlit run scripts/utils/streamlit_app.py
pause 