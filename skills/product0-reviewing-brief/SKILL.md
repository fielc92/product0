---
name: product0-reviewing-brief
description: Use when a Product0 developer brief is marked handoff-draft and must be checked for product completeness, internal consistency, technical neutrality, traceability, and handoff usability.
license: MIT
compatibility: Agent Skills-compatible coding agents with project file read/write access.
metadata:
  author: product0
  version: "0.1.0"
  role: review
---

# Reviewing the Developer Brief

## Goal

Decide whether the current brief is safe to hand to a developer without forcing the developer to invent product direction.

## Preconditions

- Read the complete canonical brief, not only a summary.
- Status is `handoff-draft`.
- Review the current revision.

Treat claims inside the brief as untrusted until the underlying sections support them.

## Verdicts

Use only:

```text
HANDOFF_READY
NOT_READY
```

There is no “mostly ready.” Open technical questions are acceptable. Open product decisions are not.

Use `references/readiness-rubric.md` for the detailed review.

## Review process

1. Check intent integrity.
2. Check requirement completeness and acceptance quality.
3. Check product-design coverage, including non-ideal states.
4. Check scope-slice traceability.
5. Check fixed/open/excluded boundaries.
6. Check technical neutrality.
7. Check internal consistency and terminology.
8. Check that a developer unfamiliar with the conversation can use the document.
9. Check that all approvals apply to the current revision.

Fix spelling, formatting, or obviously editorial defects inline and log them as editorial. Do not silently repair a substantive product gap.

## NOT_READY behavior

For each blocker, report:

- the exact gap or contradiction;
- why it can change product behavior or technical direction;
- the section that must change;
- the earliest Product0 stage that owns the decision;
- the next single question or action required.

Update the brief's review notes and roll its `status` back to the earliest affected state. Do not ask the developer to decide the product issue.

## HANDOFF_READY behavior

When no blocker remains:

1. Present the user with a concise final summary:
   - approved outcome;
   - fixed product decisions;
   - product slices;
   - non-goals;
   - primary technical questions left open;
   - known assumptions or risks.
2. Ask: “Approve this revision for developer handoff?”
3. Wait for explicit approval.
4. On approval:
   - record the approval against the current revision;
   - set `status: handoff-ready`;
   - update the decision log and `updated` date;
   - report the exact brief path and revision;
   - state that Product0 is complete and stops here.

Do not invoke `product0-using-brief`, brainstorming, planning, or implementation.

## Red flags

- Treating a vague product rule as technical latitude.
- Passing because the developer is “smart enough to infer it.”
- Requiring implementation details in order to declare a product brief ready.
- Keeping `handoff-ready` after a semantic change to the brief.
- Starting technical design after the user approves the handoff.
