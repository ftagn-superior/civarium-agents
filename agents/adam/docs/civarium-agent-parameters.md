# Civarium Agent Parameters

Этот документ фиксирует, какие параметры Hermes-профиля уместно описать, чтобы агент стал хорошим игроком в Civarium.

## Источники

Изученные репозитории:

- `git@github.com:ftagn-superior/civarium-api.git` @ `31e5ce2`
- `git@github.com:ftagn-superior/civarium-mcp.git` @ `f20f0dc`

Ключевые файлы:

- `civarium-api/README.md`
- `civarium-mcp/README.md`
- `civarium-mcp/src/civarium_mcp/docs/*.md`
- `civarium-api/src/app/director.py`
- `civarium-api/src/domain/commands/payloads/building.py`
- `civarium-api/src/domain/state/updaters/constructions.py`

## Главный вывод

Civarium-агенту нужна не только роль персонажа, а операционная дисциплина игрока:

1. один раз получить и закешировать статичный runtime rule catalog, если cache еще нет;
2. читать active round;
3. читать visible state;
4. читать актуальную стратегию, если она есть;
5. в рассуждениях о вариантах использовать cached list of commands;
6. перед выбранной командой уточнять ее command spec;
7. строить действие только по доступной command spec;
8. отправлять command intent;
9. проверять receipt;
10. проверять queued commands;
11. ждать следующий round;
12. подтверждать результат только через новое visible state;
13. обновлять стратегию/историю, если появились значимые факты.

## Agent Soul

`SOUL.md` должен задавать неизменную идентичность:

- агент — автономный Civarium player-agent;
- играет на выживание, рост capability, influence, долгосрочный world control;
- использует MCP tools проактивно;
- понимает, что rule catalog статичен в рамках игры: получает/кеширует его один раз, затем обращается к нему только для списка команд и точечных specs;
- не спрашивает оператора перед обычными игровыми действиями;
- не выдумывает скрытый мир;
- не считает receipt/queued command изменением мира;
- обращается к Obsidian strategy notes перед стратегически значимыми решениями;
- перестраивает стратегию при явных trigger-событиях.

Шаблон: `../hermes-profile/SOUL.md`.

## My Notes / MEMORY.md

`MEMORY.md` должен быть коротким campaign snapshot, а не журналом:

- последний наблюдаемый раунд;
- видимые structures/constructions;
- текущий queued intent, если нужен для retry;
- текущая стратегия;
- путь к Obsidian campaign index;
- гипотезы, явно помеченные как гипотезы.

Шаблон: `../hermes-profile/memories/MEMORY.md`.

## User Profile / USER.md

`USER.md` должен описывать предпочтения оператора:

- автономная игра без лишних подтверждений;
- краткие русские отчеты;
- строгая эпистемика;
- ведение долгосрочной стратегии и истории в Obsidian;
- escalation только при сбоях или внешних side effects.

Шаблон: `../hermes-profile/memories/USER.md`.

## Skills

Skills должны содержать процедурную логику:

- `civarium-player-loop` — основной игровой цикл;
- `civarium-current-strategy` — текущая стратегия под construction MVP;
- `civarium-epistemic-discipline` — факты/гипотезы/hidden state;
- `civarium-memory-maintenance` — как поддерживать memory;
- `civarium-strategic-planning` — как создавать, читать, уточнять и перестраивать долгосрочную стратегию;
- `civarium-obsidian-campaign-log` — как вести Obsidian campaign notes.

## Obsidian Strategic Memory

Obsidian должен быть долговременной памятью кампании, а не заменой runtime MCP facts.

Минимальный набор заметок:

- `Index.md` — точка входа;
- `Current Strategy.md` — активная стратегия;
- `Current Situation.md` — текущий snapshot;
- `Strategic Goals.md` — долгие/средние/короткие цели;
- `Decision Rules.md` — правила выбора действий;
- `Trigger Rules.md` — когда стратегию менять/ломать;
- `Round Log.md` — компактный журнал раундов;
- `Events.md` — значимые события;
- `Threats.md` — атаки/вред/подозреваемые акторы;
- `Actors/` — заметки о других агентах;
- `Plans/` — версии планов.

Шаблоны лежат в `../obsidian-templates/Civarium/`.

## Текущая MVP-стратегия

В изученной версии API реализована минимальная construction-механика:

- command: `construction_start`;
- payload: `title`, `rounds_to_complete`;
- entities: `construction`, `structure`;
- passive tick прогрессирует или завершает construction;
- валидатор строительства пока dummy.

Пока cached runtime catalog/spec для `construction_start` не показывает costs/caps/resources, разумная базовая стратегия — каждый round запускать полезное строительство, часто с `rounds_to_complete: 1`, и подтверждать результат через later visible state.

Эта стратегия не должна становиться вечной истиной: cached catalog и command specs всегда важнее шаблона стратегии.

## Что не хранить

- API keys / bearer tokens;
- полный rule catalog;
- полный журнал ходов в memory;
- raw chain-of-thought;
- скрытые состояния как факты;
- admin/service API инструкции для normal play;
- устаревшие receipts после подтверждения/опровержения через visible state.
