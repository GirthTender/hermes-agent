# Haz Crew Ops Hardening Handoff — Kanban Worker Dirty-Tree Preflight

Timestamp: 2026-05-28 13:13:48 AEST
Workspace: `/Users/girthtender/.hermes/hermes-agent`
Branch: `pr-27648-web-model-area-clean`

## Scope

Autonomous Hermes/Crew ops hardening session focused on a small, repo-safe increment in a dirty shared checkout. The selected scope was docs-only guidance for Kanban workers operating in shared git-backed workspaces.

## Shipped files

- `skills/devops/kanban-worker/SKILL.md`
  - Added `### Shared repo / dirty-tree preflight` under workspace handling.
  - Guidance now tells workers in git-backed `dir:<path>` and `worktree` workspaces to run `git status --short`, treat existing dirty/untracked files as other worker/human work, avoid broad staging, block on unrelated dirty-file conflicts, and report `changed_files` / `tests_run`.
- `website/docs/user-guide/skills/bundled/devops/devops-kanban-worker.md`
  - Manually mirrored the same section in the generated website page, without running the broad docs generator.
- `docs/plans/2026-05-28-haz-crew-ops-hardening-live-todo.md`
  - Live todo and explicit dirty-file scope ledger for this session.
- `docs/plans/2026-05-28-1313-haz-crew-ops-kanban-worker-dirty-tree-handoff.md`
  - This handoff.

## Verification commands and results

- `test -x scripts/run_tests.sh && ...`
  - Result: `scripts/run_tests.sh executable`; `.venv present`.
- `PYTHONDONTWRITEBYTECODE=1 scripts/run_tests.sh tests/website/test_generate_skill_docs.py -q -p no:cacheprovider`
  - Result: `7 passed in 8.08s`.
- `git diff --check -- skills/devops/kanban-worker/SKILL.md website/docs/user-guide/skills/bundled/devops/devops-kanban-worker.md docs/plans/2026-05-28-haz-crew-ops-hardening-live-todo.md`
  - Result: passed with no output.
- Read-back checks:
  - `skills/devops/kanban-worker/SKILL.md` lines 26-30 contain the new section.
  - `website/docs/user-guide/skills/bundled/devops/devops-kanban-worker.md` lines 44-48 contain the mirrored section.
- `git diff -- skills/devops/kanban-worker/SKILL.md website/docs/user-guide/skills/bundled/devops/devops-kanban-worker.md`
  - Result: only the intended six-line section was added to each file.
- `git status --short`
  - Result: showed the two intended tracked docs changes plus pre-existing unrelated dirty files listed below and session-owned untracked docs/plans files.

## Review verdicts

- Spec/acceptance review gate: PASS.
  - Verified the new guidance covers all required behaviors: status check, dirty/untracked ownership, no broad staging, conflict blocking, and completion/review metadata.
- Quality/safety review gate: APPROVED on re-review.
  - First pass requested explicit dirty-file accounting because the shared checkout was already dirty.
  - Re-review approved after `docs/plans/2026-05-28-haz-crew-ops-hardening-live-todo.md` documented session-owned files and excluded pre-existing dirty/shared-repo noise.

## Excluded pre-existing dirty files / paths

Observed during fresh preflight before this session's implementation and not owned by this session:

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

## Risks and notes

- No commit was made because the checkout is dirty with multiple unrelated pre-existing changes.
- The website page is generated, but the broad generator was intentionally not run in this dirty checkout because it may rewrite unrelated docs/catalog/sidebar files. The targeted generated-docs test passed.
- Full test suite was not run; targeted docs generator tests plus `git diff --check` were the appropriate verification surface for this docs-only increment.

## Next best session

Pick one of these, after either cleaning/committing current dirty work or creating an isolated worktree:

1. Implement the candidate code hardening found during discovery: relay nested delegate progress through modern `subagent.progress` metadata in `tools/delegate_tool.py`, with a focused `tests/tools/test_delegate.py` regression.
2. If staying docs-only, add a lightweight check or script to compare one generated skill docs page against its source without running the full generator.
3. In a clean checkout, finish/review the existing cron, URL safety, and slash-access dirty surfaces before stacking more changes on them.
