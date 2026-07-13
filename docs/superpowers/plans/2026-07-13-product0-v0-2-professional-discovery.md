# Product0 v0.2 Professional Discovery Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace Product0's template-driven interview with a repository-aware, senior product-discovery workflow that writes one concise developer brief only after product direction is approved.

**Architecture:** Keep `product0` as the single public governor. Route active work through orientation, direction shaping, independent challenge, atomic brief writing, and readiness review. Preserve the developer bridge and explicit session memory; retain old stage names only as compatibility aliases.

**Tech Stack:** Portable Agent Skills Markdown, JSON eval fixtures, Python 3.12 validator and unittest contracts, skills.sh repository layout.

## Global Constraints

- Product0 remains strictly pre-implementation.
- No initial brief or placeholder document may be written before direction approval.
- Repository orientation precedes product questions when repository access exists.
- Product questions are grouped into consequential decision packets, not checklist drip-feeds.
- Low-risk reversible choices delegated by the user are decided by Product0.
- Core skill files remain model- and harness-neutral.
- Project artifacts remain under `docs/product0/`.

---

### Task 1: Lock the failed landing-page run in regression contracts

**Files:**
- Modify: `tests/test_repository.py`
- Modify: `tests/baseline-failures.md`
- Create: `tests/landing-page-regression.md`
- Modify: `skills/product0/evals/evals.json`

- [ ] Add static assertions for repository orientation, delayed artifact writing, decision packets, and the absence of the old one-question instruction.
- [ ] Add the landing-page scenario with explicit pass and fail criteria.
- [ ] Run `python -m unittest discover -s tests -v` and confirm the new tests fail against v0.1 behavior.

### Task 2: Replace the active state machine

**Files:**
- Modify: `skills/product0/SKILL.md`
- Modify: `skills/product0/references/state-machine.md`
- Modify: `skills/product0/references/artifact-conventions.md`
- Create: `skills/product0-orienting-context/SKILL.md`
- Create: `skills/product0-orienting-context/references/repository-orientation.md`
- Create: `skills/product0-orienting-context/evals/evals.json`
- Create: `skills/product0-shaping-direction/SKILL.md`
- Create: `skills/product0-shaping-direction/references/product-lenses.md`
- Create: `skills/product0-shaping-direction/evals/evals.json`
- Create: `skills/product0-challenging-direction/SKILL.md`
- Create: `skills/product0-challenging-direction/evals/evals.json`

- [ ] Implement `orientation -> discovery -> direction proposal -> challenge -> approval`.
- [ ] Make the lay of the land the first user-facing Product0 output.
- [ ] Require evidence provenance and professional recommendations.
- [ ] Prevent all Product0 brief writes before direction approval.

### Task 3: Make brief creation atomic, adaptive, and reviewable

**Files:**
- Create: `skills/product0-writing-brief/SKILL.md`
- Create: `skills/product0-writing-brief/assets/product-brief-template.md`
- Create: `skills/product0-writing-brief/evals/evals.json`
- Modify: `skills/product0-reviewing-brief/SKILL.md`
- Modify: `skills/product0-reviewing-brief/references/readiness-rubric.md`
- Modify: `skills/product0-reviewing-brief/evals/evals.json`
- Modify: `skills/product0-using-brief/SKILL.md`
- Modify: `skills/product0-using-brief/evals/evals.json`

- [ ] Write one concise brief after the user approves the direction.
- [ ] Omit empty, repetitive, or inapplicable sections.
- [ ] Require type-specific strategic content and repository evidence.
- [ ] Reject assumption promotion, template completion, and disproportionate detail.

### Task 4: Preserve compatibility without using the old workflow

**Files:**
- Modify the five former stage `SKILL.md` files and their eval fixtures.

- [ ] Convert old stages into explicit compatibility aliases.
- [ ] Route discovery aliases to `product0-shaping-direction`.
- [ ] Route the former preparation alias to `product0-writing-brief`.
- [ ] Prohibit the aliases from creating documents or running the old staged interview.

### Task 5: Update packaging, docs, and validation

**Files:**
- Modify: `scripts/validate_skillset.py`
- Modify: `README.md`
- Modify: `docs/architecture.md`
- Modify: `docs/authoring.md`
- Modify: `CHANGELOG.md`
- Modify: `CONTRIBUTING.md`

- [ ] Validate active and compatibility skills separately.
- [ ] Document v0.2 behavior and artifact timing.
- [ ] Run `python scripts/validate_skillset.py`.
- [ ] Run `python -m unittest discover -s tests -v`.
- [ ] Inspect the final diff for stale v0.1 routing and placeholder-first behavior.
