# Civarium Obsidian Strategic Memory

Этот документ описывает, как Civarium-агент может самостоятельно планировать долгосрочную стратегию и вести историю кампании в Obsidian.

## Цель

Сделать агента не только реактивным исполнителем ходов, а стратегическим игроком, который:

1. анализирует текущую обстановку;
2. создает долгосрочный план, если его нет;
3. уточняет стратегию по ходу раундов;
4. удаляет/архивирует устаревшие цели;
5. перестраивает стратегию при явных trigger-событиях;
6. обращается к актуальной стратегии перед решениями;
7. ведет историю событий и угроз.

## Роль Obsidian

Obsidian — внешняя долговременная память кампании.

Он хранит:

- активную стратегию;
- текущую ситуацию;
- цели;
- decision rules;
- trigger rules;
- хронологию раундов;
- значимые события;
- угрозы и историю hostile interactions;
- заметки об известных агентах/фракциях.

Obsidian не должен хранить:

- secrets;
- полный raw MCP output каждый ход;
- raw chain-of-thought;
- скрытые догадки как факты.

## Базовый цикл с Obsidian

```text
0. Catalog cache: если статичный rule catalog еще не получен в этой игре/сессии — получить и закешировать
1. MCP: get_active_round
2. MCP: get_visible_state
3. Obsidian: read Current Strategy.md
4. Obsidian: read Current Situation.md
5. Optional search: Threats.md, Events.md, Actors/*
6. Strategy check: keep / update / rebuild
7. Catalog/spec lookup: использовать cached command list для вариантов; получить full command spec для выбранного действия
8. MCP: submit command
9. MCP: verify queued command
10. After round change: observe visible state
11. Obsidian: update situation + append logs + update goals/threats
```

## Strategy Lifecycle

### Create

Create strategy when:

- no `Current Strategy.md` exists;
- the strategy note is empty;
- strategy status is `missing`, `obsolete`, or `archived`;
- cached rule catalog/spec facts make the old plan irrelevant.

### Update

Update strategy when:

- a goal is completed;
- a construction completes;
- a command is rejected but the plan remains viable;
- visible state changes in a way that affects priorities;
- a command spec or validation result adds a small compatible constraint.

### Rebuild

Rebuild strategy when:

- new major mechanics appear;
- core action becomes invalid;
- hostile action / damage / sabotage is visible;
- another agent becomes visible;
- current plan fails repeatedly;
- resources/costs/upkeep/combat/diplomacy appear;
- operator changes doctrine.

## Note Granularity

Prefer small notes over one giant note:

- Current Strategy: active plan only.
- Current Situation: compact snapshot.
- Round Log: chronological short records.
- Events: meaningful events indexed by round/type.
- Threats: risk memory and precautions.
- Actors: one note per known agent/faction when identifiable.
- Plans: named/dated strategy versions.

## Threat Memory Example

If another agent attacks or harms us, do not only mention it in chat. Record it:

```md
### Round 42 — Attack on Outpost

- observed fact: visible state showed loss of `Outpost`
- suspected actor: Agent X
- confidence: medium
- evidence: event/state attribution if visible
- impact: lost frontier structure
- response: strategy rebuilt toward defense/scouting
- future precaution: treat Agent X as risky until contradicted
```

If attribution is not visible, write `suspected actor: unknown`, not a false certainty.

## Decision Use

Before major decisions, the agent should ask:

1. What does visible state say?
2. What does the cached runtime catalog / selected command spec allow?
3. What does Current Strategy recommend?
4. Did any Trigger Rule fire?
5. Do Threats/Actors notes change the risk of this action?
6. Should this be normal execution, minor update, or full rebuild?

## Implementation Files

- Skills:
  - `skills/civarium-strategic-planning/SKILL.md`
  - `skills/civarium-obsidian-campaign-log/SKILL.md`
- Templates:
  - `obsidian-templates/Civarium/*`
- Profile templates:
  - `hermes-profile/SOUL.md`
  - `hermes-profile/memories/MEMORY.md`
  - `hermes-profile/memories/USER.md`
