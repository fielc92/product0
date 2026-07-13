---
name: product0-challenging-direction
description: Use when Product0 has a complete proposed direction that must be independently challenged for evidence quality, strategic depth, assumptions, proportionality, and developer usefulness before user approval.
license: MIT
compatibility: Agent Skills-compatible agents. Uses an isolated reviewer when the host supports subagents and a fresh-eyes self-review otherwise.
metadata:
  author: product0
  version: "0.2.0"
  role: review
---

# Challenging Product Direction

## Goal

Prevent polished slop from reaching the user. Challenge the proposed direction before approval and before any brief is written.

## Hard gate

```text
NO BRIEF UNTIL THE DIRECTION PASSES THIS CHALLENGE.
```

## Review mode

If the host supports isolated subagents, dispatch a fresh product critic with:

- the original request;
- the lay of the land and evidence references;
- the proposed direction;
- no hidden reasoning or unrelated conversation.

Ask for a verdict and concrete findings.

If isolated review is unavailable, pause, reread the evidence and proposal from the perspective of a skeptical senior product leader, and apply the same rubric.

## Rubric

### Problem and strategy

- Does the proposal solve the actual business or user problem?
- Does it make a meaningful strategic choice?
- Are alternatives considered where they are genuinely different?
- Is the recommendation stronger than a restatement of the request?

### Evidence

- Does repository evidence support the claims?
- Are stale or conflicting sources acknowledged?
- Are user-confirmed decisions distinct from Product0 recommendations?
- Has any provisional statement become a fixed fact?

### Product depth

- Does the selected lens cover the high-value product questions?
- For marketing work: are audience, positioning, message hierarchy, differentiation, proof, objections, visuals, and conversion addressed?
- For workflow work: are actors, lifecycle, business rules, authority, and consequential exceptions addressed?
- Is the product insight sufficient for a capable developer or designer to continue?

### Proportionality

- Are routine UX defaults dominating strategic direction?
- Are requirement IDs, state tables, or product slices actually useful?
- Is the output concise relative to the initiative?
- Is the same proposition repeated in several forms?

### Boundary

- Does the proposal avoid technical design?
- Are unresolved product decisions incorrectly delegated to developers?
- Are technical questions clearly left for later?

## Verdicts

Use only:

```text
DIRECTION_READY
REVISE
```

For `REVISE`, identify the smallest correction that fixes each issue.

Resolve non-blocking findings internally and update the proposal. Ask the user only when a blocker requires their authority under Product0's escalation rules.

## Common rejection reasons

- No repository evidence despite access.
- Template completeness without insight.
- A provisional price presented as approved.
- A simple page dominated by validation, duplicate, loading, and retry mechanics.
- A one-item product slice that restates the initiative.
- The buyer, positioning, proof, or primary objection is missing.
- The proposal is too generic to guide technical brainstorming.
