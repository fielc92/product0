# Product0 v0.2.1 implementation recovery design

## Purpose

Recover the v0.2.1 patch-plan implementation without discarding the five
completed, committed tasks. The current boundary is Task 6: its partial work
is uncommitted, incomplete, and has a runtime failure. The recovery restores
the plan's test-first workflow and makes subsequent task progress observable.

## Scope and boundaries

- Preserve commits through `9dbefc6` unchanged.
- Treat the uncommitted Task 6 reviewer, rubric, linter, and test edits as
  disposable recovery material; rebuild Task 6 from the accepted patch plan.
- Do not broaden the existing v0.2.1 requirements or refactor completed Tasks
  1--5 unless a later focused audit finds a direct contract violation.
- Complete Tasks 7--10 only after Task 6 has passed its specified checks and
  is committed.

## Recovery architecture

### Task 6: deterministic brief-shape QA

Start with the planned fixtures and `tests/test_brief_lint.py`, including CLI
subprocess tests for human and JSON output. The tests define the public
contract: required finding codes, canonical product-slice grammar and bodies,
traceability and proportionality rationale rules, repeated-claim detection,
old-stage detection, and exit codes.

Implement `scripts/lint_brief.py` as a small, deterministic CLI. It strips
only the planned non-prose Markdown constructs, emits structured findings, and
keeps semantic product judgment in `reviewing-brief.md` and the readiness
rubric. File access and malformed-frontmatter failures return exit code 3;
argument errors return 2; structural errors return 1; warnings alone return
0.

The readiness rubric documents the stable rule IDs as review questions and
clear `HANDOFF_READY` / `NOT_READY` behavior. It does not claim that the
linter replaces semantic review.

### Tasks 7--10: sequential verified slices

Before starting each remaining task, inspect the live tree and the task's
explicit checklist. Make only that task's changes, run its focused tests plus
the repository suite and validator, and commit the completed slice. Preserve
the plan's final release and three-harness acceptance requirements.

## Progress and validation

Maintain the ignored local progress ledger after each successful commit with
the task number, commit SHA, exact validation commands, and any
environment-gated skip. Do not rely on broad test discovery: validation must
invoke the plan's explicit test modules, then the repository suite and
`scripts/validate_skillset.py` where applicable.

If a focused test fails, stop at that task, diagnose the failure, and report
the concrete blocker before beginning another task. No agent handoffs are used
for this recovery.

## Acceptance criteria

The recovery is complete only when Task 6 meets every listed deterministic
contract; Tasks 7--10 each have their required evidence and commit; and the
plan's final repository, validator, release, and acceptance checks pass or
are recorded as explicitly environment-gated.
