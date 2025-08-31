Param(
    [string]$Message = "",
    [string]$Remote = ""
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

# Ensure pager won't open interactive 'less' causing freezes
git config --global core.pager cat | Out-Null
git config --global pager.log false | Out-Null
git config --global pager.show-branch false | Out-Null
$env:GIT_PAGER = "cat"

# Determine timestamp and default message
$ts = Get-Date -Format 'yyyyMMdd_HHmmss'
if (-not $Message -or $Message.Trim().Length -eq 0) {
    $Message = "checkpoint: $ts"
}

# Ensure we are in a git repo
git rev-parse --is-inside-work-tree | Out-Null

# Ensure remote 'origin' exists; optionally add if provided
$haveRemote = $false
try {
    $remotes = (git remote) -split "\r?\n" | Where-Object { $_ -ne '' }
    if ($remotes -contains 'origin') { $haveRemote = $true }
} catch {
    $haveRemote = $false
}

if (-not $haveRemote) {
    if (-not $Remote -or $Remote.Trim().Length -eq 0) {
        Write-Host "No 'origin' remote configured and no -Remote provided. Skipping push; will create local commit + tag only." -ForegroundColor Yellow
    } else {
        git remote add origin $Remote
        git branch -M main | Out-Null
    }
}

# Stage, commit, tag
git add -A
git commit --allow-empty -m "$Message"
$tag = "v-checkpoint-$ts"
git tag -a $tag -m "$Message"

# Push if remote exists
if ($haveRemote -or ($Remote -and $Remote.Trim().Length -gt 0)) {
    git push -u origin HEAD:main
    git push origin --tags
    Write-Host "Created checkpoint tag $tag and pushed to origin." -ForegroundColor Green
} else {
    Write-Host "Created checkpoint tag $tag locally (no origin remote)." -ForegroundColor Yellow
}


