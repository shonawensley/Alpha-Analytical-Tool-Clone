# Validate Aux surfaces before launching Streamlit
param(
    [string[]]$DoubleStates = @('Connecticut4', 'Florida4'),
    [string[]]$RepeatStates = @('Connecticut4', 'Florida4'),
    [string[]]$VtracStates  = @('Connecticut4')
)

$ErrorActionPreference = 'Stop'

Write-Host "[Aux validation] Checking doubles/pairs..."
python scripts/tools/validate_aux_doubles.py $DoubleStates --max-n 1000 | Write-Host

Write-Host "[Aux validation] Checking repeat-watch / positional shortlist..."
python scripts/tools/validate_aux_repeat.py $RepeatStates --max-n 1000 --window 150 --shortlist-limit 5 | Write-Host

Write-Host "[Aux validation] Checking V-TRAC overlays / heatboard / sums..."
python scripts/tools/validate_aux_vtrac.py $VtracStates --max-n 1000 --window 150 --limit 10 | Write-Host

Write-Host "[Aux validation] All checks completed."
