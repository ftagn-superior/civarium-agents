---
name: civarium-epistemic-discipline
description: Use when reasoning about Civarium state, hidden information, command receipts, queued intents, and hypotheses during play.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [civarium, epistemics, hidden-state, game-agent, reasoning]
    related_skills: [civarium-player-loop]
---

# Civarium Epistemic Discipline

## Overview

Civarium agents observe only their visible slice of the world. A strong Civarium player must avoid hallucinating hidden state, future mechanics, other agents' private plans, or state changes that have not been confirmed through visible state.

Use this skill to keep observations, rule facts, hypotheses, intentions, and outcomes separate.

## When to Use

Use this skill when:

- Interpreting `get_visible_state`.
- Deciding whether an entity exists or is merely unobserved.
- Explaining the result of `submit_command`.
- Waiting for round advancement.
- Reporting strategic reasoning to the operator.

## Knowledge Buckets

Classify claims into five buckets:

1. **Observed facts** — returned by current MCP tool calls, especially `get_visible_state` and `get_active_round`.
2. **Rule facts** — returned by runtime rule catalog/specs.
3. **Queued intentions** — valid submitted commands listed by `list_queued_submitted_commands`.
4. **Hypotheses** — plausible but unobserved ideas.
5. **Confirmed outcomes** — world changes visible in a later `get_visible_state` result.

Never promote a hypothesis to an observed fact.

## Hidden State Boundary

A missing entity in visible state means:

```text
not observed by this agent
```

It does not mean:

```text
absent globally
```

Do not infer other agents' resources, structures, commands, map positions, or plans unless they appear in visible state or exposed tools.

## Receipt Semantics

A `submit_command` receipt means:

- backend received the intent;
- backend validated it;
- `is_valid=true` means it may be queued;
- `is_valid=false` means it is not queued.

A receipt does not mean the world changed.

A queued command means:

- the command was admitted for later execution;
- it can affect the world when the round advances;
- it is still not proof of a world change.

A later visible state snapshot means:

- the authenticated agent can observe that resulting state;
- only then may the agent call the change confirmed.

## Reporting Template

Use this format when useful:

```text
Наблюдаемые факты:
- ...

Факты правил:
- ...

Гипотезы:
- ...

Намерение/действие:
- ...

Подтверждение:
- receipt/queued/visible-state result
```

Keep it compact; not every report needs all sections.

## Common Pitfalls

1. **"I don't see X" -> "X doesn't exist".** Wrong. It may be hidden.
2. **"Command accepted" -> "building exists".** Wrong. Need round advancement and visible state.
3. **Assuming future design direction is implemented.** Long-term Civarium may include diplomacy/economy/combat, but current play uses only exposed mechanics.
4. **Using codebase/admin knowledge as player knowledge.** During play, act through MCP tools and visible state.

## Verification Checklist

- [ ] Every factual claim is backed by a tool result, rule spec, or explicit provided context.
- [ ] Hypotheses are labeled as hypotheses.
- [ ] Missing visible entities are described as unobserved, not globally absent.
- [ ] Receipts and queued commands are not described as world changes.
- [ ] Outcomes are confirmed through later visible state.
