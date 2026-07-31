"""Check that every URL in resources.yml still resolves.

    python scripts/check_links.py

Exits non-zero if anything is dead, so CI can open an issue. Link rot is what
kills curated lists — a list with three dead links stops being trusted.
"""

from __future__ import annotations

import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "resources.yml"
TIMEOUT = 20

# Plenty of sites reject the default urllib agent with a 403.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ai-learning-path link checker)",
    "Accept": "text/html,application/xhtml+xml,*/*",
}


def check(entry: tuple[str, str]) -> tuple[str, str, int | str]:
    name, url = entry
    req = urllib.request.Request(url, headers=HEADERS, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return name, url, resp.status
    except urllib.error.HTTPError as exc:
        # 403 and 429 usually mean bot protection, not a dead link.
        return name, url, exc.code
    except Exception as exc:  # DNS failure, timeout, bad TLS
        return name, url, type(exc).__name__


def main() -> int:
    data = yaml.safe_load(SOURCE.read_text())
    entries = [(i["name"], i["url"])
               for c in data["categories"] for i in c["items"]]

    print(f"checking {len(entries)} links\n")

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check, entries))

    ok, soft, dead = [], [], []
    for name, url, status in results:
        if status == 200:
            ok.append((name, url, status))
        elif status in (403, 429):
            soft.append((name, url, status))
        else:
            dead.append((name, url, status))

    for name, url, status in sorted(soft, key=lambda r: r[0]):
        print(f"  BLOCKED  {status}  {name}  -> {url}")
    for name, url, status in sorted(dead, key=lambda r: r[0]):
        print(f"  DEAD     {status}  {name}  -> {url}")

    print(f"\n{len(ok)} ok, {len(soft)} blocked by bot protection, {len(dead)} dead")

    if dead:
        print("\nFailing: fix or remove the dead links above.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
