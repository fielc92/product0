---
name: product0-preparing-brief
description: Use when Product0 intent, requirements, product design, and scope slices are approved and must be compiled into implementation-neutral directions for a developer's technical brainstorming.
license: MIT
compatibility: Agent Skills-compatible coding agents with project file read/write access.
metadata:
  author: product0
  version: "0.1.0"
  role: stage
---

# Preparing the Developer Brief

## Goal

Turn the approved Product0 content into one coherent, self-contained handoff that lets a developer focus technical brainstorming on code problems rather than rediscovering product direction.

## Preconditions

- Read the entire canonical brief.
- Status is `scope-approved`.
- All earlier stages are explicitly approved at the current revision.

## Hard boundary

```text
COMPILE DIRECTIONS; DO NOT CREATE AN IMPLEMENTATION PLAN.
```

Do not add code architecture, file paths, schemas, endpoints, framework choices, engineering tasks, estimates, branches, or build instructions. Do not invoke technical brainstorming.

## Process

1. Preserve approved intent, requirements, design, and slices without changing their meaning.
2. Remove duplicate explanations and resolve inconsistent terminology.
3. Build the `Developer directions` section described below.
4. Ensure every requirement ID appears in at least one product slice or is explicitly cross-cutting.
5. Ensure fixed product decisions are distinct from open technical questions.
6. Run the self-review checklist.
7. Update the existing brief in place; do not create a second handoff file.
8. Set `status: handoff-draft` and update the decision log.
9. Invoke `product0-reviewing-brief` next. Do not invoke any technical or implementation skill.

Use `assets/product-brief-template.md` as the target shape. Adapt the detail to the initiative; do not add empty ceremonial sections.

## Developer directions

The brief must state:

### Objective

The approved product outcome the technical design must enable.

### Fixed product decisions

Approved decisions the developer must preserve. A developer may challenge a contradiction, but may not silently replace a fixed decision with an easier implementation.

### Product constraints

External requirements that materially bound technical design, with their source or rationale.

### Non-goals

Adjacent work the technical design must not absorb.

### Technical design latitude

Areas where the developer is free to choose architecture, interfaces, data flow, tools, component boundaries, error mechanisms, migration strategy, and test design.

### Open technical questions

The precise code and system design questions technical brainstorming should answer. Phrase these as questions, not disguised recommendations.

### Evaluation criteria

An ordered list for comparing technical approaches, such as simplicity, behavioral correctness, compatibility, operability, security, maintainability, cost, or performance. Derive the order from the approved product direction.

### Required technical-design output

Require the developer to produce:

- two or three viable technical approaches when alternatives are meaningful;
- a recommendation with trade-offs;
- codebase-aware architecture and component boundaries;
- data and control flow;
- error, recovery, migration, compatibility, security, and observability implications where relevant;
- a testing and verification strategy;
- traceability to Product0 requirement IDs;
- explicit Product Decision Requests for any blocking product gap.

## Standard next-step contract

End the brief with:

```markdown
## Developer next step

This brief is product direction, not an implementation specification.

A developer should read it in full and separately initiate `product0-using-brief` to begin technical brainstorming. Technical brainstorming should inspect the running project and solve architecture and implementation problems while preserving the fixed product decisions, requirements, constraints, and non-goals here.

Product0 stops before that workflow begins.
```

## Self-review

Before marking `handoff-draft`, check:

- no `TBD`, `TODO`, placeholder, or unlabeled ambiguity remains;
- terminology is consistent;
- approved sections do not contradict one another;
- no implementation choice was accidentally fixed;
- product constraints are distinguishable from preferences;
- every open product decision has been resolved;
- technical questions are genuinely technical;
- the brief can be understood without the preceding conversation;
- the brief points to any relevant session records and evidence.

Fix editorial problems inline. Route substantive contradictions to the earliest affected Product0 stage.
