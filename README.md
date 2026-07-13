# Product0 Skills

Product0 is a strict pre-implementation product-direction workflow for AI coding agents.

It turns a vague product request into one approved developer brief, then stops. A developer can later use that brief to begin code-focused technical brainstorming.

```text
Product request
  -> intent
  -> product requirements
  -> product experience
  -> product scope slices
  -> developer brief
  -> HANDOFF_READY
  -> STOP

Separate developer action
  -> product0-using-brief
  -> technical brainstorming
  -> implementation planning
  -> development
```

Product0 is inspired by the composable, state-machine discipline of [Superpowers](https://github.com/obra/superpowers), while owning an earlier part of the lifecycle.

## What Product0 does

- Clarifies the problem, actor, outcome, and success evidence.
- Defines observable product behavior and business rules.
- Designs journeys, states, interactions, and product-visible failure behavior.
- Separates coherent product outcomes without producing engineering tickets.
- Produces implementation-neutral directions for developer brainstorming.
- Reviews the brief for readiness.
- Keeps one revisable conversation-memory file per session when asked.

## What Product0 never does

Product0 does not automatically inspect code architecture, create implementation plans, make branches, dispatch coding agents, or write code. Its successful terminal state is `handoff-ready`.

## Skill set

| Skill | Role |
|---|---|
| `product0` | Public entry point and state-machine governor |
| `product0-framing-intent` | Establishes the approved product problem and outcome |
| `product0-defining-requirements` | Defines observable product behavior and boundaries |
| `product0-designing-experience` | Resolves journeys, states, interactions, and product trade-offs |
| `product0-slicing-scope` | Creates outcome-oriented product slices |
| `product0-preparing-brief` | Compiles the developer-facing handoff |
| `product0-reviewing-brief` | Applies the final readiness gate |
| `product0-using-brief` | Developer-initiated bridge into technical brainstorming |
| `product0-session-memory` | Maintains one structured memory file per conversation session |

Users normally invoke only `product0`. The other skills compose behind that interface and are required dependencies, so install the complete set.

## Install with skills.sh

From a published Git repository:

```bash
npx skills add fielc92/product0 --skill '*'
```

For Codex, Claude Code, and OpenCode specifically:

```bash
npx skills add fielc92/product0 --skill '*' \
  -a codex -a claude-code -a opencode
```

From a local checkout:

```bash
npx skills add ./product0-skills --skill '*'
```

The repository uses the open Agent Skills format: one folder per skill with a `SKILL.md` containing portable YAML metadata and Markdown instructions. It intentionally avoids harness-specific tool names.

## Invoke

Natural language works across compatible agents:

```text
Use Product0 for this:
Customers should be notified when a debit order fails.
```

Agents that expose explicit skill invocation may also allow forms such as `$product0`, `/product0`, or selection through their skill UI.

## Project outputs

Product0 writes to the running project's documentation tree:

```text
docs/product0/
  briefs/
    YYYY-MM-DD-<topic>-product-brief.md
  sessions/
    YYYY-MM-DD-HHMM-<topic>-session.md
  decisions/
    YYYY-MM-DD-<topic>-product-decision-request.md
```

There is one living brief per initiative. Product0 revises it in place through every stage rather than creating separate intent, requirements, design, and scope documents.

## Session memory

During Product0, phrases such as these activate `product0-session-memory`:

```text
Remember this.
Note that consent is opt-in.
Capture this decision.
Save this for later.
Don't forget the compliance constraint.
```

The first write creates one dated session file. Every later memory write in the same conversation updates that file. A question such as “Do you remember what we decided?” reads the file without creating or changing one.

## Developer handoff

After the final review and user approval, Product0 reports:

```text
status: handoff-ready
```

Product0 stops. A developer later invokes `product0-using-brief`, which:

1. verifies the brief and revision;
2. acknowledges fixed product direction and open technical questions;
3. inspects the codebase;
4. invokes an installed technical `brainstorming` skill, including Superpowers brainstorming when available;
5. escalates missing product decisions instead of inventing them.

## Portability contract

The skills use only the standard fields `name`, `description`, `license`, `compatibility`, and string-valued `metadata`. They do not require shell commands, network access, model-specific APIs, or pre-approved tool names. The host needs only:

- Agent Skills-compatible discovery and loading;
- access to read and write project files;
- a way to ask the user questions.

See [`docs/architecture.md`](docs/architecture.md) for the workflow and [`docs/authoring.md`](docs/authoring.md) for validation and eval guidance.

## Validate

```bash
python scripts/validate_skillset.py
python -m unittest discover -s tests -v
```

## License

MIT. See [`LICENSE`](LICENSE).
