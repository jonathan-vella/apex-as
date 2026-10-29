# Product backlog

## Conventions

All items are planned and unassigned. IDs are local backlog identifiers, not
GitHub issue numbers. Repository creation does not create these issues.

- P0: resolve before dependable product implementation or real evidence handling.
- P1: required for the first usable assessment/pilot experience.
- P2: controlled expansion after the core experience is validated.
- Dependencies are actual prerequisites; list order alone is not a dependency.
- Completion requires the stated evidence, not merely files with the right names.

## AS-001 - Prove native agent-plugin distribution

**Priority:** P0. **Milestone:** M0. **Depends on:** none.

Verify the target VS Code Copilot client's supported plugin packaging,
installation, discovery, permissions and removal behavior.

Acceptance:

- Record authoritative documentation references and the tested client version.
- Install and invoke a minimal plugin without devcontainers or Docker.
- Demonstrate coexistence with APEX and no overwrites of core/user files.
- Verify removal and document whether cross-plugin invocation is supported.
- Report unsupported capabilities as blockers, not invented manifest fields or
  undocumented copy-based substitutes.

## AS-002 - Confirm profile authority and audit boundaries

**Priority:** P0. **Milestone:** M0. **Depends on:** none.

Select the first specialization and confirm the applicable checklist version,
interpretations, Module A standing and ALZ evidence ownership.

Acceptance:

- Record source provenance, effective window and redistribution rights.
- Distinguish shared controls from specialization-specific requirements.
- Resolve or explicitly block ambiguous clauses and claimed exemptions.
- Document whether externally owned ALZ evidence is acceptable; do not substitute
  policy discovery for deployment evidence.
- Do not publish restricted source documents.

## AS-003 - Define the minimum APEX compatibility contract

**Priority:** P0. **Milestone:** M0. **Depends on:** none.

Identify supported artifacts, schemas and documented recall JSON commands.

Acceptance:

- Select one exact initial APEX baseline and applicable recall version.
- Distinguish artifact-only and recall-connected modes.
- Exclude private modules, direct session-state access and Markdown parsing as a
  presumed stable API.
- Specify missing-evidence versus incompatible-contract diagnostics.
- Identify any neutral upstream contract work needed without changing core here.

## AS-004 - Define privacy, isolation and evidence ownership

**Priority:** P0. **Milestone:** M0. **Depends on:** none.

Define allowed storage, access, sharing, retention and customer approval boundaries.

Acceptance:

- Specify separate engagement state and authoritative evidence ownership.
- Define source/derivative handling and export authorization.
- Cover identifiers required by a control without assuming blanket anonymization.
- Define treatment of inaccessible evidence and untrusted embedded instructions.
- Approve synthetic-fixture rules before real customer data is used.

## AS-005 - Choose host runtime and licensing strategy

**Priority:** P0. **Milestone:** M0. **Depends on:** AS-001, AS-003.

Choose the lightest practical deterministic tooling and distribution prerequisites.

Acceptance:

- Document supported hosts and every required runtime/tool.
- Demonstrate that no container runtime is required.
- Separate optional core CLI requirements from artifact-only assessment.
- Define approved installation sources and user-controlled dependency acquisition.
- Record product-license and third-party redistribution decisions before release.

## AS-006 - Define evidence and profile schemas

**Priority:** P1. **Milestone:** M1. **Depends on:** AS-002, AS-003, AS-004.

Specify the register, versioned control rules, provenance and coverage state.

Acceptance:

- Model engagement/customer/scenario/date requirements without flattening all
  controls into one portfolio count.
- Distinguish applicability, collection, review, freshness and blocked states.
- Keep original and redacted derivative integrity separate.
- Record exact assessment versions and review/acceptance references.
- Cover incomplete and ambiguous inputs with explicit errors or unresolved states.

## AS-007 - Implement explicit input adapters

**Priority:** P1. **Milestone:** M1. **Depends on:** AS-003, AS-005, AS-006.

Consume authorized APEX artifacts and documented recall JSON when selected.

Acceptance:

- Implement explicit artifact-only and recall-connected inputs.
- Refuse unsupported required contracts with actionable messages.
- Never directly read/write core session state or mutate core artifacts/indexes.
- Preserve source locations and expose access failures.
- Do not silently substitute one input mode for another.

## AS-008 - Implement objective evidence coverage

**Priority:** P1. **Milestone:** M1. **Depends on:** AS-005, AS-006.

Evaluate structural requirements, recency, unique populations and scenario linkage.

Acceptance:

- Produce stable results for the same inputs and reference date.
- Test boundary dates, duplicate customers, migration scenarios and missing fields.
- Retain ambiguous profile rules as unresolved rather than guessing.
- Separate objective coverage from semantic sufficiency and external acceptance.

## AS-009 - Build synthetic acceptance fixtures

**Priority:** P1. **Milestone:** M1. **Depends on:** AS-004, AS-006.

Create valid, missing, stale, inaccessible and incompatible engagement examples.

Acceptance:

- Use invented identities and non-sensitive data only.
- Label fixtures as synthetic and exclude them from real portfolio eligibility.
- Include ALZ visibility limits, missing acceptance and cross-customer references.
- Document expected outcomes for each rule and failure case.

## AS-010 - Add freshness and run traceability

**Priority:** P1. **Milestone:** M1. **Depends on:** AS-007, AS-008, AS-009.

Detect evidence changes and record the precise assessment inputs.

Acceptance:

