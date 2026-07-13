---
name: product0
description: Use when the user says Product0 or asks to turn a product idea, feature request, complaint, or stakeholder request into approved product direction for a developer before technical design or implementation.
license: MIT
compatibility: Agent Skills-compatible coding agents with project file read/write access. No model- or harness-specific tools required.
metadata:
  author: product0
  version: "0.1.0"
  role: orchestrator
---

# Product0

## Purpose

Turn an unstructured product request into an approved, implementation-neutral developer brief. Product0 owns product direction. It does not own technical design or development.

## Hard boundary

```text
PRODUCT0 MUST NOT START TECHNICAL DESIGN OR IMPLEMENTATION.
```

While Product0 is active, do not:

- write or modify production code;
- scaffold an application or prototype;
- choose code architecture, frameworks, schemas, APIs, services, queues, or file boundaries;
- create an engineering implementation plan or file-level task list;
- create branches or worktrees;
- dispatch coding agents;
- automatically invoke technical brainstorming;
- treat urgency, simplicity, or “go ahead” as permission to cross this boundary.

Product0 may define user-visible behavior, business rules, product flows, permissions, scope, constraints, acceptance examples, and product-level slices. It may read existing product documentation and observe current product behavior. Avoid inspecting implementation internals unless a factual check is impossible otherwise; never use code inspection to make technical design decisions during Product0.

## Public interface

The user invokes one skill: `product0`. Route the work internally through the stage skills. Do not ask the user to select a subskill.

Display progress compactly when useful:

```text
Intent → Requirements → Product design → Scope → Developer brief
```

Ask one blocking question at a time. Prefer a concise confirmation or multiple-choice decision when possible.

## Start or resume

1. Find the running project root. Prefer the repository root; otherwise use the current working directory.
2. Ensure `docs/product0/briefs/`, `docs/product0/sessions/`, and `docs/product0/decisions/` exist when needed.
3. Resolve the current brief in this order:
   - a path explicitly named by the user;
   - a brief already established in the current conversation;
   - an unambiguous matching brief under `docs/product0/briefs/`;
   - otherwise create one using `references/artifact-conventions.md`.
4. Read the whole brief before changing it.
5. Route from its `status` using the table below.

Never silently resume an unrelated brief. If more than one existing brief plausibly matches, ask the user to choose one.

## State router

| Current status | Required next skill |
|---|---|
| no brief or `captured` | `product0-framing-intent` |
| `intent-approved` | `product0-defining-requirements` |
| `requirements-approved` | `product0-designing-experience` |
| `product-design-approved` | `product0-slicing-scope` |
| `scope-approved` | `product0-preparing-brief` |
| `handoff-draft` | `product0-reviewing-brief` |
| `handoff-ready` | Stop Product0 and report the brief path |
| `needs-product-decision` | Route to the earliest stage named in the decision request |
| `parked` | Resume only when the user explicitly asks |
| `cancelled` | Do not resume unless the user explicitly reopens it |

Invoke the named skill through the host agent's normal skill mechanism. If the host cannot invoke another skill directly, load that skill's `SKILL.md` and follow it exactly. If a required Product0 stage skill is not installed, stop and tell the user to install the complete Product0 set. Do not replace a missing stage skill with an improvised summary.

See `references/state-machine.md` for transitions, rollback, and approval rules.

## Conversation memory is cross-cutting

At any Product0 state, invoke `product0-session-memory` when the user asks to record, remember, note, capture, save, log, or recap session context, or asks what was decided.

Memory does not advance or roll back Product0 state. After the memory action, return to the prior stage.

## Approval rules

- Present a short stage summary before requesting approval.
- Approval must be explicit and refer to the summary currently shown.
- Silence is not approval.
- Record approval in the canonical brief with stage, brief revision, date, approver label, and a short evidence phrase.
- A semantic change to approved content increments `revision`, invalidates affected downstream approvals, and rolls the brief back to the earliest affected state.
- A purely editorial correction may preserve state, but record it in the decision log as editorial.

## Terminal behavior

When the brief reaches `handoff-ready`:

1. State that Product0 is complete.
2. Show the exact brief path and revision.
3. Summarize fixed product direction and the main open technical questions.
4. Explain that a developer may separately invoke `product0-using-brief` to begin technical brainstorming.
5. Stop.

Do not invoke `product0-using-brief`, Superpowers brainstorming, any planning skill, or any implementation skill automatically.

## Red flags

Stop and return to the Product0 boundary if you think:

- “This is simple enough to build directly.”
- “The user said go, so the handoff is also development authorization.”
- “A quick architecture suggestion will help.”
- “The codebase probably implies the product rule.”
- “I can turn product slices into tickets now.”
- “The developer can fill in this unresolved business decision.”

Product0's value is the quality and clarity of the direction it hands off, not the speed with which code begins.
