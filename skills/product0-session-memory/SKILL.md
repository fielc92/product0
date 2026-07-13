---
name: product0-session-memory
description: Use when, during Product0 or pre-implementation product work, the user says remember, note this, capture this, save this, do not forget, keep track, log this, asks for a recap, or asks what was decided.
license: MIT
compatibility: Agent Skills-compatible coding agents with project file read/write access.
metadata:
  author: product0
  version: "0.2.0"
  role: cross-cutting
---

# Product0 Session Memory

## Purpose

Maintain one structured, revisable memory file for the current conversation when the user explicitly requests memory. Session memory is not an automatic discovery log and never substitutes for the final brief.

## Iron laws

```text
ONE CONVERSATION SESSION = ONE SESSION FILE.
NO MEMORY WRITE WITHOUT AN EXPLICIT WRITE INTENT.
```

After establishing the current session file, always revise it. Do not create another because the topic changes, the date changes, context is compacted, or the file becomes long.

## Intent modes

### Write or update

Triggers include:

- remember this;
- note or capture this;
- save this for later;
- do not forget;
- update or correct the session notes.

Create or revise the file.

### Read only

Triggers include:

- do you remember;
- what did we decide;
- recap this session;
- what is still open.

Read only. Do not create or modify a file unless the user also asks to save or correct it.

### Close

On “close/finalize/wrap up the session,” update the same file, set `status: closed`, and summarize. Closing does not permit a second file in the same conversation.

## Resolve the file

1. Explicit path named by the user.
2. Path already established in this conversation.
3. One unambiguous linked session for the current initiative.
4. Otherwise create a file only for an explicit write request.

If multiple candidates remain, ask the user to choose. Uncertainty must not create a duplicate.

## Create once

Use:

```text
docs/product0/sessions/YYYY-MM-DD-HHMM-<descriptive-topic>-session.md
```

Start from `assets/session-memory-template.md`. Link a Product0 brief only when one already exists. Memory must not create a brief or advance Product0 state.

## Maintain, do not dump

Integrate:

- user-stated facts and constraints;
- decisions and rationale;
- rejected alternatives;
- open questions;
- corrections and superseded statements;
- concise evidence references;
- a short update log.

Do not store hidden reasoning, secrets, credentials, unrelated personal data, or a raw transcript by default. Keep user statements, Product0 recommendations, assumptions, and open risks distinct.

After the memory action, return to the Product0 conversation state that was active beforehand.
