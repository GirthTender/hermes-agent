# URL Safety IPv4-Mapped Always-Blocked Floor Handoff

Date/time: 2026-05-28 09:43:18 AEST
Workspace: `/Users/girthtender/.hermes/hermes-agent`
Branch: `pr-27648-web-model-area-clean`
HEAD: `40e821bc9`

## Live todo / status

- [x] Load relevant local workflow guidance (`AGENTS.md`, subagent-driven development skill doc, prior handoff context).
- [x] Preflight git state, branch, dirty files, and test runner availability.
- [x] Fan out read-heavy discovery across code/test, docs/workflow, and verification lanes.
- [x] Choose small repo-safe scope avoiding pre-existing dirty files.
- [x] Implement URL safety hardening in clean files only.
- [x] Run targeted controller verification.
- [x] Run two fresh subagent review gates: spec/acceptance and quality/safety.
- [x] Inspect final git status/diff.
- [x] Write repo-local handoff.

## Shipped increment

Hardened the URL safety always-blocked floor for IPv4-mapped IPv6 DNS/literal forms.

### Files changed by this session

- `tools/url_safety.py`
  - Added `_matches_always_blocked_floor()` and `_is_always_blocked_ip()` helpers.
  - Centralized the always-blocked metadata/link-local IP/network checks.
  - Normalizes IPv4-mapped IPv6 addresses through `ip.ipv4_mapped` before applying the always-blocked floor, so future IPv4 metadata sentinels do not require a separate `::ffff:x.x.x.x` entry.
  - Replaced repeated inline checks in:
    - `is_always_blocked_url()` literal IP handling
    - `is_always_blocked_url()` DNS answer handling
    - `is_safe_url()` DNS answer handling

- `tests/tools/test_url_safety.py`
  - Imported `_is_always_blocked_ip` for focused helper regression coverage.
  - Added literal IPv4-mapped metadata/link-local always-blocked URL cases.
  - Added hostname-resolution regression coverage for `::ffff:169.254.42.99`.
  - Added direct helper coverage for mapped metadata/link-local cases.

### Excluded / pre-existing dirty files left untouched

Pre-known excluded dirty files from the prompt:

- `agent/codex_responses_adapter.py`
- `agent/codex_runtime.py`
- `agent/conversation_loop.py`
- `.hermes/`

Additional dirty/untracked files observed in preflight and left out of this session's scope:

- `cron/jobs.py`
- `gateway/run.py`
- `gateway/slash_access.py`
- `tests/cron/test_jobs.py`
- `tests/gateway/test_slash_access.py`
- `tests/gateway/test_slash_access_dispatch.py`
- `docs/plans/2026-05-28-autonomous-subagent-session-handoff.md`
- `docs/plans/2026-05-28-crew-workcell-preflight-closeout.md`
- `docs/plans/2026-05-28-cron-zero-duration-hardening-handoff.md`

## Verification commands/results

Controller session verification:

```bash
PYTHONDONTWRITEBYTECODE=1 scripts/run_tests.sh tests/tools/test_url_safety.py -q -p no:cacheprovider
```

Result:

```text
123 passed in 8.18s
```

```bash
git diff --check -- tools/url_safety.py tests/tools/test_url_safety.py
.venv/bin/ruff check --no-cache tools/url_safety.py tests/tools/test_url_safety.py
```

Result:

```text
All checks passed!
```

Final intended diff summary:

```text
tests/tools/test_url_safety.py | 24 ++++++++++++++++++++++++
tools/url_safety.py            | 41 ++++++++++++++++++++++++++++++-----------
2 files changed, 54 insertions(+), 11 deletions(-)
```

Final full repo status still contains unrelated pre-existing dirty files plus this session's two modified files and this handoff.

## Review verdicts

Spec/acceptance review: **PASS**

- Confirmed helper centralization and IPv4-mapped normalization meet scope.
- Confirmed replacements cover literal and DNS-answer paths in both always-blocked floor and full safety check.
- Confirmed `is_always_blocked_url()` remains narrower than `is_safe_url()`.
- Reviewer independently ran targeted tests, diff check, and ruff successfully.

Quality/safety review: **APPROVED**

- No security regression or correctness issue found.
- Test coverage judged sufficient for the implemented hardening.
- Reviewer independently ran targeted tests, diff check, and ruff successfully.

## Risks / notes

- Full test suite was not run because the checkout already has substantial unrelated dirty work and a targeted, isolated URL-safety change was safer to verify narrowly.
- No commit was made because the repo is not clean apart from this session's intended changes.
- The helper is private and intentionally limited to `_ALWAYS_BLOCKED_IPS` / `_ALWAYS_BLOCKED_NETWORKS`; it does not apply broader private-IP blocking, preserving the documented semantic difference between `is_always_blocked_url()` and `is_safe_url()`.

## Next best autonomous session

Implement the docs/workflow hardening discovered by the docs lane: add durable Kanban/Crew worker mutation-hygiene guidance to `skills/devops/kanban-worker/SKILL.md`, regenerate the bundled skill docs, and optionally add a concise prompt nudge in `agent/prompt_builder.py` only if token/scope risk is acceptable. Keep it separate from the current dirty gateway/cron/codex files.
