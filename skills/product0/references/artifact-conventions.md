# Product0 artifact conventions

## Project structure

Create directories only when an artifact is actually being written.

```text
docs/product0/
  briefs/
    YYYY-MM-DD-<descriptive-topic>-product-brief.md
  sessions/
    YYYY-MM-DD-HHMM-<descriptive-topic>-session.md
  decisions/
    YYYY-MM-DD-<descriptive-topic>-product-decision-request.md
```

Use the project's local date and lowercase kebab-case slugs.

## Brief timing

```text
NO BRIEF BEFORE PRODUCT DIRECTION IS APPROVED.
```

Do not create a placeholder brief, pending headings, empty sections, or discovery scratch file. Initial brief creation is one coherent write after the user approves the direction proposal.

## Canonical brief

Use one brief per initiative. Revise it in place after approved semantic changes.

Initial frontmatter:

```yaml
---
product0: true
id: p0-YYYYMMDD-<slug>
title: <human-readable title>
product_type: <marketing-surface|workflow|platform-capability|integration|pricing|operations|compliance|quality|other>
status: handoff-draft
revision: 1
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

The written brief must contain no pending markers, `TBD`, or empty ceremonial headings.

## Evidence references

Use repository-relative paths and distinguish:

- repository evidence;
- user-confirmed decisions;
- Product0 recommendations;
- working assumptions;
- open risks.

Do not cite implementation details as product facts unless they describe current observable behavior or an externally imposed constraint.

## Writing rules

- Preserve the original request when it adds context.
- Prefer answer-first prose over template completion.
- Omit sections that add no decision value.
- Use requirement IDs only for complex interacting behavior that benefits from traceability.
- Use product slices only when two or more coherent outcomes, phases, or deferrals genuinely exist.
- Avoid raw approval transcripts and line-by-line decision logs.
- Do not commit artifacts unless the user or repository policy asks for commits.
