@echo off
echo Alpha Analytical Tool Reorganization
echo ==================================
echo.
echo This will organize your project according to the new structure.
echo Original files will remain in place while copies are made to the new directories.
echo.
pause

REM Create archive directory in batch if it doesn't exist
mkdir batch\archive 2>nul
echo Created batch archive directory.

REM Create archive directory in scripts if it doesn't exist
mkdir scripts\archive 2>nul
echo Created scripts archive directory.

REM Move batch files to archive
echo Moving batch files to archive...
move run_clustering_app_2.bat batch\archive\ 2>nul
move run_vtrac_test.bat batch\archive\ 2>nul
move run_simple_pattern_analyzer.bat batch\archive\ 2>nul
move run_pattern_highlighter.bat batch\archive\ 2>nul
move run_stable_pattern_test.bat batch\archive\ 2>nul
move run_streamlit_auto_analyzer.bat batch\archive\ 2>nul
move run_auto_pattern_analyzer.bat batch\archive\ 2>nul
move run_table_formatter.bat batch\archive\ 2>nul

REM Move scripts to archive (preserving originals)
echo Moving scripts to archive...
xcopy scripts\Untitled-2.py.bak scripts\archive\ /Y 2>nul
xcopy scripts\clustering_app_2.py scripts\archive\ /Y 2>nul
xcopy scripts\clustering_app_2_new.py scripts\archive\ /Y 2>nul
xcopy scripts\vtrac_analyzer.py scripts\archive\ /Y 2>nul
xcopy scripts\advanced_vtrac_analyzer.py scripts\archive\ /Y 2>nul
xcopy scripts\test_vtrac.py scripts\archive\ /Y 2>nul
xcopy scripts\vtrac_test_app.py scripts\archive\ /Y 2>nul
xcopy scripts\simple_pattern_highlighter.py scripts\archive\ /Y 2>nul
xcopy scripts\vtrac_html_test.py scripts\archive\ /Y 2>nul
xcopy scripts\test_vtrac_streamlit.py scripts\archive\ /Y 2>nul
xcopy scripts\generate_sample.py scripts\archive\ /Y 2>nul
xcopy scripts\test_vtrac_interactive.py scripts\archive\ /Y 2>nul
xcopy scripts\test_components.py scripts\archive\ /Y 2>nul

echo.
echo Reorganization complete!
echo.
echo Core scripts are now in scripts\core\
echo Batch files are now in batch\
echo Documentation is in docs\guides\
echo.
echo You can now use the new batch files to run the applications:
echo - batch\run_enhanced_analyzer.bat
echo - batch\run_integrated_app.bat
echo.
pause 