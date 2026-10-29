# AS-001 native plugin proof

**Date:** 2026-10-29. **Verdict:** partial proof; AS-001 is blocked on remaining
client acceptance gates. Full M0 is not complete.
This record separates client observations from documented capabilities.

**User deferral:** on 2026-10-29, plugin install/removal was explicitly deferred
to a later task. The next scoped work is the AS-003/AS-005 public contract/runtime
review in [plan](plan.md); no further lifecycle changes are attempted. Existing
unverified acceptance gates are not waived.
The later AS-002/AS-004 authorization added source review and design work only.
The user then clarified the product as a project-delivery artifact companion,
not a partner assessment tool; current direction is in [PRD](prd.md).
The user-supplied reference is now present under Git-ignored `tmp`
inside the local registration root; this was not present during the successful
fixture invocation. No new plugin install/use test is claimed with that material
present. Do not copy/distribute the folder or mistake Git ignore for plugin
payload filtering or a file-access boundary.
Its official public download provenance was subsequently confirmed through the
program-page link and user's conversion history; earlier restricted/private labels
do not establish confidentiality. The source remains excluded from the authored
payload because public access alone does not establish redistribution permission.

**Later implementation:** a standalone synthetic Python delivery CLI and
source-only archive builder were added without changing `plugin.json` or
`apex-as-fixture.agent.md`. Their local authoring/rehearsal tests are recorded in
[plan](plan.md#implemented-synthetic-delivery-runtime). They do not prove native
agent write permissions, install/update/remove or APEX coexistence. No plugin
lifecycle operation was performed during that implementation.

## Starting point and provenance

The worktree began clean on `special-giggle`, at `12c635d` (initial README only).
It was renamed through the app to `native-plugin-proof` before file creation.
No repository instructions, plan, PRD, roadmap, backlog, package manager or test
configuration existed in this checkout.

`gh pr view 1` reported [PR #1](https://github.com/jonathan-vella/apex-as/pull/1)
OPEN with `mergedAt: null`. Its five proposed documents were read from exact
commit `b86b394ecae468e401db35c55e19300a06ab52d6`, not merged or cherry-picked.
The bounded documents here do not silently adopt the rest of that proposal.
No commits, pushes, PR creation or remote configuration changes were performed.

## Authoritative sources

Retrieved on 2026-10-29; these are living documentation, not frozen support promises.

| Source | Relevant documented contract |
|---|---|
| [VS Code agent plugins](https://code.visualstudio.com/docs/agent-customization/agent-plugins) | Native local-folder/Git install, enable/disable, removal, `chat.plugins.enabled`, policy/harness differences, separate `/plugin` inventory |
| [Plugin authoring reference](https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference) | Root manifest schema; Copilot agent directory; supported formats; no invented manifest dependency fields |
| [Custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents) | Picker discovery and `tools` restrictions; actual tool availability depends on harness |
| [Agent file reference](https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference) | `read` alias; invocation flags; conversion does not forward `strict-tools-list`, `mcp-servers` and several other fields |
| [Agent harnesses](https://code.visualstudio.com/docs/agents/concepts/agent-harnesses) | Model, role, harness and execution environment are separate choices |
| [Tool availability](https://code.visualstudio.com/docs/agents/run/tools) | Tool availability differs from approval; Copilot tools are managed in Agent Customizations |

Documentation warns that installed hooks/MCP servers can execute code and that
plugin MCP servers are implicitly trusted on installation. This proof includes
neither. A valid manifest does not prove permissions or runtime behavior.
Documentation describes custom-agent delegation generally; it does not establish
an APEX-specific cross-plugin invocation contract. That capability is not used.

## Local environment and observations

`code --version` returned VS Code `1.144.0`, commit
`2c33b50b16c472efe58357d1d2a8a5414bc23fbf`, x64.
`code --status` reported Windows `10.0.26300`.

An existing APEX devcontainer window was observed but not used for this test,
modified or restarted. A **new native empty VS Code window** was opened using
File > New Window. This distinction matters: an existing container process on
the machine is neither required by, nor proof of, a native test.

In the new window:

1. Chat: Open Customizations opened Agent Customizations labeled **Local**.
2. Plugins listed five existing user plugins, and Agents listed 42 agents
   (20 plugin agents). These were not modified.
3. With explicit user approval, Install Plugin from Source accepted this
   checkout's root Windows path. The result appeared under **User** as
   `apex-as-proof`, Enabled. Despite starting from the Workspace add control
   in an empty window, the observed result was User scope; do not assume scope.
4. Plugins increased to six; Agents increased to 43 (21 plugin agents).
   `apex-as-fixture` displayed the exact source
   `com.github.copilot\agents\apex-as-fixture.agent.md` inside this worktree.
   The plugin was registered from the local source, not demonstrated as a
   separately copied, immutable installation.
5. In a fresh Chat composer with **Copilot** target, Interactive/manual
   permissions and Remote Connections Off, the agent appeared in the picker
   and was selected. This is distinct from the Local-labeled customization editor.
6. With separate user approval, the synthetic-only prompt below was submitted
   once through Send. An initial keyboard Return had left the prompt unsent;
   the visible chat request confirmed the subsequent Send action.
7. The completed response displayed a **Read** tool call with exactly the supplied
   fixture path, then the expected three-row table and **1 REFERENCED, 2 MISSING**.
   It included the synthetic disclaimer, contract, literal design reference,
   missing acceptance/platform references, and the required no-APEX statement.
   The client reported completion in 20 seconds. No write, command, delegation
   or Azure call appeared in this observed turn. All three source fingerprints
   below were unchanged afterward.
8. The user approved removal of only this proof's registration, preserving
   source files. Before reaching the removal control, the UI server twice
   reported active user input. Automation yielded rather than forcing focus
   or modifying host settings through a different channel. **No removal was
   performed; `apex-as-proof` remains installed.**

The client also displayed an existing Work IQ (Connector) authentication notice.
No authentication or other integration action was taken; the synthetic Read/report
completed without it. Extension-provided agent counts later increased from 43
to 60 during client activation, so the aggregate count alone is not a stable
removal assertion. Use exact plugin/agent identities.

The composer initially retained `apex-as-fixture` after completion; a subsequent
read showed the built-in Agent selected. The cause was not established.
Do not assume role selection persists, or infer effective session tools from a
later picker state. No additional prompt was submitted.

## Acceptance matrix

| Capability | Result | Evidence / limitation |
|---|---|---|
| Documented native packaging | PASS (documentation) | Agent Plugins 1.0 manifest and Copilot-specific directory |
| Native local-source install | PASS (local observation) | User inventory 5 -> 6; `apex-as-proof` enabled |
| Plugin-agent discovery and selection | PASS (local observation) | Exact plugin source; agent inventory 42 -> 43; selected in Copilot composer |
| Fixture invocation and gap report | PASS (local observation) | Completed Read of explicit path; expected IDs, statuses, literal reference, disclaimers and totals |
| Selected tool configuration and read approvals | PASS (saved client events) | `subagent.selected` recorded `tools: ["read"]`; manual path/read approvals recorded |
| Forbidden-tool enforcement | UNVERIFIED | Expanded runtime tool inventory and denial behavior not established |
| APEX coexistence | BLOCKED / unverified | No native client-control surface in follow-up; pinned upstream source inspection is not functional coexistence |
| Removal and no overwrites | BLOCKED / unverified removal | Source fingerprints still match; no editor control available; CLI inventory is not an equivalent substitute |
| No-container install/use | PASS for this fixture journey | Native empty Windows window, Copilot target, local file read; no container/dependency commands |
| Complete no-container lifecycle / clean host | NOT YET PASSED | Removal incomplete; Docker was already present elsewhere on this host |
| Automatic sibling-repository discovery | NOT CLAIMED | Explicit path required; no search tool or adapter |
| Cross-plugin APEX calls | UNVERIFIED / unused | No APEX agent invocation contract consumed |
| Automatic dependency installation | NOT PROVIDED | No installer, hooks, MCP servers or executable dependencies |
| Remote distribution and clean-host support | UNVERIFIED | No Git-source, marketplace, clean-profile or second-host test |

## Reproduction and expected result

Use a native VS Code window, not a remote/container workspace. Review all package
contents first. Ensure plugins are policy-permitted and enabled. A Copilot
account/model connection with usable entitlement/network is a client prerequisite;
this plugin cannot install or authenticate the client for you.

Run **Chat: Install Plugin from Source** and enter this checkout's absolute
root directory. Check its actual scope and Enabled status under Plugins.
Start a fresh Copilot chat and select `apex-as-fixture`. Submit, with a path
adjusted to your checkout:

```text
Read only C:\repos\copilot-worktrees\apex-as\special-giggle\fixtures\synthetic-evidence.json and report its synthetic gaps in chat. Do not write files, run commands, access Azure, or invoke other agents.
```

Expected output: SYNTHETIC ONLY; contract `apex-as.synthetic-proof/v1`;
`demo-design` REFERENCED with literal `synthetic:design-note-01`;
`demo-acceptance` and `demo-platform` MISSING; totals 1 and 2.
References must not be opened or called verified evidence.

If the read tool cannot access the supplied path, report BLOCKED. Do not enable
execution tools, copy agents into APEX, search another repository or install
dependencies to make the experiment appear to pass. Use only a separately
authorized synthetic attachment/path for any subsequent access test.

For removal, use the same Agent Customizations Plugins interface, select only
`apex-as-proof`, and use Uninstall/Remove as offered by that client. Inspect any
confirmation and source-deletion warning before proceeding: a local checkout
must survive. Verify the plugin and its agent disappear in a fresh session,
unrelated plugins remain, and source/fixture hashes remain unchanged.
Do not infer data deletion from plugin removal; host chat history may remain.

## Unattended follow-up in VS Code

The user requested unattended continuation after moving this conversation into
VS Code. `code --version` confirmed the same `1.144.0` build; `code --status`
showed the native proof workspace and an empty native window. That is host
diagnostic evidence, not proof of any role selected in those windows.
PR #1 was rechecked: still OPEN, unmerged, at the same proposal commit.

The dedicated computer-use tools are no longer available. A bounded client-tool
capability check found no alternative supported native VS Code UI/command tool.
`code --help`, `code agent --help`, `code agent ps --help`,
`code agent logs --help` and `code chat --help` were inspected. The advertised
commands offer session/host diagnostics and chat startup, but no editor plugin
uninstall command or expanded effective-tool inspector. No endpoint tokens,
remote connections or new agent host were requested.

The current official plugin documentation explicitly says the `/plugin`
commands and Agent Customizations editor use separate inventories. Therefore:

- CLI `/plugin uninstall` is not used as a substitute for removal of the
  editor-installed registration.
- Extension uninstall is not plugin uninstall.
- Private settings, caches and host databases are not edited to simulate a
  successful native removal. No focus/keyboard/browser automation workaround
  was used after computer-use became unavailable.
- No APEX clone was opened merely to call static source inspection a native
  coexistence test. The pinned upstream tree was rechecked: workspace agents
  exist (including `01-Orchestrator`), but no plugin manifest was found.

### Saved runtime evidence

Only the existing synthetic proof session was inspected:
`~/.copilot/session-state/f29bdab2-68b6-446f-a076-16ea1bc105a1/`.
Its `workspace.yaml` identifies `client_name: vscode-agent-host` and the exact
previously approved synthetic prompt. The working directory is a host-owned
empty-chat directory, not APEX or this repository. No unrelated session contents,
credentials or complete system prompts are copied into this repository.

Selected fields from its `events.jsonl`:

```json
{
  "selection": {
    "event": "subagent.selected",
    "agentName": "apex-as-fixture",
    "tools": ["read"]
  },
  "execution": {
    "event": "tool.execution_start",
    "toolName": "view",
    "path": "C:\\repos\\copilot-worktrees\\apex-as\\special-giggle\\fixtures\\synthetic-evidence.json"
  },
  "completion": {
    "event": "tool.execution_complete",
    "success": true
  },
  "permissions": [
    {"mode": "manual", "kind": "path", "result": "approved", "decisionSource": "human_response"},
    {"mode": "manual", "kind": "read", "result": "approved", "decisionSource": "host_policy"}
  ]
}
```

This is a reduced diagnostic summary, not a verbatim runtime schema. Both
permission requests belong to the same file-read call. The path approval offered
the fixture directory as a read-only directory; no denied-path behavior was
tested. The `read` alias is not a per-file sandbox.

The session records model `gpt-6.1-sol` and Copilot runtime
`1.0.103-unstable.r40031404408.gba6c003`. Exactly one tool execution was recorded;
its completion matched the call ID and succeeded. PowerShell assertions against
these events passed. The log snapshot SHA-256 was
`2452FF815F452E445E73F84AD30BF57908309C55074EA785BEB91F523E4F4EB7`.
Raw host diagnostics are local and uncommitted; logs can change with host activity.

This improves the evidence from an authored tool declaration to a client-recorded
selection and actual permission checks. It does **not** show all tools exposed to
the model, prove edit/execute/delegation are denied, or make this conversation
itself a run of `apex-as-fixture`.

### Remaining client test procedure

Use the same native editor inventory, not the CLI inventory:

1. Select the intended Copilot harness and `apex-as-fixture` in a fresh chat.
   Inspect the expanded available tools. Record canonical names and any required
   built-ins, rather than assuming the `read` alias means only one tool.
   A forbidden-tool test must establish that execute/edit/delegation is unavailable
   or denied; an LLM declining a request in prose is not enforcement evidence.
   Do not grant new write, shell, cloud or delegation permissions.
2. In a separate native workspace at APEX revision
   `504349259c26e36c750c7d6669c0b1de554e6b35`, record the APEX workspace-agent
   inventory and clean source state. Confirm both `01-Orchestrator` and the
   installed `apex-as-fixture` remain discoverable. Invoke only the add-on against
   this synthetic fixture with an explicit path. Do not invoke APEX orchestration,
   install its development dependencies, reopen in a container or change core.
   If any of those is needed, record the precise blocker, not a compatibility pass.
3. Use Agent Customizations > Plugins > `apex-as-proof` > Uninstall.
   Registration removal is approved; source deletion is not. Stop if deletion of
   the original checkout is proposed. Confirm exact plugin/agent disappearance in
   a fresh session, unchanged unrelated plugin and APEX-agent availability, and
   unchanged plugin/fixture/APEX source. Existing chat history may persist.

No new invocation or uninstall was performed in this follow-up. Last observed
installed; the current UI inventory could not be re-read. Native install/use
remains passed; native removal, full permissions and coexistence remain blocked.

## APEX, storage and host contracts

See [plan](plan.md) for the exact upstream research baseline and separate
artifact-only/recall-connected decisions. No APEX artifacts, agents, sessions,
private modules or recall commands were consumed. The proof uses no add-on state
files and never reads/writes APEX session state. Host-owned plugin registration
and chat history are separate from APEX state; their retention is a host concern.

The `read` alias is a tool allowlist, not a path-specific permission grant or an
OS sandbox. Fixture instructions are behavioral restrictions, not a demonstrated
security boundary. No adversarial isolation or all-host support is claimed.

## Checks

`python -B -m unittest discover -s tests -v`: three static tests passed.
They check the authored metadata subset, one agent/read-only declaration, absent
active integrations and exact synthetic fixture. They are not a full external
JSON Schema/YAML validator and do not test language-model compliance.
`git diff --check`: passed for tracked changes. A final standard-library check
also checks all authored files for trailing whitespace and all authored Markdown
relative links, including untracked files. No package installation was needed.
The unattended follow-up reran these checks and asserted the saved fixture-session
selection, tool call path/count, successful matching completion and source hashes.

Pre/post-invocation SHA-256 fingerprints (all matched):

| File | SHA-256 |
|---|---|
| `plugin.json` | `EB608DFA95AE2DE22FE81AE6B96699349C661C90CEA19C2436EE550E728B69A4` |
| `com.github.copilot/agents/apex-as-fixture.agent.md` | `90F228D1830C343A45B4BC4B32774F9E96E6A27B3E4D06775217E6086E440CEF` |
| `fixtures/synthetic-evidence.json` | `31D443BB94DB554670F2A2BB29068A9E8638D332890CA5DE06E4447C1A2DC011` |

## Remaining proof

Resume in an idle client to inspect the effective session tool allowlist and
complete native removal, exact-name disappearance in a fresh chat, unrelated
plugin survival and source retention. If removal offers source deletion, stop.
Then demonstrate coexistence in an
explicitly selected native APEX workspace at an exact baseline without changing
APEX core. The inspected upstream baseline has no plugin manifest and documents
a container setup; that is a limitation, not permission to repackage APEX here.
Do not treat a native empty-window test as APEX compatibility or a clean machine
with Docker absent. Keep AS-001 open until those required gates are demonstrated.
