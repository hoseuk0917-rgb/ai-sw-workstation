#!/usr/bin/env python3
from __future__ import annotations

import re
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
STATE_DIR = ROOT / "state"
REPORT_DIR = ROOT / "reports_v5_2"
REGISTRY_PATH = STATE_DIR / "repo_registry.json"
WATCHLIST_PATH = STATE_DIR / "watchlist.json"
COURSE_MAP_PATH = STATE_DIR / "course_map.json"
DISCOVERED_PATH = STATE_DIR / "discovered_candidates.json"
ARCHIVE_PATH = STATE_DIR / "archived_candidates.json"
EXTERNAL_MATERIALS_PATH = STATE_DIR / "external_materials.json"
ENABLE_GLOBAL_DISCOVERY = __import__("os").environ.get("ENABLE_GLOBAL_DISCOVERY", "0") == "1"

MAX_WATCH_PER_USER = 2
WEAK_SIGNAL_EVIDENCE_MAX = 2
ARCHIVE_SEEN_COUNT_THRESHOLD = 2


def load_json(path: Path, default: dict) -> dict:
    return v5.load_json(path, default)


def save_json(path: Path, payload: dict) -> None:
    v5.save_json(path, payload)


def normalize_candidate(c: dict) -> dict | None:
    if not isinstance(c, dict):
        return None

    username = str(c.get("username", "") or "")
    username = username.replace("\ufeff", "").replace("\u200b", "").strip()
    if not username:
        return None

    out = dict(c)
    out["username"] = username

    display_name = str(out.get("display_name", "") or "")
    display_name = display_name.replace("\ufeff", "").replace("\u200b", "").strip() or username
    out["display_name"] = display_name
    out.setdefault("priority", 5)

    ctype = out.get("type")
    if ctype not in {"single_repo", "multi_repo"}:
        if out.get("repo_name"):
            out["type"] = "single_repo"
        else:
            out["type"] = "multi_repo"

    if out["type"] == "single_repo":
        repo_name = str(out.get("repo_name", "") or "")
        repo_name = repo_name.replace("\ufeff", "").replace("\u200b", "").strip()
        if not repo_name:
            return None
        out["repo_name"] = repo_name
        if "folder_pattern" in out and out.get("folder_pattern") is not None:
            folder_pattern = str(out.get("folder_pattern", "") or "")
            folder_pattern = folder_pattern.replace("\ufeff", "").replace("\u200b", "").strip() or None
            out["folder_pattern"] = folder_pattern
        out.pop("repo_patterns", None)
    else:
        pats = out.get("repo_patterns", []) or []
        if not isinstance(pats, list):
            return None
        cleaned = []
        for x in pats:
            s = str(x)
            s = s.replace("\ufeff", "").replace("\u200b", "").strip()
            if s:
                cleaned.append(s)
        if not cleaned:
            return None
        out["repo_patterns"] = cleaned
        out.pop("repo_name", None)
        out.pop("folder_pattern", None)

    return out


def active_watch_entries(raw_watch: list[dict], archive_map: dict) -> list[dict]:
    active = []
    for w in raw_watch:
        if not isinstance(w, dict) or not w.get("repo_key"):
            continue
        if w["repo_key"] in archive_map:
            continue
        active.append(w)
    return active


def candidate_covers_repo(candidate: dict, repo_name: str) -> bool:
    if not isinstance(candidate, dict) or not repo_name:
        return False

    repo_name_s = str(repo_name).strip()
    ctype = candidate.get("type")

    if ctype == "single_repo":
        return str(candidate.get("repo_name", "") or "").strip().lower() == repo_name_s.lower()

    for pat in candidate.get("repo_patterns", []) or []:
        pat_s = str(pat or "").strip()
        if not pat_s:
            continue
        if pat_s.lower() == repo_name_s.lower():
            return True
        try:
            if re.search(pat_s, repo_name_s, re.IGNORECASE):
                return True
        except re.error:
            continue
    return False


