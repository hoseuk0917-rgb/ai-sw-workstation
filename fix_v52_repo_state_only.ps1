$ErrorActionPreference = 'Stop'

$path = '.\codyssey-tracker\collect_v5_2.py'
if (!(Test-Path $path)) { throw "Not found: $path" }

Copy-Item $path "$path.bak_fix_repo_state_$(Get-Date -Format yyyyMMdd_HHmmss)" -Force

$code = Get-Content $path -Raw -Encoding UTF8

$old = @'
        repo_state = {
            'username': item['username'],
            'display_name': item.get('display_name'),
            'repo_name': item['repo_name'],
            'repo_url': item['repo_url'],
            'week_guess': str(item.get('week', '')),
            'course_guess': course.get('course_id'),
            'course_label': course.get('course_label'),
            'confidence': course.get('confidence'),
            'status': course.get('status'),
            'evidence': course.get('evidence', [])[:5],
            'first_seen_at': prev.get('first_seen_at', now_str),
            'last_seen_at': now_str,
            'updated_at': item.get('updated_at', ''),
            'seen_count': seen_count,
            'status_history': status_history,
        }
'@

$new = @'
        repo_state = {
            'username': item['username'],
            'display_name': item.get('display_name'),
            'repo_name': item['repo_name'],
            'repo_url': item['repo_url'],
            'week_guess': str(item.get('week', '')),
            'course_guess': course.get('course_id'),
            'course_label': course.get('course_label'),
            'cohort_guess': course.get('cohort_id'),
            'cohort_label': course.get('cohort_label'),
            'phase_guess': course.get('phase_id'),
            'phase_label': course.get('phase_label'),
            'phase_confidence': course.get('phase_confidence'),
            'week_label': course.get('week_label'),
            'continuity_score': course.get('continuity_score'),
            'confidence': course.get('confidence'),
            'status': course.get('status'),
            'evidence': course.get('evidence', [])[:5],
            'first_seen_at': prev.get('first_seen_at', now_str),
            'last_seen_at': now_str,
            'updated_at': item.get('updated_at', ''),
            'seen_count': seen_count,
            'status_history': status_history,
        }
'@

if (-not $code.Contains($old)) {
    throw "Exact repo_state block not found. Stop without modifying."
}

$code = $code.Replace($old, $new)
Set-Content $path -Value $code -Encoding UTF8

Write-Host "repo_state block replaced."

python .\codyssey-tracker\collect_v5_3_2.py

Write-Host ""
Write-Host "=== registry probe ==="
Get-Content .\codyssey-tracker\state\repo_registry.json -TotalCount 140