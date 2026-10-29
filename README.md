# APEX AS

An optional agent-plugin add-on for Azure specialization evidence and repeatable
partner delivery with [APEX](https://github.com/jonathan-vella/apex).

**Status: planning.** This repository contains the product definition and delivery
backlog. There is no installable plugin or implemented evidence engine yet.

## Purpose

Help Microsoft partners use a highly repeatable delivery method while collecting
the customer-specific evidence needed for Azure specialization assessments.

Reuse the process, approved workload patterns and evidence-capture structures.
Do not reuse another customer's approvals, deployment results or compliance
conclusions.

APEX remains useful independently, including for customers who have no
specialization objective. APEX AS depends on APEX; APEX does not depend on APEX AS.

## Product boundaries

- Distribute through agent plugins for the supported VS Code Copilot environment.
- Do not require a devcontainer, Docker or a container runtime.
- Keep specialization profiles, evidence state and audit preparation outside APEX
  core.
- Consume existing APEX artifacts and documented interfaces, not copied core
  agents or private Python internals.
- Depend on an existing Azure Landing Zone (ALZ); never deploy or mutate it.
- Keep customer evidence in customer-approved storage, not this public repository.
- Preserve human approvals and existing APEX review gates.
- Report evidence gaps honestly; do not claim to certify a partner or guarantee
  an audit result.

Plugin packaging, installation, discovery and coexistence must be demonstrated in
the target client before publishing installation instructions. Plugin distribution
does not imply that every supporting tool is already installed on the host.

## Proposed experience

1. Select an engagement, specialization profile and explicit input mode.
2. Check compatibility and authorized evidence sources.
3. Map available artifacts to controls and identify missing evidence.
4. Guide evidence collection through existing delivery activities.
5. Assemble a human-reviewed evidence index and controlled audit export.

Start with read-only assessment of one authorized historical engagement. Add
in-delivery integration only after that assessment is useful and reliable.

## Documents

| Document | Purpose |
|---|---|
| [Plan](docs/plan.md) | Architecture, dependency model and implementation approach |
| [PRD](docs/prd.md) | Product requirements, boundaries and acceptance criteria |
| [Roadmap](docs/roadmap.md) | Milestones and evidence-based exit gates |
| [Backlog](docs/backlog.md) | Prioritized work items with dependencies |

## Compatibility and installation

No supported client or APEX release has been certified yet. The first milestone
will verify agent-plugin support, host requirements and the minimum APEX contract.

The proposed integration uses:

- Versioned APEX artifacts for engagement evidence.
- Documented `apex-recall` JSON commands when live session context is selected.
- A declared compatibility matrix and exact resolved installation pins.
- Separate add-on state, without direct reads or writes of APEX's session-state
  file.

There are no executable installation commands at this stage. Do not copy plugin
files into an existing APEX project as an undocumented installation workaround.

## Contributing and licensing

Use the backlog to discuss scope before implementation. Never contribute customer
data, credentials, restricted checklist copies or unapproved third-party content.

A license has not yet been selected. Public visibility alone does not grant an
open-source license; licensing and redistribution decisions precede distribution.
