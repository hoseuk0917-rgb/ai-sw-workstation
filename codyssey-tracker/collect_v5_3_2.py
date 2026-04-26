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
import external_materials as ext

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
EXTERNAL_MATERIALS_PATH = STATE_DIR / 'external_materials.json'
ENABLE_GLOBAL_DISCOVERY = __import__('os').environ.get('ENABLE_GLOBAL_DISCOVERY', '0') == '1'
SIGNATURE_VERSION = 'v5.3.1'


def load_json(path: Path, default: dict) -> dict:
    return v5.load_json(path, default)


def save_json(path: Path, payload: dict) -> None:
    v5.save_json(path, payload)


DISCOVERY_KEYWORDS_PATH = STATE_DIR / 'discovery_keywords.json'


def load_discovery_keywords() -> dict:
    return load_json(DISCOVERY_KEYWORDS_PATH, {'version': 1, 'tracks': {}})


def _flatten_item_text(item: dict) -> str:
    parts = []
    for key in ['repo_name', 'repo_url', 'description', 'readme', 'readme_text', 'display_name']:
        val = item.get(key)
        if isinstance(val, str) and val.strip():
            parts.append(val.strip())

    file_tree = item.get('file_tree', []) or []
    if isinstance(file_tree, list):
        for x in file_tree:
            if isinstance(x, str) and x.strip():
                parts.append(x.strip())
            elif isinstance(x, dict):
                for k in ['path', 'name']:
                    v = x.get(k)
                    if isinstance(v, str) and v.strip():
                        parts.append(v.strip())

    return '\n'.join(parts).lower()


def _flatten_file_names(item: dict) -> set[str]:
    out = set()
    file_tree = item.get('file_tree', []) or []
    if not isinstance(file_tree, list):
        return out

    for x in file_tree:
        if isinstance(x, str):
            name = x.replace('\\', '/').split('/')[-1].strip().lower()
            if name:
                out.add(name)
        elif isinstance(x, dict):
            for k in ['path', 'name']:
                v = x.get(k)
                if isinstance(v, str):
                    name = v.replace('\\', '/').split('/')[-1].strip().lower()
                    if name:
                        out.add(name)
    return out


def _literal_pattern_score(repo_name_l: str, patterns: list[str]) -> tuple[float, list[str]]:
    hits = []
    score = 0.0

    for pat in patterns or []:
        if not isinstance(pat, str):
            continue
        p = pat.strip().lower()
        if not p:
            continue

        if any(ch in p for ch in ['[', ']', '(', ')', '?', '^', '$', '*', '+', '\\']):
            continue

        if p == repo_name_l:
            score += 3.0
            hits.append(f'repo:{p}')
        elif p in repo_name_l:
            score += 1.5
            hits.append(f'repo~:{p}')

    return score, hits


