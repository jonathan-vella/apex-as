# APEX AS

APEX AS is an optional **project-delivery companion**: it helps partners create
checklist-aligned artifacts as they deliver projects, rather than reconstructing
documentation afterward. It does not assess partners, score eligibility or
certify compliance.

The first delivery workflow is **Infrastructure and Database Migration to
Microsoft Azure**: scope and assessment outputs, design, migration planning,
execution capture, service validation and operational handover. For every
artifact, specify what to create, when, the owner, source inputs and the review
or customer decision still needed. Drafts never stand in for tests, deployments
or customer sign-offs that have not occurred.

**Current implementation:** a dependency-free local Python delivery kit creates
all eight artifacts, with preview-bound writes, immutable revisions, separate
synthetic execution/review/customer records and a current-revision handover index.
It is a deterministic structured drafting tool, not an LLM narrative generator.
Original guidance asks for missing facts; supplied narrative is quoted as data.
It does not authenticate a sign-off, execute migrations or send a handover.

The separate experimental plugin `apex-as-proof` `0.0.1` and its read-only
`apex-as-fixture` agent are unchanged. They do **not** run the authoring kit.
No native authoring agent has been installed or tested. The runnable CLI accepts
**synthetic examples only**; real project processing is deliberately rejected
until its organizational/privacy and release gates are implemented and verified.

