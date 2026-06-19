# Adam

Adam is the first packaged Civarium Hermes player-agent.

He is designed to act as an autonomous Civarium player rather than a generic assistant: he observes visible state, reasons from cached rule/spec facts, submits valid command intents, verifies queue intake, and maintains a long-term strategy when Obsidian is available.

## Identity

- **Name:** Adam
- **Role:** first Civarium player-agent
- **Doctrine:** autonomous play, visible-state-only epistemics, commands-as-intents, static rule catalog cached once
- **Strategic memory:** optional Obsidian campaign notes

## Package contents

```text
agent.yaml
hermes-profile/
  SOUL.md
  memories/MEMORY.md
  memories/USER.md
  config.civarium-mcp.example.yaml
skills/
  civarium-player-loop/
  civarium-current-strategy/
  civarium-epistemic-discipline/
  civarium-memory-maintenance/
  civarium-strategic-planning/
  civarium-obsidian-campaign-log/
obsidian-templates/Civarium/
docs/
```

## Install into Hermes

From the repository root:

```bash
PROFILE=civarium-adam
hermes profile create "$PROFILE" 2>/dev/null || true
mkdir -p ~/.hermes/profiles/$PROFILE/memories ~/.hermes/profiles/$PROFILE/skills
cp agents/adam/hermes-profile/SOUL.md ~/.hermes/profiles/$PROFILE/SOUL.md
cp agents/adam/hermes-profile/memories/MEMORY.md ~/.hermes/profiles/$PROFILE/memories/MEMORY.md
cp agents/adam/hermes-profile/memories/USER.md ~/.hermes/profiles/$PROFILE/memories/USER.md
cp -R agents/adam/skills/* ~/.hermes/profiles/$PROFILE/skills/
```

Then merge the MCP config from:

```text
agents/adam/hermes-profile/config.civarium-mcp.example.yaml
```

into the selected profile config and provide real Civarium credentials outside git.

## Optional Obsidian setup

Copy templates into the vault:

```bash
cp -R agents/adam/obsidian-templates/Civarium "$OBSIDIAN_VAULT_PATH/Civarium"
```

Then update Adam's `MEMORY.md` in the Hermes profile with the real absolute path to `Civarium/Index.md`.

## Operational rules

1. Cache the static Civarium rule catalog once per game/session if missing.
2. Use the cached command list when reasoning about available actions.
3. Fetch or consult a full command spec only for concrete command candidates.
4. Read active round and visible state every turn.
5. Treat command receipts and queued commands as intake status, not world changes.
6. Confirm world changes only through later visible state.
7. Maintain strategy/situation/event/threat notes when Obsidian is available.

## MCP interaction contract

Adam is intended to be the reference behavior for future Civarium agents:

1. Prefer MCP resources for static docs/rules when available; use context/doc/rule tools as fallback.
2. Cache the static rule catalog once per game/session.
3. Every decision window starts with `get_active_round` and `get_visible_state`.
4. The agent then chooses a posture: command, wait, skip, update strategy, or rebuild strategy.
5. A command may be submitted only after the command decision gate passes.
6. Valid receipts must be checked with `list_queued_submitted_commands`.
7. `wait_next_round` only waits; it does not advance the world by itself.
8. Outcomes are confirmed only by later `get_visible_state`.

## Design notes

See:

- [`docs/civarium-agent-parameters.md`](docs/civarium-agent-parameters.md)
- [`docs/civarium-obsidian-strategic-memory.md`](docs/civarium-obsidian-strategic-memory.md)
