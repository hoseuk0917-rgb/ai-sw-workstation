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

KST = base.KST
ROOT = Path(__file__).resolve().parent
STATE_DIR = ROOT / 'state'
REPORT_DIR = ROOT / 'reports_v5'
SEED_PATH = STATE_DIR / 'seed_candidates.json'
REGISTRY_PATH = STATE_DIR / 'repo_registry.json'
WATCHLIST_PATH = STATE_DIR / 'watchlist.json'
COURSE_MAP_PATH = STATE_DIR / 'course_map.json'
ENABLE_GLOBAL_DISCOVERY = os.environ.get('ENABLE_GLOBAL_DISCOVERY', '0') == '1'


def load_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return default


def save_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')


def bootstrap_seed_candidates() -> list[dict]:
    data = load_json(SEED_PATH, {'seeds': []})
    seeds = data.get('seeds', [])
    if isinstance(seeds, list) and seeds:
        return seeds
    return list(base.CANDIDATES)


def normalize_candidate(c: dict) -> dict | None:
    if not isinstance(c, dict):
        return None

    username = str(c.get('username', '') or '').strip()
    if not username:
        return None

    out = dict(c)
    out['username'] = username
    out.setdefault('display_name', username)
    out.setdefault('priority', 5)

    ctype = out.get('type')
    if ctype not in {'single_repo', 'multi_repo'}:
        if out.get('repo_name'):
            out['type'] = 'single_repo'
        else:
            out['type'] = 'multi_repo'

    if out['type'] == 'single_repo':
        repo_name = str(out.get('repo_name', '') or '').strip()
        if not repo_name:
            return None
        out['repo_name'] = repo_name
        if 'folder_pattern' in out and out.get('folder_pattern') is not None:
            out['folder_pattern'] = str(out.get('folder_pattern', '') or '').strip() or None
        out.pop('repo_patterns', None)
    else:
        pats = out.get('repo_patterns', []) or []
        if not isinstance(pats, list):
            return None
        pats = [str(x).strip() for x in pats if str(x).strip()]
        if not pats:
            return None
        out['repo_patterns'] = pats
        out.pop('repo_name', None)
        out.pop('folder_pattern', None)

    return out


def build_candidate_pool() -> list[dict]:
    seeds = [normalize_candidate(c) for c in bootstrap_seed_candidates()]
    seeds = [c for c in seeds if c]

    watch = load_json(WATCHLIST_PATH, {'watch': []}).get('watch', [])
    watched = [normalize_candidate(c.get('candidate', c)) for c in watch if isinstance(c, dict)]
    watched = [c for c in watched if c]

    merged = {}
    for c in seeds + watched:
        key = (
            f"{c.get('username')}::{c.get('repo_name', '')}::{c.get('type')}::"
            f"{c.get('folder_pattern', '')}::"
            f"{','.join(c.get('repo_patterns', [])) if isinstance(c.get('repo_patterns'), list) else ''}"
        )
        merged[key] = c
    return list(merged.values())


def collect_from_pool(candidates: list[dict]) -> list[dict]:
    results = []
    seen = set()
    for c in candidates:
        try:
            ctype = c.get('type')
            uname = c.get('username')
            label = c.get('repo_name') or c.get('folder_pattern') or (
                ','.join(c.get('repo_patterns', [])) if isinstance(c.get('repo_patterns'), list) else ''
            )

            items = base.collect_single_repo(c) if ctype == 'single_repo' else base.collect_multi_repo(c)

            if not items:
                print(f"[debug:empty] type={ctype} user={uname} target={label}")
                continue

            print(f"[debug:hit] type={ctype} user={uname} target={label} count={len(items)}")

            for item in items:
                key = f"{item['username']}/{item['repo_name']}"
                if key not in seen:
                    seen.add(key)
                    results.append(item)
        except Exception as e:
            print(
                f"[candidate collect failed] "
                f"type={c.get('type')} user={c.get('username')} "
                f"repo={c.get('repo_name')} folder={c.get('folder_pattern')} "
                f"patterns={c.get('repo_patterns')} - {e}"
            )
    return results


