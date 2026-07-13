---
name: product0-session-memory
description: Use when, during Product0 or pre-implementation product work, the user says remember, note this, capture this, save this, do not forget, keep track, log this, asks for a recap, or asks what was decided.
license: MIT
compatibility: Agent Skills-compatible coding agents with project file read/write access.
metadata:
  author: product0
  version: "0.1.0"
  role: cross-cutting
---

# Product0 Session Memory

## Purpose

Maintain one structured, revisable memory file for the current conversation session. Preserve decisions and useful context without fragmenting the conversation into many note files.

## Iron law

```text
ONE CONVERSATION SESSION = ONE SESSION FILE.
```

After a file is established for the current session, always revise that same file. Do not create a new file because:

- the topic changes;
- the date rolls over;
- context is compacted;
- the user adds another remembered item;
- the session is summarized or corrected;
- the file becomes long.

Create another file only when the user explicitly starts a new session, explicitly chooses a different existing session, or no session file has ever been established for the current conversation.

## Determine the user's intent

### Write or update

Examples:

- “Remember this.”
- “Note that consent is opt-in.”
- “Capture this decision.”
- “Save this for later.”
- “Don't forget the compliance constraint.”
- “Update the session notes.”
- “Correct what we recorded earlier.”

Write or revise the session file.

### Read only

Examples:

- “Do you remember what we decided?”
- “What did we say about consent?”
- “Recap the session.”
- “What is still open?”

Read the existing session file and answer. Do not create or modify a file unless the user also asks to save, correct, or update it.

### Close or finalize

Examples:

- “Close the session.”
- “Finalize the notes.”
- “Wrap up and save the recap.”

Update the same file, produce a concise final summary, set `status: closed`, and preserve the update log. Closing does not authorize creation of a new file later in the same conversation.

## Resolve the session file

Use this order:

1. A session path explicitly named by the user.
2. The session path already established in the current conversation.
3. An exact session reference recorded in the current Product0 brief and clearly associated with this conversation.
4. If context was compacted, one unambiguous active session for the same brief and topic under `docs/product0/sessions/`.
5. Otherwise, for a write request only, create a new file.

If more than one file could be the current session, ask the user to select one. Uncertainty must not create a duplicate.

## Create once

On the first write request with no established file:

1. Use `docs/product0/sessions/YYYY-MM-DD-HHMM-<descriptive-slug>-session.md`.
2. Use the project's local time if available; otherwise use the agent environment's local time.
3. Start from `assets/session-memory-template.md`.
4. Link the current Product0 brief when one exists.
5. Add the path once to the brief's `Session records` section. This metadata update does not change Product0 state or revision.
6. Tell the user the exact session path.

## Update in place

Read the whole session file before revising it. Integrate new information into the appropriate existing sections rather than appending duplicate summaries.

Preserve:

- user-stated facts and constraints;
- decisions and their rationale;
- rejected alternatives and why;
- unresolved questions;
- corrections and superseded statements;
- references to Product0 artifacts;
- a concise chronological update log.

Do not save hidden reasoning, internal chain of thought, credentials, secrets, or unrelated personal data. Do not store a raw transcript by default. Summarize faithfully and distinguish user statements, decisions, assumptions, and agent inferences.

When the user corrects a remembered item, update the authoritative section and record the correction in the update log. Do not leave contradictory active statements.

## Return to Product0

Memory is cross-cutting. After recording or answering, return to the Product0 state that was active before this skill was invoked. Memory actions never approve a stage or start development.

## Red flags

- Creating one file per “remember” instruction.
- Treating “do you remember?” as a write request.
- Appending a transcript dump instead of maintaining structured memory.
- Creating a new file after compaction because the path is uncertain.
- Advancing Product0 state because a decision was recorded in memory.
- Leaving a correction alongside the old statement as if both remain valid.
