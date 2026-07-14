# Mock RED fixture: v0.2 hybrid runtime transcript

> Fixture data only. This is a human-readable mock transcript, not a record of a real user session.

## Mock request

**User:** “Use Product0 in the running repository: we need to design a simple landing page for the app.”

## Observed old-shape routing

**Mock Product0 runtime:** The orchestrator invokes `product0-orienting-context`, then routes to the sibling stage skills `product0-shaping-direction`, `product0-challenging-direction`, and `product0-writing-brief`.

This is the stale hybrid-runtime shape represented by the fixture. The intended v0.2.1 behavior is that the root `product0` skill is self-contained and reads its core workflow modules from its own `references/` directory.

## Expected RED context

The focused repository test is expected to fail before the self-contained workflow is implemented because the five relative core reference paths are absent from `skills/product0/SKILL.md`, while the orchestrator still contains positive sibling-stage routing language.

**Expected status:** RED regression evidence only.
