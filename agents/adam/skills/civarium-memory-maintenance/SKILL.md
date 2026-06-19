---
name: civarium-memory-maintenance
description: Use when maintaining compact persistent memory for a Civarium player profile without bloating MEMORY.md or USER.md.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [civarium, memory, profile, campaign-state, game-agent]
    related_skills: [civarium-player-loop, civarium-epistemic-discipline]
---

# Civarium Memory Maintenance

## Overview

Hermes profile memory is small and curated. For Civarium, use memory as a compact current campaign snapshot, not as a full turn log or rules manual.

The static runtime rule catalog, selected command specs, and MCP docs remain the source of rules. Memory should help the agent resume orientation quickly without replacing catalog/spec lookup.

## When to Use

Use this skill after meaningful Civarium observations or actions when persistent memory is available.

Use it to update:

- `MEMORY.md` / My Notes for campaign state and agent-side lessons;
- `USER.md` / User Profile for stable operator preferences.

Do not use memory for raw logs, secrets, full rule catalogs, or stale receipts.

## What Belongs In MEMORY.md

Store compact, current facts such as:

- last observed `round_idx` and `round_id`;
- visible structures;
- visible constructions and remaining rounds;
- current queued command id only if needed for exact retry;
- current strategic doctrine;
- active hypotheses clearly marked as hypotheses;
- MCP/tool quirks that are stable and useful.

Example:

```md
Civarium current snapshot:
- last observed round_idx: 7
- last observed round_id: ...
- visible structures: Workshop, Archive
- visible constructions: Signal Tower, 1 round remaining
- active queued intent: construction_start "Logistics Hub" (...)
- hypotheses: no observed enemy state; no combat/diplomacy mechanics exposed
```

## What Belongs In USER.md

Store stable operator preferences such as:

- operator wants autonomous Civarium play;
- operator prefers concise Russian reports;
- operator wants strict separation of facts and hypotheses;
- operator wants escalation only for config/MCP/API failures or external side effects.

## What Not To Store

Do not store:

- full raw MCP outputs;
- every past turn;
- API keys or bearer tokens;
- full rule catalog;
- hidden-state guesses as facts;
- stale command receipts after they are resolved;
- implementation details that are likely to change unless they are explicitly part of current strategy.

If a long history is useful, write a separate campaign log file in the workspace instead of memory.

## Update Pattern

After a meaningful turn:

1. Read current memory.
2. Replace the snapshot, do not append indefinitely.
3. Keep only durable or immediately resume-useful facts.
4. Remove stale queued intent after the next visible state confirms or invalidates it.
5. Keep hypotheses labeled and delete them when disproven or irrelevant.

## Common Pitfalls

1. **Using memory as a transcript.** Memory is too small; use a campaign log file for detailed history.
2. **Copying static docs into memory.** Docs and rules are retrievable via MCP; memory should stay compact.
3. **Saving secrets.** Never store `CIVARIUM_AGENT_API_KEY` in memory.
4. **Letting stale strategy override catalog/spec facts.** Memory can suggest a default, but cached catalog and command specs win.

## Verification Checklist

- [ ] Memory remains compact.
- [ ] No secrets are stored.
- [ ] Current snapshot replaces stale state.
- [ ] Hypotheses are labeled.
- [ ] User preferences are in USER.md, not mixed into game state.
- [ ] Rule details are referenced via cached catalog/spec lookup, not duplicated in full.
