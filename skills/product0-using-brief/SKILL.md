---
name: product0-using-brief
description: Use when a developer explicitly wants to begin technical design or code-focused brainstorming from a completed Product0 developer brief.
license: MIT
compatibility: Agent Skills-compatible coding agents with project read access. Integrates with an installed technical brainstorming skill when available.
metadata:
  author: product0
  version: "0.2.1"
  role: bridge
---

# Using a Product0 Brief

## Purpose

Bridge an approved Product0 brief into a separately initiated technical brainstorming workflow. Product0 itself never invokes this skill automatically.

## Hard gates

```text
DO NOT USE A BRIEF UNLESS status: handoff-ready.
DO NOT IMPLEMENT BEFORE TECHNICAL DESIGN IS APPROVED.
```

A Product0 brief is authoritative product direction, not an implementation specification.

## Start

1. Resolve and read the entire brief.
2. Confirm `status: handoff-ready` and the current revision.
3. Verify that repository evidence references still resolve where relevant.
4. Inspect the running project's implementation context.
5. Do not reopen product direction merely because another implementation would be easier.

## Acknowledge the contract

Before technical exploration, present:

```markdown
## Product0 brief acknowledgment

**Brief:** <path>
**Revision:** <revision>

### Fixed product direction
- <user-confirmed decisions that must remain true>

### Product0 recommendations
- <professional choices that guide but may be challenged with evidence>

### Working assumptions and open risks
- <items technical design must not mistake for facts>

### Non-goals
- <explicit exclusions>

### Technical brainstorming objective
<One sentence describing the code problem to solve>

### Open technical questions
- <questions the technical design must answer>
```

This is not a request to reapprove the product.

## Technical brainstorming focus

Technical brainstorming may decide:

- architecture and component boundaries;
- interfaces and data/control flow;
- internal state and persistence;
- integrations;
- validation and internal error mechanisms;
- retries, recovery, idempotency, and migration;
- security, privacy, compatibility, operability, and observability mechanisms;
- testing and verification;
- implementation trade-offs in the actual codebase.

It must preserve fixed product direction and non-goals. Treat Product0 recommendations and working assumptions according to their provenance rather than as immutable requirements.

## Invoke the technical workflow

If a technical `brainstorming` skill is installed, invoke it after acknowledgment. Superpowers brainstorming is the preferred integration when available.

Provide:

- brief path and revision;
- fixed decisions;
- Product0 recommendations;
- working assumptions and open risks;
- non-goals;
- technical brainstorming objective;
- evaluation criteria or success guardrails.

If no brainstorming skill exists, run an equivalent design-first conversation. Do not implement until the technical design is approved.

## Product Decision Request

When codebase evidence exposes a contradiction, infeasible fixed decision, or missing product rule that materially changes behavior:

1. stop technical design;
2. do not invent the answer;
3. create `docs/product0/decisions/YYYY-MM-DD-<slug>-product-decision-request.md` from `assets/product-decision-request-template.md`;
4. update the brief to `status: needs-product-decision`;
5. explain the evidence and recommended product options;
6. stop until Product0 returns the brief to `handoff-ready`.

A preference for an easier implementation is not a product gap.

## Red flags

- Treating a Product0 recommendation as an immutable user requirement.
- Treating a working assumption as a fact.
- Reopening fixed direction for implementation convenience.
- Asking broad product questions the brief already answers.
- Starting implementation because the brief is detailed.
