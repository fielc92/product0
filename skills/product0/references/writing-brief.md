# Writing the Product0 brief

## Preconditions and iron law

Orientation is complete, the direction challenge returned `DIRECTION_READY`,
the user explicitly approved the complete direction, and material product
decisions are resolved or recorded as non-blocking open risks.

```text
ONE APPROVED DIRECTION = ONE COHERENT BRIEF WRITE.
```

Create `docs/product0/briefs/YYYY-MM-DD-<descriptive-topic>-product-brief.md`.
For a revision, update the canonical brief in place and increment `revision`.
Do not create a placeholder, append discovery fragments, or preserve pending
headings.

## Writing standard

Lead with executive direction and important choices. Preserve provenance as
**Repository evidence**, **User-confirmed**, **Product0 recommendation**,
**Working assumption**, and **Open risk**. Select only type-appropriate
sections: marketing needs positioning, hierarchy, proof, objections, visual
direction, and conversion; workflows need actors, lifecycle, rules, authority,
and exceptions; platforms need consumers, boundaries, configuration, guarantees,
and control.

Use `references/brief-templates/marketing-surface.md` for marketing work and
`references/brief-templates/general.md` otherwise. Templates are menus, not
checklists: remove their comments and every empty, irrelevant, or duplicative
heading from the generated brief.

Avoid ceremony: use requirement IDs only when complex interacting behavior needs
traceability; use product slices only for two or more meaningful outcomes,
phases, or deferrals; omit empty sections, repeated propositions, transcripts,
and generic mechanics. When requirements or stable IDs appear, include a
non-empty `## Traceability rationale` explaining why named decisions and
section headings are insufficient. A small marketing brief above 1,800 body
words requires a non-empty `## Proportionality rationale` explaining its unique
decision value; an empty rationale heading never satisfies either rule.

When slices are present, use `### S-NN: <title>` headings and provide a prose
body for each independently meaningful outcome or release boundary. At least
two slices are required. Scale depth to the initiative; insight density matters
more than length.

Every brief needs frontmatter with current status and revision, executive
direction, repository and user context, type-appropriate product direction,
fixed decisions and non-goals, recommendations, assumptions and open risks,
success evidence and guardrails, directions for technical brainstorming, and the
developer next step.

## Developer next step

End with:

```markdown
## Developer next step

This brief is approved product direction, not an implementation specification.

A developer should read it in full and separately use `product0-using-brief`. Technical brainstorming may inspect the codebase and choose architecture, interfaces, data flow, persistence, error mechanisms, migrations, observability, and tests while preserving the fixed product direction and non-goals.

Product0 stops before technical design or implementation begins.
```

Set `status: handoff-draft`. Before saving, verify there are no pending markers,
unsupported facts, hidden material decisions, irrelevant evidence, redundant
sections, or disproportionate detail.
