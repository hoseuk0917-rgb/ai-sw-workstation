#!/usr/bin/env python3
"""
Codyssey 과제 자동 수집기
GitHub Actions에서 매주 일요일 오후 9시(KST)에 실행됩니다.
과정 기간: 2026년 3월 30일 ~ 2027년 9월 30일

v3: 후보 22명 (검증된 60명 중 2주차 이상+README 성실한 후보 전체 선별), 전체 주차 스캔, 단일 레포 폴더 패턴 지원
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

# 추적할 후보 수강생 목록 (22명)
# 89명 검색 → 60명 IA 2026 확인 → 2주차 이상 + README 있는 성실한 후보 전체 선별
# 중도 포기자가 생기면 해당 항목의 active를 False로 변경하세요
CANDIDATES = [
    # ── 최우선 후보: 3주차 이상 + README 상세 (★★★) ──
    {
        "username": "I-nkamanda",
        "display_name": "I-nkamanda",
        "type": "single_repo",
        "repo_name": "codyssey2026",
        "folder_pattern": r"[Pp]roblem[_]?(\d+)",
        "priority": 1,
        "active": True,
    },
    {
        "username": "0-hu",
        "display_name": "0-hu",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey[_\-]?e\d+[_\-](\d+)",
            r"codyssey[_\-]?work",
        ],
        "priority": 1,
        "active": True,
    },
    {
        "username": "kimch0612",
        "display_name": "kimch0612",
        "type": "multi_repo",
        "repo_patterns": [
            r"[Cc]odyssey[_\-]?[Ww]eek[_\-]?(\d+)",
        ],
        "priority": 1,
        "active": True,
    },
    {
        "username": "JungSaeYoung",
        "display_name": "JungSaeYoung",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey[_\-]?[Ee]\d+[_\-](\d+)",
        ],
        "priority": 1,
        "active": True,
    },
    {
        "username": "codewhite7777",
        "display_name": "codewhite7777",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey[_\-]?[Ee][_\-]?(\d+)",
            r"codyssey[_\-]?[Ee]\d+[_\-](\d+)",
        ],
        "priority": 1,
        "active": True,
    },
    {
        "username": "mov-hyun",
        "display_name": "mov-hyun",
        "type": "multi_repo",
        "repo_patterns": [
            r"e\d+[_\-](\d+)",
            r"ia[_\-]codyssey",
        ],
        "priority": 1,
        "active": True,
    },
    {
        "username": "sonjehyun123-maker",
        "display_name": "sonjehyun123-maker",
        "type": "multi_repo",
        "repo_patterns": [
            r"[Cc]odyssey[_\-]?w\d+[_\-]?[Ee](\d+)",
            r"[Cc]odyssey",
        ],
        "priority": 1,
        "active": True,
    },
    # ── 우수 후보: 2주차 + README 상세 (★★☆) ──
    {
        "username": "xifoxy-ru",
        "display_name": "xifoxy-ru",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey[_\-]?week[_\-]?(\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "LimJongHan",
        "display_name": "LimJongHan",
        "type": "multi_repo",
        "repo_patterns": [
            r"[Cc]odyssey[_\-]?[Ee]\d+[_\-](\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "sourcreamsource",
        "display_name": "sourcreamsource",
        "type": "multi_repo",
        "repo_patterns": [
            r"[Cc]odyssey[Ww]eek([Oo]ne|[Tt]wo|[Tt]hree|[Ff]our|[Ff]ive|[Ss]ix|[Ss]even|[Ee]ight|[Nn]ine|[Tt]en|\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "coding-monkey-326",
        "display_name": "coding-monkey-326",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey[_\-]?e\d+[_\-](\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "Opdata",
        "display_name": "Opdata",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey[_\-]?(\w+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "mulloc1",
        "display_name": "mulloc1",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey[_\-]?(\w+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "whdals006",
        "display_name": "whdals006",
        "type": "multi_repo",
        "repo_patterns": [
            r"[Cc]odyssey[_\-]?[Ee]\d+[_\-](\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "dolphin1404",
        "display_name": "dolphin1404",
        "type": "multi_repo",
        "repo_patterns": [
            r"[Cc]odyssey[_\-]?[Ee][_\-]?(\d+)",
            r"[Cc]odyssey",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "yeowon083",
        "display_name": "yeowon083",
        "type": "multi_repo",
        "repo_patterns": [
            r"python[_\-]?quiz[_\-]?game",
            r"quiz[_\-]?game",
            r"ia[_\-]codyssey",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "clae-dev",
        "display_name": "clae-dev",
        "type": "multi_repo",
        "repo_patterns": [
            r"ia[_\-]codyssey[_\-]?(\w+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "jhj9109",
        "display_name": "jhj9109",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey(\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "waz6432",
        "display_name": "waz6432",
        "type": "multi_repo",
        "repo_patterns": [
            r"[Cc]odyssey[Ee]\d+[_\-](\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "whitecy01",
        "display_name": "whitecy01",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey(\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "wilderif",
        "display_name": "wilderif",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey[_\-]?e\d+[_\-](\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "yacheahobbang",
        "display_name": "yacheahobbang",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey[_\-]?[Ee]\d+[_\-](\d+)",
            r"ia[_\-]codyssey",
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
    params = {"sort": "updated", "direction": "desc", "per_page": 100}
    try:
        r = requests.get(url, headers=github_headers(), params=params, timeout=15)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"  [오류] {username} 레포 조회 실패: {e}")
        return []


def get_readme(username: str, repo: str, path: str = "") -> str:
    """README 조회. path가 주어지면 해당 폴더의 README를 가져옴."""
    if path:
        url = f"https://api.github.com/repos/{username}/{repo}/contents/{path}/README.md"
    else:
        url = f"https://api.github.com/repos/{username}/{repo}/readme"
    try:
        r = requests.get(url, headers=github_headers(), timeout=15)
        if r.status_code == 404:
            return ""
        r.raise_for_status()
        return base64.b64decode(r.json().get("content", "")).decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  [오류] {username}/{repo}/{path} README 조회 실패: {e}")
        return ""


def get_repo_folders(username: str, repo: str) -> list:
    """레포 루트의 폴더 목록 조회."""
    url = f"https://api.github.com/repos/{username}/{repo}/contents/"
    try:
        r = requests.get(url, headers=github_headers(), timeout=15)
        if r.status_code != 200:
            return []
        return [item["name"] for item in r.json() if item["type"] == "dir"]
    except Exception as e:
        print(f"  [오류] {username}/{repo} 폴더 조회 실패: {e}")
        return []


def get_repo_info(username: str, repo_name: str) -> dict | None:
    """특정 레포의 정보 조회."""
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    try:
        r = requests.get(url, headers=github_headers(), timeout=15)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        print(f"  [오류] {username}/{repo_name} 조회 실패: {e}")
        return None


def detect_week(name: str, patterns: list) -> str | None:
    for pattern in patterns:
        m = re.search(pattern, name, re.IGNORECASE)
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

def collect_single_repo(c: dict) -> list:
    """단일 레포에서 폴더별로 주차를 추출하는 방식 (예: I-nkamanda/codyssey2026)."""
    results = []
    username = c["username"]
    repo_name = c["repo_name"]
    folder_pattern = c["folder_pattern"]

    print(f"\n[{c['display_name']}] 단일 레포 {repo_name} 폴더 스캔 중...")

    repo_info = get_repo_info(username, repo_name)
    if not repo_info:
        print(f"  [경고] 레포 {repo_name}을 찾을 수 없습니다.")
        return results

    folders = get_repo_folders(username, repo_name)
    for folder in folders:
        m = re.search(folder_pattern, folder, re.IGNORECASE)
        if not m:
            continue
        week = m.group(1).lstrip("0") or "0"
        print(f"  → 폴더 {folder} ({week}주차)")

        readme = get_readme(username, repo_name, folder)
        if not readme:
            # 폴더 내 README가 없으면 루트 README 시도
            readme = get_readme(username, repo_name)

        print(f"     AI 요약 중...")
        summary = summarize(readme, week)

        results.append({
            "username": username,
            "display_name": c["display_name"],
            "repo_name": f"{repo_name}/{folder}",
            "repo_url": f"https://github.com/{username}/{repo_name}/tree/main/{folder}",
            "week": week,
            "updated_at": repo_info.get("updated_at", "")[:10],
            "readme_length": len(readme),
            "summary": summary,
            "priority": c["priority"],
        })

    return results


def collect_multi_repo(c: dict) -> list:
    """여러 레포에서 주차를 추출하는 방식 (기존 방식)."""
    results = []
    username = c["username"]

    print(f"\n[{c['display_name']}] 레포 조회 중...")

    for repo in get_user_repos(username):
        name = repo["name"]
        week = detect_week(name, c["repo_patterns"])
        if week is None:
            continue

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

    return results


def collect() -> list:
    """전체 후보에서 모든 주차를 스캔하여 수집."""
    results = []
    seen = set()

    for c in CANDIDATES:
        if not c.get("active", True):
            continue

        if c.get("type") == "single_repo":
            items = collect_single_repo(c)
        else:
            items = collect_multi_repo(c)

        for item in items:
            key = f"{item['username']}/{item['repo_name']}"
            if key not in seen:
                seen.add(key)
                results.append(item)

    results.sort(key=lambda x: (int(x["week"]) if x["week"].isdigit() else 99, x["priority"]))
    return results


# ─── 보고서 생성 ──────────────────────────────────────────────────────────────

def make_report(assignments: list, now: datetime) -> str:
    date_str = now.strftime("%Y년 %m월 %d일")
    lines = [
        "# Codyssey 과제 수집 보고서",
        "",
        f"> **수집 일시**: {date_str} {now.strftime('%H:%M')} KST  ",
        f"> **총 수집 과제**: {len(assignments)}건  ",
        f"> **추적 후보**: {sum(1 for c in CANDIDATES if c.get('active', True))}명",
        "",
        "---",
        "",
    ]

    if not assignments:
        lines.append("이번 주에 새로 업데이트된 과제가 없습니다.")
        return "\n".join(lines)

    # 주차별로 그룹핑
    by_week: dict[str, list] = {}
    for a in assignments:
        by_week.setdefault(a["week"], []).append(a)

    for week in sorted(by_week.keys(), key=lambda x: int(x) if x.isdigit() else 99):
        items = by_week[week]
        # 우선순위가 높고 README가 가장 긴 항목을 대표로 선택
        primary = sorted(items, key=lambda a: (-a["readme_length"], a["priority"]))[0]

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
