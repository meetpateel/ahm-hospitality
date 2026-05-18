"""
Walks every .html under the repo root, extracts every href/src,
classifies internal vs external, and verifies internal targets exist on disk
plus return 200 against http://localhost:8000.

Usage: python tools/check_links.py
"""
from __future__ import annotations
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

ROOT = Path(__file__).resolve().parent.parent
SERVER = "http://localhost:8000"

ATTR_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
INLINE_URL_RE = re.compile(r"""url\(\s*['"]?([^'")]+)['"]?\s*\)""", re.IGNORECASE)

results: list[tuple[str, int, str, str, str]] = []  # file, line, kind, target, status

def classify(target: str) -> str:
    p = urlparse(target)
    if p.scheme in ("http", "https"):
        return "external"
    if target.startswith("mailto:"):
        return "mailto"
    if target.startswith("tel:"):
        return "tel"
    if target.startswith("#"):
        return "anchor"
    if "[TODO" in target or target.strip() == "":
        return "todo"
    return "internal"

def resolve_internal(html_file: Path, target: str) -> Path:
    target = unquote(target.split("#", 1)[0].split("?", 1)[0])
    base = html_file.parent
    return (base / target).resolve()

def check_server(target: str, html_file: Path) -> str:
    # Build URL relative to server root using the HTML file's relative path
    target = target.split("#", 1)[0].split("?", 1)[0]
    rel_dir = html_file.parent.relative_to(ROOT).as_posix()
    if rel_dir == ".":
        rel_dir = ""
    if target.startswith("/"):
        url = f"{SERVER}{target}"
    else:
        prefix = f"/{rel_dir}/" if rel_dir else "/"
        url = f"{SERVER}{prefix}{target}"
    try:
        with urlopen(url, timeout=5) as resp:
            return f"HTTP {resp.status}"
    except HTTPError as e:
        return f"HTTP {e.code}"
    except URLError as e:
        return f"ERR {e.reason}"

def scan(html_file: Path) -> None:
    text = html_file.read_text(encoding="utf-8", errors="replace")
    for lineno, line in enumerate(text.splitlines(), start=1):
        for m in ATTR_RE.finditer(line):
            target = m.group(1)
            kind = classify(target)
            if kind == "internal":
                disk = resolve_internal(html_file, target)
                if not disk.exists():
                    results.append((str(html_file.relative_to(ROOT)), lineno, "BROKEN-DISK", target, "missing on disk"))
                else:
                    status = check_server(target, html_file)
                    if not status.startswith("HTTP 2") and not status.startswith("HTTP 3"):
                        results.append((str(html_file.relative_to(ROOT)), lineno, "BROKEN-HTTP", target, status))
            elif kind == "todo":
                results.append((str(html_file.relative_to(ROOT)), lineno, "TODO-LINK", target, "placeholder"))
        for m in INLINE_URL_RE.finditer(line):
            target = m.group(1)
            kind = classify(target)
            if kind == "internal":
                disk = resolve_internal(html_file, target)
                if not disk.exists():
                    results.append((str(html_file.relative_to(ROOT)), lineno, "BROKEN-IMG", target, "image missing on disk"))

def main() -> int:
    for html in sorted(ROOT.rglob("*.html")):
        if "tools" in html.parts:
            continue
        scan(html)
    if not results:
        print("OK — no broken or placeholder links found.")
        return 0
    print(f"{len(results)} issue(s):\n")
    by_kind: dict[str, list] = {}
    for r in results:
        by_kind.setdefault(r[2], []).append(r)
    for kind in sorted(by_kind):
        rows = by_kind[kind]
        print(f"--- {kind} ({len(rows)}) ---")
        for f, ln, _, tgt, status in rows:
            print(f"  {f}:{ln}  {tgt!r}  [{status}]")
        print()
    return 1 if any(k.startswith("BROKEN") for k in by_kind) else 0

if __name__ == "__main__":
    sys.exit(main())