def build_external_seed_candidates(existing_candidates: list[dict] | None = None) -> list[dict]:
    store = load_json(EXTERNAL_MATERIALS_PATH, {"version": 1, "materials": {}})
    materials = store.get("materials", {}) or {}

    repo_keywords = ("codyssey", "mission", "workspace", "quiz", "docker", "npu", "python")
    reject_repo_keywords = ("day1", "bear", "pilot", "legacy")
    candidates: list[dict] = []
    existing_candidates = existing_candidates or []

    existing_by_user: dict[str, list[dict]] = {}
    for c in existing_candidates:
        if not isinstance(c, dict):
            continue
        username = str(c.get("username", "") or "").replace("\ufeff", "").replace("\u200b", "").strip().lower()
        if not username:
            continue
        existing_by_user.setdefault(username, []).append(c)

    grouped_repo_names: dict[str, set[str]] = {}

    for entry in materials.values():
        if not isinstance(entry, dict):
            continue

        source_type = str(entry.get("source_type", "") or "")
        source_types = entry.get("source_types", []) or []
        is_profile_like = (
            source_type in {"profile", "gist-profile"}
            or any(x in {"profile", "gist-profile"} for x in source_types)
        )
        if not is_profile_like:
            continue

        linked_repo_keys = entry.get("linked_repo_keys", []) or []
        for repo_key in linked_repo_keys:
            if not repo_key or not isinstance(repo_key, str):
                continue

            parts = [p.strip() for p in repo_key.split("/")]
            if len(parts) != 2:
                continue

            username, repo_name = parts[0], parts[1]
            username = username.replace("\ufeff", "").replace("\u200b", "").strip()
            repo_name = repo_name.replace("\ufeff", "").replace("\u200b", "").strip()
            if not username or not repo_name:
                continue

            username_l = username.lower()
            repo_name_l = repo_name.lower()

            if not any(k in repo_name_l for k in repo_keywords):
                continue
            if any(bad in repo_name_l for bad in reject_repo_keywords):
                continue

            already_covered = False
            for existing in existing_by_user.get(username_l, []):
                if candidate_covers_repo(existing, repo_name):
                    already_covered = True
                    break
            if already_covered:
                continue

            grouped_repo_names.setdefault(username, set()).add(repo_name)

    for username in sorted(grouped_repo_names.keys(), key=str.lower):
        repo_names = sorted(grouped_repo_names[username], key=str.lower)[:8]
        cand = normalize_candidate(
            {
                "username": username,
                "display_name": username,
                "type": "multi_repo",
                "repo_patterns": repo_names,
                "priority": 8,
            }
        )
        if cand:
            candidates.append(cand)

    return candidates


