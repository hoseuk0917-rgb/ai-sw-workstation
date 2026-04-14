#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path

import collect as base
import collect_v4 as v4
import collect_v5 as v5
import collect_v5_1 as v5_1
import collect_v5_2 as v5_2
import collect_v5_3_1 as v5_3_1

KST = base.KST
ROOT = Path(__file__).resolve().parent
STATE_DIR = ROOT / 'state'
REPORT_DIR = ROOT / 'reports_v5_3_2'
REGISTRY_PATH = STATE_DIR / 'repo_registry.json'
WATCHLIST_PATH = STATE_DIR / 'watchlist.json'
COURSE_MAP_PATH = STATE_DIR / 'course_map.json'
DISCOVERED_PATH = STATE_DIR / 'discovered_candidates.json'
ARCHIVE_PATH = STATE_DIR / 'archived_candidates.json'
OBS_PATH = STATE_DIR / 'repo_observations.json'
ENABLE_GLOBAL_DISCOVERY = __import__('os').environ.get('ENABLE_GLOBAL_DISCOVERY', '0') == '1'
SIGNATURE_VERSION = 'v5.3.1'


def load_json(path: Path, default: dict) -> dict:
    return v5.load_json(path, default)


def save_json(path: Path, payload: dict) -> None:
    v5.save_json(path, payload)


def update_observations(classified: list[dict]) -> tuple[dict, list[dict]]:
    store = load_json(OBS_PATH, {'version': 1, 'observations': {}})
    obs_map = store.setdefault('observations', {})
    today = datetime.now(KST).strftime('%Y-%m-%d')
    overwritten_flags = []

    for item in classified:
        repo_key = f"{item['username']}/{item['repo_name']}"
        course = item['course']
        sig = v5_3_1.stronger_content_signature(item, course)
        entries = list(obs_map.get(repo_key, []))
        prev_last = entries[-1] if entries else None
        current = {
            'date': today,
            'week_guess': str(item.get('week', '')),
            'course_guess': course.get('course_id'),
            'course_label': course.get('course_label'),
            'status': course.get('status'),
            'confidence': course.get('confidence'),
            'updated_at': item.get('updated_at', ''),
            'content_signature': sig,
            'signature_version': SIGNATURE_VERSION,
            'evidence': course.get('evidence', [])[:5],
        }

        if entries and entries[-1].get('date') == today and entries[-1].get('content_signature') == sig:
            obs_map[repo_key] = entries
            continue

        if prev_last:
            prev_sig_ver = prev_last.get('signature_version', 'legacy')
            same_sig_ver = prev_sig_ver == SIGNATURE_VERSION
            week_changed = prev_last.get('week_guess') != current['week_guess']
            sig_changed = prev_last.get('content_signature') != current['content_signature']
            status_changed = prev_last.get('status') != current['status']
            updated_changed = prev_last.get('updated_at') != current['updated_at']

            # 시그니처 버전이 바뀐 첫 비교는 baseline migration으로 처리
            if not same_sig_ver:
                current['baseline_reset_from'] = prev_sig_ver
            else:
                if week_changed or sig_changed or status_changed:
                    overwritten_flags.append({
                        'repo_key': repo_key,
                        'previous_week': prev_last.get('week_guess'),
                        'current_week': current.get('week_guess'),
                        'previous_status': prev_last.get('status'),
                        'current_status': current.get('status'),
                        'previous_updated_at': prev_last.get('updated_at'),
                        'current_updated_at': current.get('updated_at'),
                        'signature_changed': sig_changed,
                        'updated_changed': updated_changed,
                        'reason': 'same-repo-history-changed',
                    })

        entries.append(current)
        obs_map[repo_key] = entries[-20:]

    return store, overwritten_flags


def apply_overwrite_flags_to_registry(overwritten_flags: list[dict]) -> dict:
    registry = load_json(REGISTRY_PATH, {'version': 1, 'repos': {}})
    repo_map = registry.setdefault('repos', {})
    flagged_keys = {f['repo_key'] for f in overwritten_flags}
    for repo_key, repo_state in repo_map.items():
        if repo_key not in flagged_keys and repo_state.get('overwrite_suspected'):
            repo_state['overwrite_suspected'] = False
            repo_state['overwrite_reason'] = 'cleared-no-current-flag'
    for flag in overwritten_flags:
        repo_key = flag['repo_key']
        if repo_key in repo_map:
            repo_map[repo_key]['overwrite_suspected'] = True
            repo_map[repo_key]['overwrite_reason'] = flag['reason']
            repo_map[repo_key]['previous_week_guess'] = flag.get('previous_week')
            repo_map[repo_key]['previous_status'] = flag.get('previous_status')
            repo_map[repo_key]['previous_updated_at'] = flag.get('previous_updated_at')
    return registry


def active_watch_repo_keys(watchlist: dict) -> set[str]:
    return {w.get('repo_key') for w in watchlist.get('watch', []) if isinstance(w, dict) and w.get('repo_key')}


