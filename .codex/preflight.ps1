$ErrorActionPreference = 'Stop'

param(
  [string]$State = ''
)

# Ensure we run from repo root (this script sits in .codex/)
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = Resolve-Path (Join-Path $here '..')
Set-Location $root
Write-Host ("CWD: " + (Get-Location).Path)

Write-Host "Python info:"
python -V
where python | Select-Object -First 1 | ForEach-Object { Write-Host ("python => " + $_) }

Write-Host "Import check (modules.blackapple):"
try {
  python -c "import modules.blackapple as ba, sys; print('BA from:', ba.__file__)"
} catch {
  Write-Host "BA import failed; check cwd and sys.path."
}

Write-Host "Listing draw CSVs under data/cleaned:"
if (Test-Path 'data/cleaned') {
  Get-ChildItem data/cleaned *_draws.csv | Select-Object Name, FullName
} else {
  Write-Host "No data/cleaned directory found."
}

if ($State) {
  function Normalize($s) { -join ($s.ToLower() -replace '[^a-z0-9]', '') }
  $want = Normalize $State
  $wantNo4 = Normalize (($State -replace '\d+$',''))
  $cands = Get-ChildItem data/cleaned *_draws.csv -ErrorAction SilentlyContinue
  $pick = $null
  foreach ($p in $cands) {
    $stem = ($p.BaseName -replace '_draws$','')
    $sn = Normalize $stem
    if ($sn -eq $want -or $sn -eq $wantNo4) { $pick = $p; break }
  }
  if (-not $pick) {
    foreach ($p in $cands) {
      $stem = ($p.BaseName -replace '_draws$','')
      $sn = Normalize $stem
      if ($sn -like "*$want*" -or $sn -like "*$wantNo4*") { $pick = $p; break }
    }
  }
  if ($pick) {
    Write-Host ("Selected CSV for state '" + $State + "': " + $pick.FullName)
  } else {
    Write-Host ("No matching *_draws.csv found for state '" + $State + "'.")
  }
}

Write-Host "Preflight complete."
