@echo off
ECHO Running Stable Pattern Analysis Test
pushd ..
python scripts/stable_pattern_analysis_demo.py data/ai_exports/OntarioCanada4_ai_format_20250403_030615.json
popd
ECHO Test complete
PAUSE 