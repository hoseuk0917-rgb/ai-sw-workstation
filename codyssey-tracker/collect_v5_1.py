#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import collect as base
import collect_v4 as v4
import collect_v5 as v5

KST = base.KST
ROOT = Path(__file__).resolve().parent
STATE_DIR = ROOT / 'state'
REPORT_DIR = ROOT / 'reports_v5_1'
REGISTRY_PATH = STATE_DIR / 'repo_registry.json'
WATCHLIST_PATH = STATE_DIR / 'watchlist.json'
COURSE_MAP_PATH = STATE_DIR / 'course_map.json'
DISCOVERED_PATH = STATE_DIR / 'discovered_candidates.json'
ENABLE_GLOBAL_DISCOVERY = os.environ.get('ENABLE_GLOBAL_DISCOVERY', '0') == '1'


def maybe_promote_candidate(item: dict, meta: dict) -> dict:
    if meta.get('status') != 'candidate' or meta.get('course_id') != 'unknown':
        return meta

    week = str(item.get('week', ''))
    ev = list(meta.get('evidence', []))
    ev_set = set(ev)
    filenames = {p.split('/')[-1].lower() for p in (item.get('file_tree', []) or [])}
    repo_name = (item.get('repo_name', '') or '').lower()
    readme = (item.get('readme', '') or '').lower()

    # 2주차 보강: python_with_git / workspace week2 / state.json 힌트 조합 회수
    if week == '2':
        if 'python_with_git' in repo_name and ('state.json' in filenames or 'week-readme:state.json' in ev_set):
            return {
                'course_id': 'course_2026_main',
                'course_label': '2026 본과정',
                'confidence': 0.76,
                'status': 'confirmed',
                'evidence': ['rule:v5_1_python_with_git_promote'] + ev[:4],
            }
        if 'week2' in repo_name and ('quiz' in readme or 'week-readme:quiz' in ev_set) and ('state.json' in filenames or 'week-readme:state.json' in ev_set):
            return {
                'course_id': 'course_2026_main',
                'course_label': '2026 본과정',
                'confidence': 0.74,
                'status': 'confirmed',
                'evidence': ['rule:v5_1_week2_workspace_promote'] + ev[:4],
            }
        if 'state.json' in filenames and 'main.py' in filenames and (('quiz' in readme) or ('quiz' in repo_name)):
            return {
                'course_id': 'course_2026_main',
                'course_label': '2026 본과정',
                'confidence': 0.74,
                'status': 'confirmed',
                'evidence': ['rule:v5_1_state_main_quiz_promote'] + ev[:4],
            }

    # 1주차 보강: E1 + Dockerfile + main.py 혼합형 회수
    if week == '1':
        if 'dockerfile' in filenames and 'main.py' in filenames and ('e1' in repo_name or 'week1' in repo_name or 'setup' in repo_name):
            return {
                'course_id': 'course_2026_main',
                'course_label': '2026 본과정',
                'confidence': 0.7,
                'status': 'confirmed',
                'evidence': ['rule:v5_1_e1_docker_promote'] + ev[:4],
            }

    return meta


def discovered_repo_to_candidate(repo: dict) -> dict:
    return {
        'username': repo['username'],
        'display_name': repo['username'],
        'type': 'multi_repo',
        'repo_patterns': [repo['repo_name']],
        'priority': 7,
    }


