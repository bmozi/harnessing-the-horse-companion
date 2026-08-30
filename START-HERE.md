# Start Here: One Production-Readiness Journey

Prefer a printable orientation? Download the six-page
[`Reader Quick Start`](output/pdf/Harnessing-the-Horse-Reader-Quick-Start-v2.1.2.pdf).

This companion is a working kit for applying the engineering discipline in
*Harnessing the Horse*. Choose the path that matches the outcome you want. You
do not need to read every directory before using one resource, but the book is
the operating guide for deciding what belongs in the artifacts and whether the
evidence is enough.

The shortest complete path is:

`REQUEST → SPECIFY → BOUND → BUILD → CHALLENGE → PROVE → SHIP / REVISE / STOP`

The repository lets you practice that path once. The book teaches the Twelve
Standards, architecture, failure modes, security boundaries, measurement, and
adoption judgment needed to make the path a trustworthy engineering practice.

## I Have 30 Minutes

Use this path to understand the operating model and choose a first action:

1. Read the [Twelve Standards quick reference](references/twelve-standards-quick-reference.md).
2. Scan the [complete session loop](references/complete-session-loop.md).
3. Complete the [maturity assessment](exercises/maturity-assessment.md).
4. Pick one next action from the assessment. Do not begin with orchestration.

**Outcome:** one evidence-backed decision about what your practice needs next.

## I Want to Run One Governed Agent Session

Use this path for a real, bounded change in an existing repository:

For a small, local change, start with the compact
[`Small Change Session`](factory-bootstrap/small-change-session.md). It keeps
the same accountability boundary while combining the records that do not need
to be separate. Use the full path below when the change crosses an interface,
data boundary, dependency, deployment track, or material consequence.

1. Create or improve the project context file with the
   [context checklist](factory-bootstrap/01-context-file-checklist.md).
2. Define the change with the
   [Work Order template](factory-bootstrap/02-work-order-template.md).
3. Write the implementation contract with the
   [SPEC template](spec-templates/spec-md.md).
4. Follow the [first-session runbook](factory-bootstrap/04-session-loop-runbook.md).
5. Generate with the [structured prompt](prompts/structured-prompt.md).
6. Review with the [disprove-only prompt](prompts/disprove-only-review.md).
7. Record evidence and learning before declaring the session complete.
8. Make and record one explicit **SHIP**, **REVISE**, or **STOP** decision using the
   [`SESSION_DECISION.md`](factory-bootstrap/SESSION_DECISION.md).

Read the [completed fictional example](factory-bootstrap/worked-example/README.md)
before filling the blank artifacts if this is your first session.

The ordered [governed-session pack](factory-bootstrap/governed-session-pack/README.md)
places each blank artifact beside the matching stage of the worked example.

**Outcome:** a reviewable change whose scope, evidence, limitations, decision,
and learning survive the chat session that produced it.

## I Want to Bootstrap a Governed Delivery Loop

Book 2's minimum is one governed delivery loop, not a fleet of agents or a
complete multi-team factory. Work through these resources in order:

1. [Minimum governed delivery loop bootstrap](factory-bootstrap/README.md)
2. [Completed fictional governed-loop example](factory-bootstrap/worked-example/README.md)
3. [Quality-gate classification](references/quality-gate-configuration-reference.md)
4. [Tool and context configuration](references/tool-configuration-reference.md)
5. [30-day transformation roadmap](exercises/30-day-transformation-roadmap.md)
6. [Governed delivery loop readiness review](factory-bootstrap/07-factory-readiness-review.md)

Do not automate a loop that your team cannot yet run manually. Earn additional
autonomy with gate reliability, review quality, and measured outcomes.

**Outcome:** a crawl-stage governed loop operating on one repository with
explicit work intake, a bounded session loop, enforced checks, and a learning
record. Book 3 expands those prerequisites into an accountable production
system across teams.

## What the Repository Cannot Decide for You

A passing test is evidence, not permission. A completed checklist is a record,
not judgment. Before treating the result as production-ready, use the book to
answer the questions the templates intentionally cannot answer on their own:

- Is the requirement actually the right outcome?
- Is the remaining uncertainty proportionate to the consequence?
- Did the review challenge the most dangerous claim or merely confirm the
  easiest behavior?
- Does the person approving the change have the competence and authority to
  accept the risk?
- What evidence would force the team to revise, stop, or roll back?

If those answers are unclear, the toolkit has surfaced the next reading and
decision—not granted permission to ship.

## I Need a Specific Resource

| Need | Start with |
| --- | --- |
| Write a specification | [SPEC and design templates](spec-templates/README.md) |
| Generate or review with an agent | [Prompt library](prompts/README.md) |
| Configure lifecycle checks | [Checklist library](checklists/README.md) |
| Select an architecture pattern | [Pattern library](patterns/README.md) |
| Study the software-factory operating model | [Architecture overview](diagrams/README.md) |
| Copy executable reference code | [Runnable code examples](code-examples/README.md) |
| Teach or study a chapter | [Study guides](study-guides/README.md) |
| Find every book-linked asset | [Chapter-by-chapter index](INDEX.md) |
| Pair practice with book reasoning | [Book-to-toolkit map](BOOK-TO-TOOLKIT-MAP.md) |
| Understand the four-book learning path | [Series progression](SERIES-PROGRESSION.md) |

## Definition of a Successful First Use

Your first use is successful when all of the following are true:

- the task is bounded before generation;
- acceptance criteria and MUST-NOT constraints are explicit;
- automated checks run and their results are recorded;
- someone or a fresh agent challenges the implementation claim;
- unresolved findings and assumptions are visible;
- one learning is carried into the next session.

The goal is not more generated code. The goal is a result you can explain,
verify, operate, and improve.

## When to Continue to Book 3

Stay with Book 2 until one team can run this loop honestly on one repository.
Continue to *The Accountable AI Software Factory* when the problem crosses
teams, repositories, agents, durable queues, release authorities, or outcome
owners. The [Book 3 laboratory](https://github.com/bmozi/accountable-ai-software-factory-companion)
begins where an individual governed session stops being the whole system.

## Downloads and Versions

Git users can clone the repository. Other readers can use the curated archives
and printable resources on the
[GitHub Releases page](https://github.com/bmozi/harnessing-the-horse-companion/releases).
See [EDITION-MAP.md](EDITION-MAP.md) before using the materials with a print or
Kindle edition, and check [ERRATA.md](ERRATA.md) for corrections.
