---
name: product0-shaping-direction
description: Use when Product0 has oriented to the product and must turn a request into an opinionated, evidence-aware product direction without writing a brief or entering technical design.
license: MIT
compatibility: Agent Skills-compatible conversational agents. No harness-specific tools required.
metadata:
  author: product0
  version: "0.2.0"
  role: discovery
---

# Shaping Product Direction

## Goal

Operate like a senior product lead: synthesize context, choose the relevant product lens, make recommendations, resolve consequential decisions efficiently, and present one coherent direction for approval.

## Hard gates

```text
DO NOT WRITE THE BRIEF DURING DISCOVERY.
DO NOT TURN A GENERIC CHECKLIST INTO THE CONVERSATION.
```

Read the orientation output and current request first. Use `references/product-lenses.md` selectively; it is a reasoning aid, not a form to complete.

## Classify the request

Choose the primary lens:

- marketing or conversion surface;
- product workflow;
- platform capability;
- integration;
- pricing or packaging;
- internal operation;
- compliance-driven change;
- product quality or usability;
- another clearly named product problem.

Use secondary lenses only when they materially affect the result.

## Build the direction

Reason through, as relevant:

1. the business or user problem;
2. the actor, buyer, operator, or affected party;
3. the situation in which the need occurs;
4. the product outcome and strategic choice;
5. the important behavior, message, or experience;
6. differentiation, proof, trust, objections, and risk;
7. scope and meaningful non-goals;
8. success evidence and guardrails;
9. fixed decisions, recommendations, assumptions, and open risks;
10. the exact territory left for technical brainstorming.

Do not promote routine implementation defaults into product strategy.

## Decision packets

Ask only when the answer could materially change the product direction.

A decision packet:

```markdown
## Decision: <consequential topic>

**Product0 recommendation**
<Choice and rationale>

**What supports it**
<Repository evidence, user statement, or explicit assumption>

**Why it matters**
<How alternatives change audience, scope, behavior, risk, or success>

**Your input**
<One compact choice or correction; up to three tightly related decisions>
```

For a small initiative, use at most two decision packets unless a genuine blocker emerges.

Do not ask questions merely to fill:

- form fields;
- standard validation behavior;
- generic accessibility expectations;
- routine loading and error states;
- low-risk copy details;
- implementation mechanics.

Use sensible defaults and record them later as Product0 recommendations when they matter.

## Delegated authority

When the user delegates a category of decisions:

1. choose the most defensible low-risk option;
2. explain it briefly;
3. continue without asking for approval.

Escalate a decision only when it crosses the risk boundary defined by the `product0` orchestrator. “I prefer the agent to decide” is not ambiguity.

## Direction proposal

After discovery, present a complete recommendation scaled to the initiative:

```markdown
# Proposed product direction

## Executive recommendation
<Answer-first direction>

## Evidence and context
<What the repository and user established>

## Product strategy
<Type-appropriate direction using the selected lens>

## Experience or behavioral direction
<Only meaningful product-level behavior>

## Scope and non-goals
<Boundaries>

## Decisions and provenance
- **User-confirmed:** ...
- **Product0 recommendation:** ...
- **Working assumption:** ...
- **Open risk:** ...

## Directions for technical brainstorming
<What the developer should solve later, without solving it now>
```

A simple initiative can be concise. It must still contain insight.

Ask the user to choose:

```text
Approve
Revise
Park
```

Do not request separate intent, requirements, design, and scope approvals.

## Quality bar

The proposal must:

- reveal implications the raw request did not state;
- use repository context rather than restating the prompt;
- prioritize decisions over exhaustive edge cases;
- make Product0's judgment visible;
- remain implementation-neutral;
- be proportionate to the initiative.

## Red flags

- Asking “why now?” as a ritual when the timing is obvious.
- Asking the user to choose a standard field set after they delegated it.
- Spending more time on duplicate submissions than positioning or business value.
- Treating every page as a state machine.
- Producing requirement IDs for a simple content decision.
- Manufacturing three alternatives that are not meaningfully different.
- Restating the same direction under multiple headings.
