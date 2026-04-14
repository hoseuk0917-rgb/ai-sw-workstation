#!/usr/bin/env python3
from __future__ import annotations

import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import collect as base
import collect_v4 as v4
import collect_v5 as v5
import collect_v5_1 as v5_1

KST = base.KST
ROOT = Path(__file__).resolve().parent
STATE_DIR = ROOT / 'state'
REPORT_DIR = ROOT / 'reports_v5_2'
REGISTRY_PATH = STATE_DIR / 'repo_registry.json'
WATCHLIST_PATH = STATE_DIR / 'watchlist.json'
COURSE_MAP_PATH = STATE_DIR / 'course_map.json'
DISCOVERED_PATH = STATE_DIR / 'discovered_candidates.json'
ARCHIVE_PATH = STATE_DIR / 'archived_candidates.json'
ENABLE_GLOBAL_DISCOVERY = __import__('os').environ.get('ENABLE_GLOBAL_DISCOVERY', '0') == '1'

MAX_WATCH_PER_USER = 2
WEAK_SIGNAL_EVIDENCE_MAX = 2
ARCHIVE_SEEN_COUNT_THRESHOLD = 2


def load_json(path: Path, default: dict) -> dict:
    return v5.load_json(path, default)


def save_json(path: Path, payload: dict) -> None:
    v5.save_json(path, payload)


def active_watch_entries(raw_watch: list[dict], archive_map: dict) -> list[dict]:
    active = []
    for w in raw_watch:
        if not isinstance(w, dict) or not w.get('repo_key'):
            continue
        if w['repo_key'] in archive_map:
            continue
        active.append(w)
    return active


def build_candidate_pool() -> list[dict]:
    seeds = [v5.normalize_candidate(c) for c in v5.bootstrap_seed_candidates()]
    seeds = [c for c in seeds if c]
    archive_store = load_json(ARCHIVE_PATH, {'archived': []})
    archive_map = {a.get('repo_key'): a for a in archive_store.get('archived', []) if isinstance(a, dict) and a.get('repo_key')}
    watch_store = load_json(WATCHLIST_PATH, {'watch': []})
    active_watch = active_watch_entries(watch_store.get('watch', []), archive_map)
    watched = [v5.normalize_candidate(w.get('candidate', w)) for w in active_watch]
    watched = [c for c in watched if c]
    merged = {}
    for c in seeds + watched:
        key = f"{c.get('username')}::{c.get('repo_name', '')}::{c.get('type')}::{c.get('folder_pattern', '')}::{','.join(c.get('repo_patterns', [])) if isinstance(c.get('repo_patterns'), list) else ''}"
        merged[key] = c
    return list(merged.values())


def should_archive(repo_key: str, course: dict, repo_state: dict) -> tuple[bool, str]:
    if course.get('status') not in {'candidate', 'review'}:
        return False, ''
    evidence = course.get('evidence', []) or []
    seen_count = int(repo_state.get('seen_count', 0))
    has_strong = any(str(x).startswith('tier1:') for x in evidence)
    if has_strong:
        return False, ''
    if seen_count >= ARCHIVE_SEEN_COUNT_THRESHOLD and len(evidence) <= WEAK_SIGNAL_EVIDENCE_MAX:
        return True, 'low-signal-repeat'
    return False, ''


def priority_for_watch(course: dict, repo_state: dict) -> int:
    seen_count = int(repo_state.get('seen_count', 0))
    confidence = float(course.get('confidence', 0.0) or 0.0)
    if confidence >= 0.4:
        return 5
    if seen_count >= 2:
        return 7
    return 6


