# Autonomous 40-Task Live Tracker — 2026-05-29 11:13 AEST

## Scope

Continue autonomously in `/Users/girthtender/.hermes/hermes-agent` on branch `pr-27648-web-model-area-clean`.

Hard boundaries:

- No live/public/messaging/account/payment/deployment actions.
- No `git add -A`, stash, reset, clean, or broad staging.
- Preserve pre-existing dirty work unless the task specifically validates it.
- Prefer repo-safe audit, tests, tiny patches, documentation parity, and handoff evidence.

## Forty selected next tasks

1. Preflight current Hermes repo branch, dirty tree, and exclusion boundaries.
2. Inventory recent handoffs for safe next increments.
3. Pick 40 autonomous next tasks with explicit no-live-side-effects boundaries.
4. Create live 40-task session tracker artifact.
5. Run targeted baseline checks for currently dirty subsystems.
6. Inspect cron delivery hardening residual diagnostic TODO.
7. Add/verify operator diagnostic for rejected cron delivery targets if safe.
8. Run cron scheduler focused tests.
9. Inspect gateway slash-access dirty diff for consistency.
10. Run slash access focused tests.
11. Inspect URL safety dirty diff for regression scope.
12. Run URL safety focused tests.
13. Inspect codex runtime/adapter dirty diff for validation scope.
14. Run codex-related focused tests if discoverable.
15. Inspect conversation loop dirty diff for validation scope.
16. Run conversation-loop focused tests if discoverable.
17. Inspect kanban worker skill/doc dirty diff for parity.
18. Run kanban worker tool-surface tests.
19. Check bundled skill docs parity for modified skills.
20. Search modified docs for placeholder/TODO drift.
21. Run diff whitespace check over owned dirty files.
22. Create safe next-increment shortlist from audit.
23. Implement smallest safe code/doc patch from shortlist.
24. Add or adjust regression test for patch.
25. Run targeted test for patch.
26. Run spec compliance review gate.
27. Run quality/safety review gate.
28. Patch any review gaps.
29. Re-run affected tests after review fixes.
30. Re-run whitespace check after fixes.
31. Read back session tracker artifact.
32. Write final autonomous 40-task handoff artifact.
33. Verify handoff exists on disk.
34. Capture final git status with owned/excluded files.
35. Record commands and results in handoff.
36. Mark completed/blocked/deferred tasks accurately.
37. Identify next safest private action for Haz or crew.
38. Avoid live outreach/messaging/public/account/payment actions.
39. Preserve unrelated dirty files; no stash/reset/clean/broad add.
40. Deliver concise PASS/PARTIAL with evidence.

## Preflight snapshot

- Branch: `pr-27648-web-model-area-clean`.
- Dirty tree: existing Hermes/Crew ops hardening files across codex runtime, cron, gateway slash access, kanban skills/docs, URL safety, and tests.
- Untracked handoff/todo artifacts under `docs/plans/` and `.hermes/` exist before this tracker.

## Live notes

- This file is session-owned.
- Final handoff will record actual completed/deferred counts and verification command results.
