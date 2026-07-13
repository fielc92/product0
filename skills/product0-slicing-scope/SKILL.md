---
name: product0-slicing-scope
description: Use when a user or older workflow invokes the former scope-slicing stage; retained only to route existing Product0 installations into the v0.2 workflow.
license: MIT
compatibility: Agent Skills-compatible agents.
metadata:
  author: product0
  version: "0.2.0"
  role: compatibility
---

# Deprecated Product0 Compatibility Alias

```text
DEPRECATED COMPATIBILITY ALIAS
```

This skill no longer owns a separate approval stage.

1. Do not create or update a Product0 brief.
2. Do not resume the v0.1 checklist interview.
3. Load `product0-shaping-direction` and follow it exactly.
4. Preserve any current conversation context and repository orientation.
5. Tell the user only when the target skill is unavailable.

The active Product0 workflow is orientation → direction shaping → challenge → one approved brief write → review.
