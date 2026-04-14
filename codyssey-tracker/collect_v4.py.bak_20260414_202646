#!/usr/bin/env python3
"""
Codyssey 과정 분리형 수집기 v4
- v3의 레거시 컷/오염 방지를 유지
- 주차별 완화 규칙으로 정상 본과정 레포 회수율 개선
"""

from __future__ import annotations

import json
import os
import time
from collections import defaultdict
from datetime import datetime

import collect as base

KST = base.KST
REPORT_DIR = "reports_v4"
ENABLE_GLOBAL_DISCOVERY = os.environ.get("ENABLE_GLOBAL_DISCOVERY", "0") == "1"
CURRENT_MAIN_START = "2026-03-01"
LEGACY_HARD_CUTOFF = "2026-01-01"

PILOT_BLACKLIST = [
    "dummysensor",
    "env_values",
    "mars",
    "mars_mission",
    "화성",
    "화성 기지",
    "mars base",
]

MAIN_REPO_HINTS = [
    "codyssey",
    "입학연수",
    "workstation",
    "docker",
    "quiz",
    "quiz_game",
    "first_python",
    "python_with_git",
    "npu",
    "npu_simulator",
    "mini_npu",
    "mac",
]

NATIVE_HINTS = ["native", "네이티브"]


def safe_date(s: str) -> str:
    return (s or "")[:10]


def contains_any(text: str, keywords: list[str]) -> list[str]:
    t = (text or "").lower()
    return [kw for kw in keywords if kw.lower() in t]


def filenames_from_tree(file_tree: list[str]) -> set[str]:
    return {p.split('/')[-1].lower() for p in (file_tree or [])}


def repo_name_lower(item: dict) -> str:
    return (item.get('repo_name', '') or '').lower()


def readme_lower(item: dict) -> str:
    return (item.get('readme', '') or '').lower()


def text_for_blacklist(item: dict) -> str:
    repo_name = repo_name_lower(item)
    readme = readme_lower(item)
    filenames = '\n'.join(list(filenames_from_tree(item.get('file_tree', []) or []))[:150])
    return '\n'.join([repo_name, readme, filenames])


def tier_evidence_from_file_tree(file_tree: list[str]) -> list[str]:
    filenames = filenames_from_tree(file_tree)
    ev = []
    for fp in base.FINGERPRINT_TIER1:
        if fp.lower() in filenames:
            ev.append(f"tier1:{fp}")
    for fp in base.FINGERPRINT_TIER2:
        if fp.lower() in filenames:
            ev.append(f"tier2:{fp}")
    return ev


def generic_hint_evidence(item: dict) -> list[str]:
    repo_name = repo_name_lower(item)
    readme = readme_lower(item)
    ev = []
    for kw in MAIN_REPO_HINTS:
        if kw in repo_name:
            ev.append(f"repo:{kw}")
    for kw in MAIN_REPO_HINTS:
        if kw in readme and f"repo:{kw}" not in ev:
            ev.append(f"readme:{kw}")
    return ev[:6]


def week_consistency(item: dict) -> tuple[int, list[str]]:
    week = str(item.get('week', ''))
    repo_name = repo_name_lower(item)
    readme = readme_lower(item)
    score = 0
    ev = []
    if week == '1':
        kws = ['workstation', 'docker', 'setup']
    elif week == '2':
        kws = ['quiz', 'quiz_game', 'python_with_git', 'first_python', 'state.json']
    elif week == '3':
        kws = ['npu', 'npu_simulator', 'mini_npu', 'mac', 'data.json']
    else:
        kws = []
    for kw in kws:
        if kw in repo_name:
            score += 2
            ev.append(f"week-repo:{kw}")
        elif kw in readme:
            score += 1
            ev.append(f"week-readme:{kw}")
    return score, ev[:4]


