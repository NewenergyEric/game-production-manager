# One community order, ready for task-by-task handoff

[中文](README.zh.md)

**Producer question:** “An item delivery transforms a corner. What does design, code, art and QA receive? What changes if the order requires two items?”

This original planning case was actually validated, exported and impact-traced. It is not a shipped feature: all 12 tasks remain planned; final values, art pack, engine and schedule are open.

| ID | Role | Concrete work | Dependencies |
|---|---|---|---|
| T-01 | Design lead | State and submission contract | — |
| T-02 | Systems designer | Item/reward config schema | T-01 |
| T-03 | Tech lead | Transaction and idempotency boundary | T-01 |
| T-04 | Art director | Asset families, reuse and missing specs | T-01 |
| T-05 | UI designer | Five UI states and interactions | T-01, T-04 |
| T-06 | Environment artist | Corner before/after and anchors | T-04 |
| T-07 | Gameplay engineer | Validation, deduction and reward logic | T-02, T-03 |
| T-08 | Client engineer | UI/data binding and resume behavior | T-05, T-07, T-09 |
| T-09 | Localization lead | Text keys, font coverage and length | T-01, T-05 |
| T-10 | QA engineer | Boundary, duplicate and recovery checks | T-07, T-08 |
| T-11 | Integration engineer | Corner/order integration and interruptions | T-06, T-08, T-10 |
| T-12 | Production manager | Versioned artifacts and review handoff | T-09, T-10, T-11 |

## An executed change-impact query

Changing `D-CONFIG` traces to `T-02 → T-07 → T-08 → T-10 → T-11 → T-12`. Environment-art task `T-06` is not automatically redone for a configuration change. New visual requirements need their own change record. No task or baseline was mutated.

## Acceptance and asset granularity

A duplicate submission settles once; insufficient inventory is not deducted; reload restores the saved state; interrupted feedback recovers consistently; long text and glyph coverage are checked per language. Five UI states belong to one component family, not automatically five texture files.

[完整执行包 / Full package](../../examples/community-order-detailed.json) · [任务 / Tasks](tasks.csv) · [验收 / Acceptance](acceptance.csv) · [资产 BOM](asset-bom.csv) · [变更影响 / Impact](impact.json)

```sh
python scripts/production.py validate examples/community-order-detailed.json
python scripts/production.py render examples/community-order-detailed.json --out outputs/community-order
python scripts/production.py impact examples/community-order-detailed.json --changed D-CONFIG
```
