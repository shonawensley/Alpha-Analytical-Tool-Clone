param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]] $PytestArgs
)

$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$python = $env:PYTHON
if (-not $python) { $python = 'python' }
$paths = @($root, (Join-Path $root 'src'), (Join-Path $root 'scripts/auxiliary/working'))
if ($env:PYTHONPATH) { $paths += $env:PYTHONPATH }
$env:PYTHONPATH = [string]::Join([IO.Path]::PathSeparator, $paths)
$script = Join-Path $root 'scripts/run_acceptance.py'
& $python $script @PytestArgs
exit $LASTEXITCODE