def update_registry_and_watchlist(classified: list[dict], discovered: list[dict]) -> tuple[dict, dict, dict]:
    registry = v5.load_json(REGISTRY_PATH, {'version': 1, 'repos': {}})
    watchlist = v5.load_json(WATCHLIST_PATH, {'version': 1, 'watch': []})
    discovered_store = v5.load_json(DISCOVERED_PATH, {'version': 1, 'discovered': []})
    repo_map = registry.setdefault('repos', {})
    now_str = datetime.now(KST).strftime('%Y-%m-%d')

    watch_entries = {}
    for existing in watchlist.get('watch', []):
        if isinstance(existing, dict) and existing.get('repo_key'):
            watch_entries[existing['repo_key']] = existing

    for item in classified:
        repo_key = f"{item['username']}/{item['repo_name']}"
        course = item['course']
        prev = repo_map.get(repo_key, {})
        seen_count = int(prev.get('seen_count', 0)) + 1
        status_history = list(prev.get('status_history', []))
        status_history.append({'date': now_str, 'status': course.get('status'), 'course_guess': course.get('course_id')})
        status_history = status_history[-10:]
        repo_map[repo_key] = {
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
        if course.get('status') in {'candidate', 'review'}:
            cand = {
                'username': item['username'],
                'display_name': item.get('display_name', item['username']),
                'type': 'single_repo' if '/' in item['repo_name'] else 'multi_repo',
                'priority': 6,
            }
            if '/' in item['repo_name']:
                root_repo = item['repo_name'].split('/')[0]
                cand['repo_name'] = root_repo
                cand['folder_pattern'] = item['repo_name'].split('/', 1)[1]
            else:
                cand['repo_patterns'] = [item['repo_name']]
            watch_entries[repo_key] = {
                'repo_key': repo_key,
                'course_guess': course.get('course_id'),
                'course_label': course.get('course_label'),
                'status': course.get('status'),
                'candidate': cand,
                'evidence': course.get('evidence', [])[:5],
                'last_seen_at': now_str,
                'source': 'classified-run',
            }
        elif repo_key in watch_entries:
            # 확정되면 watchlist에서 제거
            del watch_entries[repo_key]

    discovered_entries = {d.get('repo_key'): d for d in discovered_store.get('discovered', []) if isinstance(d, dict) and d.get('repo_key')}
    for repo in discovered:
        repo_key = f"{repo['username']}/{repo['repo_name']}"
        discovered_entries[repo_key] = {
            'repo_key': repo_key,
            'candidate': discovered_repo_to_candidate(repo),
            'score': repo.get('score'),
            'evidence': repo.get('evidence', [])[:5],
            'last_seen_at': now_str,
            'source': 'global-discovery',
        }
        if repo_key not in watch_entries:
            watch_entries[repo_key] = {
                'repo_key': repo_key,
                'course_guess': 'unseen_discovered',
                'course_label': '전역 발견 후보',
                'status': 'candidate',
                'candidate': discovered_repo_to_candidate(repo),
                'evidence': repo.get('evidence', [])[:5],
                'last_seen_at': now_str,
                'source': 'global-discovery',
            }

    watchlist['watch'] = list(watch_entries.values())
    discovered_store['discovered'] = list(discovered_entries.values())
    return registry, watchlist, discovered_store


def build_report(all_items: list[dict], classified: list[dict], new_repos: list[dict], candidate_pool_size: int, watchlist_count: int, discovered_count: int) -> tuple[str, dict]:
    confirmed_main = [x for x in classified if x['course']['course_id'] == 'course_2026_main']
    excluded_legacy = [x for x in classified if x['course']['status'] == 'excluded']
    review_items = [x for x in classified if x['course']['status'] in {'candidate', 'review'}]
    by_week = defaultdict(list)
    for item in confirmed_main:
        by_week[item['week']].append(item)

    other_course_items = [x for x in classified if x['course']['course_id'] not in {'course_2026_main', 'unknown', 'legacy_pre2026', 'legacy_2025_pilot'}]
    by_other_course = defaultdict(list)
    for item in other_course_items:
        by_other_course[item['course']['course_label']].append(item)

    by_bucket = defaultdict(list)
    for item in review_items:
        by_bucket[item['course']['course_label']].append(item)

    client = base.init_genai()
    date_str = datetime.now(KST).strftime('%Y-%m-%d')
    lines = []
    lines.append(f'# Codyssey registry-backed collection report v5.1 ({date_str})')
    lines.append('')
    lines.append(f'- 총 수집 건수: {len(all_items)}건')
    lines.append(f'- candidate pool size: {candidate_pool_size}')
    lines.append(f'- 2026 본과정 확정: {len(confirmed_main)}건')
    lines.append(f'- 제외된 레거시/파일럿: {len(excluded_legacy)}건')
    lines.append(f'- 후보/검토 필요: {len(review_items)}건')
    lines.append(f'- watchlist size after run: {watchlist_count}')
    lines.append(f'- discovered candidate count: {discovered_count}')
    lines.append(f"- 전역 신규 탐색 활성화: {'ON' if ENABLE_GLOBAL_DISCOVERY else 'OFF'}")
    lines.append('')
    lines.append('## 1. 2026 본과정 확정 자료')
    lines.append('')
    if by_week:
        for week in sorted(by_week.keys(), key=lambda x: int(x) if str(x).isdigit() else 999):
            lines.append(f'### {week}주차')
            lines.append('')
            lines.append(v4.summarize_week_safe(client, by_week[week], week))
            lines.append('')
            lines.append('| 수강생 | 레포 | 업데이트 | 판정 증거 |')
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

    lines.append('## 2. 타과정/비본과정 정리')
    lines.append('')
    if by_other_course:
        for bucket, items in by_other_course.items():
            lines.append(f'### {bucket}')
            lines.append('')
            lines.append('| 수강생 | 레포 | 업데이트 | 신뢰도 | 근거 |')
            lines.append('| --- | --- | --- | --- | --- |')
            for item in items:
                ev = ', '.join(item['course']['evidence'][:5]) or '-'
                lines.append(f"| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | {item['updated_at']} | {item['course']['confidence']:.2f} | {ev} |")
            lines.append('')
    else:
        lines.append('_현재 실행에서는 타과정 확정/후보 레포가 뚜렷하게 분리되지 않았습니다._')
        lines.append('')

    lines.append('## 3. 후보/검토 레포 (watchlist 대상)')
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
        lines.append('_후보/검토 레포 없음._')
        lines.append('')

    lines.append('## 4. 후보 확장 정리')
    lines.append('')
    if new_repos:
        lines.append('이번 실행에서 전역 탐색으로 발견된 레포는 자동 확정하지 않고 discovered 후보와 watchlist로만 적재합니다.')
        lines.append('')
        lines.append('| 사용자 | 레포 | 점수 | 발견 증거 |')
        lines.append('| --- | --- | --- | --- |')
        for r in new_repos:
            lines.append(f"| {r['username']} | [{r['repo_name']}]({r['repo_url']}) | {r['score']} | {', '.join(r['evidence'])} |")
        lines.append('')
    else:
        lines.append('_이번 실행에서 새 후보 확장은 없었습니다. (전역 탐색 OFF 또는 신규 미발견)_')
        lines.append('')

    lines.append('## 5. 제외된 레거시/파일럿 레포')
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

    payload = {
        'generated_at': date_str,
        'totals': {
            'all_items': len(all_items),
            'candidate_pool_size': candidate_pool_size,
            'confirmed_main': len(confirmed_main),
            'excluded_legacy': len(excluded_legacy),
            'review_items': len(review_items),
            'watchlist_size': watchlist_count,
            'discovered_count': discovered_count,
            'new_repos': len(new_repos),
        },
        'items': classified,
    }
    return '\n'.join(lines), payload


def main() -> None:
    print(f"=== Codyssey v5.1 수집 시작 ({datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')}) ===")
    start_time = time.time()
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    candidates = v5.build_candidate_pool()
    print(f"candidate pool size = {len(candidates)}")
    all_items = v5.collect_from_pool(candidates)
    print(f"총 {len(all_items)}건 수집 완료")

    new_repos = []
    if ENABLE_GLOBAL_DISCOVERY:
        known_users = {c['username'].lower() for c in candidates if c.get('username')}
        new_repos = base.discover_new_repos(known_users)

    course_map = v5.load_json(COURSE_MAP_PATH, {'repo_overrides': {}, 'user_overrides': {}})
    classified = []
    for item in all_items:
        meta = v4.classify_course(item)
        meta = maybe_promote_candidate(item, meta)
        meta = v5.apply_manual_overrides(item, meta, course_map)
        merged = dict(item)
        merged['course'] = meta
        classified.append(merged)

    registry, watchlist, discovered_store = update_registry_and_watchlist(classified, new_repos)
    v5.save_json(REGISTRY_PATH, registry)
    v5.save_json(WATCHLIST_PATH, watchlist)
    v5.save_json(DISCOVERED_PATH, discovered_store)

    report_text, payload = build_report(
        all_items,
        classified,
        new_repos,
        candidate_pool_size=len(candidates),
        watchlist_count=len(watchlist.get('watch', [])),
        discovered_count=len(discovered_store.get('discovered', [])),
    )
    date_str = datetime.now(KST).strftime('%Y-%m-%d')
    v5.save_json(REPORT_DIR / f'{date_str}.json', payload)
    (REPORT_DIR / f'{date_str}.md').write_text(report_text, encoding='utf-8')
    (REPORT_DIR / 'latest.md').write_text(report_text, encoding='utf-8')

    run_snapshot = {
        'generated_at': date_str,
        'candidate_pool_size': len(candidates),
        'collected_count': len(all_items),
        'new_repo_count': len(new_repos),
        'watchlist_size': len(watchlist.get('watch', [])),
        'discovered_count': len(discovered_store.get('discovered', [])),
    }
    v5.save_json(STATE_DIR / f'run_snapshot_{date_str}.json', run_snapshot)

    print(f"보고서 생성 완료: {REPORT_DIR / f'{date_str}.md'}")
    print(f"소요 시간: {int(time.time() - start_time)}초")


if __name__ == '__main__':
    main()
