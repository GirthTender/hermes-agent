# Three-Hour Launch Prep Block

**Mode:** repo-safe only

## Guardrails

No sends, public/customer/supplier/platform contact, public links, account edits, payments, domains/DNS/mailbox changes, provider/auth/model changes, pushes, merges, deploys, restarts, smoke runs, secrets, private records, or live claims.

If any live/public/account/payment/domain/provider/runtime edge appears, stop and report:

**HELD FOR HAZ** — include the exact approval needed.

## Assigned lanes

### Hermes
- Source-of-truth hygiene.
- Monday launch command clarity.

### Nezha
- Protocol Desk / Railglass risk gate.
- No-link approval queue.

### Flores
- Yardlantern / entreepwner visual-email prep.
- Workers-rights synthesis, prep-only.

## Current evidence gathered

- Repo branch is on `pr-27648-web-model-area-clean`.
- Current workspace had one untracked file before the prior push: `docs/plans/2026-05-20-rollout-confirmation-note.md`.
- Relevant docs live under `docs/plans/` and `website/docs/reference/`.
- Gateway launch command semantics are already documented in `website/docs/reference/cli-commands.md`:
  - `hermes gateway run` = foreground
  - `hermes gateway start` = installed service
  - `hermes gateway restart` / `--all` have explicit profile scope

## Checkpoint packet format

Return packets at roughly 60, 120, and 180 minutes using this structure:

```text
OWNER:
STATUS: DONE / BLOCKED / HELD FOR HAZ / NO ACTION
FILES:
EVIDENCE:
NEXT:
GATED ACTIONS TAKEN: none
```

## Packet 0 — start state

OWNER: Hermes / Nezha / Flores
STATUS: NO ACTION
FILES:
- `docs/plans/2026-05-24-three-hour-launch-prep-block.md`
EVIDENCE:
- Guardrails recorded above.
- Existing launch-command docs identified in `website/docs/reference/cli-commands.md`.
NEXT:
- Keep working inside repo-safe bounds.
GATED ACTIONS TAKEN: none
