# How do you verify AI-generated work?

Turn a completion claim into an observable result, retain the evidence, and make a clear ship, revise, or stop decision.

## The short answer

Verify the result that matters, using a check capable of detecting the relevant failure. Keep the result, its scope, and anything you did not check. An agent saying “done” is a claim to investigate, not the evidence itself.

## How it works

Write the claim before choosing the check. “The changed endpoint rejects an expired token” can be checked by an integration test that sends an expired token to the changed endpoint. A formatter cannot establish that claim. A green unit test about a helper may be relevant without establishing the endpoint's behavior.

Retain a small evidence record: claim, exact revision, check, observed result, and limitations. A command exiting successfully supports only what that command actually exercised. A planned check is not a passing result.

## A constructed example

An agent changes a fictional task API and reports that access control is fixed. A useful check sends requests as the permitted user, a different user, and an expired session. If the acceptance claim includes recovery after restart, exercise that too. Record which cases actually ran rather than writing “security verified.”

## When to use it

Use this approach before accepting an AI-assisted change, publishing a generated artifact, or delegating a consequential action. Match effort to consequence: a local text correction needs different evidence from a payment operation.

## What to watch for

- A successful build presented as proof of correct behavior.
- The same agent repeating its own explanation without new evidence.
- Tests running against a different revision or environment.
- Screenshots or logs with no connection to the claimed result.
- Unrun checks quietly reported as passing.

## Try it

Take one recent completion claim. Replace “it works” with a behavior you can observe. Write the smallest check that could disprove that claim, run it when appropriate, and retain the result. Use the companion session decision record to choose ship, revise, or stop.

## Continue learning

Work through the [verification learning path](https://bmozi.net/learn/verification). A quiz can check recognition; the practical record is where you show what you actually tested.

## Source and further practice

Book connection: Harnessing the Horse, Chapters 7–8; The Accountable AI Software Factory, Chapter 10.

- [Quality-gate configuration reference](https://github.com/bmozi/harnessing-the-horse-companion/blob/main/references/quality-gate-configuration-reference.md)
- [Session decision record](https://github.com/bmozi/harnessing-the-horse-companion/blob/main/factory-bootstrap/SESSION_DECISION.md)
- [Disprove-only review prompt](https://github.com/bmozi/harnessing-the-horse-companion/blob/main/prompts/disprove-only-review.md)

Author: John Briggs. Updated 2026-11-24. This is original companion learning material; constructed examples are labeled.
