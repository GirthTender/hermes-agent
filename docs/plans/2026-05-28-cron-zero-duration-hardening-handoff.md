# Cron zero-duration hardening handoff

Date/time: 2026-05-28 09:25:02 AEST
Workspace: `/Users/girthtender/.hermes/hermes-agent`
Branch: `pr-27648-web-model-area-clean`

## Summary

Shipped a small, repo-safe cron scheduler hardening increment: zero-length durations are now rejected before they can become one-shot or recurring schedules.

## Shipped files

- `cron/jobs.py`
  - `parse_duration()` now raises `ValueError("Duration must be positive")` when the parsed numeric value is `0` or lower.
  - Negative values were already rejected by the duration regex; the explicit guard closes the zero-duration case.
- `tests/cron/test_jobs.py`
  - Added regression coverage for:
    - `parse_duration("0m")`
    - `parse_duration("0 h")`
    - `parse_schedule("every 0m")`
    - `parse_schedule("0m")`

## Why this scope

Parallel discovery identified zero-duration cron schedules as a low-risk code/test hardening target that avoided all pre-existing dirty/excluded files. Without the guard, `every 0m` can compute a next run equal to the previous/current timestamp, which risks scheduler churn or rapid re-trigger behavior.

## Verification commands and results

Controller final verification:

```bash
scripts/run_tests.sh tests/cron/test_jobs.py -p no:cacheprovider
```

Result:

```text
82 passed in 7.85s
```

Additional implementation/review verification reported by subagents:

```bash
scripts/run_tests.sh tests/cron/test_jobs.py -k 'ParseDuration or ParseSchedule' -p no:cacheprovider
```

Result:

```text
15 passed
```

Spec reviewer also ran:

```bash
scripts/run_tests.sh tests/cron/test_jobs.py
```

Result:

```text
82 passed
```

## Review verdicts

- Spec/acceptance review: PASS
  - Confirmed zero durations are rejected through both direct duration parsing and schedule parsing.
  - Confirmed valid positive durations remain unchanged.
- Quality/safety review: APPROVED
  - No critical issues.
  - No important issues.
  - Minor note: `parse_schedule("0m")` ultimately surfaces the existing generic invalid-schedule message after the one-shot duration branch falls through. This is acceptable for the hardening goal and consistent with the existing invalid-duration fallback behavior.

## Repo status / diff inspection

Final inspected target diff:

```diff
diff --git a/cron/jobs.py b/cron/jobs.py
@@
     value = int(match.group(1))
+    if value <= 0:
+        raise ValueError("Duration must be positive")
     unit = match.group(2)[0]  # First char: m, h, or d
```

```diff
diff --git a/tests/cron/test_jobs.py b/tests/cron/test_jobs.py
@@
+    def test_zero_duration_raises(self):
+        with pytest.raises(ValueError):
+            parse_duration("0m")
+        with pytest.raises(ValueError):
+            parse_duration("0 h")
@@
+    def test_zero_interval_duration_raises(self):
+        with pytest.raises(ValueError):
+            parse_schedule("every 0m")
+
+    def test_zero_oneshot_duration_raises(self):
+        with pytest.raises(ValueError):
+            parse_schedule("0m")
```

Final `git status --short` included this session's intended files plus pre-existing excluded files. No commit was made because the checkout is not clean apart from unrelated dirty work.

## Excluded dirty/pre-existing files

Preserved as out of scope; not intentionally modified by this session:

- `agent/codex_responses_adapter.py`
- `agent/codex_runtime.py`
- `agent/conversation_loop.py`
- `gateway/run.py`
- `gateway/slash_access.py`
- `tests/gateway/test_slash_access.py`
- `tests/gateway/test_slash_access_dispatch.py`
- `.hermes/`
- `docs/plans/2026-05-28-autonomous-subagent-session-handoff.md`
- `docs/plans/2026-05-28-crew-workcell-preflight-closeout.md`

This handoff file is also new from this session:

- `docs/plans/2026-05-28-cron-zero-duration-hardening-handoff.md`

## Risks / notes

- Full repository tests were not run because the session targeted a small cron-only hardening increment and the checkout contains unrelated dirty gateway/Codex work. Targeted cron tests passed.
- The existing generic `parse_schedule("0m")` error message is acceptable but could be improved in a later UX cleanup if desired.
- No destructive commands, staging, commit, push, credential changes, deployment, or external messages were performed.

## Next best session

Recommended next low-risk hardening increment: update `skills/software-development/subagent-driven-development/SKILL.md` to add a dirty-tree/workspace hygiene guard and replace example `git add -A` commands with explicit-path staging guidance. Discovery found this is clean, docs-only, and directly reduces autonomous crew risk in dirty workspaces.