def apply_discovery_overlay(item: dict, meta: dict, discovery_rules: dict) -> dict:
    if meta.get('status') in {'confirmed', 'excluded'}:
        return meta

    repo_name_l = str(item.get('repo_name', '') or '').strip().lower()
    text_l = _flatten_item_text(item)
    file_names = _flatten_file_names(item)

    best_track = None
    best_course_id = None
    best_score = 0.0
    best_hits = []

    tracks = (discovery_rules.get('tracks') or {})
    for track_id, track_obj in tracks.items():
        courses = (track_obj.get('courses') or {})
        for course_id, course_obj in courses.items():
            score = 0.0
            hits = []

            official = course_obj.get('official_rule', {}) or {}
            observed = course_obj.get('observed_rule', {}) or {}

            s, h = _literal_pattern_score(repo_name_l, observed.get('repo_patterns', []) or [])
            score += s
            hits.extend(h)

            s, h = _literal_pattern_score(repo_name_l, official.get('repo_patterns', []) or [])
            score += s
            hits.extend(h)

            for tok in official.get('readme_tokens', []) or []:
                if isinstance(tok, str) and tok.strip() and tok.lower() in text_l:
                    score += 1.2
                    hits.append(f'text:{tok}')

            for tok in observed.get('readme_tokens', []) or []:
                if isinstance(tok, str) and tok.strip() and tok.lower() in text_l:
                    score += 0.8
                    hits.append(f'text~:{tok}')

            for tok in official.get('file_tokens', []) or []:
                if isinstance(tok, str) and tok.strip().lower() in file_names:
                    score += 1.6
                    hits.append(f'file:{tok}')

            for tok in observed.get('file_tokens', []) or []:
                if isinstance(tok, str) and tok.strip().lower() in file_names:
                    score += 1.0
                    hits.append(f'file~:{tok}')

            if score > best_score:
                best_track = track_id
                best_course_id = course_id
                best_score = score
                best_hits = hits[:5]

    if not best_course_id or best_score < 3.5:
        return meta

    patched = dict(meta)

    best_track_obj = (tracks.get(best_track) or {})
    best_course_obj = ((best_track_obj.get('courses') or {}).get(best_course_id) or {})

    phase_id = (
        best_course_obj.get('phase_id')
        or best_track_obj.get('phase_id')
        or ('admission_bootcamp' if best_track == 'all_in_one' else (meta.get('phase_id') or 'unknown'))
    )
    phase_label = (
        best_course_obj.get('phase_label')
        or best_track_obj.get('phase_label')
        or phase_id
    )

    patched['course_id'] = best_course_id
    patched['course_label'] = best_course_id
    patched['cohort_id'] = 'cohort_2026_current'
    patched['cohort_label'] = 'cohort_2026_current'
    patched['phase_id'] = phase_id
    patched['phase_label'] = phase_label
    patched['track_id'] = best_track
    patched['track_label'] = best_track
    patched['status'] = 'review' if best_score >= 6.0 else 'candidate'
    patched['confidence'] = max(float(meta.get('confidence', 0.0) or 0.0), min(0.89, 0.40 + best_score * 0.06))

    ev = list(meta.get('evidence', []))
    ev = [f'bridge:{best_track}:{best_course_id}', f'bridge_score:{best_score:.1f}'] + best_hits + ev
    patched['evidence'] = ev[:5]
    return patched



def _append_unique_text(values: list[str], value: str, limit: int = 80) -> None:
    value = str(value or '').strip()
    if not value:
        return
    if value not in values and len(values) < limit:
        values.append(value)


