---
type: civarium-trigger-rules
status: active
last_updated: unknown
---

# Trigger Rules

## Full Strategy Rebuild

Rebuild the strategy if any of these occur:

1. Cached catalog contains command types not covered by current strategy.
2. Cached catalog contains entity types not covered by current strategy.
3. Cached catalog contains event types not covered by current strategy.
4. A core command becomes invalid by spec or validation.
5. Visible state shows hostile action.
6. Visible state shows loss/damage/sabotage/attack/resource shock.
7. Another agent or faction becomes visible.
8. Repeated actions stop producing progress.
9. The plan depends on a mechanic not exposed by catalog.
10. Operator changes doctrine.
11. Costs, scarcity, territory, combat, diplomacy, scouting, upkeep, or victory mechanics appear.

## Minor Strategy Update

Update without full rebuild if:

- a construction completes;
- a new structure appears;
- a queued command is accepted;
- a command is rejected but easy to correct;
- a short-term goal is completed;
- visible state changes without invalidating the strategic thesis.

## No Strategy Change

Keep strategy if:

- cached catalog/spec assumptions still match the active strategy;
- visible state changed as expected;
- no threats appeared;
- current short-term action remains valid.
