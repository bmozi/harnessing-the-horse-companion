# Release Assets

This directory contains the editable source for curated reader downloads.
The generated PDF lives in [`output/pdf/`](../output/pdf/).

| Source | Output | Purpose |
| --- | --- | --- |
| `reader-quick-start.json` | `Harnessing-the-Horse-Reader-Quick-Start-v2.1.0.pdf` | A concise path from opening the companion to completing one governed delivery loop |

Rebuild the PDF from the repository root:

```bash
python3 -m pip install -r release-assets/requirements-reader-guide.txt
python3 scripts/build_reader_guide.py
```

Release sources are written content licensed under CC BY-NC-SA 4.0. The
generator in `scripts/` is MIT-licensed.
