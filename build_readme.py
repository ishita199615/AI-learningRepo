"""Generate README.md from resources.yml.

    python scripts/build_readme.py
    python scripts/build_readme.py --check   # fail if README is stale

The README is a build artifact. Editing it by hand means your change is lost
the next time this runs, which is why CI regenerates and compares.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "resources.yml"
TARGET = ROOT / "README.md"

MARKER = "<!-- generated from resources.yml — do not edit by hand -->"

# How each status is shown, and whether it counts as personally vetted.
STATUS = {
    "daily-driver":        ("daily driver", True),
    "completed":           ("completed", True),
    "in-progress":         ("in progress", True),
    "partially-completed": ("partly done", True),
    "reviewed":            ("reviewed", True),
    "reference":           ("reference", True),
    "to-review":           ("not yet reviewed", False),
}

COST = {"free": "free", "freemium": "free tier", "paid": "paid"}


def slug(text: str) -> str:
    keep = [c.lower() if c.isalnum() else "-" for c in text]
    out = "".join(keep)
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")


def clean(text: str | None) -> str:
    """YAML folded scalars arrive with trailing newlines and soft wraps."""
    if not text:
        return ""
    return " ".join(str(text).split())


def render(data: dict) -> str:
    meta = data["meta"]
    cats = data["categories"]

    items = [i for c in cats for i in c["items"]]
    vetted = sum(1 for i in items if STATUS.get(i.get("status", ""), ("", False))[1])
    tags = Counter(t for i in items for t in i.get("tags", []))

    out: list[str] = [
        MARKER,
        "",
        f"# {meta['title']}",
        "",
        f"**{meta['tagline']}**",
        "",
        f"![resources](https://img.shields.io/badge/resources-{len(items)}-blue) "
        f"![vetted](https://img.shields.io/badge/personally%20vetted-{vetted}-green) "
        "![license](https://img.shields.io/badge/license-MIT-lightgrey)",
        "",
        clean(meta.get("intro", "")).replace(" Entries live", "\n\nEntries live"),
        "",
        "---",
        "",
        "## Contents",
        "",
    ]

    for c in cats:
        out.append(f"- [{c['title']}](#{slug(c['title'])}) — {len(c['items'])} entries")
    out += ["- [How to read this](#how-to-read-this)", "", "---", ""]

    for c in cats:
        out += [f"## {c['title']}", "", f"*{c['blurb']}*", ""]
        for item in c["items"]:
            label, _ = STATUS.get(item.get("status", ""), ("unknown", False))
            cost = COST.get(item.get("cost", ""), item.get("cost", ""))

            out.append(f"### [{item['name']}]({item['url']})")
            out.append("")
            facts = [
                f"**{item.get('by', '')}**",
                cost,
                item.get("level", ""),
                item.get("time", ""),
                item.get("format", ""),
            ]
            out.append(" · ".join(f for f in facts if f))
            out.append("")
            if item.get("note"):
                out.append(clean(item["note"]))
                out.append("")
            out.append(f"`{label}`" + (
                "  ·  " + " ".join(f"`{t}`" for t in item.get("tags", []))
                if item.get("tags") else ""))
            out.append("")
        out += ["---", ""]

    out += [
        "## How to read this",
        "",
        "**Status** tells you how much weight to give my opinion:",
        "",
        "| Status | Means |",
        "|---|---|",
        "| `daily driver` | I use this regularly |",
        "| `completed` | I finished it |",
        "| `in progress` | I'm working through it now |",
        "| `partly done` | I did some of it |",
        "| `reviewed` | I've used or read enough to judge it |",
        "| `reference` | I reopen it rather than read it through |",
        "| `not yet reviewed` | On my list — included for completeness, not endorsed |",
        "",
        "**Time estimates are realistic, not promotional.** If a course says "
        "\"6 hours\" and actually takes 20 once you run the code, the number here "
        "is 20.",
        "",
        f"**Most common tags:** "
        + ", ".join(f"`{t}` ({n})" for t, n in tags.most_common(8)),
        "",
        "---",
        "",
        "## Contributing",
        "",
        "Edit `resources.yml`, not this file. See "
        "[CONTRIBUTING.md](CONTRIBUTING.md).",
        "",
        "Links are checked weekly by CI. If one rots, an issue opens automatically.",
        "",
        "## License",
        "",
        "MIT. Curation is opinion, not endorsement — check licences on the "
        "linked projects themselves.",
        "",
        f"Maintained by [{meta['author']}](https://github.com/{meta['handle']}).",
        "",
    ]

    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if README.md is out of date")
    args = ap.parse_args()

    data = yaml.safe_load(SOURCE.read_text())
    rendered = render(data)

    if args.check:
        current = TARGET.read_text() if TARGET.exists() else ""
        if current.strip() != rendered.strip():
            print("README.md is stale. Run: python scripts/build_readme.py")
            return 1
        print("README.md is up to date.")
        return 0

    TARGET.write_text(rendered)
    n = sum(len(c["items"]) for c in data["categories"])
    print(f"wrote {TARGET.relative_to(ROOT)}  ({n} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
