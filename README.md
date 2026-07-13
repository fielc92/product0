# Product0 Skills

[![skills.sh](https://skills.sh/b/fielc92/product0)](https://skills.sh/fielc92/product0)

Product0 is a professional pre-implementation product-direction workflow for AI coding agents.

It inspects the running project, explains the lay of the land, shapes and challenges an opinionated product direction, writes one concise developer brief after approval, and stops before technical design or development.

```text
Product request
  -> repository orientation
  -> lay of the land
  -> professional product discovery
  -> challenged direction proposal
  -> user approval
  -> one atomic developer brief
  -> readiness review
  -> HANDOFF_READY
  -> STOP

Separate developer action
  -> product0-using-brief
  -> code-focused technical brainstorming
  -> implementation planning
  -> development
```

Product0 borrows Superpowers' strict state-machine discipline while owning the earlier product-direction layer.

## What changed in v0.2

- No brief is created before product direction is approved.
- Repository orientation happens before product questions.
- Product0 explains the existing landscape and makes a recommendation.
- Questions are consequential decision packets, not checklist drip-feeds.
- Delegated low-risk choices are decided by Product0.
- A separate critic challenges the direction before approval.
- Briefs are adaptive, evidence-aware, concise, and type-specific.
- The original v0.1 stages remain only as compatibility aliases.

## Active skill set

| Skill | Role |
|---|---|
| `product0` | Single public governor |
| `product0-orienting-context` | Inspects the repository and presents the lay of the land |
| `product0-shaping-direction` | Develops the professional product direction |
| `product0-challenging-direction` | Independently challenges quality and assumptions |
| `product0-writing-brief` | Writes one approved, adaptive developer brief |
| `product0-reviewing-brief` | Applies the final handoff-readiness gate |
| `product0-using-brief` | Developer-side bridge into technical brainstorming |
| `product0-session-memory` | One explicit memory file per conversation session |

The five v0.1 stage names remain as deprecated compatibility aliases. New workflows must not invoke them.

## Install with skills.sh

```bash
npx skills add fielc92/product0 --skill '*'
```

For Codex, Claude Code, and OpenCode:

```bash
npx skills add fielc92/product0 --skill '*' \
  -a codex -a claude-code -a opencode
```

The core skills use portable Agent Skills metadata and avoid harness-specific tool names.

## Invoke

```text
Use Product0 for this:
We need a landing page for the app.
```

Expected opening behavior:

1. inspect the project;
2. present the lay of the land and recommended framing;
3. ask only consequential product decisions.

Product0 does not create a brief at invocation time.

## Project outputs

Artifacts are created only when needed:

```text
docs/product0/
  briefs/
    YYYY-MM-DD-<topic>-product-brief.md
  sessions/
    YYYY-MM-DD-HHMM-<topic>-session.md
  decisions/
    YYYY-MM-DD-<topic>-product-decision-request.md
```

### Briefs

A brief is written only after the complete direction passes challenge and the user approves it. Initial creation is one coherent write with `status: handoff-draft`.

### Session memory

Phrases such as “remember this,” “capture this decision,” and “save this” invoke session memory. The first explicit write creates one session file; later writes update it. Recall questions are read-only.

## Developer handoff

After final review and approval, the brief becomes:

```text
status: handoff-ready
```

Product0 stops. A developer later invokes `product0-using-brief`, acknowledges fixed direction, recommendations, assumptions, non-goals, and technical questions, then begins technical brainstorming.

## Validate

```bash
python scripts/validate_skillset.py
python -m unittest discover -s tests -v
```

Behavioral eval fixtures live beside each skill. The landing-page regression scenario is documented in `tests/landing-page-regression.md`.

## License

MIT.
