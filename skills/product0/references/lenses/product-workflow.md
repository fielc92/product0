# Product-workflow lens

Use this lens for a feature or service flow that changes what people can do.
Inspect existing journeys, support evidence, domain language, policies, and
neighboring behavior. Direction approval is prohibited while a relevant marker
has an unresolved blocking product decision.

## PW01_ACTORS_AND_AFFECTED_PARTIES
- **Repository evidence to inspect:** roles, account models, support cases, and adjacent journeys.
- **Product0 recommendation:** define the initiating actor, affected parties, and whose outcome takes priority.
- **Blocking product decision:** resolve a conflict between party interests or an unowned affected user.
- **Reserved for technical brainstorming:** identity lookup and notification delivery.

## PW02_TRIGGERING_SITUATION
- **Repository evidence to inspect:** entry points, real user language, events, and current workarounds.
- **Product0 recommendation:** describe the situation that starts the workflow and its meaningful context.
- **Blocking product decision:** choose among competing triggers that alter the product promise.
- **Reserved for technical brainstorming:** event wiring and route structure.

## PW03_DESIRED_PRODUCT_OUTCOME
- **Repository evidence to inspect:** product goals, customer outcomes, and acceptance evidence.
- **Product0 recommendation:** state the user-visible outcome and the value it must create.
- **Blocking product decision:** settle an outcome trade-off that changes the feature's purpose.
- **Reserved for technical brainstorming:** service boundaries and persistence design.

## PW04_LIFECYCLE_AND_STATE_PROGRESSION
- **Repository evidence to inspect:** existing statuses, policies, audits, and related lifecycle language.
- **Product0 recommendation:** recommend the meaningful states, transitions, and completion condition.
- **Blocking product decision:** decide irreversible transitions, cancellation, or retention expectations.
- **Reserved for technical brainstorming:** state machines, tables, and transaction handling.

## PW05_BUSINESS_RULES
- **Repository evidence to inspect:** domain rules, pricing, policy documents, and known exceptions.
- **Product0 recommendation:** make the rules legible, prioritizing behavior that protects the promised outcome.
- **Blocking product decision:** resolve a rule that changes eligibility, value, or a customer commitment.
- **Reserved for technical brainstorming:** validation code and rule-engine structure.

## PW06_AUTHORITY_AND_PERMISSIONS
- **Repository evidence to inspect:** role definitions, access policies, audit needs, and ownership models.
- **Product0 recommendation:** specify who may initiate, view, change, approve, or override the workflow.
- **Blocking product decision:** decide disputed authority or a consequential override path.
- **Reserved for technical brainstorming:** authorization middleware and permission storage.

## PW07_CONSEQUENTIAL_EXCEPTIONS
- **Repository evidence to inspect:** failure cases, support escalations, compliance requirements, and historical incidents.
- **Product0 recommendation:** describe exceptions that materially affect trust, money, safety, or completion.
- **Blocking product decision:** choose the customer-facing treatment for consequential failure or ambiguity.
- **Reserved for technical brainstorming:** retries, queues, and error serialization.

## PW08_SUCCESS_EVIDENCE_AND_GUARDRAILS
- **Repository evidence to inspect:** analytics, support volume, quality thresholds, and business targets.
- **Product0 recommendation:** name outcome measures and guardrails that show the workflow is helping without harm.
- **Blocking product decision:** approve a success trade-off that could degrade another stakeholder's outcome.
- **Reserved for technical brainstorming:** dashboards, instrumentation, and alert plumbing.

## PW09_SCOPE_AND_NON_GOALS
- **Repository evidence to inspect:** request wording, roadmap, adjacent workflows, and capacity constraints.
- **Product0 recommendation:** define the smallest coherent workflow and explicit exclusions.
- **Blocking product decision:** settle a boundary that changes who receives value or what is promised.
- **Reserved for technical brainstorming:** delivery sequencing and implementation estimates.

## PW10_IMPLEMENTATION_NEUTRAL_HANDOFF
- **Repository evidence to inspect:** approved direction, assumptions, decisions, and known technical constraints.
- **Product0 recommendation:** hand off observable behavior, priorities, and risks without prescribing an architecture.
- **Blocking product decision:** resolve only product ambiguity that prevents a coherent behavioral contract.
- **Reserved for technical brainstorming:** APIs, schemas, infrastructure, and detailed interface design.
