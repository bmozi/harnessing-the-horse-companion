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
`release-assets/reader-quick-start.json` to the curated PDF in `output/pdf/`.
Its pinned ReportLab dependency is recorded in
`release-assets/requirements-reader-guide.txt`.
