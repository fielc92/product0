# Adaptive Product0 developer brief template

Use only sections that add decision value. Do not leave headings empty.

```markdown
---
product0: true
id: p0-YYYYMMDD-<slug>
title: <title>
product_type: <type>
status: handoff-draft
revision: 1
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Product0 Developer Brief: <title>

## Executive direction
<The approved recommendation and why it is the right direction>

## Context and evidence
- **Repository evidence:** `<relative/path>` — <implication>
- **User-confirmed:** <important context or decision>

## <Type-specific strategic sections>
<Only the sections selected by the relevant product lens>

## Fixed product decisions
<Decisions technical brainstorming must preserve>

## Product0 recommendations
<Professional choices made by Product0 within delegated or low-risk authority>

## Product constraints and non-goals
<External constraints and explicit exclusions>

## Success evidence and guardrails
<How success will be recognized and what must not regress>

## Working assumptions and open risks
- **Working assumption:** ...
- **Open risk:** ...

## Directions for technical brainstorming
<The implementation-neutral code and system questions the developer should solve>

## Developer next step
This brief is approved product direction, not an implementation specification.

A developer should read it in full and separately invoke `product0-using-brief`. Technical brainstorming may inspect the codebase and choose architecture, interfaces, data flow, persistence, error mechanisms, migrations, observability, and tests while preserving the fixed product direction and non-goals.

Product0 stops before technical design or implementation begins.
```

Optional sections when justified:

- Product requirements with stable IDs for complex interacting behavior.
- Product-visible state model for a genuine lifecycle.
- Acceptance examples for ambiguous or high-risk business rules.
- Product slices for two or more meaningful outcomes or release phases.
- Revision summary for an updated brief.
