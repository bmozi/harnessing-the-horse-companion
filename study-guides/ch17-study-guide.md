# Chapter 17: Security in the Agentic Era — Study Guide

Student and self-study material moved from Chapter 17 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Explain why indirect prompt injection resists traditional input validation, and describe the four layered defenses that contain it.
2. Distinguish Willison's lethal trifecta from the generation trifecta, and classify a given vulnerability under the correct model.
3. Map each of the six agentic security vectors to the engineering standard that owns its control.
4. Construct a threat model for an agentic system using the six-vector checklist, including plausible attack narratives.
5. Analyze a memory-bearing or multi-agent architecture for poisoning and cascade risk.
6. Evaluate an organization's shadow-AI exposure and construct a structural response in place of a policy response.

## Key Terms

- **Generation trifecta (this book)** — The three security failure modes intrinsic to agent-generated code: hallucinated dependencies, reproduced vulnerabilities, and secret leakage; extended in this chapter to six vectors.
- **Lethal trifecta (Willison, 2025)** — Simon Willison's established term for the dangerous runtime combination, in a single agent, of private-data access, exposure to untrusted content, and the ability to communicate externally.
- **Indirect prompt injection** — An attack that plants instructions in data the agent processes from external sources — emails, web pages, database records — rather than in prompts the attacker submits directly (Greshake et al., 2023).
- **Slopsquatting** — A supply chain attack in which attackers register package names AI agents hallucinate, so that installing generated code's dependencies executes the attacker's payload (Larson, 2024; Lanyado, 2024).
- **OWASP *Agentic AI — Threats and Mitigations* (2025)** — The OWASP GenAI Security Project's threat catalog for systems where AI agents act: fifteen named threats, opening with Memory Poisoning, Tool Misuse, and Privilege Compromise.
- **Scoped Authorization Token** — Least privilege applied at the session level: each agent session receives a token whose scope specifies which tools it may invoke.
- **Dry-Run-Default on Write Tools (this book)** — The design pattern requiring every agent-facing write tool to default to a read-only preview, with execution requiring explicit confirmation.
- **MCP (Model Context Protocol)** — The open standard for connecting LLM agents to external tools and data sources (Anthropic, 2024); the layer at which malicious tool providers become a supply chain risk.

## Review Questions

1. Why is indirect prompt injection the more dangerous variant in agentic development, and why can better models alone not eliminate it?
2. Name the three arms of the generation trifecta and, for each, the standard that owns its control.
3. How do the OWASP agentic threat catalog, NIST AI RMF, and MITRE ATLAS compose, and what does each contribute that the others do not?
4. Describe two of the four defensive postures against memory poisoning and the attack step each interrupts.
5. Why do policy documents fail against shadow AI, and what are the three components of the structural response?

## Discussion Questions

1. Section 17.1 argues that good engineering discipline is good security practice — the standards that prevent dark code also close exploitation paths. Where does the overlap end? Identify a security requirement for agentic systems that none of the Twelve Standards covers, and propose how a team should govern it.
2. The structural response to shadow AI assumes the approved workflow can be made the path of least resistance. In an organization where the approved workflow carries the harness overhead (Chapter 4) and the unapproved one carries none, is that assumption realistic? What would have to be true for it to hold?
3. Chapter 13's first-party-only MCP policy trades the ecosystem's composability for a smaller trust boundary. For what class of workload, if any, would you accept community MCP servers, and what evidence would cause you to revisit the policy?

## Exercises

**Exercise 17.1 (Core) — Classify vulnerabilities under the two trifectas.** An audit of an agentic development platform surfaces five findings: (a) a generated payment module imports `stripe-utils-pro`, a package registered three weeks ago with 41 downloads; (b) a deployed documentation agent reads private design documents, summarizes inbound partner emails, and posts digests to a public status page; (c) generated integration code logs full Authorization headers at INFO level; (d) a code-review agent with repository write access processes pull-request descriptions submitted by external contributors; (e) a generated data-access layer builds SQL queries by string concatenation. Classify each finding as lethal trifecta, generation trifecta, or both, and defend each classification in two or three sentences by naming the layer of the problem space it occupies. *(~45 min)*

*Deliverable:* A classification table with a written defense per finding.
*Assessment:* Judged against the layer definitions in Sections 17.2–17.3: runtime capability combinations versus artifacts left in the repository. Full credit requires separating the runtime-exposure findings from the generated-artifact findings and naming the owning standard (per Section 17.6) for each generated-artifact finding.

**Exercise 17.2 (Core) — Threat-model an agentic system with the six-vector checklist.** A mid-size insurer runs a claims-triage agent: it reads inbound claim emails and attachments, queries the policy database read-write through a community-maintained MCP server, keeps a persistent memory of "resolution patterns" that future sessions load, generates patches to its own parsing rules, and emails claimants directly. Work through all six vectors from Section 17.6 for this system. Then write two attack narratives — one exploiting a runtime vector and one exploiting a generation vector — each naming the entry point, the capability abused, and the point at which the mapped standard's control interrupts the attack. *(~2 h)*

*Deliverable:* A completed six-vector checklist and two attack narratives of about one page each.
*Assessment:* Judged against the vector-to-standard mapping in Section 17.6: every vector addressed, every finding mapped to the standard that owns it, and each narrative interrupted by a control the mapped standard actually provides.

**Exercise 17.3 (Core) — Write the secret-leakage controls for a context file.** Your team is generating integration code against a third-party vendor API. Write the credential-handling MUST-NOT section for the project's context file, covering all three secret-leakage vectors in Section 17.3, and specify the pre-commit secret-scanning gate that backs it (tool, trigger, gate tier). *(~45 min)*

*Deliverable:* A context-file MUST-NOT section plus a quality-gate configuration entry.
*Assessment:* Judged against Standard 6's BLOCKING criteria and the credential-handling rule in Section 17.3: the MUST-NOT list must be generation-time guidance the agent applies while writing code, and the gate must block rather than advise. Reference: the context-file template and quality-gate configuration reference in this companion repository.

**Exercise 17.4 (Challenge) — Design a structural shadow-AI response.** A 400-engineer organization has detected the signals of Section 17.7: commit-velocity anomalies on two teams, a spike in low-download dependencies, and stylistic discontinuities in several repositories. Leadership's draft response is a stricter usage policy plus network monitoring. Write the counter-proposal: a structural response covering the three components of Section 17.7, an instrumentation plan built on the three indirect signals, and an explicit argument for why the draft policy will fail. State what your proposal costs and what leadership must give up. *(~4 h+)*

*Deliverable:* A governance proposal of at most three pages.
*Assessment:* Judged against Section 17.7's three structural components. A passing proposal makes the approved workflow the path of least resistance, uses the indirect signals for engagement rather than enforcement, and prices its own overhead honestly. A proposal that reduces to a better-enforced ban fails.
