@echo off
cd /d "%~dp0"

echo Running Stable Pattern Analyzer...
streamlit run scripts/core/stable_pattern_analyzer_standalone.py
 
pause 