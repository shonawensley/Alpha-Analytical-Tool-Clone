@echo off
ECHO Running Automatic Pattern Analyzer
pushd ..
python scripts/auto_pattern_analyzer.py data/ai_exports/OntarioCanada4_ai_format_20250403_030615.json
popd
ECHO Analysis complete
PAUSE 