The proposed product documents in [PR #1](https://github.com/jonathan-vella/apex-as/pull/1)
were inspected at commit `b86b394ecae468e401db35c55e19300a06ab52d6`.
The PR was **open and unmerged** on 2026-10-29. The local PRD, plan, roadmap and
backlog now reflect the user's delivery-companion direction, not adoption of the
proposal's assessment-engine-first sequence. No remote documents were changed.

## Delivery experience

1. Agree one project's scope, delivery stage, owners and permitted inputs/outputs.
2. Select relevant guidance from the cited official checklist; retain uncertainty.
3. Reuse an authorized existing artifact or draft only what is needed next.
4. Capture actual execution outputs and decisions at their delivery checkpoints.
5. Review the current revision and request customer validation/acceptance where
   needed; keep pending actions explicit.
6. Hand over the authorized operational documents and source-linked records.

Start with the [first project workflow](docs/plan.md#first-infradatabase-project-workflow)
and [product requirements](docs/prd.md#product-purpose-and-boundaries).
APEX continues to own delivery actions and approvals. No cross-plugin delegation,
private session-state access, automatic Azure actions or APEX core changes are
assumed. Explicit project inputs allow a standalone path as well as future
read-only APEX artifact reuse.

## Run the synthetic delivery kit

From this checkout, using Python **3.11+** (tested on Windows/Python **3.15.0**).
No pip/npm install, APEX, Azure account, Docker or devcontainer is required.
Other Python/OS combinations are not yet verified.

For a complete disposable CLI rehearsal:

```powershell
python -B -m apex_as.rehearse
```

This actually previews/applies D0-D6, supplies invented review/run/customer records,
records a local handover, edits a design, checks reconfirmation, and repeats on
fresh infra-only and database-only projects. Temporary outputs are removed when
done. Use `--keep C:\existing-empty-directory` to retain the rehearsal documents,
state journal, synthetic event examples and `rehearsal-result.json` outside this
product checkout.

For a reviewed manual run, choose **three existing disjoint directories** outside
the product tree for inputs, authored documents and separate add-on state. Copy
one of `fixtures\delivery\mixed.json`, `infrastructure.json` or `database.json`
into the input directory as `brief.json`. Do not use APEX/core directories.

```powershell
$common = @(
  '--brief', 'C:\as-demo\inputs\brief.json',
  '--inputs-root', 'C:\as-demo\inputs',
  '--documents', 'C:\as-demo\documents',
  '--state', 'C:\as-demo\state'
)
$preview = python -B -m apex_as preview @common | ConvertFrom-Json
if ($LASTEXITCODE -ne 0) { throw 'Preview failed' }
$preview.changes | Select-Object path, diff | Format-List
$preview.approval
# After reviewing the exact paths, content/diffs and state/event changes:
python -B -m apex_as apply @common --approve $preview.approval
python -B -m apex_as status @common
```

`preview` has no writes. `apply` recomputes the plan and requires its exact digest;
changed inputs, outputs, guidance, destinations or state require a new preview.
Use `--artifacts ART-01 ART-02` on **both** commands for the first slice; draft
dependencies must already exist or be included. Without selection it creates or
refreshes all eight. Repeating unchanged authoring is a no-op.

Documents are created under `<documents>\<project_id>\r000001\ART-01.md`, etc.;
the separate state root has append-only `r000001.json` snapshots. No existing
file is overwritten. A user-edited artifact causes a conflict; `--carry-forward
ART-03` on preview/apply explicitly preserves its entire prior content as literal
data in a new draft revision. Review the diff for duplicates and reconcile it
before recording review. Historical documents/results/decisions remain intact.
`status` marks changed inputs/dependencies and customer reconfirmation separately.

### Input and record contracts

The three brief fixtures are runnable examples of `apex-as.delivery-brief/v1`.
Top-level fields are exact: `contract`, `synthetic: true`, opaque `project_id`,
`title`, `lanes`, `environments`, `roles`, `alz`, `inputs`, `sources`; optional
`lane_inputs` overrides shared section input for one selected lane.
The reusable original prompts and supported section keys are in
`apex_as\guidance.json`. Missing section inputs/roles become PENDING owner actions.
ALZ metadata never proves deployment and external ownership never implies failure.

An optional source is `{ "id": "demo-source", "path": "notes.txt",
"artifacts": ["ART-02"] }`. Paths are relative to the explicit input root.
Only named UTF-8 `.txt`, `.md` or `.json` files are read; no references or URLs
inside them are followed. Excerpts are included literally in their selected
drafts, so do not select content you do not want copied into that document.
No stable APEX Markdown API, optional JSON adapter or live recall is implemented.

To supply a synthetic record, save an event file **in the input root**:

```json
{
  "contract": "apex-as.delivery-events/v1",
  "synthetic": true,
  "project_id": "demo-delivery-01",
  "records": [{
    "id": "demo-test-record",
    "artifact": "ART-06",
    "kind": "execution",
    "actor": "Invented test owner",
    "at": "2026-10-29T12:00:00+00:00",
    "reference": "synthetic:invented-test-result",
    "revision": 1,
    "sha256": "<copy exact current ART-06 sha256 from status>",
    "outcome": "RECORDED",
    "lanes": ["infrastructure", "database"]
  }]
}
```

Preview/apply with `--events C:\as-demo\inputs\event.json`; do not combine this
with document authoring selection. Inspect `new_events` as well as `changes`.
The hash/revision must identify the current unchanged document and dependencies.
Record kinds/outcomes:

- `execution`: `RECORDED`/`DISPUTED`, ART-05/06 only, lane-specific. One of two
  lanes yields `PARTIALLY_RECORDED`, not full execution.
- `review`: `REVIEWED`, exact document revision and all selected lanes.
- `customer`: `PENDING`/`ACCEPTED`/`REJECTED`, ART-06/07/08 and all selected lanes.
  The actor/time/reference are **supplied claims**, not authenticated identity.
- `release`: `RELEASE_RECORDED`, previously reviewed ART-07/08 and all lanes,
  with nonempty `recipients`. This records an invented local release; no file is
  sent, no cloud operation is permitted, and no auditor is contacted.

Event IDs are immutable; identical replays are no-ops, different contents conflict.
Refresh ART-08 after events to snapshot current state and event provenance in the
handover index. Event capture does not rewrite the Markdown capture form; the
append-only journal/status holds its supplied observations. New drafts cannot
inherit prior customer acceptance; historical facts remain in `history`.

### Safety and support limits

- Current brief/events reject `synthetic: false`, wrong versions/projects, invalid
  structures and unscoped paths. A synthetic flag is a user assertion, not a
  detector of real customer data. Do not feed real material to this build.
- Inputs/documents/state must be disjoint, existing absolute directories. Output/
  state cannot be in this product tree or protected core/configuration locations.
  Symlink/junction/reparse traversal, hidden/parent source paths, core session-state
  reads, output collisions and changed preview inputs are refused.
- Exclusive creates, an exclusive per-project writer lock, source guards and
  journal chaining prevent ordinary accidental overwrites/concurrent writers.
  This is **not an OS sandbox**, protection against a malicious local process
  racing path substitution, signed/tamper-proof storage or power-loss transaction.
  A crash may leave a lock/partial generation: inspect manually; no automatic
  repair, cleanup of unknown files or recovery-success claim.
- Inputs, each document and each state snapshot are limited to 256,000 bytes.
  Journal-size overflow blocks before writing; no pruning of decision history.
  This is a bounded synthetic kit, not an unlimited production records system.
- No dependencies, network calls, shell execution from content, external tool
  invocations, core writes or automatic approvals exist in the delivery runtime.
  Code and the local state directory are trusted; source hashes are not consent.
  Model processing is not needed by this deterministic CLI.

## Source-only package

An inspected allowlist archive excludes `tmp`, the checklist, caches, Git state
and generated customer/project data, even when those exist in the working folder:

```powershell
$package = python -B -m apex_as.package --output C:\as-demo\source-kit.zip | ConvertFrom-Json
$package.files | Format-Table
# After reviewing the explicit source-file list:
python -B -m apex_as.package --output C:\as-demo\source-kit.zip --approve $package.approval
```

The destination must be outside this checkout and must not exist. The archive
contains runtime/guidance, fixtures/tests, canonical docs and the unchanged proof
manifest/agent, plus `APEX-AS-SOURCE-MANIFEST.json` with source hashes.
It is an **experimental source kit**, not a verified native authoring-plugin
release or a license grant. Do not instead zip/copy the entire working folder.

## Native plugin proof

The [AS-001 findings](docs/as-001-native-plugin-proof.md) distinguish authoritative
documentation, local observations and remaining acceptance gates. Local-folder
installation, discovery and a successful synthetic fixture read/report were
observed in Windows VS Code 1.144.0 without using a container. Saved client events
also confirm the selected agent's `read` configuration and approved file read.
Removal, forbidden-tool enforcement and native APEX coexistence remain unverified,
so AS-001 is blocked, not complete. The follow-up has no native UI-control tool;
moving this conversation into VS Code did not provide one. Do not interpret this
demonstration as a supported product release.

Plugin install/removal checks are explicitly deferred. The
[contract/runtime decisions](docs/plan.md#pinned-public-interface-review) identify
schema-pinned planning JSON as an optional future APEX input, not a prerequisite
for generic drafting. Live recall remains unselected because apparently
read-oriented operations can involve index writes or conditional Node validation.

The first profile family is now **Infrastructure and Database Migration to
Microsoft Azure**. The official program page links to a publicly downloadable
checklist, and the user confirmed that the local reference is a direct conversion.
The [source record](docs/prd.md#as-002-first-profile-and-source-authority) retains
the V2.0/V1.9 heading discrepancy and distinguishes public access from
redistribution permission. Link to the checklist; do not bundle its contents.
Partner Module A standing is not a prerequisite to creating project artifacts.
The [implementation evidence](docs/plan.md#implemented-synthetic-delivery-runtime)
separates executed local authoring tests from unverified native plugin behavior.

For a future experimental local test, use **Chat: Install Plugin from Source**
with a reviewed, source-only folder. **Do not copy or distribute this working
folder while it contains the excluded local reference under `tmp`.** Its Git
exclusion is not a plugin-packaging exclusion or access sandbox. Plugin lifecycle
tests are deferred; the previous native test preceded the supplied reference.
This is native plugin registration, not a
VSIX, a Docker image, or copying agents into APEX. Use the same customization
interface to manage it; the documented `/plugin` inventory is separate.
Select the intended harness and `apex-as-fixture` in a fresh chat, then explicitly
supply the absolute path to `fixtures\synthetic-evidence.json`. The expected
demonstration is one REFERENCED item and two MISSING items.

Review the package before enabling it. It has no hooks, MCP servers, shell tools
or dependency installer. The `read` tool restriction is not a filesystem sandbox.
Do not give it customer evidence or assume it discovers a sibling APEX repository.
See the findings for removal steps and the exact tested scope.

## Documents and checks

| Document | Scope |
|---|---|
| [Findings](docs/as-001-native-plugin-proof.md) | Sources, client observations, reproduction and blockers |
| [Plan](docs/plan.md) | First delivery workflow, artifact outlines, APEX boundaries and test cases |
| [PRD](docs/prd.md) | Delivery-companion requirements, checklist provenance and privacy design |
| [Roadmap](docs/roadmap.md) | Delivery-first milestones and separate release gates |
| [Backlog](docs/backlog.md) | Dependency-ordered delivery implementation and verified/deferred work |

Checks use the existing Python standard-library runner, with no installation:

```powershell
python -B -m unittest discover -s tests -v
git diff --check
```

Python is now the **delivery CLI runtime** and test prerequisite, but still not
a dependency of the unchanged prompt-only proof agent. APEX, `apex-recall`,
Azure CLI, Node.js, Docker and devcontainers are not required by the standalone
delivery tool. Actual support is limited to observed host/client tests.

No product license has been selected; no third-party APEX code/schema or checklist
text is included in the authored distributable files. A user-supplied checklist
reference exists locally under Git-ignored `/tmp/`; it must not enter Git or a
plugin payload. Public visibility is not an open-source license grant. Licensing
and reference redistribution rights remain release gates.
