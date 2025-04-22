Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Alpha Analytical Tool with V-TRAC Analyzer" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Change to scripts directory and run the app
Set-Location -Path "scripts"
streamlit run streamlit_app_with_analyzer_new.py

Write-Host ""
Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") 