# Delivery companion backlog

The IDs originate in the open, unmerged
[PR #1](https://github.com/jonathan-vella/apex-as/pull/1), inspected at
`b86b394ecae468e401db35c55e19300a06ab52d6`. On 2026-10-29 the user clarified
that APEX AS helps partners create checklist-aligned artifacts during each
delivery, **not assess partners**. This is the locally adopted delivery-first
backlog; the PR proposal remains historical/unmerged, and no GitHub records
were changed.

AS-001/003/005 retain their distribution, compatibility and runtime findings.
AS-002 now concerns cited artifact guidance, not partner eligibility.
AS-004 covers project authoring/processing. AS-006 through AS-021 below are
reframed planned work, not claimed implementations of their original proposal
titles. In particular AS-008 is not a compliance engine, AS-012 is not an audit
exporter, AS-015 is not an authorized customer pilot and AS-018 is not portfolio
scoring. P0 = design/release safety gate; P1 = first usable delivery journey;
P2 = later expansion. IDs are local, not issue numbers.

## AS-001 - Prove native agent-plugin distribution

**Priority:** P0. **Milestone:** M0. **Depends on:** none.
**Status:** blocked; incomplete client acceptance gates.

| Original acceptance | Actual result |
|---|---|
| Authoritative references and tested version | Recorded in [findings](as-001-native-plugin-proof.md); VS Code 1.144.0 on Windows x64 |
| Install and invoke without containers | PASS for synthetic local-source proof: native Copilot read the file and returned 1 REFERENCED / 2 MISSING |
| Coexist with APEX, no overwrites | No APEX/core files edited; APEX co-discovery and functional coexistence not demonstrated |
| Verify removal; document cross-plugin invocation | BLOCKED: prior UI automation yielded to user input; follow-up has no native UI-control tool. Editor and CLI plugin inventories are documented as separate. Cross-plugin APEX invocation remains unverified/unused |
| Unsupported capabilities are blockers | No fabricated manifest dependencies, sibling-repository discovery or copy-based installation fallback |

Keep AS-001 open until install/invoke/permissions/remove observations and a
native APEX coexistence test are all recorded. Do not equate unrelated installed
plugins coexisting with proof of APEX coexistence.

The unattended follow-up confirmed real saved fixture-session events: selected
agent `apex-as-fixture`, `tools: ["read"]`, one successful `view` call of the fixture,
and two read/path permissions approved in manual mode (human response and host
policy). This is not a forbidden-tool denial test; see the diagnostic excerpt in
[findings](as-001-native-plugin-proof.md#unattended-follow-up-in-vs-code).

**User deferral (2026-10-29):** plugin install/removal will be addressed later.
Do not retry lifecycle changes during delivery-companion design work. The gate is
deferred, not passed or waived.

When resumed, provide a supported native client-control surface, or perform the
remaining steps interactively using the findings runbook. In the same editor inventory,
remove only the proof registration (already approved; source deletion is not),
verify exact plugin/agent disappearance, then inspect expanded tools and verify
native APEX coexistence at the pinned baseline. Last observed installed; no
removal was performed by this agent and the follow-up cannot re-read that UI.
No repeated fixture submission is needed to establish the successful run.

## AS-002 - Define cited Infra/Database artifact guidance

**Priority:** P0. **Milestone:** M0. **Depends on:** none.
**Status:** original D0-D6 guidance implemented with public source/version caveats;
no exhaustive control catalogue or resolution of disputed source labels.

| Acceptance | Result |
|---|---|
| Official source/provenance | User supplied correct Microsoft program URL and confirmed direct conversion from its linked public PDF. Link verified; independent byte equivalence and redistribution rights not established |
| Version record | Local V2.0 July-Dec 2026 header, inner Module B V1.9 and local hash retained; hold only disputed guidance, not generic drafting |
| Shared vs workload guidance | Foundation/ALZ artifacts distinct from migration artifacts; no partner Module A pass/waiver lookup required to use the companion |
| External ALZ | Owner-specific input/capture request and visible dependency, not an audit acceptability verdict or reason to mutate ALZ |
| Guidance publication | Original task/outlines with citations; source PDF, copied tables and reconstructed checklist excluded by default. Publicly available is not confidential and not automatically licensed for republishing |

`apex_as/guidance.json` supplies artifact purpose, broad source locator/version,
inputs, owner, capture moment and original document-review questions for all
eight artifacts. Guidance tests check shape, IDs, dependency order and roles.
Source-specific coverage/interpretation still needs maintainer review; no
PASS/compliance labels are emitted.
Partner standing, audit population/counting and audit date are not development
prerequisites. See [PRD](prd.md#interpretation-holds) for source-specific issues.

## AS-003 - Define the minimum APEX compatibility contract

**Priority:** P0. **Milestone:** M0. **Depends on:** none.
**Status:** pinned source review and candidate contract decision recorded;
real integration and runtime acceptance deferred.

No APEX contract is consumed by this proof. The exact upstream research baseline
and recall declaration are in [plan](plan.md). It is not a compatible-version
claim. Missing reference and incompatible fixture diagnostics are specified in
the agent; runtime negative-case behavior needs observation before it is claimed.
No private state access or Markdown-as-API is permitted.

| Acceptance | Scoped result |
|---|---|
| Exact initial baseline/recall version | Research/candidate baseline `504349259c26e36c750c7d6669c0b1de554e6b35`, recall `0.2.0`; schema/document blob identities in [plan](plan.md#pinned-public-interface-review). Not a supported integration pin |
| Artifact-only vs recall-connected | Optional future APEX adapter candidate is explicit schema-pinned `iac-contract-v1` planning context. Live recall remains unselected; standalone brief/narrative inputs are the first delivery path |
| No private state/modules or Markdown-as-API | Preserved; public schemas and `show <project> --json` documentation reviewed remotely only |
| Missing vs incompatible diagnostics | Source/access/identity/version and missing-context cases specified in [plan](plan.md#diagnostic-decisions), not implemented engine behavior |
| Neutral upstream needs | Explicit-root, read-only dependency/side-effect and output-identity contracts identified before live recall; no core modifications |

New finding: `files --json` can rebuild SQLite, `health --json` calls DB
initialization, and review-bearing `show --json` can invoke a Node validator.
`dependencies = []` does not mean all recall operations are non-mutating or
Python-only. Source inspection is not a live runtime acceptance test.

Next: before an optional APEX adapter implementation, validate the chosen
planning-context contract against disposable synthetic examples and an approved
runtime. Do not silently add recall execution or interpret Markdown as a stable
machine API. This adapter is not a prerequisite for standalone drafting.
Full AS-003 APEX compatibility acceptance remains open.

The [synthetic case specification](plan.md#synthetic-contract-validation-cases)
now covers happy/invalid/missing/inaccessible/wrong-project inputs, locator escape,
recall failure/side effects, authoring and privacy/guidance cases. FX-01's prior
native fixture observation remains unchanged. DC/local authoring cases are now
executed; native fixture negative cases and optional AC/RC adapter cases remain
specified, not executed. No adapter, schema-validator dependency or evidence engine added.

## AS-004 - Define privacy, isolation and evidence ownership

**Priority:** P0. **Milestone:** M0. **Depends on:** none.
**Status:** synthetic local path/write/record controls implemented and tested;
no customer's processing/write/release authorization or production policy enforcement.

| Acceptance | Result |
|---|---|
| Separate state and authoritative ownership | Add-on state separate from APEX; actual drafts go to an approved project document location, potentially a private organization-controlled repo, never this public product repo |
| Sources/drafts/release | Distinct read/model-processing/write/revise/customer-release scope; preview/diff and revision lineage specified. Actual customer responses are not generated signatures; audit submission is not a product action |
| Required identifiers | Per-field disclosure versus source-specific identity obligations; no blanket anonymization or public cross-customer joins |
| Inaccessible/untrusted content | Local CLI tests cover missing/simulated denied input, reparse/traversal refusal, literal data rendering and no reference following. Semantic secret detection, model/native tool enforcement and real-data policy not tested |
| Synthetic fixture rules | Invented-only development authorized; intended product supports real project artifacts with engagement-specific permissions. Design is not legal/customer consent |

Added `/tmp/` Git exclusion and a static regression check for that rule. The
public local checklist reference remains within the registered plugin root; do not
copy/distribute that excluded content. File-access isolation, safe release packaging and
host/model log retention are not solved by `.gitignore`.
Four existing-runner tests, actual Git exclusion/non-tracking checks, 11-file
whitespace/link/anchor checks and four unchanged-input fingerprints passed;
see [validation limits](prd.md#validation-of-this-foundation-change).

Next real-data gate: named custodian/organizational authorization, exact scope and
processing destinations, private storage/access policy, concrete retention/hold/
deletion decisions, field-level export approval and actual isolation tests.
Development remains synthetic-only; real artifacts are an intended product use,
not prohibited forever. No customer credentials are needed to build the generic
workflow.

## AS-005 - Choose host runtime and licensing strategy

**Priority:** P0. **Milestone:** M0. **Depends on:** AS-001, AS-003.
**Status:** dependency-free Python delivery runtime selected and locally tested;
native plugin support/licensing and any optional APEX runtime remain open.

The proof agent is still prompt-only. The delivery CLI targets Python 3.11+,
standard library only, tested on native Windows/Python 3.15.0. No packages/APEX
dependencies were installed, and no global host configuration changed. Other
Python versions/platforms, clean-host native plugin support and licensing remain
release gates, not blockers to local synthetic CLI use.

The [host matrix and acquisition/license gates](plan.md#host-and-dependency-matrix)
separate current plugin, contributor tests, future artifact-only and conditional
recall requirements. APEX's MIT source/recall declarations were verified at the
pin; no third-party package or schema is bundled. APEX AS licensing is undecided.
A local Python runtime module was added; no dependency manager, acquisition,
pip/npm package or installer was introduced.

Next: resume the deferred native lifecycle tests later, test additional declared
runtime/host versions before claiming them, and decide product licensing before release.
Do not claim macOS/Linux, clean-host support or a Python-only recall integration.

## AS-006 - Specify project artifact lifecycle and reusable outlines

**Priority:** P1. **Milestone:** M0 design / M1 implementation.
**Depends on:** AS-002, AS-004 decisions for the selected slice.
**Status:** implemented for synthetic local delivery: eight original guidance
outlines, brief/events/journal contracts and three reusable workload examples.

- Use the [D0-D6 workflow](plan.md#first-infradatabase-project-workflow), ART-01..08
  and independent document/action/execution/customer-decision/freshness states.
- Specify project/lane/input/output/revision/owner metadata; no partner score.
- Keep original generic outlines distinct from public-source citations and actual
  results. No inventory/acceptance fact invented to make a template look complete.
- Define new-project and user-edited resume behavior with explicit file scope.

## AS-007 - Add optional read-only APEX artifact reuse

**Priority:** P1. **Milestone:** M3. **Depends on:** AS-003, AS-005, AS-006, AS-011.
**Status:** candidate source review only; adapter deferred.

- Consume only explicit authorized versioned inputs, initially the pinned planning
  JSON; surface wrong-project/version/access failures.
- Reuse a source by reference rather than duplicate/overwrite core artifacts;
  no direct session-state access, private imports or Markdown-as-API.
- Standalone generation remains usable without the adapter. Recall is separate
  and unselected until side effects/runtime/root binding are tested.

## AS-008 - Implement bounded document drafting and review

**Priority:** P1. **Milestone:** M1. **Depends on:** AS-004, AS-005, AS-006 slice decisions.
**Status:** implemented and tested in the local synthetic CLI; native agent authoring unverified.

- Preview ART-01/02 from an explicit brief; support a named approved output
  location, create/update scope and collision handling.
- Separate assumptions, supplied facts, pending questions and capture placeholders;
  checks concern document completeness, not specialization eligibility.
- Keep input/core files unchanged; preserve edits/history on resume, reject path
  escapes and never mark generated results/acceptance as real.
- Tests must observe actual allowed writes and failures, not only agent prose.

## AS-009 - Build synthetic delivery acceptance examples

**Priority:** P1. **Milestone:** M1. **Depends on:** AS-004, AS-006.
**Status:** implemented synthetic mixed/infra/database briefs and runtime failure
tests; no customer-derived data or native-agent failure-test claim.

- Include infra-only, database-only and mixed projects, external platform owner,
  missing input, denied access, wrong project/version and embedded instructions.
- Exercise user edits, output collisions, changed source after review, pending
  results and absent/rejected customer response.
- Retain invented labels/IDs and expected outcomes. No customer-derived data or
  copied checklist catalogue. A second project must start without prior facts.

## AS-010 - Add dependency-aware revision and capture traceability

**Priority:** P1. **Milestone:** M2. **Depends on:** AS-006, AS-008, AS-009.
**Status:** implemented append-only revisions, exact event binding and
dependency/source/provenance-aware refresh; tested locally.

- Record source/task/template versions, artifact parents and actual run facts.
- Changes flag impacted review/acceptance for reconfirmation while preserving
  historical responses/results; no automatic restamping.
- Distinguish missing, inaccessible, changed and disputed sources; hashes are
  integrity hints, not authority or consent.

## AS-011 - Deliver the first companion slice: kickoff and discovery

**Priority:** P1. **Milestone:** M1. **Depends on:** AS-002 D0-D1 guidance, AS-008, AS-009.
**Status:** standalone synthetic first slice implemented/tested; extended through
ART-08. No native Copilot authoring invocation claimed.

- Explicit synthetic project brief -> ART-01 artifact plan and ART-02 workload
  assessment-output draft for the selected lanes, with usable owner actions.
- External ALZ creates a scoped input request, no cloud operation or exemption.
- Outputs are DRAFT, results NOT_RECORDED, customer decisions not accepted.
- Prove useful standalone behavior and repeat on a second project without
  copying customer/project facts. No partner verdict or compliance engine.

## AS-012 - Assemble authorized operational handover

**Priority:** P1. **Milestone:** M2. **Depends on:** AS-004, AS-010, AS-016.
**Status:** local synthetic operational index and release-record gate implemented;
no external file transfer, customer handover or audit export performed.

- ART-07/08 use current reviewed documents, actual captured facts and unresolved
  actions; exclude unauthorized sources/identifiers.
- Preview exact included revisions and recipients; release authorization distinct
  from writing locally or receiving customer acceptance.
- No audit submission, automatic redaction-as-compliance claim or fabricated sign-off.

## AS-013 - Package the native authoring companion

**Priority:** P1. **Milestone:** M3 release gate. **Depends on:** AS-001, AS-005, AS-011.
**Status:** explicit allowlist source archive implemented/tested; native authoring
plugin wrapper, its tool availability and lifecycle remain blocked/deferred.

- Preserve proven format and unique names; do not silently broaden the fixture
  agent's permissions.
- Test authoring-tool availability/approvals and clean source-only payload.
- Preserve user/core files across update/removal; no required container, APEX
  install, automatic dependency acquisition or cross-plugin dispatch.

## AS-014 - Test declared hosts and authoring failure boundaries

**Priority:** P1. **Milestone:** M3. **Depends on:** AS-009, AS-012, AS-013.
**Status:** native Windows CLI journey and path/collision/record tests executed;
full native plugin and cross-host lifecycle still unverified.

- Run clean native install/invoke/author/revise/handover/update/remove journey on
  declared hosts and harness versions; record unsupported combinations.
- Verify path/project isolation, denied input/write access, injections, revoked
  authorization, collisions and no Azure/APEX mutations.
- No host support claim from manifest validity, Git ignore or authored instructions.

## AS-015 - Rehearse a complete synthetic project delivery

**Priority:** P1. **Milestone:** M3. **Depends on:** AS-014.
**Status:** complete local CLI rehearsal executed across three synthetic projects;
independent practitioner usefulness review and native plugin journey remain open.

- Replay D0-D6 with separately supplied synthetic execution and customer decisions,
  preserving their provenance and open actions.
- Have another practitioner review artifact usefulness, capture timing and honest
  unknowns. Measure corrections/omissions, not partner readiness.
- Any later customer pilot is separate authorization, not granted by this item.

## AS-016 - Extend in-delivery guidance through design and validation

**Priority:** P1. **Milestone:** M2. **Depends on:** AS-010, AS-011.
**Status:** ART-03..06 structured drafting and supplied synthetic capture/decision
records implemented/tested; delivery execution is still practitioner-owned.

- Draft design/decision and migration/validation plans from selected current inputs.
- Prepare capture records before the real events; incorporate only supplied run
  outputs and authentic response references afterward.
- Practitioner/APEX owners execute delivery under existing approvals. Manual
  bounded requests suffice; plugin-to-plugin calls are not prerequisites.

## AS-017 - Package a repeatable Infra/Database delivery kit

**Priority:** P2. **Milestone:** M3. **Depends on:** AS-015, AS-016.
**Status:** original reusable guidance, three briefs and CLI rehearsal/source-kit
packaging implemented; independent practitioner reuse and quantitative measures open.

- Reuse the method on a new project with fresh scope, lanes, owners and state.
- Include capture/checkpoint instructions, variant selection and honest external
  dependencies; do not copy previous customer artifacts or approvals.
- Measure reuse against an agreed denominator; no assumed percentage.

## AS-018 - Maintain artifacts across project changes

**Priority:** P2. **Milestone:** M3. **Depends on:** AS-010, AS-012, AS-015.
**Status:** input/dependency/user-edit revisions and current/historical decision
separation implemented for synthetic records. Retention/withdrawal policy for
real use remains unimplemented; no portfolio-scoring scope.

- Reopen only affected document tasks after material design/delivery changes,
  preserve originals/history and request current review where needed.
- Respect source withdrawal/retention and current handover release scope.
- No central customer corpus, cross-partner ranking or eligibility population count.

## AS-019 - Add another delivery-guidance family

**Priority:** P2. **Milestone:** M4. **Depends on:** AS-002, AS-017.
**Status:** deferred; Infra/Database remains the first family.

- Confirm source/version and permitted use for the new family.
- Reuse shared artifact methods only where applicable; keep differing guidance
  explicit and independently test synthetic examples.
- Do not silently migrate existing project decisions/templates or assume a waiver.

## AS-020 - Establish authoring compatibility and release checks

**Priority:** P1. **Milestone:** M3. **Depends on:** AS-009, AS-013.
**Status:** local runtime/guidance/archive regression tests and source manifest
implemented; hosted CI and native release acceptance not implemented.

- Test native companion runtime, payload exclusions and synthetic authoring cases.
- Add exact APEX adapter matrix only if AS-007 ships; do not make APEX a dependency
  of standalone drafting. Flag incompatible sources without silent repair.
- Publish guidance/template changes and upgrade impact; never update customer
  workspaces or rewrite their reviewed artifacts automatically.

## AS-021 - Maintain distribution, guidance and ownership

**Priority:** P2. **Milestone:** M4. **Depends on:** AS-005, AS-014, AS-017, AS-020.
**Status:** planned; product license unresolved.

- Declare license/support/maintainers and only verified installation/use limits.
- Assign checklist-change intake and track source-version ambiguities without
  republishing the source or retroactively approving affected drafts.
- Document project-data handling/removal expectations and preserve the boundary:
  delivery artifact assistance, not Microsoft/auditor endorsement or partner assessment.

## Implementation order

1. **Implemented synthetic local journey:** AS-002 original guidance, AS-006/009
   contracts/examples, AS-008/011 first slice, AS-010/016/012 revision/capture/
   handover behavior. All eight artifacts run through preview/apply/status.
2. **Executed local rehearsal/reuse:** mixed project, eight supplied synthetic
   event records, handover index, practitioner edit/reconfirmation, fresh
   infra-only/database-only projects. AS-015/017 independent practitioner
   usefulness and complete native release are not claimed.
3. **Implemented source-kit controls:** explicit archive allowlist/manifest and
   local tests for AS-013/020. No install, removal, update or hosted CI performed.
4. **Remaining release gates:** resume AS-001, complete native portions of
   AS-005/013/014, license/support decisions and independent practitioner review.
   AS-007 optional APEX adapter/recall, AS-019 new families and production
   privacy/retention/customer operations remain deferred or separately gated.

Independent synthetic design/authoring experiments can progress while AS-001
is deferred; no supported native release is claimed before its gates pass.
Specific project data/outputs need engagement authorization only when used.
No partner standing, customer audit report or cloud credential is required to
build this reusable companion. An assessment/portfolio engine is not backlog work.

## Implementation evidence and residual boundaries

The runnable commands and contracts are in
[README](../README.md#run-the-synthetic-delivery-kit); requirement mapping,
executed failure cases and limitations are in
[plan](plan.md#implemented-synthetic-delivery-runtime).
Tests run via the existing standard-library unittest runner, with no package
installation. Independent correctness review issues have regression tests.

The Windows junction test is real; symbolic-link creation is one explicit
host-privilege skip. Denied I/O tests simulate PermissionError and do not audit
ACL policy. The deterministic tool has no model/network/external execution;
no inference of LLM/native-agent enforcement. All input events are unverified
supplied synthetic claims, not authenticated decisions. Real-data mode is refused,
and no pending product/native gate was marked complete from CLI success.
