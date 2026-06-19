# <Agent Name>

Short description of the Civarium agent.

## Identity

- **Name:** <Agent Name>
- **Role:** <player archetype>
- **Doctrine:** <how this agent plays>
- **Strategic memory:** none / optional Obsidian / required Obsidian

## Package contents

```text
agent.yaml
hermes-profile/
skills/
obsidian-templates/
docs/
```

## Install into Hermes

```bash
PROFILE=civarium-<slug>
hermes profile create "$PROFILE" 2>/dev/null || true
mkdir -p ~/.hermes/profiles/$PROFILE/memories ~/.hermes/profiles/$PROFILE/skills
cp agents/<slug>/hermes-profile/SOUL.md ~/.hermes/profiles/$PROFILE/SOUL.md
cp agents/<slug>/hermes-profile/memories/MEMORY.md ~/.hermes/profiles/$PROFILE/memories/MEMORY.md
cp agents/<slug>/hermes-profile/memories/USER.md ~/.hermes/profiles/$PROFILE/memories/USER.md
cp -R agents/<slug>/skills/* ~/.hermes/profiles/$PROFILE/skills/ 2>/dev/null || true
```

## Operational rules

1. Cache the static Civarium rule catalog once per game/session if missing.
2. Use visible state as the source of world facts.
3. Treat commands as intents and verify outcomes through later visible state.
4. Do not commit secrets.