- Store resolved add-on/core-contract/profile versions and assessment time.
- Changed source evidence invalidates affected review status.
- Preserve prior review history and never restamp an approval automatically.
- State clearly that checksums are not identity or consent proof.

## AS-011 - Implement the evidence coordinator

**Priority:** P1. **Milestone:** M2. **Depends on:** AS-001, AS-007, AS-008, AS-009.

Provide assessment, collection guidance and packaging coordination through a
bounded agent experience.

Acceptance:

- Proposed mappings include source references, rationale and uncertainty.
- Agent suggestions cannot silently become reviewed evidence.
- Existing APEX owners retain delivery responsibility and approval gates.
- Imported evidence cannot issue executable instructions to the coordinator.
- No automatic Azure writes, ALZ changes or audit submissions.

## AS-012 - Implement controlled audit exports

**Priority:** P1. **Milestone:** M2. **Depends on:** AS-004, AS-006, AS-010.

Generate a reviewed index and only the permitted evidence derivatives.

Acceptance:

- Require explicit export scope and authorization.
- Verify required identifiers and redaction constraints per profile.
- Preserve original-to-derivative links and unresolved gaps.
- Never label export generation as external audit acceptance.

## AS-013 - Package the installable plugin

**Priority:** P1. **Milestone:** M2. **Depends on:** AS-001, AS-005, AS-011.

Implement the verified native plugin layout and host preflight.

Acceptance:

- Use only client-supported manifest fields and discovery mechanisms.
- Publish actual installation and removal instructions.
- Detect missing host tools without silently installing them.
- Preserve core and user-owned customization files across update/removal.

## AS-014 - Test supported hosts and failure boundaries

**Priority:** P1. **Milestone:** M2. **Depends on:** AS-009, AS-012, AS-013.

Exercise the complete plugin assessment/export journey on declared hosts.

Acceptance:

- Pass clean-host install/invoke/update/remove tests without containers.
- Test customer isolation, path boundaries and untrusted evidence.
- Test missing CLI, incompatible core, stale evidence and denied source access.
- Verify no Azure or core-state mutations occur.
- Limit published support claims to tested client/host combinations.

## AS-015 - Replay an authorized real engagement

**Priority:** P1. **Milestone:** M3. **Depends on:** AS-002, AS-004, AS-014.

Validate whether the product exposes useful and accurate gaps.

Acceptance:

- Obtain permission for the chosen engagement and storage scope.
- Independently review mappings, source traceability and limitations.
- Keep real evidence out of the public repository.
- Publish only approved aggregate findings or synthetic reproductions.
- Preserve uncovered portfolio and ALZ evidence requirements.

## AS-016 - Add in-delivery evidence collection handoffs

**Priority:** P1. **Milestone:** M3. **Depends on:** AS-011, AS-015.

Guide collection at existing APEX lifecycle activities.

Acceptance:

- Identify owner, source tool and capture point for each pilot requirement.
- Capture actual assessments, migration/test results and customer acceptance.
- Do not make plugin-to-plugin task calls a prerequisite unless proven supported.
- Do not change mandatory core workflow or reset existing approvals/reviews.
- Measure retrospective preparation effort against the previous method.

## AS-017 - Package one bounded partner delivery kit

**Priority:** P2. **Milestone:** M4. **Depends on:** AS-016.

Turn a recurring service into reusable procedure, configuration and evidence capture.

Acceptance:

- Define scope, outcomes, supported variants and ALZ prerequisites.
- Distinguish configuration-only changes from material redesign.
- Include tests, acceptance criteria and collection instructions.
- Validate use by another practitioner without copying customer-specific evidence.
- Measure reuse against an agreed denominator; do not claim 80% by assumption.

## AS-018 - Add cross-engagement portfolio coverage

**Priority:** P2. **Milestone:** M5. **Depends on:** AS-008, AS-014, AS-015.

Evaluate eligible populations without centralizing unrestricted customer evidence.

Acceptance:

- Preserve control-specific windows, customer uniqueness and scenario linkages.
- Keep access and evidence ownership separate by engagement.
- Detect duplicates and distinguish method readiness from portfolio sufficiency.
- Exclude lab/synthetic fixtures from qualifying populations.

## AS-019 - Validate the next specialization profile

**Priority:** P2. **Milestone:** M5. **Depends on:** AS-002, AS-015, AS-018.

Extend coverage without hardcoding one workload's rules into the engine.

Acceptance:

- Confirm source authority and permitted use for the new version.
- Reuse common controls only where applicability matches.
- Add independent fixtures for differing population/scenario requirements.
- Review changed interpretations and do not silently migrate prior assessments.

## AS-020 - Establish compatibility CI and release controls

**Priority:** P1. **Milestone:** M5. **Depends on:** AS-003, AS-009, AS-013.

Automate dependency verification before supported releases.

Acceptance:

- Test against exact pinned baselines and proposed compatible upgrades.
- Validate resolved contract/profile versions and detect breaking changes.
- Keep fixture data synthetic and installation sources approved.
- Publish release notes, supported versions and upgrade impact.
- Do not automatically update customer APEX installations.

## AS-021 - Publish maintained distribution and ownership

**Priority:** P2. **Milestone:** M5. **Depends on:** AS-005, AS-014, AS-015, AS-020.

Make the plugin supportable as a product rather than an experimental prompt pack.

Acceptance:

- Document licensing, support boundaries and maintainer responsibilities.
- Publish verified distribution instructions and actual release limitations.
- Define checklist-change intake and compatibility maintenance.
- Document data-handling expectations and removal behavior.
- Keep certification and audit acceptance outside product claims.
