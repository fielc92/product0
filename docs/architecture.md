# Product0 architecture

## State machine

```text
captured
  -> intent-approved
  -> requirements-approved
  -> product-design-approved
  -> scope-approved
  -> handoff-draft
  -> handoff-ready
  -> STOP
```

Cross-cutting session memory returns to the same state. `needs-product-decision`, `parked`, and `cancelled` are controlled side states.

## Artifact model

Product0 maintains one canonical developer brief per initiative. Every stage writes to a stable section in the same file and records approval against the current revision.

Semantic changes roll the brief back to the earliest affected state. Editorial changes may preserve state but must be logged.

Conversation memory is deliberately separate from the authoritative brief. It records context, rationale, rejected alternatives, corrections, and open questions. It never substitutes for stage approval.

## Product versus technical design

| Product0 | Developer technical brainstorming |
|---|---|
| Problem and outcome | Architecture and components |
| Product behavior | Internal control and data flow |
| Business rules | Data structures and persistence |
| User-visible states | Internal states and error representations |
| Product failure experience | Retry, recovery, and idempotency mechanisms |
| Permissions as behavior | Authorization implementation |
| Product slices | Engineering tasks |
| Acceptance examples | Automated test design |

The Product0 brief makes the boundary explicit through four categories:

1. Fixed product decisions.
2. Product constraints.
3. Technical design latitude.
4. Open technical questions.

## Composition

The bundle uses one public orchestrator and specialized stage skills. This keeps the user interface simple while making the internal transitions strict and testable.

```text
product0
  -> product0-framing-intent
  -> product0-defining-requirements
  -> product0-designing-experience
  -> product0-slicing-scope
  -> product0-preparing-brief
  -> product0-reviewing-brief
  -> STOP

Developer later:
product0-using-brief
  -> technical brainstorming
```
