# Product0 v0.2 state machine

## Conversation-first states

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

The first five states normally exist only in the conversation. Product0 does not create a project brief while orientation and discovery are incomplete.

## File transition

```text
direction-approved
  -> one atomic brief write
  -> status: handoff-draft
  -> readiness review
  -> final user approval
  -> status: handoff-ready
```

An explicit session-memory request may create or update one file under `docs/product0/sessions/` at any state. Memory does not approve direction or advance the state machine.

## Side states

- `parked` — the user intentionally pauses the initiative.
- `needs-product-decision` — technical brainstorming found a material product gap in an existing handoff-ready brief.
- `cancelled` — the user ends the initiative.

## Revision rules

When revising an existing brief:

1. Inspect the repository context affected by the change.
2. Reshape only the affected product direction.
3. Obtain explicit approval for the revised direction.
4. Increment `revision`.
5. Replace stale content rather than appending competing versions.
6. Set `status: handoff-draft`.
7. Re-run brief review and obtain final handoff approval.

Do not maintain per-stage approval tables. Preserve a concise revision summary and the current direction's provenance.
