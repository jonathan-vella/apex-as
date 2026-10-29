# Delivery-first roadmap

The original roadmap in
[PR #1](https://github.com/jonathan-vella/apex-as/pull/1) is open and unmerged.
This local roadmap follows the user's 2026-10-29 clarification: help partners
create checklist-aligned artifacts during every project, not assess partners.
It replaces the proposal's assessment/portfolio-first sequencing locally;
no merge, remote roadmap update or complete native product release is implied.

## M0 - Direction, source and safe delivery design

**Designed:** [product requirements](prd.md#product-purpose-and-boundaries),
[D0-D6 Infra/Database workflow](plan.md#first-infradatabase-project-workflow),
eight original artifact outlines, draft/result/customer-decision separation,
ownership/privacy and synthetic cases. The public program-to-checklist link and
user-reported direct conversion are recorded. V2.0/V1.9 heading ambiguity remains
an affected-guidance issue, not a blanket bar to generic drafting.

Module A partner standing, audit date and external-ALZ audit acceptability are not
product-development prerequisites. For each delivery, identify platform owners
and needed inputs; prepare requests/capture points, never generate a partner
pass/fail decision or mutate an ALZ to fill a documentation gap.

**Implemented locally:** reusable JSON guidance, strict synthetic brief/event
contracts, three workload examples and deterministic Python drafting through all
eight artifacts. **Not implemented:** native authoring agent, general task-state
machine, APEX adapter, real project processing or external document transmission.
Local path/write guards are not OS sandboxing or organizational consent.

### Separate native distribution gate: AS-001

Native plugin support is documented; local install/discovery and synthetic
invocation passed in a native Windows client. The
[acceptance record](as-001-native-plugin-proof.md) controls the result;
unobserved permission enforcement, coexistence or removal cannot be marked
passed. **AS-001 is blocked on client-observed removal, forbidden-tool enforcement
and native APEX coexistence.** A follow-up inspected real saved session events:
the `read` configuration and file-read approvals are confirmed, but no client
management tool is available to this session to complete the remaining UI gates.

Plugin install/removal remains explicitly deferred. Synthetic design and isolated
authoring experiments need not stop, but supported release still requires actual
native lifecycle/permission/coexistence tests, clean payload and licensing.
No required devcontainer, Docker workflow or APEX core changes are acceptable.
The local public reference under ignored `tmp` remains excluded from distribution;
Git ignore is not a packaging filter or access sandbox.

## M1 - Kickoff and discovery authoring slice (local synthetic subset passed)

AS-002 D0-D1 guidance, AS-006/009 assets/cases and AS-008/011 authoring.

**Exit:** from a synthetic project brief, create a reviewable artifact plan and
workload-assessment output draft at approved paths. Unknowns become placeholders/
owner actions; external ALZ becomes a scoped input request. Only authorized new
files/revisions change; no results/sign-offs/partner verdicts invented. Repeat
on a second project without carried-over facts. Native runtime validation must
demonstrate the write boundary, not just manifest/frontmatter validity. The local
CLI tests now exercise actual drafts, preview digest binding, source preservation,
collisions, user edits and new-project isolation. Native agent authoring remains
outside that evidence.

## M2 - Complete one project delivery record (local synthetic subset passed)

AS-010/016/012: change-aware design and migration/validation plans, execution
capture, real-response references, operations handover and current-revision index.

**Exit:** synthetic D0-D6 journey keeps plans distinct from supplied actual results
and customer decisions; changed inputs invalidate only affected current review
context, preserving history. Handover release is separately authorized and
includes open actions. The real local CLI rehearsal supplied invented execution
and pending/rejected/accepted customer records, refreshed the index and preserved
history after changes. No audit exporter, cloud execution or actual customer
interaction occurred.

## M3 - Verified native package and reusable kit

Resume AS-001; AS-005/013/014 host/runtime/package tests, AS-015/017 rehearsal and
reuse, AS-020 release checks. Add AS-007 optional APEX reuse only after its contract
and side-effect tests; standalone drafting cannot depend on it. AS-018 addresses
later project changes, not cross-customer portfolio scoring.

**Exit:** declared native hosts pass full install/use/revise/handover/update/remove
tests; another practitioner can repeat the method with fresh synthetic identity
and state. Report measured usefulness/rework, not an assumed reuse percentage.
No real customer pilot is authorized by this milestone's synthetic rehearsal.

**Progress:** an allowlist source zip/manifest is implemented/tested; the full
native CLI rehearsal repeats across mixed, infra-only and database-only projects.
These are not a native authoring-plugin package/lifecycle pass, another
practitioner's usefulness review, authenticated acceptance or hosted CI.

## M4 - Maintain and expand delivery guidance

AS-019/021: new guidance families only after Infra/Database reuse is demonstrated,
with source/version stewardship, owner-reviewed template changes, license,
support and data-handling expectations. Do not retroactively rewrite customer
documents or imply Microsoft endorsement.

See [implementation order](backlog.md#implementation-order). This roadmap contains
no partner-assessment engine, eligibility population counter or mandatory
cross-plugin task dispatch.
