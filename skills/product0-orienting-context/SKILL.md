---
name: product0-orienting-context
description: Use when starting or resuming Product0 work in a project and the existing product, repository direction, user-facing surfaces, evidence, constraints, or recent changes have not yet been summarized for the current request.
license: MIT
compatibility: Agent Skills-compatible coding agents with project read access. Works with any repository search, file reading, and history tools exposed by the host.
metadata:
  author: product0
  version: "0.2.0"
  role: discovery
---

# Orienting Product Context

## Goal

Understand the product before interviewing the user. Explain the relevant lay of the land, grounded in repository evidence, so subsequent product work starts from informed judgment rather than a blank template.

## Hard gates

```text
ORIENT BEFORE ASKING PRODUCT QUESTIONS.
DO NOT WRITE A PRODUCT0 BRIEF DURING ORIENTATION.
```

When repository access exists, do not ask the user for facts that can reasonably be found there.

## Scope

Inspect product evidence, not code architecture. Implementation files may be read to establish current visible behavior, terminology, or available surfaces, but not to choose the future technical design.

Use `references/repository-orientation.md` for source priority and stopping criteria.

## Process

1. Resolve the repository root and current request.
2. Search relevant sources purposefully; do not read the whole repository.
3. Identify:
   - what the product appears to be;
   - the target users or buyers already implied;
   - existing product direction and terminology;
   - current user-facing surfaces, assets, and flows relevant to the request;
   - known commercial, legal, operational, or timing constraints;
   - prior Product0 or design decisions;
   - contradictions, stale assumptions, and genuine gaps.
4. Distinguish direct evidence from inference.
5. Form a recommended framing for the request.
6. Present the lay of the land before asking a question.
7. Hand the context to `product0-shaping-direction`.

## Required user-facing output

```markdown
## Lay of the land

### What this product appears to be
<Concise synthesis grounded in repository evidence>

### Existing direction relevant to this request
<Positioning, users, flows, constraints, or prior decisions>

### Existing surfaces and evidence
- `<relative/path>` — <what it establishes>

### Tensions and genuine unknowns
<Only uncertainties that can materially change direction>

### Product0's recommended framing
<An opinionated starting point for the product work>
```

This is analysis, not an approval request.

## Evidence standard

- Reference repository-relative paths when possible.
- State “I could not find…” instead of inventing missing context.
- Treat stale or conflicting sources as a tension, not a fact.
- Treat code as evidence of current behavior, not product authority.
- Do not treat a README slogan as validated market evidence.

## Stopping rule

Stop inspecting when you can:

1. explain the product and request in context;
2. identify the few decisions that matter;
3. make a defensible initial recommendation.

More reading after that is research theatre.

## Red flags

- Creating `docs/product0/briefs/` before presenting the lay of the land.
- Opening with “Who is the target user?” when repository docs already answer it.
- Listing files without synthesizing implications.
- Describing architecture instead of product context.
- Claiming there is no evidence after inspecting only the README.
- Asking a generic question before showing the user what Product0 already learned.
