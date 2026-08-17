# Diagrams

Architecture diagrams used in *Harnessing the Horse* — forkable,
annotatable, reusable. Markdown/Mermaid and HTML sources are canonical; rendered exports
(`.png`, `.pdf`, `.html`) are tracked alongside for convenience.

> These artifacts are companion materials for *Harnessing the Horse*.
> The book provides the design rationale, failure modes, and case-study
> context that explain why each diagram is structured as it is. The
> diagrams in this directory are creative works licensed under
> CC BY-NC-SA 4.0 ([see `../LICENSE-CONTENT`](../LICENSE-CONTENT)).
> Attribution required for reuse; commercial republication requires
> separate licensing.

## Diagrams

### Baseline architecture diagrams (Chapter 4)

| File | Type | What it shows |
| --- | --- | --- |
| [`baseline-architecture-diagrams.md`](baseline-architecture-diagrams.md) | Mermaid + prose | The four diagrams every agent-ready project should maintain: System Context, Component, Data Flow, Deployment. Includes the maintenance discipline and the PR-template checklist. |

### Merlin Software Factory (Chapter 16 case study)

The public architecture set documents the current operating model: an EXPRESS
single-agent primary path surrounded by deterministic preflight, independent
proof, bounded recovery, human judgment, observability, memory, and measured
improvement. Use the following sequence:

1. **Orient:** start with the [premium overview](merlin-factory-architecture-premium.png).
2. **Explain:** use the [software-factory story](merlin-software-factory-promo.png)
   for presentations, team conversations, and conceptual onboarding.
3. **Study:** read the [public teaching architecture](merlin-architecture-v2.md)
   and its five focused panels.
4. **Print or teach:** use the five-page PDF for a course, workshop, or team
   architecture review.

#### Choose the right view

| Reader need | Recommended asset | Why |
| --- | --- | --- |
| Best first view | [`merlin-factory-architecture-premium.png`](merlin-factory-architecture-premium.png) ([HTML source](merlin-factory-architecture-premium.html)) | A polished, one-page map of the factory's primary lane and supporting planes. |
| Conceptual explanation or presentation | [`merlin-software-factory-promo.png`](merlin-software-factory-promo.png) ([HTML source](merlin-software-factory-promo.html)) | Explains the Discover-Design-Build-Verify-Observe arc and the role of gates, memory, and control loops without implementation density. |
| Reader-facing architecture narrative | [`merlin-architecture-v2.md`](merlin-architecture-v2.md) | Explains responsibilities, evidence flow, verification classes, human judgment, and learning without publishing private implementation topology. |
| Panel-by-panel teaching set | [`merlin-architecture-v2-visual-1.png`](merlin-architecture-v2-visual-1.png) through [`merlin-architecture-v2-visual-5.png`](merlin-architecture-v2-visual-5.png) ([HTML source](merlin-architecture-v2-visual.html)) | Five portrait panels covering preflight, the EXPRESS arc, verification policy, human judgment, and continuous improvement. |
| Print-friendly teaching set | [`merlin-architecture-v2-visual.pdf`](merlin-architecture-v2-visual.pdf) | Five A4 portrait pages, one teaching panel per page. |
| Digital composite | [`merlin-architecture-v2-visual.png`](merlin-architecture-v2-visual.png) | A single tall canvas containing all five teaching panels. |
| Historical comparison only | [`merlin-architecture.md`](merlin-architecture.md) | Preserves the lesson of the original multi-agent blueprint without publishing its former implementation map. |

The premium and promotional images are also supplied as `.jpg` and `.webp`
exports for publishing workflows that prefer those formats. HTML and
Mermaid/Markdown sources remain canonical; rendered files are convenience
exports.

#### Public abstraction boundary

The companion teaches the operating model, not Merlin's private implementation
map. Public editions intentionally omit source filenames, module and tool
inventories, model fallback order, database and deployment topology, internal
prompts, and operational thresholds. These details are unnecessary for readers
to apply the book's durable engineering principles and would become stale as the
implementation evolves.

## Conventions

- **Source first.** Mermaid `.mmd` or `.md` source lives alongside any
  rendered `.png` / `.svg` / `.pdf`. If both exist, the source is
  canonical.
- **Naming.** `<chapter-or-part>-<slug>.{mmd,md,png,svg,pdf,html}` —
  e.g. a future `ch13-agent-infrastructure-overview.mmd`. The current
  Merlin files predate this convention and keep their existing names.
- **Attribution.** Diagram source includes a comment with copyright
  and book reference so attribution survives a copy.

## Tools

Mermaid diagrams render directly on GitHub. For local preview or
regeneration:

```bash
npx -y @mermaid-js/mermaid-cli -i path/to/diagram.mmd -o path/to/diagram.svg
```

## Coverage note

This directory keeps the reusable architecture diagrams that benefit
from source access and visual exports: the baseline architecture set
from Chapter 4 and the Merlin Software Factory visuals from Chapter
16. Other figures are printed in the book where their surrounding
explanation is required.