def build_global_discovery_queries(discovery_rules: dict) -> list[dict]:
    """
    discovery_keywords.json의 track/course 힌트를 GitHub search query 후보로 변환한다.
    너무 일반적인 단어는 단독 검색하지 않고 codyssey/native 등 course identity와 결합한다.
    """
    queries: list[dict] = []

    global_obj = discovery_rules.get('global') or {}
    common_tokens = [
        x for x in (global_obj.get('common_positive_tokens') or [])
        if isinstance(x, str) and x.strip()
    ]

    # course identity / program-level seed
    identity_tokens = [
        'codyssey',
        '코디세이',
        'ai native',
        'ai-native',
        '네이티브',
    ]
    for tok in common_tokens:
        if tok.lower() in {'codyssey', 'mission', 'workspace'}:
            _append_unique_text(identity_tokens, tok)

    def add_query(q: str, source: str, track_id: str = '', course_id: str = '', kind: str = 'keyword') -> None:
        q = ' '.join(str(q or '').split())
        if not q:
            return
        if len(q) < 3:
            return
        key = q.lower()
        for old in queries:
            if old.get('q', '').lower() == key:
                return
        queries.append({
            'q': q,
            'source': source,
            'track_id': track_id,
            'course_id': course_id,
            'kind': kind,
        })

    # 기본 repo/code 검색: 너무 넓은 것은 줄이고 course 정체성을 섞는다.
    base_file_queries = [
        'filename:README.md codyssey',
        'filename:README.md "코디세이"',
        'filename:README.md "ai native"',
        'filename:README.md "네이티브"',
        'filename:Dockerfile codyssey',
        'filename:docker-compose.yml codyssey',
        'filename:requirements.txt codyssey',
        'filename:package.json codyssey',
        'filename:app.py codyssey',
        'filename:main.py codyssey',
    ]
    for q in base_file_queries:
        add_query(q, 'base', kind='base')

    tracks = discovery_rules.get('tracks') or {}
    for track_id, track_obj in tracks.items():
        if not isinstance(track_obj, dict):
            continue

        track_name = str(track_obj.get('display_name') or track_id).strip()
        if track_name:
            add_query(f'filename:README.md "{track_name}"', 'track_display_name', track_id=track_id, kind='readme')

        for topic in track_obj.get('official_topics', []) or []:
            if isinstance(topic, str) and topic.strip():
                topic_s = topic.strip()
                add_query(f'filename:README.md "{topic_s}"', 'official_topic', track_id=track_id, kind='readme')
                # course identity 결합형
                for ident in identity_tokens[:3]:
                    add_query(f'"{topic_s}" "{ident}"', 'official_topic_identity', track_id=track_id, kind='keyword')

        courses = track_obj.get('courses') or {}
        for course_id, course_obj in courses.items():
            if not isinstance(course_obj, dict):
                continue

            display = str(course_obj.get('display_name') or '').strip()
            if display:
                add_query(f'filename:README.md "{display}"', 'course_display_name', track_id=track_id, course_id=course_id, kind='readme')
                add_query(f'"{display}" codyssey', 'course_display_identity', track_id=track_id, course_id=course_id, kind='keyword')

            for bucket_name in ['official_rule', 'observed_rule', 'expansion_rule']:
                rule = course_obj.get(bucket_name) or {}

                for kw in rule.get('official_keywords', []) or []:
                    if isinstance(kw, str) and kw.strip():
                        add_query(f'filename:README.md "{kw.strip()}"', f'{bucket_name}.official_keywords', track_id=track_id, course_id=course_id, kind='readme')

                for tok in rule.get('readme_tokens', []) or []:
                    if isinstance(tok, str) and tok.strip():
                        tok_s = tok.strip()
                        # 일반 토큰은 codyssey와 결합, 구체 토큰은 README 검색
                        if len(tok_s) >= 8 or ' ' in tok_s or '-' in tok_s:
                            add_query(f'filename:README.md "{tok_s}"', f'{bucket_name}.readme_tokens', track_id=track_id, course_id=course_id, kind='readme')
                        add_query(f'"{tok_s}" codyssey', f'{bucket_name}.readme_tokens_identity', track_id=track_id, course_id=course_id, kind='keyword')

                for tok in rule.get('file_tokens', []) or []:
                    if isinstance(tok, str) and tok.strip():
                        file_tok = tok.strip().replace('\\', '/').split('/')[-1]
                        if file_tok and '.' in file_tok:
                            add_query(f'filename:{file_tok} codyssey', f'{bucket_name}.file_tokens', track_id=track_id, course_id=course_id, kind='file')

                # repo_patterns는 GitHub search query 문법과 regex 문법이 다르므로
                # regex 특수문자 많은 것은 제외하고 literal에 가까운 것만 사용
                for pat in rule.get('repo_patterns', []) or []:
                    if not isinstance(pat, str):
                        continue
                    p = pat.strip()
                    if not p:
                        continue
                    if any(ch in p for ch in ['[', ']', '(', ')', '?', '^', '$', '*', '+', '\\']):
                        continue
                    p = p.replace('[_ -]', ' ').replace('[-_ ]', ' ').strip()
                    if len(p) >= 4:
                        add_query(f'{p} codyssey', f'{bucket_name}.repo_patterns', track_id=track_id, course_id=course_id, kind='repo')

    # 과도한 API 사용 방지. 매주 cron에서 돌릴 수 있는 수준으로 제한.
    return queries[:60]


