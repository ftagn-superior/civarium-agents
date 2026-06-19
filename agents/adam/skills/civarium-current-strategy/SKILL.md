---
name: civarium-current-strategy
description: Use when choosing practical Civarium actions under the current construction-focused MVP mechanics exposed by the runtime rule catalog.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [civarium, strategy, construction, mvp, game-agent]
    related_skills: [civarium-player-loop, civarium-epistemic-discipline]
---

# Civarium Current Strategy

## Overview

This skill captures the practical strategy for the current Civarium implementation observed in the local repositories. It is intentionally subordinate to the cached runtime rule catalog and selected command specs. The catalog is static during a game, so do not re-read it every turn; re-evaluate when cached specs or command validation contradict this skill.

Current known MVP mechanics are construction-focused: agents can start constructions, passive ticks progress them, and completed constructions become structures visible to their owner.

## When to Use

Use this skill when:

- The runtime catalog exposes `construction_start`.
- The visible state contains `construction` and/or `structure` libraries.
- The agent needs to choose a useful action while the game surface is still minimal.

Do not use this as a permanent strategy if the cached catalog/specs expose richer mechanics such as resources, costs, combat, diplomacy, movement, scouting, upkeep, or victory conditions. In that case, inspect the relevant specs and adapt.

## Verify From Cache and Specs

Before using this strategy:

1. Ensure the static rule catalog is available from cache; if missing, call `get_civarium_rule_catalog` once.
2. Confirm from the cached command list that `construction_start` is an available command type.
3. Call `get_civarium_command_spec("construction_start")` only if the spec is not already cached or payload details are uncertain.
4. Confirm the payload schema fields and validators.
5. Call `get_visible_state` and inspect current `construction` / `structure` entities.

## Current Known MVP Surface

If the cached catalog exposes only:

- command: `construction_start`
- entities: `construction`, `structure`
- events: `construction_started`, `construction_progress`, `construction_completed`, `structure_created`

then the best baseline is active development: keep creating useful structures while no exposed costs, caps, or tradeoffs exist.

## Baseline Policy

- Submit a `construction_start` command each available round when no better mechanic exists.
- Prefer `rounds_to_complete: 1` unless the current schema/validators expose costs, minimum duration, caps, or strategic reasons for longer construction.
- Use structure titles that encode strategic intent.
- After the next round, verify whether the construction progressed or a structure appeared in visible state.

## Suggested Structure Names

Use names that create a plausible strategic foundation without assuming hidden mechanics:

- `Workshop`
- `Archive`
- `Signal Tower`
- `Logistics Hub`
- `Foundry`
- `Observatory`
- `Planning Hall`
- `Storehouse`
- `Command Post`
- `Research Annex`

These are titles only unless the cached rule catalog/specs give them mechanical effects. Do not claim that a `Foundry` produces metal or a `Signal Tower` scouts unless mechanics expose that.

## Payload Pattern

For the current command schema:

```json
{
  "title": "Workshop",
  "rounds_to_complete": 1
}
```

Use a fresh `client_command_id` UUID for each new intent.

## Strategic Heuristic

If existing visible structures are empty:

1. Build `Workshop`.
2. Then build `Archive` or `Planning Hall`.
3. Then build `Signal Tower` or `Logistics Hub`.

If a construction is already visible:

- Still consider starting another construction if the current validators expose no cap and accepting multiple constructions is allowed by receipts.
- If a command is rejected, treat checks as the new strategic constraint and adapt.

## Common Pitfalls

1. **Assuming title mechanics.** Titles are just strings until rules say otherwise.
2. **Forgetting passive tick timing.** Command creates construction on round advancement; passive environment can then progress/complete constructions. Confirm through later visible state.
3. **Treating this skill as source of truth.** Cached runtime catalog and command specs win.
4. **Over-optimizing nonexistent constraints.** If no costs/caps/resources exist, do not invent them.

## Verification Checklist

- [ ] Cached catalog exposes `construction_start`.
- [ ] Command spec expects `title` and `rounds_to_complete` or the payload was adapted to current schema.
- [ ] Visible state was checked before action.
- [ ] Command receipt was valid.
- [ ] Queued commands were checked.
- [ ] Later visible state confirmed the result.
