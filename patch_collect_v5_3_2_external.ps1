$ErrorActionPreference = 'Stop'

$repo = (Get-Location).Path
$target = Join-Path $repo 'codyssey-tracker\collect_v5_3_2.py'

if (!(Test-Path $target)) {
  throw "collect_v5_3_2.py not found: $target"
}

Copy-Item $target "$target.bak_$(Get-Date -Format yyyyMMdd_HHmmss)" -Force

$code = Get-Content $target -Raw -Encoding UTF8

$code = $code.Replace(
@'
import collect as base
import collect_v4 as v4
import collect_v5 as v5
import collect_v5_1 as v5_1
import collect_v5_2 as v5_2
import collect_v5_3_1 as v5_3_1
'@,
@'
import collect as base
import collect_v4 as v4
import collect_v5 as v5
import collect_v5_1 as v5_1
import collect_v5_2 as v5_2
import collect_v5_3_1 as v5_3_1
import external_materials as ext
'@
)

$code = $code.Replace(
@"
OBS_PATH = STATE_DIR / 'repo_observations.json'
ENABLE_GLOBAL_DISCOVERY = __import__('os').environ.get('ENABLE_GLOBAL_DISCOVERY', '0') == '1'
SIGNATURE_VERSION = 'v5.3.1'
"@,
@"
OBS_PATH = STATE_DIR / 'repo_observations.json'
EXTERNAL_MATERIALS_PATH = STATE_DIR / 'external_materials.json'
ENABLE_GLOBAL_DISCOVERY = __import__('os').environ.get('ENABLE_GLOBAL_DISCOVERY', '0') == '1'
SIGNATURE_VERSION = 'v5.3.1'
"@
)

$code = $code.Replace(
@'
def active_watch_repo_keys(watchlist: dict) -> set[str]:
    return {w.get('repo_key') for w in watchlist.get('watch', []) if isinstance(w, dict) and w.get('repo_key')}
'@,
@'
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

            materials[url] = {
                'url': url,
                'domain': link.get('domain', ''),
                'source_type': link.get('source_type', ''),
                'linked_repo_keys': linked_repo_keys[-20:],
                'linked_usernames': linked_usernames,
                'source_paths': source_paths[-20:],
                'first_seen_at': prev.get('first_seen_at', today),
                'last_seen_at': today,
            }

    return store
'@
)

$code = $code.Replace(
"def build_report(all_items: list[dict], classified: list[dict], watchlist: dict, new_repos: list[dict], hygiene: dict, overwritten_flags: list[dict], candidate_pool_size: int) -> tuple[str, dict]:",
"def build_report(all_items: list[dict], classified: list[dict], watchlist: dict, new_repos: list[dict], hygiene: dict, overwritten_flags: list[dict], candidate_pool_size: int, external_store: dict) -> tuple[str, dict]:"
)

$code = $code.Replace(
@'
    lines.append(f'- overwrite-suspected repos: {len(overwritten_flags)}')
    lines.append(f'- signature version: {SIGNATURE_VERSION}')
    lines.append(f"- 전역 신규 탐색 활성화: {'ON' if ENABLE_GLOBAL_DISCOVERY else 'OFF'}")
    lines.append('')
'@,
@'
    external_items = list((external_store or {}).get('materials', {}).values())

    lines.append(f'- overwrite-suspected repos: {len(overwritten_flags)}')
    lines.append(f'- external materials tracked: {len(external_items)}')
    lines.append(f'- signature version: {SIGNATURE_VERSION}')
    lines.append(f"- 전역 신규 탐색 활성화: {'ON' if ENABLE_GLOBAL_DISCOVERY else 'OFF'}")
    lines.append('')
'@
)

$code = $code.Replace(
@'
    lines.append('## 5. 제외된 레거시/파일럿 레포')
    lines.append('')
'@,
@'
    lines.append('## 5. 레포 밖 참고자료')
    lines.append('')
    if external_items:
        lines.append('| 도메인 | URL | 연결 레포 수 | 연결 사용자 |')
        lines.append('| --- | --- | --- | --- |')
        for mat in sorted(
            external_items,
            key=lambda x: (-len(x.get('linked_repo_keys', [])), x.get('domain', ''), x.get('url', ''))
        )[:80]:
            users = ', '.join(mat.get('linked_usernames', [])[:5]) or '-'
            lines.append(
                f"| {mat.get('domain','-')} | {mat.get('url','-')} | {len(mat.get('linked_repo_keys', []))} | {users} |"
            )
        lines.append('')
    else:
        lines.append('_추출된 레포 밖 참고자료 없음._')
        lines.append('')

    lines.append('## 6. 제외된 레거시/파일럿 레포')
    lines.append('')
'@
)

$code = $code.Replace(
@'
            'overwrite_suspected': len(overwritten_flags),
            'new_repos': len(new_repos),
        },
        'items': classified,
        'overwritten_flags': overwritten_flags,
'@,
@'
            'overwrite_suspected': len(overwritten_flags),
            'external_materials': len(external_items),
            'new_repos': len(new_repos),
        },
        'items': classified,
        'overwritten_flags': overwritten_flags,
        'external_materials': external_items,
'@
)

$code = $code.Replace(
@'
    registry, watchlist, discovered_store, archive_store, hygiene = v5_2.update_state(classified, new_repos)
    obs_store, overwritten_flags = update_observations(classified)
    registry = apply_overwrite_flags_to_registry(overwritten_flags)

    save_json(REGISTRY_PATH, registry)
    save_json(WATCHLIST_PATH, watchlist)
    save_json(DISCOVERED_PATH, discovered_store)
    save_json(ARCHIVE_PATH, archive_store)
    save_json(OBS_PATH, obs_store)

    report_text, payload = build_report(all_items, classified, watchlist, new_repos, hygiene, overwritten_flags, len(candidates))
'@,
@'
    registry, watchlist, discovered_store, archive_store, hygiene = v5_2.update_state(classified, new_repos)
    obs_store, overwritten_flags = update_observations(classified)
    registry = apply_overwrite_flags_to_registry(overwritten_flags)
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
'@
)

Set-Content $target -Value $code -Encoding UTF8

Write-Host "Patch applied to collect_v5_3_2.py"
python .\codyssey-tracker\collect_v5_3_2.py
Write-Host ""
Write-Host "=== verify ==="
Get-ChildItem .\codyssey-tracker\state\external_materials.json -ErrorAction Stop | Select-Object FullName, Length, LastWriteTime
Get-Content .\codyssey-tracker\reports_v5_3_2\latest.md -TotalCount 200