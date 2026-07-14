# Authoring and evaluating Product0 skills

## Principles

- Keep `product0` focused on strict routing and professional operating rules.
- Require repository orientation before questions.
- Write artifacts only after direction approval.
- Use product lenses selectively, not as forms.
- Prefer positive output contracts for response shape.
- Use hard prohibitions for boundary violations.
- Keep instructions portable across Codex, Claude Code, OpenCode, and other Agent Skills hosts.
- Optimize for decision quality and insight density, not template completeness.

## Eval-driven changes

Before changing behavior:

1. Add or revise a realistic eval that exposes the failure.
2. Record the baseline output or failure pattern.
3. Make the smallest coherent skill change.
4. Run structural validation.
5. Run behavioral evals in fresh contexts across at least two materially different models or harnesses when available.
6. Check unrelated scenarios.
7. Add observed rationalizations to `tests/baseline-failures.md`.

The validator checks repository contracts; it does not prove model behavior.

## Required behavioral dimensions

Product0 evals should cover:

- repository orientation and evidence use;
- professional product judgment;
- delegated initiative;
- question quality and decision-packet discipline;
- prevention of premature file writes;
- provenance and assumption control;
- proportionality and non-repetition;
- type-specific strategic depth;
- strict technical-design boundary;
- developer handoff quality.

## Primary regression

`tests/landing-page-regression.md` captures the v0.1 failure that motivated v0.2. Any change to discovery, writing, or review must be checked against it.

## Compatibility

Skill directories and frontmatter names must match and use lowercase hyphenated names. Descriptions must explain trigger conditions, not summarize the entire workflow. Do not add model-specific frontmatter to portable core skills.

## v0.2.1 quality and evidence

Marketing surfaces, product workflows, and platform capabilities require deep type-specific contracts. The other five lenses must not use placeholders. Use adaptive classifications, canonical S-01 slice headings, and conditional rationale sections. Keep raw harness output ignored; promote only sanitized behavioral records. A missing binary, model, authentication, or installation is blocked evidence, not a passed run.
