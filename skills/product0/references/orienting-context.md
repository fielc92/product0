# Orienting product context

## Goal

Understand the product before interviewing the user. Explain the relevant lay
of the land, grounded in repository evidence, so subsequent product work starts
from informed judgment rather than a blank template.

## Hard gates

```text
ORIENT BEFORE ASKING PRODUCT QUESTIONS.
DO NOT WRITE A PRODUCT0 BRIEF DURING ORIENTATION.
```

When repository access exists, do not ask the user for facts that can
reasonably be found there.

## Scope and process

Inspect product evidence, not code architecture. Implementation files may be
read to establish current visible behavior, terminology, or available surfaces,
but not to choose future technical design.

1. Resolve the repository root and current request.
2. Search relevant sources purposefully; do not read the whole repository.
3. Inspect, in order, existing Product0 decisions; product and business docs;
   approved design artifacts; public surfaces and flows; design and brand
   assets; relevant pricing, compliance, support, sales, or operations docs;
   recent relevant changes; then implementation only to verify visible behavior.
4. Identify the product, implied users or buyers, existing direction and
   terminology, relevant surfaces, constraints, prior decisions,
   contradictions, stale assumptions, and genuine gaps.
5. Distinguish direct evidence from inference, form a recommended framing, and
   present the lay of the land before asking a question.

Search by request terms and product synonyms. Do not inspect dependency
internals, generated files, build outputs, or unrelated infrastructure.

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

## Evidence standard and stopping rule

- Reference repository-relative paths when possible.
- State “I could not find…” instead of inventing missing context.
- Treat stale or conflicting sources as a tension, not a fact.
- Treat code as evidence of current behavior, not product authority.
- Do not treat a README slogan as validated market evidence.

Stop when you can explain the product and request in context, identify the few
decisions that matter, and make a defensible initial recommendation. More
reading after that is research theatre.
