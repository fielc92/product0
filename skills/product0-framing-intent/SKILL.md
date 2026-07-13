---
name: product0-framing-intent
description: Use when Product0 has a raw idea, feature request, complaint, or proposed solution but no approved product problem, primary actor, desired outcome, reason to act, or success signal.
license: MIT
compatibility: Agent Skills-compatible coding agents with project file read/write access.
metadata:
  author: product0
  version: "0.1.0"
  role: stage
---

# Framing Product Intent

## Goal

Convert the raw request into an approved statement of the product problem and desired outcome. Do not design the solution yet.

## Preconditions

- A canonical Product0 brief exists.
- Its status is `captured`, or a semantic intent change rolled it back to `captured`.
- Read the full brief before asking a question.

## Hard gate

```text
NO REQUIREMENTS, PRODUCT DESIGN, OR TECHNICAL DESIGN BEFORE INTENT APPROVAL.
```

A requested feature or technology is not automatically the intent.

Examples:

- “Add CSV export” is a proposed capability.
- “Use Kafka” is a proposed technical solution.
- “Customers need to reconcile filtered failed payments offline” is product intent.

## Process

1. Preserve the original request in the brief.
2. Infer what is already reasonably clear, but label inference as a proposed interpretation.
3. Ask one blocking question at a time.
4. Prefer confirmation choices when they reduce effort for the user.
5. Resolve:
   - the problem;
   - the primary actor;
   - the desired outcome;
   - why the work matters now;
   - observable evidence of success;
   - one meaningful non-goal.
6. Present a concise intent summary and ask for explicit approval.
7. On approval, update the same brief and set `status: intent-approved`.

Do not interrogate the user for information that does not affect product direction. Keep small initiatives small.

## Required brief content

```markdown
## Product intent

**Problem**
<What is difficult, risky, expensive, confusing, or impossible today?>

**Primary actor**
<Who experiences the problem or receives the outcome?>

**Desired outcome**
<What should become possible or materially better?>

**Why now**
<What event, risk, opportunity, or dependency makes this timely?>

**Evidence of success**
<What observable result would show the product problem was solved?>

**Non-goal**
<What adjacent result is deliberately not being pursued?>

**Approved intent statement**
We are solving <problem> for <actor> so that <outcome>, and we will know it succeeded when <evidence>.
```

## Approval gate

Intent is approvable only when:

- there is one primary problem;
- the primary actor is identifiable;
- the outcome is stated without depending on a specific implementation;
- success is observable;
- the non-goal narrows the work meaningfully;
- the user explicitly approves the displayed statement.

Record the approval and append a decision-log entry. Do not advance on silence or a vague topic change.

## Red flags

- Accepting a technology as a requirement without an external constraint.
- Treating “the user asked for it” as the problem.
- Writing acceptance criteria before the outcome is understood.
- Solving several independent product problems in one intent statement.
- Asking about frameworks, databases, endpoints, files, or architecture.

If the request contains several independent outcomes, propose decomposition and frame only the first coherent initiative.
