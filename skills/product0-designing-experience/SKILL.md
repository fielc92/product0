---
name: product0-designing-experience
description: Use when Product0 requirements are approved but product journeys, states, interactions, information, product-level alternatives, or user-visible failure and recovery behavior still need design.
license: MIT
compatibility: Agent Skills-compatible coding agents with project file read/write access.
metadata:
  author: product0
  version: "0.1.0"
  role: stage
---

# Designing the Product Experience

## Goal

Resolve how the product should behave and feel from the actor's perspective while leaving code problem-solving to the developer.

## Preconditions

- Read the whole canonical brief.
- Status is `requirements-approved`.
- Requirements contain no blocking product decision.

## Boundary

Product0 product design covers:

- user and operator journeys;
- entry points and triggers;
- visible states and transitions;
- actions available in each state;
- information shown and when;
- permissions as experienced by users;
- empty, loading, delayed, success, partial-success, failure, and recovery states;
- administration and product controls;
- product-level trade-offs.

It does not cover:

- system architecture;
- data models or storage layout;
- internal component boundaries;
- API shape;
- queue or event design;
- framework or vendor selection;
- implementation error types;
- automated test structure.

Classify those as technical questions for the developer brief.

## Process

1. Map the primary end-to-end journey.
2. Identify meaningful product states and transitions.
3. Identify information and controls required at each point.
4. Resolve non-ideal conditions visible to users or operators.
5. Propose two or three viable product approaches when a meaningful product trade-off exists.
6. Lead with a recommendation and explain it against the approved intent and constraints.
7. Present the design in digestible sections and obtain explicit approval.
8. Update the same brief and set `status: product-design-approved`.

Do not manufacture alternatives when there is no real product choice. A short design is acceptable for a simple initiative, but the approval gate is not optional.

## Required brief content

```markdown
## Product design

### Primary journey
<End-to-end experience>

### Entry points and triggers
<How behavior begins>

### Product states
<State, meaning, visible information, available actions>

### Interaction and information rules
<What actors can do and what the product communicates>

### Non-ideal states
<Empty, delayed, duplicate, partial, failed, cancelled, and recovery behavior as relevant>

### Administration and controls
<Product-level configuration and oversight>

### Alternatives considered
<Approaches and product trade-offs>

### Approved product approach
<Choice and rationale>
```

## Approval gate

The product design is approvable when:

- every approved requirement has a coherent place in the journey or state model;
- users and operators are not left guessing in important non-ideal states;
- the design does not silently add out-of-scope capabilities;
- product decisions are explicit;
- technical decisions remain open;
- the user explicitly approves the presented design.

Record approval and the selected alternative in the decision log.

## Red flags

- Choosing a queue because delivery is asynchronous.
- Defining database status values instead of product-visible states.
- Turning a UI mockup into an unapproved business rule.
- Ignoring operator or support experience where the requirements depend on it.
- Reopening approved intent simply because another experience is easier to implement.
