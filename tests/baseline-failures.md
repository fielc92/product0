# Product0 behavioral failure catalogue

## v0.1 landing-page failure

Prompt:

```text
Use Product0: we need to design a simple landing page for the app.
```

Observed failure pattern:

1. The agent created `docs/product0/briefs/...` before discovery was complete.
2. It wrote placeholder sections and revised the file after nearly every answer.
3. It asked a long sequence of basic questions that repository inspection or professional judgment could answer.
4. It did not explain the existing product or repository direction before interviewing the user.
5. It focused on form fields, validation, duplicates, retries, and confirmation states before positioning, proof, objections, visuals, or message hierarchy.
6. When the user delegated judgment, it proposed a default and asked for approval instead of deciding.
7. It promoted “likely 1%” into a fixed public commercial claim.
8. The final brief was hundreds of lines, repetitive, unsupported by repository evidence, and contained a one-item product slice that restated the whole initiative.

Root causes in v0.1:

- The orchestrator required a brief before discovery.
- “Ask one blocking question at a time” created a checklist interview.
- Stage templates rewarded field completion.
- Evals tested boundaries but not professional product quality.
- Readiness emphasized completeness rather than insight density and evidence.

## Rationalizations to reject

| Rationalization | Required correction |
|---|---|
| “Writing as we go preserves progress.” | Initial brief writing waits for approved direction; explicit session memory handles requested persistence. |
| “One question at a time is easier for the user.” | Use one consequential decision packet, not a drip-feed of obvious questions. |
| “The template requires every section.” | Omit any section that adds no decision value. |
| “The developer needs every edge case.” | Product0 resolves consequential product behavior; technical brainstorming handles routine implementation mechanics. |
| “A likely price is good enough for a demo.” | Provisional commercial claims remain assumptions or open risks until confirmed. |
| “A complete brief is necessarily long.” | Repetition and ceremonial traceability reduce usefulness. |

## v0.2 success criteria

Product0 must inspect first, explain the lay of the land, take professional initiative, ask only material questions, challenge its direction, write once after approval, and produce a concise evidence-backed handoff.