def build_candidate_pool() -> list[dict]:
    seeds = [normalize_candidate(c) for c in list(base.CANDIDATES)]
    seeds = [c for c in seeds if c]

    archive_store = load_json(ARCHIVE_PATH, {"archived": []})
    archive_map = {
        a.get("repo_key"): a
        for a in archive_store.get("archived", [])
        if isinstance(a, dict) and a.get("repo_key")
    }

    watch_store = load_json(WATCHLIST_PATH, {"watch": []})
    active_watch = active_watch_entries(watch_store.get("watch", []), archive_map)
    watched = [normalize_candidate(w.get("candidate", w)) for w in active_watch]
    watched = [c for c in watched if c]

    existing_candidates = seeds + watched
    external_seeded = build_external_seed_candidates(existing_candidates)

    expanded_seeded: list[dict] = []
    expanded_accounts_path = WATCHLIST_PATH.parent.parent.parent / "tmp" / "always_watch_expanded_accounts_v2.txt"
    if expanded_accounts_path.exists():
        known_users = {
            str(c.get("username", "")).strip()
            for c in existing_candidates + external_seeded
            if isinstance(c, dict) and str(c.get("username", "")).strip()
        }

        for raw in expanded_accounts_path.read_text(encoding="utf-8-sig").splitlines():
            username = raw.replace("\ufeff", "").replace("\u200b", "").strip()
            if not username or username in known_users:
                continue

            cand = normalize_candidate({
                "username": username,
                "display_name": username,
                "type": "multi_repo",
                "priority": 8,
                "repo_patterns": [
                    r"[Cc]odyssey[_\-]?[Ww]eek[_\-]?0?([1-9]\d*)",
                    r"[Cc]odyssey[_\-]?[Mm](?:ission)?[_\-]?0?([1-9]\d*)",
                    r"[Cc]odyssey[_\-]?[Ee](?:[_\-]?\d+)?[_\-]?0?([1-9]\d*)",
                    r"e1[_\-]?0?([1-9]\d*)",
                    r"rookieq([1-9]\d*)",
                    r"quiz[_\-]?game",
                    r"(?:dev[_\-]?)?workstation(?:[_\-]setup)?",
                    r"(?:mini[_\-]?)?npu(?:[_\-]simulator)?",
                    r"python[_\-]?quiz[_\-]?game",
                ],
            })
            if cand:
                expanded_seeded.append(cand)
                known_users.add(username)

    print(
        f"[debug:candidate_pool] seeds={len(seeds)} "
        f"watched={len(watched)} external_seeded={len(external_seeded)} "
        f"expanded_seeded={len(expanded_seeded)}"
    )

    merged: dict[str, dict] = {}
    before = 0
    after_count = 0
    for c in seeds + watched + external_seeded + expanded_seeded:
        key = (
            f"{c.get('username')}::{c.get('repo_name', '')}::{c.get('type')}::"
            f"{c.get('folder_pattern', '')}::"
            f"{','.join(c.get('repo_patterns', [])) if isinstance(c.get('repo_patterns'), list) else ''}"
        )
        before += 1
        merged[key] = c
        after_count = len(merged)

    print(f"[debug:candidate_pool] merged_input={before} merged_unique={after_count}")
    return list(merged.values())


def should_archive(repo_key: str, course: dict, repo_state: dict) -> tuple[bool, str]:
    if course.get("status") not in {"candidate", "review"}:
        return False, ""

    evidence = course.get("evidence", []) or []
    seen_count = int(repo_state.get("seen_count", 0))
    has_strong = any(str(x).startswith("tier1:") for x in evidence)

    if has_strong:
        return False, ""
    if seen_count >= ARCHIVE_SEEN_COUNT_THRESHOLD and len(evidence) <= WEAK_SIGNAL_EVIDENCE_MAX:
        return True, "low-signal-repeat"
    return False, ""


def priority_for_watch(course: dict, repo_state: dict) -> int:
    seen_count = int(repo_state.get("seen_count", 0))
    confidence = float(course.get("confidence", 0.0) or 0.0)

    if confidence >= 0.4:
        return 5
    if seen_count >= 2:
        return 7
    return 6


