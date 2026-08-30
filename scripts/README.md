# Repository Checks

`check_companion.py` validates the public companion's local Markdown links,
prompt manifest and evaluation fixtures, code license headers, version
alignment, and absence of retired private-architecture paths.

Run all checks from the repository root:

```bash
npm ci
npm run check
```

The script is MIT-licensed; its checks protect repository consistency but
do not replace editorial, security, or production-readiness review.

`build_reader_guide.py` renders the versioned content in
`release-assets/reader-quick-start.json` to semantic DOCX and tagged PDF
editions. `build_teaching_panels.py` does the same for the five public teaching
panels and refreshes the stable diagram PDF.

Document generation requires Python 3.10 or newer, the pinned Python package in
`release-assets/requirements-reader-guide.txt`, and LibreOffice Writer 7.6 or
newer on `PATH` as `soffice` or `libreoffice`. PDF validation additionally uses
Poppler's `pdfinfo`. The `reader-documents` CI job installs these prerequisites,
rebuilds both documents, and rejects untagged outputs.

After committing a release, build its reader downloads and repository archive
with the exact tag that will be published:

```bash
python3 scripts/build_release_assets.py --ref v2.1.2
```

The command writes the full companion ZIP, both DOCX/PDF pairs, the overview
image, and `SHA256SUMS.txt` to ignored `dist/` output.
