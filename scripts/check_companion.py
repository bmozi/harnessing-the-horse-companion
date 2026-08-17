#!/usr/bin/env python3
"""Deterministic quality checks for the public companion repository.

© 2026 John Briggs — MIT licensed (see ../LICENSE-CODE)
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
IGNORED_PREFIXES = ("http://", "https://", "mailto:", "#")
PROMPT_EXCLUSIONS = {"README.md", "complete-prompt-library.md"}
REMOVED_PUBLIC_ASSETS = {
    "diagrams/merlin-architecture-v2-diagrams.html",
    "diagrams/merlin-factory-architecture-expanded.html",
    "diagrams/merlin-factory-architecture-expanded.jpg",
    "diagrams/merlin-factory-architecture-expanded.png",
    "diagrams/merlin-factory-architecture-expanded.webp",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_markdown_links(errors: list[str]) -> int:
    checked = 0
    for markdown in ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in markdown.relative_to(ROOT).parts):
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split()[0].strip("<>")
            if target.startswith(IGNORED_PREFIXES):
                continue
            checked += 1
            relative_target = target.split("#", 1)[0]
            resolved = (markdown.parent / relative_target).resolve()
            if not resolved.exists():
                fail(errors, f"missing link target: {markdown.relative_to(ROOT)} -> {target}")
    return checked


def load_json(relative: str, errors: list[str]) -> object | None:
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"invalid JSON: {relative}: {exc}")
        return None


def check_prompt_manifest(errors: list[str]) -> tuple[int, int]:
    manifest = load_json("prompts/manifest.json", errors)
    if not isinstance(manifest, dict) or not isinstance(manifest.get("prompts"), list):
        fail(errors, "prompts/manifest.json must contain a prompts array")
        return 0, 0

    prompt_ids: set[str] = set()
    manifested_files: set[str] = set()
    eval_files: set[str] = set()
    required = {"id", "file", "purpose", "riskLevel", "inputs", "expectedOutput", "evaluationFixtures"}
    for entry in manifest["prompts"]:
        if not isinstance(entry, dict) or not required.issubset(entry):
            fail(errors, f"prompt manifest entry missing fields: {entry!r}")
            continue
        prompt_id = entry["id"]
        if prompt_id in prompt_ids:
            fail(errors, f"duplicate prompt id: {prompt_id}")
        prompt_ids.add(prompt_id)
        prompt_file = ROOT / "prompts" / entry["file"]
        if not prompt_file.exists():
            fail(errors, f"manifest prompt file does not exist: {entry['file']}")
        manifested_files.add(entry["file"])
        for fixture in entry["evaluationFixtures"]:
            fixture_path = (ROOT / "prompts" / fixture).resolve()
            if not fixture_path.exists():
                fail(errors, f"manifest evaluation fixture does not exist: {fixture}")
            eval_files.add(str(fixture_path.relative_to(ROOT)))

    expected_files = {
        path.name
        for path in (ROOT / "prompts").glob("*.md")
        if path.name not in PROMPT_EXCLUSIONS
    }
    for missing in sorted(expected_files - manifested_files):
        fail(errors, f"prompt missing from manifest: {missing}")

    fixture_count = 0
    for fixture_path in sorted((ROOT / "prompt-evals").glob("*.json")):
        fixture_count += 1
        fixture = load_json(str(fixture_path.relative_to(ROOT)), errors)
        if not isinstance(fixture, dict):
            continue
        required_fixture = {"schemaVersion", "promptId", "input", "requiredSignals", "prohibitedSignals", "passCriteria"}
        if not required_fixture.issubset(fixture):
            fail(errors, f"evaluation fixture missing fields: {fixture_path.relative_to(ROOT)}")
        if fixture.get("promptId") not in prompt_ids:
            fail(errors, f"evaluation fixture has unknown promptId: {fixture_path.relative_to(ROOT)}")
        if str(fixture_path.relative_to(ROOT)) not in eval_files:
            fail(errors, f"evaluation fixture is not referenced by manifest: {fixture_path.relative_to(ROOT)}")

    return len(prompt_ids), fixture_count


def check_code_licenses(errors: list[str]) -> int:
    checked = 0
    for suffix in ("*.ts", "*.sql"):
        for source in (ROOT / "code-examples").rglob(suffix):
            checked += 1
            opening = "\n".join(source.read_text(encoding="utf-8").splitlines()[:16])
            if "MIT licensed" not in opening:
                fail(errors, f"code example missing traveling MIT notice: {source.relative_to(ROOT)}")
    return checked


def check_public_boundary(errors: list[str]) -> None:
    for relative in REMOVED_PUBLIC_ASSETS:
        if (ROOT / relative).exists():
            fail(errors, f"private architecture asset restored to public tree: {relative}")


def check_versions(errors: list[str]) -> str:
    package = load_json("package.json", errors)
    manifest = load_json("prompts/manifest.json", errors)
    reader_guide = load_json("release-assets/reader-quick-start.json", errors)
    if not isinstance(package, dict) or not isinstance(manifest, dict) or not isinstance(reader_guide, dict):
        return "unknown"
    version = str(package.get("version", ""))
    if manifest.get("libraryVersion") != version:
        fail(errors, "package.json and prompt manifest versions differ")
    if reader_guide.get("version") != version:
        fail(errors, "package.json and reader quick-start versions differ")
    edition_map = (ROOT / "EDITION-MAP.md")
    if edition_map.exists() and f"`v{version}`" not in edition_map.read_text(encoding="utf-8"):
        fail(errors, f"EDITION-MAP.md does not name v{version}")
    reader_pdf = ROOT / "output" / "pdf" / f"Harnessing-the-Horse-Reader-Quick-Start-v{version}.pdf"
    if not reader_pdf.exists():
        fail(errors, f"reader quick-start PDF missing for v{version}")
    return version


def main() -> int:
    errors: list[str] = []
    links = check_markdown_links(errors)
    prompts, fixtures = check_prompt_manifest(errors)
    sources = check_code_licenses(errors)
    check_public_boundary(errors)
    version = check_versions(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Companion checks failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(
        f"Companion checks passed: version {version}; {links} local links; "
        f"{prompts} prompt entries; {fixtures} eval fixtures; {sources} code sources."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