def update_state(
    classified: list[dict], discovered: list[dict]
) -> tuple[dict, dict, dict, dict, dict]:
    registry = load_json(REGISTRY_PATH, {"version": 1, "repos": {}})
    watchlist = load_json(WATCHLIST_PATH, {"version": 1, "watch": []})
    discovered_store = load_json(DISCOVERED_PATH, {"version": 1, "discovered": []})
    archive_store = load_json(ARCHIVE_PATH, {"version": 1, "archived": []})

    repo_map = registry.setdefault("repos", {})
    watch_entries: dict[str, dict] = {}
    archive_entries = {
        a.get("repo_key"): a
        for a in archive_store.get("archived", [])
        if isinstance(a, dict) and a.get("repo_key")
    }
    now_str = datetime.now(KST).strftime("%Y-%m-%d")

    for item in classified:
        repo_key = f"{item['username']}/{item['repo_name']}"
        course = item["course"]
        prev = repo_map.get(repo_key, {})
        seen_count = int(prev.get("seen_count", 0)) + 1

        status_history = list(prev.get("status_history", []))
        status_history.append(
            {
                "date": now_str,
                "status": course.get("status"),
                "course_guess": course.get("course_id"),
            }
        )
        status_history = status_history[-10:]

        repo_state = {
            "username": item["username"],
            "display_name": item.get("display_name"),
            "repo_name": item["repo_name"],
            "repo_url": item["repo_url"],
            "week_guess": str(item.get("week", "")),
            "course_guess": course.get("course_id"),
            "course_label": course.get("course_label"),
            "confidence": course.get("confidence"),
            "status": course.get("status"),
            "evidence": course.get("evidence", [])[:5],
            "first_seen_at": prev.get("first_seen_at", now_str),
            "last_seen_at": now_str,
            "updated_at": item.get("updated_at", ""),
            "seen_count": seen_count,
            "status_history": status_history,
        }
        repo_map[repo_key] = repo_state

        archive_it, archive_reason = should_archive(repo_key, course, repo_state)
        if archive_it:
            archive_entries[repo_key] = {
                "repo_key": repo_key,
                "candidate": prev.get("candidate")
                or {
                    "username": item["username"],
                    "display_name": item.get("display_name", item["username"]),
                    "type": "single_repo" if "/" in item["repo_name"] else "multi_repo",
                    "repo_name": item["repo_name"].split("/")[0] if "/" in item["repo_name"] else None,
                    "folder_pattern": item["repo_name"].split("/", 1)[1] if "/" in item["repo_name"] else None,
                    "repo_patterns": [item["repo_name"]] if "/" not in item["repo_name"] else None,
                    "priority": 9,
                },
                "reason": archive_reason,
                "evidence": course.get("evidence", [])[:5],
                "archived_at": now_str,
                "seen_count": seen_count,
            }
            continue

        if course.get("status") in {"candidate", "review"}:
            cand = {
                "username": item["username"],
                "display_name": item.get("display_name", item["username"]),
                "type": "single_repo" if "/" in item["repo_name"] else "multi_repo",
                "priority": priority_for_watch(course, repo_state),
            }
            if "/" in item["repo_name"]:
                cand["repo_name"] = item["repo_name"].split("/")[0]
                cand["folder_pattern"] = item["repo_name"].split("/", 1)[1]
            else:
                cand["repo_patterns"] = [item["repo_name"]]

            watch_entries[repo_key] = {
                "repo_key": repo_key,
                "course_guess": course.get("course_id"),
                "course_label": course.get("course_label"),
                "status": course.get("status"),
                "candidate": cand,
                "evidence": course.get("evidence", [])[:5],
                "last_seen_at": now_str,
                "source": "classified-run",
            }
        else:
            archive_entries.pop(repo_key, None)

    discovered_entries = {
        d.get("repo_key"): d
        for d in discovered_store.get("discovered", [])
        if isinstance(d, dict) and d.get("repo_key")
    }
    for repo in discovered:
        repo_key = f"{repo['username']}/{repo['repo_name']}"
        candidate = v5_1.discovered_repo_to_candidate(repo)
        discovered_entries[repo_key] = {
            "repo_key": repo_key,
            "candidate": candidate,
            "score": repo.get("score"),
            "evidence": repo.get("evidence", [])[:5],
            "last_seen_at": now_str,
            "source": "global-discovery",
        }
        if repo_key not in watch_entries and repo_key not in archive_entries:
            watch_entries[repo_key] = {
                "repo_key": repo_key,
                "course_guess": "unseen_discovered",
                "course_label": "전역 발견 후보",
                "status": "candidate",
                "candidate": candidate,
                "evidence": repo.get("evidence", [])[:5],
                "last_seen_at": now_str,
                "source": "global-discovery",
            }

    by_user = defaultdict(list)
    for entry in watch_entries.values():
        user = entry.get("candidate", {}).get("username", "")
        by_user[user].append(entry)

    trimmed_watch = []
    for _, entries in by_user.items():
        entries.sort(
            key=lambda e: (
                e.get("candidate", {}).get("priority", 9),
                -len(e.get("evidence", [])),
            )
        )
        keep = entries[:MAX_WATCH_PER_USER]
        overflow = entries[MAX_WATCH_PER_USER:]
        trimmed_watch.extend(keep)
        for entry in overflow:
            archive_entries[entry["repo_key"]] = {
                "repo_key": entry["repo_key"],
                "candidate": entry.get("candidate", {}),
                "reason": "per-user-watch-cap",
                "evidence": entry.get("evidence", [])[:5],
                "archived_at": now_str,
            }

    watchlist["watch"] = trimmed_watch
    discovered_store["discovered"] = list(discovered_entries.values())
    archive_store["archived"] = list(archive_entries.values())

    hygiene = {
        "watch_kept": len(trimmed_watch),
        "archived_total": len(archive_store["archived"]),
        "discovered_total": len(discovered_store["discovered"]),
    }
    return registry, watchlist, discovered_store, archive_store, hygiene


