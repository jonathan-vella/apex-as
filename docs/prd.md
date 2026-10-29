# APEX AS delivery companion requirements

The implemented spike is a distribution experiment derived from AS-001 in the
unmerged [PR #1](https://github.com/jonathan-vella/apex-as/pull/1) proposal.
On 2026-10-29 the user also authorized AS-002 profile-source review, AS-004 privacy
design and non-runtime AS-003/AS-005 preparation, then clarified the product
direction: **help partners create artifacts during every project delivery, not
assess partners**. This PRD is the local product definition for that direction.
It supersedes assessment-first framing without claiming the PR was merged.

## Product purpose and boundaries

**User:** a partner delivery practitioner working on one authorized project.
**Job:** create useful, checklist-aligned project artifacts at the point of work,
reuse existing delivery outputs and retain actual results and decisions so the
team does not reconstruct the record later. First family: Infrastructure and
Database Migration to Microsoft Azure.

The companion should guide what to produce, when, by whom and from which inputs;
draft original content and capture structures; flag unresolved delivery inputs;
and keep versioned links between scope, plans, execution records and handover.
It must not issue a partner score, specialization eligibility verdict, Module A
waiver, audit-readiness verdict or certification claim. An artifact-completeness
check answers "what does this document still need?", not "does this partner pass?"

| Requirement | Observable acceptance for the future delivery companion |
|---|---|
| DP-01: project first | One explicit project ID/scope, stage, workload lanes, owners and approved input/output boundary; no portfolio or partner-status lookup needed to begin |
| DP-02: create at the right time | A stage-specific task identifies the next useful artifact, required inputs, accountable owner, reviewer and capture point, with source-guidance citation where established |
| DP-03: reuse before drafting | Inspect only selected artifacts; propose reuse, an authorized extension or a separate draft. Do not fork an authoritative APEX artifact or overwrite user edits by default |
| DP-04: original, grounded drafts | Assumptions/placeholders are visible; missing facts become questions/owner actions. Guidance is paraphrased and cited, not a reproduced checklist or asserted compliance |
| DP-05: capture truth | Plans, actual tool outputs, practitioner review and customer decisions remain distinct. A blank results/acceptance form is not an executed test, production deployment or signed acceptance |
| DP-06: bounded authoring | Preview intended new files/diffs in a user-approved project document location; no source, APEX state, existing approvals or unrelated files changed without explicit scope |
| DP-07: changes and review | Record input/output revisions; a changed dependency makes affected review/acceptance context stale or needs reconfirmation, never automatically restamped |
| DP-08: external owners | For an externally owned ALZ or source, create an owner-specific request with scope, purpose and needed records. Inaccessible inputs remain blocked; useful independent drafting can continue |
| DP-09: reusable project method | Run the same workflow on a second synthetic project without copying project facts, owners, results, approvals or customer identity |
| DP-10: controlled handover | Produce only authorized operational artifacts and an index of their current revisions, outstanding actions and sources. Customer release requires separate scope/recipient review; not audit submission |
| DP-11: optional APEX reuse | Explicit inputs work standalone. APEX integration is pinned, read-only and optional; no agent dispatch, sibling discovery, recall install or core changes assumed |
| DP-12: no-container use | Product install/use/removal and permitted authoring must eventually pass on declared native hosts. Current distribution proof is only a partial gate |

### First delivery slice and non-goals

The implemented local delivery slice turns a synthetic project brief into a
reviewable **delivery artifact plan and assessment-output draft**, with explicit
owner actions and guidance references. It must work without APEX, live recall,
Azure credentials or a completed partner assessment. Then extend the same
project through design, migration preparation, supplied synthetic execution
capture, validation records and handover index;
see [runtime evidence](plan.md#implemented-synthetic-delivery-runtime).
Here, "assessment output" means the project's technical workload/discovery
document, not an assessment of the partner.

Development and current tests remain synthetic-only. In the intended product,
authorized customer project artifacts are normal inputs and outputs, subject to
the access/processing and retention gates below. No particular engagement,
customer processing, deployment or document release is authorized by building
this generic product.

No retrospective partner-assessment engine, portfolio eligibility counting,
audit export/submission or automated cloud execution is planned. The companion
does not deploy/mutate an ALZ, run migrations, generate executable deployment code
as its first slice, invent sign-offs or bypass APEX delivery approvals. The delivery kit does not require an APEX JSON adapter or compliance engine.
Future structural document checks must not be marketed as audit validation.

## Implemented proof requirements

| Requirement | Acceptance evidence |
|---|---|
| Native package | Recognized plugin manifest; native local-source install recorded in target client |
| Discovery and use | Agent appears from plugin source, can be selected and reads the explicit synthetic fixture |
| Non-mutating fixture inspection | Only read tools declared; no terminal/edit/delegation tools or Azure calls observed; fixture unchanged |
| Honest gaps | `demo-design` REFERENCED; `demo-acceptance` and `demo-platform` MISSING; totals 1 and 2 |
| Honest incompatibility | Wrong fixture contract, nonsynthetic input or malformed items must not produce a passing report |
| No container | Install, invoke and remove on a native host without requiring Docker or a devcontainer |
| Coexistence | APEX and add-on discovery remain intact; no APEX/user customization overwrites |
| Clean removal | Plugin and agent disappear in a fresh session; source and unrelated customizations survive |
| Explicit boundaries | No sibling-repository discovery, APEX-agent calls, dependencies or APEX compatibility inferred |

The sample is deliberately invented and carries no official specialization
requirements. Reporting gaps is language-model behavior, not deterministic
validation. Static tests check packaging and fixture invariants only.

The [findings matrix](as-001-native-plugin-proof.md) is the proof acceptance record;
requirements above are not assertions that their tests passed. Real customer
evidence, Azure access, ALZ mutation, exports, customer pilots and evidence-engine
implementation remain out of scope for this development task. The read-only
proof is not the eventual authoring workflow; adding writes requires separately
implemented permissions, preview and isolation tests, not silently broadening it.

## AS-002: first profile and source authority

**Selected family:** Infrastructure and Database Migration to Microsoft Azure,
as requested by the user. **Authority status:** official public publication
source established; local conversion provenance confirmed by the user.
Independent PDF/Markdown equivalence and redistribution permission are not established.

| Provenance field | Observed value or boundary |
|---|---|
| Local reference | `tmp\as-infra-nov2026.md`, supplied explicitly by the user on 2026-10-29 |
| Document description | Program guide, audit checklist and FAQ for the selected specialization |
| Header version/window | V2.0; July 1 through December 31, 2026. November in the filename is not a separate effective version |
| Internal inconsistency | Module B heading carries V1.9; no precedence inferred between header, embedded tables and historical updates |
| Local snapshot | 73,586 bytes; SHA-256 `AE302FC7CC9D314E02F520DEEFFE05071928E138C5CC8BC9708CD4F202E121D4` |
| Official program page | `https://partner.microsoft.com/en-us/partnership/specialization/infra-and-database-migration#tab-4`; supplied by the user, fetched on 2026-10-29 |
| Publisher link | The page's audit-checklist link targets `https://assetsprod.microsoft.com/en-us/azure-infra-and-db-specialization-audit-checklist.pdf`; public download, not confidential merely because it was supplied locally |
| Conversion provenance | User confirmed direct conversion from that linked PDF with no intentional content edits; extraction completeness/equivalence not independently checked, no PDF downloaded here |
| Rights/default | Cite/link the public source; do not bundle the PDF, copied tables or a reconstructed checklist. Public access is not a redistribution license; permission for such distribution is not established |
| Guidance applicability | Record source version/window with each task; flag ambiguous or expired guidance. Partner audit date/standing is not needed to create project documents, and this tool makes no audit eligibility claim |

On 2026-10-29, the public Microsoft Learn
[specializations overview](https://learn.microsoft.com/en-us/partner-center/membership/specializations)
listed the selected specialization and described qualification/audit enrollment.
The page's metadata reported update date 2026-09-30 and source commit
`b1533440845dfc08787b59bfe3bb33537c502f24`.
The user subsequently supplied the correct
[program page](https://partner.microsoft.com/en-us/partnership/specialization/infra-and-database-migration#tab-4).
It was fetched and its link to the
[official public checklist](https://assetsprod.microsoft.com/en-us/azure-infra-and-db-specialization-audit-checklist.pdf)
was verified in the page HTML. This corrects the earlier "original source not
supplied" status; failed guessed URLs are not an unresolved access requirement.
The link is a living publication URL, not a frozen PDF identity. Keep the local
snapshot fingerprint; do not claim independent equivalence or publisher
confirmation of the V2.0/V1.9 discrepancy. No authenticated system was accessed.

### Interpretation holds

This is a bounded issue log, not a reconstruction of the checklist. Consult the
local reference for the original requirements; no control text is redistributed.

| Hold | Safe design consequence and closure evidence |
|---|---|
| PA-01: version discrepancy | Preserve both observed labels and cite the source. Continue generic original drafts, but hold a disputed requirement-specific instruction until clarified; no version selection by guess |
| PA-02: shared vs workload guidance | Guide foundation/ALZ artifacts separately from migration-specific artifacts; reuse only where project scope/source supports it. No Module A pass decision |
| PA-03: partner standing not relevant to product setup | No partner pass report, anniversary or waiver is needed to draft project artifacts. Do not ask for it or infer it; audit standing is outside the product's verdicts |
| PA-04: external ALZ | Record external owner, interface assumptions, requested inputs and access limitations. Draft an evidence/request outline, not an acceptance verdict. Discovery/planning is not actual deployment; do not deploy an ALZ to fill a documentation gap |
| PA-05: exceptions/deviations | Source-specific applicability or customer deviations remain explicit owner decisions. Do not silently drop an artifact or copy another specialization's exception |
| PA-06: project linkage and dates | Preserve workload, environment, actual event dates and acceptance provenance for this project. No portfolio population/eligibility logic or invented completion date |
| PA-07: source and project permissions | Keep reference redistribution and customer processing/release permissions separate. Public checklist access does not authorize disclosure of project data |

**AS-002 has a usable source record, not a completed guidance pack.** The public
source and user conversion history are recorded. The next work is original
stage/task guidance with verified citations; ambiguity blocks only affected
claims. Checklist redistribution remains excluded by default. Partner standing
and external-ALZ audit acceptability are not generic development blockers.
No program owner, auditor or customer has been contacted on the user's behalf.

### Current implementation acceptance

The original reusable `apex_as/guidance.json` outlines cover D0-D6 and ART-01..08
with source URL/version caveats, broad section locators, inputs, owner roles and
capture points. They do not reconstruct an exhaustive checklist or resolve the
internal heading-version discrepancy.

The Python CLI implements DP-01..11's **synthetic local subset**: explicit brief/
sources, lane-aware drafts, preview-bound exclusive writes, revision/owner
carry-forward, supplied exact-revision records and a local handover index.
Current contracts are `apex-as.delivery-{brief,events,state,preview,status}/v1`.
It rejects real-data mode and does not authenticate supplied actors/claims.
Artifact content is a structured original draft with supplied text and PENDING
questions, not automatically reasoned architecture or a complete specialist
assessment. Practitioners still author/verify the substantive project decisions.

Independent correctness review findings were fixed and regression-tested:
malformed event types now produce bounded errors, persisted records are validated,
oversized state is refused before writing, and the handover index tracks both
release status and event provenance even if the outcome label is unchanged.
DP-12's native plugin authoring/lifecycle and production privacy enforcement
remain unverified. A source-only archive is feasible/tested, not a released plugin.

## AS-004: privacy, isolation and evidence ownership

**Status:** design baseline; current development/test inputs are synthetic.
The intended product creates and reuses authorized real project artifacts.
The user's authorization covers this bounded work, not customer consent, legal
approval or an organizational data-retention policy. The rules below define
future acceptance gates; they are not implemented security controls.

### Data classes, ownership and storage

| Data class | Authority/owner and permitted handling |
|---|---|
| Synthetic fixtures | APEX AS maintainer owns invented demonstration material. Only synthetic, non-identifying examples may be committed under `fixtures`; never derive them by lightly editing customer evidence |
| Public checklist/local reference | Publicly downloadable publisher document, not inherently confidential. Cite/link it and retain metadata; do not bundle source text/tables or an exhaustive reconstructed checklist. Local copy remains outside authored payload |
| Existing project artifacts | Remain authoritative in the owner's selected document repository/system. Read, modify, send to a model and release are distinct authorizations; none for a real project has been supplied here |
| Future add-on state | Separate private per-project store, not APEX session state or the plugin source/install folder. Keep minimal pointers, task/revision metadata and owner actions; location/access/retention approved before use |
| Future authored artifacts | Original drafts and capture records in a user-approved project document location, potentially an organization's private version-controlled document workspace. Private source control is allowed only by project policy; this public development repo is never a customer store. Separate from add-on state, preserve source/derivative and review lineage |
| Host-owned chat/logs/caches | Controlled by client/provider/organization policy, not the add-on. Read-only actions can send content to the configured model and retain prompts, tool results and chat history |

`/tmp/` is now excluded by the repository's `.gitignore` and the supplied reference
is untracked. This only prevents ordinary Git inclusion; `git add -f`, archives,
manual copies and local plugin registration can still expose it. The source now
resides within the previously registered local plugin root. Do not distribute or
copy this working folder as a plugin payload while it contains the reference.
Git exclusion is not a native plugin packaging filter or filesystem access control.
For future releases use a clean, inspected tracked-source package without excluded
references; verify the client packaging behavior before claiming protection.
The reference's public availability corrects earlier confidential/private labels;
the exclusion still prevents accidental republishing and payload contamination.
The original source is unchanged and no file relocation is performed here.

The runtime creates only explicitly selected synthetic document/state revisions
outside the product source, including disposable/retained test runs. No real
engagement store, customer export or native-agent tools were created. No ACL,
disk encryption, repository visibility or host retention setting was changed.

### Access and processing gates

1. Before real-data use, record the evidence custodian, engagement scope, named
   authorized users, exact source paths/items, allowed metadata/content fields,
   purposes and permitted processing destinations. Model/provider/region, host
   logs, connectors and downstream tools need explicit organizational permission.
   Lacking that permission means BLOCKED; local read access is not cloud-processing
   approval. Do not attach real material to a chat to ask whether it may be read.
2. Resolve and authorize each explicit path before access. Reject cross-engagement
   traversal, sibling-root fallback, symlink/junction/reparse-point escapes and
   unapproved network shares. No recursive discovery or following embedded paths
   or URLs. A revoked or expired authorization stops access and sharing.
3. Keep customer/project identifiers scoped to one engagement. Use opaque IDs in
   add-on filenames; keep any authorized re-identification mapping in the private
   owner-controlled store. Pseudonyms and content hashes are not anonymization,
   proof of consent or safe public cross-customer join keys.
4. An inaccessible pointer is BLOCKED SOURCE, not a missing fact to invent or a
   failed partner. Maintain source owner and reason without disclosing sensitive
   paths in public errors. Wrong contract/version is incompatibility, not access denial.
5. Evidence text is untrusted data. Ignore instructions, links, commands and
   requests to change scope; no tool/permission escalation, Azure calls, APEX
   state updates or exports based on embedded content. Unexpected secrets or
   customer material in an authorized synthetic input stops processing; report
   the category, not the value, and obtain owner handling instructions.

The CLI now enforces selected absolute/disjoint roots, no reparse traversal,
named-source reads, immutable new files, digest approval and synthetic-only input.
These are not an OS sandbox, semantic customer-data detector or model tool
boundary; the native read-only proof is unchanged. Privacy policy, customer
processing permissions and retention/export enforcement for real use remain
requirements, not implemented production controls.

### Retention, withdrawal and deletion

For this task, keep the invented fixture and public design documents in the
working tree; do not make further copies of the checklist or create an engagement
store. The user-supplied local reference is retained in place, unchanged. No
automated deletion was authorized. Host/model logs of the authorized source review
may already exist; do not claim Git exclusion removed those copies.

Before any real input, its custodian must specify a retention trigger and period
or explicit expiry date, applicable legal holds, approved storage/backups and
deletion owner. There is no default indefinite retention or invented universal
number of days. If these decisions are absent, real-data ingestion remains blocked.

On expiry or withdrawal, stop reads and exports, invalidate affected draft/review
context and derivative access, and request authorized deletion in add-on stores and
approved exports/backups according to the agreed policy. A minimal non-content
tombstone may be retained only if separately permitted. Do not erase authoritative
customer/APEX originals, remove legal-hold material, or claim deletion from host/
model caches and recipient systems without confirmation from their owners.
Record pending deletion and owner acknowledgments rather than success-shaped
fallbacks. Plugin uninstall does not prove any of these retention actions.

### Review and export gates

Reading inputs, drafting a document, revising existing content and releasing a
customer handover are separate scopes. Audit submission is not a product action.
No real-project authoring or release is approved by this development task.
A future customer handover/export needs:

- exact engagement, recipient/destination, purpose, scope, profile/source version
  and expiry approved by the evidence custodian and authorized reviewer;
- a field-level decision about required customer/project identity, provenance
  and acceptance references. Do not assume blanket anonymization: if required
  identity cannot lawfully be disclosed, mark the release BLOCKED, not complete;
- source/derivative separation, source revision/checksum where permitted,
  transformation/redaction record and independent review. An unchanged checksum
  does not establish authorship, freshness, permission or customer acceptance;
- included/excluded/blocked item inventory and unresolved interpretation gaps.
  Changed inputs invalidate affected review; no automatic restamping or approval;
- confirmation that no bundled checklist text, secrets, unrelated customer
  data or unapproved identifiers are in the package. Preflight disclosure itself
  must stay within the authorized processing boundary.

Summaries in chat are disclosures too. Real evidence must not enter this public
repository, PRs/issues, telemetry, generic agent notes or a shared portfolio
index. Producing a report never means Microsoft/auditor acceptance.

### Synthetic-only rules and acceptance status

The bounded authorization permits invented, non-sensitive fixtures. Use labels
and identities that cannot be mistaken for actual customers, dates chosen only
to exercise declared test boundaries and non-resolving references such as the
existing `synthetic:` value. No copied checklist clauses, real identifiers,
customer screenshots, derived customer datasets or live URLs. Synthetic inputs
and decisions must never be mixed into real project delivery records or presented
as actual customer results.

Synthetic acceptance cases and
[runtime evidence](plan.md#implemented-synthetic-delivery-runtime) distinguish
executed local authoring/path/record tests from unexecuted native-agent and APEX
adapter cases. The deterministic CLI neither interprets data as instructions nor
calls a model/network tool. This is not a model prompt-injection red-team result.
Retention/deletion and real export enforcement remain unimplemented; customer/
organizational approval and production enforcement tests are still required.

### Validation of this foundation change

On 2026-10-29, all four tests in the existing standard-library unittest runner
passed, including the new `/tmp/` exclusion-rule regression check. Actual
`git check-ignore` confirmed the supplied reference is ignored; `git ls-files`
confirmed no `tmp` content is tracked. All 11 authored files passed whitespace,
relative-link and heading-anchor checks. The local reference, plugin manifest,
agent and synthetic fixture SHA-256 fingerprints remained unchanged.

These are static/source-integrity checks, not a release-payload, access-isolation
or privacy-enforcement test. No customer data, new packages, APEX changes, exports
or plugin lifecycle operations were introduced.

The delivery-companion realignment also passed document-link/heading checks,
coverage checks for 12 product requirements, seven stages and eight artifact
outlines, and checks for all 21 backlog IDs with no unknown dependencies or cycles.
The four existing tests and all four input fingerprints still passed. These
checks verify the specification's structure/consistency, not authoring behavior;
they predated the runtime implementation.

The later implementation exercised actual drafts, journals, error paths and
CLI subprocess operations through the same existing unittest runner. A complete
native CLI rehearsal created all eight documents, recorded eight supplied
synthetic events (including pending/rejected/accepted customer responses and
local release), preserved a practitioner edit and required reconfirmation, then
created isolated infra-only and database-only projects. No customer/cloud
operation occurred. One host symbolic-link creation test is skipped for missing
Windows privilege; a real Windows junction-boundary test passed. Native agent
permissions/install/update/remove, actual ACL policy and other platforms remain
outside that evidence. See [runtime limits](../README.md#safety-and-support-limits).
