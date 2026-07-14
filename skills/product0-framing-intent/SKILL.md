---
name: product0-framing-intent
description: Use only when the user explicitly invokes product0-framing-intent by name; this deprecated alias redirects to product0.
license: MIT
compatibility: Agent Skills-compatible agents.
metadata:
  author: product0
  version: "0.2.1"
  role: compatibility
---

# Deprecated Product0 Compatibility Alias

DEPRECATED COMPATIBILITY ALIAS

EXPLICIT INVOCATION ONLY

This name is retained for one release cycle because an older user or saved workflow may invoke it directly.

1. Do not perform discovery, approval, brief writing, or state transitions here.
2. Load `product0`.
3. Preserve the user's current request and continue under the self-contained Product0 workflow.
4. If `product0` is unavailable, report that the complete Product0 set must be installed and stop.
