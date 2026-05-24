# Nezha — Protocol Desk First 10 Risk Pass

## 1. Sources read
- `/Users/girthtender/.hermes/hermes-agent/docs/plans/2026-05-24-three-hour-launch-prep-block.md`
- `/Users/girthtender/.hermes/hermes-agent/website/docs/reference/cli-commands.md`
- `/Users/girthtender/.hermes/hermes-agent/website/docs/reference/faq.md`

## 2. Current verdict: REVISE
- This is a repo-safe internal risk draft, not a finished gate decision.
- The named Protocol Desk / Railglass files were not found in the repo during this pass, so the output is necessarily evidence-light.

## 3. Top risks
- No-link approval queue could accidentally become a live/share action if someone treats it as a sending step.
- Risk-gate language can drift into policy without a concrete repo artifact to anchor it.
- Any move from prep-only into public, platform, or account touchpoints would cross the boundary.

## 4. Work completed
- Read the launch-prep block and confirmed the assigned Nezha lane.
- Read the gateway reference to confirm the current command semantics are already documented.
- Read the FAQ material that explains installed-service behavior and PATH capture on macOS.
- Captured the current state as a checklist instead of assuming a stronger verdict than the evidence supports.

## 5. Missing evidence
- MISSING: a repo file named for Protocol Desk or Railglass.
- MISSING: an internal no-link approval queue file to inspect.
- MISSING: a concrete first-10 risk register tied to this repo path.
- MISSING: any proof that the lane has been narrowed to repo-local text only.

## 6. Next safe internal actions
- Keep the lane as a text-only risk pass.
- If a Protocol Desk or Railglass note appears later, read it and compare it against the current draft.
- Turn the top risks into a simple checklist only if the repo already contains a matching internal source.
- Stay inside planning docs and avoid any live or external step.

## 7. Exact Haz approvals needed before any external/live/account/payment/domain/provider/runtime step
- Haz approval is required before any external/live/account/payment/domain/provider/runtime action.
- Exact approvals needed:
  - send anything externally
  - publish or post a link
  - edit an account
  - move money or initiate payment
  - change domain/DNS/mailbox settings
  - change provider, auth, or model settings
  - push, merge, deploy, restart, or run smoke checks
- The approval must identify the target, the action, and the intended scope.

## 8. Gated actions taken: none
