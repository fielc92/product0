# Authoring and evaluating Product0 skills

## Principles

- Keep the `product0` orchestrator focused on routing, boundaries, artifacts, and state.
- Put stage-specific judgment in the corresponding stage skill.
- Use descriptions for realistic trigger conditions, not workflow summaries.
- Avoid harness-specific tool names.
- Prefer positive output contracts for document shape and hard prohibitions only for discipline boundaries.
- Treat the canonical brief as the source of truth.

## Eval-driven changes

Each skill contains `evals/evals.json` with realistic prompts and expected behavior. Before modifying a skill:

1. Add or revise an eval that exposes the undesired behavior.
2. Observe the baseline behavior using the target agent harnesses when possible.
3. Make the smallest instruction change that fixes the failure.
4. Run the eval across at least two materially different models or harnesses.
5. Check that unrelated evals still pass.
6. Record newly observed rationalizations in `tests/baseline-failures.md`.

The included validator performs structural checks; it does not replace model-behavior evals.

## Compatibility

The Agent Skills standard requires the skill directory name and frontmatter `name` to match, with lowercase alphanumeric names and single hyphens. Keep descriptions below 1,024 characters.

Do not add model-specific frontmatter to the portable `SKILL.md` files. Platform-specific packaging may be added outside `skills/` as an optional distribution layer, but the core set must remain usable through skills.sh.
