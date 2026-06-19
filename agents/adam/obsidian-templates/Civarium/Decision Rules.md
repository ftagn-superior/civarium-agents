---
type: civarium-decision-rules
status: active
last_updated: unknown
---

# Decision Rules

## Priority Order

1. Obey the cached static runtime rule catalog and selected command specs.
2. Act only from visible state and explicit rule facts.
3. Follow Current Strategy if still valid.
4. Prefer actions that increase future optionality.
5. Record meaningful decisions and outcomes.

## Action Selection

When choosing an action:

1. Is the command type registered?
2. Does payload match command spec?
3. Does visible state suggest the action is useful?
4. Does Current Strategy recommend this action class?
5. Did any Trigger Rule require strategy rebuild first?
6. Are there active threats requiring defensive posture?

## If Only Construction Exists

- Prefer useful 1-round construction unless validators/costs/caps say otherwise.
- Do not assume structure title effects.
- Diversify titles for future narrative/strategic interpretation.

## If No Valid Action Exists

- Record blocker.
- Update Current Situation.
- Do not fabricate unavailable mechanics.
- Wait, skip, or report `blocked` with the visible-state/rule reason.
- Escalate to operator only if blocked by MCP/API/configuration failure, missing credentials, or ambiguous external side effects.
