# Repository orientation guide

Inspect in this order, stopping when enough context exists:

1. Existing `docs/product0/` briefs and explicit product decisions.
2. README, product overview, strategy, roadmap, requirements, and business docs.
3. Existing Superpowers specs or other approved design artifacts.
4. Public routes, page copy, navigation labels, onboarding flows, screenshots, and demos.
5. Design-system guidance, brand assets, visual references, and content files.
6. Pricing, packaging, compliance, support, sales, or operational documentation relevant to the request.
7. Recent commits or change notes that materially affect the request.
8. Implementation files only when needed to verify current visible behavior.

Search by request terms plus product synonyms. For a landing page, include terms such as landing, home, marketing, hero, pricing, demo, waitlist, positioning, brand, copy, screenshot, launch, and audience.

Do not inspect dependency internals, generated files, build outputs, or unrelated infrastructure.

## Source confidence

| Label | Meaning |
|---|---|
| Direct evidence | Current repository source clearly states or demonstrates it |
| Corroborated | Two or more independent sources agree |
| Inferred | Reasonable interpretation not explicitly approved |
| Stale/conflicting | Source may no longer represent current direction |
| Missing | No credible source found |
