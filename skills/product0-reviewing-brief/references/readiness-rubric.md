# Product0 handoff-readiness rubric

## 1. Intent integrity

- The brief still solves the approved problem for the approved actor.
- Success evidence measures the intended outcome.
- Requirements and design have not drifted toward a different problem.

## 2. Requirements

- Important behavior is observable.
- Business rules and permissions are explicit.
- Scope and non-goals are compatible.
- Consequential delay, duplicate, failure, cancellation, and recovery behavior is defined where relevant.
- Constraints have a source or rationale.
- No blocking product decision remains.

## 3. Product design

- The primary journey is coherent.
- Meaningful states and transitions are described from the actor's perspective.
- Information, controls, and administration are sufficient.
- Approved product trade-offs are recorded.
- Technical architecture is not prescribed accidentally.

## 4. Product slices

- Every in-scope requirement maps to a slice or is explicitly cross-cutting.
- Slices are coherent outcomes rather than engineering layers.
- Included, excluded, and dependent behavior is clear.
- Acceptance evidence exists.

## 5. Developer directions

- Fixed product decisions are unmistakable.
- Non-goals protect against scope expansion.
- Technical latitude gives the developer room to solve the code problem.
- Open technical questions are precise.
- Evaluation criteria are ordered and derived from product direction.
- The required technical-design output is clear.

## 6. Consistency and usability

- No placeholders remain.
- Terms are used consistently.
- References resolve or are clearly identified.
- Current revision approvals are valid.
- A developer can understand the brief without access to the chat transcript.

## Blocking examples

- Undefined permissions.
- Contradictory acceptance examples.
- No product-visible behavior for a permanent failure that users must act on.
- A business rule hidden under “developer discretion.”
- Product slices that omit an approved requirement.
- A fixed technology choice with no documented external constraint.

## Non-blocking examples

- Choice of queue, framework, schema, API shape, module boundary, test framework, retry algorithm, or migration mechanism, unless an approved product constraint genuinely fixes it.
