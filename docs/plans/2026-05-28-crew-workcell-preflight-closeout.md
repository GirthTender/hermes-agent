# Crew Work-Cell Preflight and Closeout Runbook

Reusable checklist for launching and closing a Crew/Hermes work-cell with clear routing, safe fan-out, and verifiable PASS criteria.

## Trigger Conditions

Start this runbook when any of the following are true:

- A task needs multiple agents, subagents, or parallel workstreams.
- The work has repository, filesystem, deployment, messaging, or user-visible side effects.
- The request spans planning, implementation, verification, and reporting phases.
- The task owner needs a clean handoff, audit trail, or closeout summary.

Do not fan out when a single direct action is faster, safer, and fully verifiable by one agent.

## Preflight Checks

Before dispatching work:

- Confirm the exact workspace/repository path; never assume container-style paths.
- Check current git status and identify dirty files that must not be edited.
- Read local instructions such as `AGENTS.md`, task notes, or relevant runbooks.
- Identify required artifacts, output paths, and whether code changes are allowed.
- Define the owner, scope, expected deliverable, and stop conditions.
- List destructive or external side effects and require explicit confirmation before performing them.
- Choose verification commands or read-back checks before implementation begins.

## Fan-Out Rules

When splitting work across agents:

- Assign one clear owner/coordinator for final synthesis and route control.
- Give each worker a bounded task, exact paths, non-editable files, and required verification.
- Prefer independent workstreams; avoid two workers editing the same file or subsystem.
- Require workers to report: files touched, commands run, verification result, blockers, and residual risk.
- Keep shared state minimal and explicit; do not rely on hidden assumptions from another worker.
- Stop fan-out if conflicts, ambiguous ownership, or unsafe side effects appear.

## Route and Messaging Guardrails

During execution:

- Keep user-facing messages concise and outcome-oriented.
- Do not expose raw internal chain-of-thought or unrelated agent chatter.
- Route clarification questions through the coordinator unless a worker is explicitly user-facing.
- Use platform-appropriate formatting; avoid tables where the route does not support them well.
- Send files/media only when the artifact is complete and the path is verified.
- Never claim an action was performed unless a tool result or worker report confirms it.

## Closeout / PASS Criteria

A work-cell can close only when all apply:

- Required artifact or change exists at the requested path.
- Dirty-file constraints were respected.
- Verification was run and passed, or any skipped verification is explicitly justified.
- Worker outputs have been reconciled into one final answer.
- Open blockers, risks, and follow-up items are documented.
- Final response includes what changed, files touched, verification performed, and issues encountered.

## Verification Checklist

Use the lightest check that proves the deliverable:

- Read back created or edited non-code artifacts.
- Run formatting, lint, tests, or targeted commands for code/config changes.
- Check git status after work to confirm only intended files changed.
- For messaging artifacts, verify links, paths, and platform formatting assumptions.
- For side-effecting operations, verify the external state and capture the evidence.

## Minimal Closeout Template

- What I did: `<brief action summary>`
- Files created/modified: `<paths>`
- Verification: `<commands/checks and result>`
- Issues or risks: `<none, or concise list>`
