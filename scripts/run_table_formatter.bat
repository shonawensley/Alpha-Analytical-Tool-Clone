@echo off
ECHO Running Table Formatter Demo
pushd ..
python scripts/table_formatter_demo.py data/ai_exports/OntarioCanada4_ai_format_20250403_030615.json
popd
ECHO Demo complete
PAUSE 