#!/usr/bin/env python3
"""
Codyssey 과제 자동 수집기 v2
- 기존 collect.py를 보존하면서 과정/오염 분리를 강화한 실험 버전
- 핵심 목표:
  1) 2026 본과정 / 2025 파일럿 / 후보 과정 / 미분류를 먼저 가른다.
  2) 확정되지 않은 레포는 주차 요약에 섞지 않는다.
  3) GitHub 전역 신규 탐색은 기본 비활성화한다.
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
REPORT_DIR = "reports_v2"
CURRENT_MAIN_START = "2026-03-01"
ENABLE_GLOBAL_DISCOVERY = os.environ.get("ENABLE_GLOBAL_DISCOVERY", "0") == "1"

PILOT_BLACKLIST = [
    "dummysensor",
    "env_values",
    "mars",
    "mars_mission",
    "화성",
    "화성 기지",
    "mars base",
]

CURRENT_MAIN_HINTS = [
    "workstation",
    "docker",
    "quiz",
    "quiz_game",
    "npu",
    "npu_simulator",
    "mini npu",
    "입학연수",
    "codyssey",
]

NATIVE_HINTS = [
    "native",
    "네이티브",
]


def normalize_text(*parts: str) -> str:
    return "\n".join(p for p in parts if p).lower()


def safe_date(date_str: str) -> str:
    return (date_str or "")[:10]


def date_ge(a: str, b: str) -> bool:
    try:
        return a >= b
    except Exception:
        return False


def has_any_keyword(text: str, keywords: list[str]) -> list[str]:
    found = []
    for kw in keywords:
        if kw.lower() in text:
            found.append(kw)
    return found


def has_current_main_fingerprint(file_tree: list[str], text: str) -> list[str]:
    filenames = {p.split("/")[-1].lower() for p in file_tree}
    evidence = []
    for fp in base.FINGERPRINT_TIER1:
        if fp.lower() in filenames:
            evidence.append(f"tier1:{fp}")
    for fp in base.FINGERPRINT_TIER2:
        if fp.lower() in filenames:
            evidence.append(f"tier2:{fp}")
    for kw in CURRENT_MAIN_HINTS:
        if kw.lower() in text:
            evidence.append(f"hint:{kw}")
    return evidence


def classify_course(item: dict) -> dict:
    repo_name = item.get("repo_name", "")
    updated_at = safe_date(item.get("updated_at", ""))
    readme = item.get("readme", "")
    file_tree = item.get("file_tree", []) or []
    text = normalize_text(repo_name, readme, "\n".join(file_tree[:200]))

    pilot_hits = has_any_keyword(text, PILOT_BLACKLIST)
    current_hits = has_current_main_fingerprint(file_tree, text)
    native_hits = has_any_keyword(text, NATIVE_HINTS)

    if pilot_hits and not current_hits:
        return {
            "course_id": "legacy_2025_pilot",
            "course_label": "2025 파일럿",
            "confidence": 0.95,
            "status": "excluded",
            "evidence": [f"blacklist:{x}" for x in pilot_hits],
        }

    if current_hits and date_ge(updated_at, CURRENT_MAIN_START):
        return {
            "course_id": "course_2026_main",
            "course_label": "2026 본과정",
            "confidence": 0.9 if len(current_hits) >= 2 else 0.75,
            "status": "confirmed",
            "evidence": current_hits[:8],
        }

    if native_hits and not pilot_hits:
        return {
            "course_id": "course_2026_native_candidate",
            "course_label": "2026 네이티브(후보)",
            "confidence": 0.6,
            "status": "candidate",
            "evidence": [f"native:{x}" for x in native_hits],
        }

    if pilot_hits and current_hits:
        return {
            "course_id": "mixed_or_legacy",
            "course_label": "혼합/검토 필요",
            "confidence": 0.4,
            "status": "review",
            "evidence": [f"pilot:{x}" for x in pilot_hits] + current_hits[:4],
        }

    return {
        "course_id": "unknown",
        "course_label": "미분류",
        "confidence": 0.3,
        "status": "candidate",
        "evidence": current_hits[:4] if current_hits else ["insufficient-signal"],
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
    excluded_legacy = [x for x in classified if x["course"]["course_id"] == "legacy_2025_pilot"]
    review_items = [x for x in classified if x["course"]["status"] in {"candidate", "review"}]

    by_week = defaultdict(list)
    for item in confirmed_main:
        by_week[item["week"]].append(item)

    by_course_bucket = defaultdict(list)
    for item in review_items:
        by_course_bucket[item["course"]["course_label"]].append(item)

    client = base.init_genai()
    date_str = datetime.now(KST).strftime("%Y-%m-%d")
    lines = []
    lines.append(f"# Codyssey 과정 분리형 수집 보고서 v2 ({date_str})")
    lines.append("")
    lines.append(f"- 총 수집 건수: {len(all_items)}건")
    lines.append(f"- 2026 본과정 확정: {len(confirmed_main)}건")
    lines.append(f"- 제외된 레거시/파일럿: {len(excluded_legacy)}건")
    lines.append(f"- 후보/검토 필요: {len(review_items)}건")
    lines.append(f"- 전역 신규 탐색 활성화: {'ON' if ENABLE_GLOBAL_DISCOVERY else 'OFF'}")
    lines.append("")
    lines.append("## 1. 2026 본과정 확정 자료")
    lines.append("")

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

    lines.append("## 2. 후보 과정 / 미분류 / 혼합 레포")
    lines.append("")
    if by_course_bucket:
        for bucket, items in by_course_bucket.items():
            lines.append(f"### {bucket}")
            lines.append("")
            lines.append("| 수강생 | 레포 | 업데이트 | 신뢰도 | 근거 |")
            lines.append("| --- | --- | --- | --- | --- |")
            for item in items:
                ev = ", ".join(item["course"]["evidence"][:5])
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
            ev = ", ".join(item["course"]["evidence"][:5])
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
    print(f"=== Codyssey v2 수집 시작 ({datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')}) ===")
    start_time = time.time()
    all_items = base.collect()
    print(f"총 {len(all_items)}건 수집 완료")

    new_repos = []
    if ENABLE_GLOBAL_DISCOVERY:
        known_users = {c["username"].lower() for c in base.CANDIDATES}
        new_repos = base.discover_new_repos(known_users)

    report_text, payload = build_report(all_items, new_repos)
    os.makedirs(REPORT_DIR, exist_ok=True)
    date_str = datetime.now(KST).strftime("%Y-%m-%d")
    report_path = os.path.join(REPORT_DIR, f"{date_str}.md")
    latest_path = os.path.join(REPORT_DIR, "latest.md")
    json_path = os.path.join(REPORT_DIR, f"{date_str}.json")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)
    with open(latest_path, "w", encoding="utf-8") as f:
        f.write(report_text)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"보고서 생성 완료: {report_path}")
    print(f"소요 시간: {int(time.time() - start_time)}초")


if __name__ == "__main__":
    main()
