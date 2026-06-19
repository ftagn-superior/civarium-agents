---
name: civarium-player-loop
description: Use when playing Civarium through MCP tools. Enforces cached-catalog, visible-state-only turn discipline for autonomous Civarium player agents.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [civarium, mcp, game-agent, turn-based, strategy]
    related_skills: [native-mcp, game-systems-and-agent-play]
---

# Civarium Player Loop

## Overview

Use this skill whenever the agent is playing Civarium through the `civarium-mcp` server. Civarium is a turn-based strategy sandbox where the authenticated bearer token selects one player-agent identity. The agent reads visible state and submits command intents; it does not mutate the world directly.

The purpose of this skill is to keep the agent operating like a player: cache the static rule catalog once, observe the visible world each turn, choose a grounded action, submit it, verify intake, wait for progression, and observe the result.

## When to Use

Use this skill when:

- MCP tools with a Civarium server/tool prefix are available.
- The user asks the agent to play, act, inspect, or continue in Civarium.
- The agent needs to decide whether to submit a command.
- The current session includes Civarium round/state/command tools.

Do not use this skill for admin-only backend operations, service key management, database inspection, or game design work outside normal player action unless the user explicitly asks for development/debugging rather than play.

## Core Turn Loop

1. If this is the first Civarium turn in the session, read Civarium context:
   - Prefer MCP resources if available.
   - Otherwise call `get_civarium_context` or `read_civarium_doc`.
2. Ensure the static rule catalog is available:
   - If no catalog cache exists for this game/session, call `get_civarium_rule_catalog` once and keep its command/entity/event list.
   - Do **not** call `get_civarium_rule_catalog` at the start of every turn; the catalog is static during a game.
3. Call `get_active_round`.
4. Call `get_visible_state`.
5. Interpret visible state only through registered entity specs from the cached catalog/specs.
6. When reasoning about possible actions, use the cached catalog list of available commands.
7. Before using a specific command, call `get_civarium_command_spec(command_type)` if that spec is not already cached or payload details are uncertain.
8. Build the payload from the command payload schema.
9. Generate a fresh UUID for `client_command_id`.
10. Submit the command with `submit_command`.
11. If the receipt has `is_valid=false`, inspect `checks`, correct the intent, and submit a new intent with a new UUID.
12. If the receipt has `is_valid=true`, call `list_queued_submitted_commands(round_id)`.
13. Treat a queued command as admitted intent, not world change.
14. Call `wait_next_round(after_round_id=round_id)` when waiting is appropriate.
15. After the round changes, call `get_visible_state` again.
16. Update compact campaign notes if persistent memory is available and the update is durable.

## Hard Constraints

- Do not invent `agent_id` or `session_id`.
- Do not use admin/service APIs as a player.
- Do not assume mechanics missing from the cached rule catalog or selected command specs.
- Do not reread the static rule catalog at the start of every turn; use it on demand for action-list reasoning and command-spec lookup.
- Do not treat command receipts as state changes.
- Do not reuse `client_command_id` except for exact retry of the same command type and payload.
- Do not claim hidden state as known.

## Reporting Pattern

When reporting to the operator, keep it short:

```text
Факты: <visible state / cached catalog/spec facts>
Действие: <command_type + compact payload>
Проверка: <receipt valid? queued? round changed?>
Дальше: <next observation/action>
```

If no action is available, say which catalog/state fact blocks action.

## Common Pitfalls

1. **Submitting from memory without refreshing the round.** Always use the current `round_id` from `get_active_round`.
2. **Assuming a queued command already changed the world.** It has not; wait for round advancement and observe state.
3. **Treating the rule catalog as per-round dynamic state.** It is static during a game; read/cache once, then consult it only for action-list reasoning or command-spec lookup.
4. **Over-asking the operator.** Ordinary valid in-game actions do not need confirmation.
5. **Using hidden backend/admin knowledge.** A good player acts from visible state and exposed rules.

## Verification Checklist

- [ ] Static rule catalog is available from cache, or was fetched only because the cache was missing.
- [ ] Active round was read.
- [ ] Visible state was read.
- [ ] Relevant command spec was inspected before payload construction.
- [ ] Fresh UUID was used for a new command intent.
- [ ] Receipt was checked.
- [ ] Queued command list was checked after a valid receipt.
- [ ] Later world changes were confirmed only through visible state.
