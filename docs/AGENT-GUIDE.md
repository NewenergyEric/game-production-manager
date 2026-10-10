# Agent Guide · game-production-manager

[中文](AGENT-GUIDE.zh.md)

## Read order

Read `SKILL.md`, then `references/production-contract.md` and the user's source material. Use `scripts/production.py` for validation, rendering, and impact analysis. Do not treat natural-language input as approved JSON.

## Standard workflow

1. Extract goal, success criteria, constraints, scope, assumptions, and confirmed decisions.
2. Link requirements to features, deliverables/assets, work packages, tasks, milestones, and acceptance.
3. Give every task an owner, input, action, output, dependencies, stop conditions, and evidence requirement.
4. Run `validate` for coverage, duplicate IDs, dependency cycles, and acceptance evidence.
5. Run `render` for SOW, CSV, and role views; use `impact` for downstream feedback effects.
6. Hand off to executors and record submitted, accepted, or blocked only after real artifacts return.

## Failure branches

- Goal or acceptance missing: create an open decision and keep work blocked.
- Requirement has no deliverable/task: fail validation and restore traceability.
- Dependency cycle or unknown input version: preserve the block and request a sequence/baseline decision.
- Feedback changes scope: create a new version and impact report; do not overwrite old tasks.
- Agent asked to execute directly: return the execution contract, required permissions, budget, and stop conditions.

At minimum include `requirements`, `deliverables`, `tasks`, `milestones`, `acceptance`, `feedback`, and `handoff`. Every accepted item needs artifact evidence, review authority, and resolved dependencies. Never present a schedule or status field as completed production.

## Depth-case entry

[Protocol](../references/execution-depth.md) · [Case](../case-studies/community-order/README.md)

```sh
python scripts/production.py validate examples/community-order-detailed.json
python scripts/production.py render examples/community-order-detailed.json --out outputs/community-order
python scripts/production.py impact examples/community-order-detailed.json --changed D-CONFIG
```

## Tool JSON and execution gates

Human report sections are not CLI field names. Use examples/community-order-detailed.json as the tool input contract. Execution packages require exactly one version record per declared input, valid internal D-/T-/R-/M- references and explicitly registered external materials. Available inputs and accepted prerequisites are required for ready/in_progress/submitted. Document tasks review documents; implementation and QA verify runtime behavior.
