# Haz Crew Ops Hardening Live Todo — 2026-05-28

- [x] Load subagent-driven-development skill and autonomous burn-in reference.
- [x] Run preflight: git status, branch, root, test wrapper availability.
- [x] Fan out read-heavy discovery lanes.
- [x] Synthesize safe scope avoiding pre-existing dirty files: Kanban worker shared-repo dirty-tree preflight docs.
- [x] Implement smallest durable improvement through subagent(s).
- [x] Run spec/acceptance review gate: PASS.
- [x] Run quality/safety review gate: APPROVED after explicit dirty-file scope accounting.
- [x] Run final verification in controller session.
- [x] Inspect git status/diff for intended files only.
- [x] Write final handoff under docs/plans/.

## Session-owned files

- `skills/devops/kanban-worker/SKILL.md`
- `website/docs/user-guide/skills/bundled/devops/devops-kanban-worker.md`
- `docs/plans/2026-05-28-haz-crew-ops-hardening-live-todo.md`
- `docs/plans/2026-05-28-1313-haz-crew-ops-kanban-worker-dirty-tree-handoff.md`

## Explicitly excluded pre-existing dirty/shared-repo noise

Observed in fresh preflight before implementation and not owned by this session:

- `agent/codex_responses_adapter.py`
- `agent/codex_runtime.py`
- `agent/conversation_loop.py`
- `cron/jobs.py`
- `cron/scheduler.py`
- `gateway/run.py`
- `gateway/slash_access.py`
- `skills/software-development/subagent-driven-development/SKILL.md`
- `tests/cron/test_jobs.py`
- `tests/cron/test_scheduler.py`
- `tests/gateway/test_slash_access.py`
- `tests/gateway/test_slash_access_dispatch.py`
- `tests/tools/test_url_safety.py`
- `tools/url_safety.py`
- `website/docs/user-guide/skills/bundled/software-development/software-development-subagent-driven-development.md`
- `.hermes/`
- Pre-existing untracked `docs/plans/` handoffs/todos unrelated to this session.
