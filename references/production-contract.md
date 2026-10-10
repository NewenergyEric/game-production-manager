[中文](production-contract.zh.md)

# Intent-to-execution contract

`schema_version=0.1`. Original requests, valid decisions, plans, execution evidence and acceptance are different records.

| Layer | Fields and purpose |
|---|---|
| Project | id, version, goal, strategy, constraints, scope_in/out, assumptions |
| Requirements | id, text, source, status (confirmed/proposed), acceptance, owner_role |
| Deliverables | id, requirement_ids, name, type, spec, acceptance, reviewer_role |
| Assets | type=asset; spec includes category/family/base_or_variant/states/source_format/runtime_format/art_pack_ref |
| Tasks | id, deliverable_ids, depends_on, owner_role, executor_kind (human/agent/either), inputs, action, acceptance, status, artifacts, review |
| Milestones | id, goal, task_ids, exit_criteria; actual dates depend on real capacity |
| Feedback | id, source, target_ids, observation, proposed_change, status; publish a new version after a valid decision |

Inputs identify a real version or an explicit gap. Put external Art Director feature bindings in adapter records; do not invent unsupported fields in its source contract.

## State and handoff

Task states: planned / ready / in_progress / submitted / accepted / blocked / cancelled. Submitted needs artifact references; accepted additionally needs a passing review, reviewer, authority_reference and evidence. Structural validation cannot inspect inaccessible bytes or judge art quality.

An intended agent executor does not establish actual capability. Specify tools/access, budget, retry/stop conditions and escalation owner. Missing tools lead to a suitable human handoff or blocked task. Current helpers do not schedule agents or modify external task systems.

## Granularity and changes

A task has one accountable receiving role, a checkable output and explicit dependencies. Specialists can further decompose implementation; not every task needs an hourly estimate. Art scope covers states and combinations. Estimate base production, variants, reviews, integration and tests separately.

`impact` accepts a requirement, deliverable or task ID and lists directly/indirectly affected tasks. It proposes revision, not automatic rewriting. Changes state the goal, scope, capacity/date effect, acceptance and treatment of old tasks.

Generate role views from one package. Design owns gameplay, art direction owns visuals, technical leadership owns implementation feasibility, and project management maintains shared understanding and traceability.
