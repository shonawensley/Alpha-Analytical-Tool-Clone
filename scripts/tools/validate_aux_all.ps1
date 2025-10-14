# Validate Aux surfaces before launching Streamlit
param(
    [string[]]$DoubleStates = @('Connecticut4', 'Florida4'),
    [string[]]$RepeatStates = @('Connecticut4', 'Florida4'),
    [string[]]$VtracStates  = @('Connecticut4')
)

$ErrorActionPreference = 'Stop'

function Invoke-AuxValidationCommand {
    param(
        [string]$Message,
        [string[]]$CommandArgs
    )

    Write-Host $Message
    Write-Host ("Command: python {0}" -f ($CommandArgs -join ' '))
    $previousPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    $output = & python @CommandArgs 2>&1
    $exitCode = $LASTEXITCODE
    $ErrorActionPreference = $previousPreference
    $output | ForEach-Object { Write-Host $_ }
    if ($exitCode -ne 0) {
        throw "Aux validation command failed: $($CommandArgs -join ' ')"
    }
}

Invoke-AuxValidationCommand -Message "[Aux validation] Checking doubles/pairs..." -CommandArgs (@("scripts/tools/validate_aux_doubles.py") + $DoubleStates + @("--max-n", "1000"))

Invoke-AuxValidationCommand -Message "[Aux validation] Checking repeat-watch / positional shortlist..." -CommandArgs (@("scripts/tools/validate_aux_repeat.py") + $RepeatStates + @("--max-n", "1000", "--window", "150", "--shortlist-limit", "5"))

Invoke-AuxValidationCommand -Message "[Aux validation] Checking V-TRAC overlays / heatboard / sums..." -CommandArgs (@("scripts/tools/validate_aux_vtrac.py") + $VtracStates + @("--max-n", "1000", "--window", "150", "--limit", "10"))

Write-Host "[Aux validation] All checks completed."