def week_specific_confirm(item: dict, tier_ev: list[str], hint_ev: list[str], week_score: int, week_ev: list[str]) -> tuple[bool, float, list[str]]:
    week = str(item.get('week', ''))
    repo_name = repo_name_lower(item)
    readme = readme_lower(item)
    filenames = filenames_from_tree(item.get('file_tree', []) or [])

    # 1주차: Dockerfile + docker/workstation 신호가 강하면 확정
    if week == '1':
        has_dockerfile = 'dockerfile' in filenames
        has_w1_hint = any(x in repo_name or x in readme for x in ['docker', 'workstation', 'setup'])
        if has_dockerfile and has_w1_hint:
            return True, 0.82, (['tier2:Dockerfile'] if 'tier2:Dockerfile' in tier_ev else tier_ev[:1]) + week_ev[:2] + [x for x in hint_ev if x in {'repo:docker','repo:workstation','readme:docker','readme:workstation'}][:1]

    # 2주차: quiz_game.py 또는 state.json+main.py+quiz류 신호
    if week == '2':
        if 'quiz_game.py' in filenames:
            ev = []
            if 'tier1:quiz_game.py' in tier_ev:
                ev.append('tier1:quiz_game.py')
            ev.extend(week_ev[:2])
            ev.extend([x for x in hint_ev if 'quiz' in x or 'python_with_git' in x][:2])
            return True, 0.9, ev[:4]
        has_state = 'state.json' in filenames
        has_main = 'main.py' in filenames
        has_q_hint = any(x in repo_name or x in readme for x in ['quiz', 'python_with_git', 'first_python'])
        if has_state and has_main and has_q_hint:
            ev = []
            if 'tier2:main.py' in tier_ev:
                ev.append('tier2:main.py')
            if 'tier2:state.json' in tier_ev:
                ev.append('tier2:state.json')
            ev.extend(week_ev[:2])
            ev.extend([x for x in hint_ev if 'quiz' in x or 'python_with_git' in x][:1])
            return True, 0.84, ev[:4]

    # 3주차: data.json 또는 mini_npu_simulator.py 또는 npu 강신호
    if week == '3':
        if 'mini_npu_simulator.py' in filenames:
            ev = []
            if 'tier1:mini_npu_simulator.py' in tier_ev:
                ev.append('tier1:mini_npu_simulator.py')
            if 'tier2:main.py' in tier_ev:
                ev.append('tier2:main.py')
            ev.extend(week_ev[:2])
            return True, 0.9, ev[:4]
        if 'data.json' in filenames:
            ev = []
            if 'tier1:data.json' in tier_ev:
                ev.append('tier1:data.json')
            if 'tier2:main.py' in tier_ev:
                ev.append('tier2:main.py')
            ev.extend(week_ev[:2])
            return True, 0.88, ev[:4]
        has_npu_hint = any(x in repo_name or x in readme for x in ['npu', 'npu_simulator', 'mini_npu', 'mac'])
        if has_npu_hint and week_score >= 2:
            ev = week_ev[:3] + [x for x in hint_ev if 'npu' in x or 'mac' in x][:1]
            return True, 0.78, ev[:4]

    return False, 0.0, []


