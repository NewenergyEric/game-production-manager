# Human Guide · Game Production Manager

[中文](HUMAN-GUIDE.md)

## What this role solves

It turns the goals, plans, strategies, and feedback from game, art, production, and technical leads into a shared SOW, asset list, work packages, role tasks, milestones, and acceptance targets. It creates the execution contract; it does not automatically create the game, code, or art.

## 30-second start

1. Provide source requirements, confirmed decisions, constraints, existing research/analysis, and feedback.
2. Ask the agent to read `SKILL.md`, then run:

   ```text
   python scripts/production.py validate examples/merge-package.json
   python scripts/production.py render examples/merge-package.json --out outputs/merge-sow
   python scripts/production.py impact examples/merge-package.json --changed D-ORDER
   ```

3. Review goal, scope, and acceptance before handing packages to executors.
4. Add evidence and the review decision after submission. Scope changes create a new version; they do not silently modify old tasks.

## What you provide

Product goal, intended player experience, confirmed rules, resource and time constraints, deliverables, receivers, definition of done, and known feedback. Unknowns are allowed when assigned as explicit decisions.

## What you receive

SOW, requirement-to-deliverable-to-task traceability, asset/state/spec breakdown, role views, dependencies, milestones, acceptance, change impact, and receipt templates.

A plan is not production. Without a real artifact, test evidence, and acceptance authority, work cannot become `accepted`. Human and agent executors need their own tools, permissions, budget, stop conditions, and receipts.
