[中文](execution-depth.zh.md)

# Granularity that an executor can actually use

Choose a player-visible feature. Preserve confirmed rules and label new suggestions `proposed`; a design/code/art staffing list is only an overview.

## Task handoff

- **Why:** source requirement and decision version, scope in/out.
- **Start from:** files, versions, providing role, availability and prerequisite tasks. Discovery/contracts may proceed while production tasks remain planned/blocked for missing inputs.
- **Action:** module, configuration, component or asset family; states and errors to address.
- **Output:** file/object/interface names, format, specification, quantity basis and recipient. Logical state count is not automatically file count.
- **Acceptance:** observable Given/When/Then, boundary values, review environment, evidence and reviewer.
- **Stop:** conflict with approved scope, changed dependency, missing spec or access. Record the issue and impact instead of inventing a decision.

Split oversized work by independently deliverable/checkable outputs; combine mechanical steps that cannot be accepted separately. Use real staffing, throughput and history for dates. Twelve tasks do not mean twelve days.

## Three connected traces

1. `requirement → player state/rule → deliverable → task → acceptance case`.
2. `asset family → base/variant/state → art-pack version → engine spec → integration/composition review`.
3. `feedback/change → original decision → affected deliverable → downstream task/acceptance → new version`.

## Community-order example

Separate order rules, item config, submit transaction, UI binding, before/after scene assets, text/localization, QA, integration and handoff. Repeat submission, insufficient items, re-entry, failure feedback and long text need explicit expectations. Actual project owners decide server, save and idempotency strategy.

Run `validate / render / impact` on the [detailed package](../examples/community-order-detailed.en.json). It is an original planning case; every task is planned. Running its validators and exports does not develop or accept a game feature.

`detail_level: execution` requires `input_versions / outputs / entry_criteria / stop_conditions / acceptance_cases`. Pending inputs are valid in a plan, not a reason to mark downstream work ready or accepted. Complete the prerequisite work before advancing dependent tasks.