def classify_course(item: dict) -> dict:
    updated_at = safe_date(item.get('updated_at', ''))
    blacklist_text = text_for_blacklist(item)
    pilot_hits = contains_any(blacklist_text, PILOT_BLACKLIST)
    native_hits = contains_any(blacklist_text, NATIVE_HINTS)
    tier_ev = tier_evidence_from_file_tree(item.get('file_tree', []) or [])
    hint_ev = generic_hint_evidence(item)
    week_score, week_ev = week_consistency(item)

    if updated_at and updated_at < LEGACY_HARD_CUTOFF:
        return {
            'course_id': 'legacy_pre2026',
            'course_label': '레거시(날짜 컷)',
            'confidence': 0.98,
            'status': 'excluded',
            'evidence': [f'updated_at:{updated_at}', 'rule:legacy-hard-cutoff'],
        }

    if pilot_hits and not any(x.startswith('tier1:') for x in tier_ev):
        return {
            'course_id': 'legacy_2025_pilot',
            'course_label': '2025 파일럿',
            'confidence': 0.95,
            'status': 'excluded',
            'evidence': [f'pilot:{x}' for x in pilot_hits[:4]],
        }

    if native_hits and week_score == 0 and not any(x.startswith('tier1:') for x in tier_ev):
        return {
            'course_id': 'course_2026_native_candidate',
            'course_label': '2026 네이티브(후보)',
            'confidence': 0.65,
            'status': 'candidate',
            'evidence': [f'native:{x}' for x in native_hits[:3]],
        }

    if updated_at >= CURRENT_MAIN_START:
        ok, conf, ev = week_specific_confirm(item, tier_ev, hint_ev, week_score, week_ev)
        if ok:
            return {
                'course_id': 'course_2026_main',
                'course_label': '2026 본과정',
                'confidence': conf,
                'status': 'confirmed',
                'evidence': ev[:5],
            }

        # 주차 특정 규칙 외 범용 확정 규칙
        strong_tier1 = any(x.startswith('tier1:') for x in tier_ev)
        strong_tier2 = sum(1 for x in tier_ev if x.startswith('tier2:'))
        if strong_tier1 and week_score >= 1:
            return {
                'course_id': 'course_2026_main',
                'course_label': '2026 본과정',
                'confidence': 0.86,
                'status': 'confirmed',
                'evidence': (tier_ev + week_ev + hint_ev)[:5],
            }
        if strong_tier2 >= 2 and week_score >= 2:
            return {
                'course_id': 'course_2026_main',
                'course_label': '2026 본과정',
                'confidence': 0.78,
                'status': 'confirmed',
                'evidence': (tier_ev + week_ev + hint_ev)[:5],
            }

    if pilot_hits and (tier_ev or hint_ev):
        return {
            'course_id': 'mixed_or_legacy',
            'course_label': '혼합/검토 필요',
            'confidence': 0.45,
            'status': 'review',
            'evidence': ([f'pilot:{x}' for x in pilot_hits[:2]] + tier_ev + week_ev + hint_ev)[:5],
        }

    return {
        'course_id': 'unknown',
        'course_label': '미분류',
        'confidence': 0.25,
        'status': 'candidate',
        'evidence': (week_ev + hint_ev + tier_ev)[:4] or ['insufficient-signal'],
    }


def summarize_week_safe(client, items: list[dict], week: str) -> str:
    if not items:
        return '_확정된 자료가 없어 요약을 생략합니다._'
    return base.summarize_week(client, items, week)