def build_report(all_items: list[dict], classified: list[dict], watchlist: dict, new_repos: list[dict], hygiene: dict, overwritten_flags: list[dict], candidate_pool_size: int) -> tuple[str, dict]:
    confirmed_main = [x for x in classified if x['course']['course_id'] == 'course_2026_main']
    excluded_legacy = [x for x in classified if x['course']['status'] == 'excluded']
    active_keys = active_watch_repo_keys(watchlist)
    review_items = [x for x in classified if f"{x['username']}/{x['repo_name']}" in active_keys]
    by_week = defaultdict(list)
    for item in confirmed_main:
        by_week[item['week']].append(item)
    by_bucket = defaultdict(list)
    for item in review_items:
        by_bucket[item['course']['course_label']].append(item)

    client = base.init_genai()
    date_str = datetime.now(KST).strftime('%Y-%m-%d')
    lines = []
    lines.append(f'# Codyssey registry-backed collection report v5.3.2 ({date_str})')
    lines.append('')
    lines.append(f'- 총 수집 건수: {len(all_items)}건')
    lines.append(f'- candidate pool size: {candidate_pool_size}')
    lines.append(f'- 2026 본과정 확정: {len(confirmed_main)}건')
    lines.append(f'- 제외된 레거시/파일럿: {len(excluded_legacy)}건')
    lines.append(f'- active watchlist items shown: {len(review_items)}건')
    lines.append(f"- active watchlist size: {hygiene['watch_kept']}")
    lines.append(f"- archived candidate size: {hygiene['archived_total']}")
    lines.append(f"- discovered candidate size: {hygiene['discovered_total']}")
    lines.append(f'- overwrite-suspected repos: {len(overwritten_flags)}')
    lines.append(f'- signature version: {SIGNATURE_VERSION}')
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

    lines.append('## 2. 동일 레포 덮어쓰기/변조 의심 정리')
    lines.append('')
    if overwritten_flags:
        lines.append('| 레포 키 | 이전 주차 | 현재 주차 | 이전 상태 | 현재 상태 | 업데이트 변경 | 서명 변경 |')
        lines.append('| --- | --- | --- | --- | --- | --- | --- |')
        for flag in overwritten_flags:
            lines.append(f"| {flag['repo_key']} | {flag.get('previous_week','-')} | {flag.get('current_week','-')} | {flag.get('previous_status','-')} | {flag.get('current_status','-')} | {'Y' if flag.get('updated_changed') else 'N'} | {'Y' if flag.get('signature_changed') else 'N'} |")
        lines.append('')
    else:
        lines.append('_이번 실행에서는 뚜렷한 덮어쓰기/변조 의심 레포가 없었습니다._')
        lines.append('')

    lines.append('## 3. 후보/검토 레포 (actual active watchlist)')
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
        lines.append('_actual active watchlist 기준 후보/검토 레포 없음._')
        lines.append('')

    lines.append('## 4. 후보풀 청소 요약')
    lines.append('')
    lines.append(f"- active watch 유지 개수: {hygiene['watch_kept']}")
    lines.append(f"- archive로 이동한 누적 후보 개수: {hygiene['archived_total']}")
    lines.append(f"- discovered 후보 누적 개수: {hygiene['discovered_total']}")
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
            'active_watch_items_shown': len(review_items),
            'watch_kept': hygiene['watch_kept'],
            'archived_total': hygiene['archived_total'],
            'discovered_total': hygiene['discovered_total'],
            'overwrite_suspected': len(overwritten_flags),
            'new_repos': len(new_repos),
        },
        'items': classified,
        'overwritten_flags': overwritten_flags,
    }
    return '\n'.join(lines), payload


def main() -> None:
    print(f"=== Codyssey v5.3.2 수집 시작 ({datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')}) ===")
    start_time = __import__('time').time()
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    candidates = v5_2.build_candidate_pool()
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

    registry, watchlist, discovered_store, archive_store, hygiene = v5_2.update_state(classified, new_repos)
    obs_store, overwritten_flags = update_observations(classified)
    registry = apply_overwrite_flags_to_registry(overwritten_flags)

    save_json(REGISTRY_PATH, registry)
    save_json(WATCHLIST_PATH, watchlist)
    save_json(DISCOVERED_PATH, discovered_store)
    save_json(ARCHIVE_PATH, archive_store)
    save_json(OBS_PATH, obs_store)

    report_text, payload = build_report(all_items, classified, watchlist, new_repos, hygiene, overwritten_flags, len(candidates))
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
        'overwrite_suspected': len(overwritten_flags),
        'signature_version': SIGNATURE_VERSION,
    }
    save_json(STATE_DIR / f'run_snapshot_{date_str}.json', run_snapshot)

    print(f"보고서 생성 완료: {REPORT_DIR / f'{date_str}.md'}")
    print(f"소요 시간: {int(__import__('time').time() - start_time)}초")


if __name__ == '__main__':
    main()
