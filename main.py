#!/usr/bin/env python3
"""從 Markdown 檔產生目錄。"""
from __future__ import annotations

import argparse
import re
from pathlib import Path


def build_toc(text: str) -> str:
    lines = []
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if not m:
            continue
        level = len(m.group(1))
        title = m.group(2).strip()
        anchor = re.sub(r"[^\w\u4e00-\u9fff\- ]", "", title).strip().lower().replace(" ", "-")
        lines.append(f"{'  ' * (level - 1)}- [{title}](#{anchor})")
    return "\n".join(lines)


def main() -> None:
    p = argparse.ArgumentParser(description="Markdown TOC generator")
    p.add_argument("file", type=Path)
    args = p.parse_args()
    text = args.file.read_text(encoding="utf-8")
    print(build_toc(text))


if __name__ == "__main__":
    main()
