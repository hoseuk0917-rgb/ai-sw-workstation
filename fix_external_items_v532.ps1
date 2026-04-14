$ErrorActionPreference = 'Stop'

$target = '.\codyssey-tracker\collect_v5_3_2.py'
if (!(Test-Path $target)) {
  throw "File not found: $target"
}

Copy-Item $target "$target.fix2.bak_$(Get-Date -Format yyyyMMdd_HHmmss)" -Force

$code = Get-Content $target -Raw -Encoding UTF8

$old = @'
    client = base.init_genai()
    date_str = datetime.now(KST).strftime('%Y-%m-%d')
    lines = []
'@

$new = @'
    client = base.init_genai()
    date_str = datetime.now(KST).strftime('%Y-%m-%d')
    external_items = list((external_store or {}).get('materials', {}).values())
    lines = []
'@

if ($code.Contains($old)) {
  $code = $code.Replace($old, $new)
} else {
  throw "Target block not found for external_items insertion"
}

Set-Content $target -Value $code -Encoding UTF8

Write-Host "Fix applied."
python .\codyssey-tracker\collect_v5_3_2.py