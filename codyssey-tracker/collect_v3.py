#!/usr/bin/env python3
"""
Codyssey 과정 분리형 수집기 v3
- v2보다 보수적인 확정 정책
- 레거시 날짜 컷 추가
- 증거는 레포명/README 중심으로만 산출
- 애매하면 확정하지 않고 후보/검토로 남김
"""

from __future__ import annotations

import json
import os
import re
import time
from collections import defaultdict
from datetime import datetime

import collect as base

KST = base.KST
REPORT_DIR = "reports_v3"
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
]

NATIVE_HINTS = ["native", "네이티브"]
WEAK_HINTS = {"codyssey", "입학연수"}


def safe_date(s: str) -> str:
    return (s or "")[:10]


def contains_any(text: str, keywords: list[str]) -> list[str]:
    t = (text or "").lower()
    return [kw for kw in keywords if kw.lower() in t]


def tier_evidence_from_file_tree(file_tree: list[str]) -> list[str]:
    filenames = {p.split("/")[-1].lower() for p in (file_tree or [])}
    ev = []
    for fp in base.FINGERPRINT_TIER1:
        if fp.lower() in filenames:
            ev.append(f"tier1:{fp}")
    for fp in base.FINGERPRINT_TIER2:
        if fp.lower() in filenames:
            ev.append(f"tier2:{fp}")
    return ev


def repo_text(item: dict) -> str:
    repo_name = item.get("repo_name", "")
    readme = item.get("readme", "")
    # file_tree 전체는 증거 산출에는 쓰지 않음. 오염을 줄이기 위해 파일명만 사용.
    filenames = [p.split("/")[-1] for p in (item.get("file_tree", []) or [])[:150]]
    return "\n".join([repo_name, readme, "\n".join(filenames)]).lower()


def precise_hint_evidence(item: dict) -> list[str]:
    repo_name = (item.get("repo_name", "") or "").lower()
    readme = (item.get("readme", "") or "").lower()
    ev = []

    # 레포명은 가장 강한 힌트로 사용
    for kw in MAIN_REPO_HINTS:
        if kw in repo_name:
            ev.append(f"repo:{kw}")

    # README 힌트는 약한 신호는 제외하고, 최대 2개까지만 사용
    readme_hits = []
    for kw in MAIN_REPO_HINTS:
        if kw in readme and kw not in WEAK_HINTS:
            readme_hits.append(f"readme:{kw}")
    ev.extend(readme_hits[:2])
    return ev


def week_consistency_score(item: dict) -> tuple[int, list[str]]:
    week = str(item.get("week", ""))
    repo_name = (item.get("repo_name", "") or "").lower()
    readme = (item.get("readme", "") or "").lower()
    evidence = []
    score = 0

    if week == "1":
        kws = ["workstation", "docker", "setup"]
    elif week == "2":
        kws = ["quiz", "quiz_game", "python_with_git", "first_python"]
    elif week == "3":
        kws = ["npu", "npu_simulator", "mini_npu", "mac"]
    else:
        kws = []

    for kw in kws:
        if kw in repo_name:
            score += 2
            evidence.append(f"week-repo:{kw}")
        elif kw in readme:
            score += 1
            evidence.append(f"week-readme:{kw}")

    return score, evidence[:3]


