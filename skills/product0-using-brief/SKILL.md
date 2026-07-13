---
name: product0-using-brief
description: Use when a developer explicitly wants to begin technical design or code-focused brainstorming from a completed Product0 developer brief.
license: MIT
compatibility: Agent Skills-compatible coding agents with project file read/write access. Integrates with a technical brainstorming skill when one is installed.
metadata:
  author: product0
  version: "0.1.0"
  role: bridge
---

# Using a Product0 Brief

## Purpose

Bridge an approved Product0 brief into a separately initiated technical brainstorming workflow. This skill is developer-side. Product0 itself must never invoke it automatically.

## Hard gates

```text
DO NOT USE A BRIEF UNLESS status: handoff-ready.
DO NOT IMPLEMENT BEFORE TECHNICAL DESIGN IS APPROVED.
```

A Product0 brief is authoritative product direction, not an implementation specification.

## Start

1. Resolve the brief path from the user's request or the current conversation.
2. Read the entire file, including approval record, revision, non-goals, technical latitude, and open questions.
3. Confirm `status: handoff-ready` and that the handoff approval applies to the current revision.
4. If the brief is draft, stale, ambiguous, or missing, stop and report the exact problem. Do not code.
5. Inspect the running project and its relevant implementation context only after the brief is accepted.

## Acknowledge the contract

Before technical exploration, present:

```markdown
## Product0 brief acknowledgment

**Brief:** <path>
**Revision:** <revision>

### Fixed product direction
- <decisions and requirements that must remain true>

### Non-goals
- <explicit exclusions>

### Technical design latitude
- <areas the developer may decide>

### Open technical questions
- <questions technical brainstorming should answer>

### Technical brainstorming objective
<One sentence describing the code problem to solve>
```

This is an acknowledgment, not a request to reapprove the product direction.

## Technical brainstorming focus

Technical brainstorming should now solve:

- architecture and component boundaries;
- interfaces and data flow;
- internal state and persistence;
- integration strategy;
- error propagation, retries, recovery, idempotency, and migration;
- security, privacy, compatibility, operability, and observability mechanisms;
- testing and verification strategy;
- implementation trade-offs in the actual codebase.

It must preserve Product0 requirement IDs, fixed decisions, constraints, and non-goals.

## Invoke the technical workflow

If an available skill named `brainstorming` provides a technical design workflow, invoke it after the acknowledgment. Superpowers brainstorming is the preferred integration when installed.

Provide that workflow with:

- the brief path;
- the current revision;
- fixed product decisions;
- open technical questions;
- ordered evaluation criteria;
- the requirement IDs that the technical design must trace.

If no technical brainstorming skill is available, conduct an equivalent design-first workflow:

1. inspect relevant project context;
2. ask one technical question at a time;
3. propose meaningful technical approaches and trade-offs;
4. present a codebase-aware technical design;
5. obtain explicit design approval;
6. only then proceed to the host's implementation-planning workflow.

Do not return to general product discovery unless the brief contains a real product gap.

## Product Decision Request

When codebase evidence reveals a contradiction, infeasible requirement, or missing product rule that can materially change behavior:

1. stop technical design;
2. do not invent the answer;
3. create one decision request under `docs/product0/decisions/YYYY-MM-DD-<descriptive-slug>-product-decision-request.md` using `assets/product-decision-request-template.md`;
4. update the canonical brief to `status: needs-product-decision` and link the request;
5. explain which Product0 stage owns the decision;
6. stop until the revised brief returns to `handoff-ready`.

A preference for an easier implementation is not a contradiction. Do not use escalation to reopen settled product direction casually.

## Red flags

- Changing an opt-in product rule to opt-out for implementation convenience.
- Treating non-goals as future tasks in the same plan.
- Starting code because the Product0 brief is detailed.
- Asking broad product questions that the brief already answers.
- Quietly resolving a product ambiguity as an architecture choice.
