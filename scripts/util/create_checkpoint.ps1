param(
    [string]$DestinationRoot = '.codex/checkpoints'
)

$ErrorActionPreference = 'Stop'

$root = (Get-Location).Path

if (-not (Test-Path $DestinationRoot)) {
    New-Item -ItemType Directory -Path $DestinationRoot -Force | Out-Null
}

$timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$zipPath = Join-Path $DestinationRoot "backup_$timestamp.zip"

Write-Host "Creating checkpoint at $zipPath ..."

$files = Get-ChildItem -Path $root -Recurse -File -Force |
    Where-Object {
        $_.FullName -notmatch [regex]::Escape([IO.Path]::Combine($root, '.git')) -and
        $_.FullName -notmatch [regex]::Escape([IO.Path]::Combine($root, '.codex', 'checkpoints'))
    }

if (-not $files) {
    throw "No files found to archive."
}

Compress-Archive -Path $files.FullName -DestinationPath $zipPath -Force

Write-Host "Checkpoint created: $zipPath"
