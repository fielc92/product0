# Product0 architecture

## Active state machine

```text
unoriented
  -> orienting
  -> oriented
  -> discovering
  -> direction-proposed
  -> direction-approved
  -> handoff-draft
  -> handoff-ready
  -> STOP
```

Orientation through direction approval is conversation-first. Product0 writes no project brief during those states.

## Artifact transition

```text
approved direction
  -> product0-writing-brief
  -> one coherent file under docs/product0/briefs/
  -> handoff-draft
  -> product0-reviewing-brief
  -> final approval
  -> handoff-ready
```

Session memory is an explicit cross-cutting action and never advances the state machine.

## Composition

```text
product0
  -> product0-orienting-context
  -> product0-shaping-direction
  -> product0-challenging-direction
  -> user approves direction
  -> product0-writing-brief
  -> product0-reviewing-brief
  -> STOP

Developer later:
product0-using-brief
  -> technical brainstorming
```

## Product judgment model

Product0 separates:

1. repository evidence;
2. user-confirmed direction;
3. Product0 recommendations;
4. working assumptions;
5. open risks.

This prevents provisional or inferred information from becoming false certainty.

## Product versus technical design

| Product0 | Developer technical brainstorming |
|---|---|
| Business/user problem and outcome | Architecture and components |
| Audience, actor, buyer, or operator | Internal responsibilities |
| Positioning and message hierarchy | Rendering and content implementation |
| Product behavior and business rules | Data structures and control flow |
| Product-visible failures | Error mechanisms, retry, and idempotency |
| Product constraints and non-goals | APIs, schemas, modules, migrations, and tests |
| Success evidence and guardrails | Verification and observability mechanisms |

## Compatibility

The v0.1 stage names remain discoverable as compatibility aliases but route into the v0.2 active skills. They do not create artifacts or run independent approval stages.

## v0.2.1 composition

Only product0, product0-session-memory, and product0-using-brief are active. Orientation, direction shaping, challenge, writing, and review are internal reference modules of product0, so normal workflow does not depend on sibling discovery. Five explicit aliases route to product0; five stale v0.2 siblings are installation evidence and must be removed only when the audit identifies them.
