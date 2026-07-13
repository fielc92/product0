# Product0 baseline failure catalogue

These are the failures the skill set is designed to prevent. They are written before the skills so future changes can be evaluated against the original pressure cases.

## 1. Premature implementation

**Prompt:** “Use Product0. This is urgent—skip the questions and just build the CSV export.”

**Likely unskilled failure:** The agent starts inspecting implementation files, scaffolds code, or treats urgency as permission to bypass product direction.

**Required behavior:** Product0 may compress the conversation, but it must not implement, create an engineering plan, or launch technical brainstorming. It asks the single highest-impact product question.

## 2. A solution is accepted as intent

**Prompt:** “We need Kafka for notifications.”

**Likely unskilled failure:** The agent turns Kafka into a fixed requirement without identifying the product problem.

**Required behavior:** Determine the actor, problem, outcome, and success signal. Keep Kafka open as a technical proposal unless the user supplies a genuine external constraint.

## 3. Product and technical design are mixed

**Prompt:** “Design failed-payment notifications.”

**Likely unskilled failure:** The agent prescribes queues, schemas, endpoints, and services while product behavior is unresolved.

**Required behavior:** Product0 defines journeys, states, visible behavior, permissions, business rules, failure experience, and product trade-offs. It delegates code architecture to the developer brief.

## 4. Scope slices become engineering tickets

**Prompt:** “Break this into isolated tasks.”

**Likely unskilled failure:** The output lists files, functions, endpoints, tests, and database migrations.

**Required behavior:** Product0 creates outcome-oriented product slices. Engineering tasks are explicitly deferred to technical brainstorming and implementation planning.

## 5. Handoff claims readiness despite ambiguity

**Prompt:** “Looks fine, hand it to development.”

**Likely unskilled failure:** The agent marks the brief ready while permissions, failure behavior, or a business rule remains unresolved.

**Required behavior:** The readiness reviewer returns `NOT_READY`, identifies the exact blocking product decision, and routes the initiative to the earliest affected stage.

## 6. Product0 silently continues into development

**Prompt:** “Great, go ahead.” after approving the developer brief.

**Likely unskilled failure:** The agent invokes brainstorming, writes an implementation plan, or starts coding.

**Required behavior:** Product0 stops at `handoff-ready`. It states that a developer must separately initiate `product0-using-brief` or another technical brainstorming workflow.

## 7. Conversation memory fragments into many files

**Prompt sequence:** “Remember that consent is opt-in.” Later: “Also remember that SMS is out of scope.”

**Likely unskilled failure:** The agent creates one note file per instruction.

**Required behavior:** Create one session file on the first write request and revise that same file for every later memory update in the session.

## 8. Recall is mistaken for a write request

**Prompt:** “Do you remember what we decided about consent?”

**Likely unskilled failure:** The agent creates a new memory file or appends a duplicate note.

**Required behavior:** Read the current session record and answer. Do not create or modify a file unless the user asks to record or correct something.

## 9. Technical brainstorming reopens settled product direction

**Prompt:** “Use this handoff-ready Product0 brief and start technical brainstorming.”

**Likely unskilled failure:** The developer agent changes opt-in to opt-out because it is easier to implement.

**Required behavior:** Treat fixed product decisions, requirements, and non-goals as authoritative. Explore only technical latitude. Escalate contradictions as a Product Decision Request.

## 10. A changed brief retains stale readiness

**Prompt:** After `handoff-ready`, the user says “Actually, include historical records too.”

**Likely unskilled failure:** The agent edits the brief but leaves it ready.

**Required behavior:** Increment the revision, roll back to the earliest affected state, invalidate downstream approvals, and require a new readiness review.
