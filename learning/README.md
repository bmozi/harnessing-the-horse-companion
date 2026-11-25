# AI engineering learning pilot

Start with [Verify one AI-assisted change](verification/name-the-claim.md), or
use one reference when you have a question:

- [How do you verify AI-generated work?](reference/verify-ai-generated-work.md)
- [What belongs in an AI agent context file?](reference/useful-context-files.md)
- [How do you limit what an AI tool can do?](reference/bound-tool-authority.md)

## Verification: four lessons and one evidence record

1. [Name the result you need to prove](verification/name-the-claim.md)
2. [Choose evidence that can challenge the claim](verification/choose-the-check.md)
3. [Ask what would show the explanation is wrong](verification/challenge-the-explanation.md)
4. [Choose ship, revise, or stop](verification/make-the-decision.md)

The interactive edition is intended for [bmozi.net/learn](https://bmozi.net/learn).
The website imports a versioned copy of [pilot.json](pilot.json); this repository
is the canonical source. Export Markdown with `python3 scripts/export_learning.py`.
The book remains independently useful; this pilot adds original explanations
and exercises rather than reproducing manuscript chapters.

This is a new main-branch pilot, not part of the existing v2.1.2 release. Examples
are constructed. A quiz checks recognition, and a marked exercise is a reader's
own report; neither certifies production readiness. AI-assisted drafts receive
source, behavior, and presentation checks before publication. No independent
reader trial or guaranteed search visibility is claimed.

Written content retains this repository's CC BY-NC-SA 4.0 license. The website
shows attribution and the applicable license. Existing executable examples
retain their separate licenses.

## Context path

1. [Separate project rules from the current task](context/separate-project-from-task.md)
2. [Write a small context map](context/write-a-small-context-map.md)
3. [Check source authority and currency](context/check-source-currency.md)
4. [Test and maintain the handoff](context/test-the-handoff.md)

The [public discovery reference](reference/public-discovery-and-ai-citations.md)
and [discovery practice](../DISCOVERABILITY.md) explain the publishing checks and
the distinction between technical access and actual citations. The
[companion directory](companions.json) links the thirteen verified public
repositories; each retains its own licensing and evidence statements.

The canonical learning format is now schema version 2 with a `courses` array.
Earlier website imports remain identifiable by their pinned commit. There are
two four-lesson paths; the twelve-topic map remains a coverage map.
