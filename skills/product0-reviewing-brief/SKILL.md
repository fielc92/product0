---
name: product0-reviewing-brief
description: Use when a Product0 brief is marked handoff-draft and must be checked for strategic usefulness, evidence quality, provenance, proportionality, technical neutrality, and developer handoff readiness.
license: MIT
compatibility: Agent Skills-compatible coding agents with project file read/write access.
metadata:
  author: product0
  version: "0.2.0"
  role: review
---

# Reviewing the Product0 Brief

## Goal

Decide whether the written brief gives a developer high-quality product direction without forcing them to rediscover strategy or inherit fabricated certainty.

## Preconditions

- Read the complete canonical brief.
- Status is `handoff-draft`.
- Review the current revision.
- Read the source evidence referenced by the brief when available.

## Verdicts

Use only:

```text
HANDOFF_READY
NOT_READY
```

Open technical questions are acceptable. Open blocking product decisions are not.

Use `references/readiness-rubric.md`.

## Review priorities

1. **Strategic usefulness** — Is there a clear recommendation rather than a reformatted request?
2. **Evidence** — Does repository context support the direction?
3. **Provenance** — Are facts, user decisions, recommendations, assumptions, and risks distinct?
4. **Type-specific depth** — Does the selected product lens cover the questions that matter?
5. **Proportionality** — Is the brief concise relative to the initiative?
6. **Boundary** — Does it leave technical design open while resolving product direction?
7. **Developer usability** — Can a capable developer begin code-focused brainstorming without the chat transcript?

## Automatic NOT_READY conditions

- Repository access existed but the brief contains no meaningful repository evidence.
- The brief mainly restates the original request.
- A provisional claim is presented as fixed.
- Routine validation, loading, retry, or duplicate behavior dominates a strategic brief.
- The same proposition is repeated across several sections.
- Requirement IDs or product slices add ceremony without clarity.
- A marketing brief lacks audience, page job, positioning, message hierarchy, differentiation, proof, objections, visual direction, or conversion.
- A workflow brief lacks actors, lifecycle, authority, business rules, or consequential exceptions.
- The developer still has to invent a material product decision.
- The document is disproportionately long for its useful decisions.

## Review behavior

Fix obvious editorial defects and repetition inline. Do not silently repair substantive product direction.

For each blocker report:

- the exact gap;
- why it matters;
- whether Product0 can resolve it from evidence and delegated authority;
- the smallest next action.

If Product0 can resolve the issue within existing authority, revise the brief, increment the revision, and review again. Ask the user only for a decision that genuinely requires their authority.

## Handoff approval

When the brief passes:

1. Present a concise summary of:
   - executive direction;
   - strongest evidence;
   - fixed decisions;
   - Product0 recommendations;
   - assumptions and open risks;
   - questions left for technical brainstorming.
2. Ask: `Approve this written revision for developer handoff?`
3. On explicit approval:
   - set `status: handoff-ready`;
   - record the current revision and approval date in concise frontmatter or a short revision summary;
   - report the exact path;
   - stop Product0.

Do not invoke `product0-using-brief`, brainstorming, planning, or implementation.
