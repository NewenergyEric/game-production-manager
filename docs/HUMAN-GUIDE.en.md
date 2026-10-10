# Game Production Manager · Human guide

[中文](HUMAN-GUIDE.md)

Turn requirements, decisions and feedback into work packages for people or agents.

## Bring your materials

Give your agent the original brief, existing decisions and constraints.
Incomplete material is fine to start; missing inputs that affect the next step stay visible.

## The requirements exist. Help the team start

> Use `$game-production-manager`. Read the existing design, art requirements and production constraints. Summarize our shared understanding and open decisions, then break this community order into scope, deliverables, role tasks and acceptance criteria. Preserve confirmed decisions.

A SOW, deliverable and asset breakdown, role tasks, dependencies and the questions that need an owner.

## I want to hand a task to a teammate or agent

> Group this package by role. For each task, state the input version, action, output, dependencies, definition of done and conditions that require stopping to ask.

A task agreement people or agents can use. Specialist executors perform the production work and submit the actual artifacts.

## A design rule changed. What else must change?

> The order rule changed. Trace its impact through existing deliverables and tasks. List what art, engineering and QA need to review. Prepare the change list, then issue a new version after confirmation.

Affected tasks, inputs and acceptance criteria. Existing tasks retain their original version until the change is agreed.

## How to review

This role organizes and tracks work. Assigned people or agents perform coding, art, audio, testing and builds, returning artifacts and evidence.

Generating a plan does not complete a task. Accepted work requires artifacts, evidence and an authorized review. External tickets, assignments and messages require explicit authorization.

## Outputs and handoff

- **Scope and delivery:** SOW, requirement traceability, asset bases/variants/states and acceptance.
- **Role work:** owner, input, action, output, dependency and stop conditions.
- **Version and feedback:** impact analysis, real submissions, review decisions and handoff records.

[Market Intelligence](https://github.com/NewenergyEric/game-market-intelligence) supplies evidence and recommendations. The [Reverse Analyst](https://github.com/NewenergyEric/game-reverse-analyst) supplies structure and unknowns. [Art Director](https://github.com/NewenergyEric/art-director-skill) owns the visual rules. The project manager turns confirmed direction into assigned work.

## Technical entry for your agent

Python 3.10+; the core uses the standard library. Seven deterministic tests cover task coverage, dependency cycles, impact propagation, output protection and acceptance evidence.

```sh
python scripts/production.py validate examples/merge-package.json
python scripts/production.py render examples/merge-package.json --out outputs/merge-sow
python scripts/production.py impact examples/merge-package.json --changed D-ORDER
```
