"""Check that every URL in markdown files under a directory resolves.

Usage:
    python tools/check_links.py roadmaps/
    python tools/check_links.py roadmaps/fde/roadmap.md

Exit code 0 if all links are OK, 1 if any are dead.
"""

import re
import sys
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

URL_PATTERN = re.compile(r"https?://[^\s\)\]>\"']+")
TIMEOUT = 15
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
# Sites that block bots with 403/429 but work fine in a browser.
SKIP_STATUS = {403, 405, 429, 999}


def collect_urls(target: Path) -> dict[str, list[str]]:
    """Map each URL to the files it appears in."""
    files = [target] if target.is_file() else sorted(target.rglob("*.md"))
    urls: dict[str, list[str]] = {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        for match in URL_PATTERN.findall(text):
            url = match.rstrip(".,;:")
            urls.setdefault(url, []).append(str(f))
    return urls


def check(url: str) -> tuple[str, str]:
    """Return (status, detail) for a URL: ok / warn / dead."""
    req = urllib.request.Request(url, headers=HEADERS, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return ("ok", str(resp.status))
    except urllib.error.HTTPError as e:
        if e.code in SKIP_STATUS:
            return ("warn", f"{e.code} (likely bot-blocking, verify manually)")
        return ("dead", str(e.code))
    except Exception as e:
        return ("warn", f"{type(e).__name__}: {e}")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    target = Path(sys.argv[1])
    if not target.exists():
        print(f"Path not found: {target}")
        return 2

    urls = collect_urls(target)
    print(f"Checking {len(urls)} unique URLs...\n")

    dead, warned = [], []
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = dict(zip(urls, pool.map(check, urls)))

    for url, (status, detail) in sorted(results.items()):
        if status == "dead":
            dead.append((url, detail))
        elif status == "warn":
            warned.append((url, detail))

    for url, detail in warned:
        print(f"WARN  {detail:<45} {url}")
        for f in urls[url]:
            print(f"      in {f}")
    for url, detail in dead:
        print(f"DEAD  {detail:<45} {url}")
        for f in urls[url]:
            print(f"      in {f}")

    ok = len(urls) - len(dead) - len(warned)
    print(f"\n{ok} ok, {len(warned)} warnings, {len(dead)} dead")
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
