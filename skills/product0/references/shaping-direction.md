# Shaping product direction

## Goal and hard gates

Operate like a senior product lead: synthesize context, choose the relevant
product lens, make recommendations, resolve consequential decisions efficiently,
and present one coherent direction for approval.

```text
DO NOT WRITE THE BRIEF DURING DISCOVERY.
DO NOT TURN A GENERIC CHECKLIST INTO THE CONVERSATION.
```

Read the orientation output and current request first. Classify the request and
load only its matching primary lens from `references/lenses/`:

- marketing or conversion surface: `marketing-surface.md`;
- feature, journey, or service flow: `product-workflow.md`;
- reusable primitive, platform, or builder capability: `platform-capability.md`;
- external system or data handoff: `integration.md`;
- plans, entitlements, or commercial offer: `pricing-packaging.md`;
- employee, support, administrator, or operational workflow: `internal-operation.md`;
- law, policy, contractual, security, or regulatory change: `compliance-change.md`;
- reliability, usability, accessibility, performance, or trust improvement:
  `product-quality.md`.

Load a secondary lens only when it materially changes the proposed outcome,
scope, authority, guardrail, or evidence. Name the combination and why each
lens is needed. Do not run every lens as a generic checklist. If the request
does not fit a named lens, state the product problem in plain language and use
the smallest useful combination as a guide rather than manufacturing a new
interview.

## Build the direction

Use the selected lens to inspect evidence, make a professional recommendation,
identify only blocking product decisions, and preserve implementation detail for
technical brainstorming. Reason through the problem, actors and situation,
outcome and strategy, important behavior or experience, scope and non-goals,
success evidence and guardrails, provenance, and technical handoff only when
the selected lens makes each relevant. Do not promote routine implementation
defaults into product strategy.

## Decision packets

Ask only when an answer could materially change product direction.

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

For a small initiative, use at most two packets unless a genuine blocker
emerges. Do not ask to fill form fields, routine UX defaults, low-risk copy, or
implementation mechanics. When the user delegates a category, choose the most
defensible low-risk option, explain it briefly, and continue. Escalate only at
the risk boundary stated in the root Product0 skill.

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

Ask the user to choose `Approve`, `Revise`, or `Park`. Do not request separate
intent, requirements, design, and scope approvals.
