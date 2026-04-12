#!/usr/bin/env python3
"""
Codyssey 과제 자동 수집기 (2026 본과정 전용)
GitHub Actions에서 매주 일요일 오후 9시(KST)에 실행됩니다.
과정 기간: 2026년 3월 30일 ~ 2027년 9월 30일

v7: 2026 본과정(입학연수) 커리큘럼 전면 재세팅
    - 2025 파일럿 지문(mars_mission 등) 제거 및 2026 지문(quiz_game, npu_simulator 등) 추가
    - 2026 커리큘럼 기반 주차 판정 로직 수정 (1:워크스테이션, 2:퀴즈, 3:NPU)
    - 후보 45명 중 2026 본과정 수강생 17명 + 잠재적 후보 18명 집중 추적
    - 중복 수강생(leehnmn, peachily, I-nkamanda)은 2026 레포만 추적하도록 고정
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

# ─── 추가 자료 수집 설정 ─────────────────────────────────────────────────────

# 수집 대상 파일 패턴 (README 외)
ARTIFACT_PATTERNS = {
    "학습노트": [
        r".*(?:study|학습|정리|note|memo|summary).*\.md$",
        r".*(?:command[_\-]?log|troubleshoot).*\.md$",
        r".*(?:insight|discussion|guideline|checklist).*\.md$",
    ],
    "분석보고서": [
        r".*(?:log_analysis|report|분석).*\.md$",
        r".*(?:eval\d*|review|assessment).*\.md$",
    ],
    "인프라설정": [
        r"(?:.*/)?[Dd]ockerfile(?:\.\w+)?$",
        r"(?:.*/)?docker[_\-]?compose\.ya?ml$",
        r"(?:.*/)?\.?[Dd]ockerfile$",
    ],
    "설정파일": [
        r"(?:.*/)?(?:k8s|kubernetes|deploy|service|pod).*\.ya?ml$",
        r"(?:.*/)?(?:nginx|apache|config).*\.(?:conf|ya?ml)$",
    ],
    "과제명세": [
        r".*\.pdf$",
    ],
    "마크다운": [
        r".*\.md$",  # 위 카테고리에 안 잡힌 나머지 md
    ],
}

# 수집 제외 패턴
ARTIFACT_EXCLUDE = [
    r"(?:^|/)README\.md$",
    r"(?:^|/)\.github/",
    r"(?:^|/)node_modules/",
    r"(?:^|/)__pycache__/",
    r"(?:^|/)\.git/",
    r"(?:^|/)venv/",
    r"(?:^|/)\.vscode/",
]

# ─── 2026 본과정 지문(Fingerprint) 설정 ──────────────────────────────────────

# Tier 1: 이 파일이 하나라도 있으면 2026 본과정 과제 레포 확정 (score 10)
FINGERPRINT_TIER1 = [
    "quiz_game.py",
    "npu_simulator.py",
    "mini_npu_simulator.py",
    "data.json",          # 2주차 퀴즈 게임 데이터
    "questions.json",     # 2주차 퀴즈 질문
    "inventory.json",     # 1주차 또는 2주차 데이터
    "mac_operation.py",   # 3주차 NPU 연산
]

# Tier 2: 2개 이상 조합이면 확정 (score 5 each)
FINGERPRINT_TIER2 = [
    "main.py",
    "state.json",
    "utils.py",
    "requirements.txt",
    "Dockerfile",
]

# Tier 3: README 키워드 (score 3 each)
FINGERPRINT_KEYWORDS = [
    "codyssey", "코디세이", "입학연수", "워크스테이션",
    "퀴즈 게임", "quiz game", "npu simulator", "npu 시뮬레이터",
    "mac 연산", "matrix multiplication",
]

# 지문 확정 임계값
FINGERPRINT_THRESHOLD = 10

# ─── 추적할 후보 수강생 목록 (2026 본과정 중심) ──────────────────────────────────

CANDIDATES = [
    # ══════════════════════════════════════════════════════════════════════
    # ── 2026 본과정 확정 후보 (17명) ──
    # ══════════════════════════════════════════════════════════════════════
    {"username": "kimch0612", "display_name": "kimch0612", "type": "multi_repo", "repo_patterns": [r"[Cc]odyssey[_\-]?[Ww]eek[_\-]?(\d+)"], "priority": 1},
    {"username": "sonjehyun123-maker", "display_name": "sonjehyun123-maker", "type": "multi_repo", "repo_patterns": [r"[Cc]odyssey[_\-]?w\d+[_\-]?[Ee](\d+)"], "priority": 1},
    {"username": "mulloc1", "display_name": "mulloc1", "type": "multi_repo", "repo_patterns": [r"codyssey[_\-]?(?:workstation|first_python|python_with_npu)"], "priority": 1},
    {"username": "ntt65", "display_name": "ntt65", "type": "single_repo", "repo_name": "codyssey", "folder_pattern": r"(?:e1_(\d+)|week(\d+))", "priority": 1},
    {"username": "codewhite7777", "display_name": "codewhite7777", "type": "multi_repo", "repo_patterns": [r"codyssey[_\-]?[Ee][_\-]?(\d+)", r"codyssey[_\-]?[Ee]\d+[_\-](\d+)"], "priority": 1},
    {"username": "mov-hyun", "display_name": "mov-hyun", "type": "multi_repo", "repo_patterns": [r"e1[_\-](\d+)", r"quiz[_\-]?game"], "priority": 1},
    {"username": "yeowon083", "display_name": "yeowon083", "type": "multi_repo", "repo_patterns": [r"quiz[_\-]?game"], "priority": 1},
    {"username": "Kingsong97", "display_name": "Kingsong97", "type": "multi_repo", "repo_patterns": [r"codyssey[_\-]?[Ee]\d+[_\-](\d+)"], "priority": 2},
    {"username": "jonghwan159", "display_name": "jonghwan159", "type": "single_repo", "repo_name": "Codyssey", "folder_pattern": r"과정[_\-](\d+)", "priority": 1},
    {"username": "jhkr1", "display_name": "jhkr1", "type": "multi_repo", "repo_patterns": [r"[Cc]odyssey[_\-]?mission[_\-]?(\d+)"], "priority": 1},
    {"username": "junhnno", "display_name": "junhnno", "type": "multi_repo", "repo_patterns": [r"[Cc]odyssey[_\-]?[Ww]ork[Ss]pace[_\-]?[Ww]eek[_\-]?(\d+)"], "priority": 1},
    {"username": "sungho255", "display_name": "sungho255", "type": "multi_repo", "repo_patterns": [r"codyssey[_\-]?(\d+)"], "priority": 1},
    {"username": "yejoo0310", "display_name": "yejoo0310", "type": "multi_repo", "repo_patterns": [r"codyssey[_\-]?[Mm][_\-]?(\d+)"], "priority": 1},
    {"username": "yejibaek12", "display_name": "yejibaek12", "type": "multi_repo", "repo_patterns": [r"[Pp]ython[_\-]?[Qq]uiz[_\-]?[Gg]ame"], "priority": 1},
    {"username": "clae-dev", "display_name": "clae-dev", "type": "multi_repo", "repo_patterns": [r"ia[_\-]codyssey[_\-]?(?:Python|Docker)"], "priority": 1},
    {"username": "yjchoi-95", "display_name": "yjchoi-95", "type": "multi_repo", "repo_patterns": [r"claude[_\-]code"], "priority": 1},
    {"username": "leehnmn", "display_name": "leehnmn", "type": "single_repo", "repo_name": "codyssey_2026", "folder_pattern": r"project[_\-]?(\d+)", "priority": 1},
    
    # ══════════════════════════════════════════════════════════════════════
    # ── 중복/기타 2026 레포 명시적 추적 ──
    # ══════════════════════════════════════════════════════════════════════
    {"username": "peachily", "display_name": "peachily", "type": "multi_repo", "repo_patterns": [r"codyssey11[_\-]?[Ee](\d+)"], "priority": 2},
    {"username": "I-nkamanda", "display_name": "I-nkamanda", "type": "single_repo", "repo_name": "codyssey2026", "folder_pattern": r"[Pp]roblem[_\-]?(\d+)", "priority": 1},

    # ══════════════════════════════════════════════════════════════════════
    # ── 판별 불가 / 잠재적 후보 (18명) ──
    # ══════════════════════════════════════════════════════════════════════
    {"username": "Ahn-Jeongmin", "display_name": "Ahn-Jeongmin", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "Jeonghui96", "display_name": "Jeonghui96", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "Seoyeon-Baek", "display_name": "Seoyeon-Baek", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "HyeonJeong519", "display_name": "HyeonJeong519", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "LeeJeongHwi", "display_name": "LeeJeongHwi", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "Yun024", "display_name": "Yun024", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "ikasoon", "display_name": "ikasoon", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "doji-kr", "display_name": "doji-kr", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "Jeon-Yoojin", "display_name": "Jeon-Yoojin", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "seongjin-an", "display_name": "seongjin-an", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "Eomhyein", "display_name": "Eomhyein", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "Jeongseonil", "display_name": "Jeongseonil", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "seokhwan-an", "display_name": "seokhwan-an", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "kimmjen", "display_name": "kimmjen", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "KIMJW04", "display_name": "KIMJW04", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "dev-9hee", "display_name": "dev-9hee", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "YunDaeHyeon", "display_name": "YunDaeHyeon", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
    {"username": "leesanghyeok523", "display_name": "leesanghyeok523", "type": "multi_repo", "repo_patterns": [r"codyssey.*(\d+)"], "priority": 3},
]

WORD_TO_NUM = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
}

# 2026 본과정 주차 키워드 매핑
KEYWORD_TO_WEEK = {
    "workstation": "1",
    "infra": "1",
    "docker": "1",
    "terminal": "1",
    "python": "2",
    "first_python": "2",
    "quiz": "2",
    "quiz_game": "2",
    "npu": "3",
    "python_with_npu": "3",
    "mini_npu": "3",
    "npu_simulator": "3",
    "mac": "3",
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

def get_file_content(username: str, repo: str, path: str) -> str:
    url = f"https://api.github.com/repos/{username}/{repo}/contents/{path}"
    try:
        r = requests.get(url, headers=github_headers(), timeout=15)
        if r.status_code != 200:
            return ""
        data = r.json()
        if data.get("size", 0) > 100_000:
            return f"[파일 크기 초과: {data['size']:,}B — 내용 생략]"
        content_b64 = data.get("content", "")
        if not content_b64:
            return ""
        try:
            return base64.b64decode(content_b64).decode("utf-8", errors="replace")
        except Exception:
            return "[바이너리 파일 — 텍스트 변환 불가]"
    except Exception as e:
        print(f"  [오류] {username}/{repo}/{path} 파일 조회 실패: {e}")
        return ""

def get_repo_tree(username: str, repo: str) -> list:
    url = f"https://api.github.com/repos/{username}/{repo}/git/trees/main?recursive=1"
    try:
        r = requests.get(url, headers=github_headers(), timeout=15)
        if r.status_code != 200:
            url2 = url.replace("/main?", "/master?")
            r = requests.get(url2, headers=github_headers(), timeout=15)
            if r.status_code != 200:
                return []
        return [item["path"] for item in r.json().get("tree", []) if item["type"] == "blob"]
    except Exception:
        return []

def get_repo_folders(username: str, repo: str) -> list:
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
            if m.lastindex and m.lastindex >= 1:
                val = m.group(1).lower()
                resolved = WORD_TO_NUM.get(val, val.lstrip("0") or "0")
                if resolved.isdigit() and int(resolved) in VALID_WEEK_RANGE:
                    return resolved
                if resolved in KEYWORD_TO_WEEK:
                    return KEYWORD_TO_WEEK[resolved]
                # 구체적인 키워드 우선 매칭 (글자 수 긴 순서대로)
                sorted_kws = sorted(KEYWORD_TO_WEEK.keys(), key=len, reverse=True)
                for kw in sorted_kws:
                    if kw in name.lower():
                        return KEYWORD_TO_WEEK[kw]
                continue
            else:
                # 구체적인 키워드 우선 매칭 (글자 수 긴 순서대로)
                sorted_kws = sorted(KEYWORD_TO_WEEK.keys(), key=len, reverse=True)
                for kw in sorted_kws:
                    if kw in name.lower():
                        return KEYWORD_TO_WEEK[kw]
                nums = re.findall(r'(\d+)', name)
                if nums:
                    val = nums[-1].lstrip("0") or "0"
                    if val.isdigit() and int(val) in VALID_WEEK_RANGE:
                        return val
                continue
    return None

# ─── 추가 자료 수집 ──────────────────────────────────────────────────────────

def classify_artifact(path: str) -> str | None:
    path_lower = path.lower()
    for excl in ARTIFACT_EXCLUDE:
        if re.search(excl, path, re.IGNORECASE):
            return None
    for category in ["학습노트", "분석보고서", "인프라설정", "설정파일", "과제명세"]:
        for pattern in ARTIFACT_PATTERNS[category]:
            if re.search(pattern, path_lower):
                return category
    if path_lower.endswith(".md"):
        return "마크다운"
    return None

def collect_artifacts(username: str, repo: str, file_tree: list, folder_prefix: str = "") -> list:
    artifacts = []
    candidates = []
    for path in file_tree:
        if folder_prefix and not path.startswith(folder_prefix):
            continue
        category = classify_artifact(path)
        if category:
            candidates.append((category, path))
    priority_order = ["학습노트", "분석보고서", "인프라설정", "설정파일", "과제명세", "마크다운"]
    candidates.sort(key=lambda x: priority_order.index(x[0]) if x[0] in priority_order else 99)
    for category, path in candidates[:10]:
        if category == "과제명세":
            artifacts.append({"type": category, "path": path, "content": f"[PDF 파일: {path}]"})
        else:
            content = get_file_content(username, repo, path)
            if content and len(content) > 10:
                artifacts.append({"type": category, "path": path, "content": content[:3000]})
    return artifacts

# ─── 지문 기반 자동 발견 ──────────────────────────────────────────────────────

def compute_fingerprint_score(file_tree: list, readme: str = "") -> int:
    score = 0
    filenames = {path.split("/")[-1].lower() for path in file_tree}
    for fp in FINGERPRINT_TIER1:
        if fp.lower() in filenames:
            score += 10
            break
    for fp in FINGERPRINT_TIER2:
        if fp.lower() in filenames:
            score += 5
    readme_lower = readme.lower()
    for kw in FINGERPRINT_KEYWORDS:
        if kw.lower() in readme_lower:
            score += 3
    return score

def discover_new_repos(known_users: set) -> list:
    discovered = []
    seen_repos = set()
    search_queries = ["quiz_game.py", "npu_simulator.py", "data.json"]
    for query in search_queries:
        url = "https://api.github.com/search/code"
        params = {"q": f"filename:{query}", "per_page": 30}
        try:
            r = requests.get(url, headers=github_headers(), params=params, timeout=15)
            if r.status_code != 200: continue
            items = r.json().get("items", [])
            for item in items:
                repo_full = item.get("repository", {}).get("full_name", "")
                if not repo_full: continue
                username = repo_full.split("/")[0]
                repo_name = repo_full.split("/")[1] if "/" in repo_full else ""
                if username.lower() in known_users or repo_full in seen_repos: continue
                seen_repos.add(repo_full)
                file_tree = get_repo_tree(username, repo_name)
                readme = get_readme(username, repo_name)
                score = compute_fingerprint_score(file_tree, readme)
                if score >= FINGERPRINT_THRESHOLD:
                    evidence = []
                    filenames = {p.split("/")[-1].lower() for p in file_tree}
                    for fp in FINGERPRINT_TIER1:
                        if fp.lower() in filenames: evidence.append(f"[Tier1] {fp}")
                    for fp in FINGERPRINT_TIER2:
                        if fp.lower() in filenames: evidence.append(f"[Tier2] {fp}")
                    readme_lower = readme.lower()
                    for kw in FINGERPRINT_KEYWORDS:
                        if kw.lower() in readme_lower: evidence.append(f"[키워드] {kw}")
                    discovered.append({
                        "username": username, "repo_name": repo_name,
                        "repo_url": f"https://github.com/{repo_full}",
                        "score": score, "evidence": evidence,
                        "file_count": len(file_tree), "readme_length": len(readme),
                    })
                    print(f"  [지문 발견] {repo_full} (점수: {score})")
        except Exception as e:
            print(f"  [오류] 지문 검색 실패 ({query}): {e}")
        time.sleep(1)
    discovered.sort(key=lambda x: -x["score"])
    return discovered

# ─── AI 요약 ──────────────────────────────────────────────────────────────────

def init_genai():
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key: return None
    if USE_NEW_GENAI: return genai.Client(api_key=api_key)
    else:
        genai.configure(api_key=api_key)
        return "legacy"

def call_genai(client, prompt: str) -> str:
    for attempt in range(3):
        try:
            if USE_NEW_GENAI and client != "legacy":
                resp = client.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt)
                return resp.text.strip()
            else:
                model = genai.GenerativeModel("gemini-2.5-flash-lite")
                resp = model.generate_content(prompt)
                return resp.text.strip()
        except Exception as e:
            err_str = str(e).lower()
            if "429" in err_str or "rate" in err_str or "quota" in err_str:
                wait = 15 * (attempt + 1)
                time.sleep(wait)
            else:
                print(f"  [오류] AI 호출 실패: {e}")
                return ""
    return ""

def summarize_week(client, readmes: list[dict], week: str) -> str:
    if not client:
        best = max(readmes, key=lambda r: len(r["readme"]))
        return best["readme"][:2000] + "\n\n_*(API 키 없음 — 원문 일부)*_"
    sorted_readmes = sorted(readmes, key=lambda r: len(r["readme"]), reverse=True)
    selected = sorted_readmes[:3]
    combined_sources = ""
    for i, r in enumerate(selected, 1):
        readme_text = r["readme"][:4000]
        tree_text = "\n".join(r.get("file_tree", [])[:30])
        artifacts_text = ""
        for art in r.get("artifacts", [])[:5]:
            artifacts_text += f"\n**[{art['type']}] {art['path']}:**\n{art['content'][:1500]}\n"
        combined_sources += f"\n---\n### 수강생 {i}: {r['username']}\n레포: {r['repo_url']}\n**파일 구조:**\n```\n{tree_text}\n```\n**README 내용:**\n{readme_text}\n"
        if artifacts_text: combined_sources += f"**추가 자료:**\n{artifacts_text}\n"
        combined_sources += "---\n"
    prompt = f"""당신은 AI/SW 교육 과정의 학습 자료를 정리하는 전문가입니다.
