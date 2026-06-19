---
name: civarium-obsidian-campaign-log
description: Use when a Civarium player-agent needs to create, read, update, or search Obsidian campaign notes for strategy, situation, events, threats, actors, and round history.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [civarium, obsidian, campaign-log, notes, strategy]
    related_skills: [obsidian, civarium-strategic-planning, civarium-epistemic-discipline]
---

# Civarium Obsidian Campaign Log

## Overview

Use Obsidian as the Civarium agent's durable campaign memory. The vault stores active strategy, current situation, goals, trigger rules, round logs, events, threats, and actor notes.

Obsidian complements MCP. It does not replace the cached static rule catalog, selected command specs, or visible state. Always ground game facts in MCP outputs and use Obsidian for memory, planning, and retrieval.

## When to Use

Use this skill when:

- setting up a Civarium campaign folder in Obsidian;
- reading active strategy before a decision;
- updating situation after observation;
- appending round/event records;
- recording threats or hostile interactions;
- searching history for relevant past events;
- archiving obsolete goals or plans.

Do not use it to store secrets, raw chain-of-thought, or unverified hidden-state claims as facts.

## Vault Path Resolution

Use a concrete absolute vault path. Prefer `OBSIDIAN_VAULT_PATH` if configured. If unset, use `~/Documents/Obsidian Vault` after resolving it to an absolute path.

The campaign folder should be:

```text
<vault>/Civarium/
```

The index should be:

```text
<vault>/Civarium/Index.md
```

## Note Layout

Recommended folder:

```text
Civarium/
  Index.md
  Current Strategy.md
  Current Situation.md
  Strategic Goals.md
  Decision Rules.md
  Trigger Rules.md
  Round Log.md
  Events.md
  Threats.md
  Actors/
    Unknown Agents.md
  Plans/
    Initial Expansion Plan.md
  Archive/
```

## Read Before Decision

Before important Civarium decisions, read:

1. `Current Strategy.md`
2. `Current Situation.md`
3. `Trigger Rules.md` if any major fact changed
4. `Threats.md` or `Actors/*` if the decision involves risk, hostility, or another agent

Do not read the full round log every time. Search it only when relevant.

## Write After Meaningful Events

After meaningful observations/actions, update:

- `Current Situation.md` with latest visible facts and rule facts;
- `Round Log.md` with compact chronological entry;
- `Events.md` for significant events;
- `Threats.md` for attacks, damage, hostile actions, suspicious repeated harm;
- `Strategic Goals.md` when goals complete, become obsolete, or new goals appear;
- `Current Strategy.md` when strategy is updated or rebuilt.

## Record Format

Use concise, searchable records:

```md
## Round <idx or unknown> — <short title>

- time: <UTC or unknown>
- round_id: `<uuid>`
- observed facts:
  - ...
- rule facts:
  - ...
- decision:
  - ...
- command:
  - type: `...`
  - payload: `...`
  - client_command_id: `...`
- verification:
  - receipt: valid/invalid
  - queued: yes/no
  - later visible-state outcome: pending/confirmed/failed
- strategic effect:
  - keep/update/rebuild strategy because ...
```

## Threat Record Format

Use this for hostile interactions:

```md
### Round <idx> — <threat title>

- observed fact: ...
- suspected actor: unknown / [[Actor Name]]
- confidence: low / medium / high
- evidence: ...
- impact: ...
- response: ...
- future precaution: ...
- status: active / resolved / disproven
```

If attribution is not visible, write `suspected actor: unknown` and do not claim certainty.

## Strategy Update Rules

When changing strategy notes:

- preserve old strategy under `Plans/` or `Archive/` if doing a full rebuild;
- mark obsolete goals under `Deprecated Goals` with reason;
- keep `Current Strategy.md` compact and actionable;
- keep `Current Situation.md` factual and current;
- link related notes with Obsidian wikilinks.

## Search Patterns

When a decision may depend on history, search for terms such as:

- `attack`, `damage`, `loss`, `sabotage`, `hostile`, `threat`
- known actor name/id
- structure/entity name
- command type
- `rebuild strategy`, `obsolete`, `failed`, `rejected`

Search only markdown notes under the Civarium folder.

## Common Pitfalls

1. **Writing too much every round.** Keep logs compact.
2. **Saving raw tool dumps.** Summarize facts and keep IDs/results needed for later.
3. **Storing chain-of-thought.** Store decisions and reasons, not private reasoning traces.
4. **Mixing hypotheses and facts.** Label uncertainty.
5. **Letting notes override MCP.** Live rules and visible state always win.
6. **Forgetting to verify writes.** After setup or major edits, list files or read back the note.

## Verification Checklist

- [ ] Vault path was resolved to an absolute path.
- [ ] Civarium folder/index exists or was created.
- [ ] Current Strategy and Current Situation are present.
- [ ] Round/event/threat entries are concise and searchable.
- [ ] No secrets or raw hidden reasoning were written.
- [ ] Facts vs hypotheses are clearly separated.
- [ ] Important notes are linked with wikilinks.