def build_report(all_items: list[dict], new_repos: list[dict]) -> tuple[str, dict]:
    classified = []
    for item in all_items:
        meta = classify_course(item)
        merged = dict(item)
        merged['course'] = meta
        classified.append(merged)

    confirmed_main = [x for x in classified if x['course']['course_id'] == 'course_2026_main']
    excluded_legacy = [x for x in classified if x['course']['status'] == 'excluded']
    review_items = [x for x in classified if x['course']['status'] in {'candidate', 'review'}]

    by_week = defaultdict(list)
    for item in confirmed_main:
        by_week[item['week']].append(item)

    by_bucket = defaultdict(list)
    for item in review_items:
        by_bucket[item['course']['course_label']].append(item)

    client = base.init_genai()
    date_str = datetime.now(KST).strftime('%Y-%m-%d')
    lines = []
    lines.append(f'# Codyssey 과정 분리형 수집 보고서 v4 ({date_str})')
    lines.append('')
    lines.append(f'- 총 수집 건수: {len(all_items)}건')
    lines.append(f'- 2026 본과정 확정: {len(confirmed_main)}건')
    lines.append(f'- 제외된 레거시/파일럿: {len(excluded_legacy)}건')
    lines.append(f'- 후보/검토 필요: {len(review_items)}건')
    lines.append(f"- 전역 신규 탐색 활성화: {'ON' if ENABLE_GLOBAL_DISCOVERY else 'OFF'}")
    lines.append('')

    lines.append('## 1. 2026 본과정 확정 자료')
    lines.append('')
    if by_week:
        for week in sorted(by_week.keys(), key=lambda x: int(x) if str(x).isdigit() else 999):
            lines.append(f'### {week}주차')
            lines.append('')
            lines.append(summarize_week_safe(client, by_week[week], week))
            lines.append('')
            lines.append('#### 참여 수강생 및 증거')
            lines.append('| 수강생 | 레포 | 업데이트 | 과정 판정 증거 |')
            lines.append('| --- | --- | --- | --- |')
            for item in sorted(by_week[week], key=lambda x: x['priority']):
                ev = ', '.join(item['course']['evidence'][:4]) or '-'
                lines.append(f"| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | {item['updated_at']} | {ev} |")
            lines.append('')
            lines.append('---')
            lines.append('')
    else:
        lines.append('_확정 자료 없음._')
        lines.append('')

    lines.append('## 2. 후보 과정 / 미분류 / 혼합 레포')
    lines.append('')
    if by_bucket:
        for bucket, items in by_bucket.items():
            lines.append(f'### {bucket}')
            lines.append('')
            lines.append('| 수강생 | 레포 | 업데이트 | 신뢰도 | 근거 |')
            lines.append('| --- | --- | --- | --- | --- |')
            for item in items:
                ev = ', '.join(item['course']['evidence'][:5]) or '-'
                lines.append(f"| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | {item['updated_at']} | {item['course']['confidence']:.2f} | {ev} |")
            lines.append('')
    else:
        lines.append('_후보 과정/미분류 레포 없음._')
        lines.append('')

    lines.append('## 3. 제외된 레거시/파일럿 레포')
    lines.append('')
    if excluded_legacy:
        lines.append('| 수강생 | 레포 | 업데이트 | 제외 근거 |')
        lines.append('| --- | --- | --- | --- |')
        for item in excluded_legacy:
            ev = ', '.join(item['course']['evidence'][:5]) or '-'
            lines.append(f"| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | {item['updated_at']} | {ev} |")
        lines.append('')
    else:
        lines.append('_제외된 레거시/파일럿 레포 없음._')
        lines.append('')

    if new_repos:
        lines.append('## 4. 전역 신규 발견 레포')
        lines.append('')
        lines.append('기본값은 OFF이며, 활성화 시에도 자동 편입하지 않고 참고 목록으로만 남깁니다.')
        lines.append('')
        lines.append('| 사용자 | 레포 | 점수 | 발견 증거 |')
        lines.append('| --- | --- | --- | --- |')
        for r in new_repos:
            lines.append(f"| {r['username']} | [{r['repo_name']}]({r['repo_url']}) | {r['score']} | {', '.join(r['evidence'])} |")
        lines.append('')

    payload = {
        'generated_at': date_str,
        'totals': {
            'all_items': len(all_items),
            'confirmed_main': len(confirmed_main),
            'excluded_legacy': len(excluded_legacy),
            'review_items': len(review_items),
            'new_repos': len(new_repos),
        },
        'items': classified,
    }
    return '\n'.join(lines), payload


def main() -> None:
    print(f"=== Codyssey v4 수집 시작 ({datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')}) ===")
    start_time = time.time()
    all_items = base.collect()
    print(f"총 {len(all_items)}건 수집 완료")

    new_repos = []
    if ENABLE_GLOBAL_DISCOVERY:
        known_users = {c['username'].lower() for c in base.CANDIDATES}
        new_repos = base.discover_new_repos(known_users)

    report_text, payload = build_report(all_items, new_repos)
    os.makedirs(REPORT_DIR, exist_ok=True)
    date_str = datetime.now(KST).strftime('%Y-%m-%d')
    report_path = os.path.join(REPORT_DIR, f'{date_str}.md')
    latest_path = os.path.join(REPORT_DIR, 'latest.md')
    json_path = os.path.join(REPORT_DIR, f'{date_str}.json')

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_text)
    with open(latest_path, 'w', encoding='utf-8') as f:
        f.write(report_text)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"보고서 생성 완료: {report_path}")
    print(f"소요 시간: {int(time.time() - start_time)}초")


if __name__ == '__main__':
    main()
