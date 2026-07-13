# Contributing

1. Add or update a realistic failing eval before changing skill behavior.
2. Keep Product0 pre-implementation.
3. Preserve the rule that no Product0 brief is created before direction approval.
4. Preserve one explicit memory file per conversation session.
5. Keep core `SKILL.md` files portable across Agent Skills-compatible hosts.
6. Use repository evidence and type-specific product judgment rather than generic checklist completion.
7. Run:

```bash
python scripts/validate_skillset.py
python -m unittest discover -s tests -v
```

8. Describe the baseline failure, the intended behavioral change, and any live-model evals performed.
