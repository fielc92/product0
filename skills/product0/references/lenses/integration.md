# Integration lens

LENS_ID_INTEGRATION

Use this lens when the product outcome depends on another system, external partner, imported data, exported data, or a visible handoff across a boundary. The aim is to decide the customer and operator promise, not to select an API or design a transport protocol. Read the current integration inventory, customer requests, support evidence, contracts, and operational incidents before making a recommendation. A compatible technical connection is not automatically a useful product integration.

## LENS_EVIDENCE_TO_INSPECT

Inspect the user journey before and after the handoff, ownership of each system, data expectations, existing integrations, adoption and failure evidence, and any legal or commercial constraints. Look for whether users expect a source of truth, an assistive copy, a one-time import, or ongoing synchronization.

## LENS_RECOMMENDATIONS_TO_MAKE

Recommend the supported user job, the systems and data in scope, the visible status or confidence users need, and a clear boundary for what Product0 will not promise. Prefer a narrow integration that makes an outcome dependable over a broad connector with unclear value. State who benefits and how they recover when the external dependency is unavailable.

## LENS_BLOCKING_PRODUCT_DECISIONS

Escalate only decisions that change data ownership, customer commitments, privacy posture, commercial obligations, or the product's responsibility when systems disagree. Group linked choices into a compact decision packet with a recommendation, evidence or assumption, why it matters, and the minimum reply.

## LENS_IMPLEMENTATION_DETAILS_NOT_TO_ASK

Do not interview the user about authentication flows, polling cadence, webhook formats, retry policy, field mappings, SDK choice, or error serialization unless one creates a material product promise. Those are inputs to later technical brainstorming after direction is approved.