def apply_manual_overrides(item: dict, meta: dict, course_map: dict) -> dict:
    repo_key = f"{item.get('username')}/{item.get('repo_name')}"
    repo_override = (course_map.get('repo_overrides') or {}).get(repo_key)
    user_override = (course_map.get('user_overrides') or {}).get(item.get('username'))
    override = repo_override or user_override
    if not override:
        return meta

    patched = dict(meta)
    for k in ['course_id', 'course_label', 'status', 'confidence']:
        if k in override:
            patched[k] = override[k]

    ev = list(patched.get('evidence', []))
    ev.insert(0, 'manual-override')
    patched['evidence'] = ev[:5]
    return patched


def update_registry_and_watchlist(classified: list[dict]) -> tuple[dict, dict]:
    registry = load_json(REGISTRY_PATH, {'version': 1, 'repos': {}})
    watchlist = load_json(WATCHLIST_PATH, {'version': 1, 'watch': []})
    repo_map = registry.setdefault('repos', {})
    watch_entries = []
    now_str = datetime.now(KST).strftime('%Y-%m-%d')

    for item in classified:
        repo_key = f"{item['username']}/{item['repo_name']}"
        course = item['course']
        prev = repo_map.get(repo_key, {})
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

            watch_entries.append({
                'repo_key': repo_key,
                'course_guess': course.get('course_id'),
                'status': course.get('status'),
                'candidate': cand,
                'evidence': course.get('evidence', [])[:5],
                'last_seen_at': now_str,
            })

    dedup = {}
    for w in watch_entries:
        dedup[w['repo_key']] = w
    watchlist['watch'] = list(dedup.values())
    return registry, watchlist


def build_report(all_items: list[dict], classified: list[dict], new_repos: list[dict]) -> tuple[str, dict]:
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
    lines.append(f'# Codyssey registry-backed collection report v5 ({date_str})')
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

    lines.append('## 2. 후보/검토 레포 (watchlist 대상)')
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
    print(f"=== Codyssey v5 수집 시작 ({datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')}) ===")
    start_time = time.time()
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    candidates = build_candidate_pool()
    print(f"candidate pool size = {len(candidates)}")
    all_items = collect_from_pool(candidates)
    print(f"총 {len(all_items)}건 수집 완료")

    new_repos = []
    if ENABLE_GLOBAL_DISCOVERY:
        known_users = {c['username'].lower() for c in candidates if c.get('username')}
        new_repos = base.discover_new_repos(known_users)

    course_map = load_json(COURSE_MAP_PATH, {'repo_overrides': {}, 'user_overrides': {}})
    classified = []
    for item in all_items:
        meta = v4.classify_course(item)
        meta = apply_manual_overrides(item, meta, course_map)
        merged = dict(item)
        merged['course'] = meta
        classified.append(merged)

    registry, watchlist = update_registry_and_watchlist(classified)
    save_json(REGISTRY_PATH, registry)
    save_json(WATCHLIST_PATH, watchlist)

    report_text, payload = build_report(all_items, classified, new_repos)
    date_str = datetime.now(KST).strftime('%Y-%m-%d')
    save_json(REPORT_DIR / f'{date_str}.json', payload)
    (REPORT_DIR / f'{date_str}.md').write_text(report_text, encoding='utf-8')
    (REPORT_DIR / 'latest.md').write_text(report_text, encoding='utf-8')

    run_snapshot = {
        'generated_at': date_str,
        'candidate_pool_size': len(candidates),
        'collected_count': len(all_items),
        'new_repo_count': len(new_repos),
    }
    save_json(STATE_DIR / f'run_snapshot_{date_str}.json', run_snapshot)

    print(f"보고서 생성 완료: {REPORT_DIR / f'{date_str}.md'}")
    print(f"소요 시간: {int(time.time() - start_time)}초")


if __name__ == '__main__':
    main()
