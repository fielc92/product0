# Product0 v0.2.1 Recovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Recover the incomplete v0.2.1 implementation beginning at Task 6, then execute the accepted Tasks 7--10 without losing the verified commits through `9dbefc6`.

**Architecture:** Task 6 adds a small standard-library Markdown linter whose findings are deterministic and whose semantic complement remains the Product0 reviewer rubric. The remaining distribution, bridge, release-documentation, and behavioral-harness work is performed as isolated, validated commits using the accepted patch plan at `/Users/friedrich/Projects/skills/product0/.tmp/product0-v0.2.1-self-contained-workflow-patch-plan.md` as the detailed contract for Tasks 7--10.

**Tech Stack:** Python 3 standard library, `unittest`, Markdown, JSON, Git.

## Global Constraints

- Preserve all committed work through `9dbefc6`; modify no completed task unless a focused test proves a direct contract violation.
- Delete the four uncommitted Task 6 attempt files before writing the RED suite: `scripts/lint_brief.py`, `skills/product0/references/readiness-rubric.md`, and the pending edits to `reviewing-brief.md` and `tests/test_repository.py`.
- Use `python3` where `python` is unavailable; all commands named `python` in the accepted patch plan mean Python 3.
- A structural linter never replaces semantic `HANDOFF_READY` / `NOT_READY` review.
- Run explicit test modules; do not accept bare `unittest discover` output of zero tests as validation.
- Update `.superpowers/sdd/progress.md` only after each successful commit with SHA, commands, and genuine environment-gated skips.
- No subagent handoffs in this recovery.

---

## File map

| File | Responsibility |
| --- | --- |
| `scripts/lint_brief.py` | CLI, Markdown normalization, deterministic findings, human/JSON rendering, exit codes. |
| `tests/test_brief_lint.py` | Black-box CLI and finding-code contract tests. |
| `tests/fixtures/briefs/*.md` | Small, readable examples that isolate each linter rule. |
| `skills/product0/references/readiness-rubric.md` | Semantic reviewer rules using stable IDs. |
| `skills/product0/references/reviewing-brief.md` | Directs review to the rubric and scopes the linter. |
| `tests/test_repository.py` | Repository-level stable-rule and later distribution/bridge/release contracts. |

### Task 6: Recover deterministic brief-shape QA

**Files:**
- Delete: uncommitted `scripts/lint_brief.py`
- Delete: uncommitted `skills/product0/references/readiness-rubric.md`
- Revert: uncommitted hunks in `skills/product0/references/reviewing-brief.md`
- Revert: uncommitted hunks in `tests/test_repository.py`

- [ ] **Step 1: Confirm the recovery boundary**

Run: `git log --oneline -6 && git status --short`

Expected: `9dbefc6` is the newest feature commit; only the four Task 6 paths are uncommitted.

- [ ] **Step 2: Remove only those uncommitted paths/hunks**

Run: `git restore skills/product0/references/reviewing-brief.md tests/test_repository.py && rm scripts/lint_brief.py skills/product0/references/readiness-rubric.md`

Expected: `git status --short` contains no Task 6 code or test changes. Do not reset, checkout, or alter committed files.

#### Task 6.1: Write RED fixtures and CLI tests

**Files:**
- Create: `tests/test_brief_lint.py`
- Create: `tests/fixtures/briefs/good-small-marketing.md`
- Create: `tests/fixtures/briefs/bad-one-item-slice.md`
- Create: `tests/fixtures/briefs/bad-malformed-slice-heading.md`
- Create: `tests/fixtures/briefs/bad-empty-traceability-rationale.md`
- Create: `tests/fixtures/briefs/bad-empty-proportionality-rationale.md`
- Create: `tests/fixtures/briefs/bad-repeated-decisions.md`
- Create: `tests/fixtures/briefs/bad-overlong-small-marketing.md`
- Modify: `tests/test_repository.py`

