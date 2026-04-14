$ErrorActionPreference = 'Stop'

$path = '.\codyssey-tracker\collect_v5_3_2.py'
if (!(Test-Path $path)) { throw "Not found: $path" }

Copy-Item $path "$path.bak_report_tables_$(Get-Date -Format yyyyMMdd_HHmmss)" -Force

$lines = Get-Content $path

# 1) 확정 자료 표 블록 (207~211) 교체
$block1Start = 206   # 0-based index for line 207
$block1Count = 5
$block1New = @(
"        lines.append('| 수강생 | 레포 | 업데이트 | cohort | phase | week | continuity | 판정 증거 |')",
"        lines.append('| --- | --- | --- | --- | --- | --- | --- | --- |')",
"        for item in sorted(by_week[week], key=lambda x: x['priority']):",
"            course = item.get('course', {})",
"            ev = ', '.join(course.get('evidence', [])[:4]) or '-'",
"            cohort = course.get('cohort_label', '-') or '-'",
"            phase = course.get('phase_label', '-') or '-'",
"            week_label = course.get('week_label', str(item.get('week', ''))) or '-'",
"            continuity = float(course.get('continuity_score', 0.0) or 0.0)",
"            lines.append(",
"                f""| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | """,
"                f""{item['updated_at']} | {cohort} | {phase} | {week_label} | {continuity:.2f} | {ev} |""",
"            )"
)

$before1 = @()
if ($block1Start -gt 0) { $before1 = $lines[0..($block1Start-1)] }
$after1 = $lines[($block1Start + $block1Count)..($lines.Count-1)]
$lines = @($before1 + $block1New + $after1)

# 2) 후보/검토 표 블록 (현재 줄번호는 첫 교체 후 밀리므로 문자열 검색으로 찾음)
$target = "            lines.append('| 수강생 | 레포 | 업데이트 | 신뢰도 | 근거 |')"
$idx = [Array]::IndexOf($lines, $target)
if ($idx -lt 0) { throw "Target block 2 start not found" }

$block2Count = 5
$block2New = @(
"            lines.append('| 수강생 | 레포 | 업데이트 | cohort | phase | week | continuity | 신뢰도 | 근거 |')",
"            lines.append('| --- | --- | --- | --- | --- | --- | --- | --- | --- |')",
"            for item in items:",
"                course = item.get('course', {})",
"                ev = ', '.join(course.get('evidence', [])[:5]) or '-'",
"                cohort = course.get('cohort_label', '-') or '-'",
"                phase = course.get('phase_label', '-') or '-'",
"                week_label = course.get('week_label', str(item.get('week', ''))) or '-'",
"                continuity = float(course.get('continuity_score', 0.0) or 0.0)",
"                confidence = float(course.get('confidence', 0.0) or 0.0)",
"                lines.append(",
"                    f""| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | """,
"                    f""{item['updated_at']} | {cohort} | {phase} | {week_label} | {continuity:.2f} | {confidence:.2f} | {ev} |""",
"                )"
)

$before2 = @()
if ($idx -gt 0) { $before2 = $lines[0..($idx-1)] }
$after2 = $lines[($idx + $block2Count)..($lines.Count-1)]
$lines = @($before2 + $block2New + $after2)

Set-Content $path -Value $lines -Encoding UTF8

Write-Host "Patched report table blocks."

python -m py_compile .\codyssey-tracker\collect_v5_3_2.py
python .\codyssey-tracker\collect_v5_3_2.py

Write-Host ""
Write-Host "=== report preview ==="
Get-Content .\codyssey-tracker\reports_v5_3_2\latest.md -TotalCount 260
