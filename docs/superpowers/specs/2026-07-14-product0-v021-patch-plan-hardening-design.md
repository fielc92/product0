# Product0 v0.2.1 Patch-Plan Hardening Design

## Purpose

Revise the existing Product0 v0.2.1 self-contained-workflow patch plan so another agent can implement it without guessing about lens depth, brief grammar, release metadata, or behavioral-test artifact handling.

This is a targeted amendment. It preserves the existing ten-task plan and places each correction in the task that owns the affected behavior.

## Scope

The revision addresses five findings:

1. the audit expects v0.2.1 metadata, but the plan does not explicitly update every retained skill;
2. the linter recognizes traceability and proportionality rationales that the templates do not define;
3. product-slice detection assumes a syntax the writer and template do not require;
4. behavioral runs can create sensitive or large artifacts without a complete storage and sanitization contract;
5. non-marketing lenses need enough validation to prevent placeholders, while the primary feature-speccing lenses need deeper contracts.

The revision does not add a new implementation task, redesign the Product0 workflow, or expand v0.2.1 into a complete quality program for every product lens.

## 1. Tiered lens contracts

Task 3 will define three deep-contract lenses.

### Marketing surface

Retain the existing ten-marker contract covering buyer and buying situation, page job, positioning, message hierarchy, narrative, demonstration and visual direction, proof and trust, objections, conversion, measurement, and claim safety.

### Product workflow

Require stable markers for:

- actors and affected parties;
- triggering situation;
- desired product outcome;
- lifecycle or meaningful state progression;
- business rules;
- authority and permissions;
- consequential exceptions;
- success evidence and guardrails;
- scope and non-goals;
- implementation-neutral handoff boundaries.

### Platform capability

Require stable markers for:

- consumers;
- jobs or outcomes enabled;
- capability boundary;
- configuration and control;
- product-level guarantees;
- failure consequences;
- adoption and migration implications;
- success evidence and guardrails;
- scope and non-goals;
- implementation-neutral handoff boundaries.

Each deep-contract lens will have repository tests for every marker, a rule preventing direction approval while relevant product decisions remain unresolved, and an explicit boundary between product direction and later technical brainstorming.

The other five lenses are `integration`, `pricing-packaging`, `internal-operation`, `compliance-change`, and `product-quality`. Each receives a basic anti-placeholder contract:

- the file exists and contains a unique lens identifier;
- it defines evidence to inspect, recommendations to make, blocking product decisions, and implementation details that must not become interview questions;
- after frontmatter, headings, marker lines, and fenced examples are removed, it contains at least 120 prose words;
- it contains no `TBD`, `TODO`, copied marketing markers, or other placeholder content.

This weighting reflects the expected primary use: feature definition before developers begin technical brainstorming and implementation planning.

## 2. Adaptive brief grammar

Task 5 will define two conditional sections in the applicable template and writer rules.

### Traceability rationale

`## Traceability rationale` is required when `Product requirements` or stable requirement IDs are included. It explains why named decisions and section-level traceability are insufficient for the initiative.

### Proportionality rationale

`## Proportionality rationale` is required when a small marketing brief exceeds 1,800 body words. It explains what unique decision value justifies the additional length.

Empty rationale sections do not satisfy either rule.

### Product-slice grammar

Whenever product slices are present, they use this canonical form:

```markdown
## Product slices

### S-01: <independently meaningful outcome or release boundary>
```

Every slice uses `### S-NN: <title>`. At least two slices are required. Each slice describes an independently useful outcome or release boundary and cannot merely restate the whole initiative.

Task 6 aligns the reviewer and linter with the same grammar. The linter enforces structural properties such as heading form and count. The Product0 reviewer remains responsible for judging whether slices are genuinely independent.

Tests cover valid and invalid rationale sections, zero, one, and two slices, malformed slice headings, and empty rationale bodies.

## 3. Release metadata consistency

Task 7 owns the full metadata cutover because installation validation cannot pass until retained skills identify themselves as v0.2.1.

All eight retained skills report:

```yaml
metadata:
  author: product0
  version: "0.2.1"
```

Roles remain explicit:

- `product0`: `orchestrator`;
- `product0-session-memory`: `cross-cutting`;
- `product0-using-brief`: `bridge`;
- the five retained aliases: `compatibility`.

The shared parser, validator, and install audit import one `EXPECTED_VERSION = "0.2.1"` constant. They do not maintain independent release literals.

Tests assert that every expected skill reports the expected version and role, deleted sibling names are never accepted as current because of metadata alone, a root containing a current v0.2.1 `product0` plus any retained skill at another version is `mixed`, and the changelog release, validator expectation, and skill metadata agree.

Task 9 documents the release change but does not defer the metadata mutation from Task 7.

## 4. Behavioral artifact hygiene

Task 10 separates raw execution evidence from tracked release evidence.

### Raw local results

`tests/results/` is ignored by Git. It may contain:

- complete stdout and stderr;
- command traces;
- unsanitized harness payloads;
- temporary workspaces;
- intermediate extracted messages.

Raw results are local and disposable. They are never committed.

### Sanitized release records

`tests/behavioral-records/` is tracked and may contain only:

- `run.json`;
- extracted assistant messages required to support assertions;
- the generated Product0 brief;
- assertion summaries;
- fixture and commit hashes.

Before promoting an artifact into the tracked directory, the runner must:

- redact assignments and JSON/YAML fields whose case-insensitive names end in `_TOKEN`, `_API_KEY`, `_SECRET`, `_PASSWORD`, or `_CREDENTIAL`;
- redact bearer tokens and private-key blocks;
- exclude the values of matching process-environment variables and authentication output;
- reject tracked output that still contains any configured fake-secret sentinel used by the sanitization tests;
- enforce a 256 KiB limit for each tracked text artifact and a 1 MiB limit for each complete six-run release-record set;
- record whether sanitization changed the source;
- fail closed when it cannot establish that an artifact is safe.

Tracked records contain only the six release-gate runs for the current commit. Producing a new release set removes stale tracked records from prior commits. The release-gate checker reads sanitized tracked records rather than raw local results.

Task 10 modifies `.gitignore`, adds sanitization tests using fake secrets, defines retention behavior, and prohibits committing raw logs regardless of general repository policy for model-evaluation artifacts.

## 5. Integration into the ten-task plan

The amendments remain local:

- Task 3 owns tiered lens contracts and tests.
- Task 5 owns rationale headings and canonical slice grammar.
- Task 6 owns matching review and lint behavior.
- Task 7 owns the complete v0.2.1 metadata cutover and consistency tests.
- Task 9 documents the clarified contracts.
- Task 10 owns raw-versus-tracked evidence, sanitization, retention, and release-gate behavior.

The feedback-disposition table will add the five latest findings and point to their exact resolution sections. The final publish gate will additionally require:

- deep-contract tests passing for the three priority lenses;
- anti-placeholder tests passing for the other five lenses;
- all eight retained skills reporting v0.2.1;
- rationale and slice-grammar fixtures passing;
- raw behavioral results remaining untracked;
- six sanitized current-commit behavioral records passing;
- sanitization and size-limit tests passing.

## Completion criteria

The revised patch plan is ready for another implementing agent when:

- every finding above has an explicit owning task, file list, test-first instruction, verification command, and publish-gate assertion;
- no amendment introduces a new Task 11 or unrelated Product0 behavior;
- terminology for lenses, rationales, slices, skill sets, versions, and result directories is consistent throughout the plan;
- the plan contains no placeholder, unresolved choice, or instruction that depends on unstated judgment.
