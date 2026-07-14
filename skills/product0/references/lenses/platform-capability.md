# Platform-capability lens

Use this lens for reusable capabilities, primitives, or product platform work.
Inspect consumers, current adoption, extension points, operational evidence, and
the promises already made to builders. Direction approval is prohibited while a
relevant marker has an unresolved blocking product decision.

## PC01_CONSUMERS
- **Repository evidence to inspect:** consumer teams, integrations, documentation, and usage patterns.
- **Product0 recommendation:** identify the primary consumers and the distinct needs that warrant product support.
- **Blocking product decision:** resolve whose needs take priority when consumer groups conflict.
- **Reserved for technical brainstorming:** client libraries and dependency graphs.

## PC02_JOBS_AND_OUTCOMES_ENABLED
- **Repository evidence to inspect:** consumer workflows, unmet needs, adoption requests, and outcome measures.
- **Product0 recommendation:** define the jobs the capability enables and the outcomes it should improve.
- **Blocking product decision:** decide whether a proposed job belongs in this capability or another product surface.
- **Reserved for technical brainstorming:** implementation APIs and execution models.

## PC03_CAPABILITY_BOUNDARY
- **Repository evidence to inspect:** existing platform boundaries, alternatives, product taxonomy, and support burden.
- **Product0 recommendation:** state what the capability owns and the adjacent concerns it deliberately excludes.
- **Blocking product decision:** settle a boundary that changes the platform's product promise or ownership.
- **Reserved for technical brainstorming:** package layout and service decomposition.

## PC04_CONFIGURATION_AND_CONTROL
- **Repository evidence to inspect:** consumer variation, administration patterns, policy needs, and adoption friction.
- **Product0 recommendation:** recommend meaningful controls and distinguish supported configuration from bespoke customization.
- **Blocking product decision:** approve controls that create enduring product commitments or unequal access.
- **Reserved for technical brainstorming:** settings storage, UI controls, and flag implementation.

## PC05_PRODUCT_LEVEL_GUARANTEES
- **Repository evidence to inspect:** contracts, reliability evidence, support expectations, and dependency limits.
- **Product0 recommendation:** make clear guarantees, limits, and responsibilities that consumers can safely rely on.
- **Blocking product decision:** approve a guarantee with cost, legal, reliability, or support consequences.
- **Reserved for technical brainstorming:** SLO calculation, redundancy, and protocol details.

## PC06_FAILURE_CONSEQUENCES
- **Repository evidence to inspect:** incidents, fallback behavior, consumer impact, and escalation paths.
- **Product0 recommendation:** define which failures are product-significant and the expected consumer-facing consequence.
- **Blocking product decision:** decide acceptable degradation where trust, data, or a critical workflow is affected.
- **Reserved for technical brainstorming:** circuit breakers, retries, and incident tooling.

## PC07_ADOPTION_AND_MIGRATION_IMPLICATIONS
- **Repository evidence to inspect:** current consumers, legacy paths, migration cost, documentation, and rollout history.
- **Product0 recommendation:** recommend a viable adoption path and migration expectation for affected consumers.
- **Blocking product decision:** choose compatibility, deprecation, or migration commitments that materially affect users.
- **Reserved for technical brainstorming:** versioning, adapters, and rollout automation.

## PC08_SUCCESS_EVIDENCE_AND_GUARDRAILS
- **Repository evidence to inspect:** adoption data, performance evidence, support signals, and business goals.
- **Product0 recommendation:** name evidence of useful adoption and guardrails against unsafe or costly usage.
- **Blocking product decision:** resolve a metric trade-off that changes product incentives or consumer treatment.
- **Reserved for technical brainstorming:** telemetry pipelines and operational dashboards.

## PC09_SCOPE_AND_NON_GOALS
- **Repository evidence to inspect:** request boundaries, roadmap, competing platform work, and consumer expectations.
- **Product0 recommendation:** frame the smallest durable capability and its explicit non-goals.
- **Blocking product decision:** settle a scope choice that changes consumers or their supported outcomes.
- **Reserved for technical brainstorming:** milestones, staffing, and internal implementation sequencing.

## PC10_IMPLEMENTATION_NEUTRAL_HANDOFF
- **Repository evidence to inspect:** approved direction, consumer contracts, risks, and technical constraints.
- **Product0 recommendation:** hand off product guarantees, adoption intent, and unresolved risks without selecting a design.
- **Blocking product decision:** resolve only product ambiguity that prevents a coherent consumer contract.
- **Reserved for technical brainstorming:** APIs, architectures, schemas, and infrastructure choices.
