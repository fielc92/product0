# Apply Product0 v0.2 overlay

This overlay contains the complete Product0 v0.2 skill redesign. It adds new active skills and converts the v0.1 stage skills into compatibility aliases.

From the root of a clone of `fielc92/product0`:

```bash
unzip product0-v0.2-overlay.zip -d /tmp/product0-v0.2-overlay
cp -R /tmp/product0-v0.2-overlay/. .
python scripts/validate_skillset.py
python -m unittest discover -s tests -v
git status --short
git add .
git commit -m "feat: redesign Product0 professional discovery workflow"
```

Recommended review branch:

```bash
git switch -c product0-v0.2-professional-discovery
```

Run that branch command before copying the overlay if you want the changes isolated.
