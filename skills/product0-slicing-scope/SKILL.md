---
name: product0-slicing-scope
description: Use when Product0 product design is approved but the work still needs coherent product capability boundaries, release slices, dependencies, or deferrals before developer handoff.
license: MIT
compatibility: Agent Skills-compatible coding agents with project file read/write access.
metadata:
  author: product0
  version: "0.1.0"
  role: stage
---

# Slicing Product Scope

## Goal

Separate the approved direction into coherent product outcomes that a developer can understand and later translate into engineering work.

## Preconditions

- Read the full canonical brief.
- Status is `product-design-approved`.
- Product behavior is approved.

## Hard boundary

```text
PRODUCT SLICES ARE NOT ENGINEERING TASKS.
```

Do not list files, functions, endpoints, database changes, classes, migrations, test suites, commits, or implementation sequence. Those belong to technical brainstorming and implementation planning.

## Slice quality

A good product slice:

- delivers one understandable user or operational outcome;
- groups behavior that must remain coherent;
- has explicit included and excluded behavior;
- references requirement IDs;
- identifies product-level dependencies;
- has acceptance evidence;
- can be deferred without making another slice's meaning ambiguous.

A slice need not be independently deployable. It must be independently understandable and reviewable.

## Process

1. Trace every approved requirement to a proposed slice.
2. Group by coherent outcome, not technical layer.
3. Make dependencies and release order explicit only where product logic requires them.
4. Identify what belongs in the first release and what is deferred, if release slicing matters.
5. Check that no slice contains unrelated outcomes.
6. Present the slice set and ask for explicit approval.
7. Update the same brief and set `status: scope-approved`.

## Required format

```markdown
### S-01 — Notification consent

**Outcome**
Customers can control whether they receive failed-payment notifications.

**Included behavior**
- View current consent state.
- Opt in and opt out.
- Receive confirmation of the change.

**Excluded behavior**
- Delivering a notification.
- Editing message content.

**Requirements covered**
R-03, R-04, R-05

**Dependencies**
Customer identity and a usable contact channel already exist.

**Acceptance evidence**
Reference the relevant approved examples.
```

## Approval gate

Before approval, verify:

- every in-scope requirement maps to at least one slice;
- no requirement is accidentally dropped or duplicated inconsistently;
- slices describe outcomes rather than architecture;
- dependencies are product-relevant and explicit;
- deferrals agree with non-goals and the approved design;
- the user explicitly approves the slice set.

Record approval and any release-boundary decision.

## Red flags

- “Backend task,” “frontend task,” or “database task.”
- One slice per technical layer.
- Acceptance evidence that only says “tests pass.”
- A slice whose outcome cannot be explained without implementation details.
- Adding a technical enabler as a product slice with no product outcome.