def classify_course(item: dict) -> dict:
    updated_at = safe_date(item.get("updated_at", ""))
    text = repo_text(item)
    tier_ev = tier_evidence_from_file_tree(item.get("file_tree", []) or [])
    hint_ev = precise_hint_evidence(item)
    week_score, week_ev = week_consistency_score(item)
    pilot_hits = contains_any(text, PILOT_BLACKLIST)
    native_hits = contains_any(text, NATIVE_HINTS)

    strong_tier1 = any(x.startswith("tier1:") for x in tier_ev)
    strong_tier2_count = sum(1 for x in tier_ev if x.startswith("tier2:"))
    strong_hint_count = len(hint_ev)

    if updated_at and updated_at < LEGACY_HARD_CUTOFF:
        return {
            "course_id": "legacy_pre2026",
            "course_label": "레거시(날짜 컷)",
            "confidence": 0.98,
            "status": "excluded",
            "evidence": [f"updated_at:{updated_at}", "rule:legacy-hard-cutoff"],
        }

    if pilot_hits and not (strong_tier1 or strong_tier2_count >= 2):
        return {
            "course_id": "legacy_2025_pilot",
            "course_label": "2025 파일럿",
            "confidence": 0.95,
            "status": "excluded",
            "evidence": [f"pilot:{x}" for x in pilot_hits[:4]],
        }

    if native_hits and not strong_tier1 and week_score == 0:
        return {
            "course_id": "course_2026_native_candidate",
            "course_label": "2026 네이티브(후보)",
            "confidence": 0.65,
            "status": "candidate",
            "evidence": [f"native:{x}" for x in native_hits[:3]],
        }

    # 확정 정책 강화:
    # 1) 날짜가 2026-03-01 이후
    # 2) 아래 중 하나 충족
    #   - tier1 1개 이상 + 주차 일치 점수 1 이상
    #   - tier2 2개 이상 + 힌트 1개 이상 + 주차 일치 점수 1 이상
    #   - repo 이름에 주차 핵심 키워드 직접 포함 + 힌트 2개 이상
    if updated_at >= CURRENT_MAIN_START:
        if strong_tier1 and week_score >= 1:
            ev = (tier_ev + week_ev + hint_ev)[:5]
            return {
                "course_id": "course_2026_main",
                "course_label": "2026 본과정",
                "confidence": 0.92,
                "status": "confirmed",
                "evidence": ev,
            }
        if strong_tier2_count >= 2 and strong_hint_count >= 1 and week_score >= 1:
            ev = (tier_ev + week_ev + hint_ev)[:5]
            return {
                "course_id": "course_2026_main",
                "course_label": "2026 본과정",
                "confidence": 0.84,
                "status": "confirmed",
                "evidence": ev,
            }
        repo_week_kw = any(x.startswith("week-repo:") for x in week_ev)
        if repo_week_kw and strong_hint_count >= 2:
            ev = (week_ev + hint_ev + tier_ev)[:5]
            return {
                "course_id": "course_2026_main",
                "course_label": "2026 본과정",
                "confidence": 0.78,
                "status": "confirmed",
                "evidence": ev,
            }

    if pilot_hits and (strong_tier1 or strong_tier2_count >= 1):
        return {
            "course_id": "mixed_or_legacy",
            "course_label": "혼합/검토 필요",
            "confidence": 0.45,
            "status": "review",
            "evidence": ([f"pilot:{x}" for x in pilot_hits[:2]] + tier_ev + week_ev + hint_ev)[:5],
        }

    return {
        "course_id": "unknown",
        "course_label": "미분류",
        "confidence": 0.25,
        "status": "candidate",
        "evidence": (week_ev + hint_ev + tier_ev)[:4] or ["insufficient-signal"],
    }


def summarize_week_safe(client, items: list[dict], week: str) -> str:
    if not items:
        return "_확정된 자료가 없어 요약을 생략합니다._"
    return base.summarize_week(client, items, week)


