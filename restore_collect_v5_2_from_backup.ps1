$ErrorActionPreference = 'Stop'

Set-Location 'D:\코디세이\ai-sw-workstation_patch'

$src = '.\codyssey-tracker\collect_v5_2.py.bak_fix_repo_state_20260414_203800'
$dst = '.\codyssey-tracker\collect_v5_2.py'

if (!(Test-Path $src)) { throw "Backup not found: $src" }

Copy-Item $src $dst -Force
Write-Host "Restored collect_v5_2.py from backup."

python -m py_compile .\codyssey-tracker\collect_v5_2.py
python -m py_compile .\codyssey-tracker\collect_v5_3_2.py

Write-Host ""
Write-Host "=== run ==="
python .\codyssey-tracker\collect_v5_3_2.py
