from __future__ import annotations

import re
from urllib.parse import urlparse

EXTERNAL_LINK_ALLOWED_DOMAINS = [
    "velog.io",
    "tistory.com",
    "github.io",
    "notion.so",
    "notion.site",
    "youtube.com",
    "youtu.be",
    "codyssey.kr",
    "codysseycampus.kr",
]

EXTERNAL_LINK_PATTERN = re.compile(r"https?://[^\s<>()\"']+")


def classify_external_link(url: str) -> str | None:
    try:
        host = (urlparse(url).netloc or "").lower()
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
    found = []
    seen = set()
    for m in EXTERNAL_LINK_PATTERN.findall(text):
        url = m.rstrip(".,);]>")
        domain = classify_external_link(url)
        if not domain:
            continue
        if url in seen:
            continue
        seen.add(url)
        found.append({
            "url": url,
            "domain": domain,
        })
    return found


def collect_external_links_from_item(item: dict) -> list[dict]:
    external_links = []
    seen = set()

    readme = item.get("readme", "") or ""
    repo_name = item.get("repo_name", "") or ""

    for link in extract_external_links_from_text(readme):
        if link["url"] in seen:
            continue
        seen.add(link["url"])
        external_links.append({
            "url": link["url"],
            "domain": link["domain"],
            "source_type": "readme",
            "source_path": "README.md" if "/" not in repo_name else f"{repo_name.split('/',1)[1]}/README.md",
        })

    for art in item.get("artifacts", []) or []:
        content = art.get("content", "") or ""
        path = art.get("path", "") or ""
        for link in extract_external_links_from_text(content):
            if link["url"] in seen:
                continue
            seen.add(link["url"])
            external_links.append({
                "url": link["url"],
                "domain": link["domain"],
                "source_type": "artifact",
                "source_path": path,
            })

    return external_links