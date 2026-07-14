# Migrating to Product0 v0.2.1

1. Audit the target skills directory with python3 scripts/audit_install.py --format human ~/.agents/skills.
2. Remove only stale Product0 directories reported by the audit; keep unrelated skills.
3. Reinstall the complete set deterministically with npx skills add <product0-repo> --skill '*' -a <agent> --copy -y.
4. Audit the same target again.
5. Confirm exactly three active skills and five compatibility aliases. The stale sibling names are product0-orienting-context, product0-shaping-direction, product0-challenging-direction, product0-writing-brief, and product0-reviewing-brief.
