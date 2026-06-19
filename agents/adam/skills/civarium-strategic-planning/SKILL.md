---
name: civarium-strategic-planning
description: Use when a Civarium player-agent needs to create, consult, update, or rebuild long-term strategy from current rules, visible state, and campaign memory.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [civarium, strategy, planning, long-term-memory, game-agent]
    related_skills: [civarium-player-loop, civarium-epistemic-discipline, civarium-obsidian-campaign-log]
---

# Civarium Strategic Planning

## Overview

This skill teaches a Civarium player-agent to maintain a living strategy rather than choosing each round in isolation. The strategy must be grounded in the cached static runtime rule catalog, selected command specs, visible state, and durable campaign memory.

The agent should create a strategy if none exists, consult it before important decisions, update it as facts change, and rebuild it when explicit triggers show the old strategy is broken.

## When to Use

Use this skill when:

- starting or resuming a Civarium campaign;
- deciding what to do in a round;
- no long-term plan exists;
- the active strategy may be stale;
- visible state changed or cached rule/spec facts need to be applied;
- hostile action, damage, another agent, or new mechanics appear;
- the operator asks for autonomous strategic play.

Do not use this to override the cached runtime rule catalog or selected command specs. Strategy is guidance; exposed rules and visible state are facts.

## Strategic Inputs

Before creating or revising strategy, gather:

1. Cached static runtime rule catalog. If missing, fetch it once; do not reread it every turn.
2. Relevant command/entity/event specs for the action being considered.
3. Active round.
4. Visible state.
5. Current strategy note if available.
6. Current situation note if available.
7. Threats / actors / event history if relevant.

## Planning Horizons

Maintain goals at three horizons:

### Long Horizon

The broad campaign direction, e.g. durable power base, world influence, survival, eventual control.

### Mid Horizon

Multi-round priorities, e.g. infrastructure growth, defense posture, scouting, resource stabilization, diplomacy.

### Short Horizon

Immediate next actions, e.g. submit a valid command this round, verify queue, observe next state.

## Strategy Lifecycle

### 1. Create Strategy

Create a strategy when:

- no strategy note exists;
- note exists but has no active thesis;
- strategy status is `missing`, `obsolete`, or `archived`;
- cached rule/spec facts make old assumptions invalid.

A new strategy should include:

- strategic thesis;
- long/mid/short goals;
- current priorities;
- known constraints;
- trigger rules;
- next action policy.

### 2. Consult Strategy

Before major actions, compare:

- current visible facts;
- current rule facts;
- active strategy thesis;
- threats/actor memory;
- current short-term goals.

Then classify the strategy status:

- `keep`: still valid, execute it;
- `minor_update`: still valid but needs goal/situation edits;
- `rebuild`: contradicted or broken;
- `blocked`: no valid action under current rules/state.

### 3. Update Strategy

Use a minor update when:

- a goal completes;
- construction completes;
- a command is accepted/rejected but core plan remains viable;
- priorities shift slightly;
- a new fact should be reflected in current situation.

When updating, archive stale goals with reason instead of deleting them silently.

### 4. Rebuild Strategy

Use a full rebuild when a trigger fires. Preserve historical strategy in `Plans/` or `Archive/`, then write a new active thesis.

## Rebuild Triggers

Rebuild the strategy if any of these are rule-confirmed or visible-state-confirmed:

1. Cached catalog contains command types not covered by current strategy.
2. Cached catalog contains entity types not covered by current strategy.
3. Cached catalog contains event types not covered by current strategy.
4. A core command becomes invalid or constrained by spec/validation.
5. Visible state shows hostile action.
6. Visible state shows damage, loss, sabotage, attack, or resource shock.
7. Another agent/faction becomes visible.
8. Current goals are impossible or unproductive for multiple rounds.
9. Cached specs expose costs, scarcity, territory, combat, diplomacy, scouting, upkeep, or victory conditions not reflected in the strategy.
10. Operator changes doctrine.

## Decision Algorithm

Use this high-level algorithm:

```text
ensure cached rules exist + observe round + visible state
read current strategy + situation
if no strategy:
    create strategy
else if rebuild trigger fired:
    archive old plan and rebuild
else if minor facts changed:
    update current situation/goals
choose action according to current strategy and available command specs
submit command
verify receipt and queued command
after round change, observe result and update notes
```

## Current MVP Strategy Default

If the cached runtime catalog exposes only construction-focused mechanics, use a growth-first default:

- build useful structures continuously;
- prefer 1-round construction when no costs/caps exist;
- diversify titles without assuming title mechanics;
- use the cached command list when considering alternatives and fetch full specs only for concrete command candidates.

This is a default, not a permanent truth.

## Strategy Report Format

When reporting to the operator:

```text
Стратегия: kept / updated / rebuilt / blocked
Причина: <catalog/visible-state/trigger fact>
Действие: <command or no-op>
Проверка: <receipt/queue/state>
Следующее: <next strategic check>
```

## Common Pitfalls

1. **Long-term plan ignores current rules.** Cached runtime catalog and command specs win.
2. **Plan overfits current MVP.** Construction-only strategy must be revisited when mechanics expand.
3. **Deleting old goals without trace.** Archive or mark obsolete with reason.
4. **Treating suspicion as certainty.** Threats can be hypotheses unless visible state proves attribution.
5. **Reading entire history every round.** Use current strategy/situation first; search history only when relevant.

## Verification Checklist

- [ ] Static rule catalog is available from cache, or was fetched only because the cache was missing/list lookup was needed.
- [ ] Visible state was checked.
- [ ] Active strategy was read or created.
- [ ] Rebuild triggers were evaluated.
- [ ] Action follows both strategy and current command specs.
- [ ] Strategy/situation notes were updated after meaningful changes.
- [ ] Historical claims remain separated into facts vs hypotheses.
