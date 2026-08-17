# Contributing

This repository is the companion to *Harnessing the Horse* by John
Briggs. It contains reader-facing templates, prompts, checklists,
factory-bootstrap workbooks, examples, diagrams, exercises, and
references that accompany the book.

## Reporting errata

If something in this repository contradicts the book, or is broken,
out of date, or unclear:

1. Check existing issues to see if it has been reported.
2. Open a new issue with:
   - The specific file and section (or line number).
   - What the book says vs. what the asset says.
   - For broken code: the command you ran, the expected behavior,
     the actual behavior, your environment (OS, language version).
3. Tag the issue with the appropriate label: `errata`, `broken`,
   `outdated`, `unclear`.

The book itself is the canonical source. If an asset here disagrees
with the book, the asset is wrong — even if the asset reads cleanly.

## Suggesting improvements

We welcome:

- Additional worked examples that illustrate a template or prompt in
  a specific stack (Python, Go, Rust, TypeScript, etc.).
- Adaptations of prompts for additional models or tools (with
  empirical notes on what changed and why).
- Additional exercises in the format described in
  `exercises/README.md`.
- Translations of templates and prompts into other natural languages
  (with attribution preserved).

Before submitting a pull request for any of the above:

1. Open an issue describing what you intend to add and why.
2. Wait for confirmation that the contribution fits the repo's scope.
   (We may decline contributions that overlap existing assets or
   would dilute focus.)
3. Once confirmed, fork, branch, and submit a PR referencing the
   issue.

## What we will NOT accept

- **Manuscript content.** The book's prose is the author's. Do not
  submit pull requests modifying the book's framework definitions,
  case study analyses, or coined terminology.
- **Code reformatting for its own sake.** Stylistic edits without a
  functional improvement create review burden without reader benefit.
- **License changes.** This repo uses a deliberate dual-license
  arrangement: MIT for code (`LICENSE-CODE`), CC BY-NC-SA 4.0 for
  written content (`LICENSE-CONTENT`). License-modification PRs will
  be closed.
- **Mislicensed contributions.** When you contribute, classify your
  contribution correctly: source code goes under MIT, prose / templates
  / prompts / checklists / workbooks / exercises go under CC BY-NC-SA
  4.0. A contribution that
  attempts to relicense an asset (e.g., a PR moving a template into
  `code-examples/` to escape the non-commercial clause) will be closed.
- **Self-promotional additions.** Adding your own product, tool, or
  consultancy to a template or prompt is not appropriate. The book's
  examples reference specific tools where pedagogically necessary;
  reader contributions should not add commercial endorsements.

## Pull request expectations

If your PR is accepted in principle (via the issue conversation):

- Match the existing file conventions: chapter-of-origin header,
  `## Related` section, `## Provenance` block.
- Preserve the applicable license footer: MIT for executable code,
  CC BY-NC-SA 4.0 for written companion content.
- For new files: update the relevant per-directory `README.md` table
  and the top-level `INDEX.md`.
- For substantive additions: add a `CHANGELOG.md` entry under
  `## [Unreleased]`.

Before opening the pull request, validate the complete public package:

```bash
npm ci
npm run check
```

The check verifies local links, prompt metadata and evaluation fixtures,
code license headers, release-version alignment, the public/private
architecture boundary, strict TypeScript compilation, and example behavior.
Also read new prose and rendered diagrams manually; passing automation is a
floor, not an editorial or security approval.

Classify additions before placing them. Executable implementations and test
code belong in an MIT-covered code area. Prompts, templates, checklists,
workbooks, diagrams, and explanatory prose remain written content even when
they contain snippets, and belong under CC BY-NC-SA 4.0.

We commit-squash on merge and rewrite the message to follow the
repository's style. Your authorship is preserved via the GitHub PR
attribution.

## Code of conduct

Be honest, be precise, be respectful of others' time. Disagreement
about technical content is welcome; disagreement about the legitimacy
of others' contributions is not.

## Author contact

For private inquiries, including instructor adoption, commercial
licensing, or content adaptation, contact the author directly. Do not
open public issues for these topics.
