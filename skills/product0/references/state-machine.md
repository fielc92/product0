# Product0 state machine

## States

| State | Meaning | Authoritative content required |
|---|---|---|
| `captured` | A raw request and canonical brief exist | Original request |
| `intent-approved` | The product problem and outcome are approved | Intent section |
| `requirements-approved` | Observable product behavior and boundaries are approved | Intent + requirements |
| `product-design-approved` | Product experience and behavioral trade-offs are approved | Intent + requirements + product design |
| `scope-approved` | Product-level capability slices are approved | Prior sections + slices |
| `handoff-draft` | Developer directions have been compiled | Complete draft brief |
| `handoff-ready` | Independent readiness review passed | Current revision approved for handoff |
| `needs-product-decision` | Technical or product review found a blocking product gap | Product Decision Request |
| `parked` | Work is intentionally paused | Reason and resumption condition |
| `cancelled` | Work is intentionally abandoned | Reason |

There is no Product0 state for technical design, implementation planning, build authorization, coding, or delivery.

## Legal forward transitions

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

`product0-session-memory` may run from any state and returns to the same state.

## Rollback table

When approved content changes semantically, increment `revision` and move to the earliest affected state:

| Changed content | New status | Invalidated approvals |
|---|---|---|
| Original request or product intent | `captured` | intent and everything downstream |
| Requirements, business rules, scope boundary, constraints, acceptance behavior | `intent-approved` | requirements and everything downstream |
| Product journey, visible states, interactions, information, failure experience | `requirements-approved` | product design and everything downstream |
| Product slice boundaries or release composition | `product-design-approved` | scope and everything downstream |
| Developer directions, technical latitude, open technical questions, evaluation criteria | `scope-approved` | handoff draft/readiness |
| Readiness-review wording only, with no meaning change | preserve current state | none; log editorial change |

If a developer raises a Product Decision Request, set `status: needs-product-decision` and record which stage owns the answer. Once resolved, return to that stage's normal approval flow.

## Approval record

Use a table in the canonical brief:

```markdown
| Stage | Revision | Approved by | Date | Evidence |
|---|---:|---|---|---|
| Intent | 2 | user | 2026-07-13 | “Approved” after intent summary |
```

Use the local calendar date in ISO format. Do not invent a person's identity; `user` is sufficient unless the user provides a name or role.

## Revision rules

- Start at revision 1.
- Increment for semantic changes to authoritative brief content.
- Do not create a new brief file for each revision.
- Keep revision history in the decision log.
- Session-memory updates do not increment the brief revision unless they also change authoritative brief content.