**Interfaces:**
- Consumes: `python3 scripts/lint_brief.py --type TYPE --size SIZE --format human|json BRIEF.md`.
- Produces: subprocess assertions of `returncode` and `{\"findings\":[{\"code\":...,\"level\":...}]}`.

- [ ] **Step 1: Add repository RED assertion**

Add `test_review_rubric_contains_slop_rules` asserting all 14 exact IDs from accepted-plan section 6.1, including `SL01_REPOSITORY_EVIDENCE_MISSING` through `SL08_BUSINESS_CONTEXT_STILL_MISSING` and `MSR01_MESSAGE_HIERARCHY_MISSING` through `MSR06_CONVERSION_STRATEGY_MISSING`.

- [ ] **Step 2: Add black-box linter tests**

In `tests/test_brief_lint.py`, run the script with `subprocess.run(..., text=True, capture_output=True)`. Assert: good fixture exits 0; one-item returns `BRIEF_ONE_ITEM_SLICE`; malformed headings return `BRIEF_MALFORMED_SLICE_HEADING`; empty traceability returns both required codes; empty proportionality returns both required codes; repeated fixture returns `BRIEF_REPEATED_DECISION`; overlong fixture returns `BRIEF_DISPROPORTIONATE_LENGTH`; rationale permits requirements; human/JSON codes match; missing input exits 3.

- [ ] **Step 3: Make fixtures isolate each rule**

Use `## Product slices` plus `### S-01: First outcome` / `### S-02: Second outcome` and prose bodies for valid slices. Make the repeated fixture contain the same 12+ token decision sentence under three distinct `##` sections. Make the long fixture exceed 1,800 words and use an empty `## Proportionality rationale`.

- [ ] **Step 4: Run RED tests**

Run: `python3 -m unittest tests.test_brief_lint tests.test_repository.Product0RepositoryTest.test_review_rubric_contains_slop_rules -v`

Expected: failure because the script and rubric do not exist.

#### Task 6.2: Implement the readiness rubric and linter

**Files:**
- Create: `skills/product0/references/readiness-rubric.md`
- Create: `scripts/lint_brief.py`
- Modify: `skills/product0/references/reviewing-brief.md`

**Interfaces:**
- `findings(text: str, kind: str, size: str) -> list[dict[str, str]]` returns dictionaries containing `code`, `level`, and optional detail.
- `main() -> int` returns 0, 1, 2, or 3 exactly as defined below.

- [ ] **Step 1: Write rubric behavior**

Give each stable ID a reviewer-facing condition and a `NOT_READY` consequence. Cover evidence, assumptions, repeated decisions, one-item slices, technical questions, routine UX, length, missing business context, and all six marketing-surface requirements. State that editorial defects may be fixed, while strategic gaps return to direction shaping.

- [ ] **Step 2: Implement Markdown normalization**

Strip YAML frontmatter only when a closing delimiter exists; malformed frontmatter is a file-format failure. Strip fenced code blocks, HTML template comments, Markdown tables, headings, and `Developer next step` boilerplate where the individual check requires prose.

- [ ] **Step 3: Implement slice and rationale checks**

Within `## Product slices`, flag noncanonical `###` headings, zero headings, one heading, and a canonical heading without a non-empty prose paragraph before the next heading. For small marketing briefs, requirement headings require one prose sentence immediately under `## Traceability rationale`; otherwise emit both `BRIEF_TRACEABILITY_RATIONALE_EMPTY` and `BRIEF_UNJUSTIFIED_REQUIREMENT_BLOCK` as applicable.

- [ ] **Step 4: Implement repetition and length checks**

Split normalized prose by sentence punctuation or paragraph boundaries, discard sentences under 12 tokens, then compare token-set Jaccard similarity across different top-level sections. At similarity `>= 0.82` across three distinct sections emit `BRIEF_REPEATED_DECISION`. For small marketing briefs emit no length finding at 1,500 or fewer body words, warning `BRIEF_LENGTH_REVIEW` at 1,501--1,800, and error `BRIEF_DISPROPORTIONATE_LENGTH` above 1,800 unless the proportionality rationale has at least 30 words, which yields warning `BRIEF_LENGTH_JUSTIFIED_REVIEW`.

