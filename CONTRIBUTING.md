# Contributing

1. Add or update a realistic eval before changing skill behavior.
2. Keep Product0 pre-implementation. Do not add automatic implementation transitions.
3. Preserve the one-brief-per-initiative and one-memory-file-per-session invariants.
4. Keep `SKILL.md` files portable across Agent Skills-compatible hosts.
5. Run:

```bash
python scripts/validate_skillset.py
python -m unittest discover -s tests -v
```

6. Describe the behavior change and the eval scenario that justifies it.
