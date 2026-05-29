# Haz Crew Ops Hardening Handoff — Kanban Retry + Worker Tool Surface

Date/time: 2026-05-28 04:56:08 UTC
Workspace: `/Users/girthtender/.hermes/hermes-agent`
Branch: `pr-27648-web-model-area-clean`

## Scope
Autonomous Hermes/Crew ops hardening session in a dirty shared checkout. Chose a test-only increment that avoids known dirty production files and pins two Crew/Kanban operational invariants:

1. Retried swarm creation with the same idempotency key must reuse the existing topology instead of duplicating task graphs.
2. Kanban worker agents spawned with restrictive toolsets must still receive lifecycle tools when `HERMES_KANBAN_TASK` is set.

## Shipped files
- `tests/hermes_cli/test_kanban_swarm.py`
  - Added `test_create_swarm_idempotent_retry_returns_existing_topology_without_duplicates`.
  - Verifies same returned topology, persisted blackboard topology, and one-worker swarm task count remains 4 after retry.
- `tests/tools/test_kanban_worker_tool_surface.py`
  - New focused tests for model-facing Kanban lifecycle tool exposure with/without `HERMES_KANBAN_TASK`.
  - Covers `kanban_complete`, `kanban_block`, and `kanban_heartbeat` with explicit tool-definition/cache resets.
- `docs/plans/2026-05-28-ops-hardening-cron-todo.md`
  - Live controller todo for this run.
- `docs/plans/2026-05-28-0456-haz-crew-ops-kanban-retry-tool-surface-handoff.md`
  - This handoff.

## Verification commands/results
Controller-run final verification:

```bash
scripts/run_tests.sh tests/hermes_cli/test_kanban_swarm.py tests/tools/test_kanban_worker_tool_surface.py -q
```

Result:

```text
6 passed in 3.92s
```

Whitespace/syntax hygiene:

```bash
git diff --check -- tests/hermes_cli/test_kanban_swarm.py tests/tools/test_kanban_worker_tool_surface.py docs/plans/2026-05-28-ops-hardening-cron-todo.md
```

Result: passed with no output.

Status/diff inspected:

```bash
git status --short
git diff --stat -- tests/hermes_cli/test_kanban_swarm.py tests/tools/test_kanban_worker_tool_surface.py docs/plans/2026-05-28-ops-hardening-cron-todo.md
```

Observed intended scoped changes plus pre-existing dirty tree. Note: `git diff --stat` only reports tracked modifications, so the new untracked test and docs files appear in `git status --short` until staged/committed.

## Review verdicts
- Spec/acceptance review gate: PASS
  - Fresh subagent verified both requested behavioral invariants and reran targeted tests: `6 passed in 3.83s`.
- Quality/safety review gate: APPROVED
  - Fresh subagent verified determinism, env/cache isolation, no unsafe side effects, and scoped dirty-tree hygiene.
  - Also ran targeted tests (`6 passed`) and `git diff --check` clean on scoped files.

## Excluded/pre-existing dirty files
These were present in the preflight or remained dirty but were not intentionally modified by this session:

- `agent/codex_responses_adapter.py`
- `agent/codex_runtime.py`
- `agent/conversation_loop.py`
- `cron/jobs.py`
- `cron/scheduler.py`
- `gateway/run.py`
- `gateway/slash_access.py`
- `skills/devops/kanban-worker/SKILL.md`
- `skills/software-development/subagent-driven-development/SKILL.md`
- `tests/cron/test_jobs.py`
- `tests/cron/test_scheduler.py`
- `tests/gateway/test_slash_access.py`
- `tests/gateway/test_slash_access_dispatch.py`
- `tests/tools/test_url_safety.py`
- `tools/url_safety.py`
- `website/docs/user-guide/skills/bundled/devops/devops-kanban-worker.md`
- `website/docs/user-guide/skills/bundled/software-development/software-development-subagent-driven-development.md`
- `.hermes/`
- pre-existing untracked `docs/plans/2026-05-28-*` handoffs/todos not listed under shipped files above.

## Risks / notes
- No production code changed; this is hardening coverage only.
- The checkout remains broadly dirty, so no commit was attempted.
- The new `tests/tools/test_kanban_worker_tool_surface.py` is untracked until explicitly staged.
- Full suite was not run because the workspace has many unrelated dirty files and the shipped increment is small/test-only; targeted hermetic wrapper tests passed.

## Next best session
Implement a non-mutating check/dry-run/help mode for `website/scripts/generate-skill-docs.py` in a clean checkout or worktree, with focused tests, because prior ops sessions found that even `--help` currently mutates generated skill docs.
