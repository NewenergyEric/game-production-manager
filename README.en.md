[中文](README.zh.md)

# Game Production Manager

### Turn the intent into work people can start.

Turn production intent into specific handoffs: owner, input version, actions, output files, dependencies and acceptance. Rules, systems design, code, art, localization, QA and integration share stable IDs.

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-en.png?v=depth-v4">
  <img src="assets/readme/hero-en.webp?v=depth-v4" width="100%" alt="Turn requirements, decisions and feedback into work packages for people or agents.">
</picture>

[Download the full 24-second introduction · MP4](assets/readme/hero-en.mp4?raw=true) · [GIF](assets/readme/hero-en.gif) · [Transcript](assets/readme/transcript-en.md)

## Install, then ask your agent

```sh
npx skills add https://github.com/NewenergyEric/game-production-manager
```

Install in an Agent Skills-compatible tool such as Codex, Claude Code or Cursor. Put your materials where the agent can read them, then describe the question.

### Break down a production brief

> Delivering an item restores a community corner. Break this down for engineering, art, systems design, copy and QA.

Receive 12 tasks and 12 deliverables with dependencies, versioned inputs and acceptance cases. Item chains, rewards, dimensions and schedules remain open when unspecified.

### Open a specific task

> Expand T-07: how do we test transactions, saves and repeat submission? What blocks execution?

D-CONFIG and D-TECH are inputs. Validate, consume, reward and save; repeated submissions take effect once. Pending inputs keep the task planned.

### Handle feedback and change

> The order configuration changed. What needs review? Must all scene art be redone?

The actual impact tool finds T-02, T-07, T-08, T-10, T-11 and T-12. T-06 scene art is unaffected under current dependencies; visual changes require explicit additional links.

## See a concrete case

**Original production plan: a community order restores a corner.** Validation, package export and change-impact tools were actually run. Includes 12 Given/When/Then acceptance cases and three asset-family BOM rows, with formal inputs still pending.

[Full analysis and downloadable records](case-studies/community-order/README.md)

[![Game Production Manager](case-studies/community-order/dashboard-en.png?v=depth-v4)](case-studies/community-order/dashboard-en.png)

## What the team receives

- Scope and delivery agreement — `SOW.md`
- 12 tasks with versioned inputs — `tasks.csv`
- Acceptance cases and assets — `acceptance.csv · asset-bom.csv`

<details>
<summary>Boundaries, guides and validation</summary>

This is a planning case, not a produced feature. All tasks remain planned. Task and logical-state counts are not exported file counts or schedules. Acceptance requires real artifacts, review evidence and an authorized reviewer.

Core helpers use Python 3.10+ and the standard library. Remotion is optional presentation tooling.

[Human guide](docs/HUMAN-GUIDE.md) · [Agent guide](docs/AGENT-GUIDE.md) · [SKILL.md](SKILL.md) · [Tests and review](evals/) · [Motion source](motion/README.md)

```sh
python -m unittest discover -s tests -v
python scripts/check_presentation.py
```

</details>

[MIT License](LICENSE) · Made by Eric and Agents.

## Four roles. One game worth making.

For a solo creator these are four hats; for a team they are connected responsibilities. Explore what is worth making, what competitors do, the resources it requires, and the original art that defines it.

[How the roles exchange evidence, scope and visual assets](docs/WORKFLOW.md) · [Art Director](https://github.com/NewenergyEric/art-director-skill)

![Market intelligence → competitor analysis → production assessment → original art direction; prototype and cost feedback revise earlier decisions.](assets/readme/workflow-en.png)
