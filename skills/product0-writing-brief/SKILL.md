---
name: product0-writing-brief
description: Use when the user has explicitly approved a complete Product0 direction and it must be written as one concise, evidence-aware, implementation-neutral developer brief.
license: MIT
compatibility: Agent Skills-compatible coding agents with project file write access.
metadata:
  author: product0
  version: "0.2.0"
  role: artifact
---

# Writing the Product0 Brief

## Goal

Write the approved product direction once, clearly and proportionately, so a developer can begin technical brainstorming without rediscovering product strategy.

## Preconditions

- Repository orientation is complete.
- `product0-challenging-direction` returned `DIRECTION_READY`.
- The user explicitly approved the complete direction proposal.
- All material product decisions are resolved or explicitly recorded as non-blocking open risks.

## Iron law

```text
ONE APPROVED DIRECTION = ONE COHERENT BRIEF WRITE.
```

Do not create a placeholder, append discovery fragments, or carry pending headings into the document.

## Path

Create:

```text
docs/product0/briefs/YYYY-MM-DD-<descriptive-topic>-product-brief.md
```

For a revision, update the existing canonical brief in place and increment `revision`.

Use `assets/product-brief-template.md` as an adaptive shape, not a form.

## Writing standard

### Answer first

Lead with the executive direction and the important choices. Do not make the developer reconstruct the recommendation from a long history.

### Preserve provenance

Label claims as:

- **Repository evidence**
- **User-confirmed**
- **Product0 recommendation**
- **Working assumption**
- **Open risk**

### Adapt to product type

Use the relevant sections from the selected product lens. Omit inapplicable sections.

Examples:

- A marketing surface needs positioning, message hierarchy, proof, objections, visual direction, and conversion.
- A workflow needs actors, lifecycle, business rules, authority, and consequential exceptions.
- A platform capability needs consumers, boundaries, configuration, guarantees, and control.

### Avoid ceremony

- Do not create requirement IDs unless complex interacting behavior benefits from traceability.
- Do not create product slices unless there are two or more meaningful outcomes, phases, or deferrals.
- Do not include empty sections.
- Do not duplicate the same proposition under several headings.
- Do not record every conversational turn or approval.
- Do not specify generic form mechanics unless they are a material product decision.

### Scale depth

Typical targets:

- small initiative: 700–1,500 words;
- medium initiative: 1,500–3,000 words;
- large initiative: decompose before writing.

These are guidance, not quotas. Insight density matters more than length.

## Required content

Every brief needs:

1. frontmatter with current status and revision;
2. executive direction;
3. repository and user context with evidence references;
4. type-appropriate product direction;
5. fixed decisions and non-goals;
6. Product0 recommendations;
7. working assumptions and open risks;
8. success evidence and guardrails;
9. directions for technical brainstorming;
10. the standard developer next step.

The brief may include acceptance examples, requirements, states, or slices only when they clarify consequential behavior.

## Developer next step

End with:

```markdown
## Developer next step

This brief is approved product direction, not an implementation specification.

A developer should read it in full and separately invoke `product0-using-brief`. Technical brainstorming may inspect the codebase and choose architecture, interfaces, data flow, persistence, error mechanisms, migrations, observability, and tests while preserving the fixed product direction and non-goals.

Product0 stops before technical design or implementation begins.
```

Set `status: handoff-draft`, then invoke `product0-reviewing-brief`.

## Self-review before saving

- No `TBD`, `TODO`, pending marker, or empty heading.
- No unsupported fact or promoted assumption.
- Every repository reference is relevant.
- No material product decision is hidden as technical latitude.
- No repeated section adds the same information.
- Document size is proportionate.
- A developer unfamiliar with the conversation can understand the direction.
