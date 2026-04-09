#!/usr/bin/env python3
"""
Codyssey 과제 자동 수집기
GitHub Actions에서 매주 일요일 오후 9시(KST)에 실행됩니다.
과정 기간: 2026년 3월 30일 ~ 2027년 9월 30일
"""

import os
import json
import re
import base64
from datetime import datetime, timezone, timedelta

import requests
import google.generativeai as genai

# ─── 설정 ────────────────────────────────────────────────────────────────────

KST = timezone(timedelta(hours=9))

# 과정 종료일 (이 날짜 이후 실행 시 경고 출력)
COURSE_END = datetime(2027, 9, 30, tzinfo=KST)

# 추적할 후보 수강생 목록
# 중도 포기자가 생기면 해당 항목의 active를 False로 변경하세요
CANDIDATES = [
    {
        "username": "xifoxy-ru",
        "display_name": "xifoxy-ru",
        "repo_patterns": [
            r"codyssey[_\-]?week[_\-]?(\d+)",
            r"codyssey[_\-]?e\d+[_\-](\d+)",
        ],
        "priority": 1,
        "active": True,
    },
    {
        "username": "LimJongHan",
        "display_name": "LimJongHan",
        "repo_patterns": [
            r"[Cc]odyssey[_\-]?[Ee]\d+[_\-](\d+)",
            r"[Cc]odyssey[_\-]?[Ww]eek[_\-]?(\d+)",
        ],
        "priority": 1,
        "active": True,
    },
    {
        "username": "sourcreamsource",
        "display_name": "sourcreamsource",
        "repo_patterns": [
            r"[Cc]odyssey[Ww]eek([Oo]ne|[Tt]wo|[Tt]hree|[Ff]our|[Ff]ive|[Ss]ix|[Ss]even|[Ee]ight|[Nn]ine|[Tt]en|\d+)",
            r"[Cc]odyssey[_\-]?[Ww]eek[_\-]?(\d+)",
        ],
        "priority": 1,
        "active": True,
    },
    {
        "username": "coding-monkey-326",
        "display_name": "coding-monkey-326",
        "repo_patterns": [
            r"codyssey[_\-]?e\d+[_\-](\d+)",
            r"codyssey[_\-]?week[_\-]?(\d+)",
        ],
        "priority": 2,
        "active": True,
    },
]

WORD_TO_NUM = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
}

# ─── GitHub API ───────────────────────────────────────────────────────────────

def github_headers() -> dict:
    token = os.environ.get("GITHUB_TOKEN", "")
    h = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def get_user_repos(username: str) -> list:
    url = f"https://api.github.com/users/{username}/repos"
    params = {"sort": "updated", "direction": "desc", "per_page": 50}
    try:
        r = requests.get(url, headers=github_headers(), params=params, timeout=15)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"  [오류] {username} 레포 조회 실패: {e}")
        return []


def get_readme(username: str, repo: str) -> str:
    url = f"https://api.github.com/repos/{username}/{repo}/readme"
    try:
        r = requests.get(url, headers=github_headers(), timeout=15)
        if r.status_code == 404:
            return ""
        r.raise_for_status()
        return base64.b64decode(r.json().get("content", "")).decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  [오류] {username}/{repo} README 조회 실패: {e}")
        return ""


def detect_week(repo_name: str, patterns: list) -> str | None:
    for pattern in patterns:
        m = re.search(pattern, repo_name, re.IGNORECASE)
        if m:
            val = m.group(1).lower()
            return WORD_TO_NUM.get(val, val.lstrip("0") or "0")
    return None


# ─── AI 요약 ──────────────────────────────────────────────────────────────────

def summarize(readme: str, week: str) -> str:
    if not readme.strip():
        return "_README 내용 없음_"

    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        print("  [경고] GEMINI_API_KEY 없음 — README 원문으로 대체")
        return readme[:800] + "\n\n_*(API 키 없음 — 원문 일부)*_"

    genai.configure(api_key=api_key)
    # gemini-2.5-flash-lite: 무료 티어 기준 RPM 15, RPD 1,000으로 가장 넉넉
    # 매주 1회 실행 시 최대 8회 호출 → 무료 한도 내 충분히 동작
    model = genai.GenerativeModel("gemini-2.5-flash-lite")

    prompt = f"""다음은 Codyssey 프로그램 {week}주차 과제 레포의 README.md입니다.
학습자가 이 과제 내용을 자신의 학습 자료로 내재화할 수 있도록 아래 형식으로 정리해 주세요.

## 과제 주제
한 줄로 핵심 주제를 작성하세요.

## 학습 목표
이 과제를 통해 배워야 할 핵심 개념 3~5가지를 작성하세요.

## 주요 내용 요약
과제에서 다루는 주요 내용을 200자 이내로 요약하세요.

## 핵심 기술 및 개념
등장하는 기술 스택, 명령어, 개념 키워드를 나열하세요.

## 과제 요구사항
체크리스트나 수행 항목을 정리하세요 (있는 경우).

---
README 내용:
{readme[:6000]}
---
한국어로 작성해 주세요."""

    try:
        resp = model.generate_content(prompt)
        return resp.text.strip()
    except Exception as e:
        print(f"  [오류] AI 요약 실패: {e}")
        return readme[:800] + "\n\n_*(AI 요약 실패 — 원문 일부)*_"


