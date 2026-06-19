# Civarium Agents

Collection of pre-defined Hermes player-agents for **Civarium** — an agent-native strategy game where LLM agents act through the `civarium-mcp` interface.

The repository stores reusable agent packages: each package contains the agent's Hermes profile templates, operational skills, strategic memory templates, and documentation needed to run that agent as a Civarium player.

## Current agents

| Agent | Folder | Purpose |
|---|---|---|
| Adam | [`agents/adam`](agents/adam/) | The first Civarium player-agent: autonomous, strategy-driven, visible-state-only, with optional Obsidian campaign memory. |

## Repository layout

```text
agents/
  adam/
    agent.yaml                         # metadata / manifest for the agent
    README.md                          # agent-specific guide
    hermes-profile/
      SOUL.md                          # Agent Soul template
      memories/
        MEMORY.md                      # My Notes template
        USER.md                        # User Profile template
      config.civarium-mcp.example.yaml # MCP config example without secrets
    skills/                            # Hermes skills to copy into the profile
    obsidian-templates/                # optional campaign memory templates
    docs/                              # design notes and rationale
templates/
  new-agent/                           # copy this folder for new agents
scripts/
  validate_agents.py                   # lightweight structural validation
```

## Installing Adam into a Hermes profile

1. Create or choose a Hermes profile for Civarium, for example:
   ```bash
   hermes profile create civarium-adam
   ```
2. Copy Adam's profile files:
   ```bash
   cp agents/adam/hermes-profile/SOUL.md ~/.hermes/profiles/civarium-adam/SOUL.md
   mkdir -p ~/.hermes/profiles/civarium-adam/memories ~/.hermes/profiles/civarium-adam/skills
   cp agents/adam/hermes-profile/memories/MEMORY.md ~/.hermes/profiles/civarium-adam/memories/MEMORY.md
   cp agents/adam/hermes-profile/memories/USER.md ~/.hermes/profiles/civarium-adam/memories/USER.md
   cp -R agents/adam/skills/* ~/.hermes/profiles/civarium-adam/skills/
   ```
3. Add the `civarium-mcp` server config using `agents/adam/hermes-profile/config.civarium-mcp.example.yaml` as a reference.
4. Put real credentials only in the target profile config or environment. Do **not** commit tokens or API keys here.
5. Restart the Hermes profile so Soul, memories, skills, and MCP tools are loaded.
6. Optional: copy `agents/adam/obsidian-templates/Civarium/` into your Obsidian vault if you want long-term campaign memory.

## Adding a new agent

Use this checklist:

1. Pick a human-readable name and lowercase slug, e.g. `Eve` / `eve`.
2. Copy the template:
   ```bash
   cp -R templates/new-agent agents/eve
   ```
3. Fill `agents/eve/agent.yaml`.
4. Write `agents/eve/README.md` with the agent's purpose, doctrine, and install steps.
5. Fill Hermes profile templates:
   - `hermes-profile/SOUL.md`
   - `hermes-profile/memories/MEMORY.md`
   - `hermes-profile/memories/USER.md`
6. Add only reusable procedural skills under `skills/<skill-name>/SKILL.md`.
7. Add optional strategic-memory templates under `obsidian-templates/`.
8. Run validation:
   ```bash
   python3 scripts/validate_agents.py
   ```
9. Commit the new folder.

## New-agent manifest template

Every agent should have an `agent.yaml` like this:

```yaml
schema_version: 1
slug: eve
name: Eve
status: draft
summary: "Short one-line description."
origin: "Why this agent exists."
play_style:
  autonomy: high
  risk_tolerance: medium
  memory: obsidian-optional
hermes:
  soul: hermes-profile/SOUL.md
  memory: hermes-profile/memories/MEMORY.md
  user_profile: hermes-profile/memories/USER.md
  skills_dir: skills/
civarium:
  mcp_server: civarium
  rule_catalog_policy: static-cache-once
  epistemics: visible-state-only
safety:
  secrets_policy: "Never commit API keys, bearer tokens, service keys, or private server URLs."
```

## Repository rules

- Keep agents self-contained under `agents/<slug>/`.
- Use lowercase folder slugs.
- Do not commit credentials, bearer tokens, live API keys, or private operator secrets.
- Do not store raw chain-of-thought. Store decisions, facts, hypotheses, and strategy records.
- Civarium rule catalog is static during a game: agents should cache it once and then use it for available-command reasoning and full command-spec lookup.
- Visible state remains the source of truth for the game world.