def _github_search_code_items(query: str, per_page: int = 20) -> list[dict]:
    url = 'https://api.github.com/search/code'
    params = {'q': query, 'per_page': per_page}
    try:
        r = base.requests.get(url, headers=base.github_headers(), params=params, timeout=20)
        if r.status_code != 200:
            print(f"  [global-discovery] search skipped status={r.status_code} q={query}")
            return []
        return r.json().get('items', []) or []
    except Exception as e:
        print(f"  [global-discovery] search error q={query}: {e}")
        return []


def _discovery_score_from_rules(repo_name: str, file_tree: list, readme: str, discovery_rules: dict) -> tuple[float, list[str], str, str]:
    probe = {
        'repo_name': repo_name,
        'repo_url': '',
        'description': '',
        'readme': readme or '',
        'readme_text': readme or '',
        'display_name': '',
        'file_tree': file_tree or [],
    }
    base_meta = {
        'status': 'candidate',
        'confidence': 0.0,
        'course_id': 'unclassified',
        'course_label': 'unclassified',
        'evidence': [],
    }
    patched = apply_discovery_overlay(probe, base_meta, discovery_rules)
    evidence = list(patched.get('evidence', []) or [])
    score = 0.0
    for ev in evidence:
        if isinstance(ev, str) and ev.startswith('bridge_score:'):
            try:
                score = float(ev.split(':', 1)[1])
            except Exception:
                score = 0.0
    return score, evidence, str(patched.get('track_id') or ''), str(patched.get('course_id') or '')


def discover_new_repos_expanded(known_users: set, discovery_rules: dict) -> tuple[list[dict], dict]:
    """
    discovery_keywords.json 기반 전역 신규탐색.
    기존 후보풀 밖의 repo만 찾되, 코디세이/과정 정체성 신호가 있는 후보만 채택한다.
    """
    discovered: dict[str, dict] = {}
    seen_repos: set[str] = set()

    excluded_owners = {
        'hoseuk0917-rgb',
    }
    excluded_repos = {
        'hoseuk0917-rgb/ai-sw-workstation',
    }

    required_identity_tokens = {
        'codyssey',
        '코디세이',
        'ia-codyssey',
        'codyssey2026',
        'rookieq',
        'ai-sw',
        'ai sw',
        '입학연수',
        'e1-1',
        'e1_1',
        'e1-2',
        'e1_2',
        'e1-3',
        'e1_3',
    }

    stats = {
        'enabled': True,
        'query_count': 0,
        'raw_hits': 0,
        'unique_repos_seen': 0,
        'accepted': 0,
        'queries': [],
    }

    queries = build_global_discovery_queries(discovery_rules)
    print(f"[global-discovery] expanded query count = {len(queries)}")

    for qobj in queries:
        q = qobj['q']
        stats['query_count'] += 1
        items = _github_search_code_items(q, per_page=20)
        stats['raw_hits'] += len(items)
        stats['queries'].append({
            'q': q,
            'hits': len(items),
            'source': qobj.get('source', ''),
            'track_id': qobj.get('track_id', ''),
            'course_id': qobj.get('course_id', ''),
        })

        for item in items:
            repo_full = item.get('repository', {}).get('full_name', '')
            if not repo_full or '/' not in repo_full:
                continue

            username, repo_name = repo_full.split('/', 1)
            repo_full_l = repo_full.lower()
            username_l = username.lower()

            if username_l in excluded_owners:
                continue
            if repo_full_l in excluded_repos:
                continue
            if username_l in known_users:
                continue
            if repo_full_l in seen_repos:
                continue

            seen_repos.add(repo_full_l)
            stats['unique_repos_seen'] += 1

            file_tree = base.get_repo_tree(username, repo_name)
            readme = base.get_readme(username, repo_name)

            identity_text = ' '.join([
                repo_full_l,
                repo_name.lower(),
                str(readme or '').lower(),
                ' '.join([str(p).lower() for p in (file_tree or [])[:200]]),
            ])
            has_required_identity = any(tok in identity_text for tok in required_identity_tokens)
            if not has_required_identity:
                continue

            base_score = base.compute_fingerprint_score(file_tree, readme)
            bridge_score, bridge_evidence, track_id, course_id = _discovery_score_from_rules(
                repo_name=repo_name,
                file_tree=file_tree,
                readme=readme,
                discovery_rules=discovery_rules,
            )

            combined_score = float(base_score) + float(bridge_score) * 2.0

            if not track_id or not course_id or course_id == 'unclassified':
                continue

            if combined_score < 18.0:
                continue

            evidence = []
            if base_score:
                evidence.append(f'legacy_fingerprint:{base_score}')
            evidence.extend(bridge_evidence[:5])
            evidence.append(f'query:{q[:80]}')

            discovered[repo_full] = {
                'username': username,
                'repo_name': repo_name,
                'repo_url': f'https://github.com/{repo_full}',
                'score': combined_score,
                'evidence': evidence[:8],
                'file_count': len(file_tree),
                'readme_length': len(readme or ''),
                'track_id': track_id,
                'course_id': course_id,
                'discovery_source': 'expanded-global-discovery',
            }
            print(f"  [expanded-discovery] {repo_full} score={combined_score:.1f} track={track_id} course={course_id}")

        __import__('time').sleep(1)

    out = sorted(discovered.values(), key=lambda x: -float(x.get('score', 0.0)))
    stats['accepted'] = len(out)
    return out, stats


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


