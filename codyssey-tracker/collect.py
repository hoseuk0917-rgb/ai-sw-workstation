#!/usr/bin/env python3
"""
Codyssey 과제 자동 수집기
GitHub Actions에서 매주 일요일 오후 9시(KST)에 실행됩니다.
과정 기간: 2026년 3월 30일 ~ 2027년 9월 30일

v4: 보고서 구조 전면 개편
    - 주차별 학습 문서 형태로 출력 (과제 PDF 수준의 체계적 정리)
    - 수강생 레포에서 코드 구조, 트러블슈팅, 학습 자료 추출
    - 주차 감지 버그 수정 (python, docker 등 잘못된 주차명 필터링)
    - 후보 22명, 전체 주차 스캔, 단일 레포 폴더 패턴 지원

v5: 후보 대폭 확충 + 과제별 레포 패턴 보완
    - GitHub 검색으로 70명 신규 후보 발견, 우수 후보 25명 추가 (총 47명)
    - 과제마다 레포를 새로 파는 수강생 패턴 대응 (mission, m, workspace 등)
    - 단일 레포 + 폴더 패턴 수강생 대응 (week, problem, mission, e1, c01-p0N 등)
    - leehnmn: 2025 파일럿 + 2026 본과정 동시 추적
"""

import os
import json
import re
import base64
import time
from datetime import datetime, timezone, timedelta

import requests
try:
    from google import genai
    USE_NEW_GENAI = True
except ImportError:
    import google.generativeai as genai
    USE_NEW_GENAI = False

# ─── 설정 ────────────────────────────────────────────────────────────────────

KST = timezone(timedelta(hours=9))

# 과정 종료일 (이 날짜 이후 실행 시 경고 출력)
COURSE_END = datetime(2027, 9, 30, tzinfo=KST)

# 유효한 주차 범위 (숫자만 허용, 1~52)
VALID_WEEK_RANGE = range(1, 53)