- [ ] **Step 5: Implement CLI semantics**

Use `argparse` for syntax errors (exit 2). Return exit 3 for missing/unreadable input or malformed frontmatter; 1 for one or more errors; 0 for no errors or warnings only. Human output is one `LEVEL: CODE` line per finding. JSON output is exactly one object with a `findings` list and no extra stdout.

- [ ] **Step 6: Connect semantic review**

In `reviewing-brief.md`, point to `references/readiness-rubric.md` and state that the deterministic linter is structural authoring QA only, not semantic product review.

- [ ] **Step 7: Run GREEN verification**

Run:
```bash
python3 -m unittest tests.test_brief_lint -v
python3 -m unittest tests.test_repository.Product0RepositoryTest.test_review_rubric_contains_slop_rules -v
python3 -m unittest tests.test_repository -v
python3 scripts/validate_skillset.py
```

Expected: all tests pass and validator reports 0 warnings.

- [ ] **Step 8: Commit Task 6**

```bash
git add skills/product0/references/reviewing-brief.md skills/product0/references/readiness-rubric.md scripts/lint_brief.py tests
git commit -m "fix: review Product0 briefs for insight and proportionality"
```

### Task 7: Execute distribution hardening, then continue with Tasks 8--10

**Files:** The exact file lists, interfaces, fixtures, commands, and commit messages for Tasks 7--10 are contractual in the accepted patch plan sections 7--10. They cover metadata/install auditing, adaptive developer handoff, v0.2.1 documentation/release metadata, and the behavioral matrix/release gate.

- [ ] **Step 1: Before Task 7, audit the live tree**

Run: `git status --short && python3 -m unittest tests.test_repository -v && python3 scripts/validate_skillset.py`

Expected: clean worktree after Task 6 and green baseline. Then implement every Task 7 checklist item, including its RED tests before deleting stale sibling skill directories.

- [ ] **Step 2: Validate and commit Task 7**

Run exactly the Task 7 section 7.8 commands. Expected: explicit focused modules, validator, and `discover -s tests` pass. Commit message: `fix: prevent Product0 mixed-version workflow fallback`.

- [ ] **Step 3: Implement, validate, and commit Task 8**

Add the named-traceability RED test first. Run Task 8 section 8.4 commands. Expected: adaptive briefs without requirement IDs are accepted. Commit message: `fix: support adaptive Product0 briefs in developer handoff`.

- [ ] **Step 4: Implement, validate, and commit Task 9**

Add the release-version RED test before the changelog change. Run Task 9 section 9.3 commands. Expected: validator and full test suite have zero failures/warnings. Commit message: `docs: document Product0 v0.2.1 self-contained workflow`.

- [ ] **Step 5: Implement Task 10 and commit code before evidence**

Add sanitizer, runner, release-gate, and fixture tests before implementation. Run their unit tests plus repository tests. Commit implementation/fixtures, record that full SHA as `IMPLEMENTATION_SHA`, then run the six environment-gated scenarios and promote only sanitized records. Run the release gate against `IMPLEMENTATION_SHA`; create a separate evidence-only commit only if the gate passes. Do not treat blocked runs as passes.

### Task 11: Final verification and progress handoff

**Files:**
- Modify: `.superpowers/sdd/progress.md` (ignored local ledger only)

- [ ] **Step 1: Run final local checks**

Run:
```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_skillset.py
git status --short
git log --oneline -10
```

Expected: no relevant uncommitted files, validator has zero warnings, and every completed task has its own commit.

- [ ] **Step 2: Record evidence**

Append each task number, SHA, exact test commands, and either passed behavioral evidence or an explicit environment-blocked state. Never write a passed result for a blocked harness.
