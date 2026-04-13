$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonExe = Join-Path $env:LocalAppData 'Programs\Python\Python312\python.exe'

if (-not (Test-Path $pythonExe)) {
    throw "Python 3.12 non trovato in $pythonExe. Installa Python prima di lanciare questo setup."
}

& $pythonExe -m pip install --upgrade pip
& $pythonExe -m pip install -r (Join-Path $repoRoot 'requirements.txt')

Write-Host "Dipendenze installate nel Python locale: $pythonExe"