아래는 Codyssey 프로그램 {week}주차 과제에 대한 여러 수강생의 GitHub 레포 정보입니다.
이 정보들을 종합하여 **학습자가 이 주차 과제를 완벽히 이해하고 내재화할 수 있는 학습 문서**를 작성해 주세요.

형식:
## 1. 미션 개요
## 2. 학습 목표
## 3. 기능 요구사항
## 4. 핵심 기술 스택
## 5. 권장 프로젝트 구조
## 6. 구현 핵심 포인트
## 7. 트러블슈팅 & 팁
## 8. 추가 학습 자료

정보:
{combined_sources}
"""
    try:
        result = call_genai(client, prompt)
        return result if result else max(readmes, key=lambda r: len(r["readme"]))["readme"][:2000]
    except Exception:
        return max(readmes, key=lambda r: len(r["readme"]))["readme"][:2000]

# ─── 수집 ─────────────────────────────────────────────────────────────────────

def collect_single_repo(c: dict) -> list:
    results = []
    username, repo_name, folder_pattern = c["username"], c["repo_name"], c["folder_pattern"]
    print(f"\n[{c['display_name']}] 단일 레포 {repo_name} 스캔 중...")
    repo_info = get_repo_info(username, repo_name)
    if not repo_info: return results
    full_tree = get_repo_tree(username, repo_name)
    folders = get_repo_folders(username, repo_name)
    for folder in folders:
        m = re.search(folder_pattern, folder, re.IGNORECASE)
        if not m: continue
        if m.lastindex and m.lastindex >= 1: week = m.group(1).lstrip("0") or "0"
        else:
            matched_text = m.group(0).lower()
            week = KEYWORD_TO_WEEK.get(matched_text)
            if not week:
                for kw, wk in KEYWORD_TO_WEEK.items():
                    if kw in folder.lower(): week = wk; break
            if not week: continue
        if not week.isdigit() or int(week) not in VALID_WEEK_RANGE: continue
        print(f"  → 폴더 {folder} ({week}주차)")
        readme = get_readme(username, repo_name, folder)
        folder_tree = [f for f in full_tree if f.startswith(folder + "/")]
        artifacts = collect_artifacts(username, repo_name, full_tree, folder + "/")
        results.append({
            "username": username, "display_name": c["display_name"],
            "repo_name": f"{repo_name}/{folder}", "repo_url": f"https://github.com/{username}/{repo_name}/tree/main/{folder}",
            "week": week, "updated_at": repo_info.get("updated_at", "")[:10],
            "readme_length": len(readme), "readme": readme, "file_tree": folder_tree,
            "artifacts": artifacts, "priority": c["priority"],
        })
    return results

def collect_multi_repo(c: dict) -> list:
    results = []
    username = c["username"]
    print(f"\n[{c['display_name']}] 레포 조회 중...")
    for repo in get_user_repos(username):
        name = repo["name"]
        week = detect_week(name, c["repo_patterns"])
        if week is None: continue
        updated = repo.get("updated_at", "")[:10]
        print(f"  → {name} ({week}주차, 업데이트: {updated})")
        readme = get_readme(username, name)
        file_tree = get_repo_tree(username, name)
        artifacts = collect_artifacts(username, name, file_tree)
        results.append({
            "username": username, "display_name": c["display_name"],
            "repo_name": name, "repo_url": repo.get("html_url", f"https://github.com/{username}/{name}"),
            "week": week, "updated_at": updated, "readme_length": len(readme),
            "readme": readme, "file_tree": file_tree, "artifacts": artifacts, "priority": c["priority"],
        })
    return results

def collect() -> list:
    results, seen = [], set()
    for c in CANDIDATES:
        try:
            items = collect_single_repo(c) if c.get("type") == "single_repo" else collect_multi_repo(c)
            for item in items:
                key = f"{item['username']}/{item['repo_name']}"
                if key not in seen: seen.add(key); results.append(item)
        except Exception as e:
            print(f"  [치명적 오류] 후보 {c['username']} 수집 중 에러: {e}")
    return results

# ─── 메인 ─────────────────────────────────────────────────────────────────────

def main():
    print(f"=== Codyssey 주간 과제 수집 시작 ({datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')}) ===")
    start_time = time.time()
    
    # 1. 수집
    all_items = collect()
    print(f"\n총 {len(all_items)}건의 과제 수집 완료")
    
    # 2. 주차별 그룹화
    by_week = {}
    for item in all_items:
        w = item["week"]
        if w not in by_week: by_week[w] = []
        by_week[w].append(item)
    
    # 3. 지문 기반 신규 레포 발견
    known_users = {c["username"].lower() for c in CANDIDATES}
    new_repos = discover_new_repos(known_users)
    
    # 4. AI 요약 및 보고서 생성
    client = init_genai()
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)
    
    date_str = datetime.now(KST).strftime("%Y-%m-%d")
    report_path = os.path.join(report_dir, f"{date_str}.md")
    latest_path = os.path.join(report_dir, "latest.md")
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# Codyssey 주간 과제 수집 보고서 ({date_str})\n\n")
        f.write(f"- 총 수집 건수: {len(all_items)}건\n")
        f.write(f"- 신규 발견 레포: {len(new_repos)}건\n")
        f.write(f"- 소요 시간: {int(time.time() - start_time)}초\n\n")
        
        f.write("## 1. 주차별 학습 문서\n\n")
        for week in sorted(by_week.keys(), key=int):
            print(f"[{week}주차] AI 요약 중...")
            summary = summarize_week(client, by_week[week], week)
            f.write(f"### {week}주차 과제 종합\n\n")
            f.write(summary + "\n\n")
            
            f.write("#### 참여 수강생 및 자료\n")
            f.write("| 수강생 | 레포 | 업데이트 | 추가 자료 |\n")
            f.write("| --- | --- | --- | --- |\n")
            for item in sorted(by_week[week], key=lambda x: x["priority"]):
                art_str = ", ".join(set(a["type"] for a in item["artifacts"])) if item["artifacts"] else "-"
                f.write(f"| {item['display_name']} | [{item['repo_name']}]({item['repo_url']}) | {item['updated_at']} | {art_str} |\n")
            f.write("\n---\n\n")
            
        if new_repos:
            f.write("## 2. 지문 기반 신규 발견 레포\n\n")
            f.write("| 사용자 | 레포 | 점수 | 발견 증거 |\n")
            f.write("| --- | --- | --- | --- |\n")
            for r in new_repos:
                f.write(f"| {r['username']} | [{r['repo_name']}]({r['repo_url']}) | {r['score']} | {', '.join(r['evidence'])} |\n")
            f.write("\n")

    # latest.md로 복사
    with open(report_path, "r", encoding="utf-8") as src, open(latest_path, "w", encoding="utf-8") as dst:
        dst.write(src.read())
        
    print(f"\n보고서 생성 완료: {report_path}")

if __name__ == "__main__":
    main()