def apply_overwrite_flags_to_registry(registry: dict, overwritten_flags: list[dict]) -> dict:
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


def update_external_materials(classified: list[dict]) -> dict:
    store = load_json(EXTERNAL_MATERIALS_PATH, {'version': 1, 'materials': {}})
    materials = store.setdefault('materials', {})
    today = datetime.now(KST).strftime('%Y-%m-%d')

    for item in classified:
        repo_key = f"{item['username']}/{item['repo_name']}"
        links = ext.collect_external_links_from_item(item)

        for link in links:
            url = link.get('url')
            if not url:
                continue

            prev = materials.get(url, {})
            linked_repo_keys = list(prev.get('linked_repo_keys', []))
            if repo_key not in linked_repo_keys:
                linked_repo_keys.append(repo_key)

            linked_usernames = sorted(set(list(prev.get('linked_usernames', [])) + [item['username']]))

            source_paths = list(prev.get('source_paths', []))
            src_path = link.get('source_path')
            if src_path and src_path not in source_paths:
                source_paths.append(src_path)

            source_types = list(prev.get('source_types', []))
            src_type = link.get('source_type')
            if src_type and src_type not in source_types:
                source_types.append(src_type)

            materials[url] = {
                'url': url,
                'domain': link.get('domain', ''),
                'source_type': link.get('source_type', ''),
                'source_types': source_types[-20:],
                'linked_repo_keys': linked_repo_keys[-20:],
                'linked_usernames': linked_usernames,
                'source_paths': source_paths[-20:],
                'first_seen_at': prev.get('first_seen_at', today),
                'last_seen_at': today,
            }

    return store


