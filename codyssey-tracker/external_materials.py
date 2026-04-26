from __future__ import annotations

import re
from urllib.parse import urlparse


EXTERNAL_LINK_ALLOWED_DOMAINS = [
    "velog.io",
    "tistory.com",
    "github.io",
    "github.com",
    "gist.github.com",
    "notion.so",
    "notion.site",
    "youtube.com",
    "youtu.be",
    "blog.naver.com",
    "brunch.co.kr",
    "medium.com",
    "codyssey.kr",
    "codysseycampus.kr",
]

EXTERNAL_LINK_PATTERN = re.compile(r"https?://[^\s<>()\"']+")


def normalize_external_url(url: str) -> str | None:
    try:
        parsed = urlparse((url or "").strip())
    except Exception:
        return None

    scheme = (parsed.scheme or "").lower()
    host = (parsed.netloc or "").lower()
    path = (parsed.path or "").strip()

    if scheme not in {"http", "https"}:
        return None
    if not host:
        return None

    path = path.rstrip("/")
    if path.endswith(".git"):
        path = path[:-4]

    raw = f"{host}{path}"
    bad_tokens = ["???", "�", "<", ">", "{", "}"]
    if any(tok in raw for tok in bad_tokens):
        return None

    if host == "github.com":
        parts = [p for p in path.split("/") if p]
        if len(parts) == 0:
            return None
        if len(parts) > 2:
            parts = parts[:2]
        path = "/" + "/".join(parts)

    elif host == "gist.github.com":
        parts = [p for p in path.split("/") if p]
        if len(parts) == 0:
            return None
        path = "/" + parts[0]

    return f"https://{host}{path}"


def classify_external_link(url: str) -> str | None:
    normalized = normalize_external_url(url)
    if not normalized:
        return None

    try:
        host = (urlparse(normalized).netloc or "").lower()
    except Exception:
        return None

    if not host:
        return None

    for domain in EXTERNAL_LINK_ALLOWED_DOMAINS:
        if host == domain or host.endswith("." + domain):
            return domain
    return None


def extract_external_links_from_text(text: str) -> list[dict]:
    if not text:
        return []

    found: list[dict] = []
    seen: set[str] = set()

    for m in EXTERNAL_LINK_PATTERN.findall(text):
        normalized = normalize_external_url(m.rstrip(".,);]>"))
        if not normalized:
            continue

        domain = classify_external_link(normalized)
        if not domain:
            continue

        if normalized in seen:
            continue

        seen.add(normalized)
        found.append({
            "url": normalized,
            "domain": domain,
        })

    return found


def collect_external_links_from_item(item: dict) -> list[dict]:
    external_links: list[dict] = []
    seen: set[str] = set()

    readme = item.get("readme", "") or ""
    repo_name = item.get("repo_name", "") or ""
    username = item.get("username", "") or ""

    def add_link(url: str, domain: str, source_type: str, source_path: str) -> None:
        if url in seen:
            return
        seen.add(url)
        external_links.append({
            "url": url,
            "domain": domain,
            "source_type": source_type,
            "source_path": source_path,
        })

    for link in extract_external_links_from_text(readme):
        add_link(
            url=link["url"],
            domain=link["domain"],
            source_type="readme",
            source_path="README.md" if "/" not in repo_name else f"{repo_name.split('/', 1)[1]}/README.md",
        )

    for art in item.get("artifacts", []) or []:
        content = art.get("content", "") or ""
        path = art.get("path", "") or ""
        for link in extract_external_links_from_text(content):
            add_link(
                url=link["url"],
                domain=link["domain"],
                source_type="artifact",
                source_path=path,
            )

    if username:
        profile_url = f"https://github.com/{username}"
        add_link(
            url=profile_url,
            domain="github.com",
            source_type="profile",
            source_path="github-profile",
        )

        gist_url = f"https://gist.github.com/{username}"
        add_link(
            url=gist_url,
            domain="gist.github.com",
            source_type="gist-profile",
            source_path="github-gist-profile",
        )

    return external_links
