#!/usr/bin/env python3
# © 2026 John Briggs - MIT licensed
"""Build the versioned Book 2 companion release assets and checksums."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

from build_reader_guide import build as build_quick_start
from build_teaching_panels import main as build_teaching_panels

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", default="HEAD", help="Git ref to archive; use the release tag for publication")
    parser.add_argument("--skip-build", action="store_true", help="Reuse already-built reader documents")
    args = parser.parse_args()

    version = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))["version"]
    DIST.mkdir(parents=True, exist_ok=True)
    if not args.skip_build:
        build_quick_start()
        build_teaching_panels()

    prefix = f"harnessing-the-horse-companion-v{version}/"
    archive = DIST / f"Harnessing-the-Horse-Companion-Pack-v{version}.zip"
    subprocess.run(
        ["git", "archive", "--format=zip", f"--prefix={prefix}", "--output", str(archive), args.ref],
        cwd=ROOT,
        check=True,
    )

    source_files = [
        ROOT / "output" / "docx" / f"Harnessing-the-Horse-Reader-Quick-Start-v{version}.docx",
        ROOT / "output" / "pdf" / f"Harnessing-the-Horse-Reader-Quick-Start-v{version}.pdf",
        ROOT / "output" / "docx" / f"Harnessing-the-Horse-Software-Factory-Teaching-Panels-v{version}.docx",
        ROOT / "output" / "pdf" / f"Harnessing-the-Horse-Software-Factory-Teaching-Panels-v{version}.pdf",
    ]
    release_files = [archive]
    for source in source_files:
        destination = DIST / source.name
        shutil.copy2(source, destination)
        release_files.append(destination)

    overview = DIST / f"Harnessing-the-Horse-Software-Factory-Overview-v{version}.png"
    shutil.copy2(ROOT / "diagrams" / "merlin-factory-architecture-premium.png", overview)
    release_files.append(overview)

    checksums = DIST / "SHA256SUMS.txt"
    checksums.write_text(
        "".join(f"{sha256(path)}  {path.name}\n" for path in sorted(release_files, key=lambda item: item.name)),
        encoding="utf-8",
    )
    for path in [*release_files, checksums]:
        print(f"{sha256(path)}  {path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