def build_report(all_items: list[dict], classified: list[dict], watchlist: dict, new_repos: list[dict], hygiene: dict, overwritten_flags: list[dict], candidate_pool_size: int, external_store: dict) -> tuple[str, dict]:
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
    external_items = list((external_store or {}).get('materials', {}).values())
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
        lines.append('| 수강생 | 레포 | 업데이트 | cohort | phase | week | continuity | 판정 증거 |')
        lines.append('| --- | --- | --- | --- | --- | --- | --- | --- |')
        for item in sorted(by_week[week], key=lambda x: x['priority']):
            course = item.get('course', {})
            ev = ', '.join(course.get('evidence', [])[:4]) or '-'
            cohort = course.get('cohort_label', '-') or '-'
            phase = course.get('phase_label', '-') or '-'
            week_label = course.get('week_label', str(item.get('week', ''))) or '-'
            continuity = float(course.get('continuity_score', 0.0) or 0.0)
            lines.append(
                f"| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | "
                f"{item['updated_at']} | {cohort} | {phase} | {week_label} | {continuity:.2f} | {ev} |"
            )
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
            lines.append('| 수강생 | 레포 | 업데이트 | cohort | phase | week | continuity | 신뢰도 | 근거 |')
            lines.append('| --- | --- | --- | --- | --- | --- | --- | --- | --- |')
            for item in items:
                course = item.get('course', {})
                ev = ', '.join(course.get('evidence', [])[:5]) or '-'
                cohort = course.get('cohort_label', '-') or '-'
                phase = course.get('phase_label', '-') or '-'
                week_label = course.get('week_label', str(item.get('week', ''))) or '-'
                continuity = float(course.get('continuity_score', 0.0) or 0.0)
                confidence = float(course.get('confidence', 0.0) or 0.0)
                lines.append(
                    f"| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | "
                    f"{item['updated_at']} | {cohort} | {phase} | {week_label} | {continuity:.2f} | {confidence:.2f} | {ev} |"
                )
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
            'external_materials': len(external_items),
            'new_repos': len(new_repos),
        },
        'items': classified,
        'overwritten_flags': overwritten_flags,
        'external_materials': external_items,
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

    course_map = load_json(COURSE_MAP_PATH, {'repo_overrides': {}, 'user_overrides': {}})
    discovery_rules = load_discovery_keywords()

    new_repos = []
    discovery_stats = {
        'enabled': False,
        'query_count': 0,
        'raw_hits': 0,
        'unique_repos_seen': 0,
        'accepted': 0,
        'queries': [],
    }
    if ENABLE_GLOBAL_DISCOVERY:
        known_users = {c['username'].lower() for c in candidates if c.get('username')}
        new_repos, discovery_stats = discover_new_repos_expanded(known_users, discovery_rules)
    classified = []
    for item in all_items:
        meta = v4.classify_course(item)
        meta = v5_1.maybe_promote_candidate(item, meta)
        meta = apply_discovery_overlay(item, meta, discovery_rules)
        meta = v5.apply_manual_overrides(item, meta, course_map)
        merged = dict(item)
        merged['course'] = meta
        classified.append(merged)

    registry, watchlist, discovered_store, archive_store, hygiene = v5_2.update_state(classified, new_repos)
    obs_store, overwritten_flags = update_observations(classified)
    registry = apply_overwrite_flags_to_registry(registry, overwritten_flags)
    external_store = update_external_materials(classified)

    save_json(REGISTRY_PATH, registry)
    save_json(WATCHLIST_PATH, watchlist)
    save_json(DISCOVERED_PATH, discovered_store)
    save_json(ARCHIVE_PATH, archive_store)
    save_json(OBS_PATH, obs_store)
    save_json(EXTERNAL_MATERIALS_PATH, external_store)

    report_text, payload = build_report(
        all_items,
        classified,
        watchlist,
        new_repos,
        hygiene,
        overwritten_flags,
        len(candidates),
        external_store,
    )
    date_str = datetime.now(KST).strftime('%Y-%m-%d')
    save_json(REPORT_DIR / f'{date_str}.json', payload)
    (REPORT_DIR / f'{date_str}.md').write_text(report_text, encoding='utf-8')
    (REPORT_DIR / 'latest.md').write_text(report_text, encoding='utf-8')

    run_snapshot = {
        'generated_at': date_str,
        'candidate_pool_size': len(candidates),
        'collected_count': len(all_items),
        'new_repo_count': len(new_repos),
        'global_discovery': discovery_stats,
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
