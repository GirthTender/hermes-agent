# Subagent Workspace Hygiene Hardening Handoff — 2026-05-28 10:00 AEST

## Scope

Autonomous Hermes/Crew ops hardening session in `/Users/girthtender/.hermes/hermes-agent`, focused on the safest durable increment in a dirty shared checkout.

Selected scope: strengthen the `subagent-driven-development` skill so future autonomous/subagent implementation runs establish a dirty-worktree boundary and use explicit-path staging instead of broad staging.

## Shipped files

- `skills/software-development/subagent-driven-development/SKILL.md`
  - Bumped version from `1.1.0` to `1.1.1`.
  - Added a "Workspace Hygiene Pre-flight" requiring `git status --short` before implementation dispatch.
  - Added explicit dirty-tree boundary guidance for allowed paths and pre-existing changes.
  - Replaced example `git add -A` usage with explicit-path staging.
  - Added red flags for skipping status checks, broad staging, and touching out-of-scope dirty files.
  - Added a final reminder: "Check workspace first; stage explicit paths only."
- `website/docs/user-guide/skills/bundled/software-development/software-development-subagent-driven-development.md`
  - Regenerated/updated mirror for the skill page and verified it matches the source render.
- `docs/plans/2026-05-28-ops-hardening-session-todo.md`
  - Live todo/checklist for this cron-run session.
- `docs/plans/2026-05-28-subagent-workspace-hygiene-handoff.md`
  - This handoff.

## Verification commands/results

- `git diff --check -- skills/software-development/subagent-driven-development/SKILL.md website/docs/user-guide/skills/bundled/software-development/software-development-subagent-driven-development.md docs/plans/2026-05-28-ops-hardening-session-todo.md`
  - Result: passed with no output.
- Search for broad staging examples in the source skill:
  - `git add -A|git add \.` only appears inside negative/warning guidance, not as a positive instruction.
- Search for broad staging examples in the generated website page:
  - `git add -A|git add \.` only appears inside negative/warning guidance, not as a positive instruction.
- Source-to-website render check:
  - Python import of `website/scripts/generate-skill-docs.py` rendered `skills/software-development/subagent-driven-development/SKILL.md` and compared it with `website/docs/user-guide/skills/bundled/software-development/software-development-subagent-driven-development.md`.
  - Result: `website mirror matches source render`.
- Tests:
  - Skipped full test suite because this is docs/skill-only and final direct verification covered markdown whitespace plus generated page consistency. `scripts/run_tests.sh` availability was confirmed during preflight.

## Review verdicts

- Spec/acceptance review: PASS.
  - Confirmed version bump, dirty-tree preflight, allowed-path guidance, explicit staging, red flags, final reminder, and generated website mirror.
- Quality/safety review: APPROVED.
  - No critical or important issues.
  - Minor note only: generic skill examples still use direct `pytest`; pre-existing and not blocking because the skill is generic rather than Hermes-repo-specific.

## Excluded dirty files / out-of-scope work

Preflight/final status showed these pre-existing or separately-owned dirty files. They were not included in this session's scope:

- `agent/codex_responses_adapter.py`
- `agent/codex_runtime.py`
- `agent/conversation_loop.py`
- `cron/jobs.py`
- `gateway/run.py`
- `gateway/slash_access.py`
- `tests/cron/test_jobs.py`
- `tests/gateway/test_slash_access.py`
- `tests/gateway/test_slash_access_dispatch.py`
- `tests/tools/test_url_safety.py`
- `tools/url_safety.py`
- `.hermes/`
- Existing untracked handoffs:
  - `docs/plans/2026-05-28-autonomous-subagent-session-handoff.md`
  - `docs/plans/2026-05-28-crew-workcell-preflight-closeout.md`
  - `docs/plans/2026-05-28-cron-zero-duration-hardening-handoff.md`
  - `docs/plans/2026-05-28-url-safety-ipv4-mapped-floor-handoff.md`

## Risks / notes

- The repo remains dirty from multiple other work streams; do not commit with broad staging.
- I accidentally invoked `website/scripts/generate-skill-docs.py --help`; that script writes files even with `--help`. I explicitly restored unintended generated drift and kept only the intended subagent-driven-development website mirror.
- No commit or push was performed because the checkout is not clean apart from this session's intended changes.

## Next best session

Recommended next low-risk hardening increment: make `website/scripts/generate-skill-docs.py --help` non-mutating or add a dry-run/check mode so verification can compare generated docs without rewriting unrelated generated files. This directly addresses the only process hazard encountered in this run.