# 추적할 후보 수강생 목록 (47명)
CANDIDATES = [
    # ══════════════════════════════════════════════════════════════════════
    # ── 최우선 후보: 3주차 이상 + README 상세 (★★★) ──
    # ══════════════════════════════════════════════════════════════════════
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
        ],
        "priority": 1,
        "active": True,
    },
    # ══════════════════════════════════════════════════════════════════════
    # ── 우수 후보: 2주차 + README 상세 (★★☆) ──
    # ══════════════════════════════════════════════════════════════════════
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
            r"codyssey[_\-]?(?:workstation|python|docker|npu)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "mulloc1",
        "display_name": "mulloc1",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey[_\-]?(?:workstation|first_python|python_with_npu)",
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
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "clae-dev",
        "display_name": "clae-dev",
        "type": "multi_repo",
        "repo_patterns": [
            r"ia[_\-]codyssey[_\-]?(?:Python|Docker)",
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
        ],
        "priority": 2,
        "active": True,
    },
    # ══════════════════════════════════════════════════════════════════════
    # ── v5 신규 후보: GitHub 검색으로 발견 (★★☆ ~ ★☆☆) ──
    # ══════════════════════════════════════════════════════════════════════
    #
    # --- 과제마다 레포를 새로 파는 수강생 (multi-repo) ---
    {
        "username": "jhkr1",
        "display_name": "jhkr1",
        "type": "multi_repo",
        "repo_patterns": [
            r"[Cc]odyssey[_\-]?mission[_\-]?(\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "junhnno",
        "display_name": "junhnno",
        "type": "multi_repo",
        "repo_patterns": [
            r"[Cc]odyssey[_\-]?[Ww]ork[Ss]pace[_\-]?[Ww]eek[_\-]?(\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        "username": "sungho255",
        "display_name": "sungho255",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey[_\-](\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        # 과제별 레포: codyssey-m1, codyssey-m2
        "username": "yejoo0310",
        "display_name": "yejoo0310",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey[_\-]m(\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        # codyssey11-E1 → E 뒤 번호 추출
        "username": "peachily",
        "display_name": "peachily",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey\d*[_\-]?[Ee][_\-]?(\d+)",
        ],
        "priority": 2,
        "active": True,
    },
    {
        # codyssey-e1-1 패턴
        "username": "ikasoon",
        "display_name": "ikasoon",
        "type": "multi_repo",
        "repo_patterns": [
            r"codyssey[_\-]?e\d+[_\-](\d+)",
        ],
        "priority": 3,
        "active": True,
    },
    #
    # --- 단일 레포 + 폴더 패턴 수강생 (single-repo) ---
    {
        # codyssey → 1week, 2week, 3week, 4week
        "username": "park-soo-hyeon",
        "display_name": "park-soo-hyeon",
        "type": "single_repo",
        "repo_name": "codyssey",
        "folder_pattern": r"(\d+)week",
        "priority": 2,
        "active": True,
    },
    {
        # codyssey → problem_1, problem_2, problem_3, problem_4
        "username": "dldnsgkr",
        "display_name": "dldnsgkr",
        "type": "single_repo",
        "repo_name": "codyssey",
        "folder_pattern": r"problem[_\-]?(\d+)",
        "priority": 2,
        "active": True,
    },
    {
        # codyssey → e1_1, e1_2
        "username": "ntt65",
        "display_name": "ntt65",
        "type": "single_repo",
        "repo_name": "codyssey",
        "folder_pattern": r"e\d+[_\-](\d+)",
        "priority": 2,
        "active": True,
    },
    {
        # ia-codyssey → 2week, 3week, 4week, 5week
        "username": "kwonhee1",
        "display_name": "kwonhee1",
        "type": "single_repo",
        "repo_name": "ia-codyssey",
        "folder_pattern": r"(\d+)week",
        "priority": 2,
        "active": True,
    },
    {
        # ia-codyssey → mars_mission, mars_mission2 등
        "username": "kwung0206",
        "display_name": "kwung0206",
        "type": "single_repo",
        "repo_name": "ia-codyssey",
        "folder_pattern": r"(?:mars[_\-]?)?mission[_\-]?(\d+)",
        "priority": 2,
        "active": True,
    },
    {
        # codyssey-mission → mission1, mission2, mission3, mission4
        "username": "sebin1103",
        "display_name": "sebin1103",
        "type": "single_repo",
        "repo_name": "codyssey-mission",
        "folder_pattern": r"mission[_\-]?(\d+)",
        "priority": 2,
        "active": True,
    },
    {
        # codyssey-ai-sw → c01-p01-*, c01-p06-*, c01-p07-*
        "username": "jyaniee",
        "display_name": "jyaniee",
        "type": "single_repo",
        "repo_name": "codyssey-ai-sw",
        "folder_pattern": r"c\d+[_\-]p(\d+)",
        "priority": 2,
        "active": True,
    },
    {
        # codyssey_ai → missions 폴더
        "username": "OliverJoo",
        "display_name": "OliverJoo",
        "type": "single_repo",
        "repo_name": "codyssey_ai",
        "folder_pattern": r"mission[_\-]?(\d+)",
        "priority": 2,
        "active": True,
    },
    {
        # Codyssey-Assignments → Assignment-1-Docker, Assignment-2-Python
        "username": "js910",
        "display_name": "js910",
        "type": "single_repo",
        "repo_name": "Codyssey-Assignments",
        "folder_pattern": r"[Aa]ssignment[_\-]?(\d+)",
        "priority": 2,
        "active": True,
    },
    {
        # codyssey-workstation → assignment1, assignment2
        "username": "mackerel07",
        "display_name": "mackerel07",
        "type": "single_repo",
        "repo_name": "codyssey-workstation",
        "folder_pattern": r"assignment[_\-]?(\d+)",
        "priority": 3,
        "active": True,
    },
    {
        # codyssey-project → curriculum, docker, scripts
        "username": "gkrtod4477",
        "display_name": "gkrtod4477",
        "type": "single_repo",
        "repo_name": "codyssey-project",
        "folder_pattern": r"(?:curriculum|docker|scripts)",
        "priority": 3,
        "active": True,
    },
    #
    # --- 2025 파일럿 + 2026 본과정 동시 참여 ---
    {
        # codyssey (2025 파일럿, 1016파일) + codyssey_2026 (본과정)
        "username": "leehnmn",
        "display_name": "leehnmn",
        "type": "single_repo",
        "repo_name": "codyssey_2026",
        "folder_pattern": r"project[_\-]?(\d+)",
        "priority": 2,
        "active": True,
    },
    #
    # --- 활발한 단일 레포 수강생 (폴더 패턴 범용) ---
    {
        "username": "hodoon",
        "display_name": "hodoon",
        "type": "single_repo",
        "repo_name": "codyssey",
        "folder_pattern": r"(?:problem|mission|week|assignment|e\d+)[_\-]?(\d+)",
        "priority": 3,
        "active": True,
    },
    {
        "username": "hyunn9799",
        "display_name": "hyunn9799",
        "type": "single_repo",
        "repo_name": "codyssey",
        "folder_pattern": r"(?:problem|mission|week|assignment|e\d+)[_\-]?(\d+)",
        "priority": 3,
        "active": True,
    },
    {
        "username": "1anminJ",
        "display_name": "1anminJ",
        "type": "single_repo",
        "repo_name": "Codyssey",
        "folder_pattern": r"(?:essential[_\-]?step|problem|mission|week)[_\-]?(\d+)",
        "priority": 3,
        "active": True,
    },
    {
        "username": "yejibaek12",
        "display_name": "yejibaek12",
        "type": "single_repo",
        "repo_name": "Codyssey",
        "folder_pattern": r"(?:task|problem|mission|week)[_\-]?(\d+)",
        "priority": 3,
        "active": True,
    },
    {
        # 계정명 자체가 sangwoo-codyssey, 레포명은 01-infra-basics-study
        "username": "sangwoo-codyssey",
        "display_name": "sangwoo-codyssey",
        "type": "multi_repo",
        "repo_patterns": [
            r"(\d+)[_\-]",
        ],
        "priority": 3,
        "active": True,
    },
]

WORD_TO_NUM = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
}

# 주차로 오인될 수 있는 키워드 매핑 (레포 이름에 주차 번호 대신 키워드가 있는 경우)
KEYWORD_TO_WEEK = {
    "workstation": "1",
    "infra": "1",
    "python": "2",
    "first_python": "2",
    "quiz": "2",
    "quiz_game": "2",
    "npu": "3",
    "python_with_npu": "3",
    "mini_npu": "3",
    "docker": "1",  # 1주차 Docker 실습
    "curriculum": "1",
    "scripts": "1",
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


def get_repo_tree(username: str, repo: str) -> list:
    """레포 전체 파일 트리 조회 (코드 구조 파악용)."""
    url = f"https://api.github.com/repos/{username}/{repo}/git/trees/main?recursive=1"
    try:
        r = requests.get(url, headers=github_headers(), timeout=15)
        if r.status_code != 200:
            return []
        return [item["path"] for item in r.json().get("tree", []) if item["type"] == "blob"]
    except Exception:
        return []


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
    """레포 이름에서 주차 번호를 추출한다. 유효하지 않은 주차명은 키워드 매핑으로 보정."""
    for pattern in patterns:
        m = re.search(pattern, name, re.IGNORECASE)
        if m:
            if m.lastindex and m.lastindex >= 1:
                val = m.group(1).lower()
                resolved = WORD_TO_NUM.get(val, val.lstrip("0") or "0")
                # 숫자인지 확인
                if resolved.isdigit() and int(resolved) in VALID_WEEK_RANGE:
                    return resolved
                # 숫자가 아닌 키워드면 매핑 시도
                if resolved in KEYWORD_TO_WEEK:
                    return KEYWORD_TO_WEEK[resolved]
                # 키워드 매핑에도 없으면 레포 이름 전체에서 키워드 매핑 시도
                for kw, wk in KEYWORD_TO_WEEK.items():
                    if kw in name.lower():
                        return wk
                continue
            else:
                # 캡처 그룹 없는 패턴 — 레포 이름에서 키워드 매핑 시도
                for kw, wk in KEYWORD_TO_WEEK.items():
                    if kw in name.lower():
                        return wk
                # 그래도 없으면 숫자 추출
                nums = re.findall(r'(\d+)', name)
                if nums:
                    val = nums[-1].lstrip("0") or "0"
                    if val.isdigit() and int(val) in VALID_WEEK_RANGE:
                        return val
                continue
    return None


# ─── AI 요약 ──────────────────────────────────────────────────────────────────

def init_genai():
    """Gemini API 클라이언트 초기화. 한 번만 호출."""
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        return None
    if USE_NEW_GENAI:
        return genai.Client(api_key=api_key)
    else:
        genai.configure(api_key=api_key)
        return "legacy"


def call_genai(client, prompt: str) -> str:
    """Gemini API 호출 (rate limit 대응 포함)."""
    for attempt in range(3):
        try:
            if USE_NEW_GENAI and client != "legacy":
                resp = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=prompt,
                )
                return resp.text.strip()
            else:
                model = genai.GenerativeModel("gemini-2.5-flash-lite")
                resp = model.generate_content(prompt)
                return resp.text.strip()
        except Exception as e:
            err_str = str(e).lower()
            if "429" in err_str or "rate" in err_str or "quota" in err_str:
                wait = 15 * (attempt + 1)
                print(f"  [대기] Rate limit — {wait}초 후 재시도 ({attempt+1}/3)")
                time.sleep(wait)
            else:
                print(f"  [오류] AI 호출 실패: {e}")
                return ""
    return ""


def summarize_week(client, readmes: list[dict], week: str) -> str:
    """
    같은 주차의 여러 수강생 README를 종합하여 학습 문서를 생성한다.
    readmes: [{"username": ..., "readme": ..., "repo_url": ..., "file_tree": [...]}]
    """
    if not client:
        # API 키 없으면 가장 긴 README 원문 반환
        best = max(readmes, key=lambda r: len(r["readme"]))
        return best["readme"][:2000] + "\n\n_*(API 키 없음 — 원문 일부)*_"

    # 여러 README를 합쳐서 프롬프트 구성 (최대 3명, 가장 긴 순)
    sorted_readmes = sorted(readmes, key=lambda r: len(r["readme"]), reverse=True)
    selected = sorted_readmes[:3]

    combined_sources = ""
    for i, r in enumerate(selected, 1):
        readme_text = r["readme"][:4000]
        tree_text = "\n".join(r.get("file_tree", [])[:30]) if r.get("file_tree") else "(파일 트리 없음)"
        combined_sources += f"""
---
### 수강생 {i}: {r['username']}
레포: {r['repo_url']}

**파일 구조:**
```
{tree_text}
```

**README 내용:**
{readme_text}
---
"""

    prompt = f"""당신은 AI/SW 교육 과정의 학습 자료를 정리하는 전문가입니다.
아래는 Codyssey 프로그램 {week}주차 과제에 대한 여러 수강생의 GitHub 레포 정보입니다.
이 정보들을 종합하여 **학습자가 이 주차 과제를 완벽히 이해하고 내재화할 수 있는 학습 문서**를 작성해 주세요.

다음 형식을 반드시 지켜주세요:

## 1. 미션 개요
이 주차 과제의 목적과 배경을 2~3문장으로 설명하세요. 왜 이 과제를 하는지, 실무에서 어떤 의미가 있는지 포함하세요.

## 2. 학습 목표
이 과제를 완료하면 설명할 수 있어야 하는 핵심 개념 5가지를 작성하세요.

## 3. 기능 요구사항
과제에서 구현/수행해야 하는 항목을 체크리스트 형태로 정리하세요.
필수 항목과 보너스 항목을 구분하세요 (구분 가능한 경우).

## 4. 핵심 기술 스택
| 기술 | 용도 | 핵심 명령어/개념 |
형태의 표로 정리하세요.

## 5. 권장 프로젝트 구조
수강생들의 실제 파일 구조를 참고하여 이상적인 프로젝트 구조를 제시하세요.
```text
프로젝트/
├── ...
```

## 6. 구현 핵심 포인트
과제를 수행할 때 반드시 알아야 할 핵심 구현 사항 3~5가지를 설명하세요.
각 포인트마다 왜 중요한지, 어떻게 접근해야 하는지 포함하세요.

## 7. 트러블슈팅 & 팁
수강생들의 README에서 발견된 트러블슈팅 사례, 주의사항, 실습 팁을 정리하세요.
실제 에러 메시지나 해결 과정이 있으면 포함하세요.

## 8. 추가 학습 자료
이 주차 과제를 더 깊이 이해하기 위해 참고할 만한 개념, 키워드, 공식 문서 링크를 제시하세요.

---
수강생 레포 정보:
{combined_sources}
---

중요 지침:
- 한국어로 작성하세요.
- 수강생 개인의 답안을 그대로 복사하지 말고, 여러 수강생의 정보를 종합하여 정리하세요.
- 실제 과제 PDF에 나올 법한 체계적이고 전문적인 문서를 작성하세요.
- 코드 블록, 표, 체크리스트 등 마크다운 서식을 적극 활용하세요.
- 트러블슈팅이나 팁이 README에 없으면 일반적으로 자주 발생하는 이슈를 추가하세요.
"""

    result = call_genai(client, prompt)
    if not result:
        best = max(readmes, key=lambda r: len(r["readme"]))
        return best["readme"][:2000] + "\n\n_*(AI 요약 실패 — 원문 일부)*_"
    return result


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
        if not week.isdigit() or int(week) not in VALID_WEEK_RANGE:
            continue
        print(f"  → 폴더 {folder} ({week}주차)")

        readme = get_readme(username, repo_name, folder)
        file_tree = get_repo_tree(username, repo_name)
        # 해당 폴더의 파일만 필터
        folder_tree = [f for f in file_tree if f.startswith(folder + "/")]

        results.append({
            "username": username,
            "display_name": c["display_name"],
            "repo_name": f"{repo_name}/{folder}",
            "repo_url": f"https://github.com/{username}/{repo_name}/tree/main/{folder}",
            "week": week,
            "updated_at": repo_info.get("updated_at", "")[:10],
            "readme_length": len(readme),
            "readme": readme,
            "file_tree": folder_tree,
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
        file_tree = get_repo_tree(username, name)

        results.append({
            "username": username,
            "display_name": c["display_name"],
            "repo_name": name,
            "repo_url": repo.get("html_url", f"https://github.com/{username}/{name}"),
            "week": week,
            "updated_at": updated,
            "readme_length": len(readme),
            "readme": readme,
            "file_tree": file_tree,
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

def make_report(assignments: list, now: datetime, genai_client) -> str:
    date_str = now.strftime("%Y년 %m월 %d일")
    active_count = sum(1 for c in CANDIDATES if c.get("active", True))

    lines = [
        "# Codyssey 주간 학습 자료",
        "",
        f"> **수집 일시**: {date_str} {now.strftime('%H:%M')} KST  ",
        f"> **추적 후보**: {active_count}명  ",
        f"> **수집 레포**: {len(assignments)}건",
        "",
        "이 문서는 Codyssey 프로그램 수강생들의 공개 GitHub 레포를 자동 수집하여,",
        "주차별 과제 내용을 학습 자료 형태로 정리한 것입니다.",
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

    # 목차 생성
    lines.append("## 목차")
    lines.append("")
    for week in sorted(by_week.keys(), key=lambda x: int(x) if x.isdigit() else 99):
        count = len(by_week[week])
        lines.append(f"- [{week}주차 과제](#week-{week}) ({count}명 제출)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 주차별 학습 문서 생성
    for week in sorted(by_week.keys(), key=lambda x: int(x) if x.isdigit() else 99):
        items = by_week[week]
        print(f"\n{'='*60}")
        print(f"  {week}주차 학습 문서 생성 중 ({len(items)}명 레포 종합)...")
        print(f"{'='*60}")

        # README가 있는 항목만 필터
        readmes_for_ai = [
            {
                "username": a["display_name"],
                "readme": a["readme"],
                "repo_url": a["repo_url"],
                "file_tree": a.get("file_tree", []),
            }
            for a in items if a["readme"]
        ]

        # AI 종합 요약 생성
        if readmes_for_ai:
            summary = summarize_week(genai_client, readmes_for_ai, week)
        else:
            summary = "_이 주차에 README가 작성된 레포가 없습니다._"

        lines += [
            f'<a id="week-{week}"></a>',
            f"## {week}주차 과제",
            "",
            summary,
            "",
            "---",
            "",
            f"### 참고 레포 목록 ({len(items)}명)",
            "",
            "| 수강생 | 레포 | 최종 업데이트 | README 분량 | 파일 수 |",
            "|--------|------|:------------:|:-----------:|:-------:|",
        ]
        for a in sorted(items, key=lambda x: (-x["readme_length"], x["priority"])):
            length = f"{a['readme_length']:,}자" if a["readme_length"] > 0 else "없음"
            file_count = len(a.get("file_tree", []))
            lines.append(
                f"| {a['display_name']} | [{a['repo_name']}]({a['repo_url']}) | {a['updated_at']} | {length} | {file_count}개 |"
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

    # Gemini API 초기화
    genai_client = init_genai()
    if genai_client:
        print("✅ Gemini API 연결 성공")
    else:
        print("⚠️  GEMINI_API_KEY 없음 — README 원문으로 대체합니다")

    # 수집
    assignments = collect()

    # 보고서 생성
    os.makedirs("reports", exist_ok=True)
    report = make_report(assignments, now, genai_client)

    dated_path = f"reports/{now.strftime('%Y-%m-%d')}.md"
    with open(dated_path, "w", encoding="utf-8") as f:
        f.write(report)

    with open("reports/latest.md", "w", encoding="utf-8") as f:
        f.write(report)

    # JSON 저장 (readme 원문은 제외하여 용량 절약)
    json_data = []
    for a in assignments:
        entry = {k: v for k, v in a.items() if k not in ("readme", "file_tree")}
        entry["file_count"] = len(a.get("file_tree", []))
        json_data.append(entry)

    with open(f"reports/{now.strftime('%Y-%m-%d')}.json", "w", encoding="utf-8") as f:
        json.dump(
            {"collected_at": now.isoformat(), "assignments": json_data},
            f, ensure_ascii=False, indent=2,
        )

    print(f"\n완료! 총 {len(assignments)}건 수집 → {dated_path}")


if __name__ == "__main__":
    main()
