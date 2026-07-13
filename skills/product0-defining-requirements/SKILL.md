---
name: product0-defining-requirements
description: Use when Product0 intent is approved but observable behavior, business rules, permissions, scope, constraints, exceptions, acceptance examples, success measures, or guardrails remain incomplete.
license: MIT
compatibility: Agent Skills-compatible coding agents with project file read/write access.
metadata:
  author: product0
  version: "0.1.0"
  role: stage
---

# Defining Product Requirements

## Goal

Turn approved intent into a testable product-behavior contract without prescribing the implementation.

## Preconditions

- Read the entire canonical brief.
- Status is `intent-approved`.
- The approved intent is still internally consistent.

If new information changes the problem, actor, outcome, or success signal, stop and return to `product0-framing-intent`.

## Hard gate

```text
REQUIREMENTS DEFINE OBSERVABLE PRODUCT BEHAVIOR, NOT CODE STRUCTURE.
```

Do not prescribe frameworks, services, schemas, tables, endpoints, queues, classes, files, or test tools. A genuine externally imposed technical constraint may be recorded, but label its source and reason.

## Process

Ask one blocking question at a time and update the same brief in place. Resolve only what affects product behavior or the developer's constraints.

Cover:

1. actors and roles;
2. core scenarios;
3. business rules and invariants;
4. permissions and visibility;
5. included scope;
6. explicit non-goals;
7. legal, commercial, security-outcome, privacy, accessibility, platform, compatibility, operational, timing, or cost constraints;
8. product-visible failure, delay, retry, duplicate, cancellation, and recovery behavior where relevant;
9. concrete acceptance examples;
10. success measures and guardrails;
11. assumptions and open technical questions.

## Requirement format

Assign stable IDs:

```markdown
### R-01 — Export respects active filters

Given a finance operator is viewing failed payments filtered to the last 30 days,
when they export the results,
then the exported records match the currently visible filter criteria.
```

Use language a product reviewer and developer can both understand. Prefer examples over adjectives such as “easy,” “robust,” “fast,” or “scalable.”

## Classify every unknown

| Classification | Treatment |
|---|---|
| Product decision | Resolve before approval |
| Product assumption | Record only if low-impact and reversible |
| Technical design question | Deliberately leave for developer brainstorming |
| Research question | Gather evidence or mark requirements not ready |
| Out of scope | Exclude explicitly |

There must be no unlabeled uncertainty.

## Required brief content

The `Product requirements` section must contain:

- actors and permissions;
- numbered requirements with stable IDs;
- business rules;
- scope and non-goals;
- constraints;
- failure and recovery expectations;
- success measures and guardrails;
- product assumptions;
- open technical questions.

Maintain `Acceptance examples` as a separate brief section. Include representative happy paths, edge cases, and failures; do not attempt exhaustive test implementation.

## Approval gate

Before requesting approval, verify:

- every requirement traces to the approved intent;
- every important user-visible outcome is observable;
- included and excluded scope do not conflict;
- permissions are not left to developer invention;
- consequential failure behavior is defined;
- acceptance examples disambiguate the riskiest rules;
- no blocking product decision remains;
- implementation choices remain open where appropriate.

Present the requirements in readable sections, then ask for explicit approval. On approval, record it and set `status: requirements-approved`.

## Red flags

- “The developer can decide permissions.”
- “Handle errors gracefully.”
- “Make it scalable.”
- “Use best practices.”
- Requirements that name code files or internal components.
- Expanding adjacent functionality because it seems convenient.
