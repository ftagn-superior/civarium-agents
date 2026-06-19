---
type: civarium-current-strategy
status: active
strategy_version: 1
last_reviewed_round: unknown
last_updated: unknown
---

# Current Strategy

## Strategic Thesis

Пока cached Civarium catalog/specs expose only construction mechanics, maximize compounding infrastructure by building useful 1-round structures every round unless command validation or specific specs show constraints.

## Long-Term Goal

Build a durable power base capable of adapting when economy, diplomacy, scouting, combat, influence, logistics, or territory mechanics appear.

## Mid-Term Goals

1. Establish basic infrastructure.
2. Diversify structure titles to prepare for future mechanics without assuming title effects.
3. Use the cached rule catalog when reasoning about available command alternatives.
4. Maintain strict visible-state-only reasoning.
5. Record meaningful events, threats, and strategy changes.

## Short-Term Goals

1. Check active round.
2. Check visible state.
3. Inspect the relevant command spec if it is not cached or if payload details are uncertain.
4. If no better command exists, submit `construction_start`.
5. Confirm queued command.
6. Observe result next round.

## Current Priorities

1. Growth
2. Rule discovery
3. Memory hygiene
4. Risk monitoring

## Known Constraints

- Commands are intents, not immediate world changes.
- Visible state is partial.
- Cached runtime catalog and selected command specs are source of rule truth.
- Current construction titles may have no mechanical effect.
- Hidden state and other agents are unknown unless visible.

## Rebuild Triggers

Rebuild this strategy if:

- cached catalog contains command/entity/event mechanics not covered by this strategy;
- `construction_start` becomes invalid or constrained by spec/validation;
- visible state shows damage, loss, hostile action, attack, sabotage, or resource shock;
- another agent becomes visible;
- current goals are impossible or unproductive for 2+ rounds;
- new mechanics introduce costs, scarcity, territory, combat, diplomacy, scouting, upkeep, or victory conditions;
- operator changes doctrine.

## Next Action Policy

If cached rule catalog/specs support only construction and no blockers are visible, choose a useful structure title and submit a valid `construction_start` command for the active round.
