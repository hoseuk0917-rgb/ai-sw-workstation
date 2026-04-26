$ErrorActionPreference = 'Stop'

$path = '.\codyssey-tracker\collect_v5_1.py'
if (!(Test-Path $path)) { throw "Not found: $path" }

Copy-Item $path "$path.bak_preserve_meta_$(Get-Date -Format yyyyMMdd_HHmmss)" -Force

$lines = Get-Content $path

$start = 25   # line 26, 0-based
$end   = 74   # line 75, 0-based inclusive

$newBlock = @(
"def maybe_promote_candidate(item: dict, meta: dict) -> dict:",
"    if meta.get('status') != 'candidate' or meta.get('course_id') != 'unknown':",
"        return meta",
"",
"    week = str(item.get('week', ''))",
"    ev = list(meta.get('evidence', []))",
"    ev_set = set(ev)",
"    filenames = {p.split('/')[-1].lower() for p in (item.get('file_tree', []) or [])}",
"    repo_name = (item.get('repo_name', '') or '').lower()",
"    readme = (item.get('readme', '') or '').lower()",
"",
"    def promote(rule_tag: str, confidence: float) -> dict:",
"        patched = dict(meta)",
"        patched['course_id'] = 'course_2026_main'",
"        patched['course_label'] = '2026 본과정'",
"        patched['confidence'] = confidence",
"        patched['status'] = 'confirmed'",
"        patched['evidence'] = [rule_tag] + ev[:4]",
"",
"        patched.setdefault('cohort_id', 'cohort_2026_current')",
"        patched.setdefault('cohort_label', 'cohort_2026_current')",
"        patched.setdefault('phase_id', 'admission_bootcamp')",
"        patched.setdefault('phase_label', 'admission_bootcamp')",
"        patched.setdefault('phase_confidence', 0.70)",
"        patched.setdefault('week_label', week)",
"        patched.setdefault('continuity_score', 0.0)",
"        return patched",
"",
"    # 2주차 보강: python_with_git / workspace week2 / state.json 힌트 조합 특수",
"    if week == '2':",
"        if 'python_with_git' in repo_name and ('state.json' in filenames or 'week-readme:state.json' in ev_set):",
"            return promote('rule:v5_1_python_with_git_promote', 0.76)",
"        if 'week2' in repo_name and ('quiz' in readme or 'week-readme:quiz' in ev_set) and ('state.json' in filenames or 'week-readme:state.json' in ev_set):",
"            return promote('rule:v5_1_week2_workspace_promote', 0.74)",
"        if 'state.json' in filenames and 'main.py' in filenames and (('quiz' in readme) or ('quiz' in repo_name)):",
"            return promote('rule:v5_1_state_main_quiz_promote', 0.74)",
"",
"    # 1주차 보강: E1 + Dockerfile + main.py 조합 특수",
"    if week == '1':",
"        if 'dockerfile' in filenames and 'main.py' in filenames and ('e1' in repo_name or 'week1' in repo_name or 'setup' in repo_name):",
"            return promote('rule:v5_1_e1_docker_promote', 0.70)",
"",
"    return meta"
)

$before = @()
if ($start -gt 0) { $before = $lines[0..($start-1)] }
$after = $lines[($end+1)..($lines.Count-1)]
$lines = @($before + $newBlock + $after)

Set-Content $path -Value $lines -Encoding UTF8

Write-Host "Patched collect_v5_1.py"

python -m py_compile .\codyssey-tracker\collect_v5_1.py
python .\codyssey-tracker\collect_v5_3_2.py

Write-Host ""
Write-Host "=== report preview ==="
Get-Content .\codyssey-tracker\reports_v5_3_2\latest.md -TotalCount 260
