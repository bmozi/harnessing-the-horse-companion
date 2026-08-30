# External Reader Usability Pass

## Status

Recruitment is open for companion release **v2.1.2**. Automated and
cross-platform checks run in CI; those checks are not represented as human
reader evidence.

## Purpose

Determine whether a new reader can find the right entry point, complete one
bounded practice task, understand the delivery decision, and use the two
reader documents without coaching.

## Small-pass protocol

Recruit three to five readers who resemble the intended audience. Include at
least one engineering leader and one practicing software engineer. When
available, include one reader who routinely uses keyboard navigation, text
reflow, magnification, or a screen reader.

Do not introduce the repository beyond this sentence: “Use this companion to
take one AI-assisted software change from a request to a defensible delivery
decision.” Then ask each reader to perform these tasks:

1. Find the intended starting point and explain what to do first.
2. Choose one low-risk task and locate the artifact used to bound it.
3. Locate the evidence required before an AI coding agent is allowed to act.
4. Explain the difference among SHIP, REVISE, and STOP.
5. Open the Reader Quick Start and identify the smallest useful artifact for
   challenging a generated result.
6. Open the Teaching Panels and explain where human judgment enters the
   architecture.
7. Find how to report an error or accessibility barrier.

Record completion, elapsed time, wrong turns, questions, and the reader's own
words. Do not rescue the reader until a task has clearly failed; the point is
to find the seam, not to demonstrate the repository.

## Pass criteria

- At least four of five readers, or all three in a three-reader pass, find
  `START-HERE.md` within two minutes.
- At least 80 percent of tasks are completed without coaching.
- Every reader can distinguish a governed delivery decision from “the code ran.”
- No critical accessibility barrier prevents completion of tasks 5 through 7.
- Every repeated wrong turn becomes an issue with an owner and disposition.

Submit one issue per participant using the
[reader-usability form](https://github.com/bmozi/harnessing-the-horse-companion/issues/new?template=reader-usability.yml).
Aggregate conclusions only after the small pass is complete; do not average
away a severe failure.