def build_report(
    all_items: list[dict],
    classified: list[dict],
    new_repos: list[dict],
    candidate_pool_size: int,
    hygiene: dict,
) -> tuple[str, dict]:
    confirmed_main = [x for x in classified if x["course"]["course_id"] == "course_2026_main"]
    excluded_legacy = [x for x in classified if x["course"]["status"] == "excluded"]
    review_items = [x for x in classified if x["course"]["status"] in {"candidate", "review"}]

    by_week = defaultdict(list)
    for item in confirmed_main:
        by_week[item["week"]].append(item)

    by_bucket = defaultdict(list)
    for item in review_items:
        by_bucket[item["course"]["course_label"]].append(item)

    client = base.init_genai()
    date_str = datetime.now(KST).strftime("%Y-%m-%d")
    lines: list[str] = []
    lines.append(f"# Codyssey registry-backed collection report v5.2 ({date_str})")
    lines.append("")
    lines.append(f"- 총 수집 건수: {len(all_items)}건")
    lines.append(f"- candidate pool size: {candidate_pool_size}")
    lines.append(f"- 2026 본과정 확정: {len(confirmed_main)}건")
    lines.append(f"- 제외된 레거시/파일럿: {len(excluded_legacy)}건")
    lines.append(f"- 후보/검토 필요: {len(review_items)}건")
    lines.append(f"- active watchlist size: {hygiene['watch_kept']}")
    lines.append(f"- archived candidate size: {hygiene['archived_total']}")
    lines.append(f"- discovered candidate size: {hygiene['discovered_total']}")
    lines.append(f"- 전역 신규 탐색 활성화: {'ON' if ENABLE_GLOBAL_DISCOVERY else 'OFF'}")
    lines.append("")

    lines.append("## 1. 2026 본과정 확정 자료")
    lines.append("")
    for week in sorted(by_week.keys(), key=lambda x: int(x) if str(x).isdigit() else 999):
        lines.append(f"### {week}주차")
        lines.append("")
        lines.append(v4.summarize_week_safe(client, by_week[week], week))
        lines.append("")
        lines.append("| 수강생 | 레포 | 업데이트 | 판정 증거 |")
        lines.append("| --- | --- | --- | --- |")
        for item in sorted(by_week[week], key=lambda x: x["priority"]):
            ev = ", ".join(item["course"]["evidence"][:4]) or "-"
            lines.append(
                f"| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | {item['updated_at']} | {ev} |"
            )
        lines.append("")
        lines.append("---")
        lines.append("")
    if not by_week:
        lines.append("_확정 자료 없음._")
        lines.append("")

    lines.append("## 2. 후보/검토 레포 (active watchlist)")
    lines.append("")
    if by_bucket:
        for bucket, items in by_bucket.items():
            lines.append(f"### {bucket}")
            lines.append("")
            lines.append("| 수강생 | 레포 | 업데이트 | 신뢰도 | 근거 |")
            lines.append("| --- | --- | --- | --- | --- |")
            for item in items:
                ev = ", ".join(item["course"]["evidence"][:5]) or "-"
                lines.append(
                    f"| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | {item['updated_at']} | {item['course']['confidence']:.2f} | {ev} |"
                )
            lines.append("")
    else:
        lines.append("_후보/검토 레포 없음._")
        lines.append("")

    lines.append("## 3. 후보풀 청소 요약")
    lines.append("")
    lines.append(f"- active watch 유지 개수: {hygiene['watch_kept']}")
    lines.append(f"- archive로 이동한 누적 후보 개수: {hygiene['archived_total']}")
    lines.append(f"- discovered 후보 누적 개수: {hygiene['discovered_total']}")
    lines.append("")
    if new_repos:
        lines.append("이번 실행에서 새로 발견된 후보는 watchlist/registry에만 적재되고 자동 확정되지 않습니다.")
        lines.append("")
    else:
        lines.append("_이번 실행에서 새 후보 확장은 없었습니다. (전역 탐색 OFF 또는 신규 미발견)_")
        lines.append("")

    lines.append("## 4. 제외된 레거시/파일럿 레포")
    lines.append("")
    if excluded_legacy:
        lines.append("| 수강생 | 레포 | 업데이트 | 제외 근거 |")
        lines.append("| --- | --- | --- | --- |")
        for item in excluded_legacy:
            ev = ", ".join(item["course"]["evidence"][:5]) or "-"
            lines.append(
                f"| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | {item['updated_at']} | {ev} |"
            )
        lines.append("")
    else:
        lines.append("_제외된 레거시/파일럿 레포 없음._")
        lines.append("")

    payload = {
        "generated_at": date_str,
        "totals": {
            "all_items": len(all_items),
            "candidate_pool_size": candidate_pool_size,
            "confirmed_main": len(confirmed_main),
            "excluded_legacy": len(excluded_legacy),
            "review_items": len(review_items),
            "watch_kept": hygiene["watch_kept"],
            "archived_total": hygiene["archived_total"],
            "discovered_total": hygiene["discovered_total"],
            "new_repos": len(new_repos),
        },
        "items": classified,
    }
    return "\n".join(lines), payload


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
        known_users = {c["username"].lower() for c in candidates if c.get("username")}
        new_repos = base.discover_new_repos(known_users)

    course_map = load_json(COURSE_MAP_PATH, {"repo_overrides": {}, "user_overrides": {}})
    classified = []
    for item in all_items:
        meta = v4.classify_course(item)
        meta = v5_1.maybe_promote_candidate(item, meta)
        meta = v5.apply_manual_overrides(item, meta, course_map)
        merged = dict(item)
        merged["course"] = meta
        classified.append(merged)

    registry, watchlist, discovered_store, archive_store, hygiene = update_state(classified, new_repos)
    save_json(REGISTRY_PATH, registry)
    save_json(WATCHLIST_PATH, watchlist)
    save_json(DISCOVERED_PATH, discovered_store)
    save_json(ARCHIVE_PATH, archive_store)

    report_text, payload = build_report(all_items, classified, new_repos, len(candidates), hygiene)
    date_str = datetime.now(KST).strftime("%Y-%m-%d")
    save_json(REPORT_DIR / f"{date_str}.json", payload)
    (REPORT_DIR / f"{date_str}.md").write_text(report_text, encoding="utf-8")
    (REPORT_DIR / "latest.md").write_text(report_text, encoding="utf-8")

    run_snapshot = {
        "generated_at": date_str,
        "candidate_pool_size": len(candidates),
        "collected_count": len(all_items),
        "new_repo_count": len(new_repos),
        "watchlist_size": hygiene["watch_kept"],
        "archived_total": hygiene["archived_total"],
        "discovered_total": hygiene["discovered_total"],
    }
    save_json(STATE_DIR / f"{date_str}.json", run_snapshot)

    print(f"보고서 생성 완료: {REPORT_DIR / f'{date_str}.md'}")
    print(f"소요 시간: {int(time.time() - start_time)}초")


if __name__ == "__main__":
    main()