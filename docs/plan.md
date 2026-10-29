# Delivery companion plan and native proof

The full product plan in
[PR #1](https://github.com/jonathan-vella/apex-as/pull/1) remains an unmerged
proposal, inspected at `b86b394ecae468e401db35c55e19300a06ab52d6`.
The user clarified that APEX AS helps partners create checklist-aligned artifacts
through project delivery, not assess partners. This plan specifies that first
workflow and retains the actual plugin/contract research below. It does not
change the native proof agent, implement an APEX adapter or modify APEX core.
The standalone synthetic runtime is now implemented and exercised; see
[implementation evidence](#implemented-synthetic-delivery-runtime). Workflow
tables below remain the design baseline; the implementation section specifies
which dimensions and constraints are actually enforced.

See [product definition](prd.md#product-purpose-and-boundaries),
[source record](prd.md#as-002-first-profile-and-source-authority) and
[privacy boundaries](prd.md#as-004-privacy-isolation-and-evidence-ownership)
for the distinction between synthetic development and authorized production use.
Module A partner standing and an audit date are not drafting prerequisites.

## First Infra/Database project workflow

**Design baseline:** `delivery-workflow-v0.1`; runtime contracts are separately
versioned as delivery brief/events/state/preview/status v1.
Work on one migration project at a time. The companion produces drafts, capture
structures and owner actions; delivery practitioners run the work and supply
actual results. A checklist citation explains why an artifact is useful, not
that a partner meets a control. No completeness or compliance verdict is issued.

### Start and resume

Minimum explicit input:

- opaque project ID and scope; synthetic marker for development; current stage
  and whether this is new work or a revision of an existing document;
- workload lanes: infrastructure, database or both, with source/target and
  environments identified at the level known; unknown values remain unknown;
- delivery lead, specialist and reviewer roles, customer decision owner and
  ALZ/platform owner (external allowed); no invented names or acceptance;
- authorized input files or a user-supplied brief, source guidance version/date
  and approved processing boundary. An unresolved reference interpretation stays
  local to the affected guidance, not a ban on generic drafting;
- requested artifact/task and, before writing, an explicit output directory,
  allowed new files/revisions and approval policy. Preview in chat alone does
  not authorize persistent writes or external release.

No automatic APEX/sibling discovery, partner qualification lookup or CLI
dependency preflight is required. If a necessary fact is absent, draft the
independent sections with marked assumptions and a scoped owner request.
Block only sections/actions dependent on that fact. If input access or model
processing is not authorized, do not inspect it to produce the draft.

Resume from the user-selected current document and explicit project metadata.
Identify the requested stage and changes since that revision. Do not read private
APEX session state or infer completion from filenames/latest timestamps. Add-on
tasks/revisions live separately from APEX state; core artifacts remain owned
by their existing delivery team.

### Artifact and capture map

These are original delivery outlines, not a transcription of the Microsoft
checklist or an exhaustive rules catalogue. The IDs are APEX AS design IDs, not
Microsoft controls or required core filenames. One source artifact may satisfy
several delivery needs; reuse before creating another document.

| Stage / artifact | Inputs and useful original outline | Accountable owner / capture point | Completion boundary |
|---|---|---|---|
| D0 / ART-01 Project artifact plan | Brief, lane/environment scope, guidance source/version, existing document inventory. Outline: artifact ID, purpose, source citation, scope/lane, owner/reviewer, prerequisite, capture event, target location and open action | Delivery lead at kickoff; customer and external owners confirm their responsibilities | A reviewable plan can exist with pending owner actions. It is not a partner score or promise every checklist requirement is satisfied |
| D1 / ART-02 Workload assessment output | Authorized inventory/tool outputs and interviews. Outline: source baseline, dependencies, sizing/constraints, migration options, risks, licensing/cost assumptions, backup/recovery needs and questions | Infra/database specialist during discovery; attach or reference real assessment output only after it exists | Practitioner reviews findings against cited inputs. Unknown inventory stays pending; a completed draft does not mean an executed assessment or completed project |
| D2 / ART-03 Design and decision record | Reviewed assessment, constraints, architecture/ALZ inputs and requirements. Outline: target design, options/rationale, security/network/data boundaries, cost/reliability assumptions, external interfaces and deviations requiring owner decisions | Architect and platform/database owner during design; preserve actual design/review decisions | Mark assumptions and unresolved dependencies. An accepted design is not a deployed system or independent audit acceptance |
| D3 / ART-04 Migration and validation plan | Selected design, authorized planning artifacts, change controls and customer window. Outline: waves/dependencies, method/tool choice, prerequisites, backup/rollback, entry/exit conditions, test cases, capture checklist and acceptance-request owner | Migration lead before pilot/cutover; infra/database specialists own their lanes | Plan reviewed against current design and customer constraints; no permission to run it is granted by a document or checklist citation |
| D4 / ART-05 Execution capture record | Actual practitioner/tool output, change/run ID, environment, times, planned versus observed actions, exceptions and rollback facts | Authorized delivery executor at each actual run; companion prepares structure and incorporates explicitly supplied results | Empty result fields stay pending. Plans/what-if and generated narratives cannot be converted into production execution, success or consent |
| D5 / ART-06 Service validation and acceptance request | Planned test criteria, observed results, unresolved defects and current release scope. Outline: test/run/source links, expected/observed values, variance/action owner, acceptance-request text and customer response reference | Test/service owner after execution; customer alone supplies their actual decision | Test outcomes and customer response are separate. A draft email or unchecked acceptance field is not sign-off |
| D6 / ART-07 Operational handover | Current design/as-built facts, verified runbooks, operations responsibilities, monitoring/backup/recovery procedures, known limitations and support contacts | Service/operations owner before BAU handover; record customer/operations acknowledgment if received | Handover completeness and recipient authorization reviewed for current revisions. A runbook is not proof its recovery procedure was tested |
| D6 / ART-08 Delivery record index | Selected current artifacts, source/derivative links, revisions, factual results, decisions, open actions and permitted recipients | Delivery lead at project close and each material change | Index only authorized scope; preserve pending items and actual release record. Not an audit export, portfolio assessment or certification |

Every artifact header should identify project/lane/environment, artifact ID/title,
revision and parent revision, purpose/stage, guidance URL and observed source
version, input identities/revisions, author/reviewer, assumptions/open actions and
data classification. Capture records additionally identify event/time/source
and who supplied the result. Customer decisions identify the actual actor,
date, scope, referenced artifact revision and response location where permitted.
All these are conceptual fields, not a released JSON contract.

### Workload lanes and external ALZ

An infrastructure-only project gets the relevant infra tasks; a database-only
project gets database tasks; a mixed project shares common artifacts but keeps
separate lane inputs, tests, results and cutover decisions. These lanes describe
the delivered project, not whether one project satisfies a specialization's
portfolio/scenario requirements. Do not invent a second workload or customer.

For an externally owned ALZ, add an interface/request entry to ART-01/03:
responsible owner, requested design/configuration/deployment/review records,
purpose, project/environment, approved sharing route, needed-by stage, received
source/revision and access/decision state. The request asks the owner to supply
actual records or state a limitation; it never asks the model to fabricate them.
Keep local delivery work independent where possible. If a deployment prerequisite
is missing, mark that downstream action blocked, not the partner as failing.
Never deploy/modify an ALZ, run discovery or claim an exemption to close a
documentation action.

For a partner-owned ALZ, use the same provenance/capture principles; ownership
does not prove an execution occurred or that a document is externally accepted.
Uncertain checklist interpretation creates an owner clarification action, not an
automatic rejection of third-party evidence.

### Drafting, writes and status semantics

Use independent dimensions rather than one misleading COMPLETE or PASS flag:

| Dimension | Proposed values / rule |
|---|---|
| Document lifecycle | PLANNED, DRAFT, IN_REVIEW, REVIEWED, SUPERSEDED. REVIEWED requires a real reviewer record for that revision; generation alone only produces DRAFT |
| Dependency/action | OPEN, BLOCKED, RESOLVED or NOT_APPLICABLE with recorded owner/rationale. Missing input and inaccessible input are different reasons; no model-inferred waiver |
| Factual execution | NOT_RECORDED, RECORDED or DISPUTED, with source event/run provenance. Review of a plan cannot change this dimension |
| Customer decision | NOT_REQUESTED, PENDING, ACCEPTED, REJECTED or NEEDS_RECONFIRMATION. ACCEPTED requires an authentic supplied response scoped to the current revision, not a generated signature/date |
| Source freshness | CURRENT, CHANGED or UNVERIFIED relative to recorded inputs; no universal time limit inferred from a hash |
| Release | NOT_RELEASED or RELEASE_RECORDED, scoped to approved artifacts/recipients. A sent request is not an accepted delivery |

Before any future write, show the selected task, inputs, create/update paths and
preview/diff. A scoped authorization may cover several named new drafts; it does
not permit arbitrary overwrites. An existing user/APEX-owned document is reused
by reference, or revised only with explicit write scope and a diff preserving
user edits/history. An output collision must ask for a decision or create a
separately approved revision, never silently replace it.

When an input changes, identify impacted draft sections, mark review context
stale and require the affected owner to reconfirm it. Preserve historical
decisions and execution facts; do not erase them or replay old acceptance
against a materially changed output. No automatic APEX workflow transitions.
Retention/authorization withdrawal may block use even if bytes are unchanged.

### APEX and practitioner responsibility

APEX AS owns artifact guidance, original drafts and capture prompts, not cloud
execution or authoritative core workflow state. APEX/practitioners retain
requirements, architecture, governance, planning, coding, deployment and review
responsibility under their existing approvals. The delivery lead can take a
scoped request to the normal APEX role manually. No direct plugin-to-plugin task
call or mandatory extra core step is required.

Stand-alone structured briefs and explicitly selected project documents are the
first input path. Existing Markdown documents may be used as authorized narrative
sources for drafting, not parsed as a stable APEX machine API. An optional later
APEX JSON adapter can reuse the pinned planning contract below; it cannot supply
actual migration, testing or customer acceptance facts that the contract lacks.
The existing fixture agent remains read-only and is not changed into this
authoring companion by this specification.

### Synthetic walkthrough and first-slice acceptance

**Originally desk-designed; now replayed through the local CLI:** invented project `demo-delivery-01` describes an
invented application host and database to a fictitious target. Its ALZ owner is
external. The supplied brief contains no execution output, customer identities,
credentials or sign-offs.

1. D0 creates an artifact plan for both lanes and an external-platform input
   request. Missing platform records become owned actions, not inferred facts.
2. D1 drafts the workload assessment output from the brief. Unprovided inventory,
   costs and assessment-tool results are explicitly pending; no invented metrics.
3. D2/3 may draft independent design/migration sections with marked assumptions.
   The unresolved platform prerequisite blocks only the dependent delivery action.
4. D4 prepares an empty capture record. In a later synthetic exercise, only an
   explicitly supplied invented run result can change factual execution status.
5. D5 prepares validation cases and an acceptance request. No response means
   PENDING/NOT_REQUESTED as appropriate, never ACCEPTED.
6. If the design changes, affected review/acceptance needs reconfirmation while
   prior run facts remain historical records. Handover indexes current documents
   plus open actions; it does not announce a completed migration.
7. Repeat on `demo-delivery-02` with a database-only brief and new owner IDs. No
   prior project facts, responses or output paths may carry over.

The initial D0-D1 slice (ART-01/02) and its D2-D6 extensions now run independently
of a JSON adapter/recall. Their acceptance checks include:

- one explicit synthetic brief produces a useful reviewable artifact plan and
  assessment-output draft for the selected lanes, not a checklist reproduction;
- all unknown facts are placeholders/owner actions with citations to selected
  inputs; external ALZ produces a request, never a deployment command;
- input files and existing user drafts stay unchanged; only named authorized
  output files are created after preview; no Azure/core/session writes;
- new outputs are DRAFT, factual results NOT_RECORDED and customer decisions
  not accepted; no partner score/audit-readiness label;
- missing, denied, incompatible and instruction-injected inputs are visible
  bounded failures/actions; one unavailable source does not invent its contents;
- retry/resume preserves user edits/revisions, and a second project starts with
  fresh identity/scope rather than a copied first-project acceptance state.

Runtime validation of authoring, write isolation and error handling is required
for each host. The local CLI has exercised these behaviors; the native plugin
proof is still not an authoring runtime. Follow
[backlog](backlog.md#implementation-order) for completed and release-blocked work.
No partner-assessment or portfolio engine was introduced.

## Implemented synthetic delivery runtime

### Architecture and requirement mapping

`apex_as` uses the Python standard library only. There is no UI, database,
network client, command execution from input, model call, APEX install or recall
dependency. Python 3.11+ is the code target; native execution was tested on
Windows 10.0.26300/Python 3.15.0 only. This is the delivery tool's runtime decision,
not a new requirement for the unchanged prompt-only proof agent.

| Requirement | Implementation | Evidence |
|---|---|---|
| DP-01/02/04 | Strict synthetic project brief, original `guidance.json` with eight outlines, source URL/labels/locators, shared/lane-specific supplied narrative and PENDING owner actions | Guidance tests; all-artifact and lane-specific runtime tests |
| DP-03/06 | Selected source paths only; read-only originals, preview/diffs plus current digest, disjoint roots, exclusive new revision writes and explicit carry-forward of user edits | CLI preview/apply, source guards, output-collision, path/junction, denied-write rollback and user-edit tests |
| DP-05 | Blank capture structures plus separate explicit synthetic execution/customer/review/release events; exact revision/hash binding | Pending/rejected/accepted/disputed outcomes, partial-lane execution and stale-event tests |
| DP-07 | Append-only state snapshots/events, dependency hashes and recipe identities; changed inputs/user edits propagate reconfirmation; prior facts retained | Revision/staleness, immutable event replay, journal validation and event-provenance-index tests |
| DP-08/09 | External ALZ request, independent workload lanes and project-ID directories; fresh event history per project | Mixed/infra/database examples and three-project CLI rehearsal |
| DP-10 | ART-08 indexes current revisions, document/exec/customer/release state and supplied event provenance; records local synthetic release only after exact review | Release gate and handover index assertions; no files sent |
| DP-11 | Standalone explicit brief/source path. No APEX adapter, private state or cross-plugin calls | All local runtime tests and CLI rehearsal run without APEX |
| DP-12 | Native Python CLI run without containers; source-only archive allowlist tested | CLI rehearsal/package tests; native plugin authoring/update/removal still unverified/deferred |

### Commands and persistence

See [README](../README.md#run-the-synthetic-delivery-kit) for complete commands.
`preview` returns proposed file text/unified diffs, events, state snapshot and
SHA-256 approval. `apply` recomputes from the same explicit arguments; an approval
for different content or paths is refused. It rechecks source/current-document/
state fingerprints before writing, takes an exclusive project writer lock and
only creates new revision files. No user-authored file, prior state or prior
document is overwritten.

Inputs, documents and state roots must already exist, be absolute and be
pairwise disjoint; documents/state must be outside the product tree and protected
core/config locations. Named sources remain within the input root, without
parent/hidden/core-session paths or reparse traversal. Read/parse failures are
errors, not missing-success substitutions. Source excerpts are literal supplied
data: they are copied only into the selected draft, never executed or followed.
Unknown narrative keys are rejected instead of silently dropped.

New journal snapshots live at `<state>/<project>/r000001.json`; new documents
at `<documents>/<project>/r000001/ART-01.md`, etc. A snapshot holds current
artifact revision/content/recipe/dependency hashes, immutable supplied records
and a link hash to the previous snapshot. It is local trusted state, not signed,
encrypted or identity-authenticated storage. It stops accidental history edits
and mismatched project/destination reuse; it cannot protect against a malicious
operator rewriting a complete chain.

Event capture and authoring are separate preview/apply operations. Events require
synthetic-only references, actor, time, project, revision/hash and lane scope.
Execution can be partial/disputed by lane; review/customer/release cover the
selected document's lanes. Release records require an earlier current-revision
review and explicit recipients. An event does not rewrite a capture form: the
journal and `status` hold supplied observations, and refreshing ART-08 exposes
their provenance. A refreshed document is DRAFT and requires new review;
customer history is retained but its decision needs reconfirmation.

The implementation supports DRAFT/REVIEWED documents (historical revisions are
retained, not renamed), current/changed source context, lane-aware factual
recording, current or stale customer decisions and local release receipts.
It does not implement a general task-state machine, interactive LLM composition,
customer identity authentication, automatic applicability rules or delivery
execution. PENDING actions in the original drafts are practitioner work, not
automatic success. A user can edit a draft; the next update requires explicit
carry-forward and produces a separate revision with that literal prior content.

### Executed acceptance and limitations

The existing unittest runner now exercises actual output content, first-slice
and eight-artifact generation, three workload/project variants, immutable
revision/source preservation, exact preview authorization, selected source
escaping, missing and simulated denied access, malformed briefs/events/state,
wrong project/version, path escapes, output collisions, user-edited resume,
dependency staleness, partial execution, pending/rejected/accepted customer
records, release review/recipient checks and handover-index provenance refresh.
Input/state/document size limits block before successful unreadable-state
publication. Ordinary write failure cleans up only newly owned files.

`python -B -m apex_as.rehearse` launches the actual CLI for D0-D6, supplies eight
invented event records, refreshes the handover index, makes a practitioner edit,
reconfirms affected state, then repeats on fresh infra-only/database-only briefs.
A retained run completed under the session workspace, outside this repository.
It produced real Markdown drafts/journal files, not just a desk simulation.
It did not perform a migration, contact a customer, send a handover or test native
Copilot authoring.

A real Windows junction-boundary test passed. Symbolic-link creation on this host
requires an unavailable privilege, so that one creation-based test is explicitly
skipped; no privilege/settings changes were attempted. Denied read/write tests
are deterministic simulated OS failures, not an ACL policy audit.

Final local validation: `python -B -m unittest discover -s tests -v` ran 33 tests:
32 passed, zero failures/errors, one symbolic-link privilege skip. The final CLI
rehearsal passed on all three projects. Whitespace, relative links and heading
anchors passed across 23 authored files, product/artifact/backlog coverage and
dependency acyclicity passed, and the original manifest, proof agent, proof
fixture and local checklist SHA-256 fingerprints were unchanged. The excluded
reference remains untracked. No package installation, commit, push, PR, remote
change or plugin lifecycle action was performed.

Exclusive writes, locks and hash guards are accidental-mutation defenses, not
OS sandboxing or defense against hostile local path substitution races.
Power loss can leave a partial revision/lock; the next operation must report the
conflict and require manual inspection. No automatic backup restore, repair or
deletion of unknown files is provided. Each input/document/state snapshot is
limited to 256,000 bytes; history is never silently pruned. No performance or
large-engagement production claim is made.

Real project processing is currently refused (`synthetic` must be true). A flag
cannot detect mislabeled customer content, so actual customer material remains
prohibited in this development environment. The privacy/organizational gate
for future real use, license decision and native authoring permissions/lifecycle
tests remain outstanding. They do not invalidate the local synthetic kit.

### Feasible source packaging

`python -B -m apex_as.package` previews an explicit source allowlist and creates
a new zip only with its current approval digest. It includes runtime/guidance,
authored fixtures/tests/docs and the unchanged proof manifest/agent; excludes
`tmp`, checklist content, caches and Git/project state. Tests inspect archive
members and per-file hashes. It is a source kit, not a native authoring-plugin
release or a change to the installed plugin. Public distribution is still held
for licensing and native release acceptance.

## Packaging decision

Use the documented Agent Plugins 1.0 root `plugin.json` and Copilot-specific
`com.github.copilot/agents` directory. One manifest and one agent are sufficient;
no marketplace, VSIX, hooks, MCP server or build step is needed for this spike.
The installed agent takes an explicit fixture path and returns text in chat.
Do not rely on plugin-root placeholder expansion inside agent prose.

The unique plugin/agent names avoid intentionally replacing APEX roles.
No `.github/agents`, user agents or APEX files are overwritten. Local installation
changes the host's plugin inventory; it is not a zero-state-change operation.
The agent itself owns no persistent add-on state. VS Code retains its own
installation and chat state, outside APEX.

## AS-003: minimum contract decision

The proof consumes **no APEX contracts** and requires no APEX installation.
Its only input contract is `apex-as.synthetic-proof/v1`, owned here and explicitly
not a stable APEX evidence schema. Null references are gaps; wrong contract or
malformed item fields are incompatibility, not evidence gaps.

The inspected upstream baseline is
[`jonathan-vella/apex@504349259c26e36c750c7d6669c0b1de554e6b35`](https://github.com/jonathan-vella/apex/tree/504349259c26e36c750c7d6669c0b1de554e6b35).
Its README directs users through the Accelerator and a devcontainer; its tree has
no plugin manifest. This is a research baseline, **not a supported integration pin**.
Its `tools/apex-recall/pyproject.toml` declares recall `0.2.0`, Python `>=3.14`
and no runtime package dependencies. None was installed or called.

Real artifact-only integration needs an explicitly authorized path and a selected,
versioned artifact contract, validated against an exact APEX revision.
Recall-connected integration is separate and deferred; it needs exact documented
JSON commands and tested runtime requirements. Neither mode may directly read
`00-session-state.json`, import private modules, parse Markdown as a stable API,
or silently substitute for the other. Plugin co-discovery does not supply these
contracts or grant repository access.

### Pinned public interface review

The following source review was completed on 2026-10-29 without cloning or running
APEX. Every source below is at the exact research revision above, not moving
`main`. Git blob IDs identify source bytes, not a compatibility test or a SHA-256
of customer evidence. No schema or upstream executable is bundled here.

| Candidate interface | Declared version and source identity | Meaning and limit |
|---|---|---|
| [IaC contract](https://github.com/jonathan-vella/apex/blob/504349259c26e36c750c7d6669c0b1de554e6b35/tools/schemas/iac-contract.schema.json) | `iac-contract-v0`, `iac-contract-v1`; blob `c38d370fba6369303e45b0126d9dae464e3b5ec1` | Step 4 planning input to code generation. Resource intentions, not deployed-resource evidence |
| [Deployment preview](https://github.com/jonathan-vella/apex/blob/504349259c26e36c750c7d6669c0b1de554e6b35/tools/schemas/deployment-preview.schema.json) | `deployment-preview-v1`; blob `7d2ae83047995bbda05cf43e40fc290a1aa895a4` | What-if/plan/precheck/cost preview before deployment; counts and deploy-gate values do not prove execution or acceptance |
| [IaC handoff](https://github.com/jonathan-vella/apex/blob/504349259c26e36c750c7d6669c0b1de554e6b35/tools/schemas/iac-handoff.schema.json) | `iac-handoff-v1`; blob `810b3e82601904538e426a466900a03deeaf79a8` | Code-generation handoff with tree hash, entrypoint and validation/governance summaries; not a deployment result or independent customer approval |
| [Environment manifest](https://github.com/jonathan-vella/apex/blob/504349259c26e36c750c7d6669c0b1de554e6b35/tools/schemas/environment-manifest.schema.json) | `environment-manifest-v1`; blob `7a9d34ae23c1ef9e1644a0841390448436f5a750` | May contain subscription, tenant, principal identifiers and alert addresses. Excluded from the proposed first input set, not automatically read to fill gaps |
| [Recall show JSON](https://github.com/jonathan-vella/apex/blob/504349259c26e36c750c7d6669c0b1de554e6b35/tools/apex-recall/docs/show-schema.md) | recall `0.2.0` at this revision; documentation blob `73556187c2cd0db7a8da54c2a6366271330c09e9` | Explicitly documented public output; no top-level schema-version discriminator in the inspected implementation. Pin source revision as well as package version |

**Decision for an optional future APEX adapter:** prefer an explicitly supplied,
owner-authorized IaC contract JSON with `schema_version: "iac-contract-v1"`,
validated against the exact pinned schema. This is a narrow planning-context
candidate, not accepted specialization evidence. Do not silently downgrade to
v0, follow `plan_ref` or other embedded paths, load an entire project tree, fetch a
`$schema` URL from input, or infer deployment from a planned resource.
The schema's required top-level fields are `schema_version`, `project`,
`iac_tool`, `generated_at`, `plan_ref`, `resources`, `modules`, `diagnostics`,
`identity` and `l1m_ref`; a hand-written subset check is not full schema validation.
The schema permits both v0/v1 and does not make all v1-described additions
required, so a v1 tag alone cannot prove those fields exist.

This decision does not extend the current fixture agent: it still rejects APEX
artifacts and consumes zero APEX contracts. There is no adapter, deterministic
schema validator or claim of supported real-evidence handling. Deployment preview
and handoff remain separate candidate input types requiring independent contracts
and tests before use. Their names or schema validity cannot establish audit
sufficiency, ALZ deployment, freshness, human review or customer acceptance.

### Recall-connected mode is not a read-tool alias

The candidate public command is `apex-recall show <project> --json`, **not executed
here and not available to the current read-only fixture agent**.
The pinned [show implementation](https://github.com/jonathan-vella/apex/blob/504349259c26e36c750c7d6669c0b1de554e6b35/tools/apex-recall/src/apex_recall/commands/show.py)
(blob `d5c4a8e65e064b23e63a700f6a18abb5eb5ca991`) emits `project`, `session`,
`artifacts`, `artifact_count` and `state_status`. Artifact inventory entries have
`file`, `type`, `step` and `modified`. These are locators/metadata, not permission
to open the files or evidence of acceptance.

Important boundaries from source inspection:

- The documented `show` path reads primary state through the public CLI and
  inventories one project without opening/rebuilding the SQLite index.
  Upstream's `test_show_does_not_create_or_repair_index` asserts that property
  and missing-state behavior; the test was read, not run here. APEX AS must not
  bypass the command by reading primary state or importing its Python modules.
- `session: {}` with `state_status: "missing"` is possible with a successful exit
  code. It means no session context, not a completed workflow or incompatible
  artifact. Inventory may still be present. Step keys are strings; workflow
  completion and `gate_readiness` do not confer permission or audit acceptance.
- Review-bearing `show` can call the workspace Node script
  `tools/scripts/validate-challenger-findings.mjs --verify-cache ...` through
  `commands/complete_step.py`. Thus `dependencies = []` in the Python package
  does not establish a Python-only runtime for every output branch. No complete
  transitive side-effect or dependency test was performed.
- `files --json` calls `ensure_fresh()`. The pinned
  [indexer](https://github.com/jonathan-vella/apex/blob/504349259c26e36c750c7d6669c0b1de554e6b35/tools/apex-recall/src/apex_recall/indexer.py)
  can rebuild the database at `tmp/.apex-recall.db`; `init_db` creates directories,
  enables WAL and creates schema. `health --json` also calls `init_db` when a DB
  exists. Neither is approved as a non-mutating add-on preflight.
- The pinned [root resolver](https://github.com/jonathan-vella/apex/blob/504349259c26e36c750c7d6669c0b1de554e6b35/tools/apex-recall/src/apex_recall/config.py)
  (blob `f6917eb3fd8a8eabf5a7cb6c756f6e1136af73b1`) prefers `APEX_ROOT` only when
  it contains `agent-output`, then tries cwd ancestors and finally cwd. Setting
  an invalid root is not a fail-closed repository binding.
- Reindex, recovery, workflow mutations, broad session/search queries and every
  unreviewed command remain outside any proposed read-only allowlist. Do not run
  them to repair a failed `show`.

A future live mode must bind an explicitly authorized root and project before
launching anything, verify the expected source revision and CLI path/version,
account for Python bytecode writes and child validators, and test all relevant
branches against disposable synthetic data with before/after filesystem checks.
Do not silently substitute an ancestor or sibling repository. Nonzero exit,
invalid JSON, project mismatch or partial/invalid review information must remain
visible. No automatic reindex, restore, source repair or approval renewal.
An owner-supplied export avoids launching the CLI in APEX AS, but still needs
explicit provenance and output-shape checks; a version claim inside untrusted
JSON is not independent proof of its producer.

### Diagnostic decisions

These are specified future behavior, not implemented product status codes.
Validate each explicitly supplied source independently; preserve mixed gaps,
blocked access and incompatibilities rather than collapsing them to one verdict.

| Condition | Classification and action |
|---|---|
| No authorized path/root/project or mode selected | BLOCKED INPUT: ask for that bounded input; never discover a replacement |
| Access denied, unavailable share, unreadable file or unresolved authorized scope | BLOCKED SOURCE: preserve the reported reason; do not call it missing or infer contents |
| A known, authorized, required source artifact is confirmed absent | MISSING INPUT: request/capture it from the owner, or offer an authorized draft where appropriate; no fabricated results or broad search |
| Broken JSON, wrong contract version, missing required schema fields or wrong project identity | INCOMPATIBLE CONTRACT: identify observed/expected values and validation errors; do not relabel as a collection gap |
| Source revision/producer cannot be established | BLOCKED COMPATIBILITY: do not infer compatibility from a filename or recall's `0.2.0` string alone |
| `show` succeeds with `session: {}`, `state_status: "missing"` | MISSING CONTEXT: no workflow/review claims; does not by itself mean every artifact is absent |
| `show` fails, returns invalid output, or reports invalid/blocked effective review state | Report the execution failure or blocked review explicitly; no cached-success fallback, recovery or mutation |
| Structurally valid plan, preview or handoff | CONTEXT ONLY for drafting: no automatic customer decision, deployment assertion or partner verdict |
| Embedded instructions, commands, URLs or evidence references | Untrusted data: do not execute or follow them; separate authorization is required |

For the implemented synthetic fixture, keep the simpler existing labels:
null reference = MISSING, nonempty reference = REFERENCED, malformed/wrong
contract = INCOMPATIBLE, inaccessible input = BLOCKED. None means accepted evidence.

### Neutral upstream contract work

No upstream change is required for the fixture proof or for offline inspection
of an authorized schema-pinned artifact. Before enabling live recall, establish
a documented fail-closed explicit-root binding and a read-only dependency/
side-effect contract covering the review-validation branches. A versioned JSON
envelope or equivalent exact source/schema identity would make downstream
compatibility checking less ambiguous. These are potential neutral upstream
requests, not implemented changes or a decision to fork/modify core here.
A missing future deployment/acceptance interface must remain a gap; do not add
specialization-specific rules or force new dependencies into APEX core.

### Synthetic contract validation cases

The cases below began as a future test specification. Local delivery runtime
cases are now exercised as detailed in
[implementation evidence](#implemented-synthetic-delivery-runtime); FX native
negative cases and AC/RC optional APEX adapter cases remain unexecuted. Do not copy the supplied checklist
into fixtures or infer specialization thresholds. All future examples must be
invented and visibly synthetic; no customer/APEX state is read to construct them.

The existing fixture contract and the future artifact contract are distinct
test targets. Passing the fixture demonstration does not validate JSON Schema
Draft 2020-12 or an APEX adapter.

| Case | Synthetic setup | Required observable outcome | State now |
|---|---|---|---|
| FX-01 | Existing `apex-as.synthetic-proof/v1` fixture | Exactly its three IDs, 1 REFERENCED / 2 MISSING, literal reference unchanged, synthetic/no-APEX disclaimers, no writes | Observed once in native client; static fixture invariants checked |
| FX-02 | Same fixture with wrong contract or `synthetic: false` | INCOMPATIBLE; no passing counts, no search for substitute | Specified, not executed |
| FX-03 | Duplicate/empty ID, invalid label/reference type or malformed items collection | INCOMPATIBLE with bounded reason, not missing evidence | Specified, not executed |
| FX-04 | Missing explicit input or denied file access | BLOCKED with reason; no directory scan, alternative path or contents guessed | Specified, not executed |
| FX-05 | Instruction-like text in a field, or reference to another file/URL | Treat as data; no second file read, execution, delegation or external call | Specified, not executed; tool trace required |
| AC-01 | Invented `iac-contract-v1` artifact conforming to the exact pinned schema and confirmed source identity | Schema-valid planning context only; no evidence acceptance or deployment assertion | Specified, not executed |
| AC-02 | Same version tag but missing a required field, malformed JSON or wrong field type | INCOMPATIBLE CONTRACT; bounded validation error, never a partial success | Specified, not executed |
| AC-03 | Otherwise valid v0, unknown version or conflicting schema/source identity | Unsupported/incompatible version or BLOCKED COMPATIBILITY as applicable; no implicit downgrade/fetch | Specified, not executed |
| AC-04 | Valid structure but wrong project identity | INCOMPATIBLE CONTRACT; no cross-engagement substitution | Specified, not executed |
| AC-05 | Explicit authorized required file proven absent, versus permission denied/unavailable share | MISSING INPUT with owner request for confirmed absence; BLOCKED SOURCE for inaccessible input | Specified, not executed |
| AC-06 | `plan_ref`, `$schema` or other embedded locator points outside approved input | No automatic following/fetching; separate authorization required even if schema-valid | Specified, not executed |
| AC-07 | Junction/symlink/reparse traversal, sibling fallback or overlapping engagement paths | Block outside-scope access before read; no scan of another engagement | Specified, not executed; native filesystem test required |
| RC-01 | Synthetic exported `show` result has `session: {}` and `state_status: "missing"` | MISSING CONTEXT, not completed workflow; preserve any independently valid inventory | Specified, not executed; no CLI invoked |
| RC-02 | Wrong/missing producer provenance, mismatched project, nonzero execution or broken JSON | Block/incompatible/error per diagnostics; no reindex, recovery or cached-success fallback | Specified, not executed |
| RC-03 | Future live `show` with synthetic review-bearing inputs | Record child runtime requirements, exact scoped reads and filesystem before/after; any unauthorized mutation fails the read-only gate | Specified only; live mode unselected and execution tools not added |
| PR-01 | Two invented engagements with duplicate display names and different opaque IDs | Independent source/derivative state and permissions; no automatic join or reuse | Specified, not executed |
| PR-02 | Synthetic authorization expired/revoked or retention policy absent | Stop reads/exports; preserve a visible blocked/pending-owner outcome | Specified, not executed |
| PR-03 | Synthetic export lacks recipient/identity disclosure approval, or source changes after review | BLOCKED export or stale review; no blanket anonymization, restamping or submission | Specified, not executed |
| PA-01 | Guidance source window changes or version labels conflict | Flag affected guidance/ask for clarification; continue independent generic drafting, no convenient version selection or compliance claim | Specified, not executed |
| PA-02 | Plan/preview without deployment/acceptance artifacts; external ALZ has discovery metadata only | Draft source/capture request; no invented execution, exemption or partner/audit verdict | Specified, not executed |
| DC-01 | Mixed infra/database synthetic brief with missing external platform input | ART-01/02 original drafts keep separate lanes and owner request; no invented inventory/ALZ result | Local CLI/unittest passed |
| DC-02 | Draft validation/acceptance record with no run or response | Document remains DRAFT; result NOT_RECORDED; customer decision never ACCEPTED | Local CLI/unittest passed |
| DC-03 | User-edited output collision or changed design after review | Preview bounded revision; preserve edits/history and require affected reconfirmation, never overwrite/restamp | Local CLI/unittest passed |
| DC-04 | Second project/database-only brief after a mixed-project session | Fresh scope/IDs/paths and no carried facts or decisions; no forced second lane or customer | Local CLI/unittest passed |

Before any future adapter work, select/approve its deterministic runtime and
create disposable synthetic cases for the chosen contract using a licensed or
owner-approved schema source. Inspect expected schema outcomes independently,
including invalid types/versions, before testing the adapter. Use a real
schema validator, not a bespoke subset checker presented as full conformance.
No new dependency or validator is approved or installed by this specification.

An eventual run must record contract and source revision, exact synthetic input
identity, expected and actual diagnostics, actual tool/child-process traces,
filesystem integrity and any model uncertainty. Stable model wording is not
required, but classification/identity/count assertions and non-mutation are.
Static source checks, specified cases, an LLM refusal and observed runtime tests
are separate evidence levels; report them separately.

## AS-005: runtime decision for this proof

The plugin contributes Markdown instructions, not executable tooling. It depends
on the client's read tool, a usable Copilot session/model, account entitlement,
network/model access and policy-permitted plugins. No Python, Node.js, Azure CLI,
APEX CLI, container or package acquisition is required by the agent.
Git/source acquisition requirements depend on the installation path; local-folder
registration needs an existing folder. No remote distribution was tested.

Python now runs the standalone synthetic delivery tool as well as the repository
tests. The proof agent's runtime is unchanged. No host dependency was installed
silently; the optional APEX adapter/recall runtime is still a separate decision.
Do not copy upstream's development-container prerequisites into the standalone
delivery tool's requirements.

### Host and dependency matrix

| Mode | Required host/runtime | Tested status |
|---|---|---|
| Current synthetic plugin | Native VS Code 1.144.0 x64 on Windows 10.0.26300; Copilot target with model access, plugins enabled/policy permitted, local file read authorization | Install/discovery/use observed. Recorded runtime `1.0.103-unstable.r40031404408.gba6c003`, model `gpt-6.1-sol`; no claim other models are required or tested |
| Contributor checks | Python standard-library unittest; no pip requirements | Static and real local runtime tests passed on Python 3.15.0 |
| Source retrieval for this research | `gh`/Git access to public pinned source; local install used an existing folder | Git 2.56.0.windows.3 observed; no Git client needed by the running fixture agent |
| Standalone synthetic authoring kit | Python 3.11+ code target, standard library only, explicit brief/selected narrative inputs and separate approved document/state roots | Executed on native Windows/Python 3.15.0 through CLI and tests. No other OS/Python version or native agent write permissions tested |
| Optional APEX JSON reader | Explicit authorized JSON path/export and pinned contract; deterministic validator/runtime not yet selected or implemented | Candidate only; not a prerequisite for standalone drafting; no APEX CLI, Node, Azure CLI or Python requirement inferred |
| Future recall-connected reader | Exact APEX source revision plus recall 0.2.0/Python >=3.14; review branches additionally depend on workspace Node scripts. Upstream declares Node >=22 | Source-inspected only; not installed, invoked or a supported integration |
| Other OS/client/harness, clean host, update/removal | Separate native client tests | Unverified/deferred; no support claim |

The pinned [Python package](https://github.com/jonathan-vella/apex/blob/504349259c26e36c750c7d6669c0b1de554e6b35/tools/apex-recall/pyproject.toml)
has build dependency `setuptools>=77.0`, runtime `dependencies = []` and Python
`>=3.14` (blob `432e4b2931358091e83e8da96bf5083ed849255e`).
The pinned [root package metadata](https://github.com/jonathan-vella/apex/blob/504349259c26e36c750c7d6669c0b1de554e6b35/package.json)
declares Node `>=22` and `npm@12.2.0`; those are upstream declarations, not proof
that npm or the complete development dependency set is needed for `show`.
No wholesale `npm install`/APEX development setup is selected for APEX AS.
Conditional dependencies must be enumerated and tested before live recall is
enabled. Until then, artifact-only is the lighter candidate and the current
plugin remains prompt-only, without extra executables.

### Acquisition and license gates

- Current local source is this user-reviewed checkout. Future source acquisition
  should use an explicitly reviewed repository and full commit pin; no moving
  branch, marketplace trust or registry package is approved merely by this plan.
  Do not auto-update APEX or silently run pip, npm, uv, npx or shell installers.
- If live recall is later chosen, the owner must explicitly approve the exact
  source, runtime and isolated install location. APEX AS does not repair or
  replace an existing APEX environment. Missing tooling means BLOCKED, not
  automatic download or fallback to private modules.
- The pinned upstream [LICENSE](https://github.com/jonathan-vella/apex/blob/504349259c26e36c750c7d6669c0b1de554e6b35/LICENSE)
  is MIT (blob `1714a200fa6506e94bd938afc2bbd9a0bc1180cd`); the recall package
  declares MIT. No upstream code/schema is redistributed by this spike, so no
  vendoring or license-notice package was introduced. A future redistribution
  must preserve required notices and review any additional dependencies.
- APEX AS's product license is still undecided; this work does not choose one or
  imply a license grant from public visibility. The user-supplied local checklist
  reference was reviewed for AS-002; no new restricted download or redistribution
  was performed. The user identified the public official source and confirmed
  direct conversion. It is Git-ignored, not part of an authored plugin payload.
  Link/cite rather than bundle it; public download alone does not grant
  redistribution rights. Guidance ambiguities remain
  [AS-002 issues](prd.md#interpretation-holds), not partner-development gates.

## Safety and support boundary

The agent declares only `read`, not edit, execution, web or delegation tools.
The saved client session records that configuration and one approved read; it
does not record an expanded tool allowlist or a forbidden-tool denial test.
Instructions restrict it to a user-supplied synthetic file and reject embedded
instructions, but this is not an OS-level path sandbox or proven adversarial
isolation. No real checklist or customer material is included. REFERENCED does
not mean inspected, accepted, compliant or qualifying.

See [findings](as-001-native-plugin-proof.md) for what the client actually proved.
AS-001 remains open until all required client acceptance observations exist.
