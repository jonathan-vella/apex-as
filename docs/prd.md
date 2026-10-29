# Product requirements

## Product status

APEX AS is a proposed optional agent-plugin add-on to APEX. These requirements
define the intended product; they are not claims of implemented functionality.

## Problem

Partners need a repeatable delivery process and credible customer-specific
evidence for Azure specializations. Delivery artifacts, assessment exports,
migration results, acceptance records and portfolio eligibility are often handled
separately.

APEX already serves general infrastructure delivery, including customers with no
specialization objective. Adding mandatory partner-audit behavior to core would
couple different users and lifecycles unnecessarily.

## Intended users

| User | Primary need |
|---|---|
| Partner delivery lead | Apply a consistent method without hiding customer differences |
| Practitioner | Know which evidence to capture at the current activity |
| Specialization/evidence owner | Identify gaps and assemble traceable evidence |
| Customer approver | Control acceptance and sharing of customer records |
| Platform/ALZ owner | Supply scoped platform evidence without delegating platform mutation |
| Reviewer | Understand coverage, limitations and evidence provenance |

## Goals

- Make evidence capture part of delivery rather than a retrospective writing task.
- Keep APEX AS optional and independently versioned.
- Provide agent-plugin distribution without requiring a devcontainer.
- Separate reusable method from unique customer evidence.
- Make gaps, stale evidence and uncertainty visible.
- Preserve APEX approval boundaries and customer isolation.

## Non-goals

- Guaranteeing specialization qualification or audit acceptance.
- Replacing official assessments or accountable human reviewers.
- Deploying or modifying an ALZ.
- Executing migrations or fabricating their results as part of evidence assessment.
- Making APEX depend on partner-specialization functionality.
- Providing a hosted multi-customer SaaS platform in the MVP.
- Supporting every Copilot client or arbitrary APEX versions at launch.
- Reproducing restricted checklist documents in a public repository.

## Primary workflows

### Assess an existing engagement

Select profile/version and explicit input mode; verify compatibility and access;
inventory authorized evidence; propose control mappings; validate objective
coverage; return sourced gaps and a reviewer-ready index.

### Guide evidence collection

Identify a missing requirement, its owner and the relevant existing delivery
activity. Provide collection instructions without bypassing the actual tool run,
customer acceptance or core review process.

### Prepare an audit export

Select reviewed evidence; verify sharing authorization and required identifiers;
produce an index and permitted originals/derivatives; retain unresolved gaps.
Export generation never implies external acceptance.

### Review portfolio coverage

Evaluate eligible engagements against the selected control's customer counts,
recency, scenario and project-linkage rules. Do not count synthetic fixtures as
real customers or assume one global population satisfies every control.

## Functional requirements

| ID | Requirement | Acceptance |
|---|---|---|
| FR-01 | Optional native agent-plugin packaging | Install, invoke and remove through the verified client mechanism without modifying APEX core |
| FR-02 | No required devcontainer | The supported installation and assessment journey runs on a documented host without Docker/devcontainers |
| FR-03 | Explicit project and mode selection | User can distinguish artifact-only assessment from recall-connected assessment |
| FR-04 | Dependency preflight | Unsupported client, contract, APEX or required tool produces an actionable blocker |
| FR-05 | Versioned profiles | Every control mapping and result identifies its source profile/version and interpretation status |
| FR-06 | Source-aware evidence register | Entries reference authorized originals, owners, dates, classification and applicable controls |
| FR-07 | Reviewable agent mappings | Suggested mappings include rationale and evidence references; they are not automatically accepted |
| FR-08 | Deterministic coverage checks | Fixture-tested rules evaluate required metadata, populations, dates and scenarios without inventing evidence |
| FR-09 | Freshness checks | Changed referenced content invalidates affected review status rather than silently updating approval |
| FR-10 | ALZ dependency tracking | Missing platform evidence is assigned to its owner; no platform write is attempted |
| FR-11 | Controlled export | Export checks authorization and distinguishes originals from redacted derivatives |
| FR-12 | Human acceptance | Customer sign-off references remain attributable and scoped; agent text is not sign-off |
| FR-13 | Separate state | Add-on records never directly read/write core session state or rewrite core artifacts |
| FR-14 | Run traceability | Results record exact resolved add-on, core/contract and profile versions |
| FR-15 | Customer isolation | One engagement cannot silently contribute another customer's evidence or permissions |
| FR-16 | Honest results | Missing, stale, inaccessible, incompatible and not-applicable states remain distinguishable |
| FR-17 | Optional delivery integration | Collection guidance works without requiring unproven plugin-to-plugin task invocation |
| FR-18 | Explicit updates | Updates require an approved action and reassessment of affected evidence/compatibility |

## Evidence state model

Proposed states:

```text
Unmapped -> Missing -> Collected -> Reviewed -> Ready for human audit review
```

Also support Stale, Blocked and Not applicable with a documented justification.
The eventual schema must distinguish collection state, applicability and review
status where a single enumeration would lose information.

Readiness is an internal assessment against the selected profile, not a
certification. A human must approve exceptions and submission.

## Quality and safety requirements

- No default Azure writes, credential changes or consequential automatic actions.
- No silent fallback when required dependencies, state or evidence are unavailable.
- No direct access to core session-state files, including read-only parsing.
- No execution of instructions embedded in untrusted imported evidence.
- No automatic copying of evidence across customers.
- No default copying of customer material into this public product repository.
- No assumption that checksums authenticate a human or establish consent.
- No conversion of previous unresolved findings into passing evidence.
- No broad claim of operating-system support without clean-host tests.
- No runtime/package installation outside approved sources or without user control.

## MVP boundary

Include:

- One verified target-client installation path.
- One supported APEX baseline and explicit input modes.
- One approved specialization profile and its shared-control applicability.
- One evidence coordinator with deterministic validation.
- Evidence register, sourced gap report and reviewed export index.
- Synthetic acceptance fixtures and an authorized engagement pilot.

Defer:

- Multi-partner hosted storage and dashboards.
- Automatic specialization submission.
- Broad archetype catalog.
- Unverified direct cross-plugin orchestration.
- Automatic migration execution or ALZ remediation.

## Success measures

Establish baselines during the pilot:

- Time to produce and review a traceable evidence gap report.
- Applicable evidence completeness and portfolio coverage.
- Unsupported mappings identified by independent review.
- Stale evidence and missing acceptance detected before export.
- Installation/upgrade/removal success on supported hosts.
- Delivery activities reused without material redesign.
- Preparation effort compared with the partner's previous method.

The 80% reuse aspiration requires an agreed definition and comparable delivery
baseline. Do not substitute copied-file counts for reduced delivery effort.

## Release acceptance

Before calling the MVP usable:

1. Demonstrate native plugin install/discovery alongside APEX without a container.
2. Show clean uninstall and no modifications to core or user-owned files.
3. Pass compatibility, isolation and failure-path fixtures.
4. Independently review mappings and gaps from an authorized engagement.
5. Resolve source/profile licensing and publication permissions.
6. Publish actual supported versions and limitations.
7. Leave unresolved audit-interpretation and portfolio gaps visible.

## Open decisions

The first profile, partner pilot, accepted ALZ evidence path, supported client/host
matrix, runtime, license and source-profile redistribution rights remain pending.
See the [backlog](backlog.md) for the corresponding work.