# ─── 수집 ─────────────────────────────────────────────────────────────────────

def collect() -> list:
    results = []
    seen = set()

    for c in CANDIDATES:
        if not c.get("active", True):
            continue
        username = c["username"]
        print(f"\n[{c['display_name']}] 레포 조회 중...")

        for repo in get_user_repos(username):
            name = repo["name"]
            week = detect_week(name, c["repo_patterns"])
            if week is None:
                continue
            key = f"{username}/{name}"
            if key in seen:
                continue
            seen.add(key)

            updated = repo.get("updated_at", "")[:10]
            print(f"  → {name} ({week}주차, 업데이트: {updated})")

            readme = get_readme(username, name)
            print(f"     AI 요약 중...")
            summary = summarize(readme, week)

            results.append({
                "username": username,
                "display_name": c["display_name"],
                "repo_name": name,
                "repo_url": repo.get("html_url", f"https://github.com/{username}/{name}"),
                "week": week,
                "updated_at": updated,
                "readme_length": len(readme),
                "summary": summary,
                "priority": c["priority"],
            })

    results.sort(key=lambda x: (int(x["week"]) if x["week"].isdigit() else 99, x["priority"]))
    return results


# ─── 보고서 생성 ──────────────────────────────────────────────────────────────

def make_report(assignments: list, now: datetime) -> str:
    date_str = now.strftime("%Y년 %m월 %d일")
    lines = [
        "# Codyssey 과제 수집 보고서",
        "",
        f"> **수집 일시**: {date_str} {now.strftime('%H:%M')} KST  ",
        f"> **총 수집 과제**: {len(assignments)}건",
        "",
        "---",
        "",
    ]

    if not assignments:
        lines.append("이번 주에 새로 업데이트된 과제가 없습니다.")
        return "\n".join(lines)

    by_week: dict[str, list] = {}
    for a in assignments:
        by_week.setdefault(a["week"], []).append(a)

    for week in sorted(by_week.keys(), key=lambda x: int(x) if x.isdigit() else 99):
        items = by_week[week]
        primary = next((a for a in items if a["priority"] == 1), items[0])

        lines += [
            f"## {week}주차 과제",
            "",
            "### 과제 내용 정리",
            "",
            primary["summary"],
            "",
            "### 참고 레포",
            "",
            "| 수강생 | 레포 | 최종 업데이트 | README 분량 |",
            "|--------|------|:------------:|:-----------:|",
        ]
        for a in items:
            length = f"{a['readme_length']:,}자" if a["readme_length"] > 0 else "없음"
            lines.append(
                f"| {a['display_name']} | [{a['repo_name']}]({a['repo_url']}) | {a['updated_at']} | {length} |"
            )
        lines += ["", "---", ""]

    return "\n".join(lines)


# ─── 실행 ─────────────────────────────────────────────────────────────────────

def main():
    now = datetime.now(KST)
    print(f"Codyssey 과제 수집 시작: {now.strftime('%Y-%m-%d %H:%M:%S KST')}")

    if now > COURSE_END:
        print("⚠️  과정 종료일(2027-09-30)이 지났습니다. 수집을 건너뜁니다.")
        return

    assignments = collect()

    os.makedirs("reports", exist_ok=True)
    report = make_report(assignments, now)

    dated_path = f"reports/{now.strftime('%Y-%m-%d')}.md"
    with open(dated_path, "w", encoding="utf-8") as f:
        f.write(report)

    with open("reports/latest.md", "w", encoding="utf-8") as f:
        f.write(report)

    with open(f"reports/{now.strftime('%Y-%m-%d')}.json", "w", encoding="utf-8") as f:
        json.dump(
            {"collected_at": now.isoformat(), "assignments": assignments},
            f, ensure_ascii=False, indent=2,
        )

    print(f"\n완료! 총 {len(assignments)}건 수집 → {dated_path}")


if __name__ == "__main__":
    main()
