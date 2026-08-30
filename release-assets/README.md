# Release Assets

This directory contains the editable source for curated reader downloads.
The generated PDF lives in [`output/pdf/`](../output/pdf/).

| Source | Output | Purpose |
| --- | --- | --- |
| `reader-quick-start.json` | `Harnessing-the-Horse-Reader-Quick-Start-v2.1.2.docx` and `.pdf` | A concise path from opening the companion to an evidence-backed SHIP, REVISE, or STOP decision |
| `diagrams/merlin-architecture-v2-visual-1.png` through `-5.png` | `Harnessing-the-Horse-Software-Factory-Teaching-Panels-v2.1.2.docx` and `.pdf` | Five visual panels with semantic headings, alt text, and equivalent text descriptions |

Rebuild the PDF from the repository root:

```bash
python3 -m pip install -r release-assets/requirements-reader-guide.txt
python3 scripts/build_reader_guide.py
python3 scripts/build_teaching_panels.py
```

Prerequisites are Python 3.10 or newer and LibreOffice Writer 7.6 or newer.
LibreOffice must be available on `PATH` as `soffice` or `libreoffice`; it is the
export engine that preserves the Word structure as PDF tags. Poppler's
`pdfinfo` is recommended for local verification and required by CI.

Release sources are written content licensed under CC BY-NC-SA 4.0. The
generator in `scripts/` is MIT-licensed.