def build_report(all_items: list[dict], new_repos: list[dict]) -> tuple[str, dict]:
    classified = []
    for item in all_items:
        meta = classify_course(item)
        merged = dict(item)
        merged["course"] = meta
        classified.append(merged)

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
    lines = []
    lines.append(f"# Codyssey 과정 분리형 수집 보고서 v3 ({date_str})")
    lines.append("")
    lines.append(f"- 총 수집 건수: {len(all_items)}건")
    lines.append(f"- 2026 본과정 확정: {len(confirmed_main)}건")
    lines.append(f"- 제외된 레거시/파일럿: {len(excluded_legacy)}건")
    lines.append(f"- 후보/검토 필요: {len(review_items)}건")
    lines.append(f"- 전역 신규 탐색 활성화: {'ON' if ENABLE_GLOBAL_DISCOVERY else 'OFF'}")
    lines.append("")

    lines.append("## 1. 2026 본과정 확정 자료")
    lines.append("")
    if by_week:
        for week in sorted(by_week.keys(), key=lambda x: int(x) if str(x).isdigit() else 999):
            lines.append(f"### {week}주차")
            lines.append("")
            lines.append(summarize_week_safe(client, by_week[week], week))
            lines.append("")
            lines.append("#### 참여 수강생 및 증거")
            lines.append("| 수강생 | 레포 | 업데이트 | 과정 판정 증거 |")
            lines.append("| --- | --- | --- | --- |")
            for item in sorted(by_week[week], key=lambda x: x["priority"]):
                ev = ", ".join(item["course"]["evidence"][:4]) or "-"
                lines.append(f"| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | {item['updated_at']} | {ev} |")
            lines.append("")
            lines.append("---")
            lines.append("")
    else:
        lines.append("_확정 자료 없음._")
        lines.append("")

    lines.append("## 2. 후보 과정 / 미분류 / 혼합 레포")
    lines.append("")
    if by_bucket:
        for bucket, items in by_bucket.items():
            lines.append(f"### {bucket}")
            lines.append("")
            lines.append("| 수강생 | 레포 | 업데이트 | 신뢰도 | 근거 |")
            lines.append("| --- | --- | --- | --- | --- |")
            for item in items:
                ev = ", ".join(item["course"]["evidence"][:5]) or "-"
                lines.append(f"| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | {item['updated_at']} | {item['course']['confidence']:.2f} | {ev} |")
            lines.append("")
    else:
        lines.append("_후보 과정/미분류 레포 없음._")
        lines.append("")

    lines.append("## 3. 제외된 레거시/파일럿 레포")
    lines.append("")
    if excluded_legacy:
        lines.append("| 수강생 | 레포 | 업데이트 | 제외 근거 |")
        lines.append("| --- | --- | --- | --- |")
        for item in excluded_legacy:
            ev = ", ".join(item['course']['evidence'][:5]) or "-"
            lines.append(f"| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | {item['updated_at']} | {ev} |")
        lines.append("")
    else:
        lines.append("_제외된 레거시/파일럿 레포 없음._")
        lines.append("")

    if new_repos:
        lines.append("## 4. 전역 신규 발견 레포")
        lines.append("")
        lines.append("기본값은 OFF이며, 활성화 시에도 자동 편입하지 않고 참고 목록으로만 남깁니다.")
        lines.append("")
        lines.append("| 사용자 | 레포 | 점수 | 발견 증거 |")
        lines.append("| --- | --- | --- | --- |")
        for r in new_repos:
            lines.append(f"| {r['username']} | [{r['repo_name']}]({r['repo_url']}) | {r['score']} | {', '.join(r['evidence'])} |")
        lines.append("")

    payload = {
        "generated_at": date_str,
        "totals": {
            "all_items": len(all_items),
            "confirmed_main": len(confirmed_main),
            "excluded_legacy": len(excluded_legacy),
            "review_items": len(review_items),
            "new_repos": len(new_repos),
        },
        "items": classified,
    }
    return "\n".join(lines), payload


def main() -> None:
    print(f"=== Codyssey v3 수집 시작 ({datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')}) ===")
    start_time = time.time()
    all_items = base.collect()
    print(f"총 {len(all_items)}건 수집 완료")

    new_repos = []
    if ENABLE_GLOBAL_DISCOVERY:
        known_users = {c['username'].lower() for c in base.CANDIDATES}
        new_repos = base.discover_new_repos(known_users)

    report_text, payload = build_report(all_items, new_repos)
    os.makedirs(REPORT_DIR, exist_ok=True)
    date_str = datetime.now(KST).strftime("%Y-%m-%d")
    report_path = os.path.join(REPORT_DIR, f"{date_str}.md")
    latest_path = os.path.join(REPORT_DIR, "latest.md")
    json_path = os.path.join(REPORT_DIR, f"{date_str}.json")

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
