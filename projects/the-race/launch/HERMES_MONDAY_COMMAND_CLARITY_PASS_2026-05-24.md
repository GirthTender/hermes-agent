# Hermes — Monday Command Clarity Pass

## 1. Sources read
- `/Users/girthtender/.hermes/hermes-agent/docs/plans/2026-05-24-three-hour-launch-prep-block.md`
- `/Users/girthtender/.hermes/hermes-agent/website/docs/reference/cli-commands.md`
- `/Users/girthtender/.hermes/hermes-agent/website/docs/reference/faq.md`

## 2. Current verdict: REVISE
- The gateway command guidance is clearer now, but this pass is still a repo-safe draft/checklist rather than a completed operational change.
- The assigned project-specific launch files were not present in the repo yet, so the evidence is documentation-level only.

## 3. Top risks
- `hermes gateway run` vs `hermes gateway start` can still be misread without the surrounding docs.
- `--all` scope could be over-applied if the reader assumes it only affects the active profile.
- Launchd PATH issues remain a hidden failure mode on macOS if someone treats service startup like a plain shell command.

## 4. Work completed
- Read the launch-prep block plan to confirm the lane assignment and repo-safe constraints.
- Read the gateway reference section and verified the quick decision guidance is present.
- Read the FAQ section covering launchd PATH capture and the `install` / `start` sequence.
- Confirmed the docs already distinguish:
  - foreground `run`
  - installed-service `start`
  - multi-profile `restart --all`

## 5. Missing evidence
- MISSING: an in-repo project file under `projects/the-race/launch/` before this draft pass.
- MISSING: any concrete Monday launch checklist owned by the project itself.
- MISSING: any live runtime validation, which is out of scope here anyway.
- MISSING: proof that every downstream doc or note now points to the same wording.

## 6. Next safe internal actions
- Keep any follow-up limited to repo-local documentation and planning.
- If another source-of-truth note exists, compare its wording against the gateway reference.
- If a duplicate launch note appears, align it to the same run/start/restart distinction.
- Draft a tighter wording pass only if it stays purely internal and textual.

## 7. Exact Haz approvals needed before any external/live/account/payment/domain/provider/runtime step
- Haz approval is required for any:
  - external send or public link
  - account edit
  - payment action
  - domain / DNS / mailbox change
  - provider / auth / model change
  - push / merge / deploy
  - restart / smoke run / other runtime step
- Approval should name the exact target, the exact change, and the scope.

## 8. Gated actions taken: none