def update_state(classified: list[dict], discovered: list[dict]) -> tuple[dict, dict, dict, dict, dict]:
    registry = load_json(REGISTRY_PATH, {'version': 1, 'repos': {}})
    watchlist = load_json(WATCHLIST_PATH, {'version': 1, 'watch': []})
    discovered_store = load_json(DISCOVERED_PATH, {'version': 1, 'discovered': []})
    archive_store = load_json(ARCHIVE_PATH, {'version': 1, 'archived': []})
    repo_map = registry.setdefault('repos', {})
    watch_entries = {}
    archive_entries = {a.get('repo_key'): a for a in archive_store.get('archived', []) if isinstance(a, dict) and a.get('repo_key')}
    now_str = datetime.now(KST).strftime('%Y-%m-%d')

    for item in classified:
        repo_key = f"{item['username']}/{item['repo_name']}"
        course = item['course']
        prev = repo_map.get(repo_key, {})
        seen_count = int(prev.get('seen_count', 0)) + 1
        status_history = list(prev.get('status_history', []))
        status_history.append({'date': now_str, 'status': course.get('status'), 'course_guess': course.get('course_id')})
        status_history = status_history[-10:]
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
        repo_map[repo_key] = repo_state

        archive_it, archive_reason = should_archive(repo_key, course, repo_state)
        if archive_it:
            archive_entries[repo_key] = {
                'repo_key': repo_key,
                'candidate': prev.get('candidate') or {
                    'username': item['username'],
                    'display_name': item.get('display_name', item['username']),
                    'type': 'single_repo' if '/' in item['repo_name'] else 'multi_repo',
                    'repo_name': item['repo_name'].split('/')[0] if '/' in item['repo_name'] else None,
                    'folder_pattern': item['repo_name'].split('/', 1)[1] if '/' in item['repo_name'] else None,
                    'repo_patterns': [item['repo_name']] if '/' not in item['repo_name'] else None,
                    'priority': 9,
                },
                'reason': archive_reason,
                'evidence': course.get('evidence', [])[:5],
                'archived_at': now_str,
                'seen_count': seen_count,
            }
            continue

        if course.get('status') in {'candidate', 'review'}:
            cand = {
                'username': item['username'],
                'display_name': item.get('display_name', item['username']),
                'type': 'single_repo' if '/' in item['repo_name'] else 'multi_repo',
                'priority': priority_for_watch(course, repo_state),
            }
            if '/' in item['repo_name']:
                cand['repo_name'] = item['repo_name'].split('/')[0]
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
        else:
            archive_entries.pop(repo_key, None)

    discovered_entries = {d.get('repo_key'): d for d in discovered_store.get('discovered', []) if isinstance(d, dict) and d.get('repo_key')}
    for repo in discovered:
        repo_key = f"{repo['username']}/{repo['repo_name']}"
        candidate = v5_1.discovered_repo_to_candidate(repo)
        discovered_entries[repo_key] = {
            'repo_key': repo_key,
            'candidate': candidate,
            'score': repo.get('score'),
            'evidence': repo.get('evidence', [])[:5],
            'last_seen_at': now_str,
            'source': 'global-discovery',
        }
        if repo_key not in watch_entries and repo_key not in archive_entries:
            watch_entries[repo_key] = {
                'repo_key': repo_key,
                'course_guess': 'unseen_discovered',
                'course_label': '전역 발견 후보',
                'status': 'candidate',
                'candidate': candidate,
                'evidence': repo.get('evidence', [])[:5],
                'last_seen_at': now_str,
                'source': 'global-discovery',
            }

    # per-user watchlist cap
    by_user = defaultdict(list)
    for entry in watch_entries.values():
        user = entry.get('candidate', {}).get('username', '')
        by_user[user].append(entry)
    trimmed_watch = []
    for user, entries in by_user.items():
        entries.sort(key=lambda e: (e.get('candidate', {}).get('priority', 9), -len(e.get('evidence', []))))
        keep = entries[:MAX_WATCH_PER_USER]
        overflow = entries[MAX_WATCH_PER_USER:]
        trimmed_watch.extend(keep)
        for entry in overflow:
            archive_entries[entry['repo_key']] = {
                'repo_key': entry['repo_key'],
                'candidate': entry.get('candidate', {}),
                'reason': 'per-user-watch-cap',
                'evidence': entry.get('evidence', [])[:5],
                'archived_at': now_str,
            }

    watchlist['watch'] = trimmed_watch
    discovered_store['discovered'] = list(discovered_entries.values())
    archive_store['archived'] = list(archive_entries.values())

    hygiene = {
        'watch_kept': len(trimmed_watch),
        'archived_total': len(archive_store['archived']),
        'discovered_total': len(discovered_store['discovered']),
    }
    return registry, watchlist, discovered_store, archive_store, hygiene


