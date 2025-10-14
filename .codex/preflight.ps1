param(
  [string]$State = '',
  [switch]$CheckTables,
  [string]$TablesRoot = '',
  [switch]$CheckDoubles
)

Write-Host 'AAT9 Preflight (Windows)'
Write-Host '--------------------------------'
Write-Host ('CWD: ' + (Get-Location).Path)

try {
  $py = (Get-Command python -ErrorAction Stop).Source
  Write-Host ('Python: ' + $py)
} catch {
  Write-Warning 'python not found on PATH'
}

# Print key imports and their file locations
$code = @'
import importlib, json
mods = [
  ('utils.path_handler','utils.path_handler'),
  ('modules.blackapple','modules.blackapple'),
  ('modules.aux_loaders','modules.aux_loaders'),
  ('alpha_analytical.stable','alpha_analytical.stable'),
]
out = {}
for imp, name in mods:
    try:
        m = importlib.import_module(imp)
        out[name] = getattr(m, '__file__', 'NOFILE')
    except Exception as e:
        out[name] = f'IMPORT_ERROR: {e}'
print(json.dumps(out, indent=2))
'@

try {
  $imports = python -c $code
  Write-Host 'Imports:'
  Write-Host $imports
} catch {
  Write-Warning 'Failed to import one or more modules.'
}

# Draws CSV inventory
$cleaned = Join-Path (Get-Location) 'data/cleaned'
if (Test-Path $cleaned) {
  $drawsDir = Join-Path $cleaned 'draws'
  $drawDirs = @()
  if (Test-Path $drawsDir) { $drawDirs += (Resolve-Path $drawsDir).Path }
  if (Test-Path $cleaned) { $drawDirs += (Resolve-Path $cleaned).Path }
  $drawDirs = $drawDirs | Select-Object -Unique
  if ($drawDirs.Count -eq 0) {
    Write-Warning 'No draw directories found under data/cleaned.'
  } else {
    foreach ($dir in $drawDirs) {
      $csvs = Get-ChildItem $dir -Filter '*_draws.csv' -ErrorAction SilentlyContinue
      $label = if ($dir.StartsWith((Get-Location).Path, [System.StringComparison]::OrdinalIgnoreCase)) {
        $dir.Substring((Get-Location).Path.Length).TrimStart('\')
      } else {
        $dir
      }
      Write-Host ("draw inventory [" + $label + "]: " + ($csvs | Measure-Object).Count)
      $csvs | Select-Object -First 20 | ForEach-Object { ' - ' + $_.Name }
    }
  }
} else {
  Write-Warning 'data/cleaned not found.'
}


if ($CheckDoubles) {
  Write-Host "\nRunning doubles variant audit..."
  try {
    & python scripts/health/check_doubles_variants.py
  } catch {
    Write-Warning ("Doubles audit failed: " + $_.Exception.Message)
  }
}

if ($State) {
  # Resolve draws file via aux_loaders picker for the given state
  $code2 = @"
from pathlib import Path
from modules.aux_loaders import load_state_draws
draws, src = load_state_draws(r'$State')
print('State:', r'$State')
print('Source:', src)
print('Draws:', len(draws))
"@
  try {
    $sel = python -c $code2
    Write-Host "\nSelected state resolution:"
    Write-Host $sel
  } catch {
    Write-Warning 'State resolution failed.'
  }
}

# List cleaned Excel sheets (string-table inputs) if present
$cleaned_xlsx = Get-ChildItem (Join-Path (Get-Location) 'data/cleaned') -Filter '*_cleaned.xlsx' -ErrorAction SilentlyContinue
if ($cleaned_xlsx) {
  Write-Host ("\ncleaned Excel inventory: " + (($cleaned_xlsx | Measure-Object).Count))
  $cleaned_xlsx | Select-Object -First 20 | ForEach-Object { ' - ' + $_.Name }
}

# Optional combined tables check for Stable/DR/V-TRAC workflows
if ($CheckTables) {
  try {
    if (-not $TablesRoot) {
      $TablesRoot = python -c "import utils.path_handler as ph; import sys; sys.stdout.write(str(ph.get_tables_output_dir()))"
    }
  } catch {
    Write-Warning 'Could not resolve tables root via utils.path_handler.'
  }
  Write-Host "\nTables root: $TablesRoot"
  if ($TablesRoot -and (Test-Path $TablesRoot)) {
    $stateDirs = Get-ChildItem $TablesRoot -Directory -ErrorAction SilentlyContinue
    Write-Host ("tables state dirs: " + (($stateDirs | Measure-Object).Count))
    $stateDirs | Select-Object -First 15 | ForEach-Object { ' - ' + $_.Name }
    if ($State) {
      $stPath = Join-Path $TablesRoot $State
      if (Test-Path $stPath) {
        Write-Host ("State tables present: " + $stPath)
      } else {
        Write-Warning ("No tables dir for state: " + $State)
      }
    }
  } else {
    Write-Warning 'tables root not found.'
  }
}

Write-Host '--------------------------------'
Write-Host 'Tip: Use run_app.bat to launch the UI from repo root.'
