# Roadmap

## Planning basis

Milestones are ordered by prerequisites and observable exit criteria, not promised
dates. All work is planned; no implementation milestone is complete.

The product must remain an optional agent plugin, require no devcontainer, keep
APEX core independent and never mutate an ALZ.

## M0 - Validate distribution and product boundaries

**Outcome:** demonstrate that the intended add-on can be installed and discovered
in the target VS Code Copilot client.

Work:

- Verify official plugin format and installation mechanism against authoritative
  client documentation and an actual client test.
- Demonstrate coexistence with APEX, scoped tool permissions and clean removal.
- Establish the host-native dependency strategy.
- Select the pilot profile and confirm source provenance/licensing.
- Resolve APEX interface, checklist and ALZ evidence assumptions.

**Exit:** a reproducible installation proof, initial compatibility contract,
approved pilot scope and recorded limitations.

**Stop rule:** if the required native plugin mechanism is unavailable, report the
blocker. Do not quietly substitute copied agents or a required devcontainer.

**Backlog:** AS-001 through AS-005.

## M1 - Read-only evidence assessment

**Outcome:** a deterministic, traceable gap assessment without live Azure writes.

Work:

- Implement the evidence model and one versioned profile.
- Add explicit artifact-only and recall-connected adapters.
- Implement objective coverage and freshness checks.
- Add synthetic valid, missing, stale and incompatible fixtures.

**Exit:** the same fixture inputs produce stable objective coverage results;
unsupported inputs and evidence gaps are distinguishable; no core state is
directly accessed or modified.

**Backlog:** AS-006 through AS-010.

## M2 - Usable agent-plugin experience

**Outcome:** an operator can assess an engagement through the installed plugin.

Work:

- Add the evidence coordinator and sourced mapping proposals.
- Present appropriate human decisions and preserve authorization boundaries.
- Implement controlled export and host dependency diagnostics.
- Exercise customer isolation, untrusted inputs and clean uninstall.

**Exit:** install-to-assessment-to-export works on the declared host/client matrix
without a container, and independent review catches unsupported mapping claims.

**Backlog:** AS-011 through AS-014.

## M3 - Authorized engagement pilot

**Outcome:** validate real utility before expanding scope.

Work:

- Replay one authorized historical engagement.
- Independently review evidence mappings and unresolved gaps.
- Add evidence collection to a new authorized delivery using existing APEX owners.
- Measure preparation effort and reusable delivery activities.

**Exit:** the partner accepts the usefulness of the gap report and collection
workflow; actual portfolio and interpretation gaps remain explicit.

**Backlog:** AS-015 and AS-016.

## M4 - Repeatable delivery kit

**Outcome:** make one recurring partner service repeatable within bounded limits.

Work:

- Define the archetype, supported configuration and material-deviation routing.
- Package procedures, acceptance criteria, tests and evidence capture.
- Prove adaptation without carrying over customer-specific approvals or results.

**Exit:** another practitioner can use the kit within its supported scope, with
measured reuse and explicit ALZ prerequisites.

**Backlog:** AS-017.

## M5 - Portfolio readiness and maintained distribution

**Outcome:** support controlled adoption and evolution.

Work:

- Add cross-engagement coverage while retaining customer isolation.
- Add the next specialization profile only after the first is validated.
- Publish compatibility-tested releases, update instructions and limitations.
- Establish profile changes, review ownership and maintenance cadence.

**Exit:** supported versions and actual pilot findings are published, installation
and removal are tested, licensing is settled and evidence review remains human
controlled.

**Backlog:** AS-018 through AS-021.

## Parallel work

After M0, schema design and adapter work can proceed independently where their
contract prerequisites are settled. Privacy/isolation and synthetic test fixtures
should start before any real evidence import.

The detailed prerequisites in the [backlog](backlog.md) govern execution; milestone
order alone does not imply that every item depends on every earlier item.

## Release policy

- Planning documentation is not an installable release.
- Plugin installation proof is not evidence-engine correctness.
- A successful pilot is not specialization certification.
- A new checklist profile or APEX contract version requires impact analysis and
  targeted compatibility tests.
- No milestone authorizes customer-data publication or production deployment.
