$ErrorActionPreference = 'SilentlyContinue'
Write-Host 'Stopping streamlit/python...'
Stop-Process -Name streamlit -Force
Stop-Process -Name python -Force
# Also try killing anything on 8501/8502
$ports = 8501,8502
foreach ($p in $ports) {
  Get-NetTCPConnection -LocalPort $p -ErrorAction SilentlyContinue | ForEach-Object { try { Stop-Process -Id $_.OwningProcess -Force } catch {} }
}
Write-Host 'Done.'
