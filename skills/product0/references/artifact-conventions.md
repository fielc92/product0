# Product0 artifact conventions

## Project directories

```text
docs/product0/
  briefs/
    YYYY-MM-DD-<descriptive-slug>-product-brief.md
  sessions/
    YYYY-MM-DD-HHMM-<descriptive-slug>-session.md
  decisions/
    YYYY-MM-DD-<descriptive-slug>-product-decision-request.md
```

Use the project's local date and time. Use lowercase kebab-case slugs. Keep names descriptive but compact.

Examples:

```text
docs/product0/briefs/2026-07-13-failed-payment-notifications-product-brief.md
docs/product0/sessions/2026-07-13-1430-failed-payment-notifications-session.md
docs/product0/decisions/2026-07-14-payment-retry-identity-product-decision-request.md
```

## One canonical brief per initiative

Create one brief file and revise it in place throughout Product0. Do not create separate intent, requirements, design, scope, and handoff files for the same initiative.

Initial brief:

```markdown
---
product0: true
id: p0-YYYYMMDD-<slug>
title: <human-readable title>
status: captured
revision: 1
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Product0 Developer Brief: <title>

## Original request

> <preserve the user's wording>

## Product intent

_Status: pending_

## Product requirements

_Status: pending_

## Product design

_Status: pending_

## Product slices

_Status: pending_

## Developer directions

_Status: pending_

## Acceptance examples

_Status: pending_

## Risks and assumptions

_Status: pending_

## Evidence and references

_None recorded._

## Session records

_None recorded._

## Decision log

| Revision | Date | Change | Reason |
|---:|---|---|---|
| 1 | YYYY-MM-DD | Brief created | Product0 started |

## Approval record

| Stage | Revision | Approved by | Date | Evidence |
|---|---:|---|---|---|
```

## Writing rules

- Preserve the user's original request verbatim in a blockquote when practical.
- Update `updated` whenever the file changes.
- Replace pending markers; do not append duplicate versions of a section.
- Keep stable requirement IDs such as `R-01`, `R-02`.
- Keep stable product slice IDs such as `S-01`, `S-02`.
- Use relative repository paths for local references.
- Do not include implementation file paths, code snippets, schemas, or framework choices in the Product0 brief unless they are externally imposed constraints. Label such constraints explicitly.
- Do not commit files unless the user or repository policy requests a commit.