def build_report(all_items: list[dict], classified: list[dict], new_repos: list[dict], candidate_pool_size: int, hygiene: dict) -> tuple[str, dict]:
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
    lines.append(f'# Codyssey registry-backed collection report v5.2 ({date_str})')
    lines.append('')
    lines.append(f'- 총 수집 건수: {len(all_items)}건')
    lines.append(f'- candidate pool size: {candidate_pool_size}')
    lines.append(f'- 2026 본과정 확정: {len(confirmed_main)}건')
    lines.append(f'- 제외된 레거시/파일럿: {len(excluded_legacy)}건')
    lines.append(f'- 후보/검토 필요: {len(review_items)}건')
    lines.append(f"- active watchlist size: {hygiene['watch_kept']}")
    lines.append(f"- archived candidate size: {hygiene['archived_total']}")
    lines.append(f"- discovered candidate size: {hygiene['discovered_total']}")
    lines.append(f"- 전역 신규 탐색 활성화: {'ON' if ENABLE_GLOBAL_DISCOVERY else 'OFF'}")
    lines.append('')
    lines.append('## 1. 2026 본과정 확정 자료')
    lines.append('')
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
    if not by_week:
        lines.append('_확정 자료 없음._')
        lines.append('')

    lines.append('## 2. 후보/검토 레포 (active watchlist)')
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

    lines.append('## 3. 후보풀 청소 요약')
    lines.append('')
    lines.append(f"- active watch 유지 개수: {hygiene['watch_kept']}")
    lines.append(f"- archive로 이동한 누적 후보 개수: {hygiene['archived_total']}")
    lines.append(f"- discovered 후보 누적 개수: {hygiene['discovered_total']}")
    lines.append('')
    if new_repos:
        lines.append('이번 실행에서 새로 발견된 후보는 watchlist/registry에만 적재되고 자동 확정되지 않습니다.')
        lines.append('')
    else:
        lines.append('_이번 실행에서 새 후보 확장은 없었습니다. (전역 탐색 OFF 또는 신규 미발견)_')
        lines.append('')

    lines.append('## 4. 제외된 레거시/파일럿 레포')
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
            'watch_kept': hygiene['watch_kept'],
            'archived_total': hygiene['archived_total'],
            'discovered_total': hygiene['discovered_total'],
            'new_repos': len(new_repos),
        },
        'items': classified,
    }
    return '\n'.join(lines), payload


def main() -> None:
    print(f"=== Codyssey v5.2 수집 시작 ({datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')}) ===")
    start_time = time.time()
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    candidates = build_candidate_pool()
    print(f"candidate pool size = {len(candidates)}")
    all_items = v5.collect_from_pool(candidates)
    print(f"총 {len(all_items)}건 수집 완료")

    new_repos = []
    if ENABLE_GLOBAL_DISCOVERY:
        known_users = {c['username'].lower() for c in candidates if c.get('username')}
        new_repos = base.discover_new_repos(known_users)

    course_map = load_json(COURSE_MAP_PATH, {'repo_overrides': {}, 'user_overrides': {}})
    classified = []
    for item in all_items:
        meta = v4.classify_course(item)
        meta = v5_1.maybe_promote_candidate(item, meta)
        meta = v5.apply_manual_overrides(item, meta, course_map)
        merged = dict(item)
        merged['course'] = meta
        classified.append(merged)

    registry, watchlist, discovered_store, archive_store, hygiene = update_state(classified, new_repos)
    save_json(REGISTRY_PATH, registry)
    save_json(WATCHLIST_PATH, watchlist)
    save_json(DISCOVERED_PATH, discovered_store)
    save_json(ARCHIVE_PATH, archive_store)

    report_text, payload = build_report(all_items, classified, new_repos, len(candidates), hygiene)
    date_str = datetime.now(KST).strftime('%Y-%m-%d')
    save_json(REPORT_DIR / f'{date_str}.json', payload)
    (REPORT_DIR / f'{date_str}.md').write_text(report_text, encoding='utf-8')
    (REPORT_DIR / 'latest.md').write_text(report_text, encoding='utf-8')

    run_snapshot = {
        'generated_at': date_str,
        'candidate_pool_size': len(candidates),
        'collected_count': len(all_items),
        'new_repo_count': len(new_repos),
        'watchlist_size': hygiene['watch_kept'],
        'archived_total': hygiene['archived_total'],
        'discovered_total': hygiene['discovered_total'],
    }
    save_json(STATE_DIR / f'run_snapshot_{date_str}.json', run_snapshot)

    print(f"보고서 생성 완료: {REPORT_DIR / f'{date_str}.md'}")
    print(f"소요 시간: {int(time.time() - start_time)}초")


if __name__ == '__main__':
    main()

