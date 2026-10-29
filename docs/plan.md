# Product and implementation plan

## Decision

Build APEX AS as a separately versioned, optional agent-plugin product in its own
repository. Keep APEX specialization-neutral and independently usable.

The product is an evidence-enabled delivery method, not an automated
specialization-application generator. Start with one partner service and one
specialization profile; preserve room for a shared evidence model across profiles.

All interfaces and components below are proposed unless explicitly stated
otherwise. This repository does not yet implement them.

## Architecture

The dependency direction is:

```text
Supported VS Code Copilot client
    |
    +-- APEX: general infrastructure delivery
    |
    +-- APEX AS agent plugin
            |
            +-- specialization profiles and collection guidance
            +-- deterministic evidence validation and coverage
            +-- approved APEX artifacts / documented recall JSON
            +-- customer-controlled evidence store
```

Co-installation is the intended experience, not a verified capability. The first
technical spike must prove the target client's supported plugin format,
installation, discovery, tool permissions and coexistence behavior.

Do not assume that one installed plugin can invoke another plugin's agents,
that a sibling repository is automatically discovered, or that a plugin can
silently install host dependencies.

## Components and ownership

| Component | Owner | Responsibility |
|---|---|---|
| Infrastructure delivery | APEX | Requirements, architecture, governance, IaC, deployment and as-built |
| Specialization profiles | APEX AS | Versioned criteria, applicability and evidence requirements |
| Evidence engine | APEX AS | Structural checks, dates, source references and portfolio coverage |
| Evidence coordinator | APEX AS | Explain gaps, propose mappings and guide authorized collection |
| Evidence originals | Partner/customer | Authoritative records, sharing rights and retention |
| Existing ALZ | Customer/platform owner | Platform configuration and supporting platform evidence |

APEX AS must not duplicate APEX role definitions or modify its workflow graph to
make the add-on mandatory. Any necessary improvement to core must be proposed
separately as a specialization-neutral contract.

## Dependency strategy

### Consume the smallest stable surface

- Read authorized project artifacts through explicitly supported contracts.
- Use documented `apex-recall` JSON commands for selected live session context.
- Never directly read or write `00-session-state.json`.
- Do not import private recall modules or alter its index.
- Do not treat Markdown headings, agent prose or optional telemetry as stable APIs.

Artifact-only assessment and recall-connected assessment are separate, explicitly
selected modes. An unavailable CLI must not silently switch modes or imply that
current session state was checked.

### Declare compatibility and lock actual use

Maintain a compatibility declaration covering:

- Supported target client versions and verified plugin capabilities.
- Supported APEX release/revision and consumed contract identifiers.
- Recall version/commands where the selected mode requires recall.
- Host runtime/tool requirements for implemented deterministic checks.
- Add-on and specialization-profile versions.

Record exact resolved revisions and profile versions for each installation or
assessment run. Begin with one tested APEX baseline; do not claim a broad version
range until the compatibility matrix proves it.

Existing APEX schema files are useful inputs, but their existence alone does not
establish a public backward-compatibility promise. Document the subset consumed,
seek a neutral upstream contract where needed, and test upgrades explicitly.

An incompatible contract blocks the affected capability with an actionable
diagnostic. Missing engagement evidence produces a gap, not a compatibility error.
No automatic APEX upgrade, credential change or customer-file rewrite is allowed.

### Host-native operation

The supported user journey must work without a devcontainer or Docker.
Choose the lightest host toolchain that satisfies deterministic validation after
the compatibility spike; do not select a runtime merely because core development
uses it.

Assess runtime acquisition, approved package sources and operating-system support
before publication. Existing core runtime requirements still apply to capabilities
that explicitly invoke core tools.

## Evidence and state

Keep add-on state separate from APEX state and from this product repository.
Reference authoritative evidence in a customer-approved location; copying it into
Git is not the default.

The proposed evidence register records:

- Engagement and restricted customer references.
- Checklist/profile version, control identifiers and scenario.
- Original artifact location, producer and collection time.
- Actual engagement/completion dates where required.
- Source integrity and separately tracked redacted derivatives.
- Reviewer, acceptance reference, coverage state and unresolved gaps.
- Classification, sharing permissions and retention obligations.

Content hashes detect byte changes; they do not prove truth, customer consent,
human identity or non-repudiation.

Agent suggestions remain proposals until reviewed. Deterministic tooling checks
structure and coverage; accountable humans settle ambiguous interpretation and
authorize submissions.

## ALZ boundary

APEX AS never deploys or mutates an ALZ. It records prerequisites, authorized
observations and platform-owner evidence.

The supplied checklist material includes ALZ deployment obligations. Do not
substitute workload integration or policy discovery for platform-deployment
evidence. Resolve acceptable ownership, qualification/exemption and evidence
provenance with the responsible audit authority, or retain an explicit gap.

Do not classify an externally owned platform as noncompliant merely because the
workload team cannot access all of it. Record the visibility limit and responsible
owner.

## Repeatability model

Separate four layers:

1. Partner delivery method: activities, roles, gates and collection instructions.
2. Workload archetype: bounded architecture, supported variants and tests.
3. Engagement configuration: customer, region, SKU, NFR and platform dependencies.
4. Engagement evidence: actual assessments, results, approvals and outcomes.

Treat 80% repeatability as a target requiring a defined denominator and measured
baseline. A material NFR or platform change can require redesign, not merely a
different parameter.

Start with one evidence coordinator rather than a new agent fleet. Preserve the
existing delivery owner for each APEX activity. Direct cross-plugin delegation is
optional and must not be required for the initial product.

## Delivery sequence

1. Prove native plugin installation and dependency contracts.
2. Build read-only evidence assessment for one approved checklist profile.
3. Demonstrate the result on a synthetic fixture and an authorized real engagement.
4. Add explicit collection handoffs to existing delivery activities.
5. Package one reusable service archetype after the evidence process is validated.
6. Add portfolio coverage and additional profiles after the pilot succeeds.

See the [roadmap](roadmap.md) for gates and the [backlog](backlog.md) for executable
work items.

## Public repository policy

This repository contains product code, agents, profiles approved for
redistribution, documentation and synthetic fixtures.

It must not contain customer evidence, tenant inventories, credentials or
unlicensed checklist reproductions. Confirm profile provenance and permitted use;
reference authoritative sources rather than publishing restricted source text.

## Immediate decision backlog

- Authoritative checklist versions and first pilot specialization.
- Partner's existing Module A standing and ALZ evidence ownership.
- Target client plugin capabilities and supported host platforms.
- Pilot engagement, evidence access and customer sharing permissions.
- Initial APEX baseline and minimum artifact contracts.
- License and third-party redistribution policy.

The repository bootstrap does not imply these decisions are settled.
