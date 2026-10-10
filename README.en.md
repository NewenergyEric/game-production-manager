[中文](README.md)

# Game Production Manager

### Turn the intent into work people can start.

**Clear direction. Owned work. Evidence of completion.**

Bring requirements, plans and feedback from the producer, design lead, art director and engineering lead. Your agent organizes shared understanding, deliverables, asset states, roles, dependencies and acceptance, then prepares work the team or another agent can take on.

<a href="assets/readme/hero-en.mp4"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-en.png?v=workflow-v3">
  <img src="assets/readme/hero-en.gif?v=workflow-v3" width="100%" alt="Turn requirements, decisions and feedback into work packages for people or agents.">
</picture></a>

[24 seconds through one complete workflow · Watch MP4](assets/readme/hero-en.mp4) · [Transcript](assets/readme/transcript-en.md)

## Install, then ask your agent

Install in an Agent Skills-compatible tool, such as Codex, Claude Code or Cursor:

```sh
npx skills add https://github.com/NewenergyEric/game-production-manager
```

Put the materials where your agent can read them, then describe the problem. Your agent handles file organization and commands.

### The requirements exist. Help the team start

> Use `$game-production-manager`. Read the existing design, art requirements and production constraints. Summarize our shared understanding and open decisions, then break this community order into scope, deliverables, role tasks and acceptance criteria. Preserve confirmed decisions.

**You get:** A SOW, deliverable and asset breakdown, role tasks, dependencies and the questions that need an owner.

### I want to hand a task to a teammate or agent

> Group this package by role. For each task, state the input version, action, output, dependencies, definition of done and conditions that require stopping to ask.

**You get:** A task agreement people or agents can use. Specialist executors perform the production work and submit the actual artifacts.

### A design rule changed. What else must change?

> The order rule changed. Trace its impact through existing deliverables and tasks. List what art, engineering and QA need to review. Prepare the change list, then issue a new version after confirmation.

**You get:** Affected tasks, inputs and acceptance criteria. Existing tasks retain their original version until the change is agreed.

## What the team receives

- **Scope and delivery:** SOW, requirement traceability, asset bases/variants/states and acceptance.
- **Role work:** owner, input, action, output, dependency and stop conditions.
- **Version and feedback:** impact analysis, real submissions, review decisions and handoff records.

## See how one community order is handed off

The [Merge/community format example](examples/merge-package.json) starts with “deliver an item to transform a corner.” Design defines order rules, art specifies the scene and UI, and the project manager organizes the handoff.

It contains three deliverables and three planned tasks. Changing `D-ORDER` traces to `T-RULE`, `T-ART` and `T-PACK`. This is an original draft; the real project still needs to confirm item chains, rewards, art pack and specifications.

[![See how one community order is handed off](assets/readme/workflow-en.png?v=workflow-v3)](assets/readme/workflow-en.png)

## Work with the other roles

[Market Intelligence](https://github.com/NewenergyEric/game-market-intelligence) supplies evidence and recommendations. The [Reverse Analyst](https://github.com/NewenergyEric/game-reverse-analyst) supplies structure and unknowns. [Art Director](https://github.com/NewenergyEric/art-director-skill) owns the visual rules. The project manager turns confirmed direction into assigned work.

<details>
<summary><strong>Requirements, technical docs and validation</strong></summary>

Python 3.10+; the core uses the standard library. Seven deterministic tests cover task coverage, dependency cycles, impact propagation, output protection and acceptance evidence.

[Human guide](docs/HUMAN-GUIDE.en.md) · [Agent guide](docs/AGENT-GUIDE.en.md) · [Skill entry](SKILL.md) · [Validation and review](evals/)

```sh
python scripts/production.py validate examples/merge-package.json
python scripts/production.py render examples/merge-package.json --out outputs/merge-sow
python scripts/production.py impact examples/merge-package.json --changed D-ORDER
```

[CI](https://github.com/NewenergyEric/game-production-manager/actions) · [Motion source](motion/README.md)

</details>

<details>
<summary><strong>Capability boundaries and material use</strong></summary>

This role organizes and tracks work. Assigned people or agents perform coding, art, audio, testing and builds, returning artifacts and evidence.

Generating a plan does not complete a task. Accepted work requires artifacts, evidence and an authorized review. External tickets, assignments and messages require explicit authorization.

</details>

[MIT License](LICENSE) · Made by Eric and Agents.